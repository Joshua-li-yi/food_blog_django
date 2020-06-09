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
        if title == '':
            message = 'The tile can not be null'
            return render(request, 'writeblog_plus.html', {'message': message})

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


# 写博客
@check_login
def writeBlog(request):
    blog = {}
    blog['blog_title'] = 'Enter blog title'
    blog['blog_abstract'] = 'Enter blog abstract'
    blog['blog_content'] = ''
    return render(request, 'writeblog.html', {'blog': blog})