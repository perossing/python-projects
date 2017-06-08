# Python 3.6.1
# Peter Rossing, 06/08/2017
# Tech Academy Drill: Copy text files modified in last 24 hours. User selects source & destination locations (#Item 65)


import os, shutil, time
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from tkinter import filedialog


def main():

    class moveFileGUI:

        def __init__(self, master):

            self.sourceChoice = ''
            self.destChoice = ''
            
            # ===== main window settings =====
            self.master = master
            self.master.maxsize(500,340)
            self.master.minsize(500,340)
            master.resizable(False, False)

            master.title('Recent File Backup')
            master.configure(background = '#2d2d52', padx=20, pady=20)            

            self.image = PhotoImage(file = 'images/file-transfer-graphic.gif')
            Label(master, image = self.image, borderwidth=0).grid(row = 0, column = 0, columnspan = 2)

            # ===== label styling =====
            self.style = ttk.Style()
            self.style.configure('Label', foreground = '#fff', background = '#2d2d52', font = ('Arial', 11))
            
            
            # ===== labels for instructions & buttons for actions ===== 
            ttk.Label(master, text = 'Make copies of .txt files modified within the last 24 hours:',
                      style = 'self.Label', font=('Arial', 12, 'bold')).grid(row = 1, column = 0, columnspan = 2, pady=15)

            # label & button to select source folder
            ttk.Label(master, text = 'Select the location of the files you would like to move:',
                  style = 'self.Label').grid(row = 2, column = 0, pady=10, sticky=W)

            selectSourceBtn = Button(master, text = 'select source', foreground='#000', background='#9b9bf6', height=1,
                                   font=('Arial', 9), command = lambda: browseSource(self))
            selectSourceBtn.grid(row = 2, column = 1)
            
            # label & button to select destination folder
            ttk.Label(master, text = 'Select the location where you like to copy the files:',
                  style = 'self.Label').grid(row = 3, column = 0, pady=10, sticky=W)       

            selectDestBtn = Button(master, text = 'select destination', foreground='#000', background='#9b9bf6', height=1,
                                   font=('Arial', 9), command = lambda: browseDest(self))
            selectDestBtn.grid(row = 3, column = 1) 

            # button to copy files           
            button = Button(master, text = 'copy files', foreground='#fff', background='#3030e8', height=1, width=12,
                            font=('Arial', 11, 'bold'), command = lambda: copyFiles(self.sourceChoice, self.destChoice))
            button.grid(row = 4, column = 0, rowspan= 1, columnspan = 2, pady=15)
            
      
    def browseSource(self):
        self.sourceChoice = filedialog.askdirectory(parent=root, initialdir=os.getcwd(), title='Select a Source Folder') + '/'
        return self.sourceChoice

    def browseDest(self):
        self.destChoice = filedialog.askdirectory(parent=root, initialdir=os.getcwd(), title='Select a Destination Folder') + '/'
        return self.destChoice


    def copyFiles(sourceChoice, destChoice):

        if sourceChoice == '' or sourceChoice == '/':
            messagebox.showinfo('no action taken', 'No location chosen. Please choose a Source Folder')
            return

        if destChoice == '' or destChoice == '/':
            messagebox.showinfo('no action taken', 'No location chosen. Please choose a Destination Folder')
            return       

        currentTime = time.time()
        filesInSource = os.listdir(sourceChoice)
        filesCopied = 0

        for file in filesInSource:         
            sourceFile = sourceChoice+file
            copiedFile = destChoice+file         
            modifiedTime = os.path.getmtime(sourceFile)

            if currentTime - modifiedTime < 86400 and file.endswith('.txt'): # subtract number of seconds in 24 hours
                shutil.copy(sourceFile,copiedFile)
                filesCopied +=1

        if filesCopied == 0:
            messagebox.showinfo('no action taken', 'No files to copy')
        else:
            msg = str(filesCopied) + ' files have been copied from ' + sourceChoice + ' to ' + destChoice
            messagebox.showinfo('action confirmed', msg)
            
       
    root = Tk()   
    gui = moveFileGUI(root)    
    root.mainloop()


if __name__ == "__main__": main()
