/**
 * 
 * @author Grace Street CMS 270
 *
 */
public class SpaceShip extends GameItems {
	/**
	 * constructor for the Space Ship
	 * @param label  label given to the ship
	 */
	public SpaceShip(String label){
		super(label);
		oxygenBehavior = new WinningO2();
	}

}
