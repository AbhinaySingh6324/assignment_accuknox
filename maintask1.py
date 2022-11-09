import sys
from collections import defaultdict
def task1(*args):
    return main(sys.argv[1])
def main(filename):
    file = open(filename, "r")

    dict_items_for_top_3 = defaultdict(int)
    namedict = defaultdict(int)
    eater_map = set()
    count_orders = 0
    for line in file:
        linestrip = line.strip().split(" ")

        date = linestrip[0]
        time = linestrip[1]
        type = linestrip[2]
        foodmenu_id = linestrip[3]
        eater_id = linestrip[4]
        itemname = linestrip[5] + " " + linestrip[6]
        # print (itemname)
        namedict[int(foodmenu_id)] = itemname

        dict_items_for_top_3[(int)(foodmenu_id)] += 1
        count_orders += 1
        eater_map.add(eater_id)
    newli = sorted(dict_items_for_top_3.items(), key=lambda x: x[1], reverse=True)

    # flag = 0
    # for j,itr in eater_map.items():
    #     if len(set(itr))!=len(itr):
    #         flag=1

    if count_orders > len(eater_map):

        print("___________________Something Went Wrong________________________________")
        print("Multiple Orders detected")
        return False
    else:
        print("___________________Top Selling 3 Items________________________________")
        for i, j in newli[:3]:
            print(i, namedict[i], j)
        return True
    file.close()




if __name__ == "__main__":
    a = task1()

