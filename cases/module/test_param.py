import pytest

#request.param的使用
@pytest.fixture(params=["user1","user2"])
def register_user(request):
    user = request.param
    result = {"code":0,"msg":"success"}
    return user,result

def test_regiser_user(register_user):
    user,actual_result = register_user
    print("测试用户user：%s"% user )
    print("测试结果actual_result：%s"% actual_result )
    assert actual_result["msg"] == "success"