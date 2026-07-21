import java.io.IOException;
import java.util.Scanner;

public class Main {
 
    public static void main(String[] args) throws IOException {
 
        Scanner entrada = new Scanner(System.in);
        
        String name   = entrada.nextLine();
        double salary = entrada.nextDouble();
        double bonus  = (entrada.nextDouble())*0.15;
        System.out.printf("TOTAL = R$ %.2f\n",salary+bonus);
		
		entrada.close();
 
    }
 
}