import streamlit as st
import pandas as pd   
import numpy as np 

from functions import newWeek 
from functions import getColumns
from functions import spefVal




def log_input(name):
   
    score =st.number_input(name,key=name+" number",)
    
    


def button_col(score,*args):
  
   df = pd.read_csv("bubu.csv")
   for arg in args:
        st.button(arg,on_click=spefVal,args=(week,day,arg,score))
        
            
           

    

    
        
def ke (score):
    if score== 0:
        score
    

    
       
   
   
          
         
 

def button_callback():
    st.write('Button clicked!')


df = pd.read_csv("bubu.CSV")

# get collumn headers




week = st.number_input("week",max_value=12)
day = st.number_input("day", max_value=7)



week_check = df[(df["week"] == week)].shape[0]
if week_check == 0 and week != 0 and day != 0:
    #new week and day one
    # make a dataframe 
    st.write("new week")
    st.button("add week",on_click=newWeek(week,1))
    
elif week_check != 0:
    #check for day 
    day_check= df[(df["day"]== day)  & (df["week"] == week) ].shape[0]
    st.write(day_check)
    st.write(df[(df["day"]== day)  & (df["week"] == week)])


    if day_check == 0  and day != 0:
        st.write("new day")
        st.button("add day",on_click=newWeek(week,day))
        


    elif day_check == 1 :
        st.write ("ready to log") 

        score =  st.number_input("score",key="score",)
        st.write(f"score is{score}")

        if st.button("log"):
            button_col(score,"read mins","sleep score","journal","meditate","impor tasks")

            
            
        
        
        

elif day == 0 and week == 0 :
    df

