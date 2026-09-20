class MinStack {
    
    ArrayList<Integer> stacker;
    ArrayList<Integer> minStack;

    public MinStack() {
        stacker = new ArrayList<Integer>();
        minStack = new ArrayList<Integer>();
    }
    
    public void push(int val) {
        stacker.add(val);
        if (minStack.size() > 0) {
            minStack.add(Math.min(minStack.get(minStack.size() - 1), val));
        } else {
            minStack.add(val);
        }
    }
    
    public void pop() {
        System.out.println("Pre-pop" + minStack.toString());
        stacker.remove(stacker.size() - 1);
        minStack.remove(minStack.size() - 1);
        System.out.println("Post-pop" + minStack.toString());
    }
    
    public int top() {
        return stacker.get(stacker.size() - 1);
    }
    
    public int getMin() {
        System.out.println(minStack);
        return minStack.get(stacker.size() - 1);
    }
}
