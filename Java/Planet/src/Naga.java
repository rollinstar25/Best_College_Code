/**
 * 
 * @author Grace Street CMS 270
 *
 */
public class Naga extends GameItems {
	/**
	 * constructor for Naga
	 * @param label  label given to the alien
	 */
	public Naga(String label){
		super(label);
		oxygenBehavior = new DecreaseO2Naga();
	}


}
