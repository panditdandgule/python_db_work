import shutil
import psutil
import sys

path='C:/'
stat=shutil.disk_usage(path)
print("Disk usage statics:",stat)
cpu=psutil.disk_usage()