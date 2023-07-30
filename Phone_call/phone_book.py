def menu():
  print('\n*********************************Main Menu************************************')
  print('1.Create phone Book\n')
  print('2.Select phone Book\n')
  print('3.Delete Phone Book\n')
  print('4.Exit\n')
  print('********************************************************************************')
  
def menu1():
  print('\n/////////////////////////////////Sub Menu/////////////////////////////////////')
  print('1.Add Contact\n')
  print('2.Modify Contact\n')
  print('3.Show Contact\n')
  print('4.Search Contact\n')
  print('5.Delete Contact\n')
  print('6.Delete Phone Book\n')
  print('////////////////////////////////////////////////////////////////////////////////')
  
contact =[]
import re
regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
regex_name = re.compile(r'^(Mr\.|Mrs\.|Ms\.) ([a-z]+)( [a-z]+)*( [a-z]+)*$', re.IGNORECASE)
      
 
  
def create():
  dict1 = {}
  for i in range (int(input("Number of contacts: "))):
    
    name = input("Enter Contact name as Ms.|Mr.|Mrs.' '-> name: ")
    if re.fullmatch(regex_name,name):
      dict1[name] = []
      email1 = input("Enter Contact email: ")
      if(re.fullmatch(regex, email1)):
        dict1[name].append(email1)
      else:
        print("Unvalid Email")
      
    
      phone2 = input("Enter Contact Phone Number: ")
      if re.match(r"^01[0125][0-9]{8}$",phone2):
        print("valid Phone Number")
        dict1[name].append(phone2)
      else:
        print("Unvalid Phone Number")
    else:
      print("Unvalid name")
  contact.append(dict1)
  print(contact)
 
 
def select():
  dict2={}
  menu1()
  number2 = input("Enter a number from Menu: ")
  select_num = input('Enter the dictionary number: ')
  contact2 = contact[int(select_num)]
  if(number2 == "1"):   
    for j in range (1):
      name = input("Enter Contact name as Ms.|Mr.|Mrs.' '-> name: ")
      if re.fullmatch(regex_name,name):
        dict2[name] = []
        email2 = input("Enter Contact email: ")
        if(re.fullmatch(regex, email2)):
          dict2[name].append(email2)
        else:
          print("Unvalid Email")
        
        phone2 = input("Enter Contact Phone Number: ")
        if re.match(r"^01[0125][0-9]{8}$",phone2):
          print("valid Phone Number")
          dict2[name].append(phone2)
        else:
          print("Unvalid Phone Number")
      else:
        print("UnValid name")
    contact2.update(dict2)
  #print(contact2)
    
  if(number2 == "2"):
    print("##############Modification Menue############")
    print("1.Name")
    print("2.Gmail")
    print("3.Phone numer")
    print("############################################")
    search_contact = input("Enter number ")
    contact2_keys = list(contact2.keys())
    if(search_contact == "1"):
      old_key = input("Enter old name ")
      modfy_key = input("Enter new name ")
      contact2[modfy_key] = contact2.pop(old_key)   
      print(contact2)
    elif(search_contact == "2"):
      modfy_key = input("Enter new name ")
      new_phone = input("Enter new phone number")
      contact2.get(modfy_key)[0]= new_phone
      print(contact2)
    elif(search_contact == "3"):
      modfy_key = input("Enter new name ")
      new_gmail = input("Enter new Gmail Acount")
      contact2.get(modfy_key)[1] = new_gmail
      #print(contact2)
      
      
  if(number2 == "3"):
    if len(contact) != 0:
      if len(contact2) != 0:
        for i in contact2:
          print (i ,"=>",contact2[i],"\n")
      else:
        print("Empty Dictionary")
    
  if(number2 == "4"):  
    search_contact = input("Enter name ")
    contact2_keys = list(contact2.keys())
    for i in contact2_keys:
      if(i == search_contact):
        flag1 = True 
      else:
        flag1 = False
     
    if(flag1 == True):
      print(search_contact+" "+str((contact2[search_contact])))
    else:    
      print("Not found")
      
  if(number2 == "5"):  
    search_contact = input("Enter name ")
    contact2.pop(search_contact)
  
  if(number2 == "6"):  
    contact.pop(int(select_num))
    print(contact)
  
    

def input_number():
  flag = True 
  while(flag):
    menu()
    print('Please, choose a number from the menu: ')
    number1 = input()
    if(number1 == "1"):   create()
    if(number1 == "2"):   select()
    if(number1 == "3"):   contact.clear()
    if(number1 == "4"):   flag = False  

    
   
def main():
  input_number()
 
if __name__ == '__main__':
  main()
  
