package com.javaprojects;

public class Quick_Find{
    private int[] id;

    /* Now we set a parametrised constructor to set the size of the array
       and then initialize all the array elements with the indexes.
     */
    public Quick_Find(int N){
        id = new int[N];
        for(int i = 0;i < N;i++){
            id[i] = i;
        }
    }
    public boolean Connected(int p,int q){
        return id[p] == id[q];
    }
    public void Union(int p,int q){
        int pid = id[p];
        int qid = id[q];

        for(int i = 0;i < id.length ; i++){
            if(id[i] == pid){
                id[i] = qid;
            }
        }
    }
}
