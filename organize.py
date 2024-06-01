import os #this let you interact with the operating system
import shutil # this is for high level oerations for file manipulation
import sys
 

    
folder_path = 'C:\\Users\\Oluwa\\Downloads' # it will use my downloads location to organize
files = os.listdir(folder_path) # this will get the files and place them in a folder 

for file in files:
    filename,extension = os.path.splitext(file) 
    extension = extension[1:]
    
    if os.path.exists(folder_path+'/'+extension): #finds the file and places it in a folder based on what type of doc it is
        shutil.move(folder_path+'/'+file,folder_path+'/'+extension+'/'+file)
    else:
        os.mkdir(folder_path+'/'+extension)
        shutil.move(folder_path+'/'+ file, folder_path+'/'+extension+'/'+file)

print(sys.executable)