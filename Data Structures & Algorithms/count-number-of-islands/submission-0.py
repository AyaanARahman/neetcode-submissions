class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0

        rows, cols = len(grid), len(grid[0])
        visited = set()
        countIsland = 0

        # BFS explores every piece of land connected to (r, c)
        def bfs(r, c):
            queue = collections.deque()
            queue.append((r, c))
            visited.add((r, c))

            # Four possible directions: down, up, right, left. think quadrants
            directions = [
                (1, 0),
                (-1, 0),
                (0, 1),
                (0, -1)
            ]

            while len(queue) > 0:
                #popleft treats it like a queue. pop just treats it like dfs
                row, col = queue.popleft()

                # Explore all four neighbors
                for dr, dc in directions:
                    nr = row + dr
                    nc = col + dc

                    # Make sure neighbor is:
                    # 1. Inside the grid
                    # 2. Land
                    # 3. Not already visited
                    if (
                        0 <= nr < rows
                        and 0 <= nc < cols
                        and grid[nr][nc] == "1"
                        and (nr, nc) not in visited
                    ):
                        visited.add((nr, nc))
                        queue.append((nr, nc))

        # Scan every cell looking for a new, unvisited island
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1" and (r, c) not in visited:
                    bfs(r, c)
                    countIsland += 1

        return countIsland