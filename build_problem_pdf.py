#! /usr/bin/env python

from sys import argv, stdout
from ConfigParser import RawConfigParser
from subprocess import call
import os

devnull = open(os.devnull, 'wb')

def build_problem_text(probdir, report_errors=False):
    print 'Building problem "%s"...' % probdir,
    stdout.flush()

    config = RawConfigParser()
    config.read('%s/domjudge-problem.ini' % probdir)
    probid = config.get('DOMJudge', 'probid')
    probname = config.get('DOMJudge', 'name')

    if call(['cp %s/%s.pdf problemset/pdf/' % (probdir, probid)], shell=True, stderr=devnull):
        if report_errors:
            print ''
            print 'ERROR: "%s" must contain problem pdf' % probdir
        else:
            print 'Failed'

        cleanup()
        return 1

    print 'Done'

if len(argv) < 2:
    for directory in os.listdir('.'):
        if os.path.isdir(directory):
            build_problem_text(directory)
else:
    build_problem_text(argv[1], True)
