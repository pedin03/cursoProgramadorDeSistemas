//TIP To <b>Run</b> code, press <shortcut actionId="Run"/> or
// click the <icon src="AllIcons.Actions.Execute"/> icon in the gutter.
public class Main {
    public static void main(String[] args) {
        //TIP Press <shortcut actionId="ShowIntentionActions"/> with your caret at the highlighted text
        // to see how IntelliJ IDEA suggests fixing it.
        System.out.printf("Hello and welcome!");

        for (int i = 1; i <= 5; i++) {
            //TIP Press <shortcut actionId="Debug"/> to start debugging your code. We have set one <icon src="AllIcons.Debugger.Db_set_breakpoint"/> breakpoint
            // for you, but you can always add more by pressing <shortcut actionId="ToggleLineBreakpoint"/>.
            System.out.println("i = " + i);

            Mouse mouse1=new Mouse();
            mouse1.marca="Logitech";
            mouse1.modelo="Superlight";
            mouse1.cor="Rosa magenta";
            mouse1.dpi=32.000;
            mouse1.sensor="Hero 2";

            Mouse mouse2=new Mouse();
            mouse2.marca="Redragon";
            mouse2.modelo="M711 V2";
            mouse2.cor="Branco";
            mouse2.dpi=8.000;
            mouse2.sensor="Pixart PWM 3325";
        }
    }
}