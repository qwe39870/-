from django.http import HttpResponse
from django.shortcuts import render, redirect, reverse
from django.views.generic import View
from django.contrib import messages
import db


class Index(View):
    def get(self, request):
        
        return render(request, 'index.html')
    
class Search(View):
    def post(self, request):
        keyword = request.POST.get('keyword','')

        sql="select * from medicine"
        medicines =db.querydata(sql)

        results = []

        for medicine in medicines:
            keyword_match = not keyword or keyword.lower() in medicine['name'].lower()
            type_match = (keyword == medicine['type'])
            if keyword_match or type_match:
                results.append(medicine)

        if keyword == '':
            return redirect(reverse('Index'))
        
        if results==[]:

            return redirect(reverse('nothing'))
        

        feed= {'results': results}
        return render(request, 'index2.html', feed)

class Find(View):
    def post(self, request):
        color = request.POST.get('color','')  # 從表單中獲取顏色選擇器的值
        shape = request.POST.get('shape','')
        use = request.POST.get('use','')
        sql="select * from medicine"
        medicines =db.querydata(sql)

        results = []

        for medicine in medicines:
            color_match = color is '' or color == medicine['color']
            shape_match = shape is '' or shape == medicine['shape']
            use_match = use is '' or use == medicine['usee']

            if color_match and shape_match and use_match:
                results.append(medicine)

            if color=='' and shape =='' and use=='':
                return redirect(reverse('Index'))

        feed= {'results': results}

        if results==[]:

            return redirect(reverse('nothing'))
        
        return render(request, 'index2.html', feed)
        # return HttpResponse('顏色=%s 形狀=%s 劑型=%s'%(color,shape,use))

class Nothing(View):
    def get(self, request):
        
        return render(request, 'index3.html')
    
class Detail(View):
    def get(self, request, id):
        sql="select * from medicine"
        medicines =db.querydata(sql)
        medicine = next((item for item in medicines if 'id' in item and item["id"] == id), None)
        send={'medicine': medicine}
        return render(request, 'wait.html', send)
        