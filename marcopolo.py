from random import randrange
import curses

class ConsoleGameView:

  def __init__(self, game):
    self.game = game

  def print(self):
    for y in range(self.game.board.size):
      for x in range(self.game.board.size):

        player = self.game.get_player_at([x,y])

        if (player == None):
          print(".", end="")
        elif (player.is_it):
          print("X", end="")
        else:
          print("O", end="")

      print()


class Game:

  def __init__(self, size):
    self.board = Board(self, size)
    self.all_players = []
    self.non_it_players = []
    self.it_player = None




  def add_player(self, name, is_it = False):
    """Adds a new player to the game. Randomizes the position. Returns a
    reference to the player object"""

    #random position
    start = [randrange(self.board.size), randrange(self.board.size)]

    while self.board.is_cell_occupied(start):
      start = [randrange(self.board.size), randrange(self.board.size)]

    player = Player(name, start, is_it)
    self.all_players.append(player)

    #set the "it" player
    if is_it:
      self.it_player = player
    else:
      self.non_it_players.append(player)

    return player




  def is_in_goal_state(self):
    """Determines if the game is in a goal state. Basically, is the game over
    or not"""

    #players that are in the same position as the "it" player
    for p in self.non_it_players:
      if p.position == self.it_player.position:
        return True

    return False



  def get_player_at(self, cell):
    """Gets the player at the specified cell or None if no player occupies
    the cell"""

    for p in self.all_players:
      if p.position == cell:
        return p

    return None




  def marco(self, p):
    """polo returns up, down, left, or right coordinates relative to position
    indicating the general direction of the current player. This is akin calling
    out "marco" and receiving the polo response from the it player"""

    it = self.it_player

    polo = []
    if (p.position[0] < it.position[0]):
      polo.append([p.position[0] + 1, p.position[1]])
    elif (p.position[0] > it.position[0]):
      polo.append([p.position[0] - 1, p.position[1]])

    if (p.position[1] < it.position[1]):
      polo.append([p.position[0], p.position[1] + 1])
    elif(p.position[1] > it.position[1]):
      polo.append([p.position[0], p.position[1] - 1])

    return polo


class Board:

  def __init__(self, game, size):
    self.game = game
    self.size = size

  def is_valid_cell(self, cell):
    """Determines if the cell is within the bounds of the board"""

    return cell[0] >=0 and cell[1] >= 0 and \
            cell[0] < self.size and cell[1] < self.size



  def is_cell_occupied(self, cell):
    """Determines if the cell is occupied by another non-it player"""

    for p in self.game.non_it_players:
      if p.position == cell:
        return True

    return False


class Player:

  def __init__(self, name, position = [0,0], is_it = False):
    self.name = name
    self.position = position
    self.is_it = is_it


  def move_left(self, board):
    """Moves the player left. Returns True if successful, False otherwise"""
    cell = list(self.position)
    cell[0] = cell[0] - 1

    return self._move(board, cell)


  def move_right(self, board):
    """Moves the player right. Returns True if successful, False otherwise"""
    cell = list(self.position)
    cell[0] = cell[0] + 1

    return self._move(board, cell)


  def move_up(self, board):
    """Moves the player up. Returns True if successful, False otherwise"""
    cell = list(self.position)
    cell[1] = cell[1] - 1

    return self._move(board, cell)


  def move_down(self, board):
    """Moves the player down. Returns True if successful, False otherwise"""
    cell = list(self.position)
    cell[1] = cell[1] + 1

    return self._move(board, cell)


  def _move(self, board, cell):
    """Moves the player to the specified cell if possible"""

    if board.is_valid_cell(cell) and not board.is_cell_occupied(cell):
      self.position = cell
      return True
    else:
      return False
