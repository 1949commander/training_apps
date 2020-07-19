import os
import time

directory = r'C:\Users\breev\AppData\Local\Programs\Python\Python37\training_apps\file_project'
for filename in os.listdir(directory):
    if filename.endswith(".txt"):
        files = (os.path.join(directory, filename))
        times = (os.path.getmtime(files))
        print( "File Name \n{} time stamp \n{}.".format(files,times))
    else:
        continue

