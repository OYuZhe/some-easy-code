


#Euclidean algorithm
def HCF(HCFfirNum,HCFsecNum):

	hcf=0
	while HCFfirNum != 0 and HCFsecNum != 0:
		if HCFfirNum >= HCFsecNum:
			HCFfirNum = HCFfirNum % HCFsecNum
		else:
			HCFsecNum = HCFsecNum % HCFfirNum
			
	if HCFfirNum > HCFsecNum:
		hcf = HCFfirNum
	else:
		hcf = HCFsecNum
	return hcf

#computer least common multiple
def LCM(LCMfirNum,LCMsecNum,HCF):

	LCMfirNum = LCMfirNum // HCF
	LCMsecNum = LCMsecNum // HCF
	LCM = HCF * LCMfirNum * LCMsecNum
	return LCM



if __name__ == '__main__':
	firNum = eval(input("input first number:"))
	secNum = eval(input("input second number:"))
	hcf = HCF(firNum,secNum)
	lcm = LCM(firNum,secNum,hcf)
	print("highest common factor:",hcf)
	print("least common multiple:",lcm)