#!/usr/bin/env python3
# -*-coding:utf-8 -*-
import requests
import os
import json
import csv


def uploadFile(api_url, fileName):
    file = open(fileName, 'rb')
    file = {'file': file}
    response = requests.post(api_url, files=file)
    print(response.text)
    return response.text


def write_file(str_title, str_content):
    os.makedirs('base64', exist_ok=True)
    with open('base64/'+str_title+'.txt', 'a') as f:
        f.write(str_content+'\n')


def write_csv(str_title, str_content):
    with open('images.csv', 'a', newline="") as f:
        writer = csv.writer(f)
        writer.writerow((str_title, str_content))

# get file list


def getallFiles(file_dir):
    b = []
    for root, dirs, files in os.walk(file_dir):
        a = files
    for file in a:
        print(file_dir + file)
        b.append(file_dir + file)
    return b


def uploadFiles(fileList, api_url):
    for file in fileList:
        result = uploadFile(api_url, file)
        result = json.loads(result)['data'][0]
        write_csv(file.split('.')[0].split('/')[5], result)


def uploadDirFile(file_dir, api_url):
    fileList = getallFiles(file_dir)
    uploadFiles(fileList, api_url)


if __name__ == "__main__":
    with open('images.csv', 'w', newline="") as f:
        writer = csv.writer(f)
        writer.writerow(('量表字典', '图片链接'))
    url = 'http://192.168.10.196:2019/file/fdfs/upload/'
    base_dir = 'E:/www/magicpython/dealPesImages/images/'
    uploadDirFile(base_dir, url)
