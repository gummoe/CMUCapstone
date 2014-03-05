TSPtable=[["0->1",0,"4800 Forbes Ave, Pittsburgh PA 15213",2,"1300 Murray Ave, Pittsburgh PA 15217",2.01],
       ["1->2",2,"1300 Murray Ave, Pittsburgh PA 15217",1,"1013 Mirror Street, Pittsburgh PA 15217",2.51],
	   ['2->3',1,"1013 Mirror Street, Pittsburgh PA 15217",10,"7731 Board Way, Pittsburgh PA 15221",4.64],
	   ['3->4',10,"7731 Board Way, Pittsburgh PA 15221",7,"2018 Frankella Ave, Pittsburgh PA 15221",3.85],
	   ["4->5",7,"2018 Frankella Ave, Pittsburgh PA 15221",8,"10205 Clair Ave, Pittsburgh PA 15235",3.19],
	   ["5->6",8,"10205 Clair Ave, Pittsburgh PA 15235",11,"1222 N Highland Ave, Pittsburgh PA 15206",8.38],
	   ["6->7",11,"1222 N Highland Ave, Pittsburgh PA 15206",6,"1232 N Highland Ave, Pittsburgh PA 15206",0.02],
	   ["7->8",6,"1232 N Highland Ave, Pittsburgh PA 15206",5,"545 N Aiken Ave, Pittsburgh PA 15206",2.07],
	   ["8->9",5,"545 N Aiken Ave, Pittsburgh PA 15206",3,"311 Harmar Street, Pittsburgh PA 15219",4.7],
	   ["9->10",3,"311 Harmar Street, Pittsburgh PA 15219",4,"30 Pride Street, Pittsburgh PA 15219",4.31],
	   ["10->11",4,"30 Pride Street, Pittsburgh PA 15219",9,"3216 Joe Hammer Square, Pittsburgh PA 15213",2.12],
	   ["11->0",9,"3216 Joe Hammer Square, Pittsburgh PA 15213",0,"4800 Forbes Ave, Pittsburgh PA 15213",2.46]]
table=[[1,2,2.7,],
       [2,2,0.0],
	   [3,4,3.9],
	   [4,4,0.0],
	   [5,6,2.1],
	   [6,6,0.0],
	   [7,8,3.2],
	   [8,8,0.0],
	   [9,4,2.4],
	   [10,2,3.2],
	   [11,6,0.0]]
nodeNum=input('Enter the Node Number to find cluster and cost:')
intNodeNum=int(nodeNum)
for row in table:
    if(row[0]==intNodeNum):
	    clusterNo=row[1]
clusterNodeList=[];
for row in TSPtable:
	if(int(row[3])==intNodeNum):
		costofNodeOutsideCluster=float(row[5]) # cost of node outside cluster.
for row in table:
    if(row[1]==clusterNo):
        clusterNodeList.append(row[0]) # Find all nodes in a cluster.
if(int(clusterNodeList[0])==intNodeNum):
	e=0
else:
	e=1
for row in TSPtable:
	if(row[3]==clusterNodeList[0]):
		costOfEntryToCluster=row[5]
print("**** Cost of Entry to Cluster is ******"+str(costOfEntryToCluster))
ClusterLessThanMcount=0
costOfClusterNodeList=[];
for row in clusterNodeList:
	for row1 in TSPtable:
		if(int(row)==row1[3]):
		    costOfClusterNode=row1[5] # cost of the node in the cluster
		    costOfClusterNodeList.append(costOfClusterNode) #append cost of all nodes in cluster
		    if(costOfClusterNode<0.1):
			    ClusterLessThanMcount+=1
lessThanMcount=0
for row in TSPtable:
    if row[5] < 0.1:
	    lessThanMcount+=1 # No of nodes with cost less than 0.1
print("*******count of nodes less than m is*********"+str(lessThanMcount))
max=TSPtable[0][1]
for row in TSPtable:
    if(row[1] > max):
	    max=row[1]     #find the node with maximum number.
nodesInSequence=max-lessThanMcount  # no of nodes with cost more than 0.1
noofRowsinMatrix=len(TSPtable)
splitCostFromLastNodeToOrigin=TSPtable[noofRowsinMatrix-1][5]/nodesInSequence   # split cost from last node to origin.
print("********Split Cost from last node to origin is********"+str(splitCostFromLastNodeToOrigin))
sum=0.0
for row in costOfClusterNodeList:
    sum+=row
costOfNode=(e*costofNodeOutsideCluster)+(float(costOfEntryToCluster)/(len(costOfClusterNodeList)-ClusterLessThanMcount))
nodeCostPerCase=costOfNode+splitCostFromLastNodeToOrigin # cost per case of node.
print("*******Node cost per case is*****"+str(nodeCostPerCase))
