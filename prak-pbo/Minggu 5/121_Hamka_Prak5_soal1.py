import pygame
import sys
from pygame.locals import *

pygame.init()

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

WIDTH, HEIGHT = 450, 450

SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Triple T's")

class Renderable:
    def render(self):
        raise NotImplementedError("Method abstrak belum di implementasi")

class Player:
    def __init__(self, symbol):
        self.symbol = symbol

    def move(self, board):
        raise NotImplementedError("Method abstrak belum di implementasi")

class Board(Renderable):
    def __init__(self):
        self.grid = [[' ' for _ in range(3)] for _ in range(3)]

    def render(self):
        SCREEN.fill(WHITE)
        pygame.draw.line(SCREEN, BLACK, (WIDTH // 3, 0), (WIDTH // 3, HEIGHT), 5)
        pygame.draw.line(SCREEN, BLACK, (2 * WIDTH // 3, 0), (2 * WIDTH // 3, HEIGHT), 5)
        pygame.draw.line(SCREEN, BLACK, (0, HEIGHT // 3), (WIDTH, HEIGHT // 3), 5)
        pygame.draw.line(SCREEN, BLACK, (0, 2 * HEIGHT // 3), (WIDTH, 2 * HEIGHT // 3), 5)

        for row in range(3):
            for col in range(3):
                if self.grid[row][col] != ' ':
                    font = pygame.font.Font(None, 100)
                    text = font.render(self.grid[row][col], True, BLACK)
                    text_rect = text.get_rect(center=(col * WIDTH // 3 + WIDTH // 6, row * HEIGHT // 3 + HEIGHT // 6))
                    SCREEN.blit(text, text_rect)

    def is_full(self):
        for row in self.grid:
            if ' ' in row:
                return False
        return True

    def is_winner(self, symbol):
        for i in range(3):
            if self.grid[i][0] == self.grid[i][1] == self.grid[i][2] == symbol:
                return True
            if self.grid[0][i] == self.grid[1][i] == self.grid[2][i] == symbol:
                return True
        if self.grid[0][0] == self.grid[1][1] == self.grid[2][2] == symbol:
            return True
        if self.grid[0][2] == self.grid[1][1] == self.grid[2][0] == symbol:
            return True
        return False

    def place_symbol(self, symbol, row, col):
        if self.grid[row][col] == ' ':
            self.grid[row][col] = symbol
            return True
        return False

class Humane(Player):
    def move(self, board):
        while True:
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == MOUSEBUTTONDOWN:
                    pos = pygame.mouse.get_pos()
                    row = pos[1] // (HEIGHT // 3)
                    col = pos[0] // (WIDTH // 3)
                    if board.place_symbol(self.symbol, row, col):
                        return

class Computer(Player):
    def move(self, board):
        for row in range(3):
            for col in range(3):
                if board.place_symbol(self.symbol, row, col):
                    return

class TicTacToeGame:
    def __init__(self):
        self.board = Board()
        self.players = [Humane('X'), Computer('O')]
        self.current_player_index = 0

    def switch_player(self):
        self.current_player_index = (self.current_player_index + 1) % 2

    def play(self):
        while not self.board.is_full() and not self.board.is_winner('X') and not self.board.is_winner('O'):
            self.board.render()
            pygame.display.update()

            current_player = self.players[self.current_player_index]
            current_player.move(self.board)
            if self.board.is_winner(current_player.symbol):
                print(f"Player {current_player.symbol} Menang >~< !")
                break

            self.switch_player()

        if self.board.is_full() and not self.board.is_winner('X') and not self.board.is_winner('O'):
            print("Game Seri!")

def main():
    game = TicTacToeGame()
    game.play()

if __name__ == "__main__":
    main()
