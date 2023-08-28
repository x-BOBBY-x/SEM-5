#include "mpi.h"
#include <stdio.h>
#include "math.h"
int main(int argc, char *argv[])
{

int rank,size,x[100],i,s=512;
int buf[s];
MPI_Init(&argc,&argv);
MPI_Comm_rank(MPI_COMM_WORLD,&rank);
MPI_Comm_size(MPI_COMM_WORLD, &size);
MPI_Status status;
MPI_Buffer_attach(buf,s);
if(rank==0)
{
printf("enter x:");
for(int i=0;i<size;i++){
	scanf("%d",&x[i]);
}
for(int i=1;i<size;i++){
	
	MPI_Bsend(&x[i],1,MPI_INT,i,i,MPI_COMM_WORLD);
	
}
int d= pow(x[0],2);
printf("THE ANSWER FOR RANK 0 =%d\n",d);

}
else if(rank%2==0){
	MPI_Recv(&x[rank],1,MPI_INT,0,rank,MPI_COMM_WORLD,&status);
	int c= x[rank]*x[rank];
	printf("THE ANSWER FOR RANK %d =%d\n",rank,c);
	}
else{
	MPI_Recv(&x[rank],1,MPI_INT,0,rank,MPI_COMM_WORLD,&status);
	int w=x[rank]*x[rank]*x[rank];
	printf("THE ANSWER FOR RANK %d =%d\n",rank,w);
	}

MPI_Buffer_detach(&buf,&s);
MPI_Finalize();
return 0;
}
