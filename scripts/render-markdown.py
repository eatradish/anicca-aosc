import sys
import re

if __name__ == '__main__':
    print('# Anicca AOSC')
    print('This is a small utility to run `aosc-findupdate` regularly by GitHub Actions.')
    print('## Result')

    table = []

    for line in sys.stdin:
        line = line.strip()

        if 'The following packages were updated:' in line or not line:
            continue
        
        if 'Errors:' in line:
            break

        if line[0:4] == 'Name':
            print('| Package | Repo Version | New Version | Issues |')
            print('|---------|--------------|-------------|--------|')
            continue

        table.append(re.split('\s+', line.replace('->', ' '), 3))
    
    for row in sorted(table, key = lambda x: x[0]):
        row[1] = row[1].replace('+', '<br>+')
        print('|' + '|'.join(row) + '|')