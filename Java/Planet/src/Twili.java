/**
 * 
 * @author Grace Street CMS 270
 *
 */
public class Twili extends GameItems {
	/**
	 *constructor for Twili
	 * @param label  label given to alien
	 */
	public Twili(String label){
		super(label);
		oxygenBehavior= new DecreaseO2Twili();
	}
}
