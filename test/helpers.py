import odb
import os
import utl

def make_rect(design, xl, yl, xh, yh):
    xl = design.micronToDBU(xl)
    yl = design.micronToDBU(yl)
    xh = design.micronToDBU(xh)
    yh = design.micronToDBU(yh)
    return odb.Rect(xl, yl, xh, yh)

def make_result_file(filename):
    result_dir = os.path.join(os.getcwd(), 'results')
    if not os.path.exists(result_dir):
        os.mkdir(result_dir)

    root_ext = os.path.splitext(filename)
    filename = "{}-py{}".format(*root_ext)
    return os.path.join(result_dir, filename)

def diff_files(file1, file2):
    with open(file1, 'r') as f:
        lines1 = f.readlines()

    with open(file2, 'r') as f:
        lines2 = f.readlines()

    num_lines1 = len(lines1)
    num_lines2 = len(lines2)
    for i in range(min(num_lines1, num_lines2)):
        if lines1[i] != lines2[i]:
            print(f"Differences found at line {i}")
            print(lines1[i])
            print(lines2[i])
            return 1

    if num_lines1 != num_lines2:
        print(f"Number of lines differs {num_lines1} vs {num_lines2}.")
        return 1

    print("No differences found.")
    return 0

# Output voltage file is specified as ...
utl.suppress_message(utl.PSM, 2)
# Output current file specified ...
utl.suppress_message(utl.PSM, 3)
# Output spice file is specified as
utl.suppress_message(utl.PSM, 5)
# SPICE file is written at
utl.suppress_message(utl.PSM, 6)
# Reading DEF file
utl.suppress_message(utl.ODB, 127)
# Finished DEF file
utl.suppress_message(utl.ODB, 134)
