import java.util.Arrays;

public class N289_Game_Of_Life {

    public static class Solution {
        public static int[][] gameOfLife(int[][] board) {
            int[][] newCells = new int[board.length][board[0].length];
            for (int i = 0; i < board.length; i++) {
                for (int j = 0; j < board[0].length; j++) {
                    if (checkCell(board, i, j)) {
                        newCells[i][j] = 1;
                    }
                }
            }
           return newCells;
        }

        public static boolean isInside(int[][] cells, int x, int y) {
            return x >= 0 && x < cells.length && y >= 0 && y < cells[0].length;
        }

        public static int numberOfNeighbors(int[][] cells, int x, int y) {
            int neighborsNum = 0;
            for (int i = x - 1; i <= x + 1; i++) {
                for (int j = y - 1; j <= y + 1; j++) {
                    if (isInside(cells, i, j)) {
                        if (cells[i][j] != 0)
                            neighborsNum++;

                    }
                }
            }
//        }
            if (cells[x][y] != 0)
                neighborsNum--;
            return neighborsNum;
        }

        public static boolean checkCell(int[][] cells, int x, int y) {
            boolean cellIsAlive = false;
            int check = numberOfNeighbors(cells, x, y);

            if (cells[x][y] != 0) {
                if (check == 2 || check == 3) {
                    cellIsAlive = true;
                }
            } else {
                if (check == 3)
                    cellIsAlive = true;
            }

            return cellIsAlive;
        }

    }

    public static void main(String[] args) {
        int[][] board = {{0, 1, 0}, {0, 0, 1}, {1, 1, 1}, {0, 0, 0}};
        int[][] ans = Solution.gameOfLife(board);
        for (int[] an : ans) {
            System.out.println(Arrays.toString(an));
        }

    }

}
