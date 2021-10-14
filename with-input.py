#Program with input restaurantID 

import json
f = open('foodyo_output.json')
data = json.load(f)
resid = input("Enter the Restaurant ID : ")
for RestaurantName in data["body"]["Recommendations"]:
    
    if(RestaurantName["RestaurantID"] == resid):
        print(RestaurantName["RestaurantName"] )
        for menu in RestaurantName["menu"]:
            if(menu["type"] == "sectionheader"):
                for item in menu["children"]:
                    if(item["type"] =="item" and item["selected"] == 1):
                        print("--> "+item["name"])
                        for child1 in item["children"]:
                            if(child1['selected'] == 1 ):
                                print("------> "+child1["name"])
                                for child1_1 in child1["children"]:
                                    if(child1_1['selected'] == 1 ):
                                        print("----------> "+child1_1["name"])
                                        for child1_2 in child1_1["children"]:
                                            if(child1_2['selected'] == 1 ):
                                                print("---------------> "+child1_2["name"])
                                                for child1_3 in child1_2["children"]:
                                                    if(child1_3['selected'] == 1 ):
                                                        print("-------------------> "+child1_3["name"])

        

                    
f.close()