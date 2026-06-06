import os
import shutil
import datetime
import schedule
import time

source_dir = r"C:\Users\BoKu\Desktop\UV Test"
destination_dir = r"C:\Users\BoKu\Desktop\Python\14_automated_file_backup\backup"

def copy_folder_to_directory(source, dest):
    today = datetime.date.today()
    dest_dir = os.path.join(dest, str(today))
    try:
        shutil.copytree(source, dest_dir)
        print(f"Folder copied to: {dest_dir}")
    except FileExistsError:
        print(f"Folder already exists in: {dir}")
    except Exception as e:
        print(f"Error: {e}")

schedule.every().day.at("16:33").do(lambda: copy_folder_to_directory(source_dir, destination_dir))

while True:
    schedule.run_pending()
    time.sleep(60)
    print("Checked")




































