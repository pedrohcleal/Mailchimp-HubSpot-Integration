# Integração de Webhook para Cadastro de Contatos no HubSpot

Este repositório contém um script Python que permite a integração de um webhook para o cadastro de contatos no HubSpot. O webhook recebe eventos de um serviço externo, extrai dados como email e primeiro nome a partir dos eventos e, em seguida, tenta criar um contato no HubSpot com esses dados.

## Pré-requisitos

Antes de executar o script, é necessário configurar algumas variáveis de ambiente e instalar as dependências. Siga os passos abaixo:

### 1. Configurando as Variáveis de Ambiente

O script utiliza informações sensíveis, como o token de acesso e a chave de autorização, que devem ser armazenados de forma segura. Recomenda-se o uso de um arquivo `.env` para definir essas variáveis. Crie um arquivo `.env` no mesmo diretório que o script e defina as seguintes variáveis:

```
TOKEN=seu_token_de_acesso_do_HubSpot
AUTH=sua_chave_de_autorização_para_o_webhook
```

Substitua `seu_token_de_acesso_do_HubSpot` e `sua_chave_de_autorização_para_o_webhook` pelos valores apropriados.

### 2. Instalando as Dependências

Certifique-se de ter as dependências necessárias instaladas. Você pode instalá-las executando o seguinte comando:

```bash
pip install hubspot3 http.client2 json time dotenv
```

## Executando o Script

Agora que você configurou as variáveis de ambiente e instalou as dependências, pode executar o script. Use o seguinte comando:

```bash
python nome_do_script.py
```

Substitua `nome_do_script.py` pelo nome do arquivo que contém o código do script.

## Fluxo de Trabalho do Script

Este script Python realiza as seguintes etapas:

1. Estabelece uma conexão com o webhook externo.

2. Recebe eventos do webhook.

3. Extrai informações do evento, como o email e o primeiro nome.

4. Tenta criar um contato no HubSpot com o email e o primeiro nome extraídos.

5. Lida com exceções que podem ocorrer durante o processo de criação do contato.

6. Aguarda por um segundo antes de iniciar a próxima iteração.

## Vídeo Demonstrativo

https://drive.google.com/file/d/1pxe6gFcUmhWVALBl5WPmi3EkH5Z1M4XS/view?usp=share_link

## Tutorial para Configuração da Integração

Aqui estão os passos necessários para configurar a integração completa, desde a criação das contas nas respectivas plataformas até a execução do arquivo Python para realizar o cadastro de usuário no Mailchimp e atualizar a página de contato no HubSpot.

## 1. Configurando o Pipedream

### 1.1. Criar uma Conta no Pipedream

Se você ainda não possui uma conta no Pipedream, siga os passos abaixo:

- Acesse [Pipedream](https://pipedream.com).
- Clique em "Sign Up" para criar uma nova conta.
- Siga as instruções para configurar sua conta.

### 1.2. Criar uma Nova Source no Pipedream

Agora que você possui uma conta no Pipedream, siga estas etapas para criar uma nova source:

- Faça login na sua conta do Pipedream.
- No painel, clique em "Sources" no menu da esquerda.
- Clique em "New Source".
- Escolha "Webhook HTTP (payload only)".
- Copie a URL do endpoint gerada e salve-a em uma variável chamada `AUTH` no arquivo `.env`. Essa variável será usada no script Python.

## 2. Configurando o Mailchimp

### 2.1. Criar uma Conta no Mailchimp

Se você ainda não possui uma conta no Mailchimp, siga os passos abaixo:

- Acesse [Mailchimp](https://mailchimp.com).
- Clique em "Sign Up Free" para criar uma nova conta.
- Siga as instruções para configurar sua conta.

### 2.2. Configurar o Webhook no Mailchimp

Depois de criar uma conta no Mailchimp, siga estas etapas para configurar o webhook:

- Faça login na sua conta do Mailchimp.
- No painel, vá para "Audience" (Público-alvo).
- Selecione "All Contacts" (Todos os Contatos).
- Clique em "Settings" (Configurações).
- Em "Webhooks", clique em "Add a Webhook".
- Adicione a URL do endpoint criada pelo Pipedream (etapa 1.2) como o URL do webhook.
- Siga as instruções para salvar as configurações do webhook.

## 3. Configurando o HubSpot

### 3.1. Criar uma Conta no HubSpot

Se você ainda não possui uma conta no HubSpot, siga os passos abaixo:

- Acesse [HubSpot](https://www.hubspot.com).
- Clique em "Get Started Free" para criar uma nova conta.
- Siga as instruções para configurar sua conta.

### 3.2. Criar um Aplicativo Privado no HubSpot

Após criar uma conta no HubSpot, siga estas etapas para criar um aplicativo privado e obter um token de acesso:

- Faça login na sua conta do HubSpot.
- No painel, vá para "Config" (Configuração).
- Em "Integrations" (Integrações), selecione "Private Apps" (Aplicativos Privados).
- Clique em "Create a New App" (Criar um Novo Aplicativo).
- Siga as instruções para criar o aplicativo privado.
- Após a criação, você receberá um token de acesso. Salve esse token no arquivo `.env` como a variável `TOKEN`.

## 4. Executando o Arquivo Python

Agora que você configurou todas as integrações e salvou as variáveis de ambiente, você pode executar o arquivo Python fornecido no repositório. Certifique-se de que as bibliotecas necessárias estão instaladas (conforme descrito no README).

O arquivo Python realizará as seguintes ações:

- Receberá eventos do webhook criado no Pipedream.
- Extrairá informações do evento, como email e nome.
- Tentará criar um contato no Mailchimp.
- Atualizará a página de contato no HubSpot com o email e nome (que serão gerados automaticamente no HubSpot).

Com todas as etapas concluídas, você terá uma integração funcional entre o Pipedream, o Mailchimp e o HubSpot para o cadastro automático de contatos. 

## Contribuições

Se você deseja contribuir para este projeto, sinta-se à vontade para criar pull requests e relatar problemas.

## Licença

Este projeto é licenciado sob a [MIT License](LICENSE).
