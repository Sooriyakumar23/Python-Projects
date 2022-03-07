##### Turtle Race #####

# 1. Getting player choices
n = int(input("Enter the racers you want to battle: "))
guess = int(input("Enter your guess, who's gonna be the winner: "))

if n > 1 and type(n)==int:
    if type(guess)==int and 1<=guess and guess<=n:
        # 2. Importing necessary libraries
        from turtle import *
        import random
        
        # 3. Staging
        penup()
        color('black')
        setpos(300,250)
        pendown()
        setpos(300,-250)
        color('red')
        setpos(-300,-250)
        color('black')
        setpos(-300,250)
        color('green')
        setpos(300,250)
        hideturtle()
        print ("Stage is ready !")

        # 4. Assigning colors to each players
        rand_colors = []
        for j in range(n):
            rand_colors.append(["#"+''.join([random.choice('ABCDEF0123456789') for i in range(6)])])

        # 5. Calling competitors
        racers = []
        for i in range(n):
            r = Turtle()
            r.penup()
            r.setpos(600//(n-1)*i-300, -250)
            r.color(rand_colors[i])
            r.pendown()
            r.left(90)
            racers.append(r)

        # 6. Race..... Start !
        print ("Race started..... Here we go!")
        boolean = True
        while boolean:
            for i in range(n):
                c = racers[i]
                if c.pos()[1] < 250:
                    c.forward(random.randint(0,10))
                else:
                    boolean = False
                    print (f"Racer {i+1} won the match")
                    if guess == i+1:
                        print ("Congratulations, Your guess is correct !")
                    else:
                        print ("Sorry, you didn't get this time. Better luck next time.....")
    else:
        print ("Please check your guess of the winner")
else:
    print ("Please check your number of racers")
