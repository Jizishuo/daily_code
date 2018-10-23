from rediscluster import StrictRedisCluster

if __name__ == '__main__':
    try:
        #构建所有节点
        start_nodes = [
            {"host":'地址ip xxx.xxx.xxx', 'port':'7000端口号'},
            {"host": '地址ip xxx.xxx.xxx', 'port': '7001端口号'},
            {"host": '地址ip xxx.xxx.xxx', 'port': '7002端口号'},
            {"host": '地址ip xxx.xxx.xxx', 'port': '7003端口号'},
        ]
        #构建对象
        src = StrictRedisCluster(start_nodes = start_nodes, decode_responses=True)
        #设置
        result = src.set("name", '66666')
        print(result)
        #获取
        name = src.get("name")
        print(name)
    except Exception as e:
        print(e)