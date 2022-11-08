from collections import defaultdict
f = open("Accuknox2.txt","r")
dict_items_for_top_3 = defaultdict(int)
namedict = defaultdict(int)
eater_map = set()
count_orders = 0
for line in f:
    linestrip  = line.strip().split(" ")
    # print(linestrip)
    date = linestrip[0]
    time = linestrip[1]
    type = linestrip[2]
    foodmenu_id = linestrip[3]
    eater_id = linestrip[4]
    itemname = linestrip[5]+" "+linestrip[6]
    # print (itemname)
    namedict[int(foodmenu_id)] = itemname
    # eater_map[int(eater_id)].append(int(foodmenu_id))
    # checking for the given application logic
    dict_items_for_top_3[(int)(foodmenu_id)]+=1
    count_orders+=1
    eater_map.add(eater_id)
newli= sorted(dict_items_for_top_3.items(), key=lambda x:x[1],reverse=True)

# flag = 0
# for j,itr in eater_map.items():
#     if len(set(itr))!=len(itr):
#         flag=1
print("___________________Top Selling 3 Items________________________________")
for i,j in newli[:3]:

    print(i,namedict[i],j)
f.close()
print("___________________________MULTIPLE ORDERS EDGE CASE____________________")
f = open("Accuknox3.txt","r")
dict_items_for_top_3 = defaultdict(int)
namedict = defaultdict(int)
eater_map = set()
count_orders = 0
for line in f:
    linestrip  = line.strip().split(" ")
    # print(linestrip)
    date = linestrip[0]
    time = linestrip[1]
    type = linestrip[2]
    foodmenu_id = linestrip[3]
    eater_id = linestrip[4]
    itemname = linestrip[5]+" "+linestrip[6]
    # print (itemname)
    namedict[int(foodmenu_id)] = itemname
    # eater_map[int(eater_id)].append(int(foodmenu_id))
    # checking for the given application logic
    dict_items_for_top_3[(int)(foodmenu_id)]+=1
    count_orders+=1
    eater_map.add(eater_id)
newli= sorted(dict_items_for_top_3.items(), key=lambda x:x[1],reverse=True)

# flag = 0
# for j,itr in eater_map.items():
#     if len(set(itr))!=len(itr):
#         flag=1
if count_orders>len(eater_map):
    print("___________________Something Went Wrong________________________________")
    print("Multiple Orders detected")
f.close()




