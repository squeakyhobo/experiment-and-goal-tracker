import pandas as pd 
df = pd.read_csv("bubu.CSV")

week = int(input("week is it in your 12 week year: ")) 

day =int(input("what day is it in your week: ")) 

index_end = df.index.stop

def log_finder(w,d):
   #print( df[(df[d]== day) & (df[w] == week)])
    col1 = df[df["week"] == w].shape[0]
    if col1 != 0:
        
        col2 = df[(df["week"] == w) & (df["day"] == d)].shape[0]
        if col2 ==1 :
            print("ready to log")
            actual_day = d
            actual_week = w 
            
            return (actual_week,actual_day)
            
            # how to change values in rows
        elif col2 == 0:
            
            filt = (df[df["week"]== w]).shape[0]
            dayf =  (df[df["week"]==w]).iloc[filt-1]["day"]
            actual_day =dayf+1
            actual_week = w
            
            
        
            
            print("new day but not new week")
            new_WEEK = {"Mood":9,"Hours of Sleep":6,"Exercise Minutes":6,"week":w,"day":dayf+1}
            
            bubu= pd.DataFrame([new_WEEK])
        
            new_log =  pd.concat([df,bubu],ignore_index=True)
            
           
            print(new_log)
            new_log.to_csv("bubu.csv",index= False)
            
            
            return(actual_week,actual_day)
            
            
            
            
            
        
        
    elif col1 == 0:
        
        print("new week")
        
        weekf = df.iloc[index_end-1]["week"]
        actual_week=weekf+1 
        actual_day= 1
        
        new_WEEK = {"Mood":0,"Hours of Sleep":0,"Exercise Minutes":0,"week":weekf+1,"day":1}
        
        bubu= pd.DataFrame([new_WEEK])
        
        
        new_log=  pd.concat([df,bubu],ignore_index=True)
        print(new_log)
        new_log.to_csv("bubu.csv",index=False)
        return(actual_day,actual_week)
            
        
   
    
             
      
        
    
    
   




# make it able to input any data for the new row 
        