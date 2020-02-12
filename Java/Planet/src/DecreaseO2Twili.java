/**
 * 
 * @author Grace Street CMS 270
 *
 */
public class DecreaseO2Twili implements OxygenBehavior {
		int newO2= 20;
		/**
		 * method that decreases the current oxygen should the user run into a Twili
		 * @param currentOxygen  the remaining oxygen amount
		 * @return  returns the adjusted oxygen level
		 */
		public int adjustOxygen(int currentOxygen){
			return currentOxygen - newO2;
			
		}

	}

