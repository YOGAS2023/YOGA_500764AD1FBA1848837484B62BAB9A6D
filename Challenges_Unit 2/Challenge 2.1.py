# Write a program that writes a series of random numbers to a file.
# Each random number should be in range of 1 through 500. The application should let user specify how many numbers the
# file will hold.

def main():
    import random
    numberOfTimes = int(input('Enter the amount of random numbers you would like in numeric '))
    counter = 0
    outfile = open('numbers.txt', 'w')
    while counter < numberOfTimes:
        randomNumber = random.randint(1, 500)
        counter = counter + 1
        outfile.write(str(randomNumber) + '\n')

    outfile.close()
    print('Data written to numbers.txt')

main()