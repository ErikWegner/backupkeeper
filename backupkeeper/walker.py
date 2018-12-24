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
                if os.path.isfile(os.path.join(entry.path, storage_file)) or os.path.isfile(os.path.join(entry.path, '.backupdatum')):
                    existing_backups.append(BackupMetadata(created_date, '0000-00-00'))
    return existing_backups