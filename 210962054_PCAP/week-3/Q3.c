#include <stdio.h>
#include "mpi.h"
#include <string.h>
int main(int argc,char * argv[]){
	int rank,size,n,m,o,count=0,d[10],sum1=0,f;
	char b[10],c[10]="AEIOU";
	char a[10];
	o=strlen(c);
	MPI_Init(&argc,&argv);
	MPI_Comm_rank(MPI_COMM_WORLD,&rank);
	MPI_Comm_size(MPI_COMM_WORLD,&size);
	MPI_Status status;
	if(rank==0){
		n=size;
		for(int i=0;i<6;i++){
			scanf("%c",&a[i]);
		}
		m=strlen(a)/size;
		
		if(m%2==0){
		printf("READING DONE....\n");}
		else{
			return 0;
		}
	}

	MPI_Bcast(&m,1,MPI_INT,0,MPI_COMM_WORLD);
	MPI_Scatter(a,m,MPI_CHAR,b,m,MPI_CHAR,0,MPI_COMM_WORLD);
	for(int i=0; i<o; i++){
		for(int j=0;j<m;j++){
			if(a[j]==c[i]){
				count+=1;
			}
		}		
	}
	MPI_Gather(&count,1,MPI_INT,d,1,MPI_INT,0,MPI_COMM_WORLD);
	if(rank==0)
	{
		fprintf(stdout,"The Result gathered in the root \n");
		fflush(stdout);
		sum1=strlen(a);
		
		sum1=sum1-2;
		for(int i=0; i<n; i++)
		printf("%d \t",d[i]);
		for(int i=0; i<n; i++){
		sum1=sum1-d[i];
		}
		
		fprintf(stdout,"SUM=%d\t",sum1);
		fflush(stdout);
	}
	MPI_Finalize();
	return 0;
}
