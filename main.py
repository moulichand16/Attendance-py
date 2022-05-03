import pandas as pd
import numpy as np
from datetime import date
from matplotlib import pyplot as plt
today=date.today()
dte=today.strftime("%d/%m/%y")
df=pd.read_csv("ALLdata.csv")

mem=df.shape[0];
l=[]
io=str(date.today())
print(df)
i=0
apd=1
if dte in df:
    print(df)
    print(mem)
    
else:
    x=0
    print(dte+" Attendance")
    while x<mem-1:
        if i<0:
            i=0
        x=globals()['i']
        p=input("ID "+df.loc[x,'ID NO']+" (P/A) ?" )
        
        if len(p)==0:
            
            i=x-1
            if len(l):
                l.pop()
                
            print(x)
        elif len(p)==1:
            l.append(p)
            i=x+1
        elif len(p)>1:
            l.append(p[0])
            
            
            
            
            
            
        
            

    print(mem)
    print(len(l))
    df[dte]=l
    text="Atdnc"+io+".csv"

    forcomp=dte+"attendance"
    print(forcomp)
    if "Unnamed: 0," in df:
        del df['Unnamed: 0,']
    df.to_csv(text,index=False)
    df.to_csv("ALLdata.csv",index=False)

    ll=[]
    for d in range(0,mem):
        if l[d]=='p':
            l[d]=1
        else:
            l[d]=0
        ll.append(d)


    
    plt.plot(ll,l)
    plt.show()

    
        

            
              

    


