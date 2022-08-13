# -*- coding: utf-8 -*-
"""VisualizationUsingSeaborn.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/19cXKA6GvqeU0STNp8DpxCl6sSkzChC5G
"""

import seaborn as sns
fmri = sns.load_dataset("tips")
sns.lineplot(x="total_bill",
         y="tip",
         data = fmri)



sns.lineplot(x="total_bill",
           y="tip",hue='day',color=['r','b','g','y'],
          data=fmri);

sns.lineplot(x="total_bill",
           y="tip",hue='day',color=['r','b','g','y'],
          style="smoker",
        data=fmri);

import seaborn as sns
import matplotlib.pyplot as plt
df=sns.load_dataset('tips')
sns.barplot(x='sex',
            y='tip',
            data=df)
plt.show()

import seaborn as sns
import matplotlib.pyplot as plt
df=sns.load_dataset('tips')
sns.barplot(x='time',
            y='tip',
            hue='sex',
            data=df)
plt.show()

import seaborn as sns
import matplotlib.pyplot as plt
df=sns.load_dataset('titanic')
sns.barplot(x='class', y='fare',data=df, 
         order=["Third","Second","First"])
plt.show()

sns.barplot(x='class', y='fare',
          hue='sex',data=df, palette='pastel')

sns.barplot(x='class', y='fare',
          hue='sex',data=df, palette='copper_r')

import seaborn
import matplotlib.pyplot as plt

seaborn.set(style = 'whitegrid')
tip = seaborn.load_dataset("tips")

seaborn.stripplot(x="total_bill", y="day" , data=tip)

plt.show()

import seaborn
import matplotlib.pyplot as plt

seaborn.set(style = 'whitegrid')
tip = seaborn.load_dataset("tips")

seaborn.stripplot(x="day", y="total_bill" , data=tip)

plt.show()

import seaborn
import matplotlib.pyplot as plt

seaborn.set(style = 'whitegrid')
tip = seaborn.load_dataset("tips")

seaborn.stripplot(x="day", y="total_bill" , data=tip , jitter=0.8)

plt.show()

seaborn.stripplot(x="day", y="total_bill" , data=tip , linewidth=1)

seaborn.stripplot(x="day", y="total_bill" , data=tip , edgecolor='green' , linewidth=1)

seaborn.stripplot(x="day", y="total_bill" , data=tip , edgecolor='green' , linewidth=1 , hue="size" )

seaborn.stripplot(x="day", y="total_bill"  , hue="smoker" , data=tip , palette="Set1" , size=10, marker="H" , alpha= 0.3)

seaborn.stripplot(x="day", y="total_bill"  , hue="smoker" , data=tip , palette="Set1" , size=10, marker="H" , alpha=1)

seaborn.boxplot(x ='time' , y='tip', data=tip)

seaborn.stripplot(x ='time' , y='tip', data=tip)

seaborn.boxplot(x ='tip' , y='size', orient='h', data=tip)

seaborn.boxplot(x="day", y="total_bill", 
                data=tip, palette="Set2",
                dodge=True)

seaborn.boxplot(x="day", y="total_bill",
                hue="smoker", 
                data=tip,palette="Set2",
                dodge=True)

import seaborn as sns
sns.swarmplot(x="day" , y = "total_bill",
              data=tip ,size = 10)

sns.swarmplot(y="day", x="total_bill", hue="size",
              orient ="h", data =tip,marker='>' ,size = 10)

sns.swarmplot(y="sex", x="total_bill", hue="smoker",
              orient ="h", data =tip,marker='>' ,size = 10, dodge="True")

sns.swarmplot(y="sex", x="total_bill", hue="smoker",
              data = tip , dodge="True")

sns.swarmplot(x="sex", y="total_bill", hue="smoker",
              data = tip , dodge="True")

sns.swarmplot(x="day", y="total_bill", data = tip , 
              linewidth=6)

sns.swarmplot(x="day", y="total_bill", data = tip , 
              linewidth=1)

#importing reuired pacakeges
import seaborn as sns
import matplotlib.pyplot as plt

