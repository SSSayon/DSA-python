# digital_circuit

## ----- logicGate -----
class logicGate:
    def __init__(self, label):
        self.label = label
        self.output = None
    def getLabel(self):
        return self.label
    def getOutput(self):
        self.output = self.gen()
        return self.output
    
class BinaryGate(logicGate):
    def __init__(self, label):
        super().__init__(label)
        self.pinA = None
        self.pinB = None
    def getPinA(self):
        if self.pinA == None:
            return int(input("pinA for {}: ".format(self.label)))
        else:
            return self.pinA.getFrom().getOutput()
    def getPinB(self):
        if self.pinB == None:
            return int(input("pinB for {}: ".format(self.label)))
        else:
            return self.pinB.getFrom().getOutput()
    def setPin(self, connector):
        if self.pinA == None:
            self.pinA = connector
        elif self.pinB == None:
            self.pinB = connector
        else:
            raise RuntimeError("ERROR: No available pins for {}!".format(self.label))

class UnaryGate(logicGate):
    def __init__(self, label):
        super().__init__(label)
        self.pin = None
    def getPin(self):
        if self.pin == None:
            return int(input("pin for {}: ".format(self.label)))
        else:
            return self.pin.getFrom().getOutput()
    def setPin(self, connector):
        if self.pin == None:
            self.pin = connector
        else:
            raise RuntimeError("ERROR: No available pins for {}!".format(self.label))

class AndGate(BinaryGate):
    def gen(self):
      A = self.getPinA()
      B = self.getPinB()
      if A == 1 and B == 1:
          return 1
      else:
          return 0
    
class OrGate(BinaryGate):
    def gen(self):
        A = self.getPinA()
        B = self.getPinB()
        if A == 1 or B == 1:
            return 1
        else:
            return 0
        
class NotGate(UnaryGate):
    def gen(self):
        P = self.getPin()
        return 1 - P

## ----- Connector -----
class Connector:
    def __init__(self, from_gate, to_gate):
        self.from_gate = from_gate
        self.to_gate = to_gate
        to_gate.setPin(self)
    def getFrom(self):
        return self.from_gate
    def getTo(self):
        return self.to_gate
     
