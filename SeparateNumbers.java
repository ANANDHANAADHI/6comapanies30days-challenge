import java.util.*;
import  java.io.*;
public class SeparateNumbers {
    

    public static int waystoseparate(String s)

    {
        int res = 0;
        int temp = Integer.parseInt(s.substring(0));
        int i = 1, pi =1;
        while(pi+i<s.length())
        {
            int n = Integer.parseInt(s.substring(pi,pi+i));
            System.out.println(n);
            if (temp < n)
            {
                res+=1;
                temp = n;
                pi = pi+i;
            }
            else{
                i++;
            }
        }

        return res;
    }

    public static void main(String args[])
    {
        Scanner sc  = new Scanner(System.in);
        String s = sc.nextLine();
        System.out.println(waystoseparate(s));
    }
}
