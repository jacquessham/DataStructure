import csv
import Graph


routes = {}
city2num = {}
num2city = {}
with open('SimpleGraphData.csv', newline='', encoding='utf-8-sig') as csvfile:
	filereader = csv.reader(csvfile, delimiter=',')
	# Skip the header
	next(filereader)
	for row in filereader:
		# Count unique city first
		if row[0] not in city2num:
			label = int(len(city2num))
			city2num[row[0]] = label
			num2city[label] = row[0]
		if row[1] not in city2num:
			label = int(len(city2num))
			city2num[row[1]] = label
			num2city[label] = row[1]

		temp = (row[1], int(row[2]))
		if row[0] not in routes:
			routes[row[0]] = [temp]
		else:
			routes[row[0]].append(temp)

flightroutes = Graph.Graph(len(city2num))
for key in routes:
	v1 = city2num[key]
	pairs = routes[key]
	for pair in pairs:
		v2 = city2num[pair[0]]
		w = pair[1]
		flightroutes.addEdge(v1, v2, w, True)

"""
for key in num2city:
	tcost = flightroutes.outDegree(key)
	print(num2city[key],': ',tcost,sep='')

for key in num2city:
	tcost = flightroutes.outCost(key)
	print(num2city[key],': ',tcost,sep='')
"""
topSortRoutes = flightroutes.topologicalSort()
for num in topSortRoutes:
	print(num2city[num])

flightroutes.dijkstra(0)
