import java.util.ArrayList;
import java.util.Scanner;

public class Main{
    public static void main(String[] args){
    	Scanner sc = new Scanner(System.in);
    	int num = sc.nextInt();
    	int start = 1;
    	
    	while (true) {
    		if (num <= start) {
    			start = 0;
    			break;
    		}
    		
    		String str = Integer.toString(start);
    		int sum = start;
    		ArrayList<Integer> nums = new ArrayList<Integer>();
    		
    		for (int i =0; i < str.length(); i++) {
    			nums.add(Character.getNumericValue(str.charAt(i)));
    		}
    		
    		for (int i: nums) {
    			sum += i;
    		}
    		
    		if (sum == num) {
    			break;
    		}
    		start++;
    	}
    	System.out.println(start);
}
}