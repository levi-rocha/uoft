package com.utm.csc.view;

import com.utm.csc.game.Board;

public class IO {

  private Input input;
  private Output output;

  public IO() {
    input = new Input();
    output = new Output();
  }

  public IO(Input input, Output output) {
    this.input = input;
    this.output = output;
  }

  public int[] getMove(String player) {
    Integer x = null;
    Integer y = null;
    while (y == null) {
      output.showOutput("Player " + player + " [row,col]: ");
      String moveInput = input.getInput();
      String[] coordinatesInput = moveInput.split(",");
      if (coordinatesInput.length != 2) {
        output
            .showOutput("Invalid move. Enter ’<row>,<col>’ to play a position. "
                + "For example, ’0,2’.\n");
        continue;
      }
      try {
        x = Integer.parseInt(coordinatesInput[0]);
      } catch (NumberFormatException e) {
        output
            .showOutput("Invalid move. Enter ’<row>,<col>’ to play a position. "
                + "For example, ’0,2’.\n");
        continue;
      }
      try {
        y = Integer.parseInt(coordinatesInput[1]);
      } catch (NumberFormatException e) {
        output
            .showOutput("Invalid move. Enter ’<row>,<col>’ to play a position. "
                + "For example, ’0,2’.\n");
        continue;
      }
    }
    int[] move = {x, y};
    return move;
  }

  public void showBoardStatus(Board board) {
    StringBuilder status = new StringBuilder();
    String[][] squares = board.getSquaresStatus();
    for (int i = 0; i < squares.length; i++) {
      for (int j = 0; j < squares.length; j++) {
        status.append(squares[i][j]);
        if (j != squares.length - 1) {
          status.append("|");
        }
      }
      status.append("\n");
      if (i != squares.length - 1) {
        for (int j = 0; j < squares.length; j++) {
          status.append("-");
          if (j != squares.length - 1) {
            status.append("+");
          }
        }
        status.append("\n");
      }
    }
    output.showOutput(status.toString());
  }

  public void showResult(String result) {
    if (result.equals("X")) {
      output.showOutput("Player X won.");
    } else if (result.equals("O")) {
      output.showOutput("Player O won.");
    } else {
      output.showOutput("No one won.");
    }
  }

  public void showStartingMessage() {
    output.showOutput(
        "Enter ’<row>,<col>’ to play a position. For example, ’0,2’.\n");
  }

  public void showErrorMessage(String message) {
    output.showOutput(message + "\n");
  }

  public void close() {
    input.close();
  }



}
