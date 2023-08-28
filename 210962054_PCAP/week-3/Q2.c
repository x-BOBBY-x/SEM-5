#include <stdio.h>
#include "mpi.h"
int main(int argc,char * argv[]){
	int rank,size,n,m;
	float a[10],c[10],d,b[10],chunk,sum=0, sum1=0;
	MPI_Init(&argc,&argv);
	MPI_Comm_rank(MPI_COMM_WORLD,&rank);
	MPI_Comm_size(MPI_COMM_WORLD,&size);
	MPI_Status status;
	if(rank==0){
		n=size;
		printf("Enter M:");
		scanf("%d",&m);
		printf("Total Elements:%d\n",m*n);
		printf("Enter %d elements:",n*m);
		for(int i=0;i<(n*m);i++){
			scanf("%f",&a[i]);
		}
		printf("READING DONE....\n");
		
	}
	MPI_Bcast(&m,1,MPI_INT,0,MPI_COMM_WORLD);
	MPI_Scatter(a,m,MPI_FLOAT,b,m,MPI_FLOAT,0,MPI_COMM_WORLD);
	for(int i=0; i<m; i++){
		sum+=b[i];
	}

	d=sum/m;
	printf("%f",d);
	
	MPI_Gather(&d,1,MPI_FLOAT,c,1,MPI_FLOAT,0,MPI_COMM_WORLD);
	if(rank==0)
	{
		fprintf(stdout,"The Result gathered in the root \n");
		fflush(stdout);
		for(int i=0; i<n; i++)
		printf("%f \t",c[i]);
		for(int i=0; i<n; i++){
		sum1+=c[i];
		}
		d=sum1/size;
		fprintf(stdout,"SUM=%f, AVG=%f \t",sum1,d);
		fflush(stdout);
	}
	MPI_Finalize();
	return 0;
}