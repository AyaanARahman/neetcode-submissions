class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:

        rows, cols = len(grid), len(grid[0])

        time = 0
        queue = collections.deque()

        # Step 1: Find ALL initially rotten oranges
        # They are all starting points for our BFS.
        fresh = 0

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2:
                    queue.append((r, c))
                elif grid[r][c] == 1:
                    fresh += 1

        directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]

        # Step 2: Multi-source BFS
        while queue and fresh > 0:

            # Everything currently in the queue represents
            # oranges that are rotten at the START of this minute.
            for _ in range(len(queue)):
                row, col = queue.popleft()

                # Check all 4 neighbors
                for dr, dc in directions:
                    nr = row + dr
                    nc = col + dc

                    # Make sure neighbor is inside the grid
                    # and is a fresh orange.
                    if (
                        0 <= nr < rows
                        and 0 <= nc < cols
                        and grid[nr][nc] == 1
                    ):
                        # This orange becomes rotten.
                        grid[nr][nc] = 2
                        fresh -= 1

                        # It will spread the rot during the NEXT minute.
                        queue.append((nr, nc))

            # We have finished processing one entire BFS level.
            # Therefore, one minute has passed.
            time += 1

        # If fresh oranges remain, they could never be reached.
        if fresh > 0:
            return -1

        return time