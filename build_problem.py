#! /usr/bin/env python

"""Builds a problem archive ready for upload to DOMJudge
Problem directory must (at least) contain:
    * domjudge-problem.ini
    * <probid>*.py or <probid>*.py3
    * README.md OR README.html

Should also contain one or more pairs of <testcase>.in and <testcase>.out

If problem directory contains README.html, this is used directly for problem
text.

Otherwise, problem directory must contain README.md which is used to
generate HTML. Title will be set to problem name from domjudge-problem.ini, and
all images will be centered.

USAGE: build_problem.py [problem directory]
If no problem directory is provided, the script will attempt to build all
subdirectories of the current directory.
If a problem directory is provided, errors will be printed.
"""

from ConfigParser import RawConfigParser
from sys import argv, exit, stdout
from subprocess import call
import os

devnull = open(os.devnull, 'wb')

def cleanup():
    call(['rm -r tmp'], shell=True, stderr=devnull)

def build_problem(probdir, report_errors=False):
    print 'Building problem "%s"...' % probdir,
    stdout.flush()

    call(['mkdir tmp'], shell=True, stderr=devnull)
    call(['rm -r tmp/*'], shell=True, stderr=devnull)

    if call(['cp %s/domjudge-problem.ini tmp/' % probdir], shell=True, stderr=devnull):
        if report_errors:
            print ''
            print 'ERROR: "%s" must contain domjudge-problem.ini' % probdir
        else:
            print 'Failed'

        cleanup()
        return 1

    config = RawConfigParser()
    config.read('tmp/domjudge-problem.ini')
    probid = config.get('DOMJudge', 'probid')
    probname = config.get('DOMJudge', 'name')

    solution = '%s*.py*' % probid

    if call(['cp %s/%s*.py* tmp/' % (probdir, probid)], shell=True, stderr=devnull):
        if report_errors:
            print ''
            print 'ERROR: "%s" must contain one or more solutions' % probdir
        else:
            print 'Failed'

        cleanup()
        return 1

    if call(['cp %s/*.in tmp/' % probdir], shell=True, stderr=devnull) or\
            call(['cp %s/*.out tmp/' % probdir], shell=True, stderr=devnull):
        if report_errors:
            print ''
            print 'ERROR: "%s" must contain one or more testcases' % probdir
        else:
            print 'Failed'

    if call(['cp %s/README.html tmp/problem.html' % probdir], shell=True, stderr=devnull):
        if call(['cp %s/README.md tmp/' % probdir], shell=True, stderr=devnull):
            if report_errors:
                print ''
                print 'ERROR: "%s" must contain problem text' % probdir
            else:
                print 'Failed'

            cleanup()
            return 1

        call(['grip --gfm --export tmp/README.md'], shell=True, stdout=devnull)
        call(['mv tmp/README.html tmp/problem.html'], shell=True)

        f = open('tmp/problem.html', 'r+')
        prob_text = f.read()
        f.seek(0)

        # center images
        img_head_needle = r' target="_blank"><img src="'
        img_head_replace = ' target="_blank"><center><img src="'
        img_tail_needle = r' style="max-width:100%;"></a>'
        img_tail_replace = ' style="max-width:100%;"></center></a>'

        prob_text = prob_text.replace(img_head_needle, img_head_replace)
        prob_text = prob_text.replace(img_tail_needle, img_tail_replace)

        # fix title
        title_needle = '<title>tmp/README.md - Grip</title>'
        title_replace = '<title>%s</title>' % probname
        prob_text = prob_text.replace(title_needle, title_replace)

        f.write(prob_text)
        f.close()

    files = ' '.join(['tmp/domjudge-problem.ini',
        'tmp/problem.html',
        'tmp/%s' % solution,
        'tmp/too-slow.py*',
        'tmp/*.in',
        'tmp/*.out'])

    call(['mkdir build'], shell=True, stderr=devnull)
    call(['zip -j build/%s.zip %s' % (probid, files)], shell=True, stdout=devnull)

    cleanup()

    print 'Done'

if len(argv) < 2:
    for directory in os.listdir('.'):
        if os.path.isdir(directory):
            build_problem(directory)
else:
    build_problem(argv[1], True)

