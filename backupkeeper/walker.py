import os
from .backupmetadata import BackupMetadata

storage_file = ".backupkeepdate"


def walker(root_directory):
    """
       Load existing backups
    """
    existing_backups = []
    with os.scandir(root_directory) as it:
        for entry in it:
            if not entry.name.startswith('.') and entry.is_dir():
                created_date = entry.name
                storage_file_name = None

                if os.path.isfile(os.path.join(entry.path, storage_file)):
                    storage_file_name = os.path.join(entry.path, storage_file)
                if os.path.isfile(os.path.join(entry.path, '.backupdatum')):
                    storage_file_name = os.path.join(
                        entry.path, '.backupdatum')
                if storage_file_name:
                    with open(storage_file_name) as f:
                        keep_date = f.read()
                        existing_backups.append(
                            BackupMetadata(created_date, keep_date))
    return existing_backups
