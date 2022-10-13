import fetch_data

class Logic:
    def __init__(self):
        self.data = fetch_data.getData()
        self.output_list = []

        for i in range(self.getLength()):
            self.output_list.append('_')

        self.display_output = ''
    
    def getCountry(self):
        '''Return the country'''
        return self.data[1]

    def getCapital(self):
        '''Return the capital'''
        return self.data[2]

    def checkStatus(self):
        '''Check if the blanks have been filled'''
        if '_' in self.output_list:
            return True
        else:
            return False

    def getLength(self):
        '''Returns the length of the capital name'''
        return (len(self.getCapital()))

    def initialOutput(self):
        '''create the initial input of dashes'''
        self.display_output = ''.join(self.output_list)

    def capitalList(self):
        '''split the capital name into a list'''
        capital_list = []
        for i in self.getCapital():
            capital_list.append(i.lower())
        return capital_list

    def checkInput(self, letter):
        '''Check if user input letter is in capital and return index'''
        self.letter = letter
        if self.letter in self.capitalList():
            index = []
            idx = 0
            for i in self.capitalList():
                if self.letter == i:
                    index.append(idx)
                idx += 1
            return index

        else:
            return False

    def insertLetter(self):
        '''add the letter at its position'''
        for i in self.checkInput(self.letter):
            self.output_list[i] = self.letter

        self.display_output = ''.join(self.output_list)

ins = Logic()
print(ins.getCapital())