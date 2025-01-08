import os
import smtplib
from email.message import EmailMessage
import requests
import bs4

# Função para coletar as notícias do Vasco
def coletar_noticias():
    url = 'https://ge.globo.com/futebol/times/vasco/'

    requisicao = requests.get(url)  # Abrir uma requisição
    requisicao.raise_for_status()  # Verifica se houve algum erro na requisição

    pagina = bs4.BeautifulSoup(requisicao.text, 'html.parser')

    
    lista_noticias = pagina.find_all('a', class_='feed-post-link')

    noticias = []
    # Para cada noticia, coletamos o título e o link
    for noticia in lista_noticias:
        noticia_texto = noticia.text.strip()
        noticia_link = noticia.get('href')
        noticias.append(f"{noticia_texto}\nLink: {noticia_link}\n")
    
    return noticias

# Função para enviar o e-mail com as notícias
def enviar_email(noticias):
    
    email = 'rafaeljadjada0@gmail.com'
    with open('senha.txt') as f:
        senha = f.readlines()

    senha_do_email = senha[0].strip()  

    # Preparar o e-mail
    msg = EmailMessage()
    msg['Subject'] = 'Noticias do Vascão - Boa sorte guerreiro!'
    msg['From'] = email
    msg['To'] = email  
    msg.set_content("\n".join(noticias))  

    # Enviar o e-mail
    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
        smtp.login(email, senha_do_email)
        smtp.send_message(msg)

# Coletar as notícias
noticias = coletar_noticias()

# Verifica se há notícias e envia o e-mail
if noticias:
    enviar_email(noticias)
    print('Você recebeu noticias do Vascão!')
else:
    print("Nenhuma notícia encontrada.")
