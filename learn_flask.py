# -*- coding: cp936 -*-
from flask import Flask,url_for,render_template
import datetime
import json
import random


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
# cnt = 0
class Article(object):
	def __init__(self,id,title="default title",author="default author",content='hello world'):
		self.id = id
		self.title = title
		self.author = author
		self.content = content
		self.gen_random()
	def gen_random(self):
		self.title = random.choice(['News','Joke','Info'])+str(random.choice(range(999)))
		self.author =random.choice(['Stave Jobs','Bill Gats','Adam Sang'])
		self.content = 1*('test content: \nid = %s\n title = %s\n author = %s\n' %(self.id,self.title,self.author))

	
art_arr = []
for i in range(50):
	art_arr.append(Article(id = i))
art_dic = {}
for i in range(50):
	art = Article(id = i)
	art_dic[art.id] = art

@app.route('/')
@app.route('/main')
def go():
	# return render_template()
	str_now = datetime.datetime.now().strftime('%y%m%d %H:%M:%S')
	url =  url_for('static',filename = 'main.css')
	# return link+'<h1>datetime</h1>'+str_now+' static_url='+url
	return render_template('base.html')
# def head():
# 	return 'Hello flask'

@app.route('/404')
def show404():
	return link+'<h1>404 not found</h1>'

@app.route('/about')
def show_about():
	# return link+'about page'
	return render_template('about.html')

@app.route('/list')


def show_list():
	return render_template('list.html',art_dic = art_dic)


@app.route('/article/<id>')
def show_article(id):
	# return '<h1>'+title+'</h1>'
	return render_template("article.html",a =art_dic[int(id)])

# @app.route(url_for(static),filename='main.css')
# pass

if __name__ == '__main__':
	app.run(debug= True)

