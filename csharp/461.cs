public class Solution {
    public int HammingDistance(int x, int y) {
        int count = 0;

        int n = x ^ y;

        while(n != 0){
            if(n % 2 != 0) count++;
            n >>= 1;
        }
        return count;
    }
}