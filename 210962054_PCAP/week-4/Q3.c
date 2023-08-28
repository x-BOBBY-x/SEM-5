#include <stdio.h>
#include<stdlib.h>
#include "mpi.h"
int main(int argc, char* argv[])
{
int rank,size,f,n,sum,total, i,a[3][3],b[10];

MPI_Init(&argc,&argv);
MPI_Comm_rank(MPI_COMM_WORLD,&rank);
MPI_Comm_size(MPI_COMM_WORLD, &size);
MPI_Status status;
if(rank==0){
	printf("Enter the Elements:");
	for(i=0;i<3;i++){
		for(int j=0;j<3;j++){
			scanf("%d",&a[i][j]);
		}
	}
	printf("Enter the element to be searched:");
	scanf("%d",&f);
	
}
sum=0;
MPI_Bcast(&f,1,MPI_INT,0,MPI_COMM_WORLD);
MPI_Scatter(a,3,MPI_INT,b,3,MPI_INT,0,MPI_COMM_WORLD);
for(i=0;i<3;i++){
	if(b[i]==f){
		sum+=1;
	}
}
MPI_Reduce (&sum,&total, 1, MPI_INT, MPI_SUM, 0, MPI_COMM_WORLD);
if(rank==0){
printf("total=%d",total);}
MPI_Finalize();
exit(0);
}