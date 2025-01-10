#DeJanae Faison Assignment 1.3 DATE
#"100 Bottles of beer"
#Prompt user to enter a number, and the program will count down 

#Ask user to input number, set to interger
beerBottles = int(input("Enter a number of beer bottles: "))
print("***********")
#Start loop while number is bigger than 1
while beerBottles > 0:
    #print the start of the song with given number
    print(f"{beerBottles} bottles of beer on the wall, {beerBottles} of beer.")
    #print message but subtract 1 from the input
    print(f"Take one down, pass it around, {beerBottles-1} bottle(s) of beer on the wall")
    #set variable of beerBottles-1
    beerBottles -= 1

    #If the variable reaches 1, we want the message to change as it reaches 1
    if beerBottles == 1:
     print(f"{beerBottles} bottle of beer on the wall, {beerBottles} bottle of beer.")
     #print message but subtract 1 from the input
     print(f"Take one down, pass it around, {beerBottles-1} bottle of beer on the wall")
     #set variable of beerBottles-1
     beerBottles -= 1

#Breaks loop since its now less than 0
#When there is no more, print message
print("Time to buy more beer!")