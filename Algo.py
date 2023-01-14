from tkinter import *
from ttkbootstrap import *
from tkinter import ttk


class Algo:
    def __init__(self, root, title):
        self.root = root
        self.root.title(title)
        self.root.resizable(width=False, height=False)
        Label(self.root, text='Sorting Algorithm',font=('Times', 30)).grid(row=0, columnspan=6)
        #  Buttons
        self.bs = ttk.Button(self.root, text='Bubble Sort',style='info.TButton', padding=5, width=15,command=self.bubble_sort)
        self.bs.grid(column=0, row=1, padx=5, pady=5)
        self.Is = ttk.Button(self.root, text='Insertion Sort', style='info.TButton', padding=5, width=15,command=self.insertion_sort)
        self.Is.grid(column=1, row=1, padx=5, pady=5)
        self.ss = ttk.Button(self.root, text='Selection Sort', style='info.TButton', padding=5, width=15,command=self.selection_sort)
        self.ss.grid(column=2, row=1, padx=5, pady=5)
        self.ms = ttk.Button(self.root, text='Merge Sort', style='info.TButton', padding=5, width=15,command=self.merge_sort)
        self.ms.grid(column=3, row=1, padx=5, pady=5)
        self.qs = ttk.Button(self.root, text='Quick Sort', style='info.TButton', padding=5, width=15,command=self.quick_sort)
        self.qs.grid(column=4, row=1, padx=5, pady=5)

        #=====TextBox=======
        self.text_box = Text(self.root,height=25,width=90)
        self.text_box.grid(column=0,row=3,columnspan=5)
        self.text_box.config(state="normal",background="black", foreground="orange",font=('Times', 14))

    def bubble_sort(self):
        bubble_sort_code='''
        def bubbleSort(arr):
            n = len(arr)
 
            # Traverse through all array elements
            for i in range(n):
         
                # Last i elements are already in place
                for j in range(0, n-i-1):
         
                    # traverse the array from 0 to n-i-1
                    # Swap if the element found is greater
                    # than the next element
                    if arr[j] > arr[j+1]:
                        arr[j], arr[j+1] = arr[j+1], arr[j]
 
        if __name__ == "__main__":
            arr = [5, 1, 4, 2, 8]
            bubbleSort(arr)
        '''
        self.text_box.delete("1.0", "end")
        self.text_box.insert('end',bubble_sort_code)
    def insertion_sort(self):
        insertion_sort_code='''
            def insertionSort(arr):
                # Traverse through 1 to len(arr)
                for i in range(1, len(arr)):
             
                    key = arr[i]
             
                    # Move elements of arr[0..i-1], that are
                    # greater than key, to one position ahead
                    # of their current position
                    j = i-1
                    while j >= 0 and key < arr[j] :
                            arr[j + 1] = arr[j]
                            j -= 1
                    arr[j + 1] = key
             
             
            # Driver code to test above
            arr = [12, 11, 13, 5, 6]
            insertionSort(arr)
        '''
        self.text_box.delete("1.0", "end")
        self.text_box.insert("end",insertion_sort_code)

    def selection_sort(self):
        selection_sort_code='''
        def selectionSort():      
            A = [64, 25, 12, 22, 11]
            
            # Traverse through all array elements
            for i in range(len(A)):
                
                # Find the minimum element in remaining
                # unsorted array
                min_idx = i
                for j in range(i+1, len(A)):
                    if A[min_idx] > A[j]:
                        min_idx = j
                        
                # Swap the found minimum element with
                # the first element	
                A[i], A[min_idx] = A[min_idx], A[i]

            selectionSort()

        '''
        self.text_box.delete("1.0", "end")
        self.text_box.insert("end", selection_sort_code)
    def merge_sort(self):
        merge_sort_code='''
        def mergeSort(arr):
                if len(arr) > 1:
            
                    # Finding the mid of the array
                    mid = len(arr)//2
            
                    # Dividing the array elements
                    L = arr[:mid]
            
                    # into 2 halves
                    R = arr[mid:]
            
                    # Sorting the first half
                    mergeSort(L)
            
                    # Sorting the second half
                    mergeSort(R)
            
                    i = j = k = 0
            
                    # Copy data to temp arrays L[] and R[]
                    while i < len(L) and j < len(R):
                        if L[i] <= R[j]:
                            arr[k] = L[i]
                            i += 1
                        else:
                            arr[k] = R[j]
                            j += 1
                        k += 1
            
                    # Checking if any element was left
                    while i < len(L):
                        arr[k] = L[i]
                        i += 1
                        k += 1
            
                    while j < len(R):
                        arr[k] = R[j]
                        j += 1
                        k += 1
    
            # Driver Code
            if __name__ == '__main__':
                mergeSort(arr)

        '''
        self.text_box.delete("1.0", "end")
        self.text_box.insert("end", merge_sort_code)
    def quick_sort(self):
        quick_sort_code='''
            def partition(array, low, high):
            
                # Choose the rightmost element as pivot
                pivot = array[high]
            
                # Pointer for greater element
                i = low - 1
            
                # Traverse through all elements
                # compare each element with pivot
                for j in range(low, high):
                    if array[j] <= pivot:
                        # If element smaller than pivot is found
                        # swap it with the greater element pointed by i
                        i = i + 1
            
                        # Swapping element at i with element at j
                        (array[i], array[j]) = (array[j], array[i])
            
                # Swap the pivot element with
                # e greater element specified by i
                (array[i + 1], array[high]) = (array[high], array[i + 1])
            
                # Return the position from where partition is done
                return i + 1
            
            # Function to perform quicksort
            
            
            def quick_sort(array, low, high):
                if low < high:
            
                    # Find pivot element such that
                    # element smaller than pivot are on the left
                    # element greater than pivot are on the right
                    pi = partition(array, low, high)
            
                    # Recursive call on the left of pivot
                    quick_sort(array, low, pi - 1)
            
                    # Recursive call on the right of pivot
                    quick_sort(array, pi + 1, high)
            
            
            # Driver code
            array = [10, 7, 8, 9, 1, 5]
            quick_sort(array, 0, len(array) - 1)

        '''
        self.text_box.delete("1.0", "end")
        self.text_box.insert("end", quick_sort_code)

if __name__ == '__main__':
    win = Style(theme='darkly').master
    obj = Algo(win, 'Algo')
    win.mainloop()