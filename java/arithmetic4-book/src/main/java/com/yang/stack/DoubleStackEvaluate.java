package com.yang.stack;

import edu.princeton.cs.algs4.StdIn;

import java.util.Stack;

/**
 * Created by Yang on 2020/10/15 23:37
 *
 * 双Stack实现简单的运算操作
 */

public class DoubleStackEvaluate {

    /**
     * (1 + ((2 * 3 ) * (4*5)))
     *
     *
     * 思路: 使用二个Stack,第一个是是用来存储符号( , + , - , * / 这些的.
     *      还有一个Stack是用来存储值的.
     *      当遇见)的时候,就可以从 操作符中弹出符号(判断需要进行的擦走),然后从有值的Stack里面弹出二次进行操作.
     *      操作完了后放入到Stack中.
     *      最后一个Stack的值就是结果.
     * @param args
     */
    public static void main(String[] args) {

        Stack<String> ops = new Stack<String>();
        Stack<Double> values = new Stack<Double>();
        while (!StdIn.isEmpty()) {
            String s = StdIn.readString();
            if("(".equalsIgnoreCase(s)) { ops.push(s); }
            if("+".equalsIgnoreCase(s)){ ops.push(s); }
            if("-".equalsIgnoreCase(s)){ ops.push(s); }
            if("*".equalsIgnoreCase(s)){ ops.push(s); }
            if("/".equalsIgnoreCase(s)){ ops.push(s); }
            if(")".equalsIgnoreCase(s)){
                // 进行计算操作
                String op = ops.pop();
                Double val = values.pop();
                if("+".equalsIgnoreCase(op)){ val += values.pop(); }
                if("-".equalsIgnoreCase(op)){ val -= values.pop(); }
                if("*".equalsIgnoreCase(op)){ val *= values.pop();  }
                if("/".equalsIgnoreCase(op)){ val /= values.pop();  }
                values.push(val);
            } else {
                values.push(Double.parseDouble(s));
            }
        }
        System.out.println(values.pop());
    }
}
