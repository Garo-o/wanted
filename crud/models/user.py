class User(object):
    def __init__(self, id, email, roles, password=''):
        self.id = id
        self.email = email
        self.password = password
        self.roles = roles

    def json(self):
        return {'id': self.id, 'email': self.email, 'password': self.password, 'roles': self.roles}

    def json2(self):
        return {'id': self.id, 'email': self.email, 'roles': self.roles}