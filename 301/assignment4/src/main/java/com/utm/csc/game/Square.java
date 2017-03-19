package com.utm.csc.game;

public class Square {

  private String status;

  public Square() {
    status = " ";
  }

  public boolean isEmpty() {
    if (status.equals(" ")) {
      return true;
    } else {
      return false;
    }
  }

  public void fill(String player) {
    status = player;
  }

  public String getStatus() {
    return status;
  }



}
