from flask import render_template
from app import app
import pymysql.cursors

@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Miguel'}
    posts = [
        {
            'author': {'username': 'John'},
            'body': 'Beautiful day in Portland!'
        },
        {
            'author': {'username': 'Susan'},
            'body': 'The Avengers movie was so cool!'
        }
    ]
    return render_template('index.html', title='Home', user=user, posts=posts)

@app.route('/database')
def database():
    connection = pymysql.connect(host='localhost',user='blogadmin',password='bl0gs1t3',db='orapyblog',charset='utf8mb4', cursorclass=pymysql.cursors.DictCursor)
    try:
      with connection.cursor() as cur:
          sql = "select b.id, b.title title, s.subject subject, bd.blog_detail blog_detail \
                    from blog b, subject s, blog_detail bd \
                   where b.id = bd.id \
                     and b.subject_id = s.id \
                     and s.id = 1"
          cur.execute(sql)
          orablogs = cur.fetchall()
    except:
      print("An exception occurred") 
    try:
      with connection.cursor() as cur:
          sql = "select b.id, b.title title, s.subject subject, bd.blog_detail blog_detail \
                    from blog b, subject s, blog_detail bd \
                   where b.id = bd.id \
                     and b.subject_id = s.id \
                     and s.id = 2"
          cur.execute(sql)
          psqlblogs = cur.fetchall()
    except:
      print("An exception occurred") 
    try:
      with connection.cursor() as cur:
          sql = "select b.id, b.title title, s.subject subject, bd.blog_detail blog_detail \
                    from blog b, subject s, blog_detail bd \
                   where b.id = bd.id \
                     and b.subject_id = s.id \
                     and s.id = 3"
          cur.execute(sql)
          mysqlblogs = cur.fetchall()
    except:
      print("An exception occurred") 
    try:
      with connection.cursor() as cur:
          sql = "select b.id, b.title title, s.subject subject, bd.blog_detail blog_detail \
                    from blog b, subject s, blog_detail bd \
                   where b.id = bd.id \
                     and b.subject_id = s.id \
                     and s.id = 4"
          cur.execute(sql)
          monblogs = cur.fetchall()
    except:
      print("An exception occurred") 
    try:
      with connection.cursor() as cur:
          sql = "select b.id, b.title title, s.subject subject, bd.blog_detail blog_detail \
                    from blog b, subject s, blog_detail bd \
                   where b.id = bd.id \
                     and b.subject_id = s.id \
                     and s.id = 5"
          cur.execute(sql)
          hadblogs = cur.fetchall()
    except:
      print("An exception occurred") 
    try:
      with connection.cursor() as cur:
          sql = "select b.id, b.title title, s.subject subject, bd.blog_detail blog_detail \
                    from blog b, subject s, blog_detail bd \
                   where b.id = bd.id \
                     and b.subject_id = s.id \
                     and s.id = 6"
          cur.execute(sql)
          cassblogs = cur.fetchall()
    except:
      print("An exception occurred") 
    return render_template('database.html', orablogs=orablogs,psqlblogs=psqlblogs,mysqlblogs=mysqlblogs,monblogs=monblogs,hadblogs=hadblogs,cassblogs=cassblogs)


@app.route('/programming')
def programming():
    prog = {'lang': 'Python'}
    return render_template('programming.html', prog=prog)

@app.route('/devops')
def devops():
    dev = {'devops': 'All new DevOps World for a DBA....Automation'}
    return render_template('devops.html', dev=dev)

@app.route('/script')
def script():
    script = {'lang': 'Python'}
    return render_template('script.html', script=script)

@app.route('/login')
def login():
    login = {'login': 'This is going to be the login page...When I get it working to create new blogs!'}
    return render_template('login.html', login=login)

@app.route('/about')
def about():
    connection = pymysql.connect(host='localhost',user='blogadmin',password='bl0gs1t3',db='orapyblog',charset='utf8mb4', cursorclass=pymysql.cursors.DictCursor)
    try: 
      with connection.cursor() as cursor:
          sql = "select about from site"
          cursor.execute(sql)
          about = cursor.fetchone()
    except:
      print("An exception occurred") 
    try: 
      with connection.cursor() as cursor1:
          sql1 = "select site_name from site"
          cursor1.execute(sql1)
          site = cursor1.fetchone()
    except:
      print("An exception occurred") 
    try:
      with connection.cursor() as cur2:
          sql2 = "select title from blog limit 10"
          cur2.execute(sql2)
          blogs = cur2.fetchall()
    except:
      print("An exception occurred") 
    return render_template('about.html', site=site, about=about, blogs=blogs)

