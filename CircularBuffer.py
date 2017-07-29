class CB:
    buff = []
    writeptr = 0
    readptr = 0
    def __init__(self, size):
        self.buff = [0 for i in range(size)]
    def checkptr(self):
        if self.writeptr > len(self.buff)-1:
            self.writeptr = 0
        if self.readptr > len(self.buff)-1:
            self.readptr = 0
    def write(self, val):
        self.buff[self.writeptr] = val
        self.writeptr += 1
        self.checkptr()
    def read(self):
        if self.readptr != self.writeptr:
            val = self.buff[self.readptr]
            self.readptr += 1
            self.checkptr()
            return val
        else:
            return None
    def debug(self):
        print('write pointer: ' + str(self.writeptr))
        print('read pointer: ' + str(self.readptr))
        print(self.buff)

test = CB(3) #initiate the buffer

[test.write(1) for i in range(2)] #write two things to the buffer
test.debug() #print buffer status
[print(test.read()) for i in range(3)] #try reading 3 values
#As you will see, the buffer will return none due to the read pointer matching the write pointer
test.debug() #print buffer status
