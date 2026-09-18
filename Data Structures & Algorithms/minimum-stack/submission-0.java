class MinStack {
    private Stack<Integer> s;
    public MinStack() {
        s = new Stack<>();
    }
    
    public void push(int val) {
        s.push(val);
    }
    
    public void pop() {
        s.pop();
    }
    
    public int top() {
        return s.peek();
    }
    
    public int getMin() {
        Stack<Integer> tempStack = new Stack<>();
        int tempVal = s.peek();
        
        while (!s.isEmpty()){
            tempVal = Math.min(tempVal, s.peek());
            tempStack.push(s.pop());
        }

        while (!tempStack.isEmpty()){
            s.push(tempStack.pop());
        }

        return tempVal;
        
    }
}
