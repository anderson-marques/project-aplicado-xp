# Automação de Concessão de Permissões com Base em Eventos no IdP

## Objetivo

Nesta sprint, o objetivo é implementar uma automação para a concessão de permissões no AWS, utilizando eventos para monitorar alterações em grupos definidos no IdP (Identity Provider) Google Workspace. A automação permite que as permissões sejam atribuídas e removidas de forma mais dinâmica e confiável, conforme os grupos e papéis são atualizados, com base em uma convenção de nomes.

## Funcionalidades do Projeto

### 1. Monitoramento de Eventos de Grupos

A automação está configurada para monitorar eventos de criação e exclusão de grupos, a partir de atualizações em um arquivo YAML que lista as permissões de cada grupo. As alterações são detectadas por meio de GitHub Actions, que aciona o script Python para atualizar os papéis e permissões no AWS e Google Workspace.

### 2. Provisionamento Automático

A configuração dos grupos e seus respectivos papéis segue uma convenção de nomes definida, `AWS_ACCOUNT__{ACCOUNTID}__{PermissionSetNAME}`, permitindo que o script Python utilize esses dados para provisionar automaticamente as permissões associadas.

### 3. Scripts de Automação

O script de automação realiza as seguintes ações:
   - **Comparação de Arquivos YAML**: Identifica alterações entre a versão atual e a versão anterior do arquivo YAML de grupos, localizado na pasta `/historico`.
   - **Concessão e Remoção de Permissões no AWS**: Utilizando a biblioteca `boto3`, o script atualiza as permissões no AWS com base nos grupos monitorados.
   - **Gerenciamento de Grupos no Google Workspace**: Utilizando a API Directory, o script cria, remove e atualiza membros dos grupos no Google Workspace, conforme necessário.

## Validação dos Objetivos da Sprint

### Objetivo 1: Implementar a Automação de Concessão de Permissões com Base em Eventos no IdP
O script está configurado para monitorar atualizações no arquivo de definição de grupos e disparar um workflow no GitHub Actions para processar as mudanças. Quando os arquivos são alterados, o script analisa as diferenças e realiza a concessão ou remoção de permissões no AWS e no Google Workspace. 

### Objetivo 2: Desenvolver Scripts de Automação para Monitorar Eventos como Criação e Exclusão de Grupos
A automação compara as versões dos arquivos YAML para detectar adições e remoções de grupos. Com isso, o script identifica se novos grupos foram criados, atualiza os membros dos grupos existentes e exclui os que foram removidos, tudo de forma automática.

### Objetivo 3: Implementar o Provisionamento Automático de Permissões com Base nas Convenções de Nomes
O script usa a convenção de nomes `AWS_ACCOUNT__{ACCOUNTID}__{PermissionSetNAME}` para mapear os grupos e associá-los ao permission set correto no AWS. Dessa forma, o provisionamento ocorre de maneira automática, sem necessidade de intervenção manual, seguindo os padrões de nomenclatura predefinidos.

### Considerações Finais

A automação projetada nesta sprint visa proporcionar maior controle e segurança na gestão de acessos no AWS. Ela permite que as permissões sejam atribuídas de acordo com as mudanças nos grupos do IdP, garantindo que os usuários recebam acesso conforme necessário e que o princípio do menor privilégio seja aplicado de forma contínua. Além disso, a abordagem baseada em eventos simplifica o gerenciamento de grupos, oferecendo uma solução integrada para a concessão de permissões e papéis no ambiente AWS.

### Documentação Relacionada

- [Automatizando Gerenciamento de Acesso no AWS IAM](https://docs.aws.amazon.com/pt_br/IAM/latest/UserGuide/introduction_access-management.html)
- [Práticas Recomendadas para Automação no AWS](https://docs.aws.amazon.com/pt_br/IAM/latest/UserGuide/best-practices.html)
