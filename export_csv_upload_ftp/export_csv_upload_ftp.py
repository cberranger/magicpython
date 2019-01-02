#!/usr/bin/env python
#coding=utf-8
import cx_Oracle as cxo
import sys
import csv
from ftplib import FTP
import zipfile
import configparser


class Db(object):
        def __init__(self,db_host,db_port,db_user,db_passwd,db_name):
                self.db_host = db_host
                self.db_port=db_port
                self.db_user=db_user
                self.db_passwd=db_passwd
                self.db_name=db_name
        def to_database_str(self):
                database_str=self.db_user+'/'+self.db_passwd+'@'+self.db_host+':'+str(self.db_port)+'/'+self.db_name
                return database_str

class MyFtp(object):
	def __init__(self,ftp_host,ftp_port,ftp_user,ftp_passwd):
		self.ftp_host = ftp_host
		self.ftp_port=ftp_port
		self.ftp_user=ftp_user
		self.ftp_passwd=ftp_passwd


# read db config from db.conf
def readDBConf():
        cf = configparser.ConfigParser()
        cf.read('db.conf')
        db_host = cf.get("db", "db_host")
        db_port = cf.getint("db", "db_port")
        db_user = cf.get("db", "db_user")
        db_passwd = cf.get("db", "db_passwd")
        db_name=cf.get("db","db_name")
        db=Db(db_host,db_port,db_user,db_passwd,db_name)
        return db  

# read ftp config from db.conf
def readFTPConf():
	cf = configparser.ConfigParser()
	cf.read('db.conf')
	ftp_host = cf.get("ftp", "ftp_host")
	ftp_port = cf.getint("ftp", "ftp_port")
	ftp_user = cf.get("ftp", "ftp_user")
	ftp_passwd = cf.get("ftp", "ftp_passwd")
	myftp=MyFtp(ftp_host,ftp_port,ftp_user,ftp_passwd)
	return myftp 
# get log level
def readLogConf():
        cf = configparser.ConfigParser()
        cf.read('db.conf')
        log_level = cf.get("log", "log_level")
        return log_level

# create connection to ftp
def ftpconnect(yourftp):
    ftp = FTP()
    ftp.set_debuglevel(2)
    ftp.connect(yourftp.ftp_host, yourftp.ftp_port)
    ftp.login(yourftp.ftp_user, yourftp.ftp_passwd)
    return ftp

# download file from ftp
def downloadfile(ftp, remotepath, localpath):
    bufsize = 1024
    fp = open(localpath, 'wb')
    ftp.retrbinary('RETR ' + remotepath, fp.write, bufsize)
    ftp.set_debuglevel(0)
    fp.close()

# upload file from local to ftp
def uploadfile(ftp, remotepath, localpath):
    bufsize = 1024
    fp = open(localpath, 'rb')
    ftp.storbinary('STOR ' + remotepath, fp, bufsize)
    ftp.set_debuglevel(0)
    fp.close()

# zip the files to one
def zip_files( files, zip_name ):
    zip = zipfile.ZipFile( zip_name+'.zip', 'w', zipfile.ZIP_DEFLATED )
    for file in files:
        print ('compressing', file)
        zip.write( file )
    zip.close()
    print ('compressing finished')

# write log to database or file or print 
def write_log(log_name,log_content,author,log_id):
        log_level=readLogConf()
        if log_level==0:
                pass
        elif log_level==1:
                print_log()
        elif log_level==2:
                log_to_file()
        elif log_level==3:
                log_to_database()                        




# execute sql and generate csv file 
def sql_to_scv(db,sql,csv_name):
        database_str=db.to_database_str()
        conn=cxo.connect(database_str)
        curs=conn.cursor()
        rr=curs.execute(sql)
        for rowdata in rr:
                with open(csv_name+'.csv','w',encoding='utf-8')as f:
                        writer=csv.writer(f)
                        writer.writerow((rowdata))
        curs.close()
        conn.close()                


def do_all_thing(sql,csv_name,zip_file_name,file_name,remote_path,local_path):
        db=readDBConf()
        my_ftp=readFTPConf()
        sql_to_scv(db,sql,csv_name)
        zip_files(zip_file_name,csv_name)
        ftp=ftpconnect(my_ftp)
        uploadfile(ftp,remote_path,local_path)
        ftp.quit()


if __name__ == "__main__":
        sql='select * from r_tmnl_run  where rownum<1000'
        do_all_thing(sql,'articles',['articles.csv'],'articles','pub/articles.zip','articles.zip')
