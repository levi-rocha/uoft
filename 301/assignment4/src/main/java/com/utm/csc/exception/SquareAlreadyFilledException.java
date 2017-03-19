package com.utm.csc.exception;

public class SquareAlreadyFilledException extends Exception {

  private static final long serialVersionUID = 7171946933091986624L;

  public SquareAlreadyFilledException() {
    super("Square already filled!");
  }

}
