package cms330;

import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestParam;
import org.springframework.web.bind.annotation.RestController;


import java.util.*;
import java.nio.file.Files;
import java.nio.file.Paths;

@RestController
public class Controller {
    SearchEngine se;
    int count;

    // Fill this class with methods mapped to URLs

    // You should at least have a constructor that initializes the SearchEngine
    // and a query method that takes a String as input and returns its results.
    public Controller(){
        //initialize the search engine
        se = new SearchEngine();
    }
    
    @RequestMapping("/")
    public String index() {
        this.count++;

        String indexHtml = null;

        try {
            byte[] bytes = Files.readAllBytes(Paths.get("html/index.html"));
    	    indexHtml = new String(bytes);
        } catch(Exception e) {
            e.printStackTrace();
        }

    	return indexHtml;
    }
    
    @RequestMapping("/searching")
    public String searchForWord(@RequestParam(value="word") String word){
        //return results
        ArrayList<Entry> results = se.lookUpWord(word);
        String full = "";
        for(Entry e: results){
            full += e.toString();
        }
        return "<p>" + full + "</p>";
    }
    
    @RequestMapping("/alphabetLookUp")
    public String alphaLook(@RequestParam(value="letter") String letter){
        ArrayList<String> letterResults = se.alphabetLookUp(letter);
        String allLetters = "";
        for(String s: letterResults){
            allLetters += s + "<br>";
        }
        return "<p>" + allLetters + "</p>";
    }

    // Question to consider: do you want the query method to format the output
    // and return it as a String or do you want it to return an object that's
    // then formatted on the client side?

    // If you want to format the output on the server side, it must be in valid
    // HTML using <p> (for new paragraphs) and <br> (for line breaks).
}
