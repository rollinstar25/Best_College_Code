/**
 * 
 * @author Grace Street CMS 270
 *
 */
public class Metagorgon extends GameItems {
	/**
	 * constructor for Metagorgons
	 * @param label  the label given to the alien
	 */
	public Metagorgon(String label){
		super(label);
		oxygenBehavior = new DecreaseO2Metagorgon();
	}
	
}
