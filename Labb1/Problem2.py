
#//
# Lösningsförslag till Problem 2 i programmeringskursens labb 1
# med tillägget för användningsprcent
# författare Axel Roselius
# /#


print("välkommen till nedladdningsberäknaren\nJag vill ha filstorleken")
myFileSize = float(input("ange i GByte: "))
print("nu vill jag ha nedladdningshastigheten")
myBandWidth = int(input("ange i MBit/s: "))
print("och stor del av bandbredden används?")
myBWPercentage = int(input("ge mig procent i heltal tex 80 tack: "))
myTime = (myFileSize * 1000 * 8)/(myBandWidth)
print(f"Med bandbredden {myBandWidth} MBit/s kommer din fil på {myFileSize} GB ta ca {myTime} sekunder att ladda ned")
myTime = (myFileSize * 1000 * 8)/(myBandWidth*(myBWPercentage/100))
print(f"Men med störningar och andra enheter som representeras av hur stor del av bandbredden som används får vi {myTime} sekunder")
mytimformat = "eller "
mytimeHMS =myTime
myHours = 0
myMinutes = 0
mySeconds = 0

##beräkna tiden så vi får en variabel för timmar, en för minuter och en för sekundrar
myHours = int(mytimeHMS/3600)   ##beräkna antalet timmar, vi vill bara ha heltal
mytimeHMS = mytimeHMS % 3600    ##beräkna resterande tid och spara i vår variabel
myMinutes = int(mytimeHMS / 60) ##beräkna antalet minuter, vi vill bara ha heltal
mySeconds = mytimeHMS %60       ##beräkna antalet resterande sekunder

if(myHours > 0):
    mytimformat = mytimformat + f"{myHours} timmar "

if(myMinutes > 0):
    mytimformat = mytimformat + f"{myMinutes} minuter "

if(mySeconds > 0):
    mytimformat = mytimformat + f"{mySeconds} sekunder."

print(mytimformat)

print("hejdå")







