from curses import wrapper

class GameView:

  def __init__(self, game):
    self.game = game

  def print(self, screen, p):

    if p.is_it:
      self._print_polo_view(screen, p)
    else:
      self._print_marco_view(screen, p)

    screen.refresh()

  def _print_marco_view(self, screen, p):
    """prints the "marco" view of the board. Meaning all other players are
    hidden from view and only the direction of the "polo" response is visible.
    This is what the non "it" players should see."""

    polo = self.game.marco(p)

    for y in range(self.game.board.size):
      for x in range(self.game.board.size):

        if [x,y] in polo:
          screen.addstr(y, x, '*')
        elif [x,y] == p.position:
          screen.addstr(y, x, 'X')
        else:
          screen.addstr(y, x, ' ')

  def _print_polo_view(self, p):
    """prints the "polo" view of the board. Meaning all players are visible.
    This is what the "it" player should see."""


    for y in range(self.game.board.size):
      for x in range(self.game.board.size):

        player = self.game.get_player_at([x,y])

        if (player == None):
          screen.addstr(y,x, '.')
        elif (player.is_it):
          screen.addstr(y,x, 'X')
        else:
          screen.addstr(y,x, 'O')
