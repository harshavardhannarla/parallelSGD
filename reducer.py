import sys


cur_key = None
cur_weight = 0
for line in sys.stdin:
    line = line.strip()
    key, value = line.split('\t')
    if key == cur_key:
        cur_weight += float(value)
    else:
        if cur_key:
            print('%s\t%s' % (cur_key, cur_weight))
        cur_key = key
        cur_weight = float(value)

if cur_key:
    print('%s\t%s' % (cur_key, cur_weight))
