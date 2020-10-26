package com.javaprojects;

public class Quick_Union {

    /* The difference between Quick_Find and Quick union is that Quick_find is too slow for large problems
    because the time complexity will be interpreted as O(N^2) but the Quick Union algorithm has much less time complexity i.e O(N)
     */
    public int[] id;
    public Quick_Union(int N){
        id = new int[N];
        for(int i = 0;i < N;i++){
            id[i] = i;
        }
    }
    private int root(int i){
        while(i != id[i]){
            i = id[i];
        }
        return i;
    }
    public boolean connected(int p,int q){
        return root(p) == root(q);
    }
    public void union(int p,int q){
        int i = root(p);
        int j = root(q);
        id[i] = j;
    }
}
