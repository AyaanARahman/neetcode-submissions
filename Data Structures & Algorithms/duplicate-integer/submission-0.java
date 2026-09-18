class Solution {
    public boolean hasDuplicate(int[] nums) {
        Set<Integer> uniqueVals = new HashSet<>();
        for (int i = 0; i < nums.length; i++){
            if (uniqueVals.contains(nums[i])){
                return true;
            }
            uniqueVals.add(nums[i]);
        }
        return false;
 
    }
}
