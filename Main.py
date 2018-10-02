# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'voca.ui'
#
# Created by: PyQt5 UI code generator 5.11.2
#
# WARNING! All changes made in this file will be lost!
import pandas as pd
from pandas.tseries.offsets import *
from random import *
from datetime import datetime as dt
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QFont
from PyQt5.QtCore import QTime
import time
import sys
import pickle, os
import pygame
import urllib 
def addlist_(a,b):
	for i in b:
		a.append(i)
	return a
class Ui_Form(object):
	def setupUi(self, Form):
		Form.setObjectName("Form")
		Form.resize(400, 300)
		self.widget = QtWidgets.QWidget(Form)
		self.widget.setGeometry(QtCore.QRect(111, 240, 158, 25))
		self.widget.setObjectName("widget")
		self.horizontalLayout = QtWidgets.QHBoxLayout(self.widget)
		self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
		self.horizontalLayout.setObjectName("horizontalLayout")
		self.pushButton_2 = QtWidgets.QPushButton(self.widget)
		self.pushButton_2.setObjectName("pushButton_2")
		self.horizontalLayout.addWidget(self.pushButton_2)
		self.pushButton = QtWidgets.QPushButton(self.widget)
		self.pushButton.setObjectName("pushButton")
		self.horizontalLayout.addWidget(self.pushButton)
		self.widget1 = QtWidgets.QWidget(Form)
		self.widget1.setGeometry(QtCore.QRect(67, 164, 239, 25))
		self.widget1.setObjectName("widget1")
		self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.widget1)
		self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
		self.horizontalLayout_2.setObjectName("horizontalLayout_2")
		self.pushButton_3 = QtWidgets.QPushButton(self.widget1)
		self.pushButton_3.setObjectName("pushButton_3")
		self.horizontalLayout_2.addWidget(self.pushButton_3)
		self.pushButton_5 = QtWidgets.QPushButton(self.widget1)
		self.pushButton_5.setObjectName("pushButton_5")
		self.horizontalLayout_2.addWidget(self.pushButton_5)
		self.pushButton_4 = QtWidgets.QPushButton(self.widget1)
		self.pushButton_4.setObjectName("pushButton_4")
		self.horizontalLayout_2.addWidget(self.pushButton_4)
		self.widget2 = QtWidgets.QWidget(Form)
		self.widget2.setGeometry(QtCore.QRect(31, 23, 120, 25))
		self.widget2.setObjectName("widget2")
		self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.widget2)
		self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
		self.horizontalLayout_3.setObjectName("horizontalLayout_3")
		self.label = QtWidgets.QLabel(self.widget2)
		self.label.setObjectName("label")
		self.horizontalLayout_3.addWidget(self.label)
		self.time='25:00'
		self.lcdNumber = QtWidgets.QLCDNumber(self.widget2)
		self.lcdNumber.setObjectName("lcdNumber")
		self.lcdNumber.display(self.time) 
		self.horizontalLayout_3.addWidget(self.lcdNumber)
		self.widget3 = QtWidgets.QWidget(Form)
		self.widget3.setGeometry(QtCore.QRect(310, 226, 77, 54))
		self.widget3.setObjectName("widget3")
		self.verticalLayout = QtWidgets.QVBoxLayout(self.widget3)
		self.verticalLayout.setContentsMargins(0, 0, 0, 0)
		self.verticalLayout.setObjectName("verticalLayout")
		self.pushButton_6 = QtWidgets.QPushButton(self.widget3)
		self.pushButton_6.setObjectName("pushButton_6")
		self.verticalLayout.addWidget(self.pushButton_6)
		self.pushButton_7 = QtWidgets.QPushButton(self.widget3)
		self.pushButton_7.setObjectName("pushButton_7")
		self.verticalLayout.addWidget(self.pushButton_7)
		self.widget4 = QtWidgets.QWidget(Form)
		self.widget4.setGeometry(QtCore.QRect(130, 80, 150, 50))
		self.widget4.setObjectName("widget4")
		self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.widget4)
		self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
		self.verticalLayout_2.setObjectName("verticalLayout_2")
		self.label_2 = QtWidgets.QLabel(self.widget4)
		self.label_2.setObjectName("label_2")
		self.verticalLayout_2.addWidget(self.label_2)
		self.label_3 = QtWidgets.QLabel(self.widget4)
		self.label_3.setObjectName("label_3")
		self.verticalLayout_2.addWidget(self.label_3)
		self.retranslateUi(Form)
		QtCore.QMetaObject.connectSlotsByName(Form)
		self.textBrowser = QtWidgets.QTextBrowser(Form)
		self.textBrowser.setGeometry(QtCore.QRect(85, 70, 200, 80))
		self.textBrowser.setObjectName("textBrowser")
		
		self.textBrowser.setPlainText("")
	def retranslateUi(self, Form):
		_translate = QtCore.QCoreApplication.translate
		Form.setWindowTitle(_translate("Form", "单词记忆"))
		self.pushButton_2.setText(_translate("Form", "上一个"))
		self.pushButton_2.clicked.connect(self.foward)
		self.pushButton.setText(_translate("Form", "下一个"))
		self.pushButton.clicked.connect(self.next)
		self.pushButton_3.setText(_translate("Form", "完全记得"))
		self.pushButton_3.clicked.connect(self.pop_)
		self.pushButton_5.setText(_translate("Form", "有印象"))
		self.pushButton_4.setText(_translate("Form", "完全忘记"))
		self.label.setText(_translate("Form", "学习时间"))
		self.pushButton_6.setText(_translate("Form", "开始"))
		self.pushButton_6.clicked.connect(self.start)
		self.pushButton_7.setText(_translate("Form", "重新开始"))
		self.pushButton_7.clicked.connect(self.reset)
	def read_(self,word):
		w=word
		if '?' in w:
			w=w.replace('?','')
		url='https://fanyi.baidu.com/gettts?lan=uk&text='+w+'&spd=3&source=web'
		urllib.request.urlretrieve(url,'C://'+w+'.mp3')
		track = pygame.mixer.music.load('C://'+w+'.mp3')
		pygame.mixer.music.play()
		time.sleep(1)
		pygame.mixer.music.stop()
	def reset(self):
		if os.path.exists('C://log_pop_index.txt'):
			os.remove('C://log_pop_index.txt')
		if os.path.exists('C://log_index.txt'):
			os.remove('C://log_index.txt')
		if os.path.exists('C://log_date.txt'):
			os.remove('C://log_date.txt')
		if os.path.exists('C://log_plans.txt'):
			os.remove('C://log_plans.txt')
		print('已重置！')
	def pop_(self):
		global i
		if list(todayvocab[i%len(todayvocab)].values())[1] not in log_pop_index:
			log_pop_index.append(list(todayvocab[i%len(todayvocab)].values())[1])
		f=open('C://log_pop_index.txt','wb')
		pickle.dump(log_pop_index,f)
		f.close()
	def next(self):
		global i
		if len(todayvocab)==0:
			self.start()
		i+=1
		_translate = QtCore.QCoreApplication.translate
		self.textBrowser.setPlainText("")
		self.textBrowser.append('''<font size="5" color="blue"><p>'''+list(todayvocab[i%len(todayvocab)].keys())[0]+'</p>'+'</font>'+'''<font size="5" color="red"><p>'''+list(todayvocab[i%len(todayvocab)].values())[0]+'</p>'+'</font>')
		self.read_(list(todayvocab[i%len(todayvocab)].keys())[0])
		#print(list(todayvocab[i%len(todayvocab)].values())[1],log_pop_index)
	def foward(self):
		global i
		if len(todayvocab)==0:
			self.start()
		i-=1
		if i>=1:
			self.textBrowser.setPlainText("")
			self.textBrowser.append('''<font size="5" color="blue"><p>'''+list(todayvocab[i%len(todayvocab)].keys())[0]+'</p>'+'</font>'+'''<font size="5" color="red"><p>'''+list(todayvocab[i%len(todayvocab)].values())[0]+'</p>'+'</font>')
			self.read_(list(todayvocab[i%len(todayvocab)].keys())[0])
			#print(list(todayvocab[i%len(todayvocab)].values())[1],log_pop_index)
	def start(self):
		global c
		c+=1
		print('开始了！')
		global df
		global log_pop_index
		date_=[]
		try:
			f=open('C://log_index.txt','rb')
			old_index=pickle.load(f)
			f.close()
		except:
			old_index=[]
		try:
			f=open('C://log_pop_index.txt','rb')#舍弃掉的单词索引
			log_pop_index=pickle.load(f)
			f.close()
		except:
			log_pop_index=[]
		try:
			f=open('C://log_date.txt','rb')
			today=pickle.load(f)
			f.close()
		except:
			today=[]
		try:
			f=open('C://log_plans.txt','rb')
			Plans=pickle.load(f)
			f.close()
		except:
			Plans=[]
		if c<=1:
			for i in range(n):
				t=randint(1,len(df.index))
				while t in index or t in old_index:
					t=randint(1,len(df.index))
				index.append(t)
			for i in Plans:
				date_.append(i['date'])
			for i in index:
				if i not in log_pop_index:
					todayvocab.append({df.iloc[i,:2][0]:df.iloc[i,:2][1],'index':i})
			for i in Plans:
				if i['date']==str(pd.datetime.now()).split(':')[0][:-3]:
					for j in i['index']:
						if j not in log_pop_index:
							todayvocab.append({df.iloc[j,:2][0]:df.iloc[j,:2][1],'index':j})
			shuffle(todayvocab)#打乱顺序
			print('今日单词数量',len(todayvocab),'\n单词总量',len(df.index),'\n剩余单词',len(df.index)-len(log_pop_index))
			if str(pd.datetime.now()).split(':')[0][:-3] not in today:
				today.append(str(pd.datetime.now()).split(':')[0][:-3])
				for i in s:
					d=str(pd.datetime.now()+DateOffset(days=i)).split(':')[0][:-3]
					# print(d,date_)
					if d not in date_:
						Plans.append({'date':d,'index':index})
					else:
						for j in Plans:
							if j['date']==d:
								t=j['index'][:]
								for i in index: 
									if i not in log_pop_index:
										t.append(i)
								j['index']=t[:]
				for i in index:
					old_index.append(i)
				print('today',today,'\n index',index,'\n'+'todayvocab',todayvocab,'\n Plans',Plans)
				f=open('C://log_plans.txt','wb')
				pickle.dump(Plans,f)
				f.close()
				f=open('C://log_date.txt','wb')
				pickle.dump(today,f)
				f.close()
				f=open('C://log_index.txt','wb')
				pickle.dump(old_index,f)
				f.close()

if __name__ == "__main__":
	pygame.mixer.init()
	s=[1,2,4,7,15,30]
	todayvocab=[]
	index=[]
	n=10
	Plans=[]
	i=0
	c=0
	today=[]
	old_index=[]
	log_pop_index=[]
	path2='C://Users/Administrator/Desktop/新词汇.csv'
	f = open(path2)
	df=pd.read_csv(f, sep=',',low_memory=False,header=None)
	app = QtWidgets.QApplication(sys.argv)
	MainWindow = QtWidgets.QMainWindow()
	ui = Ui_Form()
	ui.setupUi(MainWindow)
	MainWindow.show()
	sys.exit(app.exec_())
