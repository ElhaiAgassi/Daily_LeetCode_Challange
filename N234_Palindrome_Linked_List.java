import java.util.Stack;

public class N234_Palindrome_Linked_List {
        public static boolean isPalindrome(ListNode head) {
            int total_length = 1;
            ListNode temp_node = head;
            while (temp_node.next != null) {
                total_length++;
                temp_node = temp_node.next;
            }
            temp_node = head;
            int half_length = total_length / 2, index = 0;

            Stack<Integer> stack = new Stack<>();
            while (temp_node != null) {
                if (index < half_length) {
                    stack.push(temp_node.val);
                } else if (index >= total_length - half_length) {
                    if (stack.pop() != temp_node.val) return false;
                }
                index++;
                temp_node = temp_node.next;
            }
            return true;

    }

//    public static void main(String[] args) {
//        ListNode l4 = new ListNode(1);
//        ListNode l3 = new ListNode(1, l4);
//        ListNode l2 = new ListNode(2, l3);
//        ListNode l1 = new ListNode(1, l2);
//
//        System.out.println(Solution.isPalindrome(l1));
//    }

}

//  Runtime: 28 ms, faster than 16.43% of Java online submissions for Palindrome Linked List.
//  Memory Usage: 102.7 MB, less than 30.45% of Java online submissions for Palindrome Linked List.
