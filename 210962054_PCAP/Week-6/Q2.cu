#include "cuda_runtime.h"
#include "device_launch_parameters.h"
#include <stdio.h>
#include <stdlib.h>
#include<string.h>

#define N 1024
__global__ void CUDACount(char *A,char* B,int n, int d_count){
int i = threadIdx.x;
int o=n-i;
int start = d_count - (o * (o + 1)) / 2;
     for(int j=0;j<o;j++){
     	B[start+j]=A[j];
     }
   
   }

int main() {
char A[N],B[N];
char *d_A,*d_B;


printf("Enter a string:");
scanf("%s",A);
int c= strlen(A)*(2+(strlen(A)-1))/2;
int size=c*sizeof(char);
cudaEvent_t start, stop;
cudaEventCreate(&start);
cudaEventCreate(&stop);
cudaEventRecord(start, 0);
cudaMalloc((void**)&d_A, strlen(A)*sizeof(char));

cudaMalloc((void**)&d_B, c*sizeof(char));

cudaMemcpy(d_A, A, strlen(A)*sizeof(char), cudaMemcpyHostToDevice);


cudaError_t error =cudaGetLastError();
if (error != cudaSuccess) {
printf("CUDA Error1: %s\n", cudaGetErrorString(error));
}

CUDACount<<<1, strlen(A)>>>(d_A, d_B, strlen(A), c);
error =cudaGetLastError();
if (error != cudaSuccess) {
printf("CUDA Error2: %s\n", cudaGetErrorString(error));
}
cudaEventRecord(stop, 0);
cudaEventSynchronize(stop);
float elapsedTime;
cudaEventElapsedTime(&elapsedTime, start, stop);
cudaMemcpy(B, d_B, size, cudaMemcpyDeviceToHost);
B[c] = '\0';
printf("string=%s",B);
cudaFree(d_A);

printf("\n");
return 0;
}