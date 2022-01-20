# Object Oriented Concepts

#https://docs.python.org/3/tutorial/modules.html
import helper

def main():

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

    # ADD LOOP and INPUT

if __name__ == "__main__":
    main()

#Private or protected? We don't do that here (in python). Go C++ if you want such stuff.