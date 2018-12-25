import datetime
from .backupmetadata import BackupMetadata


def test_older_than_is_true_on_next_day():
    """
        The backup can be removed after 2018-06-11
    """
    bm = BackupMetadata('2018-05-11', '2018-06-11')

    result = bm.older_than(datetime.date(2018, 6, 12))

    assert result == True


def test_older_than_is_false_on_actual_date():
    """
        The backup can be removed after 2018-06-11
    """
    bm = BackupMetadata('2018-05-11', '2018-06-11')

    result = bm.older_than(datetime.date(2018, 6, 11))

    assert result == False


def test_older_than_is_false_on_day_before():
    """
        The backup can be removed after 2018-06-11
    """
    bm = BackupMetadata('2018-05-11', '2018-06-11')

    result = bm.older_than(datetime.date(2018, 6, 10))

    assert result == False
