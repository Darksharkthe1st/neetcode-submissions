class MinStack {
    
    ArrayList<Integer> stacker;

    public MinStack() {
        stacker = new ArrayList<Integer>();
    }
    
    public void push(int val) {
        stacker.add(val);
    }
    
    public void pop() {
        stacker.remove(stacker.size() - 1);
    }
    
    public int top() {
        return stacker.get(stacker.size() - 1);
    }
    
    public int getMin() {
        int minVal = stacker.get(0);
        for (int i = 0; i < stacker.size(); i++) {
            if (stacker.get(i) < minVal) {
                minVal = stacker.get(i);
            }
        }
        return minVal;
    }
}
