import java.util.*;
public class RotateFunction {
    // 396 on leet code
    public static int maxRotateFunction(int[] nums) {
        int s = 0;
        for (int i : nums)
        {
            s+=i;
        }
        int tots = 0;
        int n = nums.length;
        for (int i =1;i<nums.length;i++)
        {
            tots += (i * nums[i]);
        }
        int mx = tots;
        int temp = tots;
        for (int i = 0;i<nums.length;i++)
        {
            temp = (temp-s)+((n)*nums[i]);
            // System.out.println(temp+" "+i);
            if (mx < temp){
                mx =temp;
            }
            // temp = tots;
        }
        return mx;
    }
    public static void main(String args[])
    {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int[] arr = new int[n];
        for (int i =0; i<n;i++)
        {
            arr[i] = sc.nextInt();
        }
        System.out.println(maxRotateFunction(arr));
    }
    
}
