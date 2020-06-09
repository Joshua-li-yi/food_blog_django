from django.shortcuts import render, redirect
import pymysql
# 获取当前时间
import datetime
# Create your views here.
# 导入用于装饰器修复技术的包
from functools import wraps
import socket

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

        # 获取主机名
        hostname = socket.gethostname()
        # 获取本机IP
        ip = socket.gethostbyname(hostname)

        # 字符串中删掉某个字符
        birthday = birthday.replace('-', '')
        # 获取当前时间 即为注册时间
        now_time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M')
        # print(now_time)
        print('VALUES("{}", {}, "{}" , "{}", {}, {})'.format(name, now_time, email, pwd, birthday, gender))

        # 异常检测
        if name == '' or len(name) > 20:
            message = 'The name length can not meet require'
            return render(request, 'signup.html', {'message': message})
        # 密码长度6<= <= 20
        if pwd == '' or len(pwd) > 20 or len(pwd) < 6:
            message = 'password length can not meet require'
            return render(request, 'signup.html', {'message': message})
        if pwd != pwd2:
            message = 'The password entered twice is different'
            return render(request, 'signup.html', {'message': message})
        # 名字中不能又空格和-字符
        if len(name.replace('-', '').replace(' ', '')) != len(name):
            message = 'The name have illegal character'
            return render(request, 'signup.html', {'message': message})
        # 密码中不能有空格和-字符
        if len(pwd.replace('-', '').replace(' ', '')) != len(pwd):
            message = 'The password have illegal character'
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
            'VALUES("{}", "{}", "{}" , "{}", "{}", {});'.format(name, now_time, email, pwd, birthday, gender)
        )
        # 将登陆信息插入到login表中
        sql2 = 'INSERT INTO login(ID, login_time, ip, errorcount) VALUES( (SELECT ID FROM `user` WHERE user_email = "{}"), "{}", "{}", 0); '.format(
            email, now_time, ip)

        try:
            # 执行sql语句
            print(sql)
            cursor.execute(sql)
            cursor.execute(sql2)
            # 提交到数据库执行
            db.commit()
            print('execute sql success')
            # 设置session
            request.session['is_signup'] = '1'
            request.session['email'] = email
            request.session['modify'] = 0
            return render(request, 'successRegisted.html')
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

    elif request.method == 'GET':
        return render(request, 'signup.html')


# 用户登陆
def logIn(request):
    if request.method == 'POST':
        # 获取用户名和密码
        email = request.POST.get('email')
        pwd = request.POST.get('pwd')

        # 获取主机名
        hostname = socket.gethostname()
        # 获取本机IP
        ip = socket.gethostbyname(hostname)

        # 记录登陆错误的次数
        # 存在就不设置
        request.session.setdefault('error_count', 0)
        now_time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M')

        print('begin login ')
        # 连接数据库
        db = pymysql.connect(host='localhost', port=3306, user='root', passwd='', db='food_blog', charset='utf8mb4')
        # 创建游标
        cursor = db.cursor()
        # SQL 查询语句
        sql = 'SELECT user_pass FROM user WHERE user_email = "{}"'.format(email)
        # 将登陆信息插入到login表中
        sql2 = 'INSERT INTO login(ID, login_time, ip, errorcount) VALUES( (SELECT ID FROM `user` WHERE user_email = "{}"), "{}", "{}", {}); '.format(
            email, now_time, ip, request.session['error_count'])
        # 密码错误3次开始提示
        if request.session['error_count'] < 3:
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
                            # 将登陆信息记录到login表中
                            try:
                                cursor.execute(sql2)
                                db.commit()
                            except:
                                db.rollback()

                            del request.session['error_count']
                            # 设置session
                            request.session['is_login'] = '1'
                            request.session['email'] = email
                            request.session['modify'] = 0
                            # 设置session7秒后失效
                            # request.session.set_expiry(7)
                            print("log in success")
                            return render(request, 'home.html')
                        else:
                            # 如果登陆错误则，error count +1
                            request.session['error_count'] += 1
                            print('pwd is true')
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
                db.commit()

            except:
                db.rollback()
                print('rollback')
                message = 'something error when log in'
                print(message)
                return render(request, 'logIn.html', {'message': message})
        else:
            del request.session['error_count']
            message = 'you login time is over 3 times'
            print(message)
            return render(request, 'logIn.html', {'message': message})
        cursor.close()
        # 关闭数据库连接
        db.close()
        print('close db')
    elif request.method == 'GET':
        return render(request, 'logIn.html')


