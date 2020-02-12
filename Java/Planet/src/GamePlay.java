/** GamePlay Interface */
/**
 * 
 * @author Grace Street CMS 270
 *
 */
public interface GamePlay {
	/**
	 * method that adjusts the oxygen depending on the button pressed
	 * @param row  row of button pressed
	 * @param col  column of button pressed
	 */
   void play( int row, int col ); 
   /**
    * accessor for the current amount of oxygen
    * @return  returns amount of remaining oxygen
    */
      int getOxygen( );
      /**
       * accessor for the label of the object for the button pressed
       * @param row  row of button pressed
       * @param col  column of button pressed
       * @return  returns label of object
       */
      String getLabel( int row, int col ); 
      /**
       * accessor for the prize amount of oxygen for winning
       * @return  returns the winning oxygen amount
       */
      int getWinningThreshold( );  
      
}