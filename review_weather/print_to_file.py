
def print_report(text):
    fout = open('reports.txt', 'at')
    print(text, file=fout)
    fout.close()

if __name__ == '__main__':
    info = 'booglyboodiboingaboodle'
    print_report(info)
