package com.utm.csc.view;

import static org.junit.Assert.assertArrayEquals;
import static org.mockito.Mockito.mock;
import static org.mockito.Mockito.verify;
import static org.mockito.Mockito.when;

import org.junit.Before;
import org.junit.Test;

import com.utm.csc.game.Board;

public class IOTest {

  private IO io;
  private Input inputMock = mock(Input.class);
  private Output outputMock = mock(Output.class);
  private Board boardMock = mock(Board.class);

  @Before
  public void setUp() throws Exception {
    io = new IO(inputMock, outputMock);
  }

  @Test
  public void testGetMove() {
    when(inputMock.getInput()).thenReturn("0,2");
    int[] expected = {0, 2};
    int[] actual = io.getMove("X");
    assertArrayEquals(expected, actual);
    verify(outputMock).showOutput("Player X [row,col]: ");
    verify(inputMock).getInput();
  }

  @Test
  public void testShowBoardStatus() {
    String[][] status = {{" ", " ", " "}, {" ", " ", " "}, {" ", " ", " "}};
    when(boardMock.getSquaresStatus()).thenReturn(status);
    io.showBoardStatus(boardMock);
    verify(boardMock).getSquaresStatus();
    String expectedOutput = " | | \n-+-+-\n | | \n-+-+-\n | | \n";
    verify(outputMock).showOutput(expectedOutput);
  }

  @Test
  public void testShowResult() {
    io.showResult("O");
    verify(outputMock).showOutput("Player O won.");
  }

  @Test
  public void testShowStartingMessage() {
    io.showStartingMessage();
    verify(outputMock).showOutput(
        "Enter ’<row>,<col>’ to play a position. For example, ’0,2’.\n");
  }

  @Test
  public void testShowErrorMessage() {
    io.showErrorMessage("error message");
    verify(outputMock).showOutput("error message\n");
  }

  @Test
  public void testClose() {
    io.close();
    verify(inputMock).close();
  }

}
