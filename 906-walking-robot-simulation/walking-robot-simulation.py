class Solution:
    def robotSim(self, commands: List[int], obstacles: List[List[int]]) -> int:
        obstacles = set((x, y) for x, y in obstacles)

        direction = self.get_initial_direction()
        max_dist = 0
        x, y = 0, 0
        for command in commands:
            if command < 0:
                if command == -2:
                    direction = direction.next
                elif command == -1:
                    direction = direction.prev
            elif command < 10:
                for i in range(0, command):
                    tmp_x, tmp_y = x, y
                    tmp_x += direction.dx
                    tmp_y += direction.dy
                    if (tmp_x, tmp_y) in obstacles:
                        break
                    x, y = tmp_x, tmp_y
                max_dist = max(max_dist, x ** 2 + y ** 2)

        return max_dist
        
    def get_initial_direction(self):
        dirs = [(0, 1), (-1, 0), (0, -1), (1, 0)] # U, L, D, R
        head = Node(dirs[0])
        curr = head
        for i in range(1, 4):
            curr.next = Node(dirs[i])
            curr.next.prev = curr
            curr = curr.next

        curr.next = head
        head.prev = curr
        return head

class Node:
    def __init__(self, d):
        self.prev = None
        self.next = None
        self.dx, self.dy = d
        