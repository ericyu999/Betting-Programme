# run the betting function certian times to calculate win and lose percentage
# TODO add to fund and betting selector
from betting import betting

timesToRun = 1000

win = 0
lose = 0
for i in range (timesToRun):
    if betting() == 0:
        lose += 1
    else:
        win += 1


winPercent = win / float(timesToRun)
losePercent = lose / float(timesToRun)
print(win)
print(lose)
print(winPercent)
print(losePercent)

print('After {:-9} run, you winned {:-9} times, winning percentage {:2.2%}'.format(timesToRun, win, winPercent))
print('After {:-9} run, you lose {:-9} times, losing percentage {:2.2%}'.format(timesToRun, lose, losePercent))
