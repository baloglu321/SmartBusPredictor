# -*- coding: utf-8 -*-
"""
Created on Sat Dec  3 15:39:00 2022

@author: Mehmet


This code is written to make predictions by evaluating the data read through mongo db with machine learning algorithm.
"""
import pandas as pd
import numpy as np
import pymongo
from sklearn.preprocessing import MinMaxScaler,PolynomialFeatures
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor
from sklearn.tree import DecisionTreeRegressor
from sklearn.metrics import r2_score
import datetime


#reading data via mongodb

my_client = pymongo.MongoClient("mongodb://190.92.211.191:27017")
bus_client= my_client["my_database"]
bus_collection =bus_client["bus_list"]

data=bus_collection.find()
data_df=pd.DataFrame(list(data))
data_df=data_df.drop("_id",axis=1)


#data_df.info()

#separating the timestamp column for processing
time=[]
per=[]
date=[]
def Split(text):
    tme=str(text).split(" ")[1]
    dte=str(text).split(" ")[0]
    tme=tme.split("'")[0]
    dte=dte.split("'")[1]
    dte_split=[int(dte.split('-')[0]),int(dte.split('-')[1]),int(dte.split('-')[2])]
    if int(tme.split(":")[1])>50:
        clock=int(tme.split(":")[0])+1
    
    elif int(tme.split(":")[1])<10:
        clock=int(tme.split(":")[0])    
    
    else:
        clock=int(tme.split(":")[0])+0.5
    time.append(tme)
    per.append(clock)
    date.append(dte_split)
   

timestamp=np.array(data_df[["timestamp"]]).tolist()

time_stamp=list(map(Split,timestamp))


bus_name=np.array(data_df[["municipality_id"]])
bus_name=bus_name.reshape(1,-1)[0,:].tolist()
usage=np.array(data_df[["usage"]])
usage=usage.reshape(1,-1)[0,:].tolist()
capacity=np.array(data_df[["total_capacity"]])
capacity=capacity.reshape(1,-1)[0,:].tolist()


#Label encode for converting timestamp data to days of the week

week_day=[]


for k in range(len(date)):
    w=datetime.date(date[k][0],date[k][1],date[k][2]).weekday()
    week_day.append(w)

#Capacity list for each bus   
capacity_list=[]
for t in range(10):
    capacity_data=[bus_name[t],capacity[t]]
    capacity_list.append(capacity_data)
    capacity_list.sort()
    




#Separating test data and dataset        
    
df_busname=pd.DataFrame(bus_name,columns=["bus_id"])

df_per=pd.DataFrame(per,columns=["period"])
df_week=pd.DataFrame(week_day,columns=["week_day"])
df_usage=pd.DataFrame(usage,columns=["usage"])

df_in=pd.concat([df_week,df_busname,df_per],axis=1)
df_out=df_usage

x1=df_in[:10390]
y1=df_out[:10390]
x2=df_in[10390:]
y2=df_out[10390:]


#Training

def ML_Train(x1,y1,x2,y2):
    
    
    #polynomial regression
    xreg=x1
    xtest=x2
    poly=PolynomialFeatures(degree=15)
    xtest=poly.fit_transform(xtest)
    xpoly=poly.fit_transform(xreg)
    
    
    polylr=LinearRegression()
    polylr.fit(xpoly, y1)
    
    pred_poly=polylr.predict(xtest)
    
   
    """
    #decision tree(karar ağacı)
    dtr=DecisionTreeRegressor(random_state=15)
    dtr.fit(x1,y1)
    pred_dtr=dtr.predict(x2)
    
    #random forrest
    
    rfr=RandomForestRegressor(n_estimators=200,random_state=15)
    rfr.fit(x1,y1)
    pred_rfr=rfr.predict(x2)
    
    #evaluation
    
    #print(f"polinom tahmin tutarlılığı: {r2_score(y2,pred_poly)}" )
    #print(f"svr tahmin tutarlılığı: {r2_score(scaley2,pred_svr)}" )
    #print(f"karar ağacı tahmin tutarlılığı: {r2_score(y2,pred_dtr)}" )
    #print(f"random forrest tahmin tutarlılığı: {r2_score(y2,pred_rfr)}" )
    """
    return poly,polylr
    
poly,polylr=ML_Train(x1, y1, x2, y2)

"""
def Dl_pred(x):
    
    x_min_max=scale_min_max.transform(x)
    y_dl_pred=model.predict(x_min_max)
    return y_dl_pred
"""  

def poly_pred(x):
    x_poly=poly.transform(x)
    y_poly_pred=polylr.predict(x_poly)
    
    return y_poly_pred

"""
def dtr_pred(x):
    y_dtr_pred=dtr.predict(x)
    return y_dtr_pred

def rfr_pred(x):
    y_rfr_pred=rfr.predict(x)
    return y_rfr_pred
"""
#Generating the input list for the prediction

