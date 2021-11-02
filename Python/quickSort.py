class QuickSort:
    

    def haorePartition(self, arr, start, end):
        pIndex = start
        pivot = arr[pIndex]
        while start < end:
            while start < len(arr) and arr[start] <= pivot:
                start +=1
            while arr[end] > pivot:
                end -= 1
            if start < end :
                arr[start], arr[end] = arr[end], arr[start]
        arr[pIndex], arr[end] = arr[end], arr[pIndex]
        return end

    def lumatoPartition(self,arr,start,end):
        pIndex = start
        pivot = arr[end]
        for i in range(start,end):
            if arr[i] <= pivot:
                pIndex += 1
                arr[i], arr[pIndex] and arr[pIndex], arr[i]
            arr[pIndex], arr[end], arr[end], arr[pIndex]
        return pIndex

    def quick_sort(self,elements, start, end):
        if len(elements)== 1:
            return
        if start < end:
            pi = self.lumatoPartition(elements, start, end)
            self.quick_sort(elements, start, pi-1)
            self.quick_sort(elements, pi+1, end)

if __name__ == '__main__':
    tests = [
            [11,9,29,7,2,15,28],
            [3, 7, 9, 11],
            [25, 22, 21, 10],
            [29, 15, 28],
            [],
            [6]
        ]
        # elements = ["mona", "dhaval", "aamir", "tina", "chang"]
    ob = QuickSort()
    for elements in tests:
        ob.quick_sort(elements, 0, len(elements)-1)
        print(f'sorted array: {elements}')