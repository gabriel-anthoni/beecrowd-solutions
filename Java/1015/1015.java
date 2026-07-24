import java.io.IOException;
import java.util.Scanner;

public class Main {
 
    public static void main(String[] args) throws IOException {
 
        Scanner entrada = new Scanner(System.in);
        
        String   numbers1 = entrada.nextLine();
        String[] values1 = numbers1.split("\\s+");
        String   numbers2 = entrada.nextLine();
        String[] values2 = numbers2.split("\\s+");
        
        double x1 = Double.parseDouble(values1[0]);
        double y1 = Double.parseDouble(values1[1]);
        double x2 = Double.parseDouble(values2[0]);
        double y2 = Double.parseDouble(values2[1]);
        
        double distance = Math.sqrt((Math.pow((x1-x2), 2))+(Math.pow((y1-y2), 2)));
        
        System.out.printf("%.4f\n", distance);
        
		entrada.close();
 
    }
 
}