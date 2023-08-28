#include "mpi.h"
#include <stdio.h>
#include <string.h>
int main(int argc, char *argv[])
{
	int rank,size,i,n;
		
	char x[10];
	MPI_Init(&argc,&argv);
	MPI_Comm_rank(MPI_COMM_WORLD,&rank);
	MPI_Comm_size(MPI_COMM_WORLD, &size);
	MPI_Status status;
	if(rank==0)
	{
	char x[]="HELLO";
	n=strlen(x);
	MPI_Ssend(&n,1,MPI_INT,1,3,MPI_COMM_WORLD);
	for(int i=0;i<=n-1;i++){
	MPI_Ssend(&x[i],1,MPI_CHAR,1,1,MPI_COMM_WORLD);	

	}

	fprintf(stdout,"I have sent %s from process 0\n",x);
	fflush(stdout);
	for(int i=0;i<=n-1;i++){
	MPI_Recv(&x[i],1,MPI_CHAR,1,2,MPI_COMM_WORLD,&status);
	
	}
	for(int i=0;i<=n-1;i++){
	printf("%c\n",x[i]+32);	
	}
	
	}
	else
	{
	MPI_Recv(&n,1,MPI_INT,0,3,MPI_COMM_WORLD,&status);
	for(int i=0;i<=n-1;i++){
	MPI_Recv(&x[i],1,MPI_CHAR,0,1,MPI_COMM_WORLD,&status);
	}
	fprintf(stdout,"I have received %s in process 1\n",x);
	for(int i=0;i<=n-1;i++){
	MPI_Ssend(&x[i],1,MPI_CHAR,0,2,MPI_COMM_WORLD);
	}
	fflush(stdout);
	}
	MPI_Finalize();
	return 0;
}