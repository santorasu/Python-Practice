#include<stdio.h>
#include<stdlib.h>
int main()
{
    int i,j,n;
    printf("How many number you want ");
    scanf("%d",&n);
    int a[n];
    for(i=0;i<n;i++)
    {
        a[i]=rand()%100;
    }

     for(i=0;i<n;i++)
    {
        printf("%d \t",a[i]);
    }
    printf("\nAfter sorting array \n");

    int temp;
    for(i=0;i<n;i++)
    {
        for(j=i+1;j<n;j++)
        {
            if(a[i]>a[j])
            {
                temp=a[i];
                a[i]=a[j];
                a[j]=temp;
            }
        }
    }
    for(i=0;i<n;i++)
    {
        printf("%d \t",a[i]);
    }
int key;
   printf("\nEnter which number you want: ");
   scanf("%d",&key);
   int s=0,e,m;
   e=n-1;
   m=(s+e)/2;
   while (s <= e)
 {
   if(a[m] < key)
   s = m + 1;
   else if (a[m] == key)
 {
   printf("Item found at location %d.\n", m+1);
   break;
 }
   else
   e = m - 1;
   m = (s + e)/2;
 }
   if(s > e)
   printf("Not found!\n");
 
    int location,insert;
    printf("\nEnter which location you want to insert\n");
    scanf("%d",&location);
    printf("\nWhich number want to insert\n");
    scanf("%d",&insert);
    for(i=n-1;i>=location;i--)
    {
        a[i+1]=a[i];
    }
    a[location-1]=insert;
    printf("\nInsertion Array\n");
    for(i=0;i<n+1;i++)
    {
        printf("%d\t",a[i]);
    }
    
}