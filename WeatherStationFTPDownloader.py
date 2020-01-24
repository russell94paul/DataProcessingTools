# -*- coding: utf-8 -*-
"""
Created on Thu Jan 23 02:29:02 2020

@author: RussellP
"""

import os
from ftplib import FTP, error_perm

def ftpDownloader(stationId, startYear, endYear, url="ftp.pyclass.com", user="student@pyclass.com", passwd="student123"):
    ftp=FTP(url)
    ftp.login(user, passwd)
    
    # Checks if directory exists, if not create dir
    if not os.path.exists("C:\\Data Processing\\"):
        os.makedirs("C:\\Data Processing\\")
    os.chdir("C:\\Data Processing\\")
    
    for year in range(startYear, endYear+1):
        fullpath = '/Data/%s/%s-%s.gz' % (year, stationId, year)
        filename = os.path.basename(fullpath)
        try:
            with open(filename, 'wb') as file:
                 ftp.retrbinary('RETR %s' %fullpath, file.write)
            print("%s successfully downloaded" % filename)
        except error_perm:
            print("%s is not available" % filename)
            os.remove(filename)
    ftp.close()