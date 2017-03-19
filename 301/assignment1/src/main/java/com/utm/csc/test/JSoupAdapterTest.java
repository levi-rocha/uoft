package com.utm.csc.test;

import java.io.IOException;

import org.junit.Before;
import org.junit.Test;

import com.utm.csc.document.ParsedHTMLDocument;
import com.utm.csc.parser.JSoupAdapter;

import junit.framework.TestCase;

public class JSoupAdapterTest extends TestCase {

  private JSoupAdapter adapter;

  @Before
  public void setUp() {
    adapter = new JSoupAdapter();
  }

  @Test
  public void testParsePudim() throws IOException {
    ParsedHTMLDocument document = adapter.parseURL("http://pudim.com.br");
    assertEquals("Pudim", document.getTitle());
    assertEquals("pudim@pudim.com.br",
        document.getLinks().get("mailto:pudim@pudim.com.br"));
  }

}
