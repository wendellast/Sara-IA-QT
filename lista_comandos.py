from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5 import QtGui, QtCore
from PyQt5.QtGui import QMovie
from plyer import notification
from PyQt5.QtCore import QProcess
from rich import print
import sys

class JanelaC (QMainWindow):
	def __init__(self):
		super().__init__()
		
		self.label_JG = QLabel(self)
		self.label_JG.setText("LISTA DE COMANDOS")
		self.label_JG.setAlignment(QtCore.Qt.AlignRight)
		self.label_JG.move(5,5)
		self.label_JG.setStyleSheet('QLabel {font-size:18px; color: #DB7399;font:bold}')
		self.label_JG.resize(195,20)
		##DB7399
		ListaC = QListWidget(self)
		ListaC.setGeometry(5, 30, 290, 370)
		#ListaC.setStyleSheet('background-color:black;color:blue')
		ListaC.setStyleSheet("""
		QListWidget::item{
            color: #9E6778;
            background-color:transparent;}
            
		QScrollBar:vertical{       
            border:none;
            background: #F2B8B1;
            width:3px;
            margin:0px;}
            
        QScrollBar::handle:vertical{
            background: #F2BFB1;
            min-height:0px;}
            
        QScrollBar::add-line:vertical{
            background: #F2D3CD;
            height: 0px;
            subcontrol-position:bottom;
            subcontrol-origin:margin;}
            
        QScrollBar::sub-line:vertical{
            background: #F2D3CD;
            height:0px;
            subcontrol-position:top;
            subcontrol-origin:margin;}
        """)
        

		ls = ['sara','historico','silencio','horas','aprenda','bateria','easter egg','relatório','cadastro','tira print','login','pesquisa','resumo',
        'data','abrir arquivos', 'criar arquivo', 'criar pasta','música','remover arquivo','remover pasta','editar arquivo','renomear arquivo','renomear pasta', 'esvaziar lixeira', 'abrir calculadora','playlist','desligar','temperatura do sistema','escreva','quanto é']
		ListaC.addItems(ls)

		botao_fechar = QPushButton("",self)
		botao_fechar.move(270,5)
		botao_fechar.resize(20,20)
		botao_fechar.setStyleSheet("background-image : url(img/fechar.png);border-radius: 15px;") 
		botao_fechar.clicked.connect(self.fechartudo)
			
		self.CarregarJanela()
		
	def CarregarJanela(self):
		self.setWindowFlag(Qt.FramelessWindowHint)
		self.setGeometry(50,50,300,410)
		self.setMinimumSize(300, 410)
		self.setMaximumSize(300, 410)
		self.setWindowOpacity(0.95) 
		#self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
		self.setStyleSheet("background-color: #F2B8B1")
		self.setWindowIcon(QtGui.QIcon('img/sara_icon.png'))
		self.setWindowTitle("COMANDOS")
		self.show()
	
	def fechartudo(self):
		print('botao fechar presionado')
		sys.exit()
	
	def mousePressEvent(self, event):
		if event.buttons() == Qt.LeftButton:
			self.dragPos = event.globalPos()
			event.accept()
    
	def mouseMoveEvent(self, event):
		if event.buttons() == Qt.LeftButton:
			self.move(self.pos() + event.globalPos() - self.dragPos)
			self.dragPos = event.globalPos()
			event.accept()
	
aplicacao = QApplication(sys.argv)
j = JanelaC()
sys.exit(aplicacao.exec_())
