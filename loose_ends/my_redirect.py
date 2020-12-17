# context management without using the @contextmanager
import sys

class Redirect(object): # for py2
    def __init__(self, new_stdout):
        self.new_stdout = new_stdout
    # we must provide an enter and an exit method
    def __enter__(self):
        'redirect'
        self.save_stdout = sys.stdout
        sys.stdout = self.new_stdout
    def __exit__(self, exc_type, exc_value, exc_traceback):
        'recover to original'
        sys.stdout = self.save_stdout

if __name__ == '__main__':
    with open('redirected.txt', 'at') as f_obj: # 'at' will append text
        with Redirect(f_obj):
            print('this gets redirected to our file output')
    print('no more redirection')