from .walker import walker

def test_reads():
    result = walker("test_backups")

    assert len(result) == 2
