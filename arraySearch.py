class arraySearch:
    def search(self, arr, x):
        for i in range(0, arr):
            if arr[i] == x:
                return i
        return -1