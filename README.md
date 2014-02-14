These are the exercices for the first competition fully organized by MAPS!

### Problem requirements
Each problem should have a name, and an ID (alphanumeric, at most 8 characters). All problem related files should be put in a folder with the same name as it's ID.

The following files must be present in the folder:

- `domjudge-problem.ini` (see [template](domjudge-problem.ini), change `probid` and `name`)
- `README.md` (preferred) or `README.html`, containing the problem text  
	If `README.html` doesn't exist, an HTML file will be generated from `README.md`  
	Note: Images must be put in the `images` folder
- One or more reference solutions with filename on the form `<problem ID>*.py` or `<problem ID>*.py3`. This is used for automatically verifying testcases in DOMJudge. The first line of these files should be a magic string, such as `# @EXPECTED_RESULTS@: CORRECT`. Replace `CORRECT` with `WRONG-ANSWER`, `RUN-ERROR` or `TIMELIMIT` depending on what is appropriate.
- One or more pairs of `<testcase>.in` and `<testcase>.out`

### Online judge
Martin has set up an online judge (similar to the one we will use during the contest). This is good place to test alternative solutions and timing. Only the problems with testcases have been added.

First download the fake [SSL certificate](http://95.85.46.235/domjudge/public.crt) we are using, and [add it](http://lmgtfy.com/?q=add+certificate+firefox&l=1) to your browser.

Then [log in](http://95.85.46.235/domjudge/team) to test your solutions.

The following users are registered, they all have the password `z8zsri`.

- `martinvl`
- `torgebo`
- `Alopex8064`
- `jingt`
- `markusdregi`
- `mousaka2410`
- `matiasholte`
- `HrKristiansen`
- `leifhka`
- `staalezh`
- `helenens`
- `olalia`

Send Martin an email at <martinvl@math.uio.no> if you want to be on this list!
