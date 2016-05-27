# -*- coding: cp936 -*-
from flask import Flask,url_for
import datetime


app = Flask(__name__)
link = '''
<h2>Flask Blog</h2>
<small>how to use Flask</small>
<ul>
	<li><a href="/404">404</a></li>
	<li><a href="/">main</a></li>
	<li><a href="/about">about</a></li>
	<!-- <li><a href=""></a></li> -->
	<!-- <li><a href=""></a></li> -->
</ul>
<hr>
'''


@app.route('/')
def go():
	str_now = datetime.datetime.now().strftime('%y%m%d %H:%M:%S')
	url =  url_for('static',filename = 'main.css')
	return link+'<h1>datetime</h1>'+str_now+' static_url='+url
# def head():
# 	return 'Hello flask'
@app.route('/404')
def show404():
	return link+'<h1>404 not found</h1>'
@app.route('/about')
def show_about():
	return link+'about page'
# @app.route('/<page_num>')
# def show_page(page_num):
# 	return link+'page num is %s' %(page_num)

if __name__ == '__main__':
	app.run(debug= True)

