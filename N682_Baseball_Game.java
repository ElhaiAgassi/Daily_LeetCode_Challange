public class N682_Baseball_Game {
    public static int calPoints(String[] ops) {
        int sum = 0;
        int[] arr = new int[ops.length];
        for (int i = 0, k = 0; i < ops.length; i++, k++) {

            switch (ops[i]) {
                case "+" -> arr[k] = arr[k - 1] + arr[k - 2];
                case "C" -> {
                    arr[--k] = 0;
                    k--;
                }
                case "D" -> arr[k] = arr[k - 1] * 2;
                default -> arr[k] = Integer.parseInt(ops[i]);
            }

        }
            for (int n : arr) {
                sum += n;
                System.out.print(n + ",");
            }


        return sum;
    }


    public static void main(String[] args) {
        String[] S = {"36","28","70","65","C","+","33","-46","84","C"};
        System.out.println(N682_Baseball_Game.calPoints(S));
    }
}

