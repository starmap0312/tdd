''' - to flatten list of lists:
      ex. listOfLists = [[1, 2], [3, 4, 5]]  ==> [1, 2, 3, 4, 5]
          flattened = [item for sublist in listOfLists for item in sublist]
'''

class StringCalculator(object):

    @staticmethod
    def add(numString):
        returnValue = 0
        listOfLists = [t.split(",") for t in numString.splitlines()]
        numbers = [item for sublist in listOfLists for item in sublist]
        for num in numbers:
            if num != "":
                numInt = int(num)
                if numInt < 0:
                    raise RuntimeError
                elif numInt <= 1000:
                    returnValue += numInt
        return returnValue
