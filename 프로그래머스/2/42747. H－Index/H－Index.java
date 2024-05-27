import java.util.Arrays;
import java.util.Collections;

class Solution {
    public int solution(int[] citations) {
        int answer = 0;
        int n = citations.length;
        Arrays.sort(citations);
        for (int i = 0; i < n; i++) {
            if (citations[n - i - 1] < i + 1) {
                return i;
            }
        }
        return n;
    }
}