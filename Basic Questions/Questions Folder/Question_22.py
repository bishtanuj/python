def tower_of_hanoi(disks, source, auxiliary, target):
    if disks == 1:
        print(f"Move disk 1 from {source} to {target}")
        return

    tower_of_hanoi(disks - 1, source, target, auxiliary)
    print(f"Move disk {disks} from {source} to {target}")
    tower_of_hanoi(disks - 1, auxiliary, source, target)


if __name__ == "__main__":
    disk = int(input("Enter number of disks: "))
    tower_of_hanoi(disk, 'A', 'B', 'C')

    
# OUTPUT
# Enter number of disks: 3
# Move disk 1 from A to C
# Move disk 2 from A to B
# Move disk 1 from C to B
# Move disk 3 from A to C
# Move disk 1 from B to A
# Move disk 2 from B to C
# Move disk 1 from A to C
