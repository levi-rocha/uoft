package com.utm.csc.game;

import static org.mockito.Mockito.doReturn;
import static org.mockito.Mockito.mock;
import static org.mockito.Mockito.times;
import static org.mockito.Mockito.verify;

import org.junit.Before;
import org.junit.Test;

import com.utm.csc.view.IO;

public class ControllerTest {

  private Controller controller;
  private Board boardMock = mock(Board.class);
  private IO ioMock = mock(IO.class);

  @Before
  public void setUp() throws Exception {
    controller = new Controller(boardMock, ioMock);
  }

  @Test
  public void testPlayGame() {
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
    String[][] turn0 = {{" ", " ", " "}, {" ", " ", " "}, {" ", " ", " "}};
    String[][] turn1 = {{"X", " ", " "}, {" ", " ", " "}, {" ", " ", " "}};
    String[][] turn2 = {{"X", " ", " "}, {" ", "O", " "}, {" ", " ", " "}};
    String[][] turn3 = {{"X", " ", " "}, {" ", "O", " "}, {" ", " ", "X"}};
    String[][] turn4 = {{"X", " ", "O"}, {" ", "O", " "}, {" ", " ", "X"}};
    String[][] turn5 = {{"X", " ", "O"}, {" ", "O", " "}, {"X", " ", "X"}};
    String[][] turn6 = {{"X", " ", "O"}, {"O", "O", " "}, {"X", " ", "X"}};
    String[][] turn7 = {{"X", " ", "O"}, {"O", "O", " "}, {"X", "X", "X"}};
    doReturn(turn0).doReturn(turn1).doReturn(turn2).doReturn(turn3)
        .doReturn(turn4).doReturn(turn5).doReturn(turn6).doReturn(turn7)
        .when(boardMock).getSquaresStatus();
    controller.playGame();
    verify(ioMock).showStartingMessage();
    verify(ioMock, times(4)).getMove("X");
    verify(ioMock, times(3)).getMove("O");
    verify(boardMock, times(8)).getSquaresStatus();
    verify(ioMock, times(7)).showBoardStatus(boardMock);
    verify(ioMock).showResult("X");
  }

}
