package com.utm.csc.test;

import java.io.ByteArrayOutputStream;
import java.io.PrintStream;

import org.junit.After;
import org.junit.Before;
import org.junit.Test;

import com.utm.csc.document.ParsedHTMLDocument;
import com.utm.csc.output.DocumentPrinter;

import junit.framework.TestCase;

public class DocumentPrinterTest extends TestCase {

  private ParsedHTMLDocument document;
  private DocumentPrinter printer;

  private final ByteArrayOutputStream output = new ByteArrayOutputStream();

  @Before
  public void setUp() {
    printer = new DocumentPrinter();
    document = new ParsedHTMLDocument("title");
    System.setOut(new PrintStream(output));
  }

  @After
  public void tearDown() {
    System.setOut(null);
  }

  @Test
  public void testPrintDocumentWithNoLinks() {
    printer.printDocument(document);
    String expected = "title: title\n\n";
    assertEquals(expected, output.toString());
  }

  @Test
  public void testPrintDocumentWithOneLink() {
    document.addLink("http://google.ca", "google");
    printer.printDocument(document);
    String expected =
        "title: title\n\n" + "link: http://google.ca\n" + "text: google\n\n";
    assertEquals(expected, output.toString());
  }

  @Test
  public void testPrintDocumentWithTwoLinks() {
    document.addLink("http://google.ca", "google");
    document.addLink("http://amazon.ca", "amazon");
    printer.printDocument(document);
    String expected = "title: title\n\n" + "link: http://google.ca\n"
        + "text: google\n\n" + "link: http://amazon.ca\n" + "text: amazon\n\n";
    assertEquals(expected, output.toString());
  }


}
