import pytest
#request.config的使用，添加一个hook函数pytest_addoption

def pytest_addoption(parser):
    #addoption读取命令行参数
    #help：提示给用户的帮助信息，告诉用户的选择信息，测试环境test，自动化环境uat，预发布环境pre
    parser.addoption(
        "--host",action="store",default = "test",help = "option：test or uat or pre"
    )
    #读取pytest.ini文件中自定义的参数user=小小
    parser.addini(
        name = "user",
        type = None,
        default="admin",
        help="pytest.ini:test user"
    )
    #读取pytest.ini文件中自定义的参数url地址
    parser.addini(
        name = "url",
        type = None,
        default="test",
        help="pytest.ini:test url"
    )

#方法一：request.config读取命令行参数
@pytest.fixture()
def host_env(request):
    env = request.config.getoption("--host")
    if env == "test":
        url =  "http://49.235.92.12:8200/users/login/"
    elif env == "uat":
        url =  "https://www.baidu.com"
    else:
        url = "http://49.235.92.12:7005/api/v1/login/"
    #此处为request.module
    #通过request.module反向获取请求中的测试函数，类或模板上下文
    #getattr（模板类object，名称namr，默认fault）
    server = getattr(request.module,"web_server",url)
    return server

#方法二：pytestconfig读取命令行参数
@pytest.fixture()
def get_env(pytestconfig):
    env = pytestconfig.config.getoption("--host")
    #接下来的和上面一样

#pytestconfig读取ini配置文件的参数
#autouse表示自动使用
@pytest.fixture(scope="session",autouse="True")
def get_ini(pytestconfig):
    cmdopts = pytestconfig.getini("addopts")
    print("pytestconfig读取ini配置文件的参数 %s" % cmdopts )

#pytestconfig读取ini配置文件自定义的user
@pytest.fixture(scope="session",autouse="True")
def get_user(pytestconfig):
    user = pytestconfig.getini("user")
    print("读取到ini文件的user：%s" % user)

#pytestconfig读取ini配置文件自定义的user
@pytest.fixture(scope="session",autouse="True")
def get_url(pytestconfig):
    url = pytestconfig.getini("url")
    print("读取到ini文件的url：%s" % url)
