package com.utm.csc.game;

import static org.junit.Assert.*;
import static org.mockito.Mockito.doReturn;
import static org.mockito.Mockito.mock;
import static org.mockito.Mockito.times;
import static org.mockito.Mockito.verify;

import org.junit.Test;

import com.utm.csc.view.GUI;
import com.utm.csc.view.IO;

public class ControllerTest {

  private Controller controller;
  private Board boardMock = mock(Board.class);
  private IO ioMock;

  private String[][] turn0 =
      {{" ", " ", " "}, {" ", " ", " "}, {" ", " ", " "}};
  private String[][] turn1 =
      {{"X", " ", " "}, {" ", " ", " "}, {" ", " ", " "}};
  private String[][] turn2 =
      {{"X", " ", " "}, {" ", "O", " "}, {" ", " ", " "}};
  private String[][] turn3 =
      {{"X", " ", " "}, {" ", "O", " "}, {" ", " ", "X"}};
  private String[][] turn4 =
      {{"X", " ", "O"}, {" ", "O", " "}, {" ", " ", "X"}};
  private String[][] turn5 =
      {{"X", " ", "O"}, {" ", "O", " "}, {"X", " ", "X"}};
  private String[][] turn6 =
      {{"X", " ", "O"}, {"O", "O", " "}, {"X", " ", "X"}};
  private String[][] turn7 =
      {{"X", " ", "O"}, {"O", "O", " "}, {"X", "X", "X"}};

  @Test
  public void testPlayGameConsole() {
    ioMock = mock(IO.class);
    doReturn(turn0).doReturn(turn1).doReturn(turn2).doReturn(turn3)
        .doReturn(turn4).doReturn(turn5).doReturn(turn6).doReturn(turn7)
        .when(boardMock).getSquaresStatus();
    controller = new Controller(boardMock, ioMock, 1);
    int[] move1 = {0, 0};
    int[] move2 = {1, 1};
    int[] move3 = {2, 2};
    int[] move4 = {0, 2};
    int[] move5 = {2, 0};
    int[] move6 = {1, 0};
    int[] move7 = {2, 1};
    doReturn(move1).doReturn(move3).doReturn(move5).doReturn(move7).when(ioMock)
        .getMove("X");
    doReturn(move2).doReturn(move4).doReturn(move6).when(ioMock).getMove("O");
    controller.playGame();
    verify(ioMock).showStartingMessage();
    verify(ioMock, times(4)).getMove("X");
    verify(ioMock, times(3)).getMove("O");
    verify(boardMock, times(8)).getSquaresStatus();
    verify(ioMock, times(7)).showBoardStatus(boardMock);
    verify(ioMock).showResult("X");
  }

  @Test
  public void testPlayGameGUI() {
    doReturn(turn1).doReturn(turn2).doReturn(turn3).doReturn(turn4)
        .doReturn(turn5).doReturn(turn6).doReturn(turn7).when(boardMock)
        .getSquaresStatus();
    ioMock = mock(GUI.class);
    controller = new Controller(boardMock, ioMock, 2);
    controller.playGame();
    verify(ioMock).showStartingMessage();
    try {
      controller.moveMade(0, 0);
      verify(boardMock).fillSquare(0, 0, "X");
      controller.moveMade(1, 1);
      verify(boardMock).fillSquare(1, 1, "O");
      controller.moveMade(2, 2);
      verify(boardMock).fillSquare(2, 2, "X");
      controller.moveMade(0, 2);
      verify(boardMock).fillSquare(0, 2, "O");
      controller.moveMade(2, 0);
      verify(boardMock).fillSquare(2, 0, "X");
      controller.moveMade(1, 0);
      verify(boardMock).fillSquare(1, 0, "O");
      controller.moveMade(2, 1);
      verify(boardMock).fillSquare(2, 1, "X");
    } catch (Exception e) {
      fail("Should not throw exception");
    }
    verify(boardMock, times(7)).getSquaresStatus();
    verify(ioMock).showResult("X");
  }

  @Test
  public void testRestart() {
    controller = new Controller(boardMock, ioMock, 2);
    doReturn(turn1).when(boardMock).getSquaresStatus();
    controller.moveMade(0, 0);
    controller.restart();
    assertEquals("X", controller.getCurrentPlayer());
    assertEquals(0, controller.getNumberOfMoves());
    assertEquals("tie", controller.getGameStatus());
  }
}
