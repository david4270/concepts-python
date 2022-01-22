
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
        print("Product name: "+ self.name + "\n    Processor: " + self.proc + "\n    RAM:" + str(self.ram) + "GB \n   "+" Storage: " + str(self.storage) + "GB\n   "
             + " Display Type: "+self.display["Type"] + "\n    Display Size: " + str(self.display["Size"]) +"\n    OS: " + self.osType)

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
        print("Display Type: "+self.display["Type"] + "\n   Display Size: " + str(self.display["Size"]))
        return self.display
    
    def getOSType(self):
        print(self.osType)
        return self.osType
    

# Galaxy class - child of Phone - OS version, serial ID, ONE UI version, KNOX counter, stylus support, dual SIM support
class Galaxy(Phone):
    def __init__(self, name, proc, ram, storage, display, osType, OSversion, serialID, OneUIversion, KNOXctr, SPen, dualSIM):
        super(Galaxy,self).__init__(name, proc, ram, storage, display, osType)
        self.OSversion = OSversion
        self.serialID = serialID
        self.OneUIversion = OneUIversion
        self.KNOXctr = KNOXctr
        self.SPen = SPen
        self.dualSIM = dualSIM
    
    def getDetails(self):
        Phone.getDetails(self)
        print("    OS version: "+str(self.OSversion)+"\n    SERIAL ID: " + self.serialID + "\n    One UI version: " + str(self.OneUIversion)
                + "\n    KNOX Counter: " + str(self.KNOXctr) + "\n    S Pen support: " + str(self.SPen) + "\n    Dual SIM support: " + str(self.dualSIM))
    
    def getOSversion(self):
        print(self.OSversion)
        return self.OSversion
    
    def getSerialID(self):
        print(self.serialID)
        return self.serialID
    
    def getOneUIversion(self):
        print(self.OneUIversion)
        return self.OneUIversion

    def getKNOXctr(self):
        print(self.KNOXctr)
        return self.KNOXctr
    
    def getSPen(self):
        print(self.SPen)
        return self.SPen

    def getDualSIM(self):
        print(self.dualSIM)
        return self.dualSIM


# iPhone class - child of Phone - OS version, serial ID, jailbroken
class IPhone(Phone):
    def __init__(self, name, proc, ram, storage, display, osType, OSversion, serialID, jailbroken):
        super(IPhone,self).__init__(name, proc, ram, storage, display, osType)
        self.OSversion = OSversion
        self.serialID = serialID
        self.jailbroken = jailbroken
    
    def getDetails(self):
        Phone.getDetails(self)
        print("    OS version: "+str(self.OSversion)+"\n    SERIAL ID: " + self.serialID + "\n    Jailbroken: " + str(self.jailbroken))
    
    def getOSversion(self):
        print(self.OSversion)
        return self.OSversion
    
    def getSerialID(self):
        print(self.serialID)
        return self.serialID
    
    def getJailbroken(self):
        print(self.jailbroken)
        return self.jailbroken


# Pixel class - child of Phone - OS version, Android build number, serial ID
class Pixel(Phone):
    def __init__(self, name, proc, ram, storage, display, osType, OSversion, buildNumber, serialID):
        super(Pixel,self).__init__(name, proc, ram, storage, display, osType)
        self.OSversion = OSversion
        self.buildNumber = buildNumber
        self.serialID = serialID
    
    def getDetails(self):
        Phone.getDetails(self)
        print("    OS version: "+str(self.OSversion)+"\n    Build Number: " + self.buildNumber+"\n    SERIAL ID: " + self.serialID)
    
    def getOSversion(self):
        print(self.OSversion)
        return self.OSversion
    
    def getBuildNumber(self):
        print(self.buildNumber)
        return self.buildNumber

    def getSerialID(self):
        print(self.serialID)
        return self.serialID


# Xiaomi class - child of Phone - OS version, serial ID, MIUI version, dual SIM support
class Xiaomi(Phone):
    def __init__(self, name, proc, ram, storage, display, osType, OSversion, serialID, MIUIversion, dualSIM):
        super(Xiaomi,self).__init__(name, proc, ram, storage, display, osType)
        self.OSversion = OSversion
        self.serialID = serialID
        self.MIUIversion = MIUIversion
        self.dualSIM = dualSIM
    
    def getDetails(self):
        Phone.getDetails(self)
        print("    OS version: "+str(self.OSversion)+"\n    SERIAL ID: " + self.serialID  
            + "\n    MIUI version: " + str(self.MIUIversion) + "\n    Dual SIM support: " + str(self.dualSIM))
    
    def getOSversion(self):
        print(self.OSversion)
        return self.OSversion
    
    def getSerialID(self):
        print(self.serialID)
        return self.serialID
    
    def getMIUIversion(self):
        print(self.MIUIversion)
        return self.MIUIversion

    def getDualSIM(self):
        print(self.dualSIM)
        return self.dualSIM

# Motorola class - child of Phone - OS version, serial ID, dual SIM support
class Moto(Phone):
    def __init__(self, name, proc, ram, storage, display, osType, OSversion, serialID, dualSIM):
        super(Moto,self).__init__(name, proc, ram, storage, display, osType)
        self.OSversion = OSversion
        self.serialID = serialID
        self.dualSIM = dualSIM
    
    def getDetails(self):
        Phone.getDetails(self)
        print("    OS version: "+str(self.OSversion)+"\n    SERIAL ID: " + self.serialID + "\n    Dual SIM support: " + str(self.dualSIM))
    
    def getOSversion(self):
        print(self.OSversion)
        return self.OSversion
    
    def getSerialID(self):
        print(self.serialID)
        return self.serialID
    
    def getDualSIM(self):
        print(self.dualSIM)
        return self.dualSIM

# etc class - child of Phone - OS version, serial ID
class Others(Phone):
    def __init__(self, name, proc, ram, storage, display, osType, OSversion, serialID):
        super(Others,self).__init__(name, proc, ram, storage, display, osType)
        self.OSversion = OSversion
        self.serialID = serialID
    
    def getDetails(self):
        Phone.getDetails(self)
        print("    OS version: "+str(self.OSversion)+"\n    SERIAL ID: " + self.serialID)
    
    def getOSversion(self):
        print(self.OSversion)
        return self.OSversion
    
    def getSerialID(self):
        print(self.serialID)
        return self.serialID
