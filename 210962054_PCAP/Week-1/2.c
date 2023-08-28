#include "mpi.h"
#include <stdio.h>
#include "math.h"
int main(int argc,char *argv[]){
int rank,size,power;
int x=2;
MPI_Init(&argc,&argv);
MPI_Comm_rank(MPI_COMM_WORLD,&rank);
MPI_Comm_size(MPI_COMM_WORLD,&size);
power= pow(x,rank);
printf("Rank:%d and power:%d in total %d processes \n",rank,power,size);
MPI_Finalize();
return 0;
}
