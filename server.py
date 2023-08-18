# server.py
# ifconfig
# wlan --> inet

import socket
import pickle
import numpy as np
import checkers


def start_server():
	#HOST = "127.0.0.1"
	HOST = "192.168.0.9" # server's ip
	PORT = 5000  # same port as client
	print("Conectando servidor...")
	server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	
	if verify_port(PORT,HOST,server) == False:
		print("Porta sendo usada.")
		server.close()
		
	try:
		server.bind((HOST, PORT))
	except:
		print("Erro ao abrir servidor!")
		
	print("Servidor criado!")
	
	# Inicializa o jogo
	ch = checkers.Game()
	
	server.listen(2)
	print("Esperando conexão dos jogadores: ")
	conn1, port1 = server.accept()
	print("Player 1 conectado.")
	conn2, port2 = server.accept()
	print("Player 2 conectado.")	
	
	current_turn = conn1
	opponent = conn2	
	
	w1 = 'welcome1'
	current_turn.sendall(pickle.dumps(w1))
	w2 = 'welcome2'
	opponent.sendall(pickle.dumps(w2))
	
	while True:
		fc = current_turn.recv(2048*2)
		from_client1 = pickle.loads(fc)
		
		fc2 = opponent.recv(2048*2)
		from_client2 = pickle.loads(fc2)
		
		if from_client1.startswith('ready') and from_client2.startswith('ready'):
			data1 = 'start' + '\n' + str(ch.board.get_board()) + '\n' + 'True'
			data2 = 'start' + '\n' + str(ch.board.get_board()) + '\n' + 'False'
			current_turn.sendall(pickle.dumps(data1))
			opponent.sendall(pickle.dumps(data2))
		
		elif from_client1.startswith('send move'):
			move = from_client1.split('\n')
			mov = move[1]
			move_from, move_to = ch.transform_input(mov)
			if ch.move(move_from,move_to):
				current_turn.sendall(pickle.dumps('OK'))
				current_turn, opponent = opponent, current_turn
				update1 = 'update' + '\n' + str(ch.board.get_board()) + '\n' + 'current'
				update2 = 'update' + '\n' + str(ch.board.get_board()) + '\n' + 'opponent'
				current_turn.sendall(pickle.dumps(update1))
				opponent.sendall(pickle.dumps(update2))
			else:
				current_turn.sendall(pickle.dumps('invalid'))
				opponent.sendall(pickle.dumps('wait'))
		
		elif from_client2.startswith('wait'):
			opponent.sendall(pickle.dumps('wait'))
		
	current_turn.close()
	opponent.close()

def verify_port(PORT,HOST,sock):
	test = (HOST,PORT)
	result = sock.connect_ex(test)
	if result == 0:
		print("Porta está aberta.")
		return False
	else:
		return True


start_server()