# 用户主页
# 检查是否登陆
@check_login
def home(request):
    # 连接数据库
    email = request.session['email']
    db = pymysql.connect(host='localhost', port=3306, user='root', passwd='', db='food_blog', charset='utf8mb4')
    # 创建游标
    cursor = db.cursor()
    # SQL 查询语句
    # 挑出所有发布了的文章
    sql = 'SELECT b.blog_id, b.blog_title, b.blog_excerpt, p.publish_time FROM blog b, publish_blog p WHERE b.blog_id=p.blog_id AND p.publish_time <> "" ORDER BY b.blog_modified DESC;'
    sql2 = 'SELECT b.blog_id, b.blog_title, b.blog_excerpt, p.publish_time FROM blog b, publish_blog p WHERE b.blog_id=p.blog_id AND p.ID=(SELECT u.ID FROM `user` u WHERE u.user_email="{}") ORDER BY b.blog_modified DESC;'.format(
        email)
    sql3 = 'SELECT user_name FROM `user` WHERE user_email="{}";'.format(email)
    # food time中的文章列表
    blogs = {}
    # 此用户写的blog
    my_blogs = {}
    try:
        # 执行SQL语句
        cursor.execute(sql)
        # 获取所有记录列表
        if cursor is not None:  # 注意这里。单纯判断cursor是否为None是不够的
            db_blogs = cursor.fetchall()
            for db_blog in db_blogs:
                blogs[db_blog[0]] = {'title': db_blog[1], 'abstract': db_blog[2], 'publish_time': db_blog[3]}
            # print(blogs)
        else:
            print('result is  None')
            message = 'the blogs is null'
            return render(request, 'home.html', {'message': message})
        print('execute sql success')

        # 挑选本用户的所有blog
        cursor.execute(sql2)
        # 获取所有记录列表
        if cursor is not None:  # 注意这里。单纯判断cursor是否为None是不够的
            db_my_blogs = cursor.fetchall()
            for db_my_blog in db_my_blogs:
                publish_time = db_my_blog[3]
                # 如果发布时间为空就说明该文章使草稿
                if db_my_blog[3] is None:
                    publish_time = "draft"
                my_blogs[db_my_blog[0]] = {'title': db_my_blog[1], 'abstract': db_my_blog[2],
                                           'publish_time': publish_time}

            # print(blogs)
        else:
            print('result is  None')
            message = 'the blogs is null'
            return render(request, 'home.html', {'message': message})
        print('execute sql2 success')

        cursor.execute(sql3)
        print('execute sq3 success')
        if cursor is not None:  # 注意这里。单纯判断cursor是否为None是不够的
            result = cursor.fetchone()
            print('result', result)
            # 查找该用户name
            if result is not None:
                name = result[0]
    except:
        db.rollback()
        print('rollback')
        message = 'something error when fetch blogs'
        print(message)
        return render(request, 'home.html', {'message': message})
    user = {
        'name': name,
        'email': email,
    }
    return render(request, 'home.html', {'blogs': blogs, 'myBlogs': my_blogs, 'user': user})
    cursor.close()
    # 关闭数据库连接
    db.close()
    print('close db')


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

        sql2 = 'SELECT brief_info, phone, blog_url, user_identity, other, city, qq, wechat  FROM user_info_plus WHERE ID = "{}";'.format(
            db_ID)
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
                db_city = result[5]
                db_qq = result[6]
                db_wechat = result[7]
            else:  # 如果没有就使用默认的信息
                db_brief_info = "your brief information 200 words"
                db_phone = "123456"
                db_blog_url = "https://www.baidu.com/"
                db_identity = "student"
                db_other = "other information about you 255 words"
                db_city = "beijing"
                db_qq = '123456789'
                db_wechat = '123456789'
        else:  # 如果没有就使用默认的信息
            db_brief_info = "your brief information"
            db_phone = "123456"
            db_blog_url = "https://www.baidu.com/"
            db_identity = "student"
            db_other = "other information about you"
            db_city = "beijing"
            db_qq = '123456789'
            db_wechat = '123456789'
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

    gender = ['female', 'male'][db_gender]

    info = {
        'ID': db_ID,
        'name': db_name,
        'pwd': db_pass,
        'birthday': db_birthday,
        'gender': gender,
        'brief_info': db_brief_info,
        'phone': db_phone,
        'blog_url': db_blog_url,
        'identity': db_identity,
        'other': db_other,
        'email': email,
        'city': db_city,
        'qq': db_qq,
        'wechat': db_wechat,
    }
    return render(request, 'me.html', {'info': info})


