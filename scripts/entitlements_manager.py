import yaml
import boto3
import os
import sys
from googleapiclient.discovery import build
from google.oauth2 import service_account

# Função para carregar o YAML
def load_yaml(file_path):
    with open(file_path, 'r') as file:
        return yaml.safe_load(file)

# Função para comparar arquivos YAML
def compare_yamls(new_file, old_file):
    new_data = load_yaml(new_file)
    old_data = load_yaml(old_file)
    
    # Convertendo em dicionários por grupo para facilitar a comparação
    new_groups = {f"{g['account_id']}__{g['permission_set']}": g['members'] for g in new_data}
    old_groups = {f"{g['account_id']}__{g['permission_set']}": g['members'] for g in old_data}
    
    changes = {
        'added': {},
        'removed': {}
    }
    
    for group, members in new_groups.items():
        if group not in old_groups:
            changes['added'][group] = members
        else:
            added_members = set(members) - set(old_groups[group])
            removed_members = set(old_groups[group]) - set(members)
            if added_members:
                changes['added'][group] = list(added_members)
            if removed_members:
                changes['removed'][group] = list(removed_members)
    
    for group in old_groups:
        if group not in new_groups:
            changes['removed'][group] = old_groups[group]
    
    return changes

# Função para provisionar Role Entitlement na AWS
def provision_role_entitlement(account_id, permission_set, member_email, action, aws_region):
    # Autenticando na AWS usando boto3
    session = boto3.Session(
        aws_access_key_id=os.getenv('AWS_ACCESS_KEY_ID'),
        aws_secret_access_key=os.getenv('AWS_SECRET_ACCESS_KEY'),
        region_name=aws_region
    )
    sso_admin = session.client('sso-admin')
    
    if action == 'add':
        print(f"Adicionando {member_email} ao permission set {permission_set} na conta {account_id}")
        # Código para adicionar permissão no boto3
    elif action == 'remove':
        print(f"Removendo {member_email} do permission set {permission_set} na conta {account_id}")
        # Código para remover permissão no boto3

# Função para atualizar a associação de grupos no Google Workspace
def update_google_group_membership(group_email, member_email, action):
    # Configuração da autenticação no Google
    credentials = service_account.Credentials.from_service_account_file(
        os.getenv('GOOGLE_CREDENTIALS_JSON'), scopes=['https://www.googleapis.com/auth/admin.directory.group']
    )
    service = build('admin', 'directory_v1', credentials=credentials)
    
    if action == 'add':
        try:
            service.members().insert(groupKey=group_email, body={
                'email': member_email,
                'role': 'MEMBER'
            }).execute()
            print(f"{member_email} adicionado ao grupo {group_email}")
        except Exception as e:
            print(f"Erro ao adicionar {member_email}: {e}")
    elif action == 'remove':
        try:
            service.members().delete(groupKey=group_email, memberKey=member_email).execute()
            print(f"{member_email} removido do grupo {group_email}")
        except Exception as e:
            print(f"Erro ao remover {member_email}: {e}")

# Função principal
def main():
    # Recebe os arquivos a serem comparados como argumentos
    if len(sys.argv) != 3:
        print("Uso: python entitlements_manager.py <arquivo_atual> <arquivo_antigo>")
        sys.exit(1)

    new_file = sys.argv[1]
    old_file = sys.argv[2]
    aws_region = os.getenv('AWS_REGION')

    # Comparar os arquivos YAML
    changes = compare_yamls(new_file, old_file)
    
    # Processa mudanças
    for group, members in changes['added'].items():
        account_id, permission_set = group.split('__')[:2]
        for member in members:
            provision_role_entitlement(account_id, permission_set, member, 'add', aws_region)
            update_google_group_membership(f"{account_id}__{permission_set}@yourdomain.com", member, 'add')
    
    for group, members in changes['removed'].items():
        account_id, permission_set = group.split('__')[:2]
        for member in members:
            provision_role_entitlement(account_id, permission_set, member, 'remove', aws_region)
            update_google_group_membership(f"{account_id}__{permission_set}@yourdomain.com", member, 'remove')

if __name__ == '__main__':
    main()
