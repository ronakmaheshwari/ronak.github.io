"""A tic-tac-toe game built with Python and Tkinter."""
import tkinter as tkfrom itertools import cycle
from tkinter import fontfrom typing import NamedTuple
class Player(NamedTuple):
    label: str    color: str
class Move(NamedTuple):
    row: int    col: int
    label: str = ""
BOARD_SIZE = 3DEFAULT_PLAYERS = (
    Player(label="X", color="blue"),    Player(label="O", color="green"),
)
class TicTacToeGame:    def __init__(self, players=DEFAULT_PLAYERS, board_size=BOARD_SIZE):
        self._players = cycle(players)        self.board_size = board_size
        self.current_player = next(self._players)        self.winner_combo = []
        self._current_moves = []        self._has_winner = False
        self._winning_combos = []        self._setup_board()
    def _setup_board(self):
        self._current_moves = [            [Move(row, col) for col in range(self.board_size)]
            for row in range(self.board_size)        ]
        self._winning_combos = self._get_winning_combos()
    def _get_winning_combos(self):        rows = [
            [(move.row, move.col) for move in row]            for row in self._current_moves
        ]        columns = [list(col) for col in zip(*rows)]
        first_diagonal = [row[i] for i, row in enumerate(rows)]        second_diagonal = [col[j] for j, col in enumerate(reversed(columns))]
        return rows + columns + [first_diagonal, second_diagonal]
    def toggle_player(self):        """Return a toggled player."""
        self.current_player = next(self._players)
    def is_valid_move(self, move):        """Return True if move is valid, and False otherwise."""
        row, col = move.row, move.col        move_was_not_played = self._current_moves[row][col].label == ""
        no_winner = not self._has_winner        return no_winner and move_was_not_played
    def process_move(self, move):
        """Process the current move and check if it's a win."""        row, col = move.row, move.col
        self._current_moves[row][col] = move        for combo in self._winning_combos:
            results = set(self._current_moves[n][m].label for n, m in combo)            is_win = (len(results) == 1) and ("" not in results)
            if is_win:                self._has_winner = True
                self.winner_combo = combo                break

    def has_winner(self):        """Return True if the game has a winner, and False otherwise."""
        return self._has_winner
    def is_tied(self):        """Return True if the game is tied, and False otherwise."""
        no_winner = not self._has_winner        played_moves = (
            move.label for row in self._current_moves for move in row        )
        return no_winner and all(played_moves)
    def reset_game(self):        """Reset the game state to play again."""
        for row, row_content in enumerate(self._current_moves):            for col, _ in enumerate(row_content):
                row_content[col] = Move(row, col)        self._has_winner = False
        self.winner_combo = []
class TicTacToeBoard(tk.Tk):    def __init__(self, game):
        super().__init__()        self.title("Tic-Tac-Toe Game")
        self._cells = {}        self._game = game
        self._create_menu()        self._create_board_display()
        self._create_board_grid()
    def _create_menu(self):        menu_bar = tk.Menu(master=self)
        self.config(menu=menu_bar)        file_menu = tk.Menu(master=menu_bar)
        file_menu.add_command(label="Play Again", command=self.reset_board)        file_menu.add_separator()
        file_menu.add_command(label="Exit", command=quit)        menu_bar.add_cascade(label="File", menu=file_menu)
    def _create_board_display(self):
        display_frame = tk.Frame(master=self)        display_frame.pack(fill=tk.X)
        self.display = tk.Label(            master=display_frame,
            text="Ready?",            font=font.Font(size=28, weight="bold"),
        )        self.display.pack()
    def _create_board_grid(self):
        grid_frame = tk.Frame(master=self)        grid_frame.pack()
        for row in
