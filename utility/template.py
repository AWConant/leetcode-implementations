import sys

WRITEUPS_PATH = "C:/Users/acona/Documents/source/oj-solutions/Reviewed/"
SOLUTIONS_PATH = "C:/Users/acona/Documents/source/leetcode-implementations/solutions/"

PRELUDE = "---\nID: {}\nTITLE: {}\nAUTHOR: emptyset\n---\n\n[TOC]\n\n"

APPROACH = """#### Approach #{} []\n\n**Intuition**\n\n**Algorithm**\n
<playground>\n\n```java\n{}\n```\n\n```python3\n{}\n```\n\n</playground>\n
**Complexity Analysis**\n\n* Time complexity : $$O()$$\n 
* Space complexity : $$O()$$\n\n---\n\n"""

POSTLUDE = "Analysis and solutions written by: [@emptyset](https://leetcode.com/emptyset)\n"

if len(sys.argv) != 4:
    print("Usage python3 template.py <problem id> <name> <number of approaches>")
    sys.exit()

_, pid, title, approach_count = sys.argv

outfname = "{}_{}.md".format(pid, "_".join(title.split()))

with open(WRITEUPS_PATH + outfname, "w") as outf:
    outf.write(PRELUDE.format(pid, title))

    for approach_number in range(1, int(approach_count)+1):
        # Read source for solutions in both Java and Python3
        with open(SOLUTIONS_PATH + "{}/{}.java".format(pid, approach_number), "r") as inf:
            java_code = inf.read()
        with open(SOLUTIONS_PATH + "{}/{}.py".format(pid, approach_number), "r") as inf:
            python_code = inf.read()

        outf.write(APPROACH.format(approach_number, java_code, python_code))

    outf.write(POSTLUDE)