@app.route('/oracle')
def oracle():
    connection = pymysql.connect(host='localhost',user='blogadmin',password='bl0gs1t3',db='orapyblog',charset='utf8mb4', cursorclass=pymysql.cursors.DictCursor)
    try:
      with connection.cursor() as cur:
          sql = "select b.title title, s.subject subject, bd.blog_detail blog_detail \
                    from blog b, subject s, blog_detail bd \
                   where b.id = bd.id \
                     and b.subject_id = s.id \
                     and s.id = 1"
          cur.execute(sql)
          blogs = cur.fetchall()
    except:
      print("An exception occurred") 
    return render_template('oracle.html', blogs=blogs)

@app.route('/postgres')
def postgres():
    connection = pymysql.connect(host='localhost',user='blogadmin',password='bl0gs1t3',db='orapyblog',charset='utf8mb4', cursorclass=pymysql.cursors.DictCursor)
    try:
      with connection.cursor() as cur:
          sql = "select b.title title, s.subject subject, bd.blog_detail blog_detail \
                    from blog b, subject s, blog_detail bd \
                   where b.id = bd.id \
                     and b.subject_id = s.id \
                     and s.id = 2"
          cur.execute(sql)
          blogs = cur.fetchall()
    except:
      print("An exception occurred") 
    return render_template('postgres.html', blogs=blogs)

@app.route('/mysql')
def mysql():
    connection = pymysql.connect(host='localhost',user='blogadmin',password='bl0gs1t3',db='orapyblog',charset='utf8mb4', cursorclass=pymysql.cursors.DictCursor)
    try:
      with connection.cursor() as cur:
          sql = "select b.title title, s.subject subject, bd.blog_detail blog_detail \
                    from blog b, subject s, blog_detail bd \
                   where b.id = bd.id \
                     and b.subject_id = s.id \
                     and s.id = 3"
          cur.execute(sql)
          blogs = cur.fetchall()
    except:
      print("An exception occurred") 
    return render_template('mysql.html', blogs=blogs)

@app.route('/mongodb')
def mongodb():
    connection = pymysql.connect(host='localhost',user='blogadmin',password='bl0gs1t3',db='orapyblog',charset='utf8mb4', cursorclass=pymysql.cursors.DictCursor)
    try:
      with connection.cursor() as cur:
          sql = "select b.title title, s.subject subject, bd.blog_detail blog_detail \
                    from blog b, subject s, blog_detail bd \
                   where b.id = bd.id \
                     and b.subject_id = s.id \
                     and s.id = 4"
          cur.execute(sql)
          blogs = cur.fetchall()
    except:
      print("An exception occurred") 
    return render_template('mongodb.html', blogs=blogs)

@app.route('/hadoop')
def hadoop():
    connection = pymysql.connect(host='localhost',user='blogadmin',password='bl0gs1t3',db='orapyblog',charset='utf8mb4', cursorclass=pymysql.cursors.DictCursor)
    try:
      with connection.cursor() as cur:
          sql = "select b.title title, s.subject subject, bd.blog_detail blog_detail \
                    from blog b, subject s, blog_detail bd \
                   where b.id = bd.id \
                     and b.subject_id = s.id \
                     and s.id = 5"
          cur.execute(sql)
          blogs = cur.fetchall()
    except:
      print("An exception occurred") 
    return render_template('hadoop.html', blogs=blogs)

@app.route('/blog/<p_blog>')
def test(p_blog):
    connection = pymysql.connect(host='localhost',user='blogadmin',password='bl0gs1t3',db='orapyblog',charset='utf8mb4', cursorclass=pymysql.cursors.DictCursor)
    try:
      with connection.cursor() as cur:
          sql = "select b.title title, bd.blog_detail blog_detail \
                    from blog b, subject s, blog_detail bd \
                   where b.id = bd.id \
                     and b.subject_id = s.id \
                     and b.id = " + p_blog
          cur.execute(sql)
          blogs = cur.fetchall()
    except:
      print("An exception occurred") 
    return render_template('blog.html', blogs=blogs)


