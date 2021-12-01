def get_column(matrix, indx):
	column = []
	for row in matrix:
		column.append(row[indx])
	return column


def space_number(column):
	return len(str(max(column)))



def print_matrix(matrix):
	for row in matrix:
		indx = 0
		row_str = ""
		for el in row:
			nspace = space_number(get_column(matrix, indx))
			row_str += str(el).rjust(nspace) + " "
			indx += 1

		print(row_str)	


a = [[1,11,111,7],[111111111111,4,6,11111]]
print_matrix(a)				


