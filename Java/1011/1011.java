import java.io.IOException;
import java.util.Scanner; 

public class Main {
 
    public static void main(String[] args) throws IOException {
 
        Scanner entrada = new Scanner(System.in);
        
        int    raio   = entrada.nextInt();
        double pi     = 3.14159;
        long   raio3  = (long) Math.pow(raio, 3);
        double volume = ((4.0/3.0)*pi*raio3);
        
        System.out.printf("VOLUME = %.3f\n",volume);
		
		entrada.close();
 
    }
 
}