# 写博客
@check_login
def writeBlog(request):
    blog = {}
    blog['blog_title'] = 'Enter blog title'
    blog['blog_abstract'] = 'Enter blog abstract'
    blog['blog_content'] = ''
    return render(request, 'writeblog.html', {'blog': blog})


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


# 修改用户信息
@check_login
def alter_info(request):
    email = request.session.get('email')
    if request.method == 'POST':
        # 获取用户名和密码
        name = request.POST.get('name')
        identity = request.POST.get('identity')
        gender = request.POST.get('gender')
        birthday = request.POST.get('birthday')
        pwd = request.POST.get('pwd')
        blog_url = request.POST.get('url')
        phone = request.POST.get('phone')
        qq = request.POST.get('qq')
        wechat = request.POST.get('wechat')
        city = request.POST.get('city')
        biref_info = request.POST.get('info')
        other = request.POST.get('other')

        print('------------------------')
        int_gender = 0
        if gender.lower() == 'male':
            int_gender = 1
        elif gender.lower() == 'female':
            int_gender = 0
        else:
            int_gender = 3

        # 连接数据库
        db = pymysql.connect(host='localhost', port=3306, user='root', passwd='', db='food_blog', charset='utf8mb4')
        # 创建游标
        cursor = db.cursor()
        # birthday 的异常处理，如果异常用之前的记录
        if '-' not in birthday:
            sql0 = 'SELECT user_birthday FROM `user` WHERE user_email="{}";'.format(email)
            cursor.execute(sql0)
            if cursor is not None:  # 注意这里。单纯判断cursor是否为None是不够的
                result = cursor.fetchone()
                print('result', result)
                # 判断是否有此消息
                if result is not None:
                    birthday = result[0]
        # SQL 查询语句
        sql = 'CALL modify_user_info("{}","{}", "{}", "{}", "{}", "{}", "{}","{}", {}, "{}","{}", "{}","{}", @msg);'.format(
            biref_info, other, phone, qq, wechat, blog_url, city, identity, int_gender, name, pwd, birthday, email)
        sql2 = 'SELECT @msg;'
        try:
            # 执行sql语句
            print(sql)
            cursor.execute(sql)
            print('execute sq success')
            cursor.execute(sql2)
            print('execute sq2 success')
            if cursor is not None:  # 注意这里。单纯判断cursor是否为None是不够的
                result = cursor.fetchone()
                print('result', result)
                # 判断是否有此消息
                if result is not None:
                    message = result[0]
            # 提交到数据库执行
            db.commit()
            print('execute sql success')
            # 设置message
            # message = 'blog draft save success'
            return render(request, 'modify_info_success.html', {'message': message})
        except:
            db.rollback()
            print('rollback')
            message = 'something error when alter information'
            print(message)
            return render(request, 'modify_info_success.html', {'message': message})
        cursor.close()
        # 关闭数据库连接
        db.close()
        print('close db')
    elif request.method == 'GET':
        return redirect('/user/me')


# 保存草稿
@check_login
def save_draft(request):
    email = request.session['email']
    print('---------save blog draft ---------')
    if request.method == 'POST':
        title = request.POST.get('title')
        blog_content = request.POST.get('blog')
        blog_abstract = request.POST.get('abstract')
        now_time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M')

        print('------------------------------')
        # print(title)
        # print(blog_content)
        # 连接数据库
        db = pymysql.connect(host='localhost', port=3306, user='root', passwd='', db='food_blog', charset='utf8')
        print('connect db success')
        # 创建游标
        cursor = db.cursor()

        if request.session['modify'] == 0:
            sql = 'CALL save_blog("{}","{}","{}","{}","{}", 1, 7, @msg);'.format(title, blog_abstract, blog_content,
                                                                                 now_time, email)

        else:
            sql = 'CALL save_blog("{}","{}","{}","{}","{}", 2, {}, @msg);'.format(title, blog_abstract, blog_content,
                                                                                  now_time, email,
                                                                                  request.session['bid'])
            del request.session['bid']
            request.session['modify'] = 0
        # 选择sql的执行结果
        sql2 = 'SELECT @msg;'
        try:
            # 执行sql语句
            cursor.execute(sql)
            print('execute sql success')
            cursor.execute(sql2)
            print('execute sq2 success')
            if cursor is not None:  # 注意这里。单纯判断cursor是否为None是不够的
                result = cursor.fetchone()
                print('result', result)
                # 判断是否有此用户
                if result is not None:
                    message = result[0]
            # 提交到数据库执行
            db.commit()
            print('execute sql success')
            # 设置message
            # message = 'blog draft save success'
            return render(request, 'writeblog_plus.html', {'message': message})
        except:
            # Rollback in case there is any error
            db.rollback()
            print('rollback')
            message = 'some thing error please resave'
            return render(request, 'writeblog_plus.html', {'message': message})
        cursor.close()
        # 关闭数据库连接
        db.close()
        print('close db')

    elif request.method == 'GET':
        return redirect('/user/witeBlog')


