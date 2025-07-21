
def tower(disk,source,auxi,dest):
    if(disk==1):
        print("move disk 1 from source to destination")
    else:
        tower(disk-1,source,dest,auxi)
        print("move {} from {} to {}".format(disk,source,dest))
        tower(disk-1,auxi,source,dest)

disk=int(input("Enter the disk number: "))
print("Steps involved aree")
tower(disk,'A','B','C')