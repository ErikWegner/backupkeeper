import datetime

def calc_keep_date(backupdate, existing_backups):
    """
        Calculate the date until a backup is protected from deletion.
        backupdate: The date of a backup
        existing_backups: A list of existing backup dates
    """
    parts = backupdate.split("-")
    year = int(parts[0])
    month = int(parts[1])
    day = int(parts[2])

    if check_has_backup_this_year(year, existing_backups) == False:
        year = year + 10
    else:
        if check_has_backup_this_month(year, month, existing_backups) == False:
            # add 1 year
            year = year + 1
        else:
            if is_friday(year, month, day):
                year, month, day = addWeeks(year, month, day, 2)
            else:
                year, month, day = addWeeks(year, month, day, 1)


    return f"{year:04}-{month:02}-{day:02}"


def check_has_backup_this_year(year, existing_backups):
    """
        Check if any backup in existing_backups matches year.
    """
    for backup in existing_backups:
        if backup.createdYear == year:
            return True

    return False


def check_has_backup_this_month(year, month, existing_backups):
    """
        Check if any backup in existing_backups matches year and month.
    """
    for backup in existing_backups:
        if backup.createdYear == year and backup.createdMonth == month:
            return True

    return False


def is_friday(year, month, day):
    d = datetime.date(year, month, day)
    return d.weekday() == 4

def addWeeks(year, month, day, num_weeks):
    d = datetime.date(year, month, day)
    td = datetime.timedelta(days = num_weeks * 7)
    d = d + td
    return d.year, d.month, d.day