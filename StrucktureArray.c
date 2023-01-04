#include<stdio.h>
struct StrucktureArray
{
   int age;
   float salary;
};

int main()
{
    struct  StrucktureArray person[4];
   int i;
   for ( i = 0; i < 4; i++)
   {
    printf("Enter information for person %d\n",i+1);
    printf("Enter age: ");
    scanf("%d",&person[i].age);
    printf("Enter salary: ");
    scanf("%f",&person[i].salary);
   }
   
    for ( i = 0; i < 4; i++)
    {
      printf("\n\nInformation for person %d",i+1);
      printf("\nAge: %d",person[i].age);
      printf("\nSalary: %f",person[i].salary);
    }
    
}