

your_list = 'abcdefghijklmnopqrstuvwxyz0123456789 '
complete_list = []
for current in xrange(16):
    a = [i for i in your_list]
    for y in xrange(current):
        a = [x+i for i in your_list for x in a]
    complete_list = complete_list+a

