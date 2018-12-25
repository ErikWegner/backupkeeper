import datetime
from .cmdbuilder import filter_backups, cmdbuilder
from .backupmetadata import BackupMetadata


def test_outputs_second_item():
    result = filter_backups([
        BackupMetadata('2018-01-01', '2018-06-01'),
        BackupMetadata('2018-02-01', '2018-05-01'),
        BackupMetadata('2018-03-01', '2018-07-01'),
    ], datetime.date(2018, 5, 2))

    assert len(list(result)) == 1


def test_creates_command():
    today = datetime.date.today()
    td = datetime.timedelta(days = 1)

    existing_backups = [
        BackupMetadata('2018-01-01', dateFormat(today + td)),
        BackupMetadata('2018-02-01', dateFormat(today - td)),
        BackupMetadata('2018-03-01', dateFormat(today)),
    ]

    cmds = list(cmdbuilder(existing_backups))

    assert len(cmds) == 1
    assert cmds[0] == "rm -rf 2018-02-01"

def dateFormat(d):
    return f"{d.year:04}-{d.month:02}-{d.day:02}"