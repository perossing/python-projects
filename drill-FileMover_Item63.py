# Python 2.7.13
# Peter Rossing, 06/02/2017
# Tech Academy Drill: File Mover (#Item 63)


import os, shutil
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
            master.configure(background = '#cce6ff', pady=20)            

            self.image = PhotoImage(file = 'images/copy_files.gif')
            Label(master, image = self.image).pack()

            Label(master, text = "Click the button to move files from Folder A to Folder B",
                  background='#cce6ff', font=('Arial', 11), wraplength='220', pady=10).pack()

            button = Button(master, text = "move files")
            button.pack()
            button.config(foreground='#fff', background='#1a8cff',
                          font=('Arial', 11, 'bold'), pady=10, command = moveFiles)


    def moveFiles():

        sourcePath = 'C:/Users/peros/Desktop/Folder A/'
        destPath = 'C:/Users/peros/Desktop/Folder B/'
        filesInSource = os.listdir(sourcePath)
        filesMoved = 0
  
        for file in filesInSource:         
            source = sourcePath+file
            dest = destPath+file           
            if file.endswith('.txt'):
                shutil.move(source,dest)
                filesMoved +=1
        
        if filesMoved == 0:
            tkMessageBox.showinfo('no action taken', 'No files to move')
        else:
            msg = str(filesMoved) + ' files have been moved'
            tkMessageBox.showinfo('action confirmed', msg)

            
    root = Tk()   
    gui = moveFileGUI(root)
    root.mainloop() 


if __name__ == "__main__": main()
