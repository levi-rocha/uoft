package com.utm.csc.game;

import static org.junit.Assert.assertEquals;

import org.junit.Before;
import org.junit.Test;

public class SquareTest {

  private Square square;

  @Before
  public void setUp() throws Exception {
    square = new Square();
  }

  @Test
  public void testIsEmpty() {
    assertEquals(" ", square.getStatus());
    assertEquals(true, square.isEmpty());
  }

  @Test
  public void testFill() {
    square.fill("X");
    assertEquals("X", square.getStatus());
  }

}
