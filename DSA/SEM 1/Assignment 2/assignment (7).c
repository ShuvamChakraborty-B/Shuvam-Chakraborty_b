/*7. Write a program to allocate memory using calloc( ) and then reallocate the previously
allocated memory using realloc( ). Display the elements which have been taken after
reallocation.*/
#include <stdio.h>
#include <stdlib.h>
int main()
{
    int is, fs, *ptr;
    printf("Enter the size of the array: ");
    scanf("%d", &is);
    ptr = (int *)calloc(is ,(sizeof(int)));

    for (int i = 0; i < is; i++)
    { printf("Enter value for block %d: ",i);
      scanf("%d",&ptr[i]);
    }

     for (int i = 0; i < is; i++)
    { printf("The value for block %d: %d \n",i,ptr[i]);
      
    }

    printf("Enter the value for reallocation:");
    scanf("%d",&fs);
    ptr=(int*)realloc(ptr,fs*sizeof(int));
    printf("Enter the value of next %d elements \n",fs-is);
    for(int i=is;i<fs;i++)
         { printf("Enter the  value for block %d: ",i);
           scanf("%d",&ptr[i]);
    }
    
    printf("All the elements are: \n");
     for (int i = 0; i < fs; i++)
    { printf("The value for block %d: %d \n",i,ptr[i]);
      
    }
    return 0;

}