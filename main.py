from read_email import Mail
from move_file import MoveFile
from read_save_pdf import Read_Save_PDF
from excel import File_Excel
from rename_file_pdf import Name_PDF
import time

print("Read the E-mail.")
print("Download Attachments")
email = Mail().read_mail()
time.sleep(2)
print("End Attachments")
input("Wait for action")

print("Move Files")
time.sleep(2)
move = MoveFile().move_file()
input("Wait for action")

print("Extract information PDF")
time.sleep(2)
save = Read_Save_PDF().save_pdf_txt()
create = Read_Save_PDF().create_list_pdf()
input("Wait for action")

print()
print("Edinting Table")
time.sleep(2)
test = File_Excel().save_file_excel()  
input("Wait for action")

time.sleep(2)
move_xlsx = MoveFile().move_file_xlsx()
input("Wait for action")

print("Save file PDF")
time.sleep(2)
rename = Name_PDF().name_pdf()
input("DEU CERTO?")
input("Fim da Escrita")


input("Press Enter to finish...")