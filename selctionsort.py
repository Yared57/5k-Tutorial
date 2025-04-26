class Solution: 
    def selectionSort(self, arr):
        for i in range(len(arr)):
            localmin = i
            for j in range(i + 1, len(arr)):
                if arr[j] <= arr[localmin]:
                    localmin = j
            arr[localmin], arr[i] = arr[i], arr[localmin]
        return arr
