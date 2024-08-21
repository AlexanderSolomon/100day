import random
import gameData
import art
"""I shall make it so the list does not get smaller and they can potentially get the same person twice otherwise it needs to pop from the dictionary and get smaller"""


print(art.logo)


# set locations to be swaped for names and numbers
infoA = []
infoB = []

followerCountA = 0
followerCountB = 0


# Create a score counter
score = 0 

# Chances to guess = 1

      

# a function that create 2 random numbers from list
def find2randoms():
    global followerCountA,followerCountB, infoA, infoB
    x = random.randint(0,49)
    y = random .randint(0,49)
    
    n1 = gameData.data[x]
    n2 = gameData.data[y]
    
    infoA.append(n1)
    infoB.append(n2)
    
    followerCountA = gameData.data[x].get("follower_count")
    followerCountB = gameData.data[y].get("follower_count")
    
    
    # print(gameData.data[x].get("name"))
    # print(gameData.data[x].get("follower_count"))
    
    # print(gameData.data[y].get("name"))
    # print(gameData.data[y].get("follower_count"))

#get new random in B place
def bRandon():
    global followerCountB, infoA, infoB
    x = random.randint(0,49)
    b = gameData.data[x]
    infoB.append(b)
    followerCountB = gameData.data[x].get("follower_count")
    
    

def vursus():
    global score
    print({infoA[0].get("name")})
    #print(followerCountA)
    
    print(art.vs)
    
    print({infoB[0].get("name")})
    #print(followerCountB)
    
    

# while chances guess option
def gamestart():
    global score,followerCountB, followerCountA
    chances = True 
    while chances == True:
        vursus()
        
        if followerCountA > followerCountB:
            #print("A is larger")
            a = "a"
        else:
            a = "b"
    
        answer = input("Who has more followers A or B").lower()
        # clear and renew while correct answer
        if answer == a:
            # add score
            score = score+1
            print(f"your score: {score} ")
            # create a function that replaces a and holds the new a b
            #print(followerCountA)
            followerCountA = followerCountB
            #print(followerCountA)
            infoA.clear()
            infoA.append(infoB[0])
            #print(infoA)
            infoB.clear()
            bRandon()
            
            
        else:
            print(f"you loose")
            chances = False
            
            
        
   
def replaceAandNewB():
    global infoA, infoB
    infoA.clear()
    infoA.append(infoB[0])
    infoB.clear()
    print(f"this is now location A: {infoA}")
    print(infoB)
    






#print(infoA)
#print(infoB)
#print(followerCountA)
#print(followerCountB)
find2randoms()
gamestart()
print(f"current score {score}")




# print(followerCountA)
# print(followerCountB)
# print(infoA)
# print("just name")
# print({infoA[0].get("name")})
# print(infoB)




#after guess remove b and insert to A



# create placements of the 2 values


# create replacements


# selecet value A or B as being the higher value 


# compare the 2 values selected
    








# get a random value from the dictionary
# x = random.randint(0,50)
# print(x)
# print(gameData.data[1].get("follower_count"))
# print(gameData.data[x].get("follower_count"))
# print(gameData.data[x])


# get random names from dictionary and vs art between them







