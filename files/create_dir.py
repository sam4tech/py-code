
from datetime import datetime

import os


print("1. Print current system time. ")
print("2. Create a folder with name. ")
print("3. Create a file with name. ")
print("4. shutdown os. ")
ch = input("Enter your choice :")

if (ch == '1') :
    now = datetime.now()
    print("Current time =", now)
    dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
    print("date and time =", dt_string)

elif (ch == '2') :

    path = "C:\\Users\\cutes\\OneDrive\\Desktop\\Python\\samiii"

    if not os.path.exists(path) :
        # os.chdir(path)
        new_folder =input("Enter folder name : ")
        os.makedirs(new_folder)
        print("Folder created ")
    else :
        print("Folder already exists")

elif (ch == '3') :
    new_file = "file1.txt"
    file = open(new_file, "w")
    file.write("heyy sam")
    file.close()

elif (ch == '4') :
    
    shutdown = input("Do you wish to shutdown your computer ? (yes / no): ") 
    
    if shutdown == 'no': 
        exit() 
    else: 
        os.system("shutdown /s /t 1") 