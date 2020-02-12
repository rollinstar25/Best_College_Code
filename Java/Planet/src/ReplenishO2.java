import java.util.Random;
/**
 * 
 * @author Grace Street CMS 270
 *
 */
public class ReplenishO2 implements OxygenBehavior {
	int newOxygenLevel;
	/**
	 * method that replenished oxygen when the user runs into an oxygen tank
	 * @param currentOxygen  remaining amount of oxygen
	 * @return returns the adjusted oxygen level
	 */
	public int adjustOxygen(int currentOxygen){
		Random rand = new Random();
		newOxygenLevel = rand.nextInt(300)+1;
		return currentOxygen + newOxygenLevel;
	}

}
