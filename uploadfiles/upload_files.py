#!/usr/bin/env python3
# -*-coding:utf-8 -*-
import requests
import os
import json


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
        write_file('result', file.split('.')[0]+result)


def uploadDirFile(file_dir, api_url):
    fileList = getallFiles(file_dir)
    uploadFiles(fileList, api_url)


if __name__ == "__main__":
    #url = 'http://localhost:8020/scaleDetails/importScaleDetail'
    url = 'http://localhost:8020/PortalScaleExpression/importExpression'
    base_dir = 'E:/work/趣味量表/aaaabbbb/'
    uploadDirFile(base_dir, url)
