import rpy2.robjects as robjects
from rpy2.robjects.packages import importr
cluster = importr('cluster')

#matrix
v = robjects.FloatVector([0, 2.7, 1.2, 2.1, 2.3, 2.2, 2.6, 0, 1.5, 6.8, 3.9, 3.8, 1.2, 1.6, 0, 3.2, 3.6, 2.3, 2.1, 6.8, 3.3, 0, 2.6, 3,
                       2.5, 4, 4.7, 2.9, 0, 4.1, 2.3, 3.9, 2.3, 3.2, 5, 0])
m = robjects.r['matrix'](v, nrow = 6)

#input is matrix, output is the best number of clusters
robjects.r('''
  best.cluster <- function(matrix){
  my.k.choices <- 2: (ncol(matrix)-1)
  avg.sil.width <- rep(0, times=length(my.k.choices))
  for (ii in (1:length(my.k.choices)) ){
    avg.sil.width[ii] <- pam(matrix, k=my.k.choices[ii])$silinfo$avg.width
  }
  cbind.sil.width <- cbind(my.k.choices, avg.sil.width)
  #A LARGE average silhouette width indicates that the observations are properly clustered.
  best.k <- cbind.sil.width[which.max(data.frame(cbind.sil.width)[,2])][1]
  cluster<-pam(matrix,best.k)$clustering
  return (cluster)
}
'''
)

robjects.r('''
  k.number <- function(matrix){
  my.k.choices <- 2: (ncol(matrix)-1)
  avg.sil.width <- rep(0, times=length(my.k.choices))
  for (ii in (1:length(my.k.choices)) ){
    avg.sil.width[ii] <- pam(matrix, k=my.k.choices[ii])$silinfo$avg.width
  }
  cbind.sil.width <- cbind(my.k.choices, avg.sil.width)
  #A LARGE average silhouette width indicates that the observations are properly clustered.
  best.k <- cbind.sil.width[which.max(data.frame(cbind.sil.width)[,2])][1]
  return (best.k)
}
'''
)

#call best.cluster function in R, return the cluster distribution
r_f = robjects.r['best.cluster'] 
#call k.number function in R, return the number of cluster
r_k = robjects.r['k.number'] 
res = r_f(m)
k_res = int(r_k(m)[0])


result = []
for i in res:
  result.append(res[i])
#print cluster distribution
print(result)

indexlist = []
for i in range(0, k_res):
  temp= []
  for j in range(0, len(result)):
    if(result[j] == (i+1)):
      temp.append(j)
  indexlist.append(temp)
#indexlist is a list, which contains the list of household that are in the same cluster

print(indexlist)
