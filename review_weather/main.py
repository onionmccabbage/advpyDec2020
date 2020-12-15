from weather import Weather
from location import Location
from countries import countries
from print_to_file import print_report

def main():
    l1 = Location('Edinburgh', 'uk')
    w_edi = Weather('bright', 9.04, l1)
    l2 = Location('Galway', 'ie')
    w_gal = Weather('windy', 6.70, l2)
    l3 = Location('Kingston', 'jm')
    w_kt = Weather('Sunny', 27.98, l3)
    w_kt.changeTemp()
    
    print(w_edi)
    print(w_gal)
    print(w_kt)

    # put this into the report text file
    print_report(w_edi)
    print_report(w_gal)
    print_report(w_kt)


if __name__ == '__main__':
   main()
