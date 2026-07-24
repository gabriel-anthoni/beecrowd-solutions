import java.io.IOException;
import java.util.Scanner;

public class Main {
 
    public static void main(String[] args) throws IOException {
 
        Scanner entrada = new Scanner(System.in);
        
        String   numbers = entrada.nextLine();
        String[] values = numbers.split("\\s+");
        
        double A  = Double.parseDouble(values[0]);
        double B  = Double.parseDouble(values[1]);
        double C  = Double.parseDouble(values[2]);
        double pi = 3.14159;
        
        double Triangulo = ((A*C)/2);
        double Circulo   = (pi*(C*C));
        double Trapezio  = (((A+B)*C)/2);
        double Quadrado  = (B*B);
        double Retangulo = (A*B);
        
        System.out.printf("TRIANGULO: %.3f\nCIRCULO: %.3f\nTRAPEZIO: %.3f\nQUADRADO: %.3f\nRETANGULO: %.3f\n",Triangulo,Circulo,Trapezio,Quadrado,Retangulo);
		
		entrada.close();
 
    }
 
}