class Solution {
    public boolean isValidSudoku(char[][] board) {
        boolean[] ten = new boolean[10];
        for (char[] row : board) {
            for (int i = 0; i < ten.length; i++) {
                ten[i] = false;
            }
            for (char c : row) {
                if (c == '.') {
                    continue;
                }
                if (ten[c-'0']) {
                    return false;
                } else {
                    ten[c-'0'] = true;
                }
            }
        }

        for (int j = 0; j < board[0].length; j++) {
            for (int k = 0; k < ten.length; k++) {
                ten[k] = false;
            }
            for (int i = 0; i < board.length; i++) {
                char c = board[i][j];
                if (c == '.') {
                    continue;
                }
                if (ten[c-'0']) {
                    return false;
                } else {
                    ten[c-'0'] = true;
                }
            }
        }

        for (int x = 0; x < 3; x++) {
            for (int y = 0; y < 3; y++) {
                int i = y*3;
                int j = x*3;
                
                for (int k = 0; k < ten.length; k++) {
                    ten[k] = false;
                }

                for (int k = 0; k < 9; k++) {
                    char c = board[i + k/3][j + k % 3];
                    if (c == '.') {
                        continue;
                    }
                    if (ten[c-'0']) {
                        return false;
                    } else {
                        ten[c-'0'] = true;
                    }
                }
            }
        }
        return true;
    }
}
