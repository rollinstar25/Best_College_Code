/**
 * 
 * @author Grace Street CMS 270
 *
 */
public class OxygenTank extends GameItems {
	/**
	 * constructor for the oxygen tank
	 * @param label  label given to the oxygen tank
	 */
	public OxygenTank(String label){
		super(label);
		oxygenBehavior= new ReplenishO2();
	}
}
