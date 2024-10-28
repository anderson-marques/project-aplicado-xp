import boto3
import os
import sys
import json
from googleapiclient.discovery import build
from google.oauth2 import service_account
from datetime import datetime

# Função para remover o usuário do Google Workspace
def remove_google_workspace_membership(username):
    credentials = service_account.Credentials.from_service_account_file(
        os.getenv('GOOGLE_CREDENTIALS_JSON'), scopes=['https://www.googleapis.com/auth/admin.directory.group']
    )
    service = build('admin', 'directory_v1', credentials=credentials)
    domain = os.getenv('DOMAIN') or username.split('@')[1]
    group_key = f"{username}@{domain}"

    try:
        service.members().delete(groupKey=group_key, memberKey=username).execute()
        print(f"{username} removido do Google Workspace")
    except Exception as e:
        print(f"Erro ao remover {username} do Google Workspace: {e}")

# Função para criar e anexar uma SCP no AWS Organizations
def create_scp_revoke_user(username, aws_region):
    org_client = boto3.client('organizations', region_name=aws_region)
    policy_name = f"RevokeAccess_{username}"
    timestamp = datetime.utcnow().isoformat() + "Z"  # Tempo UTC para revogação baseada em tempo

    # Definir SCP para negar ações com base em userid e sourceIdentity e uma condição de revogação baseada em tempo
    scp_policy = {
        "Version": "2012-10-17",
        "Statement": [
            {
                "Effect": "Deny",
                "Action": "*",
                "Resource": "*",
                "Condition": {
                    "StringEquals": {
                        "aws:userid": [f"*: {username}"],
                        "aws:SourceIdentity": username
                    },
                    "DateLessThan": {
                        "aws:TokenIssueTime": timestamp
                    }
                }
            }
        ]
    }

    try:
        # Cria a SCP
        create_policy_response = org_client.create_policy(
            Content=json.dumps(scp_policy),
            Description=f"Revoke access for {username}",
            Name=policy_name,
            Type="SERVICE_CONTROL_POLICY"
        )
        policy_id = create_policy_response['Policy']['PolicySummary']['Id']
        print(f"SCP criada com sucesso: {policy_name}")

        # Anexa a SCP ao destino especificado
        target_id = os.getenv('TARGET_ID')
        org_client.attach_policy(
            PolicyId=policy_id,
            TargetId=target_id
        )
        print(f"SCP {policy_name} anexada com sucesso ao destino {target_id}")

    except Exception as e:
        print(f"Erro ao criar ou anexar a SCP para {username}: {e}")

# Função para remover Role Entitlements no AWS Identity Center
def remove_identity_center_entitlement(username, aws_region):
    sso_client = boto3.client('sso-admin', region_name=aws_region)
    identity_store_id = os.getenv('IDENTITY_STORE_ID')
    permission_set_arn = os.getenv('PERMISSION_SET_ARN')
    account_id = os.getenv('ACCOUNT_ID')

    try:
        # Remove entitlements para o usuário especificado
        response = sso_client.delete_account_assignment(
            InstanceArn=f"arn:aws:sso:::instance/{identity_store_id}",
            TargetId=account_id,
            PermissionSetArn=permission_set_arn,
            PrincipalType="USER",
            PrincipalId=username
        )
        print(f"Role entitlement removido para {username} no AWS Identity Center")
    except Exception as e:
        print(f"Erro ao remover Role Entitlement para {username}: {e}")

# Função principal
def main():
    if len(sys.argv) < 2:
        print("Uso: python revoke_access.py <username> [aws_region]")
        sys.exit(1)

    username = sys.argv[1]
    aws_region = sys.argv[2] if len(sys.argv) > 2 else os.getenv('AWS_REGION', 'us-east-1')

    # Remover o usuário do Google Workspace
    remove_google_workspace_membership(username)
    
    # Criar e anexar uma SCP para revogar acessos no AWS Organizations
    create_scp_revoke_user(username, aws_region)
    
    # Remover Role Entitlement no AWS Identity Center
    remove_identity_center_entitlement(username, aws_region)

if __name__ == '__main__':
    main()
