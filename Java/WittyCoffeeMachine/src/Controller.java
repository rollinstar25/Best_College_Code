import java.text.NumberFormat;

import javafx.event.ActionEvent;
	import javafx.fxml.FXML;
	import javafx.scene.control.Button;
	import javafx.scene.control.Label;
import javafx.scene.control.RadioButton;
import javafx.scene.control.TextField;
	import javafx.scene.text.Font;
	
public class Controller {

private double amountNumber;
	
	@FXML private Button enter, go, cancel;//added a cancel button
	//I put them into radiobuttons because you can visually see which one it is selected
	@FXML private RadioButton blackCoffee, coffeeWithSugar, coffeeWithSugarAndCreamer;
	@FXML private Label headerText, currentSelection, amountPaid, change;
	@FXML private TextField moneyPutIn;
	
	public static final NumberFormat MONEY = NumberFormat.getCurrencyInstance(); // added this so that we get it to look like money
	
	private CoffeeModel cc; // needs to be model, not CoffeeModel
	
	public void initialize( ) {
		cc = new CoffeeModel( ); // same reason as above
		
		headerText.setFont(new Font(20));
		go.setDisable(true);
		moneyPutIn.setDisable(true); //just disabled buttons for convenience
		amountPaid.setText(MONEY.format(amountNumber));
		cancel.setDisable(true);
		change.setText("");
		enter.setDisable(true);
		
	}
	
	@FXML protected void setSelection( ActionEvent ae ) {
		if( ae.getSource( ) == blackCoffee) {
			cc.setCoffeeType( "Black"); 
		} else if (ae.getSource( ) == coffeeWithSugar) {
			cc.setCoffeeType( "Sugar");
		} else if (ae.getSource( )  == coffeeWithSugarAndCreamer) {
			cc.setCoffeeType( "Sugar and Creamer");
		}
		moneyPutIn.setDisable(false); //reenable text field
		enter.setDisable(false);// reenabled the enter button
	}
	
	@FXML protected void calculateAmountPaid( ActionEvent ae ) {
		double price = .35;
		String amount = moneyPutIn.getText();//had to change to amount because same variable name as the button
		 amountNumber += Double.parseDouble( amount);

		 if( amountNumber >= price){
			 go.setDisable(false);	
			 amountPaid.setText(MONEY.format(amountNumber)); //Displays the amount paid on GUI
			 
		 }
	}
	
	@FXML protected void go( ActionEvent ae) {
		
		cc.calculateChange(amountNumber);
		// this will turn the result into a string and put it into the GUI
		change.setText(MONEY.format(cc.calculateChange(amountNumber)));
		cancel.setDisable(false); //reenables the cancel button
		
	}
	//created this as a stepping stone to our refund button
	@FXML protected void reset(ActionEvent ae){
		amountNumber = 0.00;
		initialize();//returns to the beginning state, still need to work out clearing the text field though...(you'll see when you run it)
		
	}

}
