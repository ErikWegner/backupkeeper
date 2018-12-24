from .calc import calc_keep_date
from .backupmetadata import BackupMetadata


def test_keep_first_backup_for_10_years():
    """
       If no other backup exists, the first backup is kept for 10 years.
    """
    backupdate = '2018-05-05'  # Saturday
    existing_backups = []

    keep_date = calc_keep_date(backupdate, existing_backups)

    assert keep_date == '2028-05-05'


def test_keep_second_backup_for_1_year():
    """
       If no other monthly backup exists, the backup is kept for 1 year.
    """
    backupdate = '2018-06-06'  # Wednesday
    existing_backups = []
    existing_backups.append(
        BackupMetadata('2018-05-05', '2028-05-05'),
    )

    keep_date = calc_keep_date(backupdate, existing_backups)

    assert keep_date == '2019-06-06'


def test_keep_monday_backup_for_1_week():
    """
       If other backups exists, the backup for monday to thursday is kept for 1 week.
    """
    backupdate = '2018-05-07'  # Monday
    existing_backups = [
        BackupMetadata('2018-05-05', '2028-05-05'),
        BackupMetadata('2018-05-06', '2019-05-06'),
    ]

    keep_date = calc_keep_date(backupdate, existing_backups)

    assert keep_date == '2018-05-14'


def test_keep_tuesday_backup_for_1_week():
    """
       If other backups exists, the backup for monday to thursday is kept for 1 week.
    """
    backupdate = '2018-05-08'  # Tuesday
    existing_backups = [
        BackupMetadata('2018-05-05', '2028-05-05'),
        BackupMetadata('2018-05-06', '2019-05-06'),
        BackupMetadata('2018-05-07', '2018-05-14'),
    ]

    keep_date = calc_keep_date(backupdate, existing_backups)

    assert keep_date == '2018-05-15'


def test_keep_wednesday_backup_for_1_week():
    """
       If other backups exists, the backup for monday to thursday is kept for 1 week.
    """
    backupdate = '2018-05-09'  # Wednesday
    existing_backups = [
        BackupMetadata('2018-05-05', '2028-05-05'),
        BackupMetadata('2018-05-06', '2019-05-06'),
        BackupMetadata('2018-05-07', '2018-05-14'),
        BackupMetadata('2018-05-08', '2018-05-15'),
    ]

    keep_date = calc_keep_date(backupdate, existing_backups)

    assert keep_date == '2018-05-16'


def test_keep_thursday_backup_for_1_week():
    """
       If other backups exists, the backup for monday to thursday is kept for 1 week.
    """
    backupdate = '2018-05-10'  # Thursday
    existing_backups = [
        BackupMetadata('2018-05-05', '2028-05-05'),
        BackupMetadata('2018-05-06', '2019-05-06'),
        BackupMetadata('2018-05-07', '2018-05-14'),
        BackupMetadata('2018-05-08', '2018-05-15'),
        BackupMetadata('2018-05-09', '2018-05-16'),
    ]

    keep_date = calc_keep_date(backupdate, existing_backups)

    assert keep_date == '2018-05-17'


def test_keep_friday_backup_for_2_weeks():
    """
       If other backups exists, the backup for friday is kept for 14 week.
    """
    backupdate = '2018-05-11'  # Friday
    existing_backups = [
        BackupMetadata('2018-05-05', '2028-05-05'),
        BackupMetadata('2018-05-06', '2019-05-06'),
        BackupMetadata('2018-05-07', '2018-05-14'),
        BackupMetadata('2018-05-08', '2018-05-15'),
        BackupMetadata('2018-05-09', '2018-05-16'),
    ]

    keep_date = calc_keep_date(backupdate, existing_backups)

    assert keep_date == '2018-05-25'


def test_carry_over_to_next_month():
    """
       Date will carry over to next month
    """
    backupdate = '2018-05-18'  # Friday
    existing_backups = [
        BackupMetadata('2018-05-05', '2028-05-05'),
        BackupMetadata('2018-05-06', '2019-05-06'),
        BackupMetadata('2018-05-07', '2018-05-14'),
        BackupMetadata('2018-05-08', '2018-05-15'),
        BackupMetadata('2018-05-09', '2018-05-16'),
        BackupMetadata('2018-05-11', '2018-05-25'),
    ]

    keep_date = calc_keep_date(backupdate, existing_backups)

    assert keep_date == '2018-06-01'


