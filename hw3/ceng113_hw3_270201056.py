menu_text = "1. Log in / change user\n2. Create new user\n3. Add friend\n4. Show my friends\n5. Exit"
def f0():
  print(menu_text)
  option=input("")
  return option
confirmed = 3549
user = "#"
password = "$"
def f1(): 
  f = open("users.txt", "r")
  satır=[]
  satır=(f.readlines())
  for i in range(len(satır)):
    satır[i]=satır[i].split(";")
  i1 = "*"
  for i in range(len(satır)):
    if user == satır[i][0]:
      i1 = i
    elif i1 != "*":
      pass
    else :
      i1 = "*"  
  i2 ="^"
  for i in range(len(satır)):
    if password == satır[i][1]:
      i2 = i
    elif i2 != "*":
      pass  
    else:
      i2 ="^"
  if i1 == i2 :
    confirmed = i1 
    return i1 
  elif i1 == "*" or i2 == "^":
    confirmed = 3549
    return confirmed   
def f2():
  new_user_name = input("Please enter username:\n")
  f = open("users.txt", "r")
  satır=[]
  instants_users=[]
  satır=(f.readlines())
  for i in range(len(satır)):
    satır[i]=satır[i].split(";")
    instants_users.append(satır[i][0])
  f.close()
  if " " in new_user_name :
    uygun1 = "-"
    print("Username not valid\n")
    return
  elif new_user_name in instants_users :
    uygun1= "-"
    print("Username not valid\n")
    return
  elif new_user_name == new_user_name.lower() and new_user_name.isalnum()== True :
    uygun1 = "+"
  else:
    uygun1= "-"
    print("Username not valid\n")
    return 
  new_user_password = input("Please enter password:\n")
  if 4<=len(new_user_password)<=8 and new_user_password.isalnum()== True and new_user_password.isalpha()== False :
    uygun2 = "+"
  else :
    uygun2 = "-"
    print("Password not valid\n")
    return
  if uygun1== "+" and uygun2 == "+":
    new_user = []
    new_user.append(new_user_name +";"+ new_user_password+";\n")
    satır.append(new_user)
    b = []
    b1= " "
    for i in range(len(satır)-1):
      b.append(satır[i][0]+";"+satır[i][1]+";"+satır[i][2])
    b = b+(satır[-1])
    for i in range(len(b)):
      if b1 == " ":
        b1= b1.replace(" ",b[i])
      else:
        b1 = b1+ b[i]
    f = open("users.txt", "w")
    f.write(b1)
    f.close
  return new_user_name, new_user_password 
def f3(): 
  n_friend = input("Please enter the name of your new friend:\n")
  f = open("users.txt", "r")
  satır=[]
  instants_users=[]
  satır=(f.readlines())
  for i in range(len(satır)):
    satır[i]=satır[i].split(";")
    instants_users.append(satır[i][0])
  f.close()
  if n_friend in instants_users :
    if len(satır[f1()][2]) ==1:
      new= n_friend+"\n"
    else:
      new= ","+ n_friend+"\n"
    satır[f1()][2]=(satır[f1()][2].replace("\n",new))     
    b = []
    b1= " "
    for i in range(len(satır)):
      b.append(satır[i][0]+";"+satır[i][1]+";"+satır[i][2])
    for i in range(len(b)):
      if b1 == " ":
        b1= b1.replace(" ",b[i])
      else:
        b1 = b1+ b[i]
    f = open("users.txt", "w")
    f.write(b1)
    f.close
  else :
    print("Friend not found\n")
  
def f4():
  f = open("users.txt", "r")
  satır=[]
  satır=(f.readlines())
  f.close
  for i in range(len(satır)):
    satır[i]=satır[i].split(";")
  satır[f1()][2]=satır[f1()][2].replace("\n","")
  print(satır[f1()][2])
while True :
  print(menu_text)
  option=input("")
  if option in ("1","2","3","4","5"):
    if option== "1":
      user= input("Please enter username:\n")
      password = input("Please enter password:\n")
      f1()
      if f1() < 3549:
        print("Logged in\n")
      else : 
        print("Wrong password or username\n")
    elif option== "2":
      f2()
    elif option== "3":
      if f1() == 3549:
        print("You need to log in first\n")
      
      elif f1() != 3549:
        f3()
      
    elif option== "4":
      if f1() != 3549:
        f4()
      else:
        print("You need to log in first\n")
    elif option== "5":
      break  
  else : 
    print("Invalid option\n")