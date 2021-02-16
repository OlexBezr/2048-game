class _2048_model(): 
	FIELD_PADDING_TOP = 100
	FIELD_PADDING_LEFT = 20
	BLOCK_MARGIN = 10

	def __init__(self) :
		self.field_padding_left = 20
		self.field_padding_top = 100
	@classmethod		
	def field_render(cls, column, row): 
		# return like this: 
		# 
		# [
		# 	[
		# 		{'index': 0, 'score': 0, 'position': {'x': 25, 'y': 105}}, 
		# 		{'index': 1, 'score': 0, 'position': {'x': 130, 'y': 105}}, 
		# 		{'index': 2, 'score': 0, 'position': {'x': 235, 'y': 105}}, 
		# 		{'index': 3, 'score': 0, 'position': {'x': 340, 'y': 105}}
		# 	], 
		# 	[
		# 		{'index': 4, 'score': 0, 'position': {'x': 25, 'y': 210}}, 
		# 		{'index': 5, 'score': 0, 'position': {'x': 130, 'y': 210}}, 
		# 		{'index': 6, 'score': 0, 'position': {'x': 235, 'y': 210}}, 
		# 		{'index': 7, 'score': 0, 'position': {'x': 340, 'y': 210}}
		# 	]
		# 	....
		# ]

		game_field = []
		index_ = 0
		
		block_widht, block_height = 105, 105
		
		for i in range(0, row):
			game_field.append([])
			if i == 0 : 
				position_y = _2048_model.FIELD_PADDING_TOP + _2048_model.BLOCK_MARGIN*i
			else :
				position_y = block_height * i + _2048_model.BLOCK_MARGIN*i + _2048_model.FIELD_PADDING_TOP 
			
			for j in range(0, column):
				if j == 0: 
					position_x = _2048_model.FIELD_PADDING_LEFT + _2048_model.BLOCK_MARGIN*j
				else : 
					position_x = block_widht * j + _2048_model.BLOCK_MARGIN*j + _2048_model.FIELD_PADDING_LEFT 
					
				game_field[-1].append({
					'index' : index_,
					'score' : 0,
					'position' : {
						'x': position_x,
						'y': position_y
					},
					'width' : block_widht,
					'height' : block_height,

					'step_top' : 0,
					'step_down' : 0,
					'step_right' : 0,
					'step_left' : 0
				})

				index_ +=1
		return game_field


	@classmethod
	def move_top(cls, game_field) :
		def step_top(): 
			iteration = 1

			while iteration < len(game_field): # прохожу column N раз что бы сдвинуть все
				for row in game_field: 
					index_r = game_field.index(row)
					if not index_r-1 < 0: 
						for block in row: 
							index_b = row.index(block)
							try: 
								if game_field[index_r-1][index_b]['score'] == 0 and block['score'] != 0: # если выше чисто и текущий блок не 0
									game_field[index_r-1][index_b]['score'] = block['score'] # заменяю score
									# здесь нужно сделать анимацию
									view_.animation_move_block_top(block)
									block['score'] = 0 # текущий блок очищаю
									block['step_top'] += 1
							except IndexError: 
								pass
				iteration +=1
		def join_blocks() :
			for row in game_field: 
				index_r = game_field.index(row)
				if not index_r+1 > len(game_field): 
					for block in row: 
						index_b = row.index(block)
						try: 
							if game_field[index_r+1][index_b]['score'] == game_field[index_r][index_b]['score']: # если нижний блок такой же как и текущий
								game_field[index_r][index_b]['score'] = game_field[index_r][index_b]['score']*2 # удваитаю текущий блок
								game_field[index_r+1][index_b]['score'] = 0 # тот что ниже очищаю
								step_top() # еще раз поднимаю все блоки
						except IndexError: 
							pass

		step_top()
		join_blocks()

	@classmethod
	def move_down(cls, game_field) :
		def step_down(): 
			iteration = 1
			while iteration < len(game_field): # прохожу column N раз что бы сдвинуть все
				for row in game_field: 
					index_r = game_field.index(row)
					if not index_r+1 > len(game_field): 
						for block in row: 
							index_b = row.index(block)
							try: 
								if game_field[index_r+1][index_b]['score'] == 0: # если выше чисто
									game_field[index_r+1][index_b]['score'] = block['score'] # заменяю score
									block['score'] = 0 # текущий блок очищаю
							except IndexError: 
								pass
				iteration +=1
		def join_blocks() :
			# здесь нужно проходить row с конца
			count_row = len(game_field)-1

			while count_row >= 0 : 
			# for row in game_field: 
				row = game_field[count_row]
				index_r = game_field.index(row)
				if not index_r-1 < 0: 
					for block in row: 
						index_b = row.index(block)
						try: 
							if game_field[index_r-1][index_b]['score'] == game_field[index_r][index_b]['score']: # если нижний блок такой же как и текущий
								game_field[index_r][index_b]['score'] = game_field[index_r][index_b]['score']*2 # удваитаю текущий блок
								game_field[index_r-1][index_b]['score'] = 0 # тот что ниже очищаю
								step_down() # еще раз поднимаю все блоки
						except IndexError: 
							pass
				count_row -=1

		step_down()
		join_blocks()
		
	# [
	# 	[0,2,,0]
	# 	[0,4,0,0]
	# 	[0,2,0,0]
	# 	[0,0,0,0]
	# ]
	@classmethod
	def move_left(cls, game_field) :
		def step_left():

			iteration = 1
			while iteration < len(game_field): # прохожу row N раз что бы сдвинуть все
				for row in game_field: 
					for block in row:
						index_b = row.index(block)
						if not index_b-1 < 0: 
							try:
								if row[index_b-1]['score'] == 0: # если левый блок пустой
									row[index_b-1]['score'] = block['score'] # заменяю score
									block['score'] = 0 # текущий блок очищаю
							except IndexError: 
								pass
				iteration +=1
		def join_blocks():
			for row in game_field: 
				# index_r = game_field.index(row)
				for block in row: 
					index_b = row.index(block)
					if not index_b-1 < 0:
						try: 
							if row[index_b-1]['score'] == row[index_b]['score']: # если левый блок такой же как и текущий
								row[index_b]['score'] = row[index_b]['score']*2 # удваитаю текущий блок
								row[index_b-1]['score'] = 0 # тот что левее очищаю
								step_left() # еще раз сдвигаю все блоки
						except IndexError: 
							pass
		step_left()
		join_blocks()
	
	@classmethod
	def move_right(cls, game_field) :
		def step_right():
			iteration = 1
			while iteration < len(game_field): # прохожу row N раз что бы сдвинуть все
				for row in game_field: 
					for block in row:
						index_b = row.index(block)
						if not index_b+1 > len(row): 
							try: 
								if row[index_b+1]['score'] == 0: # если левый блок пустой
									row[index_b+1]['score'] = block['score'] # заменяю score
									row[index_b]['score'] = 0 # текущий блок очищаю
							except IndexError: 
								pass
				iteration +=1

		def join_blocks():
			# здесь так же нужно начиноть с другой сторовы, иначе все что в row есть соединится
			# like [2,2,2,2] -> [0,0,0,8], а должно быть [0,0,4,4]
			for row in game_field: 
				# index_r = game_field.index(row)a
				count_block = len(row)-1
				while count_block >= 0:
				# for block in row: 
					block = row[count_block]
					index_b = row.index(block)
					if not index_b+1 > len(row):
						try: 
							if row[index_b+1]['score'] == row[index_b]['score']: # если правый блок такой же как и текущий
								row[index_b]['score'] = row[index_b]['score']*2 # удваитаю текущий блок
								row[index_b+1]['score'] = 0 # тот что правее очищаю
								step_right() # еще раз сдвигаю все блоки
						except IndexError: 
							pass
					count_block -= 1
		step_right()
		join_blocks()

	@classmethod
	def get_empty_blocks(cls, game_field) :
		empty_pos = []
		for row in game_field:
			for block in row:
				if block['score'] == 0: 
					empty_pos.append({
						'column': row.index(block),
						'row': game_field.index(row),
						'index': block['index']
					})

		return empty_pos

	@classmethod
	def add_random_block_to_field(cls, game_field):
		import random
		empty_pos = cls.get_empty_blocks( game_field )
		random_pos = int(random.uniform(0, len(empty_pos)-1))
		col = empty_pos[random_pos]['column']
		row = empty_pos[random_pos]['row']

		random_score = random.random()
		# 20% - 4 ; 80% - 2
		if random_score < 0.2 : 
			game_field[ row ][ col ]['score'] = 4
		else : 
			game_field[ row ][ col ]['score'] = 2
		return random_pos

	@classmethod
	def get_total_score(cls, game_field):
		total_score = 0
		for row in game_field:
			for block in row:
				total_score += block['score']

		return str(total_score)
