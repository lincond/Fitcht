#!/usr/bin/python
#-*-coding: utf-8 -*-

# console.py
# @author: Lincon Dias

import sys

class Console():
	
	#Construtor
	def __init__(self):
		#Console Version
		self.version = '0.0.1a'
		print "Console Inciado, versao " + self.version

		#Programa esta rodando.
		self.isRunnig = True

		#Chama a primeira captura de argumentos.
		while self.isRunnig:
			self.est = self.core(self.getNextValue())

	#Retorna uma entrada de dados.
	def getNextValue(self):
		self.val1 = raw_input(">")
		return self.val1

	#Inicia algum processo recebido pelo console.
	def init(self, processName):
		print "Incializando componente " + processName
		sys.exit()

	#Coração do Console.
	def core(self, value):
		self.value = value

		#Lista de comandos disponives no menu principal.
		self.commands = ["/start", "/join", "/help", "/exit", "/version"]
		self.index = 0

		#Primeira verificação antes de incializar o algum comando.
		for x in self.commands:
			if self.value == x:
				self.index = 0
				self.init(x)
				break
			else:
				self.index += 1
				if self.index == 4:
					print "Entre com um comando valido. Digite /help para obter ajuda."

	

