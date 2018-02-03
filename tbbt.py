import random
matchups = [("Rock","Scissors"),("Scissors","Paper"),("Paper","Rock"),("Rock","Lizard"),("Lizard","Spock"),("Spock","Scissors"),("Scissors","Lizard"),("Lizard","Paper"),("Paper","Spock"),("Spock","Rock")]
game =['Rock','Paper','Scissors','Spock','Lizard']
opt = random.choice(game)
myscore = 0
compscore = 0
print ("Rock/Paper/Scissors/Spock/Lizard  or quit game ?")
myopt = raw_input(("Choose your option"))
while myopt != "quit":

    if myopt == opt:
        print'I chose:',opt,'you chose:',myopt,'It is a TIE'
    elif (opt, myopt) in matchups:
        print'I chose:',opt,'you chose',myopt,"I win"
        compscore+=1;
    elif (myopt, opt) in matchups :
        print'I chose:',opt,'::you chose:',myopt,"::You win"
        myscore+=1;
    else:
        print 'I did not understand. Pls choose one of the five'
        pass
    print ("Rock/Paper/Scissors/Spock/Lizard  or quit game ?")
    myopt = raw_input(("Choose your option"))
    opt = random.choice(game)
print('Computer has Scored : ',compscore)

print ('You have Scored : ',myscore)