from django.shortcuts import render, redirect
import pymysql
# 获取当前时间
import datetime
# Create your views here.
# 导入用于装饰器修复技术的包
from functools import wraps
# Create your views here.

"""
session会用到数据库，所以使用之前需要初始化数据库，
即执行makemigrations migrate

1. 设置session
2. 获取session
3. 删除session
"""


# 装饰器函数，用来判断是否登录
def check_login(func):
    @wraps(func)  # 装饰器修复技术
    def inner(request, *args, **kwargs):
        ret = request.session.get("is_login")
        # 1. 获取cookie中的随机字符串
        # 2. 根据随机字符串去数据库取 session_data --> 解密 --> 反序列化成字典
        # 3. 在字典里面 根据 is_login 取具体的数据

        if ret == "1":
            # 已经登录，继续执行
            return func(request, *args, **kwargs)
        # 没有登录过，重新登陆
        else:
            # ** 即使登录成功也只能跳转到home页面，现在通过在URL中加上next指定跳转的页面
            # 获取当前访问的URL
            # next_url = request.path_info
            # return redirect("/app02/login/?next={}".format(next_url))
            # return redirect('/user/logIn')
            return render(request, 'notLogIn.html')
    return inner


# 用户注册
def register(request):

    if request.method == 'POST':
        # 获取表单中的数据
        email = request.POST.get('userEmail')
        name = request.POST.get('userName')
        pwd = request.POST.get('pwd1')
        pwd2 = request.POST.get('pwd2')
        gender = request.POST.get('gender')
        birthday = request.POST.get('datetimepicker')
        # 字符串中删掉某个字符
        birthday = birthday.replace('-', '')
        # 获取当前时间 即为注册时间
        now_time = datetime.datetime.now().strftime('%Y%m%d')
        # print(now_time)
        # print(birthday)
        print('VALUES(1, "{}", {}, "{}" , "{}", {}, {})'.format(name, now_time, email, pwd, birthday, gender))
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
        # ID为自增ID所以不用进行赋值
        sql = (
            'INSERT INTO `user`(user_name, user_registered, user_email, user_pass, user_birthday, gender) '
            # {}作为占位符
            'VALUES("{}", {}, "{}" , "{}", {}, {})'.format(name, now_time, email, pwd, birthday, gender)
        )

        try:
            # 执行sql语句
            cursor.execute(sql)
            # 提交到数据库执行
            db.commit()
            print('execute sql success')
            # 设置session
            request.session['is_signup'] = '1'
            request.session['email'] = email
            test_signup = request.session.get('is_signup')
            test_email = request.session.get('email')
            print('test_signup', test_signup)
            print('test_email', test_email)
            # return redirect('/user/successRegisted')
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
    if request.method == 'POST':
        # 获取用户名和密码
        email = request.POST.get('email')
        pwd = request.POST.get('pwd')

        print('begin login ')
        # 连接数据库
        db = pymysql.connect(host='localhost', port=3306, user='root', passwd='', db='food_blog', charset='utf8mb4')
        # 创建游标
        cursor = db.cursor()
        # SQL 查询语句
        sql = 'SELECT user_pass FROM user WHERE user_email = "{}"'.format(email)

        try:
            # 执行SQL语句
            cursor.execute(sql)
            # 获取所有记录列表
            if cursor is not None:  # 注意这里。单纯判断cursor是否为None是不够的
                result = cursor.fetchone()
                print('result', result)
                # 判断是否有此用户
                if result is not None:
                    db_pwd = result[0]
                    # 判断密码是否正确
                    if db_pwd == pwd:
                        print("log in success")
                        # 设置session
                        request.session['is_login'] = '1'
                        request.session['email'] = email
                        # 设置session7秒后失效
                        # request.session.set_expiry(7)
                        return render(request, 'home.html')
                    else:
                        print('pwd not true')
                        message = 'the pwd is not true, please input again'
                        return render(request, 'logIn.html', {'message': message})
                else:
                    print('result is  None')
                    print('this user not exist')
                    message = 'this user not exist, please chick the name whether true or not'
                    return render(request, 'logIn.html', {'message': message})
            else:
                print('cursor is None')
                print('this user not exist')
                message = 'this user not exist, please chick the name whether true or not'
                return render(request, 'logIn.html', {'message': message})
            print('execute sql success')
        except:
            db.rollback()
            print('rollback')
            message = 'something error when log in'
            print(message)
            return render(request, 'logIn.html', {'message': message})
        cursor.close()
        # 关闭数据库连接
        db.close()
        print('close db')
    elif request.method =='GET':
        return render(request, 'logIn.html')


