#include<stdio.h>
int main(){
  int arr[2][3],i,j;
  printf("enter the array value: \n");
  for ( i = 0; i <2; i++)
  {
    for ( j = 0; j < 3; j++)
    {
      printf("\nplease%dth row %dthcoloumn: ",i+1,j+1);
      scanf("%d",&arr[i][j]);
    }
    
  }
printf("\nthe number matrix is: ");
printf("\n");
  for ( i = 0; i <2; i++)
  {
    for ( j = 0; j < 3; j++)
    {
      printf("%d\t",arr[i][j]);
    }
    printf("\n");
    
  }
  
  return 0;
}