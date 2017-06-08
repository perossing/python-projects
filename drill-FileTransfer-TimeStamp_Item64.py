# Python 2.7.13
# Peter Rossing, 06/07/2017
# Tech Academy Drill: Copy text files modified in last 24 hours (#Item 64)


import os, shutil, time
from Tkinter import *
import tkMessageBox


def main():

    class moveFileGUI:

        def __init__(self, master):

            self.master = master
            self.master.minsize(300,250) # height, width of main window
            self.master.maxsize(300,250)

            master.title('File Mover Drill')
            master.resizable(False, False)
            master.configure(background = '#d5ff80', pady=20)            

            self.image = PhotoImage(file = 'images/copy_files.gif')
            Label(master, image = self.image).pack()

            Label(master, text = "Click the button to move recently modified files",
                  background='#d5ff80', font=('Arial', 11), wraplength='220', pady=10).pack()

            button = Button(master, text = "move files")
            button.pack()
            button.config(foreground='#fff', background='#558000',
                          font=('Arial', 11, 'bold'), pady=10, command = moveFiles)


    def moveFiles():

        currentTime = time.time()
        
        sourcePath = 'C:/Users/peros/Desktop/Folder A/'
        destPath = 'C:/Users/peros/Desktop/Folder B/'
        filesInSource = os.listdir(sourcePath)
        filesCopied = 0

        for file in filesInSource:         
            sourceFile = sourcePath+file
            copiedFile = destPath+file         
            modifiedTime = os.path.getmtime(sourceFile)

            if currentTime - modifiedTime < 86400 and file.endswith('.txt'): # subtract number of seconds in 24 hours
                shutil.copy(sourceFile,copiedFile)
                filesCopied +=1

        if filesCopied == 0:
            tkMessageBox.showinfo('no action taken', 'No files to copy')
        else:
            msg = str(filesCopied) + ' files have been copied'
            tkMessageBox.showinfo('action confirmed', msg)

       
    root = Tk()   
    gui = moveFileGUI(root)
    root.mainloop() 


if __name__ == "__main__": main()
