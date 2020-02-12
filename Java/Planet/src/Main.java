import javafx.application.Application;
import javafx.stage.Stage;
import javafx.scene.Scene;
import javafx.scene.control.*;
import java.util.*;
/**
 * 
 * @author Grace Street CMS 270
 *
 */
public class Main extends Application {
	/**
	 * starts the program
	 * @param primaryStage  the initial stage of the game
	 */
	@Override
	public void start(Stage primaryStage) {
		try {
		 TextInputDialog dialog = new TextInputDialog("4" );
         dialog.setTitle("Grid Size for Game");
         dialog.setHeaderText("");
         dialog.setContentText("Enter the grid size");

         // Traditional way to get the response value.
         Optional<String> result = dialog.showAndWait();
         if (result.isPresent()){
            int gridSize =  Integer.parseInt(result.get());


   // The Java 8 way to get the response value (with lambda expression).
   //result.ifPresent(name -> System.out.println("Your name: " + name));
         
	        PlanetHYXGUI phxy = new PlanetHYXGUI( gridSize );
			Scene scene = new Scene(phxy,400,400);
			primaryStage.setScene(scene);
			primaryStage.setTitle("PlanetHYX");
			primaryStage.show( );
         }
		} catch(Exception e) {
			e.printStackTrace();
		}
	}
	/**
	 * main program
	 * @param args
	 */
	public static void main(String[] args) {
		launch(args);
	}
}
