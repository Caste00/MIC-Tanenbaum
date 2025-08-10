from memory import Memory

class Cpu:
    ILOAD = 0x15
    ISTORE = 0x36
    
    def __init__(self):
        self.memory = Memory()
        self.mar = 0
        self.mdr = 0
        self.pc = 0
        self.mbr = 0
        self.mbru = 0
        self.sp = self.memory.RAM_SIZE - 1
        self.lv = 0
        self.cpp = 0
        self.tos = 0 
        self.opc = 0
        self.h = 0
        self.z = 0
        self.n = 0
        
    def reset(self):
        self.memory.reset()
        self.mar = 0
        self.mdr = 0
        self.pc = 0
        self.mbr = 0
        self.mbru = 0
        self.sp = self.memory.RAM_SIZE - 1
        self.lv = 0
        self.cpp = 0
        self.tos = 0 
        self.opc = 0
        self.h = 0
        self.z = 0
        self.n = 0
        
    def fetch_byte(self):
        self.mar = self.pc
        self.mbr = self.memory.read_byte(self.mar)
        self.pc += 1
        
    def fetch_word(self):
        self.mar = self.pc
        byte_array = [self.memory.read_byte(self.mar + i) for i in range(4)]
        self.pc += 4
        self.mdr = int.from_bytes(byte_array, byteorder='big', signed=False)
        
    def execute(self, max_cycle): 
        cycle_use = 0
        while cycle_use < max_cycle:
            # fetch next instruction (MAIN1)  
            self.fetch_byte()
            opcode = self.mbr            
            cycle_use += 1
            
            match opcode:
                case self.ILOAD:    
                    self.h = self.lv
                    self.mar = self.mbru + self.h
                    self.mdr = self.memory.read_word(self.mar)
                    self.sp += 1
                    self.memory.write_word(self.mar, self.mdr)
                    
                    cycle -= 4
                    
                    # cycle -= numero di cicli per iload