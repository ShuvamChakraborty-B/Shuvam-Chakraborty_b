#include <stdio.h>

// Function to swap two elements
void swap(int *a, int *b) {
    int temp = *a;
    *a = *b;
    *b = temp;
}

// Function to partition the array and return the pivot index
int partition(int arr[], int low, int high) {
    int pivot = arr[high];
    int i = low - 1;

    for (int j = low; j < high; j++) {
        if (arr[j] <= pivot) {
            i++;
            swap(&arr[i], &arr[j]);
        }
    }

    swap(&arr[i + 1], &arr[high]);
    return i + 1;
}

// Function to perform the Quick Sort algorithm
void quickSort(int arr[], int low, int high) {
    if (low < high) {
        // Find the pivot index such that elements smaller than the pivot are on the left, and larger are on the right
        int pivotIndex = partition(arr, low, high);

        // Recursively sort the sub-arrays
        quickSort(arr, low, pivotIndex - 1);
        quickSort(arr, pivotIndex + 1, high);

        // Print the array after each iteration
        printf("Iteration: ");
        for (int i = low; i <= high; i++) {
            printf("%d ", arr[i]);
        }
        printf("\n");
    }
}

int main() {
    int arr[] = {27, 15, 39, 21, 28, 70};
    int n = sizeof(arr) / sizeof(arr[0]);

    printf("Original Array: ");
    for (int i = 0; i < n; i++) {
        printf("%d ", arr[i]);
    }
    printf("\n\n");

    // Call the Quick Sort function
    quickSort(arr, 0, n - 1);

    printf("\nSorted Array: ");
    for (int i = 0; i < n; i++) {
        printf("%d ", arr[i]);
    }

    return 0;
}
