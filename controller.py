import sys 
import pygame as pg
from pygame.locals import *
from view import _2048_view
from model import _2048_model

window_size = w_width, w_height = 600, 600
FPS = 30

view_ = _2048_view()
model_ = _2048_model()

pg.init()
pg.mixer.init()
pg.display.set_caption("2054")


game_field = model_.field_render( 4, 4 )
screen = pg.display.set_mode(window_size)
clock = pg.time.Clock()
pressed_keys = pg.key.get_pressed()

model_.add_random_block_to_field(game_field)
model_.add_random_block_to_field(game_field)


# view_.draw_field(pg, screen, game_field)


def do_after_event(game_field) : 
	view_.print_in_cmd(game_field)

while 1:
	clock.tick(10)
	for event in pg.event.get():
		if event.type == pg.QUIT : 
			sys.exit()

		if event.type == pg.KEYDOWN: 
			if event.key == pg.K_UP:
				move = model_.move_top(game_field)
				if move == True : # если никакого движения не произошло не добавлять блок
					model_.add_random_block_to_field(game_field)

				do_after_event(game_field)

			if event.key == pg.K_LEFT:
				move = model_.move_left(game_field)
				if move == True : # если никакого движения не произошло не добавлять блок
					model_.add_random_block_to_field(game_field)
				do_after_event(game_field)

			if event.key == pg.K_DOWN:
				move = model_.move_down(game_field)
				if move == True : # если никакого движения не произошло не добавлять блок
					model_.add_random_block_to_field(game_field)
				do_after_event(game_field)

			if event.key == pg.K_RIGHT:
				move = model_.move_right(game_field)
				if move == True : # если никакого движения не произошло не добавлять блок
					model_.add_random_block_to_field(game_field)
				do_after_event(game_field)


	view_.draw_total_score(pg, screen, game_field)




	# move animation
	for row in game_field: 
		for block in row: 
			# view_.animation_move_block_top(block)
			view_.draw_block( pg, screen, block)

			# border
			# pg.draw.rect( screen, (191,173,163), ( block['position']['x'], block['position']['y'], block['width'], block['height']), 10)

	if model_.game_over(game_field) : 
		font = pg.font.Font(None, 50)
		text = font.render( 'Game Over', True, ( 180, 0, 0))
		screen.blit( text, ( (w_width / 2 - text.get_rect().width / 2), (w_height / 2 - text.get_rect().height / 2) ) )
