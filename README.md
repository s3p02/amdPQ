## Write a program that program behaves like this:

aaeeeeebcdffff -> aaze5bcdzf4

aefrtdddggg -> aefrtzd3zg3

aertttefze -> aerzt3efze

## Solution:

```virtualenv -p /usr/local/bin/python3 py3env```

Using Python 3.7.0 - ```source ../py3env/bin/activate```

```coverage run main.py```

![Main Program Run](program_run.png)

```coverage report -m```

![Code Coverage](code_coverage_report.png)
