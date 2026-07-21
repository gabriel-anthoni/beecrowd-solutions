import java.io.IOException;
import java.util.Scanner;

public class Main {
 
    public static void main(String[] args) throws IOException {
 
        Scanner entrada = new Scanner(System.in);
        
        double A = (entrada.nextDouble())*2;
        double B = (entrada.nextDouble())*3;
        double C = (entrada.nextDouble())*5;
        System.out.printf("MEDIA = %.1f\n",((A+B+C)/10));
		
		entrada.close();
 
    }
 
}