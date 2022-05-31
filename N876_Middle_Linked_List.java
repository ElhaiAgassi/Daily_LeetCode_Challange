public class N876_Middle_Linked_List {
    public static ListNode middleNode(ListNode head) {
        if (head.next == null) return head;
        if (head.next.next == null) return head.next;

        ListNode temp1 = head, temp2 = head;


        while (temp2 != null && temp2.next != null) {
            temp1 = temp1.next;
            temp2 = temp2.next.next;
        }
        return temp1;
    }


//    public static void main(String[] args) {
//        ListNode l5 = new ListNode(4);
//        ListNode l4 = new ListNode(4,l5);
//        ListNode l3 = new ListNode(3, l4);
//        ListNode l2 = new ListNode(2, l3);
//        ListNode l1 = new ListNode(1, l2);
//
//        System.out.println(middleNode(l1).val);
//    }

}


//Runtime: 0 ms, faster than 100.00% of Java online submissions for Middle of the Linked List.
//        Memory Usage: 41.5 MB, less than 49.99% of Java online submissions for Middle of the Linked List.
