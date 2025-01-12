#DeJanae Faison  2.2 Assignment 
#Debugging Assignment
def dogs():
    #List of Dog Breeds
    dogsTuple=('Bulldog','Beagle','Rottweiler','Dachshund','Poodle','Chihuahua',
    'Great Dane', 'Maltese','Chow Chow', 'Afghan Hound','Boxer','St Bernard','Basset Hound',
    'Shiba Inu','Doberman','Samoyed','Yorkie','Cocker Spaniel','Corgi','Bichon')
    
    #User Input view list
    start=(input("Want to view a list of Dog Breeds? Y or N "))
    start=start.upper()
    #if user says y, display single statement of dogs
    if start == 'Y':
        #the blank prints are for line breaks to be more readable
        print()
        #places a comma between each breed
        print(' , '.join(dogsTuple))
        print()
        reverselist=(input("Lets put them in reverse shall we? Y or N "))
        reverselist=reverselist.upper()
        if reverselist == 'Y':
            #tuples dont support the reverse function so it has to be converted to a list
            dog_list=list(dogsTuple)
            #sorts the list in descending order
            dog_list.sort(reverse=True)
            #enumerate counts the objects in the list
            #index starts at 0 so it needs to indicate starting at 1
            for i, value in enumerate(dog_list, start= 1):
                print(f"{i}. {value}")
        
dogs()