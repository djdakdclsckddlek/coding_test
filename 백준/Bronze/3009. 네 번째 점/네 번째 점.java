import java.util.ArrayList;
import java.util.Scanner;

public class Main{
    public static void main(String[] args){
    Scanner sc = new Scanner(System.in);
	ArrayList<Integer> arrX = new ArrayList<Integer>();
	ArrayList<Integer> arrY = new ArrayList<Integer>();
	
	for (int i =0; i <3; i ++) {
		int x = sc.nextInt();
		int y = sc.nextInt();
		
		if (arrX.indexOf(x) != -1) {
			arrX.remove(arrX.indexOf(x));
		} else {			
			arrX.add(x);
		}
		
		if (arrY.indexOf(y) != -1) {
			arrY.remove(arrY.indexOf(y));
		} else {			
			arrY.add(y);
		}
		
	}
	int x = arrX.get(0);
	int y = arrY.get(0);
	System.out.println(x + " " + y);
}
}