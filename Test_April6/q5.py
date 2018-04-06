# question 5

import numpy as np
from scipy import stats

x=[11.95,11.91,11.86,12.00,11.93,12,11.94,12.10,11.95,11.99,11.94,11.89,12.01,11.99,11.94]
temp=stats.itemfreq(x)
print("frequencey distribution is as follows: \n",temp)
meanx=np.mean(x)
medx=np.median(x)
modex=stats.mode(x)    

print("mean, median, mode are :", meanx,medx,modex[0])       
