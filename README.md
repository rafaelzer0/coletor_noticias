# Coletor de Notícias do Vasco e Envio por E-mail
Este repositório contém um script Python que coleta as últimas notícias do time de futebol Vasco da Gama no site Globo Esporte e envia essas notícias por e-mail.

## Como Funciona
O script realiza as seguintes etapas:

Coleta de Notícias: O script acessa o site Globo Esporte para o time Vasco da Gama e coleta os títulos das últimas notícias, juntamente com os links.
Envio de E-mail: Após coletar as notícias, ele envia um e-mail com os detalhes das notícias para o seu próprio e-mail (ou para o destinatário configurado no código).
## Requisitos
Python 3.x
Bibliotecas Python:
requests
bs4 (BeautifulSoup)
smtplib
email

Para instalar as dependências, execute o seguinte comando:
pip install requests beautifulsoup4

## O que o Script Faz
Coleta as Notícias: Usa o requests e BeautifulSoup para fazer uma requisição ao site Globo Esporte e buscar as últimas notícias relacionadas ao Vasco da Gama.
Envio por E-mail: Usa o módulo smtplib para enviar um e-mail para você com os links e títulos das notícias.
Verificação: Antes de enviar o e-mail, o script verifica se há notícias coletadas. Caso não haja, ele imprime uma mensagem dizendo que nenhuma notícia foi encontrada.

## Segurança
Senha do E-mail: O script requer que você forneça a senha do seu e-mail para autenticação. Se você estiver usando a autenticação de dois fatores (2FA) no Gmail, será necessário gerar uma senha de app através da sua conta Google.
Backup de E-mails: Este script envia um e-mail para o mesmo endereço de e-mail usado para autenticação. Certifique-se de que o e-mail está correto no código e que você tenha acesso ao mesmo.

