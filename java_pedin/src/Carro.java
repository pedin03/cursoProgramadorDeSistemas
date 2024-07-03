public class Carro {
    public String marca;
    public String modelo;
    public String cor;
    public String placa;
    protected int ano;
    private boolean ligado;

    public Carro(String marca, String modelo, String cor, String placa, int ano){
        setMarca(marca);
        setModelo(modelo);
        setCor(cor);
        setPlaca(placa);
        setAno(ano);
        setLigado(false);
    }
    public void imprimir(){
        System.out.println("O carro da marca"+marca+"do modelo"+modelo+", sua cor"+cor+"da placa"+placa+"e do ano de"+ano+".");
    }

    protected void ligar() {
        if (ligado == false) {
            //ligado = true;
            setLigado(true);
            System.out.println("O Carro foi ligado!");
        } else {
            System.out.println("O carro já estava ligado!");
        }
    }
    protected void desligar() {
        if (ligado == true) {
            //ligado = false;
            setLigado(false);
            System.out.println("O Carro foi desligado!");
        } else {
            System.out.println("O carro já estava desligado!");
        }
    }
    public void drift(){
            if (ligado == true) {
                System.out.println("uuurr!");
            }
            else{
                System.out.println("O carro está desligado!");
            }
            }
    public void acelerar(){
            if(ligado==true) {
                System.out.println("Vruum!");
            }
            else{
                System.out.println("O carro está desligado!");
            }
    }
    private void passar_marcha(){
        System.out.println("A Marcha foi trocada!");
    }
    private void ligar_farol(){
        System.out.println("Os faróis foram acesos!");
    }
    public void setMarca(String marca){
        this.marca=marca;
    }
    public String getMarca(){
        return marca;
    }

    public void setModelo(String modelo) {
        this.modelo = modelo;
        System.out.println("O modelo foi definido");
    }
    public String getModelo() {
        return modelo;
    }

    public void setCor(String cor) {
        this.cor = cor;
        System.out.println("A cor foi definida");
    }
    public String getCor(){
        return cor;
    }
    public void setPlaca(String placa) {
        this.placa = placa;
        System.out.println("A placa foi definida");
    }
    public String getPlaca(){
        return placa;
    }
    public void setAno(int ano) {
        this.ano = ano;
        System.out.println("O ano foi definido");
    }
    public String getAno(){
        return ano;
    }

    public void setLigado(boolean ligado) {
        this.ligado = ligado;
    }
    public String getLigado(){
        return ligado;
    }


}
