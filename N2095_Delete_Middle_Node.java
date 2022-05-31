public class N2095_Delete_Middle_Node {
    public static ListNode deleteMiddle(ListNode head) {

        if (head.next == null) return null;
        if (head.next.next == null) {
            head.next = null;
            return head;
        }

        ListNode temp1 = head, temp2 = head;
        while (temp2.next != null && temp2.next.next != null&& temp2.next.next.next != null) {
            temp1 = temp1.next;
            temp2 = temp2.next.next;
        }
        temp1.next = temp1.next.next;
        return head;
    }

    public static void main(String[] args) {
        ListNode l7 = new ListNode(7);
        ListNode l6 = new ListNode(6,l7);
        ListNode l5 = new ListNode(5, l6);
        ListNode l4 = new ListNode(4, l5);
        ListNode l3 = new ListNode(3, l4);
        ListNode l2 = new ListNode(2, l3);
        ListNode l1 = new ListNode(1, l2);
        deleteMiddle(l1);
        System.out.print("[");
        for (ListNode i = l1; i != null; i = i.next) {
            System.out.print(i.val + ",");
        }
        System.out.println("]");
    }

}
//Runtime: 5 ms, faster than 60.54% of Java online submissions for Delete the Middle Node of a Linked List.
//Memory Usage: 209 MB, less than 57.38% of Java online submissions for Delete the Middle Node of a Linked List.

