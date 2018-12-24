from .calc import calc_keep_date

def test_keep_first_backup_for_10_years():
    """
       If no other backup exists, the first backup is kept for 10 years.
    """
    backupdate = '2018-05-05'
    existing_backups = []

    keep_date = calc_keep_date(backupdate, existing_backups)

    assert keep_date == '2028-05-05'
