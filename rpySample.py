import rpy2.robjects as robjects
from rpy2.robjects import FloatVector
from rpy2.robjects.packages import importr
from numpy import matrix
import array

stats = importr('stats')
base = importr('base')
cluster = importr('cluster')

letters = robjects.r['letters']
rcode = 'paste(%s, collapse="-")' %(letters.r_repr())
res = robjects.r(rcode)
print(res)
print robjects.r['pi'][0]

ctl = FloatVector([4.17,5.58,5.18,6.11,4.50,4.61,5.17,4.53,5.33,5.14])
trt = FloatVector([4.81,4.17,4.41,3.59,5.87,3.83,6.03,4.89,4.32,4.69])
group = base.gl(2, 10, 20, labels = ["Ctl","Trt"])
weight = ctl + trt

robjects.globalenv["weight"] = weight
robjects.globalenv["group"] = group
lm_D9 = stats.lm("weight ~ group")
print(stats.anova(lm_D9))


testmatrix = matrix([[0.0,2.6,1.2,2.1,2.5,2.3],[2.7,0.0,1.6,6.8,4.0,3.9]])
testboolean = base.isSymmetric(testmatrix)

