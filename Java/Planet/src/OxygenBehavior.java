/**Oxygen Behavior Interface
 * 
 * @author Grace Street CMS 270
 *
 */
public interface OxygenBehavior {
	/**
	 * abstract method for adjusting the oxygen levels
	 * @param currentOxygen  amount of oxygen remaining
	 * @return   adjusted amount of oxygen
	 */
	public int adjustOxygen(int currentOxygen);

}
