# Jingyi Fang , allysonf@usc.edu
# ITP 115, Spring 2020
# Assignment 1
# Description: This program creates a Mad Libs story. Users put inputs and this program generates outputs.


def main():
    animal = input("Enter an animal")
    adjective = input("Enter an adjective")
    number = input("Enter a number")
    verb = input("Enter a verb")
    number2 = int(input("Enter a second number"))
    number3 = int(input("Enter a third number"))
    number4 = int(number2 + number3)
    number5 = input("Enter a decimal number")
    name = input("Enter a name")
    verb2 = input("Enter another verb (-ing)")




    print("Today I went to see "+ "\"" + animal + "\"." + " They are very " + "\"" + adjective + "\".")
    print("I learned that they need to " + "\"" + verb + "\"" " at least " "\"" + number + "\"" + " hours per day.")
    print("Initially, I saw "+ "\"" + str(number2) + "\"" +" \"" + animal + "\".")
    print("After a while, " + "\"" + str(number3) + "\"" + " more came.")
    print("Overall, there are "+ "\"" + str(number4) + "\""+ " \"" + animal + "\".")
    print("According to the zoo keeper, in total, they eat "+ "\"" + number5 + "\"" + " kilos of bamboo per day!")
    print("The name of one of them is "+"\"" + name + "\".")
    print("He is currently "+ "\"" + verb2 + "\".")


main()
