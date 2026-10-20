#//
# Lösningsförslag till del 4: refaktorering i programmeringskursens labb 2
# författare Axel Roselius
# /#

a=[120,95,310,80,450]
b=0
c=0
for x in a:
 b=b+x
 if x>300:c=c+1
print("tot",b)
print("snitt",b/len(a))
print("hog",c)
