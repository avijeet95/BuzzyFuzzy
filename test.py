# Converting to fuzzy sets

import numpy as np


def mem1(x,hb,lb):
	return float((hb-x) / (hb-lb))

def mem2(x,hb,lb):
	return float((x-lb) / (hb-lb))


def runApriori():
	itemSet = set()

def preprocess():
	fname = 'iris.csv'

	data = np.genfromtxt(fname,delimiter=',')

	data = data[1:]

	attribute =[]

	attribute.append(data[:,1])
	attribute.append(data[:,2])
	attribute.append(data[:,3])
	attribute.append(data[:,4])


	dev = []

	dev.append(np.std(attribute[0]))
	dev.append(np.std(attribute[1]))
	dev.append(np.std(attribute[2]))
	dev.append(np.std(attribute[3]))
	for x in dev:
		print x

	mean = []

	mean.append(np.mean(attribute[0]))
	mean.append(np.mean(attribute[1]))
	mean.append(np.mean(attribute[2]))
	mean.append(np.mean(attribute[3]))
	for x in mean:
		print x

	#fow low set

	low_lb = []
	low_lb.append(np.amin(attribute[0]))
	low_lb.append(np.amin(attribute[1]))
	low_lb.append(np.amin(attribute[2]))
	low_lb.append(np.amin(attribute[3]))

	low_hb = []

	low_hb.append(mean[0] - (dev[0]/2) + (mean[0] * 0.1))
	low_hb.append(mean[1] - (dev[1]/2) + (mean[1] * 0.1))
	low_hb.append(mean[2] - (dev[2]/2) + (mean[2] * 0.1))
	low_hb.append(mean[3] - (dev[3]/2) + (mean[3] * 0.1))

	# for medium set

	med_lb = []
	med_lb.append(mean[0] - (dev[0]/2) - (mean[0] * 0.1))
	med_lb.append(mean[1] - (dev[1]/2) - (mean[1] * 0.1))
	med_lb.append(mean[2] - (dev[2]/2) - (mean[2] * 0.1))
	med_lb.append(mean[3] - (dev[3]/2) - (mean[3] * 0.1))


	med_hb = []
	med_hb.append(mean[0] + (dev[0]/2) + (mean[0] * 0.1))
	med_hb.append(mean[1] + (dev[1]/2) + (mean[1] * 0.1))
	med_hb.append(mean[2] + (dev[2]/2) + (mean[2] * 0.1))
	med_hb.append(mean[3] + (dev[3]/2) + (mean[3] * 0.1))

	# for high set

	high_lb = []
	high_lb.append((mean[0] + (dev[0]/2)) - (mean[0] * 0.1))
	high_lb.append((mean[1] + (dev[1]/2)) - (mean[1] * 0.1))
	high_lb.append((mean[2] + (dev[2]/2)) - (mean[2] * 0.1))
	high_lb.append((mean[3] + (dev[3]/2)) - (mean[3] * 0.1))

	high_hb = []
	high_hb.append(np.amax(attribute[0]))
	high_hb.append(np.amax(attribute[1]))
	high_hb.append(np.amax(attribute[2]))
	high_hb.append(np.amax(attribute[3]))

	#For Attribute 0

	a0_low = []
	a0_med = []
	a0_high = []

	for x in attribute[0]:
		if x >= low_lb[0] and x < med_lb[0]:
			a0_low.append(1)
			a0_med.append(0)
			a0_high.append(0)
		elif x >= med_lb[0] and x <= low_hb[0]:
			a0_low.append(mem1(x,low_hb[0], med_lb[0]))
			a0_med.append(mem2(x,low_hb[0], med_lb[0]))
			a0_high.append(0)
		elif x >low_hb[0] and x < high_lb[0]:
			a0_low.append(0)
			a0_med.append(1)
			a0_high.append(0)
		elif x <= med_hb[0] and x >= high_lb[0]:
			a0_low.append(0)
			a0_med.append(mem1(x,med_hb[0], high_lb[0]))
			a0_high.append(mem2(x,med_hb[0], high_lb[0]))
		else :
			a0_low.append(0)
			a0_med.append(0)
			a0_high.append(1)

	# print len(a0_high)