# 发布文章
@check_login
def blog_deploy(request):
    email = request.session['email']
    print('-------blog deploy--------')
    if request.method == 'POST':
        title = request.POST.get('title')
        blog_content = request.POST.get('blog')
        blog_abstract = request.POST.get('abstract')
        now_time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M')
        print('------------------------------')
        # print(title)
        # print(blog_content)
        print(blog_abstract)
        # 连接数据库
        db = pymysql.connect(host='localhost', port=3306, user='root', passwd='', db='food_blog', charset='utf8')
        print('connect db success')
        # 创建游标
        cursor = db.cursor()
        # 如果是直接发布的
        if request.session['modify'] == 0:
            # sql语句
            # （）实现多行字符串连接
            # ID为自增ID所以不用进行赋值
            # {}作为占位符
            # 两个语句必须分成两次执行
            sql1 = 'INSERT INTO blog(blog_title, blog_content, blog_modified, blog_excerpt) ' + 'VALUES("{}", "{}", "{}", "{}"); '.format(
                title,
                blog_content,
                now_time, blog_abstract)
            sql2 = 'INSERT INTO publish_blog(ID, blog_id, publish_time) ' + 'SELECT ID,LAST_INSERT_ID(),"{}" FROM `user` WHERE user_email="{}";'.format(
                now_time, email)
        else:  # 如果是先修改后发布的
            sql1 = 'UPDATE blog SET blog_title = "{}", blog_excerpt="{}", blog_content="{}", blog_modified="{}" WHERE blog_id = {};'.format(
                title, blog_abstract, blog_content, now_time, request.session['bid'])
            sql2 = 'UPDATE publish_blog SET publish_time="{}" WHERE blog_id={};'.format(now_time,
                                                                                        request.session['bid'])
            del request.session['bid']
            request.session['modify'] = 0

        try:
            # 执行sql语句
            cursor.execute(sql1)
            print('execute sql1 success')
            # if deploy == 1:
            cursor.execute(sql2)
            print('execute sql2 success')
            # 提交到数据库执行
            db.commit()
            # 设置message
            message = 'blog deploy success'
        except:
            # Rollback in case there is any error
            db.rollback()
            print('rollback')
            message = 'some thing error please redeploy'
        return render(request, 'writeblog_plus.html', {'message': message})
        cursor.close()
        # 关闭数据库连接
        db.close()
        print('close db')

    elif request.method == 'GET':
        return redirect('/user/witeBlog')


# 查看博客
def see_blog(request, bid):
    # print(bid)
    # 连接数据库
    db = pymysql.connect(host='localhost', port=3306, user='root', passwd='', db='food_blog', charset='utf8mb4')
    print('connect database success')

    # 创建游标
    cursor = db.cursor()
    # 创建视图
    sql1 = 'CREATE VIEW browse_blog AS SELECT u.user_name, u.user_email, b.blog_title, b.blog_excerpt, b.blog_content, b.blog_modified FROM blog b, publish_blog p, `user` u WHERE b.blog_id = p.blog_id AND u.ID = p.ID AND  b.blog_id = {};'.format(
        bid)
    # 查询视图
    sql2 = 'SELECT * FROM browse_blog;'
    # 删除该视图
    sql3 = 'DROP VIEW browse_blog;'
    blog = {}
    try:
        # 执行SQL 1 语句
        cursor.execute(sql1)
        print('execute create view success ')
        cursor.execute(sql2)
        print('success select data from view')
        # 获取所有记录列表
        if cursor is not None:  # 注意这里。单纯判断cursor是否为None是不够的
            result = cursor.fetchone()
            print('result', result)
            # 判断是否有此用户
            if result is not None:
                blog['user_name'] = result[0]
                blog['user_email'] = result[1]
                blog['blog_id'] = bid
                blog['blog_title'] = result[2]
                blog['blog_abstract'] = result[3]
                # print(result[4])
                # a = repr(result[4])[1:-1]
                # print(a)
                blog['blog_content'] = repr(result[4])[1:-1]
                print(blog['blog_content'])
                blog['blog_modified'] = result[5]
            else:
                print('result is  None')
                print('this user not exist')
                message = 'this user not exist, please reload this page or log in again'
                return render(request, 'blog.html', {'message': message})
        else:
            print('cursor is None')
            print('this user not exist')
            message = 'this user not exist, please reload this page or log in again'
            return render(request, 'blog.html', {'message': message})
        # 执行SQL 3 删除该视图语句
        cursor.execute(sql3)
        # db.commit()
    except:
        db.rollback()
        print('rollback')
        message = 'something error, please reload this page or log in again'
        return render(request, 'blog.html', {'message': message})

    cursor.close()
    # 关闭数据库连接
    db.close()
    print('close db')
    return render(request, 'blog.html', {'blog': blog})


