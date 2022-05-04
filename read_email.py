import imaplib
import email
 
class Mail():

    def read_mail(self,):
        #conect to server gmail with imap
        objConexao = imaplib.IMAP4_SSL("imap.gmail.com")

        #insert login and password e-mail
<<<<<<< HEAD
        login = "doc.glenbrier@gmail.com"
        password = "Dc*gb2022!"           
=======
        login = ""
        password = ""
>>>>>>> 8579118163b4049da91e385897bdc874d75ce3f2

        #login
        objConexao.login(login,password)

        #browse inbox
        objConexao.list()
        objConexao.select(mailbox='inbox',readonly=False)

        resposta,idDosEmails = objConexao.search(None, 'UNSEEN')

        #browse only email via id
        for nun in idDosEmails[0].split():
            #decoding the email and throwing the parts into a variable
            resultado,dados = objConexao.fetch(nun,'(RFC822)')
            texto_email = dados[0][1]
            texto_email = texto_email.decode('UTF-8')
            texto_email = email.message_from_string(texto_email)

            #scrolling through email parts.
            for part in texto_email.walk():
                #if you have attachment, get the name of the attachment
                if part.get_content_maintype() == 'multipart':
                    continue
                if part.get('Content-Disposition') is None:
                    continue
                #get the name file in attachment
                fileName = part.get_filename()
                #create a file the same name of attachment
                arquivo = open(r'C:\Users\Warley Souza\Music\read_excel\{}.pdf'.format(fileName), 'wb')
                #write the binary attachment in the file
                arquivo.write(part.get_payload(decode=True))
                arquivo.close()
            
# test = Mail().read_mail()     