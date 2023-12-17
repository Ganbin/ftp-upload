# file_check.py

import os
import time
from synchronize import run
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

def get_files_in_folder(folder):
    """
    Get a list of file names in the specified folder.
    """
    return [file for file in os.listdir(folder) if os.path.isfile(os.path.join(folder, file))]

def main():
    folder = os.getenv('LOCAL_FOLDER')
    sleep_interval = int(os.getenv('SLEEP_INTERVAL'))

    # Set an initial set of files in folder
    initial_files = set(get_files_in_folder(folder))

    while True:
        print(f"Check for new files in {folder}")
        # Get the current set of files in folder
        current_files = set(get_files_in_folder(folder))

        # Check for new files
        new_files = current_files - initial_files

        if new_files:
            print(f"New files detected: {new_files}")

            # Run the synchronization method from script1.py
            run()

            # Update the initial set of files
            initial_files = current_files

        # Sleep for a specified interval (e.g., 60 seconds)
        print(f"Sleeping for {sleep_interval} seconds ...")
        time.sleep(sleep_interval)

if __name__ == "__main__":
    main()
