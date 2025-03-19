import random
conti=False
def game():
    print('''
     _                                             
    | |                                            
    | |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
    | '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
    | | | | (_| | | | | (_| | | | | | | (_| | | | |
    |_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                        __/ |                      
                       |___/                             
          
    ''')


    HANGMAN= ['''
      +---+
      |   |
      O   |
     /|\  |
     / \  |
          |
    =========''', '''
      +---+
      |   |
      O   |
     /|\  |
     /    |
          |
    =========''', '''
      +---+
      |   |
      O   |
     /|\  |
          |
          |
    =========''', '''
      +---+
      |   |
      O   |
     /|   |
          |
          |
    =========''', '''
      +---+
      |   |
      O   |
      |   |
          |
          |
    =========''', '''
      +---+
      |   |
      O   |
          |
          |
          |
    =========''', '''
      +---+
      |   |
          |
          |
          |
          |
    =========''']

    country_name=[
        "AFGHANISTAN", "ALBANIA", "ALGERIA", "ANDORRA", "ANGOLA", "ARGENTINA",
        "ARMENIA", "AUSTRALIA", "AUSTRIA", "AZERBAIJAN", "BAHAMAS", "BAHRAIN",
        "BANGLADESH", "BARBADOS", "BELARUS", "BELGIUM", "BELIZE", "BENIN",
        "BHUTAN", "BOLIVIA", "BRAZIL", "BULGARIA", "CANADA", "CHILE",
        "CHINA", "COLOMBIA", "COSTARICA", "CROATIA", "CUBA", "CYPRUS",
        "CZECHIA", "DENMARK", "DJIBOUTI", "DOMINICA", "ECUADOR", "EGYPT",
        "ESTONIA", "ETHIOPIA", "FIJI", "FINLAND", "FRANCE", "GERMANY",
        "GHANA", "GREECE", "GUATEMALA", "HONDURAS", "HUNGARY", "ICELAND",
        "INDIA", "INDONESIA", "IRAN", "IRAQ", "IRELAND", "ISRAEL", "ITALY",
        "JAMAICA", "JAPAN", "JORDAN", "KAZAKHSTAN", "KENYA", "KOREA",
        "KUWAIT", "LATVIA", "LEBANON", "LITHUANIA", "LUXEMBOURG", "MALAYSIA",
        "MEXICO", "MONACO", "MONGOLIA", "MOROCCO", "NEPAL", "NETHERLANDS",
        "NIGERIA", "NORWAY", "PAKISTAN", "PANAMA", "PARAGUAY",
        "PERU", "PHILIPPINES", "POLAND", "PORTUGAL", "QATAR", "ROMANIA",
        "RUSSIA", "SAUDIARABIA", "SINGAPORE", "SLOVAKIA", "SLOVENIA",
        "SOUTHAFRICA", "SPAIN", "SRILANKA", "SWEDEN", "SWITZERLAND",
        "THAILAND", "TURKEY", "UKRAINE", "URUGUAY", "VENEZUELA", "VIETNAM",
        "YEMEN", "ZAMBIA", "ZIMBABWE"
    ]



    country=random.choice(country_name)
    word_length=len(country)
    cond=False
    life= 6

    display=[]
    for _ in range(word_length):
        display+= '_'

    print(f'The country  has {word_length} letters : {' '.join(display)}')
    print(f' LIVES  : {life} ')
    while not cond:
        guess=input('Guess a letter : ').upper()
        
        if guess in display:
            print(f'YOU HAVE ALREDY GUESSED THE LETTER "{guess}"')
        
        for position in range(word_length):
            if guess == country[position]:
                display[position]=guess
               
        if display.count('_')==0:
            print('YOU WIN!')
            cond=True
       
        if guess not in country:
            life=life-1
            print(HANGMAN[life])
            print(f'THE LETTER "{guess}" IS NOT IN THE WORD')
            
            print(f'LIVES left : {life} ')
          
            
            if life==0:
                print('YOU LOST')
                print(f'Correct word was "{country}"')
               
                print('GAME OVER')
                cond=True
        
                
        print(f'{' '.join(display)}')  


while not conti==True :
    game()
    play_again=input('PLAY AGAIN ?(yes/no) : ').lower()
    if play_again=='yes':
        play_again='a'
    elif play_again=='no':
        conti=True
        print('THANK YOU!')   
