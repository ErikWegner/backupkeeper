#!/usr/bin/env python3

import os
import sys
from backupkeeper import walker, cmdbuilder

existing_backups = walker.walker('.')
cmds = cmdbuilder.cmdbuilder(existing_backups)
for cmd in cmds:
    print(cmd)
