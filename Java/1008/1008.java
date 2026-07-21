import java.io.IOException;
import java.util.Scanner;

public class Main {
 
    public static void main(String[] args) throws IOException {
 
        Scanner entrada = new Scanner(System.in);
        
        int number      = entrada.nextInt();
        int hoursWorked = entrada.nextInt();
        double salary   = entrada.nextDouble();
        System.out.printf("NUMBER = %d\nSALARY = U$ %.2f\n",number,(salary*hoursWorked));
		
		entrada.close();
 
    }
 
}