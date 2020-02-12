import javafx.scene.*;
import javafx.scene.control.*;
import javafx.scene.layout.*;
import javafx.scene.paint.*;
import javafx.event.*;
/**
 * 
 * @author Grace Street CMS 270
 *
 */
public class PlanetHYXGUI extends BorderPane{
	private Label scoreLabel, scorePoints, gameStatus;
	private Button [][] buttons;  // 2-D array of buttons
	private GamePlay planet;
	
   // constructor
	/**
	 * constructor for the GUI
	 * @param gridSize   the size of the grid on the screen
	 */
	public PlanetHYXGUI( int gridSize ) {
		
		planet = new PlanetHYX( gridSize );
		
		gameStatus = new Label( "Choose a square");
		gameStatus.setStyle( "-fx-font-size:18");
		gameStatus.setTextFill( Color.BLUE);
		setTop( gameStatus);
		
		// bottom
		HBox scoreLayout = new HBox( );
		scoreLabel= new Label( "Oxygen level: ");
		scorePoints = new Label(Integer.toString( planet.getOxygen( )));
		scoreLayout.getChildren().addAll(scoreLabel, scorePoints);
		setBottom( scoreLayout);
		
		GridPane grid = new GridPane( );
		
		RowConstraints rowConstraints = new RowConstraints( );
		rowConstraints.setPercentHeight(100.0/gridSize);
		
		ColumnConstraints colConstraints = new ColumnConstraints( );
		colConstraints.setPercentWidth(100.0/gridSize);
		
		for ( int i= 0; i< gridSize; i++ ) {
			grid.getRowConstraints( ).add( rowConstraints);
			grid.getColumnConstraints().add(colConstraints);
		}
		
		buttons = new Button[gridSize][gridSize];
		PlayHandler ph = new PlayHandler( ); // instantiate inner class
		
		for ( int row = 0; row < gridSize; row++ ) {
			for ( int col = 0; col < gridSize; col++ ) {
				buttons[row][col] = new Button( "" );
				grid.add( buttons[row][col], col, row);
				buttons[row][col].setMaxWidth(Double.MAX_VALUE);
				buttons[row][col].setMaxHeight(Double.MAX_VALUE);
				buttons[row][col].setOnAction( ph );
			}
		}
		
		setCenter( grid);
		
	} // end constructor
	
	private class PlayHandler implements EventHandler<ActionEvent> {
		public void handle( ActionEvent event ) {
			//determine which button was pressed
		
			for ( int row = 0; row < buttons.length; row++ ) {
				for ( int col = 0; col < buttons.length; col++ ) {
					if ( event.getSource( ) == buttons[row][col]) {
						planet.play( row, col);
						buttons[row][col].setText( String.valueOf(planet.getLabel( row, col )));
						buttons[row][col].setOnAction(null);//makes it so that we wont respond to it anymore, can't click it again
						break;
				}
			}
				
			scorePoints.setText( Integer.toString(planet.getOxygen( )));
		}  if ( planet.getOxygen( ) >= planet.getWinningThreshold( ) ) {
	          gameStatus.setText("Game over! You're going home!" );
	          gameStatus.setTextFill(Color.BLUE);
	          disableButtons( );
	      } else if (planet.getOxygen( ) <= 0 ) {
	          gameStatus.setText( "Game over! You lost!" );
	          gameStatus.setTextFill(Color.RED);
	          disableButtons( ); 
	      }
	 
	    }
	  }
	  
	  private void disableButtons( ) {
		  for ( int row = 0; row < buttons.length; row++ ) {
		    for ( int col = 0; col < buttons[0].length; col++ ) {
		        buttons[row][col].setDisable(true);
		    }
		  }
	  }
}
	  