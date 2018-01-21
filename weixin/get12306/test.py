#!/usr/bin/env python
#-*- coding:utf-8 -*-
'''
Created on 19:47 2017/11/7 

@author: acer
'''

# from weixin.get12306.get12306 import query_train_info,get_query_url
# str =u'2017-11-20 北京南 南京南'
# url = get_query_url(str)
# info_list = query_train_info(url)
# print(info_list)

import time
#
# newdate = time.time()
# print(newdate)
# time.sleep(30)
# print(time.time())
# print(time.time()-newdate)

def test():
    i =1
    if i>10:
        print('heloo')
        return 0
    else:
        i=i+1
        return test()
if __name__ == '__main__':
    test()