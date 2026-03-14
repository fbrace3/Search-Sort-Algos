# floyds
from random import randint as ri
INF = float('inf')

def floyds(W):
    dist = [row[:] for row in W]
    for k in range(len(dist)):
        for i in range(len(dist)):
            for j in range(len(dist)):
                dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])


    return dist

def printAdjMat(mat, width=3):
    res_str = '    ' + ''.join([str(v).rjust(width,' ') for v in range(len(mat))]) + '\n'
    res_str += ' ' + '-' * ((width + 1) * len(mat)) + '\n'
    for i, row in enumerate(mat):
        row_str = [str(elem).rjust(width, ' ') if elem < INF else '999' for elem in row]
        res_str += '' + str(i).rjust(2, ' ') + ' |' + ''.join(row_str) + "\n"
    print(res_str)

def main():

    k = input("Enter the size of the array (integer): ")
    k = int(k)

    mat = [[] for _ in range(k)]
    for y in range(len(mat)):
        for x in range(len(mat)):
            if x == y:
                mat[x].append(0)
            else:
                mat[x].append(ri(0, 100))

    
    
    
    printAdjMat(mat, k)
    z = floyds(mat)
    printAdjMat(z, k)

if __name__ == "__main__":
    main()
