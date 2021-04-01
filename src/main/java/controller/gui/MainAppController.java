package controller.gui;

import java.util.EnumMap;

import javafx.fxml.FXML;
import javafx.scene.control.SplitPane;
import javafx.scene.layout.AnchorPane;
import javafx.scene.layout.GridPane;
import javafx.scene.layout.Pane;
import javafx.scene.layout.VBox;

public class MainAppController {
	
	@FXML private GridPane numbers;
	@FXML private NumbersController numbersController;
	
	public void startTimer(double[] data) {
//		System.out.println(numbersController);
		numbersController.updateNumDisplay(data);
	}
	
	@FXML private GridPane graph;
	@FXML private GraphController graphController;
	
	public void mainAppInitializeGraphs() {
        graphController.initializeGraphs();
	}
	
	public void mainAppAddGraphData(double[] data) {
		graphController.addGraphData(data);
	}
	
	@FXML private VBox map;
	@FXML private MapController mapController;
	
	public void mainAppInitializeMap() throws Exception {
		mapController.initializeMap();
	}
	
	@FXML private SplitPane rawData;
	@FXML private RawDataController rawDataController;
	
	public void mainAppIntitializeRawData() throws Exception {
		rawDataController.initializeRawDataController();
	}
	
	public void mainAppAddMapData(double[] data) {
		mapController.addMapData(data);
	}
	
	public void mainAppAddRawData(double[] data) {
		rawDataController.addRawData(data);
	}
	
	@FXML private VBox gyro3d;
	@FXML private Gyro3dController gyro3dController;
	
	public void mainAppInitializeGyro() throws Exception {
		gyro3d.getChildren().add(gyro3dController.initializeGyro());
	}
	public void mainAppAddGyroData(double[] data){
		gyro3dController.addGyroData(data);
	}
}