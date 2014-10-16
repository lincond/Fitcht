#!/usr/bin/python
#-*-coding: utf-8 -*-

# clientServer.py
# @author: Lincon Dias

import sys
import socket
import select
import urllib2
import console
import time
import thread

class Server():

	#Variaveis globais
	global IP
	global PORT
	global BUFFER

	#Construtor
	def __init__(self):
		#Versao
		self.version = '0.0.1a'
		print "Servidor inciado, versao " + self.version

		#Programa esta rodando.
		self.isRunnig = True

		#Variaveis para o socket
		self.PORT = 10647
		self.IP = self.myIP()
		self.BUFFER = 4096

		#Listas
		self.CONNECTION_LIST = []
		self.USERS_LIST = []
		self.FILES_LIST = []

		#Incia o socket para conectar no fitserver 
		self.host_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		self.host_socket.socket.settimeout(2)
		try:
			self.host_socket.connect((host, self.PORT))
		except:
			print "Impossivel conectar a essa sala, tenha certeza que o IP esta correto"

		print "Sala de arquivos iniciada em " + self.IP + ":" + self.PORT

		#Inicia a thread
		thread.start_new_thread(self.listen_thread, (self.host_socket, self.CONNECTION_LIST, self.USERS_LIST, self.FILES_LIST))

		#Console para o servidor fazer alterações
		self.con = console.Console(1)

	#Caputra o ip
	def myIP(self):
		self.myip = urllib2.urlopen("http://myip.dnsdynamic.org/").read()
		return self.myip

	#Thread de verificações
	def listenThread(self, hsock, lista, users, files):
		#Variaveis para tratar
		self.CONNECTION_LIST = lista
		self.USERS_LIST = users
		self.FILES_LIST = files
		self.host_socket = hsock

		self.read_sockets, self.write_sockets, self.error_sockets = select.select(self.CONNECTION_LIST, [], [])

		for sock in self.read_sockets:
			if sock == self.host_socket:
				self.sockfd, self.addr = self.host_socket.accept()
				self.CONNECTION_LIST.append(self.sockfd)
				print "Cliente (%s, %s) conectado" %self.addr
				self.usr = "(%s, %s)" %self.addr
				self.USERS_LIST.append(self.usr)
				self.prompt()
			else:
				try:
					self.data = sock.recv(self.BUFFER)
					if self.data:
						print self.data

				except:
					print "Cliente (%s, %s) esta offline" %self.addr
					sock.close()
					self.CONNECTION_LIST.remove(sock)
					self.USERS_LIST.remove(usr)
					self.prompt()
					continue

		time.sleep(2)

	#Função para printar o prompt na tela
	def prompt(self):
		sys.stdout.write(">")
		sys.stdout.flush()