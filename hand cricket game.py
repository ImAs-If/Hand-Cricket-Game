import random as rd
score =0
while True:
    player_1= int(input("Player_1:"))
    player_2=rd.randint(1,7)
    if player_1 >7 or player_1 < 1:
        print("Please,Enter valid value ( 1 to 7 )")
        continue

    else:
        if player_1!= player_2:
            score+=player_1
            print(player_2)
        else:
            print(player_2)
            print("OUT!!!!!!")
            break

print("Your score is:",score)