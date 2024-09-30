# Convenções de Nomes

## Objetivo:

Este documento define as convenções de nomes que serão utilizadas para criar e gerenciar grupos AWS de forma automatizada, facilitando a concessão e revogação de permissões quando novos membros ingressarem ou deixarem os grupos. As convenções de nomes estabelecidas aqui são críticas para garantir uma automação consistente e simplificada do processo de gerenciamento de papéis (roles) e permission sets.

## Convenção de Nomes

A convenção de nomes seguirá dois formatos distintos, baseados no tipo de recurso AWS sendo gerenciado:

### 1. Grupos baseados em conta AWS

- **Formato:** `AWS_Account_{AccountID}__{PermissionSet}`

- **Descrição:**
  - `AWS_Account`: Prefixo padrão que identifica que o grupo está relacionado a uma conta AWS específica.
  - `{AccountID}`: ID da conta AWS à qual o grupo pertence (12 dígitos).
  - `{PermissionSet}`: Conjunto de permissões que será atribuído aos membros do grupo.

- **Exemplo:**
  ```bash
  AWS_Account_123456789012__Admin
  AWS_Account_987654321098__ReadOnly

### 2. Grupos baseados em Organizational Units (OUs)

- **Formato:** `AWS_OU_{OU}__{PermissionSet}`

- **Descrição:**
    - `AWS_OU`: Prefixo padrão que indica que o grupo está associado a uma Organizational Unit (OU).
    - `{OU}`: Nome ou ID da OU no AWS Organizations.
    - `{PermissionSet}`: Conjunto de permissões aplicável a todos os membros desta OU.

- **Exemplo:**
    ```bash
    AWS_OU_Development__PowerUser
    AWS_OU_Production__ReadOnly
    ````

- **Diretrizes Gerais**:
    - O separador `__` (dois underscores) deve ser sempre utilizado para separar o identificador (AccountID ou OU) do PermissionSet.
    - Todos os nomes devem ser em inglês e usar o formato PascalCase para o PermissionSet.
    - IDs de contas AWS devem ser representados exatamente como aparecem no console AWS (12 dígitos numéricos).
    - O nome das OUs deve ser descritivo e consistente com o que está definido no AWS Organizations.

- **Exemplos Adicionais:**
    - **Grupos Baseados em Contas**:
    ```bash
    AWS_Account_111122223333__Admin
    AWS_Account_444455556666__ReadOnly
    ```
    - **Grupos Baseados em OUs**:
    ```bash
    AWS_OU_Finance__Billing
    AWS_OU_Security__SecurityAudit
    ```

### 3. Automação e Gestão de Papéis
Com esta convenção de nomes, será possível automatizar a atribuição de roles e permission sets de forma eficiente. A automação poderá:

    - Adicionar novos membros automaticamente ao grupo apropriado com base em seu AccountID ou OU.
    - Remover membros quando eles deixarem de pertencer a um grupo específico.
    - Garantir que as permissões estejam sempre atualizadas com base nas mudanças organizacionais.

### Considerações Finais

Estas convenções de nomes foram projetadas para serem simples e eficazes. Elas facilitam o gerenciamento de permissões no AWS, especialmente quando integrado com scripts ou ferramentas de automação, como AWS IAM Identity Center ou outros sistemas de gestão de identidades e acessos.

## Documentação Relacionada:

- AWS IAM Identity Center
- AWS Organizations