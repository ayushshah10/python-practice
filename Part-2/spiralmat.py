def spiral(l1):
    ans = []

    while l1:
        ans.extend(l1.pop(0))

        if l1 and l1[0]:
            for i in l1:
                ans.extend(l1.pop())
        
        if l1:
            for i in l1[::-1]:
                ans.extend(l1.pop(0))
    return ans

l1 = [[1,2,4],[3,4,5],[6,7,5]]
# print(spiral(l1))



def print_spiral(matrix):
    while matrix:
        print(matrix.pop(0), end=" ")

        if matrix and matrix[0]:
            for row in matrix:
                print(row.pop(), end=" ")

        if matrix:
            print(matrix.pop()[::-1], end=" ")

        if matrix and matrix[0]:
            for row in matrix[::-1]:
                print(row.pop(0), end=" ")

print_spiral(l1)