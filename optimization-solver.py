from scipy.optimize import minimize

var1 = 'C'
var2 = 'F'
mylist = {var1, var2}

var3 = 'N'


list_cf=[(50,4), (100,8), (1000,8), (2000,3), (100,6), (10000,4)]

i=[1,2,3,4,5]


    
def tasimaMaliyeti(C,F):
    cost = (10000 / C) * F * 2 * 100
    return cost

def tasimaMaliyeti2(C,F):
    cost = (10000 / C) * F * 2 * 100
    print("{C} {F} \ncost={cost}".format("C, F"))
    return cost


# input("C:")
# input("F:")

cost = lambda C,F: (10000 // C) * F * 2 * 100
   
# print(cost(10000,4), cost(2000, 3), cost(1000, 8), cost(100, 6), cost(50, 4))
#min değer {ii} için 3000 

print("results= ","\n",
      'cost(2000, 3): {}'.format(cost(2000, 3)),"\n", 
      'cost(100, 6): {}'.format(cost(100, 6)),"\n",
      'cost(10000, 4): {}'.format(cost(1000, 4)
                                  ))
#bu ifadeler için de seçim yapılabilirdi ama net görmek için tekrarladndı

Cx1=1000; Fx1=8
Cx2=50;   Fx2=4
Cx3=10000;Fx3=4



while(1):
    # kisitlamamak icin kapatildi
    # a= input("a:")
    # if (a == 1):
    #     print("basla")     
   
        if i[2] == 3:
            def tasimaMaliyeti(s_list):
                
                print( s_list,  cost(10000, 4), "\n" ,
                      "{} {}".format(Cx3, Fx3) 
                      )
        
                return
            
            
        s_list = [i[0]]
        # print("Fonksiyon çağrılmadan önce list: ", mylist)
        tasimaMaliyeti(s_list)
    
        
        #ii
        if i[0]==1:
            
            def minimum(C,F):
                cost(2000, 3)
                return minimize
            # minimum(2000,3)
            def tasimaMaliyeti(s_list):
                
                s_list.append(list_cf[3])
                print( s_list , "\n" ,"{} {}".format(Cx1, Fx1),
                      cost(2000, 3) , "\n",
                      "{} {}".format(2000, 3))
                return
            
            
        s_list = [i[1]]
        # print("Fonksiyon çağrılmadan önce list: ", mylist)
        tasimaMaliyeti(s_list)
        
        #iii
        if i[1]==2:
            
        
            def tasimaMaliyeti(s_list):
                
                s_list.append(list_cf[4])
                print( s_list , "\n" ,"{} {}".format(Cx2, Fx2),
                      cost(100, 6) , "\n", 
                      "{} {}".format(100, 8) , "\n",
                      "{} {}".format(100, 6))
                return
            
            def tasimaMaliyeti2(s1_list):
                if var3 == 1:
                    s1_list.append(cost(10000,4))
                
                else:
                    s1_list.append(cost(2000, 3))
                return
            s1_list = [i[0]]
            
        s_list = [i[2]]
        
        tasimaMaliyeti2(s1_list)
        tasimaMaliyeti(s_list)
    # else:
    #     print("islem yok")
   
        # kisitlamamak icin kapatildi
        # a= input("a:")
        # if (a == 0):
        #     print("islem yapma") 
        
 