from datetime import datetime

class User:
    def __init__(self, name:str, email:str, password:str):
        self.name = name
        self._email = email
        self._password = password


    #Getters
    def get_email(self):
        print(f"Email accessed at {datetime.now()}")
        return self._email 
    
    
    @property    #More appropriate
    def email(self):
        return self._email
    

    #Setters
    def set_email(self, new_email):
        self._email = new_email

    @email.setter    #More appropriate
    def email(self, new_email):
        self._email = new_email

    def clean_email(self):
        return self._email.lower().strip()
    



user1 = User("Nelson", "nElSon@gMail.com", "abc")
print(user1.get_email())
print(user1.email)

user1.set_email("nel@GMail.com")
print(user1.clean_email())

#  __private 
#  _protected




