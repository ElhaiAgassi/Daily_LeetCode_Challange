class N13_Roman_to_Integer {
    public static int romanToInt(String s) {
        int sum = 0;
        int carry = 0;
        for (int i = 1; i < s.length(); i++) {
            int a = value(s.charAt(i-1));
            int b = value(s.charAt(i));
            if (a < b) {
                sum -= a + carry;
                carry = 0;
            } else if (a > b) {
                sum += a+carry;
                carry = 0;
            } else {
                carry += a;
            }
        }

        sum+=value(s.charAt(s.length()-1));
        return sum;
    }

    public static int value(char c) {
        switch (c) {
            case 'I':
                return 1;
            case 'V':
                return 5;
            case 'X':
                return 10;
            case 'L':
                return 50;
            case 'C':
                return 100;
            case 'D':
                return 500;
            case 'M':
                return 1000;
            default:
                System.out.println("Error - invalid input");
                return 0;
        }

    }


    public static void main(String[] args) {
        System.out.println(romanToInt(""));
    }
}

//  Runtime: 7 ms, faster than 61.96% of Java online submissions for Roman to Integer.
//  Memory Usage: 44.6 MB, less than 70.52% of Java online submissions for Roman to Integer.
