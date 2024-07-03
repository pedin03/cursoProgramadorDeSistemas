//TIP To <b>Run</b> code, press <shortcut actionId="Run"/> or
// click the <icon src="AllIcons.Actions.Execute"/> icon in the gutter.
public class Main {
    public static void main(String[] args) {
        /*int num=17;
        double num2=10.8;
        String nome="Pedro";
        System.out.println("Hello,"+nome+"!");
        if(num>10){
            System.out.println("Maior que 10");
        }
        else{
            System.out.println("Menor que 10!");
        }
        for(int i=0; i<10; i+=1){
            System.out.println(i);
        }*/
    Carro carro1=new Carro("Ford", "Mustang","Azul","OYB-3321",2022);
    Carro carro2=new Carro("Porsche","911","Preto","VSF-2214",2021);
    carro1.imprimir();
    carro2.imprimir();
    //carro1.marca="Ford";
       // carro1.setMarca("Ford");
    //carro1.setModelo("Mustang");
    //carro1.setCor("Azul");
    //carro1.setPlaca("OYB-3321");
    //carro1.setAno(2022);
    //carro1.setLigado(boolean ligado);
       // System.out.println("O carro da marca "+carro1.marca+" e modelo "+carro1.modelo+", é do ano de "+carro1.ano+" e possui a placa "+carro1.placa+".");//
   //carro1.ligar();
   //carro1.desligar();
        //carro1.acelerar();
        //carro1.drift();
    }
}

