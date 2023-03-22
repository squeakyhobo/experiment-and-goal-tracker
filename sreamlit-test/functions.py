import pandas as pd 
import numpy as np 



def diction_maker():
   df = pd.read_csv("bubu.CSV")
   diction ={}
   for i in range((df.columns.shape[0])):
      metric = (df.columns[i])
      
      diction.update({metric:None})
   return diction 



def newWeek(week,day):
   df = pd.read_csv("bubu.CSV")
   week_skel = diction_maker()
   week_skel["week"] = week
   week_skel["day"] = day
   newone = pd.concat([df,pd.DataFrame([week_skel])],ignore_index=True,axis=0)
   pd.DataFrame.to_csv(newone,"bubu.CSV",index= False)
   

def getColumns():
   # search for the day and week 
   df =pd.read_csv("bubu.CSV")
   x= []
   i= 0 
   for i in range((df.columns.shape[0])):
      metric = df.columns[i]
      x.append(metric)
      
   return x
      
      

      


# ask whihch values to edit th
def spefVal(week , day ,name,score ):
   
   df =pd.read_csv("bubu.csv")
   current = df[(df["week"]==week)&(df["day"]== day)]

   currIndex = current.index.values
   
   
       
   for i in range ((df.columns.shape[0])):
      if name == df.columns[i]:
         col_index =i


   df.iloc[currIndex,col_index] = score
   df.to_csv("bubu.csv",index=False)
   
   
   


   





