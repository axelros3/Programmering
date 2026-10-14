
#//
# Lösningsförslag till Problem 2 i programmeringskursens labb 1
# författare Axel Roselius
# /#


print("välkommen till nedladdningsberäknaren\nJag vill ha filstorleken")
myFileSize = float(input("ange i GByte: "))
print("nu vill jag ha nedladdningshastigheten")
myBandWidth = int(input("ange i MBit/s: "))
myTime = (myFileSize * 1000 * 8)/(myBandWidth)
print(f"Med bandbredden {myBandWidth} kommer din fil på {myFileSize} GB ta ca {myTime} sekunder att ladda ned")

mytimformat = "eller "
mytimeHMS =myTime
myHours = 0
myMinutes = 0
mySeconds = 0

##beräkna antalet timmar
##while (mytimeHMS  >= 3600):
myHours = mytimeHMS/3600
mytimeHMS = mytimeHMS % 3600
myMinutes = mytimeHMS / 60
mySeconds = mytimeHMS %60

if(myHours > 0):
    mytimformat = mytimformat + f"{myHours} timmar "

if(myMinutes > 0):
    mytimformat = mytimformat + f"{myMinutes} minuter "

if(mySeconds > 0):
    mytimformat = mytimformat + f"{mySeconds} sekunder."

print(mytimformat)

print("hejdå")







