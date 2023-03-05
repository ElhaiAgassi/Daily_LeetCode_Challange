import java.util.Collections;
import java.util.LinkedList;
import java.util.List;

public class N989_add_to_array {
    public static List<Integer> addToArrayForm(int[] num, int k) {
        List<Integer> ans = new LinkedList<>();
        for (int i = 0; i < num.length; i++) {
            int current = num.length - i - 1;
            int sum = (num[current] + k) % 10;
            ans.add(sum);
            k = (k + num[current]) / 10;
        }
        while (k > 0) {
            ans.add(k % 10);
            k /= 10;
        }
        Collections.reverse(ans);
        return ans;
    }


    public static void main(String[] args) {
        int[] ar = new int[]{2, 1, 5};
        System.out.println(addToArrayForm(ar, 806));
    }
}
