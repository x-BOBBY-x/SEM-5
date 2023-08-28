#include "mpi.h"
#include <stdio.h>
int main(int argc,char *argv[]){
int rank,size;
int a=5;
int b=4;
MPI_Init(&argc,&argv);
MPI_Comm_rank(MPI_COMM_WORLD,&rank);
MPI_Comm_size(MPI_COMM_WORLD,&size);
if(rank==0){
printf("%d)a-b=%d\n",rank,a-b);}
else if(rank==1){
printf("%d)a+b=%d\n",rank,a+b);}
else if(rank==2){
printf("%d)a*b=%d\n",rank,a*b);}
MPI_Finalize();
return 0;
}
