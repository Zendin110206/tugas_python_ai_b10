def hanoi_solver(total_disks):
    # Prepare the 3 rods. 
    # Rod 0 is Source, Rod 1 is Auxiliary (helper), Rod 2 is Target.
    # range(total_disks, 0, -1) creates the initial pile, e.g., [3, 2, 1]
    rods = [list(range(total_disks, 0, -1)), [], []]

    moves_history = []
    
    # Capture the current state of the rods.
    def record_state():
        current_state = f"{rods[0]} {rods[1]} {rods[2]}"
        moves_history.append(current_state)

    # Record the initial state before making any moves.
    record_state()

    # Recursive divide-and-conquer engine.
    def move_disk(n, source, target, auxiliary):
        # Base case: move a single disk directly to the target rod.
        if n == 1:
            disk = rods[source].pop()
            rods[target].append(disk)
            record_state()
            return
        
        # Move n - 1 disks from the source rod to the auxiliary rod.
        move_disk(n - 1, source, auxiliary, target)
        
        # Move the largest disk from the source rod to the target rod.
        disk = rods[source].pop()
        rods[target].append(disk)
        record_state()
        
        # Move n - 1 disks from the auxiliary rod to the target rod.
        move_disk(n - 1, auxiliary, target, source)

    # Trigger the recursive engine when there are disks to move.
    if total_disks > 0:
        # Move all disks from index 0 (A) to index 2 (C), using index 1 (B) as helper.
        move_disk(total_disks, 0, 2, 1)

    # Join all recorded snapshots with newline characters for the expected output format.
    return "\n".join(moves_history)


print(hanoi_solver(3))
