package com.utm.csc.parser;

import java.io.IOException;

import org.jsoup.Jsoup;
import org.jsoup.nodes.Document;
import org.jsoup.nodes.Element;
import org.jsoup.select.Elements;

import com.utm.csc.document.ParsedHTMLDocument;

public class JSoupAdapter {

  public ParsedHTMLDocument parseURL(String url) throws IOException {
    Document doc = Jsoup.connect(url).get();
    String title = doc.title();
    ParsedHTMLDocument parsed = new ParsedHTMLDocument(title);
    Elements links = doc.getElementsByTag("a");
    for (Element link : links) {
      String linkHref = link.attr("href");
      String linkText = link.text();
      if (linkHref.length() != 0)
        parsed.addLink(linkHref, linkText);
    }
    return parsed;
  }

}
