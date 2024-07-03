public class Mouse {
    String marca;
    String modelo;
    String cor;
    int dpi;
    String sensor;
    Boolean mexer=false;
    Boolean ligado=false;

    void ligar(){
        if(ligado == false){
            ligado = true;
            System.out.println("O mouse está ligado!");
        } else {
            System.out.println("O mouse já estava ligado!");
        }
    }
    void desligar(){
        if(ligado==true){
            ligado=false;
            System.out.println("O mouse está desligado!");
        } else {
            System.out.println("O mouse já estava desligado!");
        }
    }
    void mexer(){
        if(mexer=false){
            mexer=true;
            System.out.println("O mouse está rastreando.");
        } else {
            System.out.println("Mexa o mouse para rastrear.");
        }
    }
}
public class Mouse {
    String marca;
    String modelo;
    String cor;
    int dpi;
    String sensor;
    Boolean mexer=false;
    Boolean ligado=false;


}
