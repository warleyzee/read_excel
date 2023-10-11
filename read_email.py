import imaplib
import email
 
class Mail():

    def __init__(self, ):
        self.login = "doc.glenbrier@gmail.com"
        self.password = "ywwivewnpewuvfhq"

    def mark_email_as_read(self, objConexao, email_id):
        # Marca o email como lido
        objConexao.store(email_id, '+FLAGS', '(\Seen)')

    def read_mail(self):
        # Connect to Gmail server with IMAP
        objConexao = imaplib.IMAP4_SSL("imap.gmail.com")

        # Login
        
        objConexao.login(self.login, self.password)

        # Browse inbox
        objConexao.select(mailbox='inbox', readonly=False)

        resposta, idDosEmails = objConexao.search(None, 'UNSEEN')

        # Browse only emails via ID
        for num in idDosEmails[0].split():
            # Decoding the email and extracting the parts into a variable
            resultado, dados = objConexao.fetch(num, '(RFC822)')

            # Check if fetch was successful
            if resultado != 'OK':
                continue

            texto_email = dados[0][1]
            if texto_email is None:
                continue

            texto_email = texto_email.decode('UTF-8')
            texto_email = email.message_from_string(texto_email)

            # Scrolling through email parts.
            for part in texto_email.walk():
                # If it's a multipart email, skip it
                if part.get_content_maintype() == 'multipart':
                    continue
                # Check if Content-Disposition is None
                if part.get('Content-Disposition') is None:
                    continue
                # Get the filename from the attachment
                fileName = part.get_filename()
                if fileName is None:
                    continue
                # Create a file with the same name as the attachment
                arquivo = open(r'C:\Users\Warley Souza\Music\read_excel\{}'.format(fileName), 'wb')
                # Write the binary attachment to the file
                arquivo.write(part.get_payload(decode=True))
                arquivo.close()

            # Marca o email como lido após processá-lo
            self.mark_email_as_read(objConexao, num)     
                
# test = Mail().read_mail()     