@check_login
def blog_modify(request, bid):
    # print(bid)
    email = request.session['email']
    # 连接数据库
    db = pymysql.connect(host='localhost', port=3306, user='root', passwd='', db='food_blog', charset='utf8mb4')
    print('connect database success')

    # 创建游标
    cursor = db.cursor()

    sql1 = 'SELECT u.user_email FROM publish_blog p, `user` u WHERE p.ID = u.ID AND blog_id={};'.format(bid)
    try:
        # 执行SQL 1 语句
        cursor.execute(sql1)
        # 获取所有记录列表
        if cursor is not None:  # 注意这里。单纯判断cursor是否为None是不够的
            result = cursor.fetchone()
            # print('result', result)
            if result is not None:
                if email == result[0]:
                    request.session['modify'] = 1
                    request.session['bid'] = bid
                    # SQL 查询语句
                    sql2 = 'SELECT blog_title, blog_excerpt, blog_content FROM blog WHERE blog_id={};'.format(bid)

                    blog = {}
                    try:
                        cursor.execute(sql2)
                        print('success select data from view')
                        # 获取所有记录列表
                        if cursor is not None:  # 注意这里。单纯判断cursor是否为None是不够的
                            result = cursor.fetchone()
                            # print('result', result)
                            if result is not None:
                                blog['blog_id'] = bid
                                blog['blog_title'] = result[0]
                                blog['blog_abstract'] = result[1]
                                blog['blog_content'] = result[2]
                            else:
                                print('result is  None')
                                message = 'this blog not exist'
                                return render(request, 'writeblog.html', {'alert': message})
                        else:
                            print('cursor is None')
                            message = 'this blog not exist'
                            return render(request, 'writeblog.html', {'alert': message})
                    except:
                        db.rollback()
                        print('rollback')
                        message = 'something error, please reload this page or log in again'
                        return render(request, 'writeblog.html', {'alert': message})

                    return render(request, 'writeblog.html', {'blog': blog})
                else:
                    message = 'your are not the author of this blog'
                    return render(request, 'writeblog_plus.html', {'message': message})
            else:
                print('result is  None')
                message = 'this blog not exist'
                return render(request, 'writeblog.html', {'alert': message})
        else:
            print('cursor is None')
            print('this user not exist')
            message = 'this user not exist, please reload this page or log in again'
            return render(request, 'writeblog.html', {'alert': message})
    except:
        db.rollback()
        print('rollback')
        message = 'something error, please reload this page or log in again'
        return render(request, 'writeblog.html', {'alert': message})

    cursor.close()
    # 关闭数据库连接
    db.close()
    print('close db')


