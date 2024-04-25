import java.util.Scanner;

public class Main{
    public static void main(String[] args){
    Scanner sc = new Scanner(System.in);
	int x = sc.nextInt();
	int y = sc.nextInt();
	int maxX = sc.nextInt();
	int maxY = sc.nextInt();
	
	int max = 1000;
	
	if (x < max) {max = x;}
	if (y < max) {max = y;}
	if (maxX - x < max) {max = maxX-x;}
	if (maxY - y < max) {max = maxY -y;}
	
	System.out.println(max);
}
}