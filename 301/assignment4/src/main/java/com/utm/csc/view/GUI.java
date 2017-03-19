package com.utm.csc.view;

import java.awt.Dimension;
import java.awt.Font;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;

import javax.swing.JButton;
import javax.swing.JFrame;
import javax.swing.JLabel;
import javax.swing.JPanel;
import javax.swing.border.EmptyBorder;

import com.utm.csc.game.Controller;
import com.utm.csc.view.swing.ControlButton;
import com.utm.csc.view.swing.TicTacButton;

public class GUI extends IO {

  private JFrame frame;
  private JPanel panel;
  private JButton b00, b01, b02, b10, b11, b12, b20, b21, b22, bnew, bquit;
  private JLabel label;

  private Controller controller;

  public GUI(Controller controller) {
    this.controller = controller;
    initialize();
  }

  private void initialize() {

    label = new JLabel("X Turn");
    label.setFont(new Font("Microsoft Sans Serif", Font.PLAIN, 16));
    label.setBounds(98, 250, 60, 40);

    initTicTacButtons();

    bnew = new ControlButton("New", 10, 250);
    bnew.addActionListener(new ActionListener() {
      public void actionPerformed(ActionEvent e) {
        bnewpress();
      }
    });

    bquit = new ControlButton("Quit", 160, 250);
    bquit.addActionListener(new ActionListener() {
      public void actionPerformed(ActionEvent e) {
        bquitpress();
      }
    });

    panel = new JPanel();
    panel.setPreferredSize(new Dimension(240, 300));
    panel.setLayout(null);
    panel.setBorder(new EmptyBorder(5, 5, 5, 5));

    panel.add(b00);
    panel.add(b01);
    panel.add(b02);
    panel.add(b10);
    panel.add(b11);
    panel.add(b12);
    panel.add(b20);
    panel.add(b21);
    panel.add(b22);
    panel.add(bnew);
    panel.add(bquit);
    panel.add(label);

    frame = new JFrame("Tic-Tac-Toe");
    frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
    frame.setLocationRelativeTo(null);
    frame.setResizable(false);

    frame.setContentPane(panel);
    frame.pack();
  }

  private void initTicTacButtons() {
    b00 = new TicTacButton(0, 0);
    b00.addActionListener(new ActionListener() {
      public void actionPerformed(ActionEvent e) {
        b00press();
      }
    });

    b01 = new TicTacButton(TicTacButton.SIDE, 0);
    b01.addActionListener(new ActionListener() {
      public void actionPerformed(ActionEvent e) {
        b01press();
      }
    });

    b02 = new TicTacButton(TicTacButton.SIDE * 2, 0);
    b02.addActionListener(new ActionListener() {
      public void actionPerformed(ActionEvent e) {
        b02press();
      }
    });

    b10 = new TicTacButton(0, TicTacButton.SIDE);
    b10.addActionListener(new ActionListener() {
      public void actionPerformed(ActionEvent e) {
        b10press();
      }
    });

    b11 = new TicTacButton(TicTacButton.SIDE, TicTacButton.SIDE);
    b11.addActionListener(new ActionListener() {
      public void actionPerformed(ActionEvent e) {
        b11press();
      }
    });

    b12 = new TicTacButton(TicTacButton.SIDE * 2, TicTacButton.SIDE);
    b12.addActionListener(new ActionListener() {
      public void actionPerformed(ActionEvent e) {
        b12press();
      }
    });

    b20 = new TicTacButton(0, TicTacButton.SIDE * 2);
    b20.addActionListener(new ActionListener() {
      public void actionPerformed(ActionEvent e) {
        b20press();
      }
    });

    b21 = new TicTacButton(TicTacButton.SIDE, TicTacButton.SIDE * 2);
    b21.addActionListener(new ActionListener() {
      public void actionPerformed(ActionEvent e) {
        b21press();
      }
    });

    b22 = new TicTacButton(TicTacButton.SIDE * 2, TicTacButton.SIDE * 2);
    b22.addActionListener(new ActionListener() {
      public void actionPerformed(ActionEvent e) {
        b22press();
      }
    });
  }

