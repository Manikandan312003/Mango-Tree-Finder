row,coloum,tree=map(int,input().split())
if tree%row in [0,1] or tree<=row:
    print("True")
else:
    print("False")

