class _2048_model: 
	@classmethod
	def print_score(cls, game_field) :
		row_l = []
		print('-----')
		for row in game_field:
			score_row = []
			for block in row: 
				score_row.append( block['score'])
			print(score_row)
		print('-----')
	
		return row_l
		
	@classmethod
	def move_top(cls, game_field) :
		def step_top(): 
			iteration = 1

			while iteration < len(game_field): # прохожу column N раз что бы сдвинуть все
				for row in game_field: 
					print('+++',iteration)
					cls.print_score(game_field)
					index_r = game_field.index(row)
					if not index_r-1 < 0: 
						for block in row: 
							index_b = row.index(block)
							try: 
								if game_field[index_r-1][index_b]['score'] == 0: # если выше чисто
									game_field[index_r-1][index_b]['score'] = block['score'] # заменяю score
									block['score'] = 0 # текущий блок очищаю
							except IndexError: 
								continue
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
							continue

		step_top()
		join_blocks()

	@classmethod
	def move_down(cls, game_field) :
		def step_down(): 
			iteration = 1
			while iteration < len(game_field): # прохожу column N раз что бы сдвинуть все
				for row in game_field: 
					print('+++',iteration)
					cls.print_score(game_field)
					index_r = game_field.index(row)
					if not index_r+1 > len(game_field): 
						for block in row: 
							index_b = row.index(block)
							
							try: 
								if game_field[index_r+1][index_b]['score'] == 0: # если выше чисто
									game_field[index_r+1][index_b]['score'] = block['score'] # заменяю score
									block['score'] = 0 # текущий блок очищаю
							except IndexError: 
								continue
				iteration +=1
		def join_blocks() :
			# здесь нужно проходить row с конца
			len_game_field = len(game_field)-1

			while len_game_field > 0 : 
			# for row in game_field: 
				row = game_field[len_game_field]
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
							continue
				len_game_field -=1

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
		iteration = 1
		while iteration < len(game_field): # прохожу row N раз что бы сдвинуть все
			for row in game_field: 
				print('+++',iteration)
				cls.print_score(game_field)
				for block in row:
					index_b = row.index(block)
					if not index_b-1 < 0: 
						try:
							if row[index_b-1]['score'] == 0: # если левый блок пустой
								row[index_b-1]['score'] = block['score'] # заменяю score
								block['score'] = 0 # текущий блок очищаю
						except IndexError: 
							continue
			iteration +=1
	
	@classmethod
	def move_right(cls, game_field) :
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
							continue
			iteration +=1

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