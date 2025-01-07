# Defining variable and defining it as true
torch_lit = True
if torch_lit == True:
    # We are wiritng an if statment . If torch_lit is True, We want the print statment to run
    print("venture forth into the cave!")

    weather = "sunny"
    print ("Tome for a picnic!")

    gold_coins = 10
    silver_coins = 50
    if gold_coins > 5 and silver_coins > 30:
        print("Enough to buy the magic potion!")
    else:
        print("You do not have enough")

    income = 4000
    expenses = 4500
    savings = income - expenses
    if savings > 1000:
            print("Great job! You saved a lot this month!")
    elif savings <= 0:
         print ("Looks like you've spent all or more than you earned!")
    else:
         print("Every little bit counsts! Keep saving.")

jet = "fast"
print("jet")

is_sunny = False
have_money = True

if is_sunny and not have_money:
     print("Great day for a walk in the park!")
else:
     print("print consdier indoor activities or saving for a sunny outing.")

is_friendly = False
has_quest = True

if not is_friendly:
     print(" Be cautious! This chracther might not be helpful")
elif has_quest:
     print("This characther has a questf for you")
else:
     print("Just a regualr villager passign by.")
