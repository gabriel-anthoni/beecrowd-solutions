import java.io.IOException;
import java.util.Scanner;

public class Main {
 
    public static void main(String[] args) throws IOException {
 
        Scanner entrada = new Scanner(System.in);
        
        int totalDays = entrada.nextInt();
        int years     = Math.round(totalDays/365);
        int months    = Math.round((totalDays%365)/30);
        int days      = (totalDays%365)%30;
        
        System.out.printf("%d ano(s)\n%d mes(es)\n%d dia(s)\n",years,months,days);
        
		entrada.close();
 
    }
 
}