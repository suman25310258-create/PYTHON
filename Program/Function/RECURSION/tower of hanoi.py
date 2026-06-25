# WAP TO DEMONSTRATE POPULAR 'TOWER-OF-HANOI' PROBLEM
#------------------------------------------------------#
              # RULES OF THE GAME #

#1. Only one disk can be moved at a time
#2. Only the top disk of a rod can be moved
#3. A larger disk cannot be placed on a smaller disk
#======================================================#

def tower_of_hanoi(n, source, auxiliary, destination):
    if n == 1:
        print("Move disk 1 from", source, "to", destination)
        return

    tower_of_hanoi(n - 1, source, destination, auxiliary)
    print("Move disk", n, "from", source, "to", destination)
    tower_of_hanoi(n - 1, auxiliary, source, destination)


# Input number of disks
n = int(input("Enter number of disks:"))
print() 

tower_of_hanoi(n, 'A', 'B', 'C')