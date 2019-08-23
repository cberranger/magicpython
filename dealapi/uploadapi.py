#!/usr/bin/env python3
# -*-coding:utf-8 -*-
import requests
import os
import json


def uploadImg(api_url, img_name):
    img = open(img_name, 'rb')
    img_file = {'file': img}
    response = requests.post(api_url, files=img_file)
    return response.text


def write_file(str_title, str_content):
    os.makedirs('base64', exist_ok=True)
    with open('base64/'+str_title+'.txt', 'a') as f:
        f.write(str_content)


if __name__ == "__main__":
    url = 'http://192.168.10.241:2019/file/fdfs/upload/'
    for i in range(1, 61):
        print('上传'+str(i))
        result = uploadImg(url, 'images/' + str(i) + '.png')
        result = json.loads(result)['data'][0]
        print(result)
        a = '<img src='+result+' />'
        write_file('urls', str(i)+' : '+a+'\n')
