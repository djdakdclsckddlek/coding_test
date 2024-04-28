import java.util.Arrays;
import java.util.Scanner;

public class Main{
    public static void main(String[] args){
    Scanner sc = new Scanner(System.in);
    
    while (true) {
    String st = sc.nextLine();
    if (st.equals("0 0 0")) {
    	break;
    }
    
    int[] input = Arrays.stream(st.split(" ")).mapToInt(Integer::parseInt).toArray();
    Arrays.sort(input);
   
    int a = input[0];
    int b = input[1];
    int c = input[2];
    
    if (c >= (a + b)) {
    	System.out.println("Invalid");
    } else if (a == b && b == c) {
    	System.out.println("Equilateral ");
    } else if (a != b && b != c && a != c) {
    	System.out.println("Scalene ");
    } else {
    	System.out.println("Isosceles ");
    }
    }
}
}