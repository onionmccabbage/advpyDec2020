# exploring functional programming
# import our modules
# import my_modules.my_map
from my_modules.my_map import my_gen
from my_modules.my_filter import between as f10_20 # we can rename imports

def main():
    gen = my_gen() # was my_modules.my_map.my_gen()
    f = filter(f10_20, (2,13,25))
    print(f)

# exercise this code
if __name__ == '__main__':
    main()
