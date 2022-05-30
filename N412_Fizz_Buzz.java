import java.util.ArrayList;
import java.util.List;

public class N412_Fizz_Buzz {
    public static List<String> fizzBuzz(int n) {
        List<String> list = new ArrayList<>();
        for (int i = 1; i <= n; i++) {
            int x= i %3, y=i%5;
            if ((x==0) && y==0){ list.add("FizzBuzz");}
            else if(y==0){list.add("Buzz");}
            else if(x==0){list.add("Fizz");}
            else list.add(""+i);
        }
        return list;
    }

    public static void main(String[] args) {
        System.out.println(fizzBuzz(15));
    }
}
//         Runtime: 2 ms, faster than 60.46% of Java online submissions for Fizz Buzz.
//        Memory Usage: 48.3 MB, less than 45.48% of Java online submissions for Fizz Buzz.
//