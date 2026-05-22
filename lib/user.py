class User:
    def __init__(self, email, password, id = None):
        self.id = id
        self.email = email
        self.password = password