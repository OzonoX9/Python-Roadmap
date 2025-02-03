#If Statement
total = 100
country = "US"
if country == "US":
    if total <= 50:
        print("Shipping Cost is  $50")
    elif total <= 100:
        print("Shipping Cost is $25")
    elif total <= 150:
        print("Shipping Costs $5")
    else:
        print("FREE")
if country == "AU":
    if total <= 50:
        print("Shipping Cost is  $100")
    else:
        print("FREE")
        
#Switch Statement
def SwitchExample(argument):
    switcher = {
        0: " This is Case Zero ",
        1: " This is Case One ",
        2: " This is Case Two ",
    }
    return switcher.get(argument, "nothing")

if __name__ == "__main__":
    argument = 1
    print (SwitchExample(argument))