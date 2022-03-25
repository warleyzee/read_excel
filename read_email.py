import imaplib
import email
 
class Mail():

    def read_mail(self,):
        #Conectando ao servidor do gmail com imap
        objConexao = imaplib.IMAP4_SSL("imap.gmail.com")

        #passando login e senha para entrar no email
        login = "doc.glenbrier@gmail.com"
        password = "Dc*gb2022!"

        #fazendo login
        objConexao.login(login,password)

        #Percorrer caixa de entrada
        objConexao.list()
        objConexao.select(mailbox='inbox',readonly=False)

        resposta,idDosEmails = objConexao.search(None, 'UNSEEN')

        #percorer cada email atraves do id
        for nun in idDosEmails[0].split():
            #decodificando o email e jogando em uma variavel as partes
            resultado,dados = objConexao.fetch(nun,'(RFC822)')
            texto_email = dados[0][1]
            texto_email = texto_email.decode('UTF-8')
            texto_email = email.message_from_string(texto_email)

            #percorrendo as partes do email.
            for part in texto_email.walk():
                #se tiver anexo, pegar o nome do anexo
                if part.get_content_maintype() == 'multipart':
                    continue
                if part.get('Content-Disposition') is None:
                    continue
                #pegando o nome do arquivo em anexo
                fileName = part.get_filename()
                #criando um arquivo com o mesmo nome do anexo
                arquivo = open(r'C:\Users\Warley Souza\Music\read_excel\{}.pdf'.format(fileName), 'wb')
                #escrevendo o binario do anexo no arquivo
                arquivo.write(part.get_payload(decode=True))
                arquivo.close()
            
# test = Mail().read_mail()     