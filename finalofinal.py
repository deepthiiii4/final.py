import math
import pyfiglet
name = str(input("enter name: "))
length = int(input("enter the banner length: "))
y = len(name)
char_len = 6*y
j = math.ceil(length/6)-1
while(char_len>length):
    if(char_len % length != 0):
     name1 = name[:j]+"-"
     name2 = name[j:]
     print(pyfiglet.figlet_format(name1, font="6x10"))
     print()
     print(pyfiglet.figlet_format(name2, font="6x10"))

    
     break
while(char_len == length):
    print(pyfiglet.figlet_format(name, font="6x10"))
    break
    
while(char_len<length):
     out3 = pyfiglet.figlet_format(name, font="6x10")
     print(out3)
     break
      



 
