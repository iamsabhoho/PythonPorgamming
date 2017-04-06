import TikTokLib as tl

grid = {1:'',2:'',3:'',4:'',5:'',6:'',7:'',8:'',9:''}
tl.displayGrid(grid)
print(tl.checkWinner(grid) + ' won.')
grid = tl.playersInput(grid, 'x')
tl.displayGrid(grid)

