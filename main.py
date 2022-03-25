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

time.sleep(2)
move = MoveFile().move_file()

print("Extract information PDF")
save = Read_Save_PDF().save_pdf_txt()
create = Read_Save_PDF().create_list_pdf()

print()
time.sleep(2)
print("Edinting Table")
excel = File_Excel().save_file_exce()

time.sleep(2)
move_xlsx = MoveFile().move_file_xlsx()

print("Save file PDF")
time.sleep(2)
rename = Name_PDF().name_pdf()


# input("Press Enter to finish...")