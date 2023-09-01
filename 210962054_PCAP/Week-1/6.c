#include "mpi.h"
#include <stdio.h>
int fact(int n);
int fibo(int n);
int main(int argc,char *argv[]){
int rank,size;
MPI_Init(&argc,&argv);
MPI_Comm_rank(MPI_COMM_WORLD,&rank);
MPI_Comm_size(MPI_COMM_WORLD,&size);
if(rank%2==0){
printf("%d)factorial=%d \n",rank,fact(rank));}
else{
printf("%d)fibonnaci=%d \n",rank,fact(rank));}
MPI_Finalize();
int u= fibo(4);
printf("%d",u);
return 0;
}
int fact(int n){
int i;
if(n==0){
return 1;}
else{
return n*fact(n-1);}}
int fibo(int n){
int i;
if(n==0){return 0;}
else if(n==1){return 1;}
else{
return fibo(n-1)+fibo(n-2);}}
