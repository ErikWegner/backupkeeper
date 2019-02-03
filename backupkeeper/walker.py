import os
import re
from .backupmetadata import BackupMetadata

storage_file = ".backupkeepdate"


def walker(root_directory):
    """
       Load existing backups
    """
    existing_backups = []
    datepattern = re.compile('\\d{4}-\\d{2}-\\d{2}')
    with os.scandir(root_directory) as it:
        for entry in it:
            if entry.name.startswith('.') or not entry.is_dir():
                continue
            if datepattern.match(entry.name) is None:
                continue
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
