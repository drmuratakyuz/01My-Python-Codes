class enemy: #defination of a class
  left_life = 3 # defination a global variable
  def attack(self): #defination of first function in the class
    print("Attaaaacckkkkk!!!!")
    self.left_life -=1
  
  def ishealive(self): #defination of second function in the class
    if (self.left_life <=0):
      print("Dead")
    else:
      print(str(self.left_life) + " life left.")
  #defination of the different enemies 
enemy01 = enemy()
enemy02 = enemy()
enemy03 = enemy()
enemy04 = enemy()
# the attacks of the enemies (after each attack the left life number is down )
enemy01.attack()  
enemy02.attack()
enemy02.attack()
enemy03.attack()
enemy03.attack()
enemy03.attack()

#printing the left lifes of each enemies
enemy01.ishealive()
enemy02.ishealive()
enemy03.ishealive()
enemy04.ishealive()