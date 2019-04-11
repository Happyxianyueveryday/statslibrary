import numpy as np

def LoadFile(filename):		#load input file containing training data
	lines = open(filename, "rb")
	dataset =[]
	for line in lines:
		line = line.strip().split(',')
		dataset.append(line)
	dataset = np.array(dataset).astype(np.float64)
	return dataset

def ByClass(dataset):		#separate data by class
	classes = np.unique(dataset[:,-1])
	div_class = {}
	for i in classes:
		div_class[i] = dataset[dataset[:,-1] == i]
	return div_class

def Mean(data):
	mean = data.mean(axis = 0)
	return mean

def Tresh(vector, data1, data2):
	mu1 = Mean(np.dot(vector, data1.T))
	mu2 = Mean(np.dot(vector, data2.T))
	return (mu1+mu2)/2, mu1, mu2
	

def main(dataset):		#assuming given two class problem
	div_data = ByClass(dataset)
	class1, class2 = div_data
	class1_data, class2_data = div_data[class1], div_data[class2] 
	class1_data = class1_data[:,:-1]
	class2_data = class2_data[:,:-1]
	mean1 = Mean(class1_data)
	mean2 = Mean(class2_data)
	mean = Mean(dataset[:,:-1])
	mean1, mean2, mean = mean1.T, mean2.T, mean.T
	
	
	m,n = class1_data.shape
	diff1 = class1_data - np.array(list(mean1)*m).reshape(m,n)
	m,n = class2_data.shape
	diff2 = class2_data - np.array(list(mean2)*m).reshape(m,n)
	diff = np.concatenate([diff1, diff2])
	m, n = diff.shape
	withinClass = np.zeros((n,n))
	diff = np.matrix(diff)
	for i in xrange(m):
		withinClass += np.dot(diff[i,:].T, diff[i,:])
	opt_dir_vector = np.dot(np.linalg.inv(withinClass), (mean1 - mean2))
	print 'Vector = ', np.matrix(opt_dir_vector).T
	
	threshold, mu1, mu2 = Tresh(opt_dir_vector, class1_data, class2_data)
	print 'Threshold = ', threshold, 'm1 = ', mu1, 'm2 = ', mu2
	
	
if __name__ == '__main__':	
	filename = 'data.txt'
	dataset = LoadFile(filename)
	main(dataset)
