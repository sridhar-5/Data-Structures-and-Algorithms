package com.javaprojects;

import java.util.Scanner;

public class Main {
    public static  void main(String[] args){
        Scanner input = new Scanner(System.in);
        int N = input.nextInt();
        Quick_Find uf = new Quick_Find(N);

        int no_of_iterations = input.nextInt();
        int i = no_of_iterations;
        while(i <= no_of_iterations){
            int p = input.nextInt();
            int q = input.nextInt();
            if(!uf.Connected(p,q)){
                uf.Union(p,q);
                System.out.println(p + "   " + q);
            }
            no_of_iterations--;
        }
    }
}
