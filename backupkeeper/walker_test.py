from .walker import walker


def test_reads():
    result = walker("test_backups")

    assert len(result) == 2


def test_reads_keep_dates():
    result = walker("test_backups")

    assert result[0]._keep_date == "2019-05-11" or result[0]._keep_date == "2019-12-01"
    assert result[1]._keep_date == "2019-12-01" or result[1]._keep_date == "2019-05-11"
