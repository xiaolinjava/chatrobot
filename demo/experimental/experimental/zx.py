#!/usr/bin/python
# -*- coding: utf-8 -*-


def info(object, spacing = 10, collapse = 1):
    """Print methods and doc strings.
    Takes module, class, list, dictionary, or string."""
    methodList = [method for method in dir(object) if callable(getattr(object, method))]
    processFunc = collapse and (lambda s: " ".join(s.split())) or (lambda s: s)
    
    print("\n".join(["%s %s" %(
                      method.ljust(spacing), 
                      processFunc(str(getattr(object, method).__doc__))) 
                     for method in methodList]))
    
    
if __name__ == "__main__":
    info([], collapse=1)
    
#ljust是一个新的字符串方法， 用空格填充字符串以合指定的长度。 
#如果指定的长度小于字符串， 如果指定的长度小于字符串，ljust 将简单地返回未变化的字符串。它决不会截断字符串。
    



