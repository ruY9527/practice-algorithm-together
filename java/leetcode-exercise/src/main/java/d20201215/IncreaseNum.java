package d20201215;

/**
 * Created by Yang on 2020/12/15 23:19
 *
 * link : https://leetcode-cn.com/problems/monotone-increasing-digits/
 */

public class IncreaseNum {


    public static void main(String[] args) {

        System.out.println(monotoneIncreasingDigits(1234));
        System.out.println(monotoneIncreasingDigits(332));

    }

    public static int monotoneIncreasingDigits(int N) {
        char[] strN = Integer.toString(N).toCharArray();
        int i = 1;
        while (i < strN.length && strN[i-1] <= strN[i]){
            i += 1;
        }
        if(i < strN.length){
            while (i > 0 && strN[i-1] > strN[i]) {
                strN[i -1] -= 1;
                i -= 1;
            }
            for(i += 1;i<strN.length;++i){
                strN[i] = '9';
            }
        }
        return Integer.parseInt(new String(strN));
    }

}
