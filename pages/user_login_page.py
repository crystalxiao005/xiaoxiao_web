from common.base import Base


class UserLoginPage(Base):
    username_loc = ("id", "username")
    password_loc = ("id", "password_l")
    login_btn_loc = ("id", "jsLoginBtn")

    forget_password_loc = ("link text", "忘记密码？")
    feedback_loc = ("id", "feedback")

    tips_loc = ("id", "jsLoginTips")

    def input_username(self, text):
        '''输入登录邮箱'''
        self.send(self.username_loc, text)

    def input_password(self, text):
        '''输入密码'''
        self.send(self.password_loc, text)

    def click_login_btn(self):
        '''点登陆按钮'''
        self.click(self.login_btn_loc)

    def get_tips(self):
        return self.get_text(self.tips_loc)

    def get_href(self):
        return self.get_attribute(self.feedback_loc, "href")