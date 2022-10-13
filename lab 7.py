def minimum_mpg():
    while True:
        try:
            user_mpg = float(input('Enter the minimum mpg ==> '))
            if user_mpg <= 0:
                print('Fuel economy given must be greater than 0')
            elif user_mpg > 100:
                print('Fuel economy must be less than 100')
            else:
                return user_mpg
        except ValueError:
            print('You must enter a number for the fuel economy')
            
def open_file():
    while True:
        try:
            my_file = input('Enter the name of the input vehicle file ==> ')
            main_file = open(my_file, 'r')
            return main_file
        except FileNotFoundError:
            print('Could not open file', my_file)
        except IOError:
            print('There is an IO Error', my_file)

def output_file():
    while True:
        try:
            out_file = input('Enter the name of the file to output to ==> ')
            file2 = open(out_file, 'w')
            return file2
        except IOError:
            print('There is an IO Error', out_file)

mpg = minimum_mpg()
file = open_file()
fileout = output_file()

next(file)
for row in file:
    try:
        car = row.split('\t')
        combined_mpg = float(car[-3])
        if combined_mpg >= mpg:
            output = '{:<5}{:<20}{:<40}{:>10}.000\n'.format(car[0], car[1], car[2],  car[-3])
            fileout.write(output)
    except ValueError:
        print('Could not convert value {} for vehicle {} {} {}'.format(car[-3], car[0], car[1], car[2]))

file.close()
fileout.close()
