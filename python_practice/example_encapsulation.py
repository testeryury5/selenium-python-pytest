
class Bank:

    def __init__(self):
        self.name = 'Bank of America'
        self.login = 'Yuriy'
        self.__password = '12345'


unsecured = Bank()
print(unsecured.name)
print(unsecured.login)
print(unsecured.password)