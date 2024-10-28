# Sprint 3: Monitoramento, Ajustes e Manutenção na Automação de Permissões

## Objetivo

O objetivo desta sprint foi aprimorar a automação de concessão e revogação de permissões implementada nas sprints anteriores, garantindo a correta aplicação das permissões e a remoção segura de acessos para ex-funcionários. Também foram realizadas atividades de monitoramento e ajustes contínuos para otimizar a segurança e a precisão do sistema.

## Funcionalidades do Projeto

1. Monitoramento e Logs
Implementação de logs para rastreamento das atividades de automação, permitindo identificar falhas e pontos de melhoria na aplicação das permissões.

2. Automação de Offboarding
Automação do processo de desligamento (offboarding), removendo automaticamente permissões de ex-funcionários no AWS Identity Center e Google Workspace.

3. Ajustes Baseados em Resultados de Testes
Modificações na lógica de concessão e remoção de permissões, com ajustes específicos nas convenções de nome e no gerenciamento de grupo para maior precisão e segurança.

## Validação dos Objetivos da Sprint

Objetivo 1: Monitorar Logs e Identificar Falhas
O sistema foi ajustado para registrar logs detalhados das operações, facilitando a identificação de falhas e a aplicação de melhorias.

Objetivo 2: Implementar Automação de Desligamento
O script de desligamento foi implementado e testado, removendo acessos de forma automática e garantindo o cumprimento do princípio do menor privilégio.

Objetivo 3: Ajustar Processos de Automação
Com base nos testes, foram realizados ajustes nos scripts para adequar os processos de concessão e revogação, visando assegurar que as permissões sejam corretamente aplicadas.

## Considerações Finais

Esta sprint consolidou a automação de concessão e revogação de acessos, trazendo maior eficiência e segurança. A abordagem contínua de monitoramento e ajustes permite que o sistema se adapte dinamicamente a mudanças nos grupos e permissões, garantindo a correta gestão de acessos no ambiente AWS.

## Documentação Relacionada

- [Introdução o gerenciamento de acessos na AWS](https://docs.aws.amazon.com/pt_br/IAM/latest/UserGuide/introduction_access-management.html)
- [Melhores Práticas para Gerenciamento de Usuários na AWS](https://docs.aws.amazon.com/pt_br/IAM/latest/UserGuide/best-practices.html)