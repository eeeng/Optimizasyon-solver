#i
 #var='k' or'k1'

N=[1,2,3]

cost = lambda C,F: 10000//C * 2 * F * 100

#ii 
def transCost(C,F):
    cost(C, F)
    print(f"{C} {F} \ncost={cost}")   
    return cost
        
print("cost = 10000 / C * 2 * F * 100")

while(1):    
    for k in N:    
        if N[0] == 1:
            cost0 = cost(10000,4)
            print("", N[0],"\t \t", cost0, "\n",
                  "{} {}".format(10000, 4))
          
               
        if N[1] == 2:
                # k+=1
            cost1 = cost(2000, 3)
            print("", N[1], "\t \t", "{} {}".format(2000, 3), "\n",
                  "{} {}".format(1000,8), "",cost1, "\n",
                  "{} {}".format(2000,3))
            
         
        if N[2] == 3:
                # k+=1
            cost2 = cost(100, 6)
            print("", N[2] , "\t \t", "{} {}".format(100, 6), "\n",
                  "{} {}".format(50, 4), "\t", cost2, "\n", 
                  "{} {}".format(100, 8) , "\n",
                  "{} {}".format(100, 6))
            continue
#iii
                                       
            #input("N: ")
            if N[0]==1:                
                print("", N[0],"\t \t", cost0, "\n",
                      "{} {}".format(10000, 4))
                
                
            else:    
                print("", N[0], "\t \t", "{} {}".format(2000, 3), "\n",
                      "{} {}".format(1000,8), "",cost1, "\n",
                      "{} {}".format(2000,3))

            
            break
    break
