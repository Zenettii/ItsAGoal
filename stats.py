from csv import DictReader
theReader = DictReader(open('Squad-Attributes-18-Feb-2012.csv'),delimiter=',')
idDict,substats,stats = {},{},{}
count = 0
date = '08032012'#change this to user input

for lineDict in theReader:
#    if count == 0:
    substats[count] = lineDict
    idDict[count] = lineDict['Name']
    stats[count] = substats[count]
    count += 1

print(idDict)
for item in stats:
    print(idDict[item],"stats: ",stats[item],"\n")


