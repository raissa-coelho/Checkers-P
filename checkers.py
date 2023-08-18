
import numpy as np

col = ['a','b','c','d','e','f','g','h']
l = ['8','7','6','5','4','3','2','1']
black = ['B']
white = ['W']
white_queen = ['WQ']
black_queen = ['BQ']
skip = []

class Game():

	def __init__(self):
		self.board = Board()
		self.player1 = {'color': 'white', 'dead_pieces': 12}
		self.player2 = {'color': 'black', 'dead_pieces': 12}
		self.turn = True
	
	def check_win(self):
		if self.player1['dead_pieces'] == 0:
			return 2
		if self.player2['dead_pieces'] == 0:
			return 1
		
	def reset_board(self):
		self.board.set_board()
		self.turn = True
	
	def update_turn(self,turn):
		self.turn = turn
	
	def get_turn(self):
		return self.turn
	
	def is_valid_move(self,move_from, move_to, board, piece):
		p = Piece(move_to,move_from,board)
		
		if piece == 'B' or piece == 'W':
			return p.is_valid(move_from, move_to, board, self.turn)

		return False
	
	def move(self,move_from,move_to):
		for i in range(len(col)):
			if move_from[0] == col[i]:
				num_from = i
			if move_to[0] == col[i]:
				num_to = i
		
		for i in range(len(l)):
			if move_from[1] == l[i]:
				num_l_from = i
			if move_to[1] == l[i]:
				num_l_to = i
		
		b = self.board.get_board()
		
		if b[num_l_from][num_from] == ' ':
			print(f'Não há uma peça nesta posição.')
			return False
		
		piece = b[num_l_from][num_from]
		
		if self.check_piece_color(piece):
			print(f'Não é a sua peça')
			return False
		
		target = b[num_l_to][num_to]

		if target in white or target in black:
			print(f"Não pode comer a peça.")
			return False	
		
		if self.is_valid_move(move_from, move_to, b, piece):
			if target == ' ':
				b[num_l_from][num_from]	= ' '
				b[num_l_to][num_to] = piece
				self.board.update_board(b)
				if len(skip) > 0:
					b[skip[0]][skip[1]] = ' '
					skip.clear()
				if piece in black:
					self.player1['dead_pieces'] -= 1
				if piece in white:
					self.player2['dead_pieces'] -= 1

			if piece in white:
				turn = False
				self.update_turn(turn)
			elif piece in black:
				turn = True 
				self.update_turn(turn)
			return True
		else:
			print(f'8: Movimento inválido.')
			return False
		
		return True

	def check_piece_color(self,piece):
		if self.turn:
			if piece not in white:
				return True
		else:
			if piece not in black:
				return True
		return False
	
	def transform_input(self,move):
		m = move.split(' ')
		m_from = list(m[0])
		m_to = list(m[1])
		
		try:
			if int(m_from[1]) < 1 or int(m_from[1]) > 8:
				print(f"1: Não é um número entre 1 - 8.")
			if m_from[0] < 'a' or  m_from[0] > 'h':
				print(f'2: Não é uma letra entre a - h')
			return m_from, m_to
		except:
			print(f"3: {m_from} não está no formato certo: [letra][número]") 
			return None		
		return None
	
class Board():

	def __init__(self):
		self.line = [' ', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
		self.column = [['8'], ['7'], ['6'], ['5'], ['4'], ['3'], ['2'], ['1']]
		self.board = [[' ', 'B', ' ', 'B', ' ', 'B', ' ', 'B'],
			          ['B', ' ', 'B', ' ', 'B', ' ', 'B', ' '],
                      [' ', 'B', ' ', 'B', ' ', 'B', ' ', 'B'],
                      [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                      [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                      ['W', ' ', 'W', ' ', 'W', ' ', 'W', ' '],
                      [' ', 'W', ' ', 'W', ' ', 'W', ' ', 'W'],
                      ['W', ' ', 'W', ' ', 'W', ' ', 'W', ' ']]
	
	def print_board(self):
		b = np.hstack((self.column, self.board))
		for row in b:
			print(' - '.join(row))
		for i in self.line:
			print(i, end =' - ')
		print(f'\n')
	
	def get_board(self):
		return self.board
	
	def update_board(self,board):
		self.board = board

	def set_board(self):
		board = [[' ', 'B', ' ', 'B', ' ', 'B', ' ', 'B'],
			        ['B', ' ', 'B', ' ', 'B', ' ', 'B', ' '],
                    [' ', 'B', ' ', 'B', ' ', 'B', ' ', 'B'],
                    [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                    [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                    ['W', ' ', 'W', ' ', 'W', ' ', 'W', ' '],
                    [' ', 'W', ' ', 'W', ' ', 'W', ' ', 'W'],
                    ['W', ' ', 'W', ' ', 'W', ' ', 'W', ' ']]

class Piece():

	def __init__(self,move_to,move_from,board):
		self.move_to = move_to
		self.move_from = move_from
		self.board = board

	def is_valid(self, move_from, move_to, board, turn):

		for i in range(len(col)):
			if move_from[0] == col[i]:
				num_from_ = i
			if move_to[0] == col[i]:
				num_to = i

		for i in range(len(l)):
			if move_from[1] == l[i]:
				num_l_from = i
			if move_to[1] == l[i]:
				num_l_to = i
		
		if  num_l_to == num_l_from and num_to == num_from_:
			print(f'ERRO')
			return False
		
		if  abs( num_l_from - num_l_to) != abs( num_from_ - num_to):
			print(f'ERRO')
			return False
		
		# CHECK if there is something in the way
		x = 1 if (num_l_to) - (num_l_from) > 0 else -1
		y = 1 if num_to - num_from_ > 0 else -1
		
		i =  (num_l_from) + x
		j =  num_from_ + y
		
		while(i < num_l_to if x==1 else i > num_l_to):
			if board[i][j] != ' ':
				if board[i][j] in black and turn == False:
					print(f'Caminho bloqueado.')
					return False
				if board[i][j] in white and turn == True:
					print(f'Caminho bloqueado.')
					return False
			skip.append(i)
			skip.append(j)
			i += x
			j += y

		# CHECK moving backward
		if turn == white:
				if num_l_from - num_l_to < 0:
					print(f'ERRO')
					return False
		elif turn == black:
				if num_l_from - num_l_to > 0:
					print(f'ERRO')
					return False	

		return True	
