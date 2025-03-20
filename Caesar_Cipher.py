alphabets=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


cond=True
def ceaser(Plain_text, shift_num):
    code=''
    for char in Plain_text:
        if char in alphabets:
            
            position=alphabets.index(char)
            if choice=='encode':
                new_position=position+shift_num
            elif choice=='decode':
                new_position=position-shift_num
            new_letter=alphabets[new_position]
            code=code+new_letter
        else:
            code=code+char
    print(f'Your {choice}d text is \n{code}\n')
    


print('''
                                       _       _               
  ___ __ _  ___  ___  __ _ _ __    ___(_)_ __ | |__   ___ _ __ 
 / __/ _` |/ _ \/ __|/ _` | '__|  / __| | '_ \| '_ \ / _ \ '__|
| (_| (_| |  __/\__ \ (_| | |    | (__| | |_) | | | |  __/ |   
 \___\__,_|\___||___/\__,_|_|     \___|_| .__/|_| |_|\___|_|   
                                        |_|                    
      ''')      
while cond==True:
    choice=input('Type "encode" for encrypt and "decode" for decrypt :\n').lower()

    text=input('Type your message :\n').lower()
    shift=int(input('Give the shift number :\n'))
    shift=shift%25
    ceaser(Plain_text=text, shift_num=shift)
    a=input('Do you want to go again type "yes".Otherwise "no" : ').lower()
    if a=='no':
        cond=False
print('Thank you!')        
    
