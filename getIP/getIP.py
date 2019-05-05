#导包
import fileinput
import re

def readArw():

    for line in fileinput.input(r"ip92.txt"):   #读取文件信息  raw.txt我的是存放在G盘
        print(line)

def readIp():
    with open(r'ip92.txt', 'r') as f:  # with open（文件名+操作方法+缓存时间/默认为0）
        print("Name of the file: ", f.name)  # 打印文件名
        for line in f.readlines():
            result2 = re.findall('[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}',line) #匹配ip正则表达式方法一、

            # result2 = re.findall(r'(?<![\.\d])(?:\d{1,3}\.){3}\d{1,3}(?![\.\d])',line) #匹配ip正则表达式方法二、
            if not result2 == []:
                print(result2[0])
                result = result2[0] + '\n'
                with open('92.txt', 'a+') as w:
                    w.write(result)

import logging

__all__ = ['logger']


# create logger 创建日志
logger = logging.getLogger('Jackzz')
logger.setLevel(logging.DEBUG)
# create file handler which logs even debug messages
fh = logging.FileHandler('raw.log', mode='w')  # NOTICE: this will clear the log file!
fh.setLevel(logging.DEBUG)
# create console handler with a higher log level
ch = logging.StreamHandler()
ch.setLevel(logging.INFO)
# create formatter and add it to the handlers
formatter = logging.Formatter('[%(asctime)s][%(name)s][%(levelname)s]: %(message)s')
fh.setFormatter(formatter)
ch.setFormatter(formatter)
# add the handlers to the logger
logger.addHandler(fh)
logger.addHandler(ch)
# logger.addFilter(fh)
# logger.addFilter(ch)



if __name__ == '__main__':
    readArw()#执行
    readIp()#执行def readIp()中定义的操作
    logger.info('logger test')
    # log = Logger('arw.log',level='debug')
    # log.logger.debug('debug')
    # log.logger.info('info')
    # log.logger.warning('警告')
    # log.logger.error('报错')
    # log.logger.critical('严重')
    # Logger('error.log', level='error').logger.error('error')