/* Driver Class
Contains the main method and such
*/
import java.util.*;
public class Driver{
    public static void main(String[] args){
        //Instantiate SearchEngine
        SearchEngine start = new SearchEngine();
        System.out.println("Good morrow to you, sir or madam. Please chooseth a word to findeth.");
        Scanner user = new Scanner(System.in);
        String userWord = user.next();
        //Look up
        start.lookUpWord(userWord);
        
        //Need to include exception error cases
    }
}