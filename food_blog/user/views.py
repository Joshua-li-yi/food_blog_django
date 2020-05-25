from django.shortcuts import render
import pymysql
# 获取当前时间
import datetime
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
        birthday = request.POST.get('datetimepicker')
        # 字符串中删掉某个字符
        birthday = birthday.replace('-', '')
        # 获取当前时间 即为注册时间
        now_time = datetime.datetime.now().strftime('%Y%m%d')
        # print(now_time)
        # print(birthday)
        print( 'VALUES(1, "{}", {}, "{}" , "{}", {}, {})'.format(name, now_time, email, pwd, birthday, gender))
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
def home(request):
    return render(request, 'home.html')


# 自己的简历
def me(request):
    return render(request, 'me.html')


# 写博客
def writeBlog(request):
    return render(request, 'writeblog.html')