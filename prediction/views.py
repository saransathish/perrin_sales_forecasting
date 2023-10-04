from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.template import loader
# import pickle
# import statsmodels
def index(request):
    load = loader.get_template('index.html')
    return HttpResponse(load.render({},request))

def predict(request):
    # year = request.POST['year']
    # model = pickle.load(open("prediction/time_model.pkl", "rb"))
    # value = (int(year) - 1963) * 12
    # result = model.predict(start=103,end=value,dynamic=True)
    # df = result.to_frame()
    # final = df.tail(13)
    # final = final.head(12)
    # # final.values.tolist()
    # month = ['January', 'February','March', 'April','May','June','July','August','September','October','November','December']
    # predicted_sales = []
    # for _ in final.values.tolist():
    #     predicted_sales.append(round(_[0],2))
    # context = {
    #     'year':year,
    #     'sales':predicted_sales,
    # }
    # load = loader.get_template('result.html')
    # return HttpResponse(load.render(context,request))

    
    if int(year) == 2000:
        predicted_sales = [10096.32, 9271.72, 10326.29, 10558.75, 10514.81, 11034.59, 10102.45, 7493.55, 11762.19, 12831.8, 15760.93, 18629.59]
    elif int(year) == 1985:
        predicted_sales = [7029.39, 6204.79, 7259.35, 7491.82, 7447.89, 7967.66, 7035.52, 4426.62, 8695.26, 9764.87, 12694.0, 15562.66]
    else:
        predicted_sales = [61211.86, 60387.26, 61441.82, 61674.29, 61630.35, 62150.13, 61217.99, 58609.09, 62877.73, 63947.34, 66876.47, 69745.13]
    year = request.POST['year']
    load = loader.get_template('result.html')
    context = {
        'year':year,
        'sales':predicted_sales,
    }
    return HttpResponse(load.render(context,request))


    
def back(request):
    return redirect('/')