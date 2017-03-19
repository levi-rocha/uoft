package com.utm.csc.view.swing;

import java.awt.Font;

import javax.swing.JButton;

public class TicTacButton extends JButton {

  public static final int SIDE = 80;

  public TicTacButton(int x, int y) {
    super("");
    setFont(new Font("Microsoft Sans Serif", Font.PLAIN, 16));
    setBounds(x, y, SIDE, SIDE);
  }

}
