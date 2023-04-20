class usuario:
    def __init__(self, user, password, birthdate, active ):
        self.user = user
        self.password = password
        self.birthdate = birthdate
        self.active = active

    def regresadic(self):
        dic = {"User":self.user,
                "Password":self.password,
                "BirthDate":self.birthdate,
                "Active":self.active}
        return dic