package com.utm.csc.document;

import java.util.HashMap;

public class ParsedHTMLDocument {

  private String title;
  private HashMap<String, String> links;


  public ParsedHTMLDocument(String title) {
    this.title = title;
    this.links = new HashMap<String, String>();
  }

  public void addLink(String link, String text) {
    links.put(link, text);
  }

  public HashMap<String, String> getLinks() {
    return links;
  }

  public String getTitle() {
    return title;
  }


}
