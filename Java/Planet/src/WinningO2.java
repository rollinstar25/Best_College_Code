/**
 * 
 * @author Grace Street CMS 270
 *
 */
public class WinningO2 implements OxygenBehavior {
	 int winningO2 = 900;
	/**
	 * method that awards the user oxygen upon winning the game
	 * @param currentOxygen  the remaining amount of oxygen
	 * @return the adjusted oxygen level
	 */
	public int adjustOxygen(int currentOxygen){
		return currentOxygen + winningO2;
	}

}
