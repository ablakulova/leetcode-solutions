public class Solution {
    public int SingleNumber(int[] nums) {
        int xOr = 0;

        foreach(int num in nums){
          xOr ^= num;
        }

        return xOr;
    }
}