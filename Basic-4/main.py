# Object Oriented Concepts

#https://docs.python.org/3/tutorial/modules.html
import helper

def main():

    setGalaxy = []
    setiPhone = []
    setPixel = []
    setXiaomi = []
    setMoto = []
    setOthers = []

    while(1):
        print("Type number - 1: Add phone info 2: Search phone info 3: Print whole product set 4: Delete phone info")
        print("Press any other key to discontinue")
        op = input()

        if(op == "1"):

            print("Enter your phone brand: ")
            brand = input()

            #Common input
            print("What's your phone's name?")
            name = input()
            print("What's your phone's processor?")
            proc = input()
            print("How many GB's of RAM does your phone have?")
            ram = input()
            print("How many GB's of storage does your phone have?")
            storage = input()
            print("Which type of display does your phone use?")
            typeDisplay = input()
            print("How big is your phone's screen (in inches)?")
            sizeDisplay = input()
            displayInfo = {"Type":typeDisplay,"Size":sizeDisplay}
            print("Which operating system does your phone use?")
            osType = input()

            if(brand.lower() == "galaxy"):
                print("Which OS version are you using?")
                OSversion = input()
                print("What is your phone's serial ID?")
                serialID = input()
                print("What is your phone's One UI version?")
                OneUIversion = input()
                print("If your phone's warranty is void, type 1. Otherwise type 0")
                KNOXctr = input()
                print("If your phone supports S Pen, type 1. Otherwise type 0")
                SPen = input()
                print("If your phone supports Dual SIM, type 1. Otherwise type 0")
                dualSIM = input()
                GalaxyPhone = helper.Galaxy(name,proc,ram,storage,displayInfo,osType,OSversion,serialID,OneUIversion,KNOXctr,SPen,dualSIM)
                setGalaxy.append(GalaxyPhone)
            elif(brand.lower() == "iphone"):
                print("Which OS version are you using?")
                OSversion = input()
                print("What is your phone's serial ID?")
                serialID = input()
                print("If your phone is jailbroken, type 1. Otherwise type 0")
                jailbroken = input()
                iPhone = helper.IPhone(name,proc,ram,storage,displayInfo,osType,OSversion,serialID,jailbroken)
                setiPhone.append(iPhone)
            elif(brand.lower() == "pixel"):
                print("Which OS version are you using?")
                OSversion = input()
                print("Which build version is installed on your phone?")
                buildNumber = input()
                print("What is your phone's serial ID?")
                serialID = input()
                pixel = helper.Pixel(name,proc,ram,storage,displayInfo,osType,OSversion,buildNumber,serialID)
                setPixel.append(pixel)
            elif(brand.lower() == "xiaomi" or brand.lower() == "redmi"):
                print("Which OS version are you using?")
                OSversion = input()
                print("What is your phone's serial ID?")
                serialID = input()
                print("What is your phone's MIUI version?")
                MIUIversion = input()
                print("If your phone supports Dual SIM, type 1. Otherwise type 0")
                dualSIM = input()
                xiaomi = helper.Xiaomi(name,proc,ram,storage,displayInfo,osType,OSversion,serialID,MIUIversion,dualSIM)
                setXiaomi.append(xiaomi)
            elif(brand.lower() == "moto"):
                print("Which OS version are you using?")
                OSversion = input()
                print("What is your phone's serial ID?")
                serialID = input()
                print("If your phone supports Dual SIM, type 1. Otherwise type 0")
                dualSIM = input()
                moto = helper.Moto(name,proc,ram,storage,displayInfo,osType,OSversion,serialID,dualSIM)
                setMoto.append(moto)
            else:
                print("Which OS version are you using?")
                OSversion = input()
                print("What is your phone's serial ID?")
                serialID = input()
                other = helper.Xiaomi(name,proc,ram,storage,displayInfo,osType,OSversion,serialID)
                setOthers.append(other)
        
        elif(op=="2"):
            print("Which model do you want to search?")
            name = input()
            if("galaxy" in name.lower()):
                for gl in setGalaxy:
                    if(gl.name == name):
                        gl.getDetails()
            elif("iphone" in name.lower()):
                for ip in setiPhone:
                    if(ip.name == name):
                        ip.getDetails()
            elif("pixel" in name.lower()):
                for px in setPixel:
                    if(px.name == name):
                        px.getDetails()
            elif("mi" in name.lower()):
                for mi in setXiaomi:
                    if(mi.name == name):
                        mi.getDetails()
            elif("moto" in name.lower()):
                for mt in setMoto:
                    if(mt.name == name):
                        mt.getDetails()
            else:
                for ot in setOthers:
                    if(ot.name == name):
                        ot.getDetails()
        elif(op=="3"):
            print("Which product lineup would you want to see?")
            name = input()
            if("galaxy" in name.lower()):
                for gl in setGalaxy:
                    gl.getDetails()
                    print()
            elif("iphone" in name.lower()):
                for ip in setiPhone:
                    ip.getDetails()
                    print()
            elif("pixel" in name.lower()):
                for px in setPixel:
                    px.getDetails()
                    print()
            elif("mi" in name.lower()):
                for mi in setXiaomi:
                    mi.getDetails()
                    print()
            elif("moto" in name.lower()):
                for mt in setMoto:
                    mt.getDetails()
                    print()
            else:
                for ot in setOthers:
                    ot.getDetails()
                    print()
        elif(op=="4"):
            print("Which model do you want to delete?")
            name = input()
            if("galaxy" in name.lower()):
                for gl in setGalaxy:
                    if(gl.name == name):
                        setGalaxy.remove(gl)
            elif("iphone" in name.lower()):
                for ip in setiPhone:
                    if(ip.name == name):
                        setiPhone.remove(ip)
            elif("pixel" in name.lower()):
                for px in setPixel:
                    if(px.name == name):
                        setPixel.remove(px)
            elif("mi" in name.lower()):
                for mi in setXiaomi:
                    if(mi.name == name):
                        setXiaomi.remove(mi)
            elif("moto" in name.lower()):
                for mt in setMoto:
                    if(mt.name == name):
                        setMoto.remove(mt)
            else:
                for ot in setOthers:
                    if(ot.name == name):
                        setOthers.remove(ot)
        else:
            del setGalaxy
            del setiPhone
            del setPixel
            del setXiaomi
            del setMoto
            del setOthers
            return
    

    """
    GalaxyNote10plus = helper.Galaxy("Galaxy Note 10+","Samsung Exynos 9825",12,256,{"Type":"AMOLED","Size": 6.8},"Android",12,"434236324643",4.0,0,1,1)
    GalaxyNote10plus.getDetails()
    print()
    GalaxyNote10plus.getOneUIversion()
    GalaxyNote10plus.getName()
    print()

    Pixel6 = helper.Pixel("Pixel 6","Google Tensor (Samsung Exynos 9845)",8,128,{"Type":"AMOLED","Size": 6.4},"Android",12,"SQ1D","543743233")
    Pixel6.getDetails()
    print()
    Pixel6.getBuildNumber()
    Pixel6.getOSType()
    print()

    Iphone12mini = helper.IPhone("iPhone 12 mini","Apple A14",4,64,{"Type":"AMOLED","Size": 5.4},"iOS",15.3,"89043250548",0)
    Iphone12mini.getDetails()
    print()
    Iphone12mini.getJailbroken()
    Iphone12mini.getProc()
    print()
    """
    # ADD LOOP and INPUT

if __name__ == "__main__":
    main()

#Private or protected? We don't do that here (in python). Go C++ if you want such stuff.