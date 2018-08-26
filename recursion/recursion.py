def hanoi(disks, start_peg, staging_peg, goal_peg):
    if (disks >= 1):
        hanoi(disks - 1, start_peg, goal_peg, staging_peg)
        print("Move disk", disks, "from peg", start_peg, "to peg", goal_peg)
        hanoi(disks - 1, staging_peg, start_peg, goal_peg)


hanoi(8, "A", "B", "C")

""" ===================================================================  """
int linecount():
    if at front of line:
        return 1

  return linecount()+1
