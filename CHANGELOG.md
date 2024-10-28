# Changelog

## [2023-10-27]

- Bugfix: Corrigido erro no parâmetro --domain para extrair automaticamente o domínio do username caso não seja fornecido.
- Ajuste: Refatorada a função revoke_aws_temp_credentials para evitar duplicação de SCPs ao criar novas políticas de revogação.

## [2023-10-26]

- Melhoria: Adicionada validação para verificar se o username é um email válido antes de tentar remover do Google Workspace.
- Novo: Implementada condição DateLessThan para revogar acessos temporários com base no tempo em ambos os scripts.

## [2023-10-25]

- Ajuste: Modificada a função de remoção de Role Entitlement para utilizar PrincipalId em vez de username, visando maior precisão.
- Bugfix: Corrigida a falha onde o target_id da SCP não era carregado corretamente de os.getenv.

## [2023-10-24]

- Novo: Adicionada função de logging para registrar ações e erros durante a execução dos scripts.
- Ajuste: Ajuste no carregamento do arquivo JSON de credenciais do Google para tratar exceções.

## [2023-10-22]

- Melhoria: Implementada configuração para especificar a aws:SourceIdentity na criação da SCP, melhorando o rastreamento de eventos.

## [2023-10-21]

- Bugfix: Corrigido erro de sintaxe ao definir condição de negação em create_scp_revoke_user.
- Ajuste: Atualizado PermissionSetArn para ser carregado de variáveis de ambiente, melhorando a flexibilidade.

## [2023-10-20]

- Novo: Adicionada lógica para remover automaticamente o usuário de todos os grupos no Google Workspace caso o grupo específico não seja identificado.
- Melhoria: Simplificado o código do entitlement_manager.py para melhor performance em operações de comparação YAML.