import java.io.IOException;
import java.util.Scanner;

public class Main {
 
    public static void main(String[] args) throws IOException {
 
        Scanner entrada = new Scanner(System.in);
        
        String   numbers = entrada.nextLine();
        String[] values = numbers.split("\\s+");
        
        int A = Integer.parseInt(values[0]);
        int B = Integer.parseInt(values[1]);
        int C = Integer.parseInt(values[2]);
        
        if((A >= B) && (A >= C)) {
        	System.out.printf("%d eh o maior\n",A);
        } else if ((B >= A) && (B >= C)) {
        	System.out.printf("%d eh o maior\n",B);
        } else {
        	System.out.printf("%d eh o maior\n",C);
        }
        
		entrada.close();
 
    }
 
}