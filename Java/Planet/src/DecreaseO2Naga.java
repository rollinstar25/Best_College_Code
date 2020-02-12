/**
 * 
 * @author Grace Street CMS 270
 *
 */
public class DecreaseO2Naga implements OxygenBehavior {
		int newO2= 55;
		/**
		 * method that decreases the current oxygen should the user run into a Naga
		 * @param currentOxygen  the remaining oxygen amount
		 * @return  returns the adjusted oxygen level
		 */
		public int adjustOxygen(int currentOxygen){
			return currentOxygen - newO2;
			
		}

	}
