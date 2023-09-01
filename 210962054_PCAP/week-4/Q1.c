#include <stdio.h>
#include<stdlib.h>
#include "mpi.h"
int main(int argc, char* argv[])
{
int rank,size,prd,fact=1,factsum, i;
MPI_Init(&argc,&argv);
MPI_Comm_rank(MPI_COMM_WORLD,&rank);
MPI_Errhandler_set(MPI_COMM_WORLD, MPI_ERRORS_RETURN);
MPI_Comm_size(MPI_COMM_WORLD, &size);
prd=rank+1;
MPI_Scan (&prd,&fact, 1, MPI_INT, MPI_PROD, MPI_COMM_WORLD);
MPI_Reduce (&fact,&factsum, 1, MPI_INT, MPI_SUM, 0, MPI_COMM_WORLD);

if(rank==0)
printf("Sum of all the factorial=%d",factsum);
MPI_Finalize();
exit(0);
}