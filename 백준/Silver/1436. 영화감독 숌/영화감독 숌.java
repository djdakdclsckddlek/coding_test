import java.util.ArrayList;
import java.util.Scanner;

public class Main {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int input = sc.nextInt();
		int cur = 1666;
		// 666 1666 2666 3666 4666 5666 6660 6661 6662 6663 6664 6665
		// 6666 6667 6668 6669 7666 8666 9666 10666
		// 11666 12666 13666 14666 15666 16660 16661 16663 16664 16665 16666 1666
		
		ArrayList<Integer> table = new ArrayList<Integer>();
		table.add(666);
		
		while (table.size() < input) {
				String str = Integer.toString(cur);
				if (str.contains("666")) {
					table.add(cur);
					cur++;
				} else {
					cur++;
				}
			}
		System.out.println(table.get(input-1));
}
}