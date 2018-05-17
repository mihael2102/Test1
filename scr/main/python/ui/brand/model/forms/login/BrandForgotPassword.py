from scr.main.python.ui.brand.model.ca_base_page.BrandBasePage import BrandBasePage


class BrandForgotPassword(BrandBasePage):

    def __init__(self):
        super().__init__()

    def set_email(self, email):
        forgot_password_link = super().wait_load_element("//input[@name='login']")
        forgot_password_link.clear()
        forgot_password_link.send_keys(email)
        return BrandForgotPassword()

    def restore_password(self):
        forgot_password_link = super().wait_load_element("//button[contains(text(),'Restore password')]")
        forgot_password_link.click()
        return BrandForgotPassword()
