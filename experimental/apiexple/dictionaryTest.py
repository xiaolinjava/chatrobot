'''
Created on 2012-7-2

@author: Administrator
'''

def buildConnectionString(params):
    """Build a connection string from a dictionary of parameters. 
    
    Returns string. """
    return ";".join(["%s=%s" %(k,v) for k, v in params.items()])


if __name__ == "__main__" :
    
    """ 创建一个dictionary哈希对象"""
    myParams = {"server": "mpilgrim", "database": "master", "uid": "sa", "pwd": "secret"}
    
    """ 打印指定key的哈希值"""
    print(myParams["server"]) 

    """动态添加哈希元素 """
    myParams["conn"] = "jdbc"
    myParams["poolsize"] = 10
    myParams[1] = "abc"
    print(myParams)
    
    ''' 删除独立元素'''
    del myParams[1]
    print(myParams)

    ''' 清除哈希表的所有元素'''
    myParams.clear()
    print(myParams)
    
    """动态修改指定key的哈希值,如果不存在，等同于添加哈希元素 """
    myParams["pwd"] = "sa"

    print(buildConnectionString(myParams))
    
    

    
    
    