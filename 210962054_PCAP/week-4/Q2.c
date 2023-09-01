#include <stdio.h>
#include<stdlib.h>
#include "mpi.h"
int main(int argc, char* argv[])
{
int rank,size,n, i,done=0;
double mypi, pi, h, sum, x;

MPI_Init(&argc,&argv);
MPI_Comm_rank(MPI_COMM_WORLD,&rank);
MPI_Comm_size(MPI_COMM_WORLD, &size);
while (!done)
    {
	if (rank == 0) {
	    printf("Enter the number of intervals: (0 quits) ");
	    scanf("%d",&n);
	}
	MPI_Bcast(&n, 1, MPI_INT, 0, MPI_COMM_WORLD);
	if (n == 0) break;
  
	h   = 1.0 / (double) n;
	sum = 0.0;
	for (i = rank + 1; i <= n; i += size) {
	    x = h * ((double)i - 0.5);
	    sum += 4.0 / (1.0 + x*x);
	}
	mypi = h * sum;
    
	MPI_Reduce(&mypi, &pi, 1, MPI_DOUBLE, MPI_SUM, 0,
		   MPI_COMM_WORLD);
    
	if (rank == 0)
	    printf("pi is approximately %.16f",
		   pi);
    }
    MPI_Finalize();
    return 0;
}

