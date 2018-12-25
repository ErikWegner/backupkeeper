import datetime


class BackupMetadata():
    def __init__(self, created_date, keep_date):
        self._created_date = created_date
        self._keep_date = keep_date
        self.__setupProps()

    def __setupProps(self):
        parts = self._created_date.split("-")
        self.createdYear = int(parts[0])
        self.createdMonth = int(parts[1])
        self.createdDay = int(parts[2])

        parts = self._keep_date.split("-")
        self.keep_date_date = datetime.date(
            int(parts[0]), int(parts[1]), int(parts[2]))

    def older_than(self, reference_date):
        return self.keep_date_date < reference_date
