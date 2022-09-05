class User:
    count = 0

    def __init__(self, name, login, password):
        self._name = name
        self._login = login
        self._password = password
        if self.__class__ == User:
            User.count += 1

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value

    @property
    def login(self):
        return self._login

    def set_password(self, value):
        self._password = value

    password = property(fset=set_password)

    def show_info(self):
        return f'{self._name}, {self._login}'


class SuperUser(User):
    count = 0

    def __init__(self, name, login, password, role):
        super().__init__(name, login, password)
        self.role = role
        SuperUser.count += 1

    @property
    def role(self):
        return self._role

    @role.setter
    def role(self, value):
        self._role = value

    def show_info(self):
        return super().show_info() + f' - {self._role}'


user1 = User('Paul McCartney', 'paul', '1234')
user2 = User('George Harrison', 'george', '5678')
user3 = User('Richard Starkey', 'ringo', '8523')
admin = SuperUser('John Lennon', 'john', '0000', 'admin')

print(user1.show_info())
print(admin.show_info())

users = User.count
admins = SuperUser.count

print(f'Всего обычных пользователей: {users}')
print(f'Всего супер-пользователей: {admins}')

user3.name = 'Ringo Star'
print(user3.name)

print(user2.login)
user2.login = 'geo'

user1.password = 'Pa$$wOrd'
print(user2.password)
