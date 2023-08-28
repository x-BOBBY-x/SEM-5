#include <stdio.h>
#include<stdlib.h>
#include "mpi.h"
int main(int argc, char* argv[])
{
int rank,size,f,n,sum,total[4], i,a[4][4],b[100];

MPI_Init(&argc,&argv);
MPI_Comm_rank(MPI_COMM_WORLD,&rank);
MPI_Comm_size(MPI_COMM_WORLD, &size);
MPI_Status status;
if(rank==0){
	printf("Enter the Elements:\n");
	for(i=0;i<4;i++){
		for(int j=0;j<4;j++){
			scanf("%d",&a[i][j]);
		}
	}
}
MPI_Bcast(&f,1,MPI_INT,0,MPI_COMM_WORLD);
MPI_Scatter(a,4,MPI_INT,b,4,MPI_INT,0,MPI_COMM_WORLD);
MPI_Scan (b,total, 4, MPI_INT, MPI_SUM, MPI_COMM_WORLD);
MPI_Gather(total,4,MPI_INT,a[rank],4,MPI_INT,0,MPI_COMM_WORLD);
if(rank==0){
printf("OUTPUT:\n");
for(i=0;i<4;i++){
		for(int j=0;j<4;j++){
			printf("%d \t",a[i][j]);
		}
		printf("\n");
	}
MPI_Finalize();
exit(0);
}}