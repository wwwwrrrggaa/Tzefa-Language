# Press the green button in the gutter to run the script.
import ErrorCorrection
import topy


if __name__ == '__main__':
    textlist = [
    "MAKEINTEGER INTEGERONE 96",
    "MAKEINTEGER INTEGERTWO 144",
    "MAKEINTEGER TEMPTWO 0",
    "MAKEINTEGER ZERO 0",
    "BASICCONDITION GCDCOMPARE BIGGER",
    "LEFESIDE GCDCOMPARE INTEGERTWO",
    "RIGHTSIDE GCDCOMPARE ZERO",
    "WHILE GCDCOMPARE 11",
    "MODULU INTEGERONE INTEGERTWO",
    "ASSIGNINT INTEGERONE INTEGERTWO",
    "ASSIGNINT INTGERTWO TEMPORARY"

    ]
    listofindentchanges = [0] * (len(textlist) + 1)
    firstword=[ErrorCorrection.handelfirstword(textlist[i].split(" ")[0])[1] for i in range(len(textlist))]
    linelist = [ErrorCorrection.toline(textlist[i],firstword[i],listofindentchanges) for i in range(len(textlist))]
    topy.makepyfile(linelist)
    import test