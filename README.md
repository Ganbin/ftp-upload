# ftp-upload

This script is designed to monitor a specific folder and upload any new files to an FTP server at regular intervals.

It's particularly useful for mirroring new files from Chia DataLayer™ to a personal server.

To use this script, ensure you create a `.env` file with the necessary configurations.

```py
FTP_HOST="ftp.example.com"
FTP_USER="ftpuser"
FTP_PASS="ftppassword"
LOCAL_FOLDER="/path/to/.chia/mainnet/data_layer/db/server_files_location_mainnet/"
REMOTE_FOLDER="/path/to/mirror/"
SLEEP_INTERVAL=600
```

## Usage

```sh
python3 file_check.py
```

## Chia DataLayer™

[Chia DataLayer - True Data Integrity On a Blockchain](https://www.chia.net/datalayer/)
[DataLayer User Guide](https://docs.chia.net/guides/datalayer-user-guide/)
[Chia DataLayer™️ Explainer | Chia Network](https://www.youtube.com/watch?v=gjx67gCnGdA)
