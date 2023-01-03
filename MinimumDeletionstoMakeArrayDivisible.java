import java.util.*;
//  Question no 2344 in leetcode platform
public class MinimumDeletionstoMakeArrayDivisible {
    public static int gcd(int x,int y)
    {
        if (y == 0){
            return x;
        }
        else{
            return gcd(y,x%y);
        }
    }
    public int minOperations(int[] nums, int[] numsDivide) {

        int Gcd = numsDivide[0];
        for (int i =1;i<numsDivide.length;i++)
        {
            Gcd = gcd(Gcd,numsDivide[i]);
        }
        Arrays.sort(nums);
        int cnt = 0;
        for(int i : nums){
            if (Gcd%i !=0){
                cnt++;
            }
            else{

            return cnt;
            }
        }
        return -1;
    }
    
}
