import TikTokLib as tl

grid = {1:'O',2:'X',3:' ',4:'O',5:'X',6:' ',7:' ',8:'O',9:'X'}

#Ask the human player what symbol he/she prefers
symbol = input('Who is starting? (H/M) ')
#X always starts the game
if symbol is 'H':
    turn = {'X':'human', 'O':'machine'}
else:
    turn = {'X':'machine', 'O':'human'}



gridStruct = {'grid': grid,
              'score': tl.checkWinner(grid, symbol),
              'turn': 'X',
              'children': []}

print(gridStruct)
#Generate Children
numChildren = 0
cellsInGrid = list(grid.values())
for c in cellsInGrid:
    if c is '':
        numChildren += 1

def getChildren(gridStruct, symbol):
    gridChildStruct = {}
    grid = gridStruct['grid']
    score = gridStruct['score']
    turn = gridStruct['turn']
    children = gridStruct['children']

    if score is None:
        for cellkey, cellValue in grid.items():
            if cellValue is ' ':
                gridChild = grid.copy()
                gridChild[cellkey] = turn

                scoreChild = tl.checkWinner(gridChild, symbol)
                turnChild = 'X' if turn is 'O' else 'O'

                gridChildStruct['grid'] = gridChild
                gridChildStruct['score'] = scoreChild
                gridChildStruct['turn'] = turnChild
                gridChildStruct['children'] = []
                tl.displayGrid(gridChild)
                print(scoreChild)


                children.append(getChildren(gridChildStruct, symbol))
        gridStruct['children'] = children
        gridStruct = bestChildren(gridStruct)

    return gridStruct

def bestChildren(gridStruct):
    turn = gridStruct['turn']
    children = gridStruct['children']

    scoreChildren = [child['score'] for child in children]
    score = max(scoreChildren) if turn is 'X' else min(scoreChildren)

    best = scoreChildren.index(score)

    gridStruct['score'] = score
    gridStruct['nextMove'] = children[best]

    return gridStruct


getChildren(gridStruct, symbol)
