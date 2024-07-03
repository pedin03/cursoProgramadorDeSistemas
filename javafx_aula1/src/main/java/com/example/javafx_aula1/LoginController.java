package com.example.javafx_aula1;

import javafx.fxml.FXML;
import javafx.scene.control.*;
import javafx.stage.Stage;

import java.io.IOException;
import java.sql.*;

public class LoginController {
    @FXML
    private Label texto;
    @FXML
    private TextField email;
    @FXML
    private PasswordField senha;
    @FXML
    private Button entrar;
    @FXML
    private Hyperlink esqueciSenha;
    @FXML
    private Hyperlink criarconta;

    @FXML
    private void cliquebotaoentrar() throws IOException {
            String mail = email.getText();
            String pass = senha.getText();

            if (validarLogin(mail,pass)==true){
                telaCadastro();
            }
            else{
                texto.setText("Usuário ou senha incorretos");
            }
    }

    @FXML
    private void telaCadastro() throws IOException {
        Stage stage = (Stage) email.getScene().getWindow();
        SceneSwitcher.switchScene(stage, "hello-view.fxml");
    }

    private boolean validarLogin(String mail, String password) {
        String url = "jdbc:mysql://localhost:3306/aplicacao";
        String user = "root";
        String pwd = "";

        String query = "SELECT * FROM usuarios WHERE email = ? AND senha= ?";

        try (Connection connection = DriverManager.getConnection(url, user, pwd);
             PreparedStatement preparedStatement = ((Connection) connection).prepareStatement(query)) {

            preparedStatement.setString(1, mail);
            preparedStatement.setString(2, password);

            ResultSet resultSet = preparedStatement.executeQuery();
            return resultSet.next();

        } catch (SQLException e) {
            e.printStackTrace();
        }
        return false;
    }
}
