package com.utm.csc.view;

import java.util.Scanner;

public class Input {

  private Scanner scan;

  public Input() {
    scan = new Scanner(System.in);
  }

  public String getInput() {
    String input = scan.nextLine();
    return input;
  }

  public void close() {
    scan.close();
  }

}
