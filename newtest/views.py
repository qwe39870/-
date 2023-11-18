from django.http import HttpResponse
from django.shortcuts import render, redirect, reverse
from django.views.generic import View
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from .forms import Auth
from .models import Test
import db

# Create your views here.
class Testindex(View):
    def get(self, request):

        data_list = Test.objects.all()
        
        return render(request, 'testinsex.html', {'data_list': data_list})
    

class Index(View):
    def get(self, request):
        
        return render(request, 'index.html')
    
class Search(View):
    def post(self, request):
        keyword = request.POST.get('keyword','')

        sql="select * from newtest_test"
        medicines =db.querydata(sql)

        results = []

        # 舊版
        # for medicine in medicines:
        #     keyword_match = not keyword or keyword.lower() in medicine['name'].lower()
        #     type_match = (keyword == medicine['type'])
        #     if keyword_match or type_match:
        #         results.append(medicine)

        # 在你的程式碼中應用 LCS
        for medicine in medicines:
            keyword_lower = keyword
            name_lower = medicine['name']

            m = len(keyword_lower)
            n = len(name_lower)

            # 創建一個二維表格來存儲LCS的長度
            dp = [[0] * (n + 1) for _ in range(m + 1)]

            # 填充表格
            for i in range(1, m + 1):
                for j in range(1, n + 1):
                    if keyword_lower[i - 1] == name_lower[j - 1]:
                        dp[i][j] = dp[i - 1][j - 1] + 1
                    else:
                        dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

            # 回溯，構造 LCS
            i, j = m, n
            lcs_result = []
            while i > 0 and j > 0:
                if keyword_lower[i - 1] == name_lower[j - 1]:
                    lcs_result.append(keyword_lower[i - 1])
                    i -= 1
                    j -= 1
                elif dp[i - 1][j] > dp[i][j - 1]:
                    i -= 1
                else:
                    j -= 1

                # 因為我們是從後往前回溯，所以要反轉結果
            lcs_result.reverse()

                # 檢查是否是子序列或者包含 LSC 的一部分
            keyword_match =  len(lcs_result) > 1 or all(char in name_lower for char in keyword_lower)

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
        sql="select * from newtest_test"
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
    
class Login(View):
    def get(self, request):
        # 判斷是否登入，有登入就跳回首頁
        # if request.user.is_authenticated:
        #     return redirect(reverse('Index'))
        
        return render(request, 'login.html')

    def post(self, request):
        username = request.POST.get('username','')
        password = request.POST.get('password','')

        exist = User.objects.filter(username=username).exists()
        if not exist:
            return HttpResponse("帳號不存在")
        user = authenticate(username=username, password=password)
        if user:
            login(request, user)
            # 进一步检查用户是否是超级用户
            if user.is_superuser:
            # 如果是超级用户，重定向到 Django 管理后台
                return redirect('admin:index')
            else:
            # 如果不是超级用户，重定向到首页或其他适当的页面
                return redirect('Index')
        else:
            return HttpResponse('密碼錯誤')
        
class Register(View):
    def get(self, request):

        form = Auth()
        
        return render(request, 'register.html', {'form': form})

    def post(self, request):
        form = Auth(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username','')
            password = form.cleaned_data.get('password','')
            return HttpResponse('帳號為:{}, 密碼為{}'.format(username,password))

        else:
            print(form.errors)
            return render(request, 'register.html', {'form': form})
        
        # username = request.POST.get('username','')
        # password = request.POST.get('password','')
        # check_password = request.POST.get('check_password','')

        # if password != check_password:
        #     return HttpResponse('密碼不一樣')

        # exist = User.objects.filter(username=username).exists()
        # if exist:
        #     return HttpResponse("帳號已存在")
        
        # User.objects.create_user(username=username, password=password)
        
        # return redirect(reverse('login'))
       