# exploring context manager
from contextlib import contextmanager
import sys # we will usee stdout in this code

# lets redirect some data
@contextmanager # python 3 (also Python 2.7)
def stdout_redirect(new_stdout):
    save_stdout = sys.stdout # keep hold of the original output stream
    # change the output context
    sys.stdout = new_stdout
    yield # stdout is a generator!
    # now return to the original context
    sys.stdout = save_stdout

if __name__ == '__main__':
    # switch context and back
    with open('new_out.txt', 'wt') as file_obj: # 'wt' will overrite text
        with stdout_redirect(file_obj):
            print('hello from a redirected system standard output stream')
    # we should see that the stdout has been returned to the default
    print('back again')