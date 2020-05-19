from django.shortcuts import render
import pymysql

# Create your views here.
def register(request):
    if request.method == 'POST':
        return render(request, 'signup.html')
    elif request.method =='GET':
        email = request.POST.get('userEmail')
        name = request.POST.get('userName')
        pwd = request.POST.get('pwd')
        # 连接数据库
        # db = pymysql.connect(host='localhost', port=3306, user='root', passwd='', db='food_blog', charset='utf8mb4')
        # # 创建游标
        # cursor = db.cursor()
        # # sql语句
        # sql = """
        # INSERT INTO user
        # """
        # # 执行语句
        # cursor.execute(sql)
        # # 关闭游标
        # cursor.close()
        # # 关闭数据库连接
        # db.close()
        print(email, name, pwd)
        return render(request, 'home.html')
