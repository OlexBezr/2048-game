class _2048_events: 
	# [
	# 	[0,0,0,0]
	# 	[0,0,0,0]
	# 	[0,0,0,0]
	# 	[0,0,0,0]
	# ]
	@classmethod
	def move_top(cls, game_field) :
		iteration = 1
		while iteration < game_field.index(game_field[-1]):
			# ------- прохождение по строкам и столбцам
			for row in game_field: 
				index_r = game_field.index(row)
				if index_r != 0 : 
					for block in row:
						if block['score'] != 0: 
							index_b = row.index(block)
			# ------ /
							# если выше цыфры совпадают
							if game_field[index_r-1][index_b]['score'] == block['score']: 
								game_field[index_r-1][index_b]['score'] = game_field[index_r-1][index_b]['score']*2 # удваиваю то что выше
								block['score'] = 0 # текущий блок очищаю
							elif game_field[index_r-1][index_b]['score'] == 0: # если выше чисто
								game_field[index_r-1][index_b]['score'] = block['score'] # заменяю score
								block['score'] = 0 # текущий блок очищаю
			iteration +=1
