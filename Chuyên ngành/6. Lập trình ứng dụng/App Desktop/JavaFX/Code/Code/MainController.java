
import javafx.scene.Node;
import javafx.scene.Scene;
import javafx.stage.Stage;
import javafx.event.ActionEvent;
import javafx.fxml.FXML;
import javafx.fxml.FXMLLoader;
import javafx.scene.image.ImageView;
import javafx.scene.Parent;
import javafx.scene.control.MenuBar;;

public class MainController {

    @FXML
    private ImageView myImage;

    @FXML
    private MenuBar myMenuBar;

    @FXML
    private void handleClick(ActionEvent event) {
        try{
            Parent root = FXMLLoader.load(getClass().getResource("View1.fxml"));
            Stage stage = (Stage) myMenuBar.getScene().getWindow();
            Scene scene = new Scene(root);
            stage.setScene(scene);
            stage.show();
        }
        catch(Exception e){
            
        }
    }

}
