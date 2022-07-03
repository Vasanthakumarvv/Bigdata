complextup=[(1,
            "Madison's Family",
            [{"gender":"male","Relation":"self","personalinfo":{"title":"Ms","name":"Madison"}},
             {"gender":"female","Relation":"spouse","personalinfo":{"title":"Mrs","name":"Elisa"}},
             {"gender":"female","Relation":"daughter","personalinfo":{"title":"Miss","name":"Hanna","hobby":"book reading"}},
             {"gender":"male","Relation":"son","personalinfo":{"title":"Master","name":"Dave","schooling":True}}]),
           (2,
            "Vasanth's Family",
            [{"gender":"male","Relation":"self","personalinfo":{"title":"Ms","name":"Madison"}},
             {"gender":"female","Relation":"spouse","personalinfo":{"title":"Mrs","name":"Elisa"}},
             {"gender":"female","Relation":"daughter","personalinfo":{"title":"Miss","name":"Hanna","hobby":"book reading"}},
             {"gender":"male","Relation":"son","personalinfo":{"title":"Master","name":"Dave","schooling":True}}])]

for i in complextup:
    if(i[0]==2):
        for j in i[2]:
            print("jvalue",j)
            if j['Relation']=='son':
                if j['personalinfo'] ['schooling']:
                    print(i[2][0]['personalinfo']['name'])












#Two ways to print a list or any collection item
lst=[(1,2,3),(4,5,6),(7,8,9)]
#1.Using the index
for i in range(len(lst)):
    if(i==0):
        continue
        print(lst[i])
    else:
        print(lst[i])

#2.Using the list values
for i in lst:
    print(i)

lst=["asas","bbbb","ccc"]
#1.Using the index
for i in range(len(lst)):
    if(i==0):
        continue
        print(lst[i])
    else:
        print(lst[i])


# for i in lst:
#     print("index {} and value {}".format(index,i))






# print("id is "+str(complextup[0]))
# print("Family name is " + str(complextup[1]))
# print("gender of first list element is " + complextup[2][0]["gender"])
# print("relation of first list element is " + complextup[2][0]["Relation"])
# print("personalinfo of the first list element is " + str(complextup[2][0]["personalinfo"]))
# print("personalinfo title of the first list element is " + str(complextup[2][0]["personalinfo"]["title"]))
# print("personalinfo name of the first list element is " + (complextup[2][0]["personalinfo"]["name"]))
# print("personalinfo name of the second list element is " + str(complextup[2][1]["personalinfo"]["name"]))
# print("personalinfo hobby of the third list element is " + str(complextup[2][2]["personalinfo"]["hobby"]))
# print("personalinfo schooling info of the fourth list element is " + str(complextup[2][3]["personalinfo"]["schooling"]))