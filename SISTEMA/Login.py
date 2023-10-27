class Login:
    def __init__(self, login_id, email, password, registration_date, user_id):
        self.login_id = login_id
        self.email = email
        self.password = password
        self.user_id = user_id

    def get_login_id(self):
        return self.login_id

    def get_email(self):
        return self.email

    def get_password(self):
        return self.password

    def get_user_id(self):
        return self.user_id
