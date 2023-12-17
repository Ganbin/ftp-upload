# ftp-upload

A simple script to upload files to ftp server

I use it to push new file from Chia DataLayer™ into my own mirror.

Make sur to create a file named `.env` with the following content:

```
FTP_HOST=ftp.example.com
FTP_USER=ftpuser
FTP_PASS=ftppassword
LOCAL_FOLDER="/path/to/.chia/mainnet/data_layer/db/server_files_location_mainnet/"
REMOTE_FOLDER="/path/to/mirror/"
```
