package com.utm.csc.game;

import com.utm.csc.exception.InvalidSquareException;
import com.utm.csc.exception.SquareAlreadyFilledException;

public class Board {

  private Square[][] squares;

  public Board() {
    squares = new Square[3][3];
    for (int i = 0; i < 3; i++) {
      for (int j = 0; j < 3; j++) {
        squares[i][j] = new Square();
      }
    }
  }

  public Board(Square[][] squares) {
    this.squares = squares;
  }

  public void fillSquare(int x, int y, String player)
      throws SquareAlreadyFilledException, InvalidSquareException {
    if (x >= 0 && x < 3 && y >= 0 && y < 3) {
      if (squares[x][y].isEmpty()) {
        squares[x][y].fill(player);
      } else {
        throw new SquareAlreadyFilledException();
      }
    } else {
      throw new InvalidSquareException();
    }

  }

  public String[][] getSquaresStatus() {
    String[][] status = new String[3][3];
    for (int i = 0; i < 3; i++) {
      for (int j = 0; j < 3; j++) {
        status[i][j] = squares[i][j].getStatus();
      }
    }
    return status;
  }

}
