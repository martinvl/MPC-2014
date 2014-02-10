from check_rps import get_third, get_score, IllegalMovesError

# ---- get_third tests ----
if get_third('Rock', 'Paper') != 'Scissors':
    raise Exception()

if get_third('Rock', 'Scissors') != 'Paper':
    raise Exception()

if get_third('Paper', 'Rock') != 'Scissors':
    raise Exception()

if get_third('Paper', 'Scissors') != 'Rock':
    raise Exception()

if get_third('Scissors', 'Rock') != 'Paper':
    raise Exception()

if get_third('Scissors', 'Paper') != 'Rock':
    raise Exception()

try:
    print get_third('Rock', 'Rock')
    raise Exception()
except IllegalMovesError:
    pass

try:
    print get_third('Paper', 'Paper')
    raise Exception()
except IllegalMovesError:
    pass

try:
    print get_third('Scissors', 'Scissors')
    raise Exception()
except IllegalMovesError:
    pass

# ---- get_score tests ----
if get_score('Rock', 'Rock') != .5:
    raise Exception()

if get_score('Rock', 'Paper') != 0:
    raise Exception()
if get_score('Rock', 'Scissors') != 1:
    raise Exception()
if get_score('Paper', 'Rock') != 1:
    raise Exception()
if get_score('Paper', 'Paper') != .5:
    raise Exception()
if get_score('Paper', 'Scissors') != 0:
    raise Exception()
if get_score('Scissors', 'Rock') != 0:
    raise Exception()
if get_score('Scissors', 'Paper') != 1:
    raise Exception()
if get_score('Scissors', 'Scissors') != .5:
    raise Exception()

# ---- All OK ----
print 'all tests passed'
