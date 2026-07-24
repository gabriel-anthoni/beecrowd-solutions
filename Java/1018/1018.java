import java.io.IOException;
import java.util.Scanner;

public class Main {
 
    public static void main(String[] args) throws IOException {
 
        Scanner entrada = new Scanner(System.in);
        
        int money = entrada.nextInt();
        int values[] = {100,50,20,10,5,2,1};
        
        System.out.printf("%d\n", money);
        for(int value = 0;value < values.length;value++) {
        	System.out.printf("%d nota(s) de R$ %d,00\n",(money/values[value]),values[value]);
        	money %= values[value];
        }
        
		entrada.close();
 
    }
 
}