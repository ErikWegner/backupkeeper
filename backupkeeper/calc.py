def calc_keep_date(backupdate, existing_backups):
    """
        Calculate the date until a backup is protected from deletion.
        backupdate: The date of a backup
        existing_backups: A list of existing backup dates
    """
    if len(existing_backups) == 0:
        parts = backupdate.split("-")
        parts[0] = str(int(parts[0]) + 10)
        return f"{parts[0]}-{parts[1]}-{parts[2]}"