  private void b00press() {
    b00.setEnabled(false);
    b00.setText(controller.getCurrentPlayer());
    controller.moveMade(0, 0);
    updatePlayer();
  }

  private void b01press() {
    b01.setEnabled(false);
    b01.setText(controller.getCurrentPlayer());
    controller.moveMade(0, 1);
    updatePlayer();
  }

  private void b02press() {
    b02.setEnabled(false);
    b02.setText(controller.getCurrentPlayer());
    controller.moveMade(0, 2);
    updatePlayer();
  }

  private void b10press() {
    b10.setEnabled(false);
    b10.setText(controller.getCurrentPlayer());
    controller.moveMade(1, 0);
    updatePlayer();
  }

  private void b11press() {
    b11.setEnabled(false);
    b11.setText(controller.getCurrentPlayer());
    controller.moveMade(1, 1);
    updatePlayer();
  }

  private void b12press() {
    b12.setEnabled(false);
    b12.setText(controller.getCurrentPlayer());
    controller.moveMade(1, 2);
    updatePlayer();
  }

  private void b20press() {
    b20.setEnabled(false);
    b20.setText(controller.getCurrentPlayer());
    controller.moveMade(2, 0);
    updatePlayer();
  }

  private void b21press() {
    b21.setEnabled(false);
    b21.setText(controller.getCurrentPlayer());
    controller.moveMade(2, 1);
    updatePlayer();
  }

  private void b22press() {
    b22.setEnabled(false);
    b22.setText(controller.getCurrentPlayer());
    controller.moveMade(2, 2);
    updatePlayer();
  }

  private void bnewpress() {
    controller.restart();
    resetButtons();
    updatePlayer();
  }

  private void bquitpress() {
    System.exit(0);
  }

  private void updatePlayer() {
    label.setText(controller.getCurrentPlayer() + " Turn");
  }

  public void showResult(String result) {
    disableButtons();
    if (result.equals("X")) {
      label.setText("X won.");
    } else if (result.equals("O")) {
      label.setText("O won.");
    } else {
      label.setText("Tie.");
    }
  }

  private void disableButtons() {
    b00.setEnabled(false);
    b01.setEnabled(false);
    b02.setEnabled(false);
    b10.setEnabled(false);
    b11.setEnabled(false);
    b12.setEnabled(false);
    b20.setEnabled(false);
    b21.setEnabled(false);
    b22.setEnabled(false);
  }

  private void resetButtons() {
    b00.setEnabled(true);
    b00.setText("");
    b01.setEnabled(true);
    b01.setText("");
    b02.setEnabled(true);
    b02.setText("");
    b10.setEnabled(true);
    b10.setText("");
    b11.setEnabled(true);
    b11.setText("");
    b12.setEnabled(true);
    b12.setText("");
    b20.setEnabled(true);
    b20.setText("");
    b21.setEnabled(true);
    b21.setText("");
    b22.setEnabled(true);
    b22.setText("");
  }

  public void showStartingMessage() {
    frame.setVisible(true);
  }

  public JFrame getFrame() {
    return frame;
  }

  public JPanel getPanel() {
    return panel;
  }

  public JButton getB00() {
    return b00;
  }

  public JButton getB01() {
    return b01;
  }

  public JButton getB02() {
    return b02;
  }

  public JButton getB10() {
    return b10;
  }

  public JButton getB11() {
    return b11;
  }

  public JButton getB12() {
    return b12;
  }

  public JButton getB20() {
    return b20;
  }

  public JButton getB21() {
    return b21;
  }

  public JButton getB22() {
    return b22;
  }

  public JButton getBnew() {
    return bnew;
  }

  public JButton getBquit() {
    return bquit;
  }

  public JLabel getLabel() {
    return label;
  }

}
