#include<stdio.h>
#include<stdlib.h>
int main()
{
    int i,j,n;
    printf("Enter how many number: ");
    scanf("%d",&n);
    int a[n];
    for ( i = 0; i < n; i++)
    {
        a[i]= rand()%100;
    }
    
    for ( i = 0; i < n; i++)
    {
        printf("%d\t",a[i]);
    }

  int temp;
    for(i=0; i<n; i++)
    {
        for(j=i+1; j<n; j++)
        {
            if(a[i]>a[j])
            {
                temp=a[i];
                a[i]=a[j];
                a[j]=temp;
            }
        }
    }
    printf("\n\nAfter Shorting Array: \n");
    for(i=0; i<n; i++)
    {
        printf(" %d\t",a[i]);
    }


    int key;
    printf("\nEnter which element you want? \n");
    scanf("%d",&key);
    int s=0,e=n-1;
    int m= (s+e)/2;
   while (s<=e)
   {
    m=(s+e)/2;
    if(a[m]==key)
    {
        printf("Item found at %d posision",m+1);
        break;
    }
    else if (a[m]<key)
    {
        s=m+1;
    }
    else
    {
        e=m-1;
    }
    
   }
   
   
}