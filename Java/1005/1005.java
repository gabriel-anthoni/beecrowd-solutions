import java.io.IOException;
import java.util.Scanner;

public class Main {
 
    public static void main(String[] args) throws IOException {
 
        Scanner entrada = new Scanner(System.in);
        
        double A = (entrada.nextDouble())*3.5;
        double B = (entrada.nextDouble())*7.5;
        System.out.printf("MEDIA = %.5f\n",((A+B)/11));
		
		entrada.close();
 
    }
 
}