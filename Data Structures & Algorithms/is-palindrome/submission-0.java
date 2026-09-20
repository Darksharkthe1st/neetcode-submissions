class Solution {
    public boolean isPalindrome(String s) {
        char[] charry = s.toCharArray();
        ArrayList<Character> charray = new ArrayList<>(charry.length);
        for (char c : charry) {
            if (Character.isLetter(c) || Character.isDigit(c)) {
                charray.add(Character.toLowerCase(c));
            }
        }
        for (int i = 0; i < charray.size() / 2; i++) {
            if (charray.get(i) != charray.get(charray.size()-i-1)) {
                return false;
            }
        }
        return true;
    }
}
