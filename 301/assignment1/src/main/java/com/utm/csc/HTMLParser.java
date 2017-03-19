package com.utm.csc;

import java.io.IOException;

import com.utm.csc.document.ParsedHTMLDocument;
import com.utm.csc.output.DocumentPrinter;
import com.utm.csc.parser.JSoupAdapter;

public class HTMLParser {

  public static void main(String[] args) {
    JSoupAdapter adapter = new JSoupAdapter();
    ParsedHTMLDocument document;
    DocumentPrinter printer = new DocumentPrinter();
    // for each url
    for (String url : args) {
      // parse url using jsoup adapter
      try {
        document = adapter.parseURL(url);
        printer.printDocument(document);
      } catch (IOException e) {
        System.out.println("There was an error with the url: " + url);
        e.printStackTrace();
      }
    }
  }
}
