package com.utm.csc.view.swing;

import java.awt.Font;

import javax.swing.Action;
import javax.swing.Icon;
import javax.swing.JButton;

public class ControlButton extends JButton {

  public static final int HEIGHT = 40;
  public static final int WIDTH = 70;

  public ControlButton(String text, int x, int y) {
    super(text);
    setFont(new Font("Microsoft Sans Serif", Font.PLAIN, 16));
    setBounds(x, y, WIDTH, HEIGHT);
  }

}
