from django.shortcuts import render
from . import bus_cap_pred


        

lines=["Eyüpsultan","Pendik","Emirgan","Taksim","Kadıköy","Karaköy","Beşiktaş","Ortaköy","Üsküdar","Kuzguncuk"]

def home(request):
    data={
         "lines" : lines
        }
    return render(request,"index.html",data)

def eyüpsultan(request):
    result_reg,per_time=bus_cap_pred.pred_bus(0)
    table_head=["Tarih","Period","Kapasite","Tahmini Doluluk oranı(%)"]
    regressions=[]
    if per_time:
        info=[]
    else :
        info=["Saat 16:30 ile 08:00 arasında aktif sefer bulunmamaktadır"]    
    
    for result in result_reg:
        regressions.append([result[0],result[2],result[3],result[5]])
        

    data={
         "table_head": table_head,
         "regressions" : regressions,
         "line" : lines[0],
         "info": info
        }
    return render(request,"bus_0.html",data)

def pendik(request):
    result_reg,per_time=bus_cap_pred.pred_bus(1)
    table_head=["Tarih","Period","Kapasite","Tahmini Doluluk oranı(%)"]
    if per_time:
        info=[]
    else :
        info=["Saat 16:30 ile 08:00 arasında aktif sefer bulunmamaktadır"] 
    regressions=[]

    for result in result_reg:
        regressions.append([result[0],result[2],result[3],result[5]])
        

    data={
         "table_head": table_head,
         "regressions" : regressions,
         "line" : lines[1],
         "info":info
        }
    return render(request,"bus_0.html",data)

def emirgan(request):
    result_reg,per_time=bus_cap_pred.pred_bus(2)
    table_head=["Tarih","Period","Kapasite","Tahmini Doluluk oranı(%)"]
    regressions=[]
    if per_time:
        info=[]
    else :
        info=["Saat 16:30 ile 08:00 arasında aktif sefer bulunmamaktadır"] 
    for result in result_reg:
        regressions.append([result[0],result[2],result[3],result[5]])
        

    data={
         "table_head": table_head,
         "regressions" : regressions,
         "line" : lines[2],
         "info":info
        }
    return render(request,"bus_0.html",data)

def taksim(request):

    result_reg,per_time=bus_cap_pred.pred_bus(3)
    table_head=["Tarih","Period","Kapasite","Tahmini Doluluk oranı(%)"]
    regressions=[]
    if per_time:
        info=[]
    else :
        info=["Saat 16:30 ile 08:00 arasında aktif sefer bulunmamaktadır"] 
    for result in result_reg:
        regressions.append([result[0],result[2],result[3],result[5]])
        

    data={
         "table_head": table_head,
         "regressions" : regressions,
         "line" : lines[3],
         "info":info
        }
    return render(request,"bus_0.html",data)


def kadıköy(request):
    result_reg,per_time=bus_cap_pred.pred_bus(4)
    table_head=["Tarih","Period","Kapasite","Tahmini Doluluk oranı(%)"]
    regressions=[]
    if per_time:
        info=[]
    else :
        info=["Saat 16:30 ile 08:00 arasında aktif sefer bulunmamaktadır"] 

    for result in result_reg:
        regressions.append([result[0],result[2],result[3],result[5]])
        

    data={
         "table_head": table_head,
         "regressions" : regressions,
         "line" : lines[4],
         "info":info

        }
    return render(request,"bus_0.html",data)


def karaköy(request):
    result_reg,per_time=bus_cap_pred.pred_bus(5)
    table_head=["Tarih","Period","Kapasite","Tahmini Doluluk oranı(%)"]
    regressions=[]
    if per_time:
        info=[]
    else :
        info=["Saat 16:30 ile 08:00 arasında aktif sefer bulunmamaktadır"] 
    for result in result_reg:
        regressions.append([result[0],result[2],result[3],result[5]])
        

    data={
         "table_head": table_head,
         "regressions" : regressions,
         "line" : lines[5],
         "info":info

        }
    return render(request,"bus_0.html",data)

def beşiktaş(request):
    result_reg,per_time=bus_cap_pred.pred_bus(6)
    table_head=["Tarih","Period","Kapasite","Tahmini Doluluk oranı(%)"]
    regressions=[]
    if per_time:
        info=[]
    else :
        info=["Saat 16:30 ile 08:00 arasında aktif sefer bulunmamaktadır"] 

    for result in result_reg:
        regressions.append([result[0],result[2],result[3],result[5]])
        

    data={
         "table_head": table_head,
         "regressions" : regressions,
         "line" : lines[6],
         "info":info
        }
    return render(request,"bus_0.html",data)

def ortaköy(request):
    result_reg,per_time=bus_cap_pred.pred_bus(7)
    table_head=["Tarih","Period","Kapasite","Tahmini Doluluk oranı(%)"]
    regressions=[]
    if per_time:
        info=[" "]
    else :
        info=["Saat 16:30 ile 08:00 arasında aktif sefer bulunmamaktadır."] 
    for result in result_reg:
        regressions.append([result[0],result[2],result[3],result[5]])
        

    data={
         "table_head": table_head,
         "regressions" : regressions,
         "line" : lines[7],
         "info":info
        }
    return render(request,"bus_0.html",data)

def üsküdar(request):
    result_reg,per_time=bus_cap_pred.pred_bus(8)
    table_head=["Tarih","Period","Kapasite","Tahmini Doluluk oranı(%)"]
    regressions=[]
    if per_time:
        info=[]
    else :
        info=["Saat 16:30 ile 08:00 arasında aktif sefer bulunmamaktadır"] 
    for result in result_reg:
        regressions.append([result[0],result[2],result[3],result[5]])
        

    data={
         "table_head": table_head,
         "regressions" : regressions,
         "line" : lines[8],
         "info":info
        }
    return render(request,"bus_0.html",data)

def kuzguncuk(request):
    result_reg,per_time=bus_cap_pred.pred_bus(9)
    table_head=["Tarih","Period","Kapasite","Tahmini Doluluk oranı(%)"]
    regressions=[]
    if per_time:
        info=[]
    else :
        info=["Saat 16:30 ile 08:00 arasında aktif sefer bulunmamaktadır"] 
    for result in result_reg:
        regressions.append([result[0],result[2],result[3],result[5]])
        

    data={
         "table_head": table_head,
         "regressions" : regressions,
         "line" : lines[9],
         "info":info
        }
    return render(request,"bus_0.html",data)                    
