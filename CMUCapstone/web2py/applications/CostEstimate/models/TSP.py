from numpy import matrix
import random


class TSP(object):

    def __init__(self, node_matrix):
        self.node_matrix = node_matrix
        self.tsp_solution = None

    def solve(self):
        matrix = self.node_matrix
        # Uncomment the row below for unit testing
        # matrix = [[0, 1.7, 1.7, 1.7, 2.0],[2.1, 0, 1.7, 1.8, 1.3],[2.6, 2.2, 0, 2.0, 1.7],[1.2, 1.5, 2.1, 0, 2.4],[1.9, 2.1, 1.8, 2.3, 0]]

        tour = [0]
        rowNum = 0
        while(len(tour) < len(matrix)):
            min_val = 10000
            for col in range(0, len(matrix)):
                if matrix[rowNum][col] == 0:
                    continue
                elif (col in tour) == True:
                    continue
                else:
                    min_val = min(min_val, matrix[rowNum][col])

            temp = []
            for i in range(0, len(matrix)):
                if matrix[rowNum][i] == min_val:
                    if (i in tour) == False:
                        temp.append(i)
            rowNum = random.choice(temp)
            tour.append(rowNum)

        tour.append(0)
        for num in range(0, len(tour)):
            tour[num] = tour[num]+1

        print "This is the tour:"
        print tour

