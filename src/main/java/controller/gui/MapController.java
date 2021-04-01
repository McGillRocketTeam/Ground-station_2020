
	package controller.gui;

	import java.io.InputStream;

	import javafx.fxml.FXML;
	import javafx.scene.image.Image;
	import javafx.scene.image.ImageView;
	import javafx.scene.paint.Color;
	import javafx.scene.shape.Circle;
	import javafx.scene.text.Text;

	import java.io.FileInputStream; 
	import java.io.IOException;
	import java.io.InputStream;
	import javafx.application.Application; 
	import javafx.scene.Group; 
	import javafx.scene.Scene;  
	import javafx.stage.Stage;  
	import javafx.geometry.Insets;

	import javafx.scene.layout.StackPane;
	import javafx.scene.control.Label;
	import javafx.scene.control.Button;
	import javafx.scene.layout.*; 
	import javafx.event.ActionEvent; 
	import javafx.event.EventHandler; 
	import javafx.scene.transform.Scale;

	import javafx.scene.canvas.Canvas;
	import javafx.scene.canvas.GraphicsContext;
	import javafx.event.EventHandler;
	import javafx.scene.layout.Pane;
	import javafx.scene.paint.CycleMethod;
	import javafx.scene.paint.LinearGradient;
	import javafx.scene.paint.Stop;
	import javafx.scene.layout.VBox;
	import java.util.*;

	import javafx.collections.ObservableList; 

	import javafx.application.Application;
	import javafx.beans.InvalidationListener;
	import javafx.beans.Observable;
	import javafx.beans.property.DoubleProperty;
	import javafx.beans.property.SimpleDoubleProperty;
	import javafx.event.EventHandler;
	import javafx.scene.Scene;
	import javafx.scene.control.ScrollPane;
	import javafx.scene.image.Image;
	import javafx.scene.input.ScrollEvent;
	import javafx.fxml.FXMLLoader;

	import javafx.scene.text.TextAlignment;
	
	/**
	 * This class is used to create a visual map and indicator for the McGill Rocket Team Ground Station 2021. <p>
	 * 
	 * The background image currently being used can be found as src\main\resources\GoogleEarthMap.JPG. <p>
	 * 
	 * Change image: 
	 * If one chooses to make use of a different image, it must be oriented with north facing the top of the screen. 
	 * The upper and lower latitudes and longitudes must also be edited in the MapController class. <p>
	 * 
	 * Change image sizes:
	 * If one chooses to change image size, do so by changing the image_width, image_height, image_width_expanded, image_height_expanded
	 * parameters in the MapController class. <p>
	 * 
	 * @author Samuel Valentine
	 */
	
	public class MapController {
		
		/**
		 * To change image: 
		 * If one chooses to make use of a different image, it must be oriented with north facing the top of the screen. 
		 * The upper and lower latitudes and longitudes must also be edited in the MapController class. <p>
		 * 
		 * Note the following: 
		 * 	lower_lat = top of the screen
		 * 	upper_lat = bottom of the screen
		 * 	lower_lon = left of the screen
		 * 	upper_lon = right of the screen <p>
		 * 
		 * To change image size(s):
		 * If one chooses to change image size, do so by changing the image_width, image_height, image_width_expanded, image_height_expanded
		 * parameters in the MapController class.
		*/
			
		// THE STARTING SIZE OF THE IMAGE (INDEPENDANTLY CUSTOMIZABLE)
		private int image_width  = 2878	 	/10;
		private int image_height = 1634		/10;
		
		// THE ENLARGED SIZE OF THE IMAGE (INDEPENDANTLY CUSTOMIZABLE)
		private int image_width_extended  = 2878 	/2;
		private int image_height_extended = 1634 	/2;
		
		// THE CORNER LATITUDES AND LONGITUDES (MUST BE CHANGED WITH EVERY NEW IMAGE)
		final double lower_lat = 33.1736; // Top of the screen
		final double upper_lat = 32.8802; // Bottom of the screen
		final double lower_lon = 107.2299; // Left of the screen
		final double upper_lon = 106.7599; // Right of the screen
		
		// Necessary initializations (DON'T TOUCH)
		Circle circle = new Circle();
        Circle circle_extended = new Circle();
        
		
	    public static double decimal_converter(double degrees, double minutes, double seconds) {
	    	
	    	/**
	    	 * Converts latitudes and longitudes from the form [Degrees, Minutes, Seconds] to decimal values 
	    	 * that can be used in the circle-plotting algorithm.
	    	 * If latitudes and longitudes are already in this form (like old data), then this transformation is unnecessary
	    	 */
	    	
	    	return degrees + minutes/60 + seconds/3600;
	    }
	    
	    
	    public int find_x (double lon, int width) {
	    	/**
	    	 * Takes the longitude value and scales it proportionally to the width of the image on which the circle
	    	 * portraying the rocket's location will be displayed.
	    	 */
	    	 
	    	return Math.abs((int)(((lon - lower_lon)/(upper_lon-lower_lon))*width));
	    }
	    
	    
	    public int find_y (double lat, int height) {
	    	/**
	    	 * Takes the latitude value and scales it proportionally to the height of the image on which the circle
	    	 * portraying the rocket's location will be displayed.
	    	 */
	    	return Math.abs((int)(((lat - lower_lat)/(upper_lat-lower_lat))*height));
	    }
	    
	    
	    @FXML
	    StackPane stackpane;
	    
	    @FXML
	    StackPane stackpane2;
	    
	    @FXML
	    Label latlabel;
	   
	    @FXML
	    Label lonlabel;
	    
		public void initializeMap() throws Exception{
			
			/**
			 * Initializes all settings for both integrated and extended map displays. <p>
			 * Initializes button and creates event handler. <p>
			 */
			
	        // 	=== Get the image ===
	        ClassLoader classloader = Thread.currentThread().getContextClassLoader();
	    	InputStream stream = classloader.getResourceAsStream("GoogleEarthMap.JPG");
	        Image image = new Image(stream);
	        ImageView iv = new ImageView(image);
	        ImageView iv2 = new ImageView(image);
	        iv.setFitWidth(image_width);
	        iv.setPreserveRatio(true);
	        
	        //	=== Create button and button activation ===
	        Button button = new Button();
	        
	    	button.setText("Enlarge Map");
	        
	        EventHandler <ActionEvent> event = new EventHandler <ActionEvent> () {
	        	public void handle(ActionEvent e) {
	        		
	        		e.consume();
	        		
	        		iv2.setFitWidth(image_width_extended);
	        		iv2.setPreserveRatio(true);
	        		
	        		StackPane secondaryLayout = new StackPane();
	                secondaryLayout.getChildren().add(iv2);
	                secondaryLayout.getChildren().add(circle_extended);
	                
	                Scene secondScene = new Scene(secondaryLayout, image_width_extended,image_height_extended);

	                Stage newWindow = new Stage();
	                newWindow.setTitle("Map");
	                newWindow.setScene(secondScene);
	                newWindow.show();
	            } 
	        }; 
	        
	        button.setOnAction(event);
	        
	        //	==== Add to stackpanes to send to FXML file ====
	        stackpane.getChildren().add(iv);
	        stackpane.getChildren().add(circle);
	        stackpane.setPadding(new Insets(20));
	       
	        stackpane2.getChildren().add(button);
	        stackpane2.setPadding(new Insets(20));
		}
		
		
		public void addMapData(double[] data) {
			
			/**
			 * Updates integrated and extended maps using passed data, one index at a time.
			 */
			
			//	=== SIZE & COLOR OF CIRCLE ===
			//  Integrated display
	        circle.setRadius(5); 
	        circle.setFill(Color.RED);
			       
			//	Enlarged display
			circle_extended.setRadius(5); 
			circle_extended.setFill(Color.RED);
			
			//	=== Get data ===
			float x = Math.abs(Float.parseFloat(String.valueOf(data[DataIndex.LONGITUDE_INDEX.getOrder()])));
			float y = Math.abs(Float.parseFloat(String.valueOf(data[DataIndex.LATITUDE_INDEX .getOrder()])));
			
			//	=== Apply data ===
			//	Integrated Display
			circle.setTranslateX(-image_width  / 2 + find_x(x,image_width ));
			circle.setTranslateY(-image_height / 2 + find_y(y,image_height));
			
			//	Enlarged Display
			circle_extended.setTranslateX(-image_width_extended  / 2 + find_x(x,image_width_extended ));
			circle_extended.setTranslateY(-image_height_extended / 2 + find_y(y,image_height_extended));
			
			//	Create labels 
			latlabel.setText("Lat: "+x);
			lonlabel.setText("Lon: "+y);
			latlabel.setTextAlignment(TextAlignment.CENTER);
			lonlabel.setTextAlignment(TextAlignment.CENTER);
		}
	}