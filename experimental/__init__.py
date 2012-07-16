#!/usr/bin/python
# -*- coding: utf-8 -*-

from zx import info

import dictionaryTest
import zx
from compiler.ast import Module


li = []

#缺省值可以不传人
info(li)

zx.info(li, 20, 2)

info(dictionaryTest, 30, 0)

#可以通过指定参数名称调用
info(dictionaryTest, collapse = 2)

#参数可以通过名称，以任意顺序指定
info(collapse = 3, object = li)


#使用getattr创建分发者
import statsout

def output(data, format = "text"):
    #getattr 接受一个缺省的返回值
    output_function = getattr(statsout, "output_%s" %format, statsout.output_default)
    output_function(data)
    
    
if __name__ == "__main__":
    output("abc")
 
    output("abc", "hidden")
     
    output(format = "select", data = 'def')

    #即使格式函数找不到，也不会抛异常，显示调用的是缺省类型
    output(format = "abc", data = 'def')




































