import curses
from marcopolo import Game, Player, Board
from view import GameView

game = None
view = None
jonathan = None

def loop(screen):
    screen.clear()
    view.print(screen, jonathan)

    while True:
      view.print(screen, jonathan)
      c = screen.getch()

      if c == curses.KEY_LEFT:
        jonathan.move_left(game.board)
      elif c == curses.KEY_RIGHT:
        jonathan.move_right(game.board)
      elif c == curses.KEY_UP:
        jonathan.move_up(game.board)
      elif c == curses.KEY_DOWN:
        jonathan.move_down(game.board)
      elif c == ord('q'):
        break

      if game.is_in_goal_state():
        break



def main():

  global game
  global view
  global jonathan
  game = Game(10)
  view = GameView(game)
  jonathan = game.add_player('Jonathan')
  game.add_player('Rochelle', True)

  curses.wrapper(loop)

if __name__ == "__main__":
    main()
