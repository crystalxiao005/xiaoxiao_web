from common.base import Base


class UserRegisterPage(Base):
    email_loc = ("id", "id_email")
    password_loc = ("id", "id_password")
    btn_loc = ("id", "jsEmailRegBtn")
    back_index_loc = ("link text", "回到首页")
    login_now_loc = ("link text", "[立即登录]")
    # 注册成功
    register_success_loc = ("css selector", "body>h1")

    def input_email(self, text=''):
        '''输入邮箱'''
        self.send(self.email_loc, text)

    def input_password(self, text=''):
        '''输入密码'''
        self.send(self.password_loc, text)

    def click_btn(self):
        '''点击注册按钮'''
        self.click(self.btn_loc)

    def get_register_result(self):
        '''获取注册的结果'''
        result = self.get_text(self.register_success_loc)
        return result




