#Brenna Kieft
lemon_cake={"egg":2,"sugar":1,"butter":1,"vanilla":2,"flour":2,"milk":1,"baking powder":2,"lemon":1}
red_velvet={"egg":3,"flour":2,"cocoa powder":2,"salt":4,"butter":1,"vegetable oil":1, "vanilla":2,"sugar":2 }
def cake():
    match = []
    x = red_velvet
    y = lemon
    for ingredient in x:
        if ingredient in y:
          match.append(ingredient)
    print(match)
cake()
