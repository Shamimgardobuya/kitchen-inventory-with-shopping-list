print("This is the store of Mugato Kitchen,it contains foodstuff for the list for this week")
# Oils=[{"Kimbo":14},{"Elianto":12}]

goods=[{"Oils":{"Kimbo":14,"Elianto":12}},{"Cereals":{"Maize":34,"Rice 4kgs":23}},{"Flour":{"Jembe":12,"Ajab":24,"Butterfly":23}}]
print(f"{goods}")
# Cereals=[{"Maize":34},{"Rice 4kgs":23}]
# Flour=[{"Jembe":12},{"Ajab":24},{"Butterfly"}]
z="yes" or "no"
addition={}
purple=str(input("Do you wish to add a new item to the store"))
if purple=="yes":
    new_item=str(input("Enter a new item "))
    number=int(input(f"How many numbers of {new_item} would you like to add "))
    addition[new_item]=number
    goods.append(addition)
    print(f" here are your new goods and updated {goods}")

    
elif purple=="no" or  "no":
    taking=str(input("Would you like to take an item instead? "))
    if taking=="yes":
        item_ing=str(input("Which item would you like to take "))
        if item_ing=="Rice" or "rice" or"want rice":
            numberings=int(input("how many 4kgRice do you need? "))
            if numberings>goods[1]["Cereals"]["Rice 4kgs"]:
                print({goods[1]["Cereals"]['Rice 4kgs']},"are the 4kgsRice bags of  food left")
            elif numberings<goods[1]["Cereals"]["Rice 4kgs"]:
                z=goods[1]["Rice 4kgs"]=23-numberings
                
                print(f"You have taken {numberings},the new number of 4kgRice bags is {z}")
                print(goods)
                item_ing=str(input("Which item would you like to take "))
                numberings=int(input("how many 4kgRice do you need? "))
            elif numberings<goods[1]["Cereals"]["Rice 4kgs"]:
                z=goods[1]["Rice 4kgs"]=23-numberings
                print(f"You have taken {numberings},the new number of 4kgRice bags is {z}")
                
            if goods[1]["Rice 4kgs"]==5:
                print("The number of 4kg Rice is less stock")
                amount=int(input("How many bags of Rice do you wish to buy? "))
                shopping_list=[]
                shopping_list.append({"Rice":amount})
                print(f"Here is your shopping list {shopping_list}")
                
                
#want to create a shopping list 
#when number of value of goods reach five append the key to list.
#create an empty list and use rice as an example. 
#prob,dictionary is not updated it uses the original value of dictionary.
#are we gonna repeat  our code.
#append the rice and value needed.





    
    


#find items
#using dictionaries inside lists
#Dictionary has keys of the name of items with value as the number
#Store each item
#if items needed  reduce value and update list.
            # def likes(names):
            #     x=0
            #     while x<len(names):
            #         if len(names)==0:
            #             print("no one likes this")
            #         elif len(names)>0:
            #                 x+=1
            #                 print(f"{names[x]}  likes this ")
                            
            # likes(["John","Jame","Eunice"])
#updating list
#want to add a value to my stock
#3Bags of tomatoes
#write origin list and append the dictionary of tomatoes//
#had to make sure i had a main list that would append the item
#variables became the key and under values a new dictionary with a sub item like elianto with its own value
#assign value of the dictionart
#Reducing value from item
#Request input from user the main item they want 
#condition it to be the 
#decrease value by subtracting the value.access index then key then value






