import sys 
import pygame as pg
from pygame.locals import *
from view import _2048_view
from model import _2048_model

window_size = w_width, w_height = 600, 600

view_ = _2048_view()
model_ = _2048_model()

pg.init()
pg.mixer.init()
pg.display.set_caption("2054")


game_field = _2048_view.field_render( 4, 4 )
screen = pg.display.set_mode(window_size)
clock = pg.time.Clock()
pressed_keys = pg.key.get_pressed()

model_.add_random_block_to_field(game_field)
model_.add_random_block_to_field(game_field)

# game_field[0][0]['score'] = 2
# game_field[1][0]['score'] = 2
# game_field[2][0]['score'] = 2
# game_field[3][0]['score'] = 2


screen.fill( (0,0,0) )
view_.draw_field(pg, screen, game_field)

while 1:
	for event in pg.event.get():
		if event.type == pg.QUIT : 
			sys.exit()

		if event.type == pg.KEYDOWN: 
			# pass
			if event.key == pg.K_UP:
				model_.move_top(game_field)
				model_.add_random_block_to_field(game_field)

				model_.print_score(game_field)


			if event.key == pg.K_LEFT:
				model_.move_left(game_field)
				model_.add_random_block_to_field(game_field)

				model_.print_score(game_field)

			if event.key == pg.K_DOWN:
				model_.move_down(game_field)
				model_.add_random_block_to_field(game_field)

				model_.print_score(game_field)

			if event.key == pg.K_RIGHT:
				model_.move_right(game_field)
				model_.add_random_block_to_field(game_field)

				model_.print_score(game_field)

			# if pressed_keys[K_SPACE]:
			# if event.button == 1: 
		# if event.key == pg.K_UP:
		# 	print('gg')
		# screen.fill( (0,0,0) )
		# print(pg.K_UP)
		view_.draw_field(pg, screen, game_field)

	# ballrect = ballrect.move(speed)
	# if ballrect.left < 0 or ballrect.right > w_width:
	# 	speed[0] = -speed[0]
	# if ballrect.top < 0 or ballrect.bottom > w_height:
 	# 	speed[1] = -speed[1]


	# screen.blit(ball, ballrect)
	# pg.display.flip()
	# pg.draw.rect( screen, COLORS['white'], position)
