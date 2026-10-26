class Solution:
    def numIslands(self, grid):
        # start with frist index if its 1 , counti t as land and conver all 1's connected to it to 0 using below function

        rows = len(grid)
        columns = len(grid[0])
        islands = 0

        for i, value in enumerate(grid):
            for j, value in enumerate(grid[i]):
                print("grid[i][j]", grid[i][j])

                if grid[i][j] == "1":
                    print("equal")
                    islands = islands + 1
                    seen = set()
                    def fillColor(i, j):
                        if grid[i][j] == "1":
                            grid[i][j] = 0

                        if j + 1 < columns and grid[i][j+1] == "1" and (i, j+1) not in seen:
                            grid[i][j+1] = 0
                            seen.add((i, j+1))
                            fillColor(i, j+1)

                        if j - 1 >= 0 and grid[i][j-1] == "1" and (i, j-1) not in seen:
                            grid[i][j-1] = 0
                            seen.add((i, j-1))
                            fillColor(i, j-1)

                        if i + 1 < rows and grid[i + 1][j] == "1" and (i + 1, j) not in seen:
                            grid[i + 1][j] = 0
                            seen.add((i + 1, j))
                            fillColor(i + 1, j)

                        if i - 1 >= 0 and grid[i - 1][j] == "1" and (i - 1, j) not in seen:
                            grid[i - 1][j] = 0
                            seen.add((i - 1, j))
                            fillColor(i - 1, j)
            
                    fillColor(i, j)

        print("islands", islands)
        return islands



sol = Solution()
grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]
print(sol.numIslands(grid))

