import java.io.IOException;
import java.util.Scanner;

public class Main {
 
    public static void main(String[] args) throws IOException {
 
        Scanner entrada = new Scanner(System.in);
        
        int    totalDistance = entrada.nextInt();
        double fuelConsumed  = entrada.nextDouble();
        
        System.out.printf("%.3f km/l\n",(totalDistance/fuelConsumed));
        
		entrada.close();
 
    }
 
}