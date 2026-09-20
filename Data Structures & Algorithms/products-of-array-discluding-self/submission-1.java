class Solution {
    public int[] productExceptSelf(int[] nums) {
        int[] output = new int[nums.length];
        output[0] = 1;
        int mull = 1;
        for (int i = 0; i < nums.length-1; i++) {
            mull *= nums[i];
            output[i+1] = mull;
        }

        mull = 1;
        for (int i = nums.length-1; i > 0; i--) {
            mull *= nums[i];
            output[i-1] *= mull;
        }

        return output;
    }
}  
