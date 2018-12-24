#!/usr/bin/env python3

import os
import sys
from backupkeeper import walker, calc

if len(sys.argv) == 1:
    print("Date argument missing.")
    print(F"Usage: {sys.argv[0]} <YYYY-MM-DD>")
    exit(-1)

backup_date = sys.argv[1]
existing_backups = walker.walker('.')
keep_date = calc.calc_keep_date(backup_date, existing_backups)
with open(os.path.join(backup_date, walker.storage_file), 'w') as f:
    f.write(keep_date)
