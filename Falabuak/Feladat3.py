print("3.Feladat:")
vereseg=0
dontetlen =0
gyoztelem=0
for i in golk:
    if i< 0:
        vereseg+=1
    if i==0:
        dontetlen+=1
    if i> 0:
        gyoztelem+=1

#gyoztelem=len(golk)-dontetlen-vereseg
print(f"A szezonban  csapatnak {gyoztelem} győzelem, {dontetlen} döntetlen, {vereseg} veresége volt")