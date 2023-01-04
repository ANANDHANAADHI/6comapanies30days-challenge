import java.util.*;
class Substringcontainsabc {
    public static int numberOfSubstrings(String s) {
        HashMap<Character,Integer> hash = new HashMap<Character,Integer>();
        hash.put('a',0);
        hash.put('b',0);
        hash.put('c',0);
        int cnt =0 ,j =0;
        int a =-1,b =-1,c =-1;
        for( int i = 0;i<s.length();i++)
        {
            // System.out.println(hash + " " +cnt);
            if (s.charAt(i) == 'a')
            {
                a = i;
            }
            else if (s.charAt(i) == 'b')
            {
                b = i;
            }
            else
            {
                c = i;
            }
            if (a == -1 ||b == -1||c == -1)
            {
                continue;
            }
            else
            {
                j = Math.min(a,Math.min(c,b));
                cnt += j+1;
            }
           
        
        }
        return cnt;

    }
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String s = sc.next();
        System.out.println(numberOfSubstrings(s));
    }
}
