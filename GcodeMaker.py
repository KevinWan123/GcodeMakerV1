
import pandas as pd

#USE ABSOLUTE POSITIONING

#Print Location
PrintX=10000 
PrintY=20000
PrintZ=30000

#Intermediate Z of print
InterZ = 25000
#Dispensing Position
DispX = 40000
DispY = 50000
DispZ = 60000

#Print Speed
F = 10000
with open("print.txt", "w") as file:
    file.write(f"F{10000}\n")
    file.write(f"$global[1]=0\n")
    file.write(f"$global[4]= 0\n")
    print('Done')

df = pd.read_excel("ResinPrint.xlsx")
Layer = df["Layers"].max()
Dispense = df["Dispense"]
Thickness = df["Thickness"]
Exposure = df["Exposure"]
Image = df["Index"]

ThicknessCounter = Thickness[0]

with open("print.txt", "a") as file:
    for i in range(0, Layer):
        #Go to Dispense location
        file.write(f"G90 X {DispX}\n")
        file.write(f"G90 Y {DispY}\n")
        file.write(f"G90 Z {DispZ}\n")

        #Pause for Dispension
        file.write("G4 P2\n")
        file.write(f"$global[1]={Dispense[i]}\n")
        file.write("G4 P6\n")

        file.write(f"\n")

        #Go to Print Step
        file.write(f"G90 Z {InterZ}\n")
        file.write(f"G90 X {PrintX}\n")
        file.write(f"G90 Y {PrintY}\n")

        # Go to print Z
        file.write(f"F4000\n")
        file.write(f"\n")
        file.write(f"\\\Print \n")
        file.write(f"G90 Z {PrintZ - ThicknessCounter}\n")
        file.write(f"\n")
        ThicknessCounter +=  Thickness[i]

        print(PrintZ - ThicknessCounter)

        #Turn Dlp to right image 
        file.write(f"$global[4] = 102\n")
        file.write(f"$global[4] = {Image[i]}\n")

        #Print
        file.write(f"\\\Exposure Time \n")
        file.write(f"G4 P{Exposure[i]}\n")
        file.write(f"$global[4] = 101\n")
        file.write(f"$global[4] = 0\n")
        
        #Leaving Print
        file.write("F2000\n")
        file.write(f"G91 Z-10000\n")
        file.write(f"F{F}\n")




        









        
   