data = sns.load_dataset("tips")
sns.jointplot(x = "total_bill" , y = "tip",
              kind="kde" , data = data)

plt.show()

#importing reuired pacakeges
import seaborn as sns
import matplotlib.pyplot as plt

data = sns.load_dataset("tips")
sns.jointplot(x = "total_bill" , y = "tip",
              kind="scatter" , data = data)

plt.show()

#importing reuired pacakeges
import seaborn as sns
import matplotlib.pyplot as plt

data = sns.load_dataset("tips")
sns.jointplot(x = "total_bill" , y = "tip",
              kind="hist" , data = data)

plt.show()

#importing reuired pacakeges
import seaborn as sns
import matplotlib.pyplot as plt

data = sns.load_dataset("tips")
sns.jointplot(x = "total_bill" , y = "tip",
              kind="hex" , data = data)

plt.show()

#importing reuired pacakeges
import seaborn as sns
import matplotlib.pyplot as plt

data = sns.load_dataset("tips")
sns.jointplot(x = "total_bill" , y = "tip",
              kind="reg" , data = data)

plt.show()

#importing reuired pacakeges
import seaborn as sns
import matplotlib.pyplot as plt

data = sns.load_dataset("tips")
sns.jointplot(x = "total_bill" , y = "tip",
              kind="resid" , data = data)

plt.show()

import matplotlib.pyplot as plt
import numpy as np 
import pandas as pd

import seaborn as sns

sns.set_theme()
tips = sns.load_dataset("tips")
sns.relplot(
    data = tips,
    x ="total_bill",y="tip",col='time',hue='smoker',style="size"
)

from seaborn.utils import load_dataset
import pandas as pd,numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

dt=load_dataset('tips')

print(dt.head())

plt.subplot(3,2,1) #subplot(row,col,place)
sns.barplot(x='day' , y = 'tip', data= dt)

plt.subplot(3,2,2)
sns.swarmplot(x='day' , y = 'tip', data= dt)

plt.subplot(3,2,3)
sns.scatterplot(x='day' , y = 'tip', data= dt)

plt.subplot(3,2,5)
sns.lineplot(x='day' , y = 'tip', data= dt)
plt.show()

import matplotlib.pyplot as plt
hours = [17,20,22,25,26,27,30,31,32,38,40,40,45,55]

#initalazation layout

fig,ax = plt.subplots(figsize = (4,4))

#plot
ax.hist(hours, bins = 5, edgecolor = "k");

import numpy as np
median_hours = np.median(hours)
bins = [10,20,30,40,50,60]

fig , ax = plt.subplots(figsize = (7,7))
plt.hist(hours, bins=bins,edgecolor ="black", color="red",alpha =0.3)

# axyline axis vertical line
plt.axvline(median_hours,color="black",ls ="--", label="median hour")
plt.legend();



import numpy as np
median_hours = np.median(hours)
bins = [10,20,30,40,50,60]

fig , ax = plt.subplots(figsize = (7,7))
plt.hist(hours, bins=bins,edgecolor ="black", color="#69b3a2",alpha =0.3)

# axyline axis vertical line
plt.axvline(median_hours,color="black",ls ="--", label="median hour")
plt.legend();

import numpy as np
median_hours = np.median(hours)
bins = [10,20,30,40,50,60]

fig , ax = plt.subplots(figsize = (7,7))
plt.hist(hours, bins=bins,edgecolor ="black", color="#69b3a2",alpha =6.3)

# axyline axis vertical line
plt.axvline(median_hours,color="black",ls ="--", label="median hour")
plt.legend();

# proper curve = symetric curve or positive symetric

# stack or area plot

import matplotlib.pyplot as plt
# List of days 
week = [1,2,3,4,5]

# no of study Hours
Studying = [7,8,6,11,7]

#no of playing hours
playing = [8,5,7,8,13]

mobile = [2,3,4,5,6]

#Stackplot with x,y,colors value

plt.stackplot(week,Studying ,playing,mobile,
              colors = ['r','c','k'])
plt.xlabel('week')
plt.ylabel('No of Hours')

plt.title('represantation of study and playing  wrt to week')

plt.show()