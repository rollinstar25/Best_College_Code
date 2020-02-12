/*Entry Class
Contains the info on all the individual entries
*/
package cms330;
import java.util.*;


public class Entry{
    
    private String play;
    private String act;
    private String scene;
    private String character;
    private String line;
    
    /* Constructor for Entry 
    Will be NULL by default unless set otherwise
    */
    public Entry(String play, String act, String scene, String character, String line){
        this.play = play;
        this.act = act;
        this.scene = scene;
        this.character = character;
        this.line = line;
    }
    
    //Getters and Setters, just in case
    /**
    Accessor for play
    @return this.play  the play name
    */
    public String getPlay(){
        return this.play;
    }
    /**
    Mutator for play
    @args String newPlay  the new play
    */
    public void setPlay(String newPlay){
        this.play = newPlay;
    }
    /**
    Accessor for act
    @return this.act  the act
    */
    public String getAct(){
        return this.act;
    }
    /** 
    Mutator for act
    @args String newAct  the new act
    */
    public void setAct(String newAct){
        this.act = newAct;
    }
    /**
    Accessor for scene
    @return this.scene  the scene
    */
    public String getScene(){
        return this.scene;
    }
    /**
    Mutator for scene
    @args String newScene  the new scene
    */
    public void setScene(String newScene){
        this.scene = newScene;
    }
    /**
    Accessor for character
    @return this.character  character name
    */
    public String getCharacter(){
        return this.character;
    }
    
    /**
    Mutator for character
    @args String newCharacter  the new name
    */
    public void setCharacter(String newCharacter){
        this.character = newCharacter;
    }
    /**
    Accessor for line
    @return this.line  the line of play
    */
    public String getLine(){
        return this.line;
    }
    /** 
    Mutator for line
    @args String newLines   the newLines set
    */
    public void setLine(String newLines){
        this.line = newLines;
    }
    /** toString Method
    */
    @Override
    public String toString(){
        return "'''<br>" + this.play +"<br>" + this.act + ", " + this.scene + "<br>" + this.character
        + "<br>" + this.line + "<br>'''<br>";
    }
    
}
