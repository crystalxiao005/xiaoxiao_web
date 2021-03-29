from pages.user_register_page import UserRegisterPage




class TestRegisterCase():

    def test_register_success_1(self, driver, base_url):
        '''输入未注册的邮箱，注册成功'''
        register = UserRegisterPage(driver, base_url)
        register.open("/users/register/")
        # 输入邮箱，密码，点登陆
        register.input_email("999@qq.com")
        register.input_password("123456")
        register.click_btn()
        # 实际结果
        actual_result = register.get_register_result()
        # 期望结果
        expect_result = "尊敬的用户，您好，账户已激活成功！"
        # 断言
        assert actual_result == expect_result


    def test_register_fail_1(self, driver, base_url):

        
        '''已注册过的邮箱，注册失败'''
        register = UserRegisterPage(driver, base_url)
        register.open("/users/register/")
        # 输入邮箱，密码，点登陆
        register.input_email("1234@qq.com")
        register.input_password("123456")
        register.click_btn()
        # 实际结果
        actual_result = register.get_register_result()
        # 期望结果
        expect_result = "尊敬的用户，您好，账户已激活成功！"
        # 断言
        assert actual_result != expect_result



