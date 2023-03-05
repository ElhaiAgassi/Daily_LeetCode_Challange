

public class reverseBST {


    static class Node {
        int data;
        Node left;
        Node right;

        Node(int data) {
            this.data = data;
            left = null;
            right = null;
        }
    }

    static class BinaryTree {
        Node root;

        BinaryTree() {
            root = null;
        }

        void reverseOrder() {
            int height = height(root);

            for (int i = height; i >= 1; i--) {
                printLevel(root, i);
            }
        }

        int height(Node node) {
            if (node == null) {
                return 0;
            } else {
                int leftHeight = height(node.left);
                int rightHeight = height(node.right);

                return Math.max(leftHeight, rightHeight) + 1;
            }
        }

        void printLevel(Node node, int level) {
            if (node == null) {
                return;
            }
            if (level == 1) {
                System.out.print(node.data + " ");
            } else if (level > 1) {
                printLevel(node.right, level - 1);
                printLevel(node.left, level - 1);
            }
        }
    }

    static class Main {
        public static void main(String[] args) {
            BinaryTree tree = new BinaryTree();
            tree.root = new Node(1);
            tree.root.left = new Node(2);
            tree.root.right = new Node(3);
            tree.root.left.left = new Node(4);
            tree.root.left.right = new Node(5);

            System.out.println("Binary tree in reverse order:");
            tree.reverseOrder();
        }
    }
}


