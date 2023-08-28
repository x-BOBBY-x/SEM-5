#include <stdio.h>
#include "mpi.h"
int fact(int n){
int i;
if(n==0){
return 1;}
else{
return n*fact(n-1);}}
int main(int argc,char * argv[]){
	int rank,size,a[10],b,chunk,n,sum=0;
	MPI_Init(&argc,&argv);
	MPI_Comm_rank(MPI_COMM_WORLD,&rank);
	MPI_Comm_size(MPI_COMM_WORLD,&size);
	MPI_Status status;
	if(rank==0){
		n=size;
		printf("Enter %d elements:",n);
		for(int i=0;i<n;i++){
			scanf("%d",&a[i]);
		}
		printf("READING DONE....\n");
		chunk=n/size;
	}
	MPI_Scatter(a,1,MPI_INT,&b,1,MPI_INT,0,MPI_COMM_WORLD);
	
	
	b=fact(b);
	
	MPI_Gather(&b,1,MPI_INT,a,1,MPI_INT,0,MPI_COMM_WORLD);
	if(rank==0)
	{
	fprintf(stdout,"The Result gathered in the root \n");
	fflush(stdout);
	for(int i=0; i<n; i++)
	fprintf(stdout,"%d \t",a[i]);
	fflush(stdout);
	for(int i=0; i<n; i++){
	sum+=a[i];
	}
	fprintf(stdout,"SUM=%d \t",sum);
	fflush(stdout);
	}
	MPI_Finalize();
	return 0;
}