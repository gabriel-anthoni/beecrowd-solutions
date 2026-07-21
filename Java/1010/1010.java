import java.io.IOException;
import java.util.Scanner;

public class Main {
 
    public static void main(String[] args) throws IOException {
 
        Scanner entrada = new Scanner(System.in);
        
        String   numbers = entrada.nextLine();
        String[] product = numbers.split("\\s+");
        String   numbers2 = entrada.nextLine();
        String[] product2 = numbers2.split("\\s+");
        
        double value1 = (Double.parseDouble(product[2]))*(Integer.parseInt(product[1]));
        double value2 = (Double.parseDouble(product2[2]))*(Integer.parseInt(product2[1]));
        
        System.out.printf("VALOR A PAGAR: R$ %.2f\n",value1+value2);
		
		entrada.close();
 
    }
 
}