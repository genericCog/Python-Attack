import random

myHealth = 100
monsterHealth = 100

print("A monster has appeared!")

while True:
    print("Monster's health:",monsterHealth)
    print("My health:",myHealth)

    myAttack = random.randint(7,12)
    myHeal = random.randint(5,15)
    monsterAttack = random.randint(7,12)
    monsterHeal = random.randint(5,15)

    if myHealth <= 0 or monsterHealth <= 0:
        print("GAME OVER")
        break
    else:
        monsterMove = random.randint(1,2)

        if monsterMove == 1:
            print("MONSTER ATTACKS FOR",monsterAttack,"POINTS!")
            myHealth = myHealth - monsterAttack
        elif monsterMove == 2:
            print("MONSTER HEALS FOR",monsterHeal,"POINTS!")
            monsterHealth = monsterHealth + monsterHeal
            if monsterHealth > 100:
                monsterHealth = 100

        print("Monster's health:",monsterHealth)
        print("My health:",myHealth)

    if myHealth <= 0 or monsterHealth <= 0:
        print("GAME OVER")
        break
    else:
        print("My moves:")
        print("1: Attack. Attacks the monster for 7 to 12 damage")
        print("2: Heal. Heals us for 5 to 15 points")

        myMove = eval(input("What would you like to do? Press 1 or 2."))

        if myMove == 1:
            print("YOU ATTACK FOR",myAttack,"POINTS!")
            monsterHealth = monsterHealth - myAttack
        elif myMove == 2:
            print("YOU HEAL YOURSELF FOR",myHeal,"POINTS!")
            myHealth = myHealth + myHeal
            if myHealth > 100:
                myHealth = 100
    
