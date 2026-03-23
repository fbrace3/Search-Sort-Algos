#restaraunt chooser / decision maker
from random import choice as c

def decisionMaker(decisions, iterations):

    # create array with 'iteration' number of random choices
    arr = [c(decisions) for x in range(iterations)]

    #create a count dictionary to keep track of the number of each choice
    count = {}
    for _ in arr:
        count[_] = count.get(_, 0) + 1
    
    print(f"\nThe count is: {count}")

    ordered = max(count.items(), key=lambda item: item[1])
    return ordered, count


def main():
    choices = []
    x = ''

    while x != 'done':
        x = input("Enter a choice for consideration    (Enter 'done' when finished):")
        x = x.lower()
    

        if x in choices:
            print("choice is already in the decision tree, try again")
        elif x == '':
            continue
        if x not in choices and x != 'done':
            choices.append(x)
            print(choices)
        
    
    print(f"\nHere are the choices we will be deciding from: {choices}\n")
    num = input("Whats the sample size? (1 to 1000): \n")

    y = decisionMaker(choices, int(num))
    percent = (y[0][1] / int(num)) * 100
    print(f"\nThe final choice is: {y[0][0]}, with {y[0][1]} counts. \nIt represents {percent}% of the sample\n")
    # for x in y[1].items():
    #     print(x)

if __name__ == "__main__":
    main()