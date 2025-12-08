class SortingAlgo:
    def __init__(self,set):
        self.set=set
    def bubblesort(self):
        n =len(self.set)
        for i in range(n-1):
            for j in range(n-1,i,-1):
                if self.set[j]<self.set[j-1]:
                    self.set[j],self.set[j-1]=self.set[j-1],self.set[j]
        return self.set


example = [2, 6, 3, 8, 2, 9, 2, 10, 3, 22, -1]
ins1 = SortingAlgo(example)
print(ins1.bubblesort())