# 用户注销
@check_login
def log_off(request):
    # 连接数据库
    email = request.session['email']
    del request.session['is_login']
    del request.session['email']
    db = pymysql.connect(host='localhost', port=3306, user='root', passwd='', db='food_blog', charset='utf8')
    print('connect db success')
    # 创建游标
    cursor = db.cursor()
    # 删除发布的博客
    sql1 = 'DELETE b,p FROM blog b, publish_blog p WHERE b.blog_id = p.blog_id AND p.ID = ( SELECT ID FROM `user` u WHERE u.user_email = "{}" );'.format(
        email)
    # 删除用户检索garbage的信息
    sql2 = 'DELETE s FROM `user` u, search s WHERE u.ID = s.ID AND u.user_email= "{}";'.format(email)
    # 删除用户附加信息
    sql3 = 'DELETE FROM user_info_plus WHERE ID = (SELECT ID FROM `user` WHERE user_email="{}");'.format(email)
    # 删除用户登陆信息
    sql4 = 'DELETE FROM login WHERE ID = (SELECT ID FROM `user` WHERE user_email="{}");'.format(email)
    # 删除用户信息
    sql5 = 'DELETE FROM `user` WHERE user_email = "{}";'.format(email)
    try:
        # 执行sql语句
        cursor.execute(sql1)
        cursor.execute(sql2)
        cursor.execute(sql3)
        cursor.execute(sql4)
        cursor.execute(sql5)
        # 提交到数据库执行
        db.commit()
        print('execute sql success')
        print('user log off success')
        return render(request, 'logOff.html')
        # return render(request, 'home')
    except:
        # Rollback in case there is any error
        db.rollback()
        print('rollback')
        message = 'some thing error, data base rollback'
        return render(request, 'home.html', {'message': message})
    cursor.close()
    # 关闭数据库连接
    db.close()
    print('close db')


# 删除blog
@check_login
def delete_blog(request, bid):
    # 连接数据库
    db = pymysql.connect(host='localhost', port=3306, user='root', passwd='', db='food_blog', charset='utf8')
    print('connect db success')
    # 创建游标
    cursor = db.cursor()
    # 删除发布的博客
    # sql1 = 'DELETE b,p FROM blog b, publish_blog p WHERE b.blog_id = p.blog_id AND b.blog_id = {};'.format(
    #     bid)
    sql1 = 'DELETE FROM publish_blog WHERE blog_id={};'.format(bid)
    sql2 = 'DELETE FROM blog WHERE blog_id={};'.format(bid)
    try:
        print(sql1)
        # 执行sql语句
        cursor.execute(sql1)
        cursor.execute(sql2)
        # 提交到数据库执行
        db.commit()
        print('execute sql success')
        print('blog ' + bid + ' delete success')
        message = 'blog ' + bid + ' delete success'
        return render(request, 'blog_delete.html', {'message': message})
    except:
        # Rollback in case there is any error
        db.rollback()
        print('rollback')
        message = 'something error delete blog fail'
        return render(request, 'blog_delete.html', {'message': message})
    cursor.close()
    # 关闭数据库连接
    db.close()
    print('close db')


@check_login
def garbage_search(request):
    if request.method == 'POST':
        email = request.session['email']
        garbage = request.POST.get('garbage')
        now_time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M')

        # 连接数据库
        db = pymysql.connect(host='localhost', port=3306, user='root', passwd='', db='food_blog', charset='utf8mb4')
        print('connect database success')

        # 创建游标
        cursor = db.cursor()
        # 创建视图
        sql1 = 'SELECT g.garbage_name, c.garbage_catgory_name, g.garbage_description, g.garbage_img, c.garbage_category_description FROM garbage g, garbage_catgory c WHERE g.garbage_catgory_id = c.garbage_catgory_id AND g.garbage_name LIKE "%{}%";'.format(garbage)
        # 查询视图
        sql2 = 'INSERT INTO search(ID, garbage_name, search_time) VALUES( (SELECT ID FROM `user` WHERE user_email = "{}"), "{}", "{}"); '.format(
            email, garbage, now_time)
        # 删除该视图
        garbages = {}
        try:
            # print(sql2)
            # print(sql1)
            cursor.execute(sql2)
            # 执行SQL 1 语句
            cursor.execute(sql1)
            print('select garbages success')

            if cursor is not None:  # 注意这里。单纯判断cursor是否为None是不够的
                db_garbages = cursor.fetchall()
                for db_garbage in db_garbages:
                    garbages[db_garbage[0]] = {'category_name': db_garbage[1], 'garbage_description': db_garbage[2], 'img': db_garbage[3], 'category_description': db_garbage[4]}
                # 必须得commit数据库才能看到
                db.commit()
                return render(request, 'garbage.html', {'garbages': garbages})
            else:
                print('result is  None')
                message = 'the garbage is null'
                db.commit()
                return render(request, 'garbage.html', {'message': message})
            print('execute sql success')

        except:
            db.rollback()
            print('rollback')
            message = 'something error, please research again'
            return render(request, 'home.html', {'message': message})

        cursor.close()
        # 关闭数据库连接
        db.close()
        print('close db')
    elif request.method == 'GET':
        return redirect('/user/home')
