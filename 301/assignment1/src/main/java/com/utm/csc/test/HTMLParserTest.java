package com.utm.csc.test;

import java.io.ByteArrayOutputStream;
import java.io.PrintStream;

import org.junit.After;
import org.junit.Before;
import org.junit.Test;

import com.utm.csc.HTMLParser;

import junit.framework.TestCase;

public class HTMLParserTest extends TestCase {

  private final ByteArrayOutputStream output = new ByteArrayOutputStream();

  @Before
  public void setUp() {
    System.setOut(new PrintStream(output));
  }

  @After
  public void tearDown() {
    output.reset();
    System.setOut(null);
  }

  @Test
  public void testRunWithPudim() {
    HTMLParser.main(new String[] {"http://pudim.com.br"});
    String expected = "title: Pudim\n\n" + "link: mailto:pudim@pudim.com.br\n"
        + "text: pudim@pudim.com.br\n\n";
    assertEquals(expected, output.toString());
  }
}
