class Solution {
    public int[] topKFrequent(int[] nums, int k) {
        if (k == nums.length) {
            return nums;
        }

        HashMap<Integer, Integer> freqMap = new HashMap<>();
        for (int i = 0; i < nums.length; i++) {
            Integer value = freqMap.get(nums[i]);
            if (value == null) {
                value = 0;
            }
            freqMap.put(nums[i], value + 1);
        }
        
        PriorityQueue<Value> que = new PriorityQueue<Value>();

        for (int x : freqMap.keySet()) {
            que.add(new Value(x, freqMap.get(x)));
        }

        int[] topK = new int[k];
        for (int i = 0; i < k; i++) {
            topK[i] = que.poll().a;
        }
        return topK;
    }

    class Value implements Comparable {
        int a, b;
        public Value(int a, int b) {
            this.a = a;
            this.b = b;
        }
        public int compareTo(Object o) {
            Value other = (Value)o;
            return other.b-b;
        }
    }
}
