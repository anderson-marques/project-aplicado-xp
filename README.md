# project-aplicado-xp

# Sprint 1: Preparação e Configuração Inicial

## Objetivos:
- Definir as convenções de nomes para grupos e contas AWS.
- Estabelecer a lista de permissões e papéis (roles) baseada nas responsabilidades dos usuários.
- Configurar o ambiente de desenvolvimento com as ferramentas essenciais (AWS IAM Identity Center, EventBridge, etc.).

## Atividades:
1. **Definir e documentar a convenção de nomes**  
   - Criar um padrão claro para nomeação de grupos, contas e recursos na AWS.
   - Alinhar as convenções com as melhores práticas de segurança e organização.

2. **Criar a lista de permission sets e roles no AWS**  
   - Definir permission sets baseados nas responsabilidades de cada grupo de usuários.
   - Criar os papéis (roles) necessários e atribuí-los aos grupos adequados.

3. **Configuração inicial do ambiente AWS**  
   - Configurar o AWS IAM Identity Center para gerenciamento de identidades e acessos.
   - Implementar o EventBridge para orquestração de eventos.
   - Garantir que os principais serviços AWS estejam configurados corretamente para o ambiente de desenvolvimento.

## Evidências:
- **Documentação da convenção de nomes:**  
  Arquivo detalhando as convenções de nomes estabelecidas para os grupos e contas AWS, armazenado na pasta `docs/naming-conventions.md`.

- **Lista de roles e permissões criadas no AWS:**  
  Documento contendo a lista completa de permission sets e roles, incluindo suas descrições e responsabilidades, disponível em `docs/aws-permissions-and-roles.md`.

- **Ambiente AWS configurado:**  
  Logs e capturas de tela mostrando a configuração do AWS IAM Identity Center, EventBridge e outros serviços principais, armazenados na pasta `evidence/aws-setup/`.
  
## Links Relacionados:
- [Documentação do AWS IAM Identity Center](https://docs.aws.amazon.com/singlesignon/latest/userguide/what-is.html)
- [Documentação do EventBridge](https://docs.aws.amazon.com/eventbridge/latest/userguide/what-is-amazon-eventbridge.html)
