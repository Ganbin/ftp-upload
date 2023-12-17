from ftplib import FTP
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

def get_remote_file_names(ftp, remote_folder):
    """
    Get a set of file names for all files in the remote folder.
    """
    remote_file_names = set()
    ftp.cwd(remote_folder)
    ftp.retrlines('NLST', remote_file_names.add)
    return remote_file_names

def upload_file_ftp(ftp, local_file_path, remote_folder):
    # Open the local file in binary mode
    with open(local_file_path, 'rb') as local_file:
        # Change to the remote folder
        ftp.cwd(remote_folder)

        # Upload the file to the FTP server
        ftp.storbinary('STOR {}'.format(os.path.basename(local_file_path)), local_file)

def synchronize_folders(local_folder, remote_folder, ftp_host, ftp_user, ftp_passwd):
    # Connect to FTP server
    ftp = FTP()
    ftp.connect(ftp_host)
    ftp.login(user=ftp_user, passwd=ftp_passwd)

    # Get the set of file names in local and remote folders
    local_file_names = set(file_name for file_name in os.listdir(local_folder) if file_name != '.DS_Store')
    remote_file_names = get_remote_file_names(ftp, remote_folder)
    print(f"Local files length: {len(local_file_names)}")
    print(f"Remote files length: {len(remote_file_names)}")

    # Find new or modified files in local folder
    new_or_modified_files = local_file_names - remote_file_names
    print(f"New files length: {len(new_or_modified_files)}")

    # Upload new or modified files to remote folder
    for file_name in new_or_modified_files:
        local_file_path = os.path.join(local_folder, file_name)
        upload_file_ftp(ftp, local_file_path, remote_folder)
        print(f"Uploaded {file_name} to FTP")

    # Close the FTP connection
    ftp.quit()

def run():
    # Set your FTP credentials and paths
    ftp_host = os.getenv('FTP_HOST')
    ftp_user = os.getenv('FTP_USER')
    ftp_passwd = os.getenv('FTP_PASS')
    local_folder = os.getenv('LOCAL_FOLDER')
    remote_folder = os.getenv('REMOTE_FOLDER')
    
    print(f"Synchronize: {local_folder} with {ftp_host}/{remote_folder}")

    # Synchronize folders
    synchronize_folders(local_folder, remote_folder, ftp_host, ftp_user, ftp_passwd)

if __name__ == "__main__":
    run()