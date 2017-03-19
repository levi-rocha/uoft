package com.utm.csc.view;

import static org.junit.Assert.assertEquals;
import static org.junit.Assert.assertFalse;
import static org.junit.Assert.assertTrue;
import static org.mockito.Mockito.mock;

import org.junit.Before;
import org.junit.Test;

import com.utm.csc.game.Controller;

public class GUITest {

  private Controller cMock = mock(Controller.class);
  private GUI gui;

  @Before
  public void setUp() throws Exception {
    gui = new GUI(cMock);
  }

  @Test
  public void testShowResultX() {
    gui.showResult("X");
    assertEquals("X won.", gui.getLabel().getText());
    assertFalse(gui.getB00().isEnabled());
    assertFalse(gui.getB01().isEnabled());
    assertFalse(gui.getB02().isEnabled());
    assertFalse(gui.getB10().isEnabled());
    assertFalse(gui.getB11().isEnabled());
    assertFalse(gui.getB12().isEnabled());
    assertFalse(gui.getB20().isEnabled());
    assertFalse(gui.getB21().isEnabled());
    assertFalse(gui.getB22().isEnabled());
  }

  @Test
  public void testShowResultO() {
    gui.showResult("O");
    assertEquals("O won.", gui.getLabel().getText());
    assertFalse(gui.getB00().isEnabled());
    assertFalse(gui.getB01().isEnabled());
    assertFalse(gui.getB02().isEnabled());
    assertFalse(gui.getB10().isEnabled());
    assertFalse(gui.getB11().isEnabled());
    assertFalse(gui.getB12().isEnabled());
    assertFalse(gui.getB20().isEnabled());
    assertFalse(gui.getB21().isEnabled());
    assertFalse(gui.getB22().isEnabled());
  }

  @Test
  public void testShowResultTie() {
    gui.showResult("tie");
    assertEquals("Tie.", gui.getLabel().getText());
    assertFalse(gui.getB00().isEnabled());
    assertFalse(gui.getB01().isEnabled());
    assertFalse(gui.getB02().isEnabled());
    assertFalse(gui.getB10().isEnabled());
    assertFalse(gui.getB11().isEnabled());
    assertFalse(gui.getB12().isEnabled());
    assertFalse(gui.getB20().isEnabled());
    assertFalse(gui.getB21().isEnabled());
    assertFalse(gui.getB22().isEnabled());
  }

  @Test
  public void testShowStartingMessage() {
    gui.showStartingMessage();
    assertTrue(gui.getFrame().isVisible());
  }

}
