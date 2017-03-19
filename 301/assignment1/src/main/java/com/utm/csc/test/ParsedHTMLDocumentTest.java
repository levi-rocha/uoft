package com.utm.csc.test;

import org.junit.Before;
import org.junit.Test;

import com.utm.csc.document.ParsedHTMLDocument;

import junit.framework.TestCase;

public class ParsedHTMLDocumentTest extends TestCase {

  private ParsedHTMLDocument document;

  @Before
  public void setUp() {
    document = new ParsedHTMLDocument("title");
  }

  @Test
  public void testCreateEmptyWithTitle() {
    assertEquals("title is different from expected", "title",
        document.getTitle());
    assertEquals("link map size different from expected", 0,
        document.getLinks().size());
  }

  @Test
  public void testAddLink() {
    document.addLink("http://google.ca", "google");
    assertEquals("link was different from expected", "google",
        document.getLinks().get("http://google.ca"));
  }

}
