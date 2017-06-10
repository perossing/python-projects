# Python 3.6.1
# Peter Rossing, 06/09/2017
# Tech Academy Drill: Copy text files modified since last backup.
#                     Last backup date/time saved & recalled from database. User selects source & destination locations (#Item 66)


import os, shutil, time, datetime
import sqlite3
from tkinter import *
from tkinter import ttk, messagebox, filedialog, StringVar


def main():

    def getLastBackupTime(updateMessage):
        try:
            with sqlite3.connect('file-backup-log.db') as connection: 
                cur = connection.cursor()
                cur.execute("SELECT date, time, unix FROM lastBackup WHERE unix = (SELECT MAX(unix) FROM lastBackup)")
                for row in cur.fetchall():
                    return row
            cur.close()
            connection.close()
        except:
            pass

    
    def logBackupTime(updateMessage):
        with sqlite3.connect('file-backup-log.db') as connection:
            cur = connection.cursor()
            unixLogTime = time.time()
            logDate = (datetime.datetime.fromtimestamp(int(unixLogTime)).strftime('%m/%d/%Y'))
            logTime = (datetime.datetime.fromtimestamp(int(unixLogTime)).strftime('%H:%M:%S'))
            cur.execute("CREATE TABLE IF NOT EXISTS lastBackup(date TEXT, time TEXT, unix NUMERIC)")
            cur.execute("INSERT INTO lastBackup (date, time, unix) VALUES(?,?,?)",(logDate, logTime, unixLogTime))
            connection.commit()
        cur.close()
        connection.close()
        updateMessage.set('last backup:  ' + logDate + ' at ' + logTime)
            
            
    # ========== GUI =========
    class userInterface:

        def __init__(self, master):
            
            self.sourceChoice = ''
            self.destChoice = ''
            self.updateMessage = StringVar()
            lastBackup = (getLastBackupTime(self.updateMessage))
            
            # ===== main window settings =====
            master.maxsize(525,410)
            master.minsize(525,410)
            master.resizable(False, False)
            master.title('Recent File Backup')
            master.configure(background = '#2d2d52', padx=15, pady=15)
            self.master = master
            self.master.protocol('WM_DELETE_WINDOW', lambda: ask_quit(self))

            # ===== frames =====            
            self.topFrame = Frame(master, bg='#2d2d52')
            self.topFrame.pack(fill=X)
            self.bottomFrame = Frame(master, height=125, bg='#cfcffc', border=2, relief='ridge', padx=20, pady=10)
            self.bottomFrame.pack(fill=X)

            self.topFrame.grid_columnconfigure(0, weight=1) # makes grid within frames full width
            self.bottomFrame.grid_columnconfigure(0, weight=1)
            
            # label -- image
            self.image = PhotoImage(file = 'images/file-transfer-graphic.gif')
            Label(self.topFrame, image = self.image, borderwidth=0).grid(row=0, column =0, columnspan=2)          
            
            # label -- instruction
            ttk.Label(self.topFrame, text = 'Make copies of .txt files modified within 24 hours of your last backup:',
                      foreground = '#fff', background = '#2d2d52', font=('Arial', 13, 'bold'), wraplength=400, justify='center').grid(row=1, column=0, columnspan=2)

            # label -- last update
            if lastBackup == None:
                self.updateMessage.set('no backups found')
            else:
                self.updateMessage.set('last backup:  ' + lastBackup[0] + ' at ' + lastBackup[1])
                
            ttk.Label(self.topFrame, textvariable = self.updateMessage,
                  style = 'self.Label', foreground = '#ffd24d', background = '#2d2d52', font=('Arial', 12, 'bold')).grid(row=2, column=0, columnspan=2, pady=20)                         

           
            # label & button to select source folder
            ttk.Label(self.bottomFrame, text = 'Select the location of the files you would like to move:', foreground='#000', background='#cfcffc',
                  font=('Arial', 11)).grid(row=3, column = 0, pady=10, sticky=W)

            selectSourceBtn = Button(self.bottomFrame, text = 'select source', foreground='#fff', background='#2d2d52', height=1,
                                   font=('Arial', 9), command = lambda: browseSource(self))
            selectSourceBtn.grid(row=3, column=1)
            
            # label & button to select destination folder
            ttk.Label(self.bottomFrame, text = 'Select the location where you like to copy the files:', foreground='#000', background='#cfcffc',
                  font=('Arial', 11)).grid(row=4, column=0, pady=10, sticky=W)       

            selectDestBtn = Button(self.bottomFrame, text = 'select destination', foreground='#fff', background='#2d2d52', height=1,
                                   font=('Arial', 9), command = lambda: browseDest(self))
            selectDestBtn.grid(row=4, column=1) 

            # button to copy files           
            button = Button(self.bottomFrame, text = 'copy files', foreground='#fff', background='#3030e8', height=1, width=15,
                            font=('Arial', 11, 'bold'), command = lambda: copyFiles(self.sourceChoice, self.destChoice, self.updateMessage))
            button.grid(row=5, column=0, rowspan=1, columnspan=2, pady=10)
            
      
    def browseSource(self):
        self.sourceChoice = filedialog.askdirectory(parent=root, initialdir=os.getcwd(), title='Select a Source Folder') + '/'
        return self.sourceChoice

    def browseDest(self):
        self.destChoice = filedialog.askdirectory(parent=root, initialdir=os.getcwd(), title='Select a Destination Folder') + '/'
        return self.destChoice


    def copyFiles(sourceChoice, destChoice, updateMessage):

        if sourceChoice == '' or sourceChoice == '/':
            messagebox.showinfo('no action taken', 'No location chosen. Please choose a Source Folder')
            return

        if destChoice == '' or destChoice == '/':
            messagebox.showinfo('no action taken', 'No location chosen. Please choose a Destination Folder')
            return

        lastBackup = (getLastBackupTime(updateMessage))

        if lastBackup == None:
            backupTimestamp = time.time()         
        else:
            backupTimestamp = lastBackup[2]
            
        filesInSource = os.listdir(sourceChoice)
        filesCopied = 0
        for file in filesInSource:         
            sourceFile = sourceChoice+file
            copiedFile = destChoice+file         
            modifiedTime = os.path.getmtime(sourceFile)

            if backupTimestamp - modifiedTime < 86400 and file.endswith('.txt'): # subtract number of seconds in 24 hours
                shutil.copy(sourceFile,copiedFile)
                filesCopied +=1

        if filesCopied == 0:
            messagebox.showinfo('no action taken', 'No files to copy')
        else:
            msg = str(filesCopied) + ' files have been copied from ' + sourceChoice + ' to ' + destChoice
            messagebox.showinfo('action confirmed', msg)

        logBackupTime(updateMessage)
        
        

    def ask_quit(self):
        if messagebox.askokcancel('Exit program', 'Okay to exit application?'):
            self.master.destroy()
            os._exit(0)      

        
       
    root = Tk()
    gui = userInterface(root)    
    root.mainloop()


if __name__ == "__main__": main()
