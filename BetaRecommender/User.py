class User:
  def __init__(self, name, att1, att2, attN):
    self.name = name
    self.att1 = att1
    self.att2 = att2
    self.attN = attN
    
  def printUser(self):
    print(user," profile:\n",att1", "att2"," attN)
    
    
# get user input 
attributes = [X, Y, Z]
choices = []
n = input("Name: " )

for i in attributes:
  choices += input("please rate the importance of ",i," from 1-10: " )
     
me = User(n, choices[0], choices[1], choices[2])

me.printUser()
