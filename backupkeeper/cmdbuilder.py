import datetime


def cmdbuilder(existing_backups):
    today = datetime.date.today()
    for backup in filter_backups(existing_backups, today):
        yield f"rm -rf {backup._created_date}"


def filter_backups(existing_backups, reference_date):
    for backup in existing_backups:
        if backup.older_than(reference_date):
            yield backup