def Day_creat():
    today=datetime.datetime.today()
    week_date=[]
    next_date=[]
    next_bus_id=[]
    next_period=[]
    next_capacity=[]
    for w in range(2):
        for b in range(10):
            
            period=np.arange(8,17,0.5).tolist()
            cap=capacity_list[b][1]
            for p in period:
                next_period.append(p)
                next_bus_id.append(b)
                next_capacity.append(cap)        
                week=today.weekday()
                week_date.append(week)
                today_date=today.strftime("%d-%m-%Y")
                next_date.append(today_date)
        today+=datetime.timedelta(days=1)
        
        
    df_week_date=pd.DataFrame(week_date,columns=["week_day"])   
    df_bus_id=pd.DataFrame(next_bus_id,columns=["bus_id"])  
    df_period=pd.DataFrame(next_period,columns=["period"])
    df_next_date=pd.DataFrame(next_date,columns=["Date"])
    df_capacity=pd.DataFrame(next_capacity,columns=["Kapasite"])
    x=pd.concat([df_week_date,df_bus_id,df_period],axis=1)
    x_table=pd.concat([df_next_date,df_bus_id,df_period,df_capacity],axis=1)
    
    return x,x_table
        
x,x_table=Day_creat()    

#Occupancy rate calculation
def Ocupancy(pred_x,capacity):

    ocupancy=[]
    for k,x in enumerate(pred_x):
        percent=round(100-(((int(capacity[k])-int(x))/int(capacity[k]))*100),2)

        ocupancy.append(percent)
    return ocupancy    



def Predict(x,x_table):
    
    
    y_poly_pred=poly_pred(x)
    #y_dtr_pred=dtr_pred(x)
    #y_rfr_pred=rfr_pred(x)
    
    
    df_poly_pred=pd.DataFrame(y_poly_pred,columns=["Polinom Regresyon Tahminleri"])    
    #df_dtr_pred=pd.DataFrame(y_dtr_pred,columns=["Karar Ağacı Tahminleri"])
    #df_rfr_pred=pd.DataFrame(y_rfr_pred,columns=["Rassal Orman Tahminleri"])
    
    
    
   
    pred_poly=pd.concat([x_table,df_poly_pred],axis=1)
    #pred_dtr=pd.concat([x_table,df_dtr_pred],axis=1)
    #pred_rfr=pd.concat([x_table,df_rfr_pred],axis=1)
    
    
    ocupancy_poly=Ocupancy(y_poly_pred,np.array(x_table[["Kapasite"]]))
    df_ocupancy_poly=pd.DataFrame(ocupancy_poly,columns=["Tahmini doluluk oranı"])
    pred_poly=pd.concat([pred_poly,df_ocupancy_poly],axis=1)
    """
    ocupancy_dtr=Ocupancy(y_dtr_pred,np.array(x_table[["Kapasite"]]))
    df_ocupancy_dtr=pd.DataFrame(ocupancy_dtr,columns=["Tahmini doluluk oranı"])
    pred_dtr=pd.concat([pred_dtr,df_ocupancy_dtr],axis=1)
    
    ocupancy_rfr=Ocupancy(y_rfr_pred,np.array(x_table[["Kapasite"]]))
    df_ocupancy_rfr=pd.DataFrame(ocupancy_rfr,columns=["Tahmini doluluk oranı"])
    pred_rfr=pd.concat([pred_rfr,df_ocupancy_rfr],axis=1)
    """
    return pred_poly



def pred_bus(bus_id):

    Poly_reg_pred=Predict(x, x_table)
    today=datetime.datetime.today()
    hour=today.strftime("%H-%M")
    if int(hour.split("-")[1])>50:
        per=int(hour.split("-")[0])+1
    
    elif int(hour.split("-")[1])<10:
        per=int(hour.split("-")[0])    
    
    else:
        per=int(hour.split("-")[0])+0.5
        
        
        
    def list_them(per_time,last):
        
        result_reg=[]
        for i in range(180):
            if Poly_reg_pred.bus_id[i]==int(bus_id) and per_time==False :  
                result_reg.append(Poly_reg_pred.iloc[i+180].tolist())
            if Poly_reg_pred.bus_id[i]==int(bus_id) and last and Poly_reg_pred.period[i]==16.5 and per_time:
                result_reg.append(Poly_reg_pred.iloc[i].tolist())

            elif Poly_reg_pred.bus_id[i]==int(bus_id) and per_time and Poly_reg_pred.period[i]==per and last==False :
                result_reg.append(Poly_reg_pred.iloc[i].tolist())
                result_reg.append(Poly_reg_pred.iloc[i+1].tolist())
        return result_reg           
                    
    if per>17 or per<8:
        per_time=False
        last=False
        result_reg=list_them(per_time,last)
        
        
    elif per==16.5 or per==17 :
        per_time=True
        last=True
        result_reg=list_them(per_time,last)
    else :
        per_time=True
        last=False
        result_reg=list_them(per_time,last)

    

                 
    return result_reg,per_time






    
    
    
    