# Day 
# Create own class in Python  
class User:
    pass 
user_1=User()

# Working with Attributes 
class User:
    pass
user_1=User()
user_1.id="001"
user_1.username="Abhishek"
print(user_1.username)
print(user_1.id)

# Class Constructor
class User:
    def __init__(self):
        pass
user_1=User()
user_1.id="001"
user_1.username="Abhishek"
print(user_1.username)
print(user_1.id)
user_2=User()
user_2.id="002"
user_2.username="Abhi"
print(user_2.username)

# Attributes and __init__ function
class User:
    def __init__(self,user_id,username):
       self.id=user_id
       self.username=username
user_1=User("001","Abhishek")
user_2=User("002","Rohan")
print(f"the id of first user {user_1.id} and name is {user_1.username}" )
print(f"the id of first user {user_2.id} and name is {user_2.username}" )

# Adding Methods to a class
class User:
    def __init__(self,user_id,username):
       self.id=user_id
       self.username=username
       self.followers=0
       self.following=0
    def follow(self,user):
        user.following+=1
        self.followers+=1