#include<stdio.h>
#include<stdbool.h>
#include<stdlib.h>
#define N 200
#define LIM 0.5
#define e 8.854e-12
#define V 16800
#define dr LIM*2/N
int m2Dex(float m){
  printf("dex = %d",(int)((m + LIM)/dr));
  return ((int)(m+LIM)/dr);
}
int main(){
  double phimap[N][N][N];
  bool flagmap[N][N][N];
  for(int i = 0 ; i < N; i++) {
    for(int j = 0 ; j < N; j++) {
      for(int k = 0 ; k < N; k++) {
        //phimap[i][j][k] = 0;
        //flagmap[i][j][k] = false;
      }
    }
  }
  /**
  for(float z = -0.2;z<0.2;z = z + dr){
    for(float y = -0.2;y<0.2;y = y + dr){
      int xDex = m2Dex(0.2);
      int yDex = m2Dex(y);
      int zDex = m2Dex(z);
      phimap[xDex][yDex][zDex] = V/2;
      flagmap[xDex][yDex][zDex] = true;
      yDex = m2Dex(-0.2);
      phimap[xDex][yDex][zDex] = -V/2;
      flagmap[xDex][yDex][zDex] = true;
    }
  }

  int count = 0;
  double maxerr = 1;
  double conv = 10e-6;
  double curerr;
  double prev_phi;
  double tmp;
  double maxphi = 0;

  while(maxerr>conv){
    maxerr = 0;
    curerr = 0;
    count++;
    for(int i = 1;i<N-1;i++){
      for(int j = 1;j<N-1;j++){
        for(int k = 1;k<N-1;k++){
          if(flagmap[i][j][k]){
            continue;
          }
          prev_phi = phimap[i][j][k];
          tmp = 1/6*(phimap[i+1][j][k] + phimap[i-1][j][k] + phimap[i][j+1][k] + phimap[i][j-1][k] + phimap[i][j][k+1] + phimap[i][j][k-1]);
          if(maxphi<abs(tmp)){
            maxphi = abs(tmp);
          }
          phimap[i][j][k] = tmp;
          curerr = (abs(phimap[i][j][k] - prev_phi))/maxphi;
          if(maxerr < curerr){
            maxerr = curerr;
          }
        }
      }
    }
    if(count % 100 == 0){
      printf("count = %d",count);
    }
  }
  **/
  return 0;
}
