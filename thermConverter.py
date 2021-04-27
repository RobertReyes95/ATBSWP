
ferh = (input("Enter F for Fernghit to Celcius Converter or enter C for celcius to fernhaite converter: "))

if ferh == "F": 
    fN = input("Please enter the tempeture you wish to convert: ")
    one = int(fN) - 32
    two = one / 1.8
    finalC = round(two, 1)
    results = str(fN) + " degrees fernheit converts to  " + str(finalC) + "c"
    print(results)
elif ferh == "C":
    cN = input("Please enter theF tempeture you wish to convert: ")
    div = int(cN) * 9/5
    plus = int(div) + 32
    resultsC = str(cN) + " degrees celcius converts to " + str(plus) + "F"
    print(resultsC)

