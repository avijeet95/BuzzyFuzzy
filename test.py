# Converting to fuzzy sets

import numpy as np


def mem1(x,hb,lb):
	return float((hb-x) / (hb-lb))

def mem2(x,hb,lb):
	return float((x-lb) / (hb-lb))

def preprocess(num):
	fname = 'iris.csv'

	data = np.genfromtxt(fname,delimiter=',')

	data = data[1:]  #if there is heading


	attribute =[]

	for i in range(1,num): 
		attribute.append(data[:,i])


	dev =[]  #calulate standard deviation

	for i in range(0,len(attribute)):
		dev.append(np.std(attribute[i]))

	# print dev
	mean = [] #calculate mean
	for i in range(0,len(attribute)):
		mean.append(np.mean(attribute[i]))

	# print mean
	
	#for low set

	low_lb = []
	for i in range(0,len(attribute)):
		low_lb.append(np.amin(attribute[i]))

	# print low_lb

	low_hb = []
	for i in range(0,len(attribute)):
		low_hb.append(mean[i] - (dev[i]/2) + (mean[i] * 0.05))

	# print low_hb
	# for medium set

	med_lb = []
	for i in range(0,len(attribute)):
		med_lb.append(mean[i] - (dev[i]/2) - (mean[i] * 0.05))

	med_hb = []
	for i in range(0,len(attribute)):
		med_hb.append(mean[i] + (dev[i]/2) + (mean[i] * 0.05))

	# for high set

	high_lb = []
	for i in range(0,len(attribute)): 
		high_lb.append((mean[i] + (dev[i]/2)) - (mean[i] * 0.05))

	high_hb = []
	for i in range(0,len(attribute)):
		high_hb.append(np.amax(attribute[i]))

	#For Attribute 0
	low = []
	med = []
	high = [] 
	for i in range(0,len(attribute)):  
		ai_low = []
		ai_med = []
		ai_high = []  
		for x in attribute[i]:
			if x >= low_lb[i] and x < med_lb[i]:
				ai_low.append(1)
				ai_med.append(0)
				ai_high.append(0)
			elif x >= med_lb[i] and x <= low_hb[i]:
				ai_low.append(mem1(x,low_hb[i], med_lb[i]))
				ai_med.append(mem2(x,low_hb[i], med_lb[i]))
				ai_high.append(0)
			elif x >low_hb[i] and x < high_lb[i]:
				ai_low.append(0)
				ai_med.append(1)
				ai_high.append(0)
			elif x <= med_hb[i] and x >= high_lb[i]:
				ai_low.append(0)
				ai_med.append(mem1(x,med_hb[i], high_lb[i]))
				ai_high.append(mem2(x,med_hb[i], high_lb[i]))
			else :
				ai_low.append(0)
				ai_med.append(0)
				ai_high.append(1)
		low.append(ai_low)
		med.append(ai_med)
		high.append(ai_high)


	attribute = []  # Final attribute matrix

	for i in range(0,len(low)):
		attribute.append(low[i])
		attribute.append(med[i])
		attribute.append(high[i])

	attribute=np.array(attribute)
	attribute=attribute.transpose()
	print attribute
	np.savetxt("foo.csv", attribute, delimiter=",")
	
if __name__ == "__main__":
	num=5
	preprocess(num)
