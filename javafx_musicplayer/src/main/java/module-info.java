module com.example.javafx_musicplayer {
    requires javafx.controls;
    requires javafx.fxml;


    opens com.example.javafx_musicplayer to javafx.fxml;
    exports com.example.javafx_musicplayer;
}