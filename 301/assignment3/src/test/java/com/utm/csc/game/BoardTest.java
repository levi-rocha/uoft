package com.utm.csc.game;

import static org.junit.Assert.assertEquals;
import static org.junit.Assert.fail;
import static org.mockito.Mockito.mock;
import static org.mockito.Mockito.verify;
import static org.mockito.Mockito.when;

import org.junit.Before;
import org.junit.Test;

public class BoardTest {

  private Board board;
  private Square[][] squaresMock = new Square[3][3];

  @Before
  public void setUp() throws Exception {
    for (int i = 0; i < 3; i++) {
      for (int j = 0; j < 3; j++) {
        squaresMock[i][j] = mock(Square.class);
      }
    }
    board = new Board(squaresMock);
  }

  @Test
  public void testFillSquare() {
    when(squaresMock[1][2].isEmpty()).thenReturn(true);
    try {
      board.fillSquare(1, 2, "O");
    } catch (Exception e) {
      fail();
    }
    verify(squaresMock[1][2]).isEmpty();
    verify(squaresMock[1][2]).fill("O");
  }

  @Test
  public void testGetSquareStatus() {
    when(squaresMock[0][0].getStatus()).thenReturn("X");
    String[][] status = board.getSquaresStatus();
    String actual = status[0][0];
    assertEquals("X", actual);
    verify(squaresMock[0][0]).getStatus();
  }

}
