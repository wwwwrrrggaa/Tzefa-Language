# Press the green button in the gutter to run the script.
import ErrorCorrection


if __name__ == '__main__':
    textlist = [
    "MAKEINTEGER INTEGERONE 96",
    "MAKEINTEGER INTEGERTWO 144",
    "MAKEINTEGER TEMPTWO 0",
    "MAKEINTEGER ZERO 0",
    "NEWLIST GCDLIST 0",
    "BASICCONDITION GCDCOMPARE BIGGER",
    "LEFESIDE GCDCOMPARE INTEGERTWO",
    "RIGHTSIDE GCDCOMPARE ZERO",
    "LISTFUNCTION GCD GCBLIST",
    "MODULU INTEGERONE INTEGERTWO",
    "ASSIGNINT INTEGERONE INTEGERTWO",
    "ASSIGNINT INTGERTWO TEMPORARY",
    "IFTRUE GCDCOMPARE 12",
    "GCD GCDLIST GCDLIST"


    ]
    listofindentchanges = [0] * (len(textlist) + 1)
    #firstword=[ErrorCorrection.handelfirstword(textlist[i].split(" ")[0])[1] for i in range(len(textlist))]
    #linelist = [ErrorCorrection.toline(textlist[i],firstword[i],listofindentchanges) for i in range(len(textlist))]
    compiledlinelist=[ErrorCorrection.toline
                      (textlist[lineindex],ErrorCorrection.handelfirstword(textlist[lineindex].split(" ")[0])[1],listofindentchanges)
                      for lineindex in range(len(textlist))]
    import topy
    topy.makepyfile(compiledlinelist)
    import test