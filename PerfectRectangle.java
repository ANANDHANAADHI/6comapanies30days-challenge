import java.util.*;
import java.io.*;
class PerfectRectangle {
    public static boolean isRectangleCover(int[][] rectangles) {
// 391.Perfect Reactangle
     if (rectangles.length == 0 || rectangles[0].length == 0) return false;
     int x1 = Integer.MAX_VALUE;
     int x2 = Integer.MIN_VALUE;
     int y1 = Integer.MAX_VALUE;
     int y2 = Integer.MIN_VALUE;

     HashSet<String> set = new HashSet<String>();
     int area = 0;
     for(int[] rect : rectangles) 
     {
         x1 = Math.min(rect[0],x1);
         x2 = Math.max(rect[2],x2);
         y1 = Math.min(rect[1],y1);
         y2 = Math.max(rect[3],y2);
         area += (rect[2] - rect[0])* (rect[3] - rect[1]);
         String s1 = rect[0] + " " + rect[1];
         String s2 = rect[0] + " " + rect[3];
         String s3 = rect[2] + " " + rect[3];
         String s4 = rect[2] + " " + rect[1];
         if (!set.add(s1)) set.remove(s1);
         if (!set.add(s2)) set.remove(s2);
         if (!set.add(s3)) set.remove(s3);
         if (!set.add(s4)) set.remove(s4);
     }
     if (!set.contains(x1 + " " + y1) || !set.contains(x1 + " " + y2) || !set.contains(x2 + " " + y1) || ! set.contains(x2 + " " + y2) || set.size() != 4) return false;
     return area == (x2-x1)*(y2-y1);
    }

    public static void main(String args[])
    {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int[][] a = new int[n][4];
        int[] arr = new int[n+1];
        for (int i =0; i<n;i++)
        {
            for (int j = 0;j<4;j++)
            {
            arr[j] = sc.nextInt();
            }
            a[i] = arr;
        }
        System.out.println(isRectangleCover(a));
    }
    
}