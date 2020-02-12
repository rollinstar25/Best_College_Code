/*SearchEngine Class

Objective: SearchEngine will:
    1. Takes in files
    2. Reads the files
    3. Tokenizes the input into play, act, scene, character, and line
    4. places words larger than 4 letters into index
    5. also contains method to look up in index
*/
import java.util.*;
import java.io.*;

public class SearchEngine{
    
    //variables
    private HashMap<String, ArrayList<Entry>> index;
    private ArrayList<Entry> info;
    
    private String title;
    private String act;
    private String scene;
    private String character;
    private String line;
    
    private String keyWord;
    
    /**Constructor for SearchEngine
    */
    public SearchEngine(){
        index = new HashMap<String, ArrayList<Entry>>();
        //creates the index with hashmap
        try{
            createIndex(index);
        }
        catch(FileNotFoundException fe){
            System.out.println("File Not Found");
        }
    }
    /**createIndex Method
    This method takes a Hashmap and fills it with values from a file
    
    @args:
        HashMap map  the index or hashmap beign filled
    */
    public void createIndex(HashMap map) throws FileNotFoundException{
        
    File playFolder = new File("texts");
    File[] files = playFolder.listFiles();
        //Create 2 scanners, one to read through lines, the other to tokenize input
        for(int i = 0; i < files.length; i++){ //loops through the plays
            Scanner lineReader = new Scanner(files[i]);
            this.title = lineReader.nextLine();//sets the title
            while(lineReader.hasNextLine()){
                String reader = lineReader.nextLine();
                reader = reader.replace("\t", " "); //replacing tab and all other punctuation with nothing,
                Scanner wordScanner = new Scanner(reader);
                while(wordScanner.hasNext()){
                    keyWord = wordScanner.next();
                    
                    if(keyWord.equals("ACT")){
                        keyWord += (" " + wordScanner.next());//adds the roman numerals
                        this.act = keyWord;
                    }
                    else if(keyWord.equals("SCENE")){
                        keyWord += (" " + wordScanner.next());
                        this.scene = keyWord;
                        reader = lineReader.nextLine();
                    }
                    else if(keyWord.equals("[")){
                        while(!keyWord.equals("]")){
                            keyWord = wordScanner.next();
                        }
                    }
                    else{
                        //need to grab the character name
                        if(keyWord.matches("[A-Z]{2,12}")){
                            this.character = keyWord;
                        }
                        
                        if(keyWord.length() > 4){
                            String undercase = keyWord.toLowerCase();
                            this.line = reader;
                            addNewWord(undercase);
                        }
                    }
                }//end word while
            }//end line while
        }//end of play for loop
        
    }//end createIndex
    
    /**addNewWord Method
    This method takes a word and adds it to a Hashmap.
    
    @args:
        String word    word being added
    */
    public void addNewWord(String word){
        //Need to be able to check if it's already in there
        Entry newWord = new Entry(title, act, scene, character, line);
        if(!index.containsKey(word)){
            //create new arraylist
            info = new ArrayList<Entry>();
            //add the entry
            info.add(newWord);
            //map it
            index.put(word, info);
        }
        else{
            //grab current array list
            info = index.get(word); 
            //add the element to it
            info.add(newWord);
        }
    }//end addNewWord
    
    /**lookUpWord Method
    This method looks up a specific word in the Hashmap, returns exceptions if 
    there is an error of any kind
    
    @args:
        String word  the word being looked up
    */
    public void lookUpWord(String word){
        if(word.length() <= 4){
            throw new IllegalArgumentException("words must be 5 letters or more.");
        }
        String lower = word.toLowerCase();
        
        if(!index.containsKey(lower)){
            throw new NoSuchElementException("This word does not exist in our store.");
        }
        
        ArrayList<Entry> wordInfo = index.get(lower);
        System.out.println("Hereth art thine results...\n");
        for(Entry entry: wordInfo){
            System.out.println(entry.toString());
            }// end for
    }//end lookUpWord
    
    
}//end of SearchEngine Class