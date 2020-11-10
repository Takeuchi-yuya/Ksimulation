#include<stdio.h>
#include<stdbool.h>
#include<stdlib.h>
#include<math.h>
#define N 200
#define LIM 0.5
#define e 8.854e-12
#define V 16800
#define dr LIM*2.0/N
int m2Dex(float m){
  //printf("%lf\n dr = %lf\n",m+LIM,dr);
  float tmp1 = dr;
  float tmp2 = m+LIM;
  float tmp3 = tmp2/tmp1;
  //printf("1 = %lf\n 2  = %lf\n 3 = %lf\n",tmp1,tmp2,tmp3);
  //printf("int = %d\n",(int)round(tmp3));
  return ((int)round(tmp3));
}

double ***malloc_3dim_phimap(int n1, int n2, int n3) {
  int i, j;
  double ***array;
  array = (double ***)malloc(n1 * sizeof(double **));
  for (i = 0; i < n1; i++) {
    array[i] = (double **)malloc(n2 * sizeof(double *));
    for (j = 0; j < n2; j++)
      array[i][j] = (double*)malloc(n3 * sizeof(double));
  }
  return array;
}
bool ***malloc_3dim_flagmap(int n1, int n2, int n3) {
  int i, j;
  bool ***array;
  array = (bool ***)malloc(n1 * sizeof(bool **));
  for (i = 0; i < n1; i++) {
    array[i] = (bool **)malloc(n2 * sizeof(bool *));
    for (j = 0; j < n2; j++)
      array[i][j] = (bool*)malloc(n3 * sizeof(bool));
  }
  return array;
}
/* 3次元配列の開放 */
void free_3dim_array(void ***array, int n1, int n2, int n3) {
  int i, j;
  for (i = 0; i < n1; i++) {
    for (j = 0; j < n2; j++)
      free(array[i][j]);
    free(array[i]);
  }
  free(array);
}

void print_3dim_array(double ***array, int n1, int n2, int n3) {
  int i, j, k;
  for (i = 1; i < n1-1; i++) {
    for (j = 1; j < n2-1; j++) {
      for (k = 1; k < n3-1; k++)
        printf("%lf ", array[i][j][k]);
      printf("\n");
    }
    printf("\n");
  }
}



int main(){
  printf("start\n");
  double ***phimap = malloc_3dim_phimap(N, N, N);
  bool ***flagmap = malloc_3dim_flagmap(N, N, N);
  for(int i = 0 ; i < N; i++) {
    for(int j = 0 ; j < N; j++) {
      for(int k = 0 ; k < N; k++) {
        phimap[i][j][k] = 0;
        flagmap[i][j][k] = false;
      }
    }
  }
  for(float z = -0.2;z<0.2;z = z + dr){
    for(float y = -0.2;y<0.2;y = y + dr){
      int xDex = m2Dex(0.2);
      int yDex = m2Dex(y);
      int zDex = m2Dex(z);
      //printf("%d %d %d \n",xDex,yDex,zDex);
      phimap[xDex][yDex][zDex] = V;
      flagmap[xDex][yDex][zDex] = true;
      yDex = m2Dex(-0.2);
      phimap[xDex][yDex][zDex] = 0;
      flagmap[xDex][yDex][zDex] = true;
    }
  }
  //print_3dim_array(phimap,N,N,N);
  int count = 0;
  double maxerr = 1;
  double conv = 10e-6;
  double curerr;
  double prev_phi;
  double tmp;
  double maxphi = 1;
  printf("loop start\n conv = %lf\nmaxerr = %lf\n",conv,maxerr);
  while(maxerr>conv){
    //printf("test\n");
    maxerr = 0;
    curerr = 0;
    count++;
    for(int i = 1;i<N-1;i++){
      for(int j = 1;j<N-1;j++){
        for(int k = 1;k<N-1;k++){
          //print_3dim_array(phimap,N,N,N);
          if(flagmap[i][j][k]){
            continue;
          }
          prev_phi = phimap[i][j][k];
          tmp = (phimap[i+1][j][k] + phimap[i-1][j][k] + phimap[i][j+1][k] + phimap[i][j-1][k] + phimap[i][j][k+1] + phimap[i][j][k-1])/6;
          //printf("tmp = %lf\n",tmp);
          if(maxphi<abs(tmp)){
            maxphi = abs(tmp);
          }
          phimap[i][j][k] = tmp;
          curerr = (abs(phimap[i][j][k] - prev_phi))/maxphi;
          //printf("curerr = %lf\n phimap = %lf\n prev_phi = %lf\n maxphi  = %lf\n",curerr,phimap[i][j][k],prev_phi,maxphi);
          if(maxerr < curerr){
            maxerr = curerr;
          }
        }
      }
    }
    //printf("maxerr = %lf\nconv = %lf\n",maxerr,conv);
    if(count % 100 == 0){
      printf("count = %d\n maxerr = %lf\n",count,maxerr);
    }
  }
  printf("%d\n",count);
  free_3dim_array((void***)phimap, N, N, N);
  free_3dim_array((void***)flagmap, N, N, N);

  printf("end\n");

  return 0;
}
