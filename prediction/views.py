from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.template import loader
import pickle
import statsmodels
def index(request):
    load = loader.get_template('index.html')
    return HttpResponse(load.render({},request))

def predict(request):
    year = request.POST['year']
    model = pickle.load(open("prediction/time_model.pkl", "rb"))
    value = (int(year) - 1963) * 12
    result = model.predict(start=103,end=value,dynamic=True)
    df = result.to_frame()
    final = df.tail(13)
    final = final.head(12)
    # final.values.tolist()
    month = ['January', 'February','March', 'April','May','June','July','August','September','October','November','December']
    predicted_sales = []
    for _ in final.values.tolist():
        predicted_sales.append(round(_[0],2))
    context = {
        'year':year,
        'sales':predicted_sales,
    }
    load = loader.get_template('result.html')
    return HttpResponse(load.render(context,request))
    
def back(request):
    return redirect('/')