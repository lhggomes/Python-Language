from ftplib import FTP
from datetime import datetime

start = datetime.now()
ftp = FTP('wevoftp.santaclara.com.br')
ftp.login()
ftp.cwd('trademarketing/')
files = ftp.nlst()

# Print out the files
for file in files:
    print("Downloading..." + file)
    ftp.retrbinary("RETR " + file, open("C:\\Users\\Lucas\\Downloads\\Download\\" + file, 'wb').write)

ftp.close()

