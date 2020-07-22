import csv
import sys


def countTotalBits(num): 
      
     # convert number into it's binary and  
     # remove first two characters 0b. 
     binary = bin(num)[2:] 
     #print(len(binary))
     return len(binary)
y = 0
x = 0

def TempCoder(tempv):
    global y
    
    y = y << countTotalBits(tempv)
    y = y ^ tempv

    return y

def DateAndTimeCoder(dtv):
    global x
    x = x << countTotalBits(dtv)
    x = x ^ dtv

    return x

for arguments in sys.argv:
    arg = arguments;
#decoder
if arguments == "-r":
    #print("hola")
    decode = open("Output.csv", "r")
    csv_decoder = csv.reader(decode,delimiter=',')
    line_count = 0
    for rows in csv_decoder:
        if line_count == 0:
            line_count += 1
        else:
            for lines in rows:
                line_count +=1
                if line_count==3:
                    num = 0
                    
                    while(num < 100):
                        num = binary & int(lines)
                        #num = num >> 2
                        print(num)
                        
                    print(int(lines))
                #print(lines)
                #print(line_count)
            
    
else:
    with open('Input.csv') as csv_file:
        output = open("Output.csv", "a")
        output.write("DateAndTime,Climate\n")
        csv_reader = csv.reader(csv_file,delimiter=',')
        line_count = 0
        
        for rows in csv_reader:
            if line_count == 0:
                line_count += 1
            else:
                print(rows[0] + " " + rows[1] + " " + rows[2] + " " + rows[3])
                line_count += 1
                data = rows[0].split("-", 2)
                
                DT = 0
                Temp = 0
                sign = 0
                
                #DateAndTime
                #Year, Month
                for i in range(2):
                    DT = DateAndTimeCoder(int(data[i]))
                    #x = x << countTotalBits(int(data[i]))
                    #x = x ^ int(data[i])

                #Day
                data2 = data[2].split("T")
                DT = DateAndTimeCoder(int(data2[0]))
                #x = x << countTotalBits(int(data2[0]))
                #x = x ^ int(data2[0])
                print(data2)

                #Hours,Minutes,Seconds
                data3 = data2[1].split(":")
                for i in range(3):
                    if i == 2:
                        data4 = data3[i].split(".")
                        DT = DateAndTimeCoder(int(data4[0]))
                        print("its me")
                        print(data4[1])

                        
                        if data4[1].find('-') < 0:
                            sign = 1
                            #print("plus")
                        else:
                            sign = 0
                            #print("minus")

                        symbol = ''
                        if sign == 1:
                            symbol = '+'
                        elif sign == 0:
                            symbol = '-'
                            
                        data5 = data4[1].split(symbol)
                        print("its me")
                        print(data5)
                        print(symbol)

                        
                        for i in range(2):
                            DT = DateAndTimeCoder(int(data5[i]))
                         
                    else:
                        DT = DateAndTimeCoder(int(data3[i]))

                 
                print(data3)
                print(sign)
                #MinTemp,MaxTemp,Precipitation
                for i in range(4):
                    if i == 0:
                        continue
                    else:
                        Temp = TempCoder(int(rows[i]))
                        #y = y << countTotalBits(int(rows[i]))
                        #y = y ^ int(rows[i])
                

                #Sybmol coder
                DT = DateAndTimeCoder(sign)   
                        
                
                print(data)
                print("codificado")
                print(DT)
                x = 0
                print(Temp)
                y = 0
                output.write("{},{}\n".format(DT, Temp))
                #for tmp in data:
                #    print(tmp)
    output.close()            



#x = 0
#x = x << countTotalBits(2020)
#x = x ^ 2020
#print(x)
#x = x << countTotalBits(12)
#x = x^12
#print(x)
#x = x << countTotalBits(13)
#x = x^13
#print(x)
#x = x << countTotalBits(19)
#x = x^19
#print(x)
#x = x << countTotalBits(30)
#x = x^30
#print(x)

print(countTotalBits(105630))
print(countTotalBits(52318))
#print(countTotalBits(8887625200695790))





