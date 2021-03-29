from pages.user_login_page import UserLoginPage


class TestLoginCase():

    def test_login_success(self, login_instance:UserLoginPage):
        login_instance.open('/users/login/')
        login_instance.input_username("1234@qq.com")
        login_instance.input_password("123456")
        login_instance.click_login_btn()
        # 获取实际结果
        actual_result = login_instance.get_title()
        exepect_result = "欢迎访问在线学习网——首页"
        assert actual_result == exepect_result


    def test_login_fail(self, login_instance:UserLoginPage):
        login_instance.open('/users/login/')
        login_instance.input_username("1234@qq.com")
        login_instance.input_password("1234567")
        login_instance.click_login_btn()
        # 获取实际结果

        actual_result = login_instance.get_tips()
        assert actual_result == "用户名或密码错误"

    def test_link_feedback(self, login_instance:UserLoginPage, base_url):
        '''意见反馈的link'''
        login_instance.open('/users/login/')
        actual_result = login_instance.get_href()
        expected_href = base_url+"/users/feedbackiframe/"
        assert actual_result == expected_href

