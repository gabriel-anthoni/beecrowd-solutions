import java.io.IOException;
import java.util.Scanner;

public class Main {
 
    public static void main(String[] args) throws IOException {
 
        Scanner entrada = new Scanner(System.in);
        
        int totalSeconds = entrada.nextInt();
        int hours        = Math.round(totalSeconds/3600);
        int minutes      = Math.round((totalSeconds/60)%60);
        int seconds      = totalSeconds%60;
        
        System.out.printf("%d:%d:%d",hours,minutes,seconds);
        
		entrada.close();
 
    }
 
}