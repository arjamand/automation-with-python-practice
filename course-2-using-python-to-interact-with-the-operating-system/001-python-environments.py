# 2024-06-23 13:45:45


# #001
# #!/usr/bin/env python3
# import numpy as np

# def numpyArray():
#     x = np.array([[1, 2, 3], [4, 5, 6]], np.int32)
#     y = np.array([[3, 6, 2], [9, 12, 8]], np.int32)
#     return x*y
# print(numpyArray())





#002
#check for system resources

import shutil
import psutil

def check_disk_usage():
    du = shutil.disk_usage("/")
    free = du.free / du.total * 100 
    return free > 20

def check_cpu_usage():
    usage = psutils.cpu_percent(1)
    return usage < 75
if check_disk_usage and check_cpu_usage :
    print("PC is in healthy condition .")
elif check_disk_usage and not check_cpu_usage:
    print("Storage is Good , Cpu not so good .")
elif not check_disk_usage and check_cpu_usage:
    print("You are nearly out of storage , CPU usage is goos .")
else :
    print("Eroorrrrr")