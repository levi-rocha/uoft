package com.utm.csc.game;

import com.utm.csc.exception.InvalidSquareException;
import com.utm.csc.exception.SquareAlreadyFilledException;
import com.utm.csc.view.GUI;
import com.utm.csc.view.IO;

public class Controller {

  private Board board;
  private IO io;
  private String currentPlayer;
  private String gameStatus;
  private int numberOfMoves;
  private int mode;

  public Controller(int mode) {
    board = new Board();
    this.mode = mode;
    if (mode == 1) {
      io = new IO();
    } else {
      io = new GUI(this);
    }
    gameStatus = "tie";
    currentPlayer = "X";
    numberOfMoves = 0;
  }

  public Controller(Board board, IO io, int mode) {
    this.mode = mode;
    this.board = board;
    this.io = io;
    gameStatus = "tie";
    currentPlayer = "X";
    numberOfMoves = 0;
  }

  public void playGame() {
    io.showStartingMessage();
    if (mode == 1) {
      gameLoop();
      showResult();
      io.close();
    }
  }

  private void gameLoop() {
    while (!isGameOver()) {
      try {
        makeMove();
        switchPlayer();
        numberOfMoves++;
        io.showBoardStatus(board);
      } catch (Exception e) {
        io.showErrorMessage(e.getMessage());
      }
    }
  }

  private void makeMove()
      throws SquareAlreadyFilledException, InvalidSquareException {
    int[] coordinates = io.getMove(currentPlayer);
    board.fillSquare(coordinates[0], coordinates[1], currentPlayer);
  }

  private void switchPlayer() {
    if (currentPlayer.equals("X")) {
      currentPlayer = "O";
    } else {
      currentPlayer = "X";
    }
  }

  private boolean isGameOver() {
    String[][] statuses = board.getSquaresStatus();
    int numberOfSquares = statuses.length * statuses.length;
    if (checkRows(statuses)) {
      return true;
    } else if (checkColumns(statuses)) {
      return true;
    } else if (checkDiagonals(statuses)) {
      return true;
    } else if (numberOfMoves == numberOfSquares) {
      return true;
    } else {
      return false;
    }

  }

  private boolean checkRows(String[][] statuses) {
    for (int i = 0; i < statuses.length; i++) {
      boolean rowFilled = true;
      String first = statuses[i][0];
      if (!first.equals(" ")) {
        for (int j = 0; j < statuses.length; j++) {
          if (!first.equals(statuses[i][j])) {
            rowFilled = false;
            break;
          }
        }
        if (rowFilled) {
          gameStatus = first;
          return true;
        }
      }
    }
    return false;
  }

  private boolean checkColumns(String[][] statuses) {
    for (int i = 0; i < statuses.length; i++) {
      boolean colFilled = true;
      String first = statuses[0][i];
      if (!first.equals(" ")) {
        for (int j = 0; j < statuses.length; j++) {
          if (!first.equals(statuses[j][i])) {
            colFilled = false;
            break;
          }
        }
        if (colFilled) {
          gameStatus = first;
          return true;
        }
      }
    }
    return false;
  }

  private boolean checkDiagonals(String[][] statuses) {
    boolean diagFilled = true;
    String first = statuses[0][0];
    if (!first.equals(" ")) {
      for (int i = 0; i < statuses.length; i++) {
        if (!first.equals(statuses[i][i])) {
          diagFilled = false;
          break;
        }
      }
      if (diagFilled) {
        gameStatus = first;
        return true;
      }
    }
    int back = statuses.length - 1;
    diagFilled = true;
    first = statuses[0][back];
    if (!first.equals(" ")) {
      for (int i = 1; i < statuses.length; i++) {
        if (!first.equals(statuses[i][back - i])) {
          diagFilled = false;
          break;
        }
      }
      if (diagFilled) {
        gameStatus = first;
        return true;
      }
    }
    return false;
  }

  private void showResult() {
    io.showResult(gameStatus);
  }

  public void moveMade(int x, int y) {
    try {
      board.fillSquare(x, y, currentPlayer);
      switchPlayer();
      numberOfMoves++;
      if (isGameOver()) {
        showResult();
      }
    } catch (Exception e) {
      e.printStackTrace();
    }
  }

  public void restart() {
    board = new Board();
    gameStatus = "tie";
    currentPlayer = "X";
    numberOfMoves = 0;
  }

  public int getNumberOfMoves() {
    return numberOfMoves;
  }

  public String getGameStatus() {
    return gameStatus;
  }

  public String getCurrentPlayer() {
    return currentPlayer;
  }


}
