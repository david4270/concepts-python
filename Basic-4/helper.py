
# Phone class - name, processor, memory, storage, display size, display tech, operating system

class Phone:
    #Constructor
    def __init__(self, name, proc, ram, storage, display, osType):
        self.name = name
        self.proc = proc
        self.ram = ram
        self.storage = storage
        self.display = display
        self.osType = osType
    
    def getDetails(self):
        print("Product name: "+ self.name + "\n Processor: " + self.proc + "\n RAM:" + str(self.ram) + "GB \n"+" Storage: " + str(self.storage) + "GB\n"
             + " Display Type: "+self.display["Type"] + "\n Display Size: " + str(self.display["Size"]) +"\n OS: " + self.osType)

    def getName(self):
        print(self.name)
        return self.name
    
    def getProc(self):
        print(self.proc)
        return self.proc

    def getRAM(self):
        print(self.ram)
        return self.ram
    
    def getStorage(self):
        print(self.storage)
        return self.storage

    def getDisplay(self):
        print("Display Type: "+self.display["Type"] + "\nDisplay Size: " + str(self.display["Size"]))
        return self.display
    
    def getOSType(self):
        print(self.osType)
        return self.osType
    

# Galaxy class - child of Phone - OS version, serial ID, ONE UI version, KNOX counter, stylus support, dual SIM support


# iPhone class - child of Phone - OS version, serial ID, jailbroken


# Pixel class - child of Phone - OS version, Android build number, serial ID


# Xiaomi class - child of Phone - OS version, serial ID, MIUI version, dual SIM support


# Motorola class - child of Phone - OS version, serial ID, dual SIM support


# etc class - child of Phone - OS version, serial ID

