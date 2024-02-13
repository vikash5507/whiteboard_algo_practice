# Cron Expression Parser

### Problem Statement:
Write a command line application or script which parses a cron string and expands each field to show the times at which it will run. You may use whichever language you feel most comfortable with.
You should only consider the standard cron format with five time fields (minute, hour, day of month, month, and day of week) plus a command, and you do not need to handle the special time strings such as "@yearly". The input will be on a single line.
The cron string will be passed to your application as a single argument.

```~$ your-program "*/15 0 1,15 * 1-5 /usr/bin/find"```

INPUT:
```buildoutcfg 
*/15 0 1,15 * 1-5 /usr/bin/find
```

EXPECTED OUTPUT:
```buildoutcfg
minutes       0 15 30 45
hours         0
day of month  1 15
month         1 2 3 4 5 6 7 8 9 10 11 12
day of week   1 2 3 4 5
command       /usr/bin/find
```

### Running the Script:
- Download the code, move to `deliveroo/cron-text-parser` folder
- Ensure Python3 is installed in local environment
```bash
python3 cron_parser.py "*/15 0 1,15 * 1-5 /usr/bin/find"
```

### Running Test Cases:
- Download the code, move to `deliveroo/cron-text-parser` folder
- Ensure Python3 is installed in local environment
```bash
python3 test_cron_parser.py
```