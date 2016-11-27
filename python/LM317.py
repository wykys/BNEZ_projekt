# wykys 2016
# program pro vypocty hodnot delice R1 R2 pro LM317


def UpravNaRadu(Ex, R2):	
	delta = abs(Ex[0] - R2)
	R_ok = Ex[0]

	for i in Ex:
		if abs(i - R2) < delta:
			delta = abs(i - R2)
			R_ok = i
		if abs(i/10 - R2) < delta:
			delta = abs(i/10 - R2)
			R_ok = i/10
		if abs(i/100 - R2) < delta:
			delta = abs(i/100 - R2)
			R_ok = i/100
		if abs(i*10 - R2) < delta:
			delta = abs(i*10 - R2)
			R_ok = i*10
		if abs(i*100 - R2) < delta:
			delta = abs(i*100 - R2)
			R_ok = i*100
	return R_ok

def SpoctiR2(Vo, R1):
	Vr = 1.25
	Iadj = 50e-6
	R1 = float(R1)
	return (Vo - Vr)/(Vr/R1 + Iadj)

def OverVo(R1, R2):
	Vr = 1.25
	Iadj = 50e-6
	R1 = float(R1)
	R2 = float(R2)
	return Vr*(1+R2/R1) + Iadj*R2

def SpoctiStabik(Vo, EXX):
	delta = abs(Vo)
	R1_ok = 1
	R2_ok = 1
	U2_ok = 1

	for R1 in EXX:
		R2 = SpoctiR2(Vo, R1)
		R2 = UpravNaRadu(EXX, R2)
		U2 = OverVo(R1, R2)
		if abs(Vo - U2) < delta:
			delta = abs(Vo - U2)
			R1_ok = R1
			R2_ok = R2
			U2_ok = U2
	
	print "R1 = {} \tR2 = {} \t U2 = {:.4f}".format(R1_ok, R2_ok, U2_ok)

E3 = (100, 220, 470)
E6 = (100, 150, 220, 330, 470, 680)
E12 = (100, 120, 150, 180, 220, 270, 330, 390, 470, 560, 680, 820)
E24 = (100, 110, 120, 130, 150, 160, 180, 200, 220, 240, 270, 300, 330, 360, 390, 430, 470, 510, 560, 620, 680, 750, 820, 910)
E48 = (100, 102, 110, 115, 121, 127, 133, 140, 147, 154, 162, 169, 187, 196, 205, 215, 226, 237, 243, 249, 261, 274, 287, 301, 316, 332, 348, 365, 383, 402, 422, 442, 464, 487, 511, 536, 562, 590, 619, 649, 681, 715, 750, 787, 825, 866, 909, 953)
E96 = (100, 102, 105, 107, 110, 113, 115, 118, 121, 124, 127, 130, 133, 137, 140, 143, 147, 150, 154, 158, 162, 165, 169, 174, 178, 182, 187, 191, 196, 200, 205, 210, 215, 221, 226, 232, 237, 243, 249, 255, 261, 267, 274, 280, 287, 294, 301, 309, 316, 324, 332, 340, 348, 357, 365, 374, 383, 392, 402, 412, 422, 432, 442, 453, 464, 475, 487, 499, 511, 523, 536, 549, 562, 576, 590, 604, 619, 634, 649, 665, 681, 698, 715, 732, 750, 768, 787, 806, 825, 845, 866, 887, 909, 931, 953, 976)
E192 = (100, 101, 102, 104, 105, 106, 107, 109, 110, 111, 113, 114, 115, 117, 118, 120, 121, 123, 124, 126, 127, 129, 130, 132, 133, 135, 137, 138, 140, 142, 143, 145, 147, 149, 150, 152, 154, 156, 158, 160, 162, 164, 165, 167, 169, 172, 174, 176, 178, 180, 182, 184, 187, 189, 191, 193, 196, 198, 200, 203, 205, 208, 210, 213, 215, 218, 221, 223, 226, 229, 232, 234, 237, 240, 243, 246, 249, 252, 255, 258, 261, 264, 267, 271, 274, 277, 280, 284, 287, 291, 294, 298, 301, 305, 309, 312, 316, 320, 324, 328, 332, 336, 340, 344, 348, 352, 357, 361, 365, 370, 374, 379, 383, 388, 392, 397, 402, 407, 412, 417, 422, 427, 432, 437, 442, 448, 453, 459, 464, 470, 475, 481, 487, 493, 499, 505, 511, 517, 523, 530, 536, 542, 549, 556, 562, 569, 576, 583, 590, 597, 604, 612, 619, 626, 634, 642, 649, 657, 665, 673, 681, 690, 698, 706, 715, 723, 732, 741, 750, 759, 768, 777, 787, 796, 806, 816, 825, 835, 845, 856, 866, 876, 887, 898, 909, 919, 931, 942, 953, 965, 976, 988)

Vo = 4.5
EXX = E3

print "E3 ====================================================================="
SpoctiStabik(Vo, E3)
print "E6 ====================================================================="
SpoctiStabik(Vo, E6)
print "E12 ===================================================================="
SpoctiStabik(Vo, E12)
print "E24 ===================================================================="
SpoctiStabik(Vo, E24)
print "E48 ===================================================================="
SpoctiStabik(Vo, E48)
print "E96 ===================================================================="
SpoctiStabik(Vo, E96)
print "E192 ==================================================================="
SpoctiStabik(Vo, E192)