# 用户主页
# 检查是否登陆
@check_login
def home(request):
    email = request.session.get("email")
    print(email)
    # 删除会话 是否已经注册
    return render(request, 'home.html')


# 自己的简历信息
@check_login
def me(request):
    email = request.session.get('email')
    print(email)
    # 连接数据库
    db = pymysql.connect(host='localhost', port=3306, user='root', passwd='', db='food_blog', charset='utf8mb4')
    # 创建游标
    cursor = db.cursor()
    # SQL 查询语句
    sql1 = 'SELECT ID, user_name, user_pass, user_birthday, gender FROM user WHERE user_email = "{}"'.format(email)

    try:
        # 执行SQL 1 语句
        cursor.execute(sql1)
        # 获取所有记录列表
        if cursor is not None:  # 注意这里。单纯判断cursor是否为None是不够的
            result = cursor.fetchone()
            print('result', result)
            # 判断是否有此用户
            if result is not None:
                db_ID = result[0]
                db_name = result[1]
                db_pass = result[2]
                db_birthday = result[3]
                db_gender = result[4]

            else:
                print('result is  None')
                print('this user not exist')
                message = 'this user not exist, please reload this page or log in again'
                return render(request, 'me.html', {'message': message})
        else:
            print('cursor is None')
            print('this user not exist')
            message = 'this user not exist, please reload this page or log in again'
            return render(request, 'me.html', {'message': message})
        print('execute sql 1 success')

        sql2 = 'SELECT brief_info, phone, blog_url, user_identity, other FROM user_info_plus WHERE ID = "{}";'.format(db_ID)
        # 执行SQL 2 语句
        cursor.execute(sql2)
        # 获取所有记录列表
        if cursor is not None:  # 注意这里。单纯判断cursor是否为None是不够的
            result = cursor.fetchone()
            print('result', result)
            # 判断是否有此用户的附加信息
            if result is not None:
                db_brief_info = result[0]
                db_phone = result[1]
                db_blog_url = result[2]
                db_identity = result[3]
                db_other = result[4]
            else:  # 如果没有就使用默认的信息
                db_brief_info = "your brief information"
                db_phone = "your phone"
                db_blog_url = "https://www.baidu.com/"
                db_identity = "engineer"
                db_other = "other information about you"
        else:  # 如果没有就使用默认的信息
            db_brief_info = "your brief information"
            db_phone = "your phone"
            db_blog_url = "https://www.baidu.com/"
            db_identity = "engineer"
            db_other = "other information about you"
        print('execute sql 2 success')
    except:
        db.rollback()
        print('rollback')
        message = 'something error, please reload this page or log in again'
        return render(request, 'me.html', {'message': message})

    cursor.close()
    # 关闭数据库连接
    db.close()
    print('close db')

    info = {
        'ID': db_ID,
        'name': db_name,
        'pwd': db_pass,
        'birthday': db_birthday,
        'gender': db_gender,
        'brief_info': db_brief_info,
        'phone': db_phone,
        'blog_url': db_blog_url,
        'identity': db_identity,
        'other': db_other,
    }
    return render(request, 'me.html', {'info': info})


# 写博客
@check_login
def writeBlog(request):
    return render(request, 'writeblog.html')


# 成功注册之后进行登陆
def successRegisted(request):
    ret = request.session.get("is_signup")
    # 删除会话 是否已经注册
    del request.session['is_signup']
    if ret == '1':
        request.session['is_login'] = '1'
        return redirect('/user/home')
    else:
        return redirect('/user/register')


# 退出登陆
@check_login
def logOut(request):
    # 删除会话记录
    del request.session['is_login']
    del request.session['email']
    return redirect('/user/logIn')