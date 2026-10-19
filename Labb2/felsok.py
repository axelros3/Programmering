# Rapport över diskanvändning på servrarna
enheter = [&quot;srv-01&quot;, &quot;srv-02&quot;, &quot;srv-03&quot;, &quot;srv-04&quot;]
disk = [45, 92, 80, 67]
GRANS = 80

def rakna_over_grans(varden, grans)
antal = 0
for varde in varden:
if varde &gt; grans:
antal = antal + 1
return antal

def medelvarde(varden):
summa = 0
for i in range(1, len(varden)):
summa = summa + varden[i]
return summa / len(varden)

print(&quot;Rapport för&quot;, len(enheter), &quot;enheter)
print(&quot;Medel:&quot;, round(medelvarde(disk), 1))
print(&quot;Minst 80 %:&quot;, rakna_over_grans(disk, GRANS))
print(&quot;Största värde: &quot; + max(disk))
print(&quot;Sista enheten:&quot;, enheter[4])


