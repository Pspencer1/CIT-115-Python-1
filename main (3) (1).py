def getDataInput():
    lstRecordsBLC = []
    file = open("RealEstateData.csv", "r")

    firstLine = True
    for line in file:
        if firstLine:
            firstLine = False
            continue

        lstRecordsBLC.append(line.strip())

    file.close()
    return lstRecordsBLC


def getMedian(lstValuesBLC):
    lstValuesBLC.sort()
    intLenBLC = len(lstValuesBLC)

    if intLenBLC % 2 == 1:
        return lstValuesBLC[intLenBLC // 2]
    else:
        mid1 = lstValuesBLC[intLenBLC // 2]
        mid2 = lstValuesBLC[intLenBLC // 2 - 1]
        return (mid1 + mid2) / 2
    

def main():
    lstRecordsBLC = getDataInput()
    lstPricesBLC = []
    dictCityBLC = {}
    dictZipBLC = {}
    dictTypeBLC = {}
       
    for record in lstRecordsBLC:
        if record.strip() == "":
            continue

        fields = record.split(",")   

        strCityBLC = fields[1]
        strZipBLC = fields[2]
        strTypeBLC = fields[7]
        fltPriceBLC = float(fields[8])

        lstPricesBLC.append(fltPriceBLC)

        if strCityBLC in dictCityBLC:
            dictCityBLC[strCityBLC] += fltPriceBLC
        else:
            dictCityBLC[strCityBLC] = fltPriceBLC

        if strZipBLC in dictZipBLC:
            dictZipBLC[strZipBLC] += fltPriceBLC
        else:
            dictZipBLC[strZipBLC] = fltPriceBLC

        if strTypeBLC in dictTypeBLC:
            dictTypeBLC[strTypeBLC] += fltPriceBLC
        else:
            dictTypeBLC[strTypeBLC] = fltPriceBLC

    lstPricesBLC.sort()

    fltMinBLC = lstPricesBLC[0]
    fltMaxBLC = lstPricesBLC[-1]
    fltTotalBLC = sum(lstPricesBLC)
    fltAvgBLC = fltTotalBLC / len(lstPricesBLC)
    fltMedianBLC = getMedian(lstPricesBLC)
   
    print(f"Min: ${fltMinBLC:.2f}")
    print(f"Max: ${fltMaxBLC:.2f}")
    print(f"Total: ${fltTotalBLC:.2f}")
    print(f"Average: ${fltAvgBLC:.2f}")
    print(f"Median: ${fltMedianBLC:.2f}")

    print("\nCity Totals:")
    for city in dictCityBLC:
        print(city, f"${dictCityBLC[city]:.2f}")

    print("\nZip Totals:")
    for zipCode in dictZipBLC:
        print(zipCode, f"${dictZipBLC[zipCode]:.2f}")

    print("\nProperty Type Totals:")
    for ptype in dictTypeBLC:
        print(ptype, f"${dictTypeBLC[ptype]:.2f}")


main()