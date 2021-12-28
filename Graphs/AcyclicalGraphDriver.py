import csv
import Graph


classes = {}
class2num = {}
num2class = {}
with open('SimpleAcylicalGraphData.csv', newline='', encoding='utf-8-sig') as csvfile:
	filereader = csv.reader(csvfile, delimiter=',')
	# Skip the header
	next(filereader)
	for row in filereader:
		# Count unique city first
		if row[0] not in class2num:
			label = int(len(class2num))
			class2num[row[0]] = label
			num2class[label] = row[0]
		if row[1] not in class2num:
			label = int(len(class2num))
			class2num[row[1]] = label
			num2class[label] = row[1]

		temp = (row[1], int(row[2]))
		if row[0] not in classes:
			classes[row[0]] = [temp]
		else:
			classes[row[0]].append(temp)

schedule = Graph.Graph(len(class2num))
for key in classes:
	v1 = class2num[key]
	pairs = classes[key]
	for pair in pairs:
		v2 = class2num[pair[0]]
		w = pair[1]
		schedule.addEdge(v1, v2, w, False)


for key in num2class:
	tcost = schedule.inDegree(key)
	print(num2class[key],': ',tcost,sep='')

print(num2class)

classOrder = schedule.topologicalSort()
for num in classOrder:
	print(num2class[num])

