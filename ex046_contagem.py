print('-='*13, '\n\t\033[33mCONTAGEM REGRESSIVA!\033[m')
print('-='*13)

from time import sleep
for c in range( 10, -1, -1):
    print(c)
    sleep(1)
from emoji import emojize
print(emojize(':fireworks:'*10, use_aliases=True))
