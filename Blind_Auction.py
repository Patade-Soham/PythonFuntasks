

print('welcome to the blind auction')
auction={}
bigger_bid=[]
def game(name, bid):
    auction[name]=bid

while True:
    a=input('Write your name : ')
    b=int(input('Give your bid : '))
    game(a, b)
    bidders=input('Are there any other biders? (yes/no)')
    if bidders=='yes':
        continue
    else:
        break
for key in auction:
    bigger_bid.append(auction[key])
bigger_bid.sort()
bigger_bid.reverse()

highest_bid=bigger_bid[0]
winner=''
if highest_bid==auction[key]:
    winner=key
print(winner)

    
