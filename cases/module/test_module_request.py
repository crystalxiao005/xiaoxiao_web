
#request.module 通过resuest反向获取请求中的测试函数，类或模板上下文
web_server = "https://hub.docker.com/"

def test_modul(host_env):
    print("读取环境 :%s" % host_env)