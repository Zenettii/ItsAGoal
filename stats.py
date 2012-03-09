from csv import DictReader
theReader = DictReader(open('Squad-Attributes-18-Feb-2012.csv'),delimiter=',')
idDict,substats,stats = {},{},{}
count = 0
#date = '08032012'#change this to user input
menu = ('(1) Import stats files','(2) Show ID and names',
        '(3) View stats of player')
userMenu = ''

for lineDict in theReader:
    substats[count] = lineDict#obtain all the stats from each line
    idDict[count] = lineDict['Name']#These two lines will move 
    lineDict.pop('Name')#the name and ID into idDict
    stats[count] = substats[count]# Put a copy into stats, each copy of stats are linked to player ID
    count += 1

#THIS IS FOR TESTING PURPOSE#
#print(idDict)
#for item in stats:
#    print(idDict[item],"stats: ",stats[item],"\n")
#THIS IS FOR TESTING PURPOSE#

while userMenu != 'q':
    for item in menu:
        print(item)
    userMenu = input("\nPlease enter choice: ")

    if userMenu == '1':
        print("Not yet setup, but we'll ask for file name to import")
    if userMenu == '2':
        print("ID\t\tName")
        for ids in idDict:
            print(ids,"\t\t",idDict[ids])
        print("\n\n")
    if userMenu == '3':
        ids = int(input("Please enter ID of player: "))
        for item in stats[ids]:
            print(item,":",stats[ids][item])
        print("\n\n")


