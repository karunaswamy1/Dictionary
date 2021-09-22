my_dict = {
    'a':50, 
    'b':58, 
    'c':56,
    'd':40, 
    'e':100, 
    'f':20
    }
three_highest=max(my_dict,key=my_dict.get)
three_highest=max(my_dict.values())
print(three_highest)
