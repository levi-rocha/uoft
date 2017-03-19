package com.utm.csc;

import com.utm.csc.game.Controller;

/**
 * Hello world!
 *
 */
public class App {
  public static void main(String[] args) {
    Controller controller;
    if (args.length > 0) {
      if (args[0].equals("gui")) {
        controller = new Controller(2);
      } else {
        controller = new Controller(1);
      }
    } else {
      controller = new Controller(1);
    }
    controller.playGame();
  }
}
