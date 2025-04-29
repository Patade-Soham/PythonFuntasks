import random
import os
data = [
    {'name': 'Bali', 'searches': 18410491, 'description': 'Tourist island', 'country': 'Indonesia'},
    {'name': 'Baseball', 'searches': 27687921, 'description': 'Sport', 'country': 'United States'},
    {'name': 'Spider-Man', 'searches': 32909642, 'description': 'Superhero movie', 'country': 'United States'},
    {'name': 'Lionel Messi', 'searches': 174319593, 'description': 'Footballer', 'country': 'Argentina'},
    {'name': 'Avengers: Endgame', 'searches': 38121662, 'description': 'Superhero movie', 'country': 'United States'},
    {'name': 'PS5', 'searches': 53752493, 'description': 'Gaming console', 'country': 'Japan'},
    {'name': 'Tom Holland', 'searches': 42214008, 'description': 'Actor', 'country': 'United Kingdom'},
    {'name': 'MacBook', 'searches': 33607244, 'description': 'Laptop', 'country': 'United States'},
    {'name': 'Dwayne Johnson', 'searches': 48616777, 'description': 'Actor', 'country': 'United States'},
    {'name': 'Emma Watson', 'searches': 31800133, 'description': 'Actress', 'country': 'United Kingdom'},
    {'name': 'AirPods', 'searches': 26392684, 'description': 'Earbuds', 'country': 'United States'},
    {'name': 'Football', 'searches': 79421763, 'description': 'Global sport', 'country': 'International'},
    {'name': 'Tesla Model 3', 'searches': 13477487, 'description': 'Electric car', 'country': 'United States'},
    {'name': 'Serena Williams', 'searches': 32929120, 'description': 'Tennis player', 'country': 'United States'},
    {'name': 'Oppenheimer', 'searches': 39558435, 'description': 'Biopic film', 'country': 'United States'},
    {'name': 'WWE', 'searches': 37936039, 'description': 'Wrestling entertainment', 'country': 'United States'},
    {'name': 'LeBron James', 'searches': 58159437, 'description': 'Basketball player', 'country': 'United States'},
    {'name': 'New York', 'searches': 28121191, 'description': 'Major city', 'country': 'United States'},
    {'name': 'Taylor Swift', 'searches': 61670265, 'description': 'Singer-songwriter', 'country': 'United States'},
    {'name': 'Kylie Jenner', 'searches': 59950499, 'description': 'Media personality', 'country': 'United States'},
    {'name': 'Cricket', 'searches': 81252639, 'description': 'Popular in Asia', 'country': 'International'},
    {'name': 'F1', 'searches': 42159753, 'description': 'Motor racing', 'country': 'International'},
    {'name': 'Game of Thrones', 'searches': 26368245, 'description': 'TV series', 'country': 'United States'},
    {'name': 'Paris', 'searches': 29765520, 'description': 'Capital city', 'country': 'France'},
    {'name': 'Neymar', 'searches': 29845601, 'description': 'Footballer', 'country': 'Brazil'},
    {'name': 'Roger Federer', 'searches': 38847142, 'description': 'Tennis player', 'country': 'Switzerland'},
    {'name': 'Elon Musk', 'searches': 103217224, 'description': 'Entrepreneur', 'country': 'United States'},
    {'name': 'Dubai', 'searches': 29409457, 'description': 'Tourist destination', 'country': 'UAE'},
    {'name': 'London', 'searches': 22131812, 'description': 'Capital city', 'country': 'United Kingdom'},
    {'name': 'Barbie', 'searches': 39129552, 'description': 'Fantasy movie', 'country': 'United States'},
    {'name': 'Samsung Galaxy', 'searches': 22410556, 'description': 'Smartphone', 'country': 'South Korea'},
    {'name': 'Basketball', 'searches': 65589624, 'description': 'Sport', 'country': 'United States'},
    {'name': 'MS Dhoni', 'searches': 42170327, 'description': 'Cricketer', 'country': 'India'},
    {'name': 'Virat Kohli', 'searches': 59659549, 'description': 'Cricketer', 'country': 'India'},
    {'name': 'Tokyo', 'searches': 27746463, 'description': 'Capital city', 'country': 'Japan'},
    {'name': 'The Batman', 'searches': 37081883, 'description': 'DC movie', 'country': 'United States'},
    {'name': 'Kim Kardashian', 'searches': 46925445, 'description': 'TV personality', 'country': 'United States'},
    {'name': 'Hockey', 'searches': 21540411, 'description': 'Sport', 'country': 'Canada'},
    {'name': 'Maldives', 'searches': 21099653, 'description': 'Tourist country', 'country': 'Maldives'},
    {'name': 'Breaking Bad', 'searches': 34415360, 'description': 'TV series', 'country': 'United States'},
    {'name': 'iPhone', 'searches': 121835081, 'description': 'Smartphone', 'country': 'United States'},
    {'name': 'Cristiano Ronaldo', 'searches': 193238350, 'description': 'Footballer', 'country': 'Portugal'},
    {'name': 'Avengers: Endgame', 'searches': 48215203, 'description': 'Superhero movie', 'country': 'United States'},
    {'name': 'Serena Williams', 'searches': 34783761, 'description': 'Tennis player', 'country': 'United States'},
    {'name': 'MacBook', 'searches': 37982017, 'description': 'Laptop', 'country': 'United States'},
    {'name': 'WWE', 'searches': 46805776, 'description': 'Wrestling entertainment', 'country': 'United States'},
    {'name': 'Tokyo', 'searches': 29442182, 'description': 'Capital city', 'country': 'Japan'},
    {'name': 'Neymar', 'searches': 28534299, 'description': 'Footballer', 'country': 'Brazil'},
    {'name': 'Basketball', 'searches': 61311779, 'description': 'Sport', 'country': 'United States'},
    {'name': 'Tom Holland', 'searches': 39362794, 'description': 'Actor', 'country': 'United Kingdom'},
    {'name': 'Roger Federer', 'searches': 35189347, 'description': 'Tennis player', 'country': 'Switzerland'},
    {'name': 'Dubai', 'searches': 27421695, 'description': 'Tourist destination', 'country': 'UAE'},
    {'name': 'Tennis', 'searches': 46582038, 'description': 'Sport', 'country': 'International'},
    {'name': 'Lionel Messi', 'searches': 175788347, 'description': 'Footballer', 'country': 'Argentina'},
    {'name': 'Barbie', 'searches': 40084599, 'description': 'Fantasy movie', 'country': 'United States'},
    {'name': 'New York', 'searches': 26029614, 'description': 'Major city', 'country': 'United States'},
    {'name': 'Paris', 'searches': 30572152, 'description': 'Capital city', 'country': 'France'},
    {'name': 'PS5', 'searches': 58434469, 'description': 'Gaming console', 'country': 'Japan'},
    {'name': 'Emma Watson', 'searches': 33226320, 'description': 'Actress', 'country': 'United Kingdom'},
    {'name': 'Tennis', 'searches': 54421725, 'description': 'Sport', 'country': 'International'},
    {'name': 'Samsung Galaxy', 'searches': 26333811, 'description': 'Smartphone', 'country': 'South Korea'},
    {'name': 'Dwayne Johnson', 'searches': 53428832, 'description': 'Actor', 'country': 'United States'},
    {'name': 'AirPods', 'searches': 31721584, 'description': 'Earbuds', 'country': 'United States'}
]

