#!/usr/bin/python
#-*-coding: utf-8 -*-

# console.py
# @author: Lincon Dias

import sys
import clientServer

class Console():
	
	#Construtor
	def __init__(self, local):
		#Console Version
		self.version = '0.0.1a'
		print "Console Inciado, versao " + self.version

		#Em qual lugar o console esta?
		self.local = local

		#Programa esta rodando.
		self.isRunnig = True

		#Chama a primeira captura de argumentos.
		while self.isRunnig:
			self.est = self.core(self.getNextValue(), local)

	#Retorna uma entrada de dados.
	def getNextValue(self):
		self.val1 = raw_input(">")
		return self.val1

	#Inicia algum processo recebido pelo console.
	def init(self, processName):
		print "Incializando componente " + processName
		if processName == "/start":
			self.server = clientServer.Server()
		else:
			sys.exit()

	#Coração do Console.
	def core(self, value, local):
		self.value = value

		self.local = local

		#Lista de comandos disponives no menu principal.
		#Locais (0 - Menu Principal, 1 - Server, 2 - Cliente)
		if self.local == 0:
			self.commands = ["/start", "/join", "/help", "/exit", "/version"]
			self.par1 = 4

		if self.local == 1:
			self.commands = ["/add", "/list", "/help", "/stop", "/version", "/users"]
			self.par1 = 5	

		self.index = 0

		#Primeira verificação antes de incializar o algum comando.
		for x in self.commands:
			if self.value == x:
				self.index = 0
				self.init(x)
				break
			else:
				self.index += 1
				if self.index == self.par1:
					print "Entre com um comando valido. Digite /help para obter ajuda."

	

