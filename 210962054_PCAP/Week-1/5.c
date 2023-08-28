#include "mpi.h"
#include <stdio.h>
#include <string.h>
int main(int argc,char *argv[]){
int rank,size;
char string[]="HELLO";
char a;
MPI_Init(&argc,&argv);
MPI_Comm_rank(MPI_COMM_WORLD,&rank);
MPI_Comm_size(MPI_COMM_WORLD,&size);
string[rank]=string[rank]+32;
printf("Rank:%d in total %s processes \n",rank,string);
MPI_Finalize();
return 0;
}

