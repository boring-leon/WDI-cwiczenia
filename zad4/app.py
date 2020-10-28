import helpers

sequenceLength = int(input("Podaj dlugosc ciagu: "))
sequenceCount = int(input("Podaj ilosc ciagow: "))
sequenceItemRange = int(input("Podaj zakres elementow ciagow: "))

for x in range(sequenceCount):
    sequence = helpers.getRandomSequenceOf(sequenceLength, sequenceItemRange)
    helpers.printMostCommonElementMessage(sequence)
    print('\n')

