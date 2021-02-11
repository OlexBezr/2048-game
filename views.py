class _2048_view:
	def __init__(self) :
		self.fps = 30
		self.colors = {
			'black' : (0,0,0),
			'white' : (255,255,255)
		}

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
		
		field_padding_left = 20
		field_padding_top = 100
		
		block_margin = 10
		block_widht, block_height = 105, 105
		
		for i in range(0, row):
			game_field.append([])
			if i == 0 : 
				position_y = field_padding_top + block_margin*i
			else :
				position_y = block_height * i + block_margin*i + field_padding_top 
			
			for j in range(0, column):
				if j == 0: 
					position_x = field_padding_left + block_margin*j
				else : 
					position_x = block_widht * j + block_margin*j + field_padding_left 
					
				game_field[-1].append({
					'index' : index_,
					'score' : 0,
					'position' : {
						'x': position_x,
						'y': position_y
					},
					'width' : block_widht,
					'height' : block_height
				})

				index_ +=1
		print(game_field)
		return game_field

	@classmethod
	def draw_field(cls, pg, screen, game_field):
		# print(cls.colors)
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
		for row in game_field: 
			for block in row: 
				pg.draw.rect( screen, BLOCK_COLOR[ str(block['score']) ], ( block['position']['x'], block['position']['y'], block['width'], block['height']))
				pg.draw.rect( screen, (191,173,163), ( block['position']['x'], block['position']['y'], block['width'], block['height']), 10)
				# screen.blit(ball, ballrect)
				pg.display.flip()
