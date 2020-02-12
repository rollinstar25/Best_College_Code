/**
 * 
 * @author Grace Street CMS 270
 *
 */
public abstract class GameItems {
	protected OxygenBehavior oxygenBehavior;
	protected String label;
	
	/**
	 * constructor for GameItems
	 * @param label  the label given to each game item
	 */
	public GameItems(String label){
		this.label = label;
		}
	/**
	 * method performs an adjustment to the oxygen levels
	 * @param currentOxygen    remaining amount of oxygen
	 * @return  returns the current oxygen after adjustment
	 */
	public int performOxygenAdjustment(int currentOxygen){
		return oxygenBehavior.adjustOxygen(currentOxygen);
	}
	public String getLabel(){
		return label;
	}


}
