'''
    Enviando e-mail com python
    Material de apoio
    https://blog.chcdc.com.br/posts/enviar-emails-com-python/
    https://code.tutsplus.com/pt/tutorials/sending-emails-in-python-with-smtp--cms-29975
    https://www.pythonforbeginners.com/code-snippets-source-code/using-python-to-send-email
    http://rosettacode.org/wiki/Send_email#Python
'''
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib

# extrai a mensagem do arquivo 'layout.txt'
with open('layout.txt', 'r', encoding="utf8") as arquivo:
    message = arquivo.read()

# cria a instancia para a mensagem
msg = MIMEMultipart()
# seu e-mail e senha
my_email = ""
my_password = ""
from_email = my_email

# separar da seguinte forma ['','','']
# caso queira fazer um teste existem sites como o 10MinuteMail
to_email = ['g']
# titulo da mensagem
msg['Subject'] = "Enviada atrávez de um script"

msg.attach(MIMEText(message, 'plain'))
# conectando-se aos servidores do Gmail e protegendo login e senha
server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login(from_email, my_password)

# dispara o e-mail
texto = msg.as_string()
try:
    for send in to_email:
        server.sendmail(from_email, send, texto)
        print ("Enviado com sucesso para ", send)
except:
    print ("Erro ao enviar e-mail para ", send)
finally:
    server.quit()
