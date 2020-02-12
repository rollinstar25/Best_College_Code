import java.util.Random;

/**
 * 
 * @author Grace Street CMS 270
 *
 */
public class PlanetHYX implements GamePlay {
	GameItems[][]gridArray;
	protected int currentOxygen = 500;
	protected int winningThreshold = 900;
	protected String label;
	
	/**
	 * constructor for PlanetHYX
	 * @param gridSize  the size of the grid of buttons 
	 */
	public PlanetHYX(int gridSize){
		gridArray = new GameItems [gridSize][gridSize];
		Random rand = new Random();
		for(int row = 0; row < gridSize ; row++){
			for(int col = 0; col < gridSize; col++){
				int value = rand.nextInt(10)+1;
				if(value >= 1 && value <= 3) {
					//place new Oxygen tank
					gridArray[row][col]= new OxygenTank("OxygenTank");
					//System.out.println("OxygenTank at ["+col+"]["+row+"]\n");
				}
				else if(value == 4){
					//place a Metagorgon
					gridArray[row][col] = new Metagorgon("Metagorgon");
					//System.out.println("Metagorgon at ["+col+"]["+row+"]\n");
				}	
				else if(value > 4 && value <= 6){
					//place a Naga
					gridArray[row][col] = new Naga("Naga");
					//System.out.println("Naga at ["+col+"]["+row+"]\n");
				}
				else if(value > 6 && value <= 10){
					//place a Twili
					gridArray[row][col] = new Twili("Twili");
					//System.out.println("Twili at ["+col+"]["+row+"]\n");
				}
				else{
					throw new IllegalArgumentException("The value has gone out of bounds.");
				}
			}
		}
		//place a spaceship at random place
		gridArray[rand.nextInt(gridSize)][rand.nextInt(gridSize)] = new SpaceShip("Space Ship");
		
	}
	/**
	 * method that adjusts the oxygen levels depending on the button the user presses
	 * @param int row  the row in which the button was pressed
	 * @param int col  the column in which the button was pressed
	 */
	public void play(int row, int col){
		
	  currentOxygen = gridArray[row][col].performOxygenAdjustment(currentOxygen);
		
	}
	/**
	 * accessor for the current oxygen the user has
	 * @return currentOxygen  amount of oxygen left
	 */
	public int getOxygen(){
		return currentOxygen;
		
	}
	/**
	 * accessor for the label of the object at the location the user pressed the button
	 * @param int row   row of the button pressed
	 * @param int col   column of the button pressed
	 * @return  label of object at the location [row][col]
	 */
	public String getLabel(int row, int col){
		return gridArray[row][col].getLabel();
		
	}
	/**
	 * accessor for the amount of oxygen the user gets for winning the game
	 * @return winningThreshold   amount of oxygen won upon victory
	 */
	public int getWinningThreshold(){
		return winningThreshold;
	}

}
