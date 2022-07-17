public class Solution {
    public string ConvertToBase7(int num) {
        StringBuilder sb = new StringBuilder();
        bool isNeg = num < 0;
        num = num < 0 ? -num : num;

        while(num > 0){
            sb.Append(num % 7);
            num /= 7;
        }
        if(isNeg) { sb.Append("-"); }

        return sb.Length == 0 ? "0" : string.Join("", sb.ToString().Reverse());
    }
}