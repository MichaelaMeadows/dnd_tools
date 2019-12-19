import random

##### Constants ####
#General Goodness - Higher just makes generally better stat pools. 395 seems like a good default cause it averages about 12
general_goodness = 395
#Lower the average stat pool power cap
max_goodness = 410
# How much 'better' the best row is allowed to be
goodness_gap = 3
#Require there's at least 1 17 or 18 in the grid somewhere
require_high_value = True
#For very high variance rolls, you may want to cap the max stat power
max_power = 78

iteration = 0
####################

def getDieValue():
  #return (random.randint(1, 6) + random.randint(1, 6) + random.randint(1, 6))
  #return (random.randint(1, 8) + random.randint(1, 8)) + 2
  return (random.randint(3,20) - 2)



def checkGrid(grid):
    max_val = 0
    runner_up = 0
    temp = 0
    row_sums=[]
    # checking the rows
    for y in range(0, 6):
        temp = sum(grid[y])
        row_sums.append(temp)
        if (temp > max_val):
            runner_up = max_val
            max_val = temp

    # checking the columns
    for y in range(0, 6):
        tmp = []
        for z in range(0, 6):
            tmp.append(grid[z][y])
        row_sums.append(sum(tmp))
        if (sum(tmp) > max_val):
            runner_up = max_val
            max_val = sum(tmp)


    if (max_val > max_power):
        print('Maximum power is too high')
        return True

    print(row_sums)
    if ((max_val - runner_up) > goodness_gap):
        print('One row seems too good. Re generating')
        return True
    return False

needToGen = True

while(needToGen):
    iteration += 1
    print('iteration count ' + str(iteration))
    print('Testing new generation')
    total = 0
    found_high_value = False

    grid = {}
    for y in range (0,6):
     grid[y] = []

    for x in range(0,36):
     num = getDieValue()
     if (num >= 17):
         found_high_value = True
     total += num
     grid[(x % 6)].append(num)

    for y in range (0,6):
     print(grid[y])

    print('Pool Strength was ' + str(total))
    if ((total > general_goodness) or (total > max_goodness)):
        needToGen = checkGrid(grid)
    else:
        print('Pool is not within power boundaries')

    if(require_high_value and not (found_high_value)):
        print('No high values present')
        needToGen = True
print('Pool conditions satisfied')
