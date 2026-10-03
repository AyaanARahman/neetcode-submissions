class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:

        # Map each course → list of prerequisites
        preMap = {i: [] for i in range(numCourses)}

        # Build the graph
        for crs, pre in prerequisites:
            preMap[crs].append(pre)

        # Courses currently being explored in the current DFS path
        visited = set()

        def dfs(crs):

            # If we encounter a course already on the current
            # DFS path, we've found a cycle.
            if crs in visited:
                return False

            # No prerequisites → nothing else to explore.
            # This course can be completed.
            if preMap[crs] == []:
                return True

            # Mark this course as being explored.
            visited.add(crs)

            # Explore EVERY prerequisite.
            for pre in preMap[crs]:
                if not dfs(pre):
                    return False

            # We've successfully explored all prerequisites.
            # Remove this course from the current DFS path.
            visited.remove(crs)

            # Mark this course as fully processed.
            # We don't need to DFS through its prerequisites again.
            preMap[crs] = []

            return True

        # Try every course because the graph may be disconnected.
        for crs in range(numCourses):
            if not dfs(crs):
                return False

        return True