logo = """
    __  ___       __             
   / / / (_)___ _/ /_  ___  _____
  / /_/ / / __ `/ __ \/ _ \/ ___/
 / __  / / /_/ / / / /  __/ /    
/_/ ///_/\__, /_/ /_/\___/_/     
   / /  /____/_      _____  _____
  / /   / __ \ | /| / / _ \/ ___/
 / /___/ /_/ / |/ |/ /  __/ /    
/_____/\____/|__/|__/\___/_/     
"""
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')
def higher(one,two):
    if one['searches']>two['searches']:
        print(f"Bingo! {one['name']} is highly searched")
        return True
       
    elif one['searches']<two['searches']:
        print('you lose')
        return False
    else:
        print('uknown error occured')
def lower(one,two):
    if one['searches']<two['searches']:
        print(f"Bingo! {one['name']} is less searched")
        return True
    elif one['searches']>two['searches']:
        print('you lose')
        return False
    else:
        print('uknown error occured')
        return True
def function():
    score=0
    rec=True
    while True:
        
        lis=['Higher','Lower']
        task=random.choice(lis)

        a=random.choice(data)
        b=random.choice(data)
    
        if a!=b:
            print(f'''
                  A : {a['name']}, a {a['description']}, of {a['country']}
                  B : {b['name']}, a {b['description']}, of {b['country']} 
                  ''')
            if task == 'Higher':
                choice= input(f'Which of these has {task} searches : ').lower()
                if choice == 'a':
                    rec=higher(a, b)
                    if rec==True:
                        score=score+1
                        
                        print('score :',score)
                        continue
                    else:
                        print("Wrong!")
                        print(f"{a['name']}: {a['searches']}, {b['name']}: {b['searches']}")
                        print(f"Final score: {score}")
                        break
                    
                elif choice=='b':
                    rec=higher(b, a)
                    if rec==True:
                        score=score+1
                        
                        print('score :',score)
                        continue
                    else:
                        print("Wrong!")
                        print(f"{a['name']}: {a['searches']}, {b['name']}: {b['searches']}")
                        print(f"Final score: {score}")
                        break
                    
            elif task=='Lower':
                choice= input(f'Which of these has {task} searches : ').lower()
                if choice == 'a':
                    rec=lower(a, b)
                    if rec==True:
                        score=score+1
                        
                        print('score :',score)
                        continue
                    else:
                        print("Wrong!")
                        print(f"{a['name']}: {a['searches']}, {b['name']}: {b['searches']}")
                        print(f"Final score: {score}")
                        break
                elif choice=='b':
                    rec=lower(b, a)
                    if rec==True:
                        score=score+1
                        
                        print('score :',score)
                        continue
                    else:
                        print("Wrong!")
                        print(f"{a['name']}: {a['searches']}, {b['name']}: {b['searches']}")
                        print(f"Final score: {score}")
                        break
               

      
        elif a==b:
            continue
        clear_screen()

while True:
    
    print(logo)
    function()
    play=input('play again (y/n): ').lower()
    
    if play=='y':
        
        continue
    
    else:
        
        break
print('thank you')
    

