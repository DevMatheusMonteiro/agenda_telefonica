class Email:
    def __init__(self, email:str=None):
        self.__email = email
    @property
    def email(self):
        return self.__email
    @email.setter
    def email(self, email:str):
        if email != None and email.strip() != "":
            self.__email = email