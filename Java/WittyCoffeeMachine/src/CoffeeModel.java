import java.text.NumberFormat;

public class CoffeeModel {

	public static final double CREAM_CAPACITY = 400.0;
	public static final double SUGAR_CAPACITY = 650.0;
	public static final NumberFormat MONEY = NumberFormat.getCurrencyInstance(); 
	
	private double change;
	private double price;
	private double creamLeft = CREAM_CAPACITY;
	private double sugarLeft = SUGAR_CAPACITY;

	/**
	 * Constructor for the Coffee Machine
	 */
	public CoffeeModel(){
		setPrice(0.35);
	}
	
	/**
	 * mutator for the price of a cup of coffee
	 * @param price  cost of the coffee
	 * @return  if price is positive, returns a reference to the CoffeeMachineModel object
	 *          otherwise, throws an exception
	 */
	public CoffeeModel setPrice(double price){
		if(price >= 0.00){
		this.price = price;
		return this;
		}
		else{
			throw new IllegalArgumentException("The price of the coffee must be positive.");
		}
	}
	
	/**
	 * accessor for the price of a cup of coffee
	 * @return price   the cost of the coffee
	 */
	public double getPrice(){
		return price;
	}
	
	/**
	 * method that reduces the amount of creamer left in the machine
	 * @return creamLeft   amount of creamer left in chamber
	 */
	public double useCreamer(){
		if(creamLeft < 5.0){
			System.out.println("Warning!! \nThere is not enough creamer! Please Refill!");
		}
		return creamLeft -= 5.0;
	}
	
	/**
	 * method that reduces the amount of sugar left in the machine
	 * @return sugarLeft    the amount of sugar left in the chamber
	 */
	public double useSugar(){
		if(sugarLeft < 6.5){
			System.out.println("Warning!! \nThere is not enough sugar! Please Refill!");
		}
		return sugarLeft -= 6.5;
	}
	
	/**
	 * method that calculates the change the user will receive
	 * @param amount   the amount of money the user puts in
	 * @return  if the amount > price, returns a string with the amount of change the user will receive
	 *          if the amount < price, returns a statement asking for more money
	 *          
	 */
	public double calculateChange(double amount){
		if(amount > price){
			change = amount - price;
			 
	
		}
		else if(amount < price){
			String changeString ="Please put in more money. The price is : " + MONEY.format(price);
			
		}
		
		return change;
	}
	
	/**
	 * method sets the coffe's type and calls the methods to make that coffee
	 * @param type  the type of coffee the user wants
	 */
	public void setCoffeeType(String type){
		
		if(type.equals("Black")){
			
		}
				
		else if(type.equals("Sugar")){
			useSugar();
		}
		else if(type.equals("Sugar and Creamer")){
			useCreamer();
			useSugar();
		}
		else
			throw new IllegalArgumentException("Never heard of this kind of coffee...\n"
					+"Please put in Black, Sugar, or Sugar and Creamer");
	}
	/**
	 * toString method for the Coffee Machine
	 * @return price      the cost of the coffee
	 *         creamLeft  the amount of cream left in the machine
	 *         sugarLeft  the amount of sugar left in the machine
	 */
	public String toString(){
		return "The price of coffee is : " + MONEY.format(price) 
		+ "\nRemaining Creamer: "+ creamLeft
		+"\nRemaining Sugar: "+ sugarLeft;
	}
}

