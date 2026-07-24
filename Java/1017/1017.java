import java.io.IOException;
import java.util.Scanner;

public class Main {
 
    public static void main(String[] args) throws IOException {
 
        Scanner entrada = new Scanner(System.in);
        
        int travelHours = entrada.nextInt();
        double AverageSpeed = entrada.nextDouble()*travelHours;
        
        System.out.printf("%.3f\n", AverageSpeed/12);
        
		entrada.close();
 
    }
 
}