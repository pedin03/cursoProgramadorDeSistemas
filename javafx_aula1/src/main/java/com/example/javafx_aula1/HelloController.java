package com.example.javafx_aula1;

import javafx.fxml.FXML;
import javafx.scene.control.*;
import javafx.stage.Stage;

import java.io.IOException;
import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.PreparedStatement;
import java.sql.SQLException;

public class HelloController {
    @FXML
    private Label texto;
    @FXML
    private TextField nome;
    @FXML
    private TextField email;
    @FXML
    private PasswordField senha;
    @FXML
    private PasswordField confirmaSenha;
    @FXML
    private CheckBox termos;
    @FXML
    private Button cadastrar;
    @FXML
    private Hyperlink esqueciSenha;

    @FXML
private void cliquebotaocadastrar() {
        if(termos.isSelected()) {

            String name = nome.getText();
            String mail = email.getText();
            String pass = senha.getText();
            String confPass = confirmaSenha.getText();

            if(confereSenha(pass,confPass)==true) {
                SalvarNoBanco(name,mail,pass);

                System.out.println(name);
                System.out.println(mail);
                System.out.println(pass);
                System.out.println(confPass);
                texto.setText("Cadastro realizado com sucesso!");
            }else{
                texto.setText("Senhas não conferem!");
            }
            }else{
            texto.setText("Termos de uso obrigatório!");
        }
    }

    private boolean confereSenha(String senha, String confirmaSenha) {
        if(senha.equals(confirmaSenha)){
            return true;
        }else{
            return false;
        }
    }
    @FXML
    private void telaLogin() throws IOException {
        Stage stage = (Stage) email.getScene().getWindow();
        SceneSwitcher.switchScene(stage, "login-view.fxml");
    }

    private void SalvarNoBanco(String name, String mail, String pass) {
        String url = "jdbc:mysql://localhost:3306/aplicacao";
        String user = "root";
        String pwd = "";

        String query = "INSERT INTO usuarios (nome, email, senha) VALUES (?, ?, ?)";

        try (Connection connection = DriverManager.getConnection(url, user, pwd);
             PreparedStatement preparedStatement = connection.prepareStatement(query)) {

            preparedStatement.setString(1, name);
            preparedStatement.setString(2, mail);
            preparedStatement.setString(3, pass);

            int rowsAffected = preparedStatement.executeUpdate();
            if (rowsAffected > 0) {
                System.out.println("Usuário salvo com sucesso!");
            }

        } catch (SQLException e) {
            e.printStackTrace();
        }
    }
}