package com.utm.csc.output;

import java.util.HashMap;

import com.utm.csc.document.ParsedHTMLDocument;

public class DocumentPrinter {

  public void printDocument(ParsedHTMLDocument document) {
    System.out.print("title: " + document.getTitle() + "\n\n");
    HashMap<String, String> links = document.getLinks();
    for (String link : links.keySet()) {
      System.out.print("link: " + link + "\n");
      System.out.print("text: " + links.get(link) + "\n\n");
    }
  }

}
