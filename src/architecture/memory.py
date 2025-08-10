class Memory:
    RAM_SIZE = 64 * 1024
    data = bytearray(RAM_SIZE)
    
    def reset(self):
        self.data = bytearray(self.RAM_SIZE)
    
    def _check_address(self, address):
        if not(0 <= address <= self.RAM_SIZE):
            raise ValueError(f"Invalid memory address: {address}, (max {self.RAM_SIZE - 1})")
        
    def _check_byte(self, data):
        if not(0 <= data <= 255):
            raise ValueError(f"Invalid data: {data}, (data must be between 0 and 255)")        
    
    def _check_word(self, data):
        if not(0 <= data <= (2**32 - 1)):
            raise ValueError(f"Invalid data: {data} (data must be between 0 and 4294967295)")
    
    def read_byte(self, address):
        self._check_address(address)
        return self.data[address]
    
    def write_byte(self, address, data):
        self._check_address(address)
        self._check_byte(data)
        self.data[address] = data
        
    def read_word(self, address):
        self._check_address(address)
        byte_array = [self.read_byte(address + i) for i in range(4)]
        data = int.from_bytes(byte_array, byteorder="big", signed=False)
        
    def write_word(self, address, data):
        self._check_address(address)
        self._check_word(data)
        byte_array = data.to_bytes(4, byteorder="big", signed=False)
        for i, b in enumerate(byte_array):
            self.write_byte(address + i, b)