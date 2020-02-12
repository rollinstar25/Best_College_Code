import javafx.application.Application;
import javafx.fxml.FXMLLoader;
import javafx.stage.Stage;
import javafx.scene.Scene;
import javafx.scene.layout.*;


public class CoffeeMain extends Application {
	@Override
	public void start(Stage primaryStage) {
		try {
			VBox root = FXMLLoader.load( 
					getClass( ).getResource("coffee_machine.fxml"));
					
			Scene scene = new Scene(root,600,400);
			primaryStage.setScene(scene);
			primaryStage.setTitle( "Coffee Machine");
			primaryStage.show();
		} catch(Exception e) {
			e.printStackTrace();
		}
	}
	
	public static void main(String[] args) {
		launch(args);
	}
}

