# file to collect data from user and raise errors
reset = input("Would you like to reset your stats or continue from your last save? ('reset' or 'continue')")
# reset = 'reset'
changeStats = False
if reset == 'reset':
    changeStats = True
elif reset == 'continue':
    pass
else:
    raise ValueError

