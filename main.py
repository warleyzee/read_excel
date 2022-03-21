from read_email import Mail
from move_file import MoveFile
from read_save_pdf import Read_Save_PDF
from excel import File_Excel
import time

print()
print("Lendo o E-mail.")
email = Mail().read_mail()
time.sleep(2)
print("Fim da Leitura")


move = MoveFile().move_file()
print("Arquivo movidos")

save = Read_Save_PDF().save_pdf_txt()
create = Read_Save_PDF().create_list_pdf()

print()
print("Prencher tabela")
excel = File_Excel().save_file_exce()
input("Press Enter to finish...")