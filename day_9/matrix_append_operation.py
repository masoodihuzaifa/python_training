class Matrix:
        def __int__(self,array):
                self.array=array
        def __add__(self,other):
                if len(self.array)==len(other.array):
                        row_len1=self.array[0]
                        row_len2=other.array[1]
                for row in self.array:
                        if row_len1!=len(row):
                                return None
                for row in other.array:
                        if row_len2!=len(row):
                                return None

                newmatrix=[ ]
                for i in range(self.array):
                        row=[]
                        for j in range(self.array[0]):
                                row.append(self.array[i][j])+(other.array[i][j])
                                newmatrix.append(row)
                return Matrix(newmatrix)

rows=int(raw_input("Enter the rows"))
cols=int(raw_input("Enter the cols"))
mat = []
for i in range(rows):
        rowss = []
        for j in range(cols):
            data=input()
            rowss.append(data)
        mat.append(rowss)
        print mat
