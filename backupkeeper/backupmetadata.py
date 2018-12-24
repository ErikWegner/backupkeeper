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