def test_keep_first_day_of_month_for_1_year_even_on_friday():
    """
       If other backups exists, the backup for friday is kept for 14 week.
    """
    backupdate = '2018-06-01'  # Friday
    existing_backups = [
        BackupMetadata('2018-05-05', '2028-05-05'),
        BackupMetadata('2018-05-06', '2019-05-06'),
        BackupMetadata('2018-05-07', '2018-05-14'),
        BackupMetadata('2018-05-08', '2018-05-15'),
        BackupMetadata('2018-05-09', '2018-05-16'),
        BackupMetadata('2018-05-11', '2018-05-25'),
        BackupMetadata('2018-05-18', '2018-06-01'),
        BackupMetadata('2018-05-25', '2018-06-08'),
    ]

    keep_date = calc_keep_date(backupdate, existing_backups)

    assert keep_date == '2019-06-01'


def test_keep_first_day_of_month_for_1_year_even_on_monday():
    """
       If other backups exists, the backup for friday is kept for 14 week.
    """
    backupdate = '2018-07-01'  # Monday
    existing_backups = [
        BackupMetadata('2018-05-05', '2028-05-05'),
        BackupMetadata('2018-05-06', '2019-05-06'),
        BackupMetadata('2018-05-07', '2018-05-14'),
        BackupMetadata('2018-05-08', '2018-05-15'),
        BackupMetadata('2018-05-09', '2018-05-16'),
        BackupMetadata('2018-05-09', '2018-05-16'),
        BackupMetadata('2018-05-11', '2018-05-25'),
        BackupMetadata('2018-05-18', '2018-06-01'),
        BackupMetadata('2018-05-25', '2018-06-08'),
        BackupMetadata('2018-06-01', '2019-06-01'),
    ]

    keep_date = calc_keep_date(backupdate, existing_backups)

    assert keep_date == '2019-07-01'


def test_keep_first_day_of_year_for_10_years_even_on_tuesday():
    """
       On the first day of the new year, keep backup for 10 years
    """
    backupdate = '2019-01-01'  # Tuesday
    existing_backups = [
        BackupMetadata('2018-05-05', '2028-05-05'),
        BackupMetadata('2018-05-06', '2019-05-06'),
        BackupMetadata('2018-05-07', '2018-05-14'),
        BackupMetadata('2018-05-08', '2018-05-15'),
        BackupMetadata('2018-05-09', '2018-05-16'),
        BackupMetadata('2018-05-09', '2018-05-16'),
        BackupMetadata('2018-05-11', '2018-05-25'),
        BackupMetadata('2018-05-18', '2018-06-01'),
        BackupMetadata('2018-05-25', '2018-06-08'),
        BackupMetadata('2018-06-01', '2019-06-01'),
    ]

    keep_date = calc_keep_date(backupdate, existing_backups)

    assert keep_date == '2029-01-01'


def test_keep_first_backup_of_year_for_10_years_even_on_tuesday():
    """
       If no other backup exists for the year, the first backup is kept for 10 years.
    """
    backupdate = '2019-01-01'  # Tuesday
    existing_backups = [
        BackupMetadata('2018-05-05', '2028-05-05'),
        BackupMetadata('2018-05-06', '2019-05-06'),
        BackupMetadata('2018-05-07', '2018-05-14'),
        BackupMetadata('2018-05-08', '2018-05-15'),
        BackupMetadata('2018-05-09', '2018-05-16'),
        BackupMetadata('2018-05-09', '2018-05-16'),
        BackupMetadata('2018-05-11', '2018-05-25'),
        BackupMetadata('2018-05-18', '2018-06-01'),
        BackupMetadata('2018-05-25', '2018-06-08'),
        BackupMetadata('2018-06-01', '2019-06-01'),
    ]

    keep_date = calc_keep_date(backupdate, existing_backups)

    assert keep_date == '2029-01-01'
