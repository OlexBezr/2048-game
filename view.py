from model import _2048_model as model_

class _2048_view:


	@classmethod
	def print_in_cmd(cls, game_field) :
		row_l = []
		print('-----')
		for row in game_field:
			score_row = []
			for block in row: 
				score_row.append( block['score'])
			print(score_row)
		print('-----')
	
		return row_l


	# @classmethod
	# def draw_field(cls, pg, screen, game_field):
	# 	# screen.fill( (0,0,0) )
	# 	for row in game_field: 
	# 		for block in row: 

	# 			cls.draw_block( pg, screen, block)
	# 			cls.draw_total_score( pg, screen, game_field)
	# 			cls.draw_block_score( pg, screen, block)

	# 			pg.display.flip()
	
	@classmethod
	def draw_block(cls, pg, screen, block):
		# нужно сделать генератор цветов
		BLOCK_COLOR = {
			'0': (214,205,196),
			'2' : (239,230,221),
			'4' : (239,227,205),
			'8': (247,178,123),
			'16': (247,150,99),
			'32': (247,124,90),
			'64': (247,93,59),
			'128':(241,213,121),
			'256':(239,206,99),
			'512':(238,202,82),
			'1024':(239,198,58),
			'2048': (239,194,41)
		}
		#block
		block['rect'] = pg.draw.rect( screen, BLOCK_COLOR[ str(block['score']) ], ( block['position']['x'], block['position']['y'], block['width'], block['height']))
		cls.draw_block_score(pg, screen, block)
		pg.display.update()
		pg.display.flip()

	@classmethod
	def draw_block_score(cls, pg, screen, block) :
		if block['score'] != 0 : 
			font = pg.font.Font(None, 40)
			text = font.render( str( block['score'] ) , True, ( 180, 0, 0) )

			text_pos_center_x = block['position']['x'] + (block['width'] / 2 - text.get_rect().width / 2)
			text_pos_center_y = block['position']['y'] + (block['height'] / 2 - text.get_rect().height / 2)

			screen.blit( text, ( text_pos_center_x, text_pos_center_y ) )

	@classmethod
	def draw_total_score(cls, pg, screen, game_field) : 
		total_score = model_.get_total_score(game_field)

		font = pg.font.Font(None, 30)
		text = font.render( 'Score: ' + total_score, True, ( 180, 0, 0) )

		screen.blit( text, ( 40, 10 ) )
		pg.display.update()

	# @classmethod
	# def animation_move_block_top(cls, game_field):
	# 	# анимация должно быть 0.5 секунд
	# 	# колонки двигаются с разно скоростью что бы они останавливали анимацию в одно время 
	# 	# при соединении нужно сделать перемищение нижнего блока на верхний. и заменить эго на новый блок 
	# 	# [
	# 	# 	[0,0,2,0]    [2,4,2,2]
	# 	# 	[0,2,0,2]    [0,0,4,0]
	# 	# 	[0,2,4,0]    [0,0,0,0]
	# 	# 	[2,0,0,0]    [0,0,0,0]
	# 	# ]

	# 		# for new_row in new_game_field : 


	# 	# for old_row in old_game_field :
	# 	# 	new_row = new_game_field[ old_game_field.index(old_row) ]

	# 	# 	for index_b in range(0, len(old_game_field)-1)
	# 	# 		if old_row[]
	# 	for row in game_field : 
	# 		for block in row : 
	# 			if block["step_top"] != 0 : 


	# @classmethod
	# def animation_move_block_top(cls, block):

	# 	# просто переместить плавно вверх блок

	# 	#

	# 	step_one_tick = (block['height']+ model_.BLOCK_MARGIN) / 100

	# 	need_be_on = block['positon']['y']- model_.BLOCK_MARGIN - block['height']


	# 	block['positon']['x']
	# 	block['positon']['y']

	@classmethod
	def animation_move_block_top(cls, block):
		if block["step_top"] != 0 : 
			step_one_tick = (( block['height'] + model_.BLOCK_MARGIN) / 100) * block["step_top"]
			block['positon']['y'] -= step_one_tick
			block["step_top"] -= 1





