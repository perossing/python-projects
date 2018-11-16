import os, shutil, time
import sqlite3


def getLastBackupTime():
    with sqlite3.connect('file-backup-log.db') as connection:
        cur = connection.cursor()
        cur.execute("SELECT * FROM lastBackup WHERE recordNo = (SELECT MAX(recordNo) FROM lastBackup)")
        for row in cur.fetchall():
            lastBackup = row
    print(lastBackup)

getLastBackupTime()  
