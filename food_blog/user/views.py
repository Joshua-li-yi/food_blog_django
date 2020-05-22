from django.shortcuts import render
import pymysql

# Create your views here.


# 用户注册
def register(request):

    if request.method == 'POST':
        # 获取表单中的数据
        email = request.POST.get('userEmail')
        name = request.POST.get('userName')
        pwd = request.POST.get('pwd1')
        pwd2 = request.POST.get('pwd2')
        gender = request.POST.get('gender')

        print( 'VALUES(1, "{}", 20200920, "{}" , "{}", 20000920, {})'.format(name, email, pwd, gender))
        # 异常检测
        if name == '':
            message = 'The name can not be none'
            return render(request, 'signup.html', {'message': message})
        if pwd=='':
            message = 'password can not be none'
            return render(request, 'signup.html', {'message': message})
        if pwd != pwd2:
            message = 'The password entered twice is different'
            return render(request, 'signup.html', {'message': message})

        # 连接数据库
        db = pymysql.connect(host='localhost', port=3306, user='root', passwd='', db='food_blog', charset='utf8')
        print('connect db success')
        # 创建游标
        cursor = db.cursor()

        # sql语句
        # （）实现多行字符串连接
        sql = (
            'INSERT INTO `user` '
            # {}作为占位符
            'VALUES(2, "{}", 20200920, "{}" , "{}", 20000920, "{}")'.format(name, email, pwd, gender)
        )

        try:
            # 执行sql语句
            cursor.execute(sql)
            # 提交到数据库执行
            db.commit()
            print('execute sql success')
            return render(request, 'successRegisted.html')
            # return render(request, 'home')
        except:
            # Rollback in case there is any error
            db.rollback()
            print('rollback')
            message = 'some thing error, data base rollback'
            return render(request, 'signup.html', {'message': message})

        cursor.close()
        # 关闭数据库连接
        db.close()
        print('close db')

        # print(email, name, pwd)

    elif request.method =='GET':
        return render(request, 'signup.html')


# 用户登陆
def logIn(request):
    return render(request, 'logIn.html')
    # if request.method == 'POST':
    #     # email = request.POST.get('userEmail')
    #     # name = request.POST.get('userName')
    #     # pwd = request.POST.get('pwd')
    #     # 连接数据库
    #     # db = pymysql.connect(host='localhost', port=3306, user='root', passwd='', db='food_blog', charset='utf8mb4')
    #     # # 创建游标
    #     # cursor = db.cursor()
    #     # # sql语句
    #     # sql = """
    #     # INSERT INTO user
    #     # """
    #     # # 执行语句
    #     # cursor.execute(sql)
    #     # # 关闭游标
    #     # cursor.close()
    #     # # 关闭数据库连接
    #     # db.close()
    #     # print(email, name, pwd)
    #     # return render(request, 'home.html')
    # elif request.method =='GET':
    #     return render(request, 'logIn.html')

# 用户主页
def home(request):
    return render(request, 'home.html')