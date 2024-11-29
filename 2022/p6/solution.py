class Marker:
    def __init__(self):
        self.signals= []
    def add_signal(self, signal):
        if len(self.signals) == 14:
            if len(self.signals) == len(set(self.signals)):
                print("Marker is valid")
                print("Marker signals are: ", self.signals)
                return True
            self.signals.remove(self.signals[0]) # remove the first element
            self.signals.append(signal)
            return False
        self.signals.append(signal)
        return False

with open('p6-input.txt') as f:
    for line in f:
        line = line.strip()
        signals = Marker() 
        counter = 0
        for c in line:
           unique = signals.add_signal(c) 
           if unique:
                print(counter, c)
                break
           counter += 1