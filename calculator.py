person1 = 100
person2 = 100
percHigh = 0
percLow = 0


counter = 0

while counter < 365:
    
    persHigh = person1 + (person1 * 0.01)
    person1 = persHigh;

    persLow = person2 - (person2 * 0.01)
    person2 = persLow
    
    
    counter = counter + 1
else:
    print("If I improve 1% Everyday: ", persHigh, "XP")
    print("If I get 1% Worse Everyday: ", persLow, "XP")

