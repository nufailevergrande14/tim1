#proses fuzzyfikasi :

x_asap1 = input ("masukan nilai asap1 =")
x_alkohol1 = input ("masukan nilai alkohol1 =")
x_gas1 = input ("masukan nilai gas1 = ")

asap = int (x_asap1)
alkohol = int (x_alkohol1)
gas = int (x_gas1)

#menghitung asap
if asap<= 30 :
    value_sedikitA = 1
    value_banyakA = 0
if asap > 30 and asap < 100 :
    value_sedikitA = (100- asap)/(100 - 30)
    value_banyakA = (asap - 30)/(100 - 30)
if asap >= 100 :
    value_sedikitA = 0
    value_banyakA= 1

print ('asap')
print ('asap', value_sedikitA)
print ('asap', value_banyakA)



#menghitung alkohol

if alkohol <= 50 :
    value_sedikitB = 1
    value_banyakB = 0
if asap > 50 and alkohol < 100 :
    value_sedikitB = (100- alkohol)/(100- 50)
    value_banyakB = (alkohol - 50)/(100 - 50)
if asap >= 100 :
    value_sedikitB = 0
    value_banyakB= 1


print ('alkohol')
print ('alkohol', value_sedikitB)
print ('alkohol', value_banyakB)



 #menghitung gas
if gas  <= 20 :
    value_sedikitC = 1
    value_banyakC = 0
if gas > 20 and gas < 100 :
    value_sedikitC = (20- gas)/(100 - 20)
    value_banyakC = (gas - 700)/(100 - 20)
if gas >= 100 :
    value_sedikitC = 0
    value_banyakC = 1

print ('gas')
print ('gas', value_sedikitC)
print ('gas', value_banyakC)


#proses inferensi 
#proses buzzer
speed=[]
def fungsiinferensiterbuka (variabel_asap, variabel_alkohol, variabel_gas) :
    if variabel_asap != 1:
        if variabel_alkohol != 1:
            if variabel_gas !=1:
                hasil_output = min (variabel_asap, variabel_alkohol , variabel_gas)
                speed.append([hasil_output, 100])

def fungsiinferensitertutup (variabel_asap, variabel_alkohol , variabel_gas) :
    if variabel_asap != 0:
        if variabel_alkohol != 0:
            if variabel_gas !=0:
                hasil_output = min (variabel_asap, variabel_alkohol, variabel_gas)
                speed.append([hasil_output, 10])
#proses led hijau
#speed=[]
def fungsiinferensiterbuka (variabel_asap, variabel_alkohol, variabel_gas) :
    if variabel_asap != 1:
        if variabel_alkohol != 0:
            if variabel_gas !=0:
                hasil_output = min (variabel_asap, variabel_alkohol, variabel_gas)
                speed.append([hasil_output, 30])

def fungsiinferensitertutup (variabel_asap, variabel_alkohol, variabel_gas) :
    if variabel_asap != 0:
        if variabel_alkohol != 0:
            if variabel_gas !=0:
                hasil_output = min (variabel_asap, variabel_alkohol, variabel_gas)
                speed.append([hasil_output, 10])
#proses led orange
#speed=[]
def fungsiinferensiterbuka (variabel_asap, variabel_alkohol, variabel_gas) :
    if variabel_asap != 1:
        if variabel_alkohol != 1:
            if variabel_gas !=0:
                hasil_output = min (variabel_asap, variabel_alkohol, variabel_gas)
                speed.append([hasil_output, 70])

def fungsiinferensitertutup (variabel_asap, variabel_alkohol, variabel_gas) :
    if variabel_asap != 0:
        if variabel_alkohol != 0:
            if variabel_gas !=0:
                hasil_output = min (variabel_asap, variabel_alkohol, variabel_gas)
                speed.append([hasil_output, 30])
#proses led merah
#speed=[]
def fungsiinferensiterbuka (variabel_asap, variabel_alkohol, variabel_gas) :
    if variabel_asap != 1:
        if variabel_alkohol != 1:
            if variabel_gas !=1:
                hasil_output = min (variabel_asap, variabel_alkohol, variabel_gas)
                speed.append([hasil_output, 100])

def fungsiinferensitertutup (variabel_asap, variabel_alkohol, variabel_gas) :
    if variabel_asap != 0:
        if variabel_alkohol != 0:
            if variabel_gas !=0:
                hasil_output = min (variabel_asap, variabel_alkohol, variabel_gas)
                speed.append([hasil_output, 70])


fungsiinferensiterbuka(value_banyakC, value_banyakA, value_banyakB)
fungsiinferensiterbuka(value_banyakC, value_sedikitA, value_sedikitB)
fungsiinferensiterbuka(value_banyakC, value_banyakA, value_sedikitB)
fungsiinferensiterbuka(value_sedikitC, value_sedikitA, value_banyakB)
fungsiinferensiterbuka(value_sedikitC, value_banyakA, value_banyakB)
fungsiinferensitertutup(value_sedikitC, value_sedikitA, value_sedikitB)
fungsiinferensitertutup(value_sedikitC, value_banyakA, value_sedikitB)


#print ('maka speed adalah', speed)

#proses defuzzyfikasi

perkalian_new = 0
pembagian_new = 0

for j in range (0, len(speed)):
    perkalian = speed[j][0]*speed[j][1]
    pembagian = speed[j][0]
    perkalian_new = perkalian_new + perkalian
    pembagian_new = pembagian_new + pembagian

z = perkalian_new/pembagian_new

print ('persentasi HIGH (z) = ', z, '[%]')