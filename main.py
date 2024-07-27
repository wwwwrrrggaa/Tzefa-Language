# Press the green button in the gutter to run the script.
import ErrorCorrection
import topy


if __name__ == '__main__':
    textlist = [
        "MAKEINTEGER NUIMY 743",
        "MAKEINTEGER NUKMY 13",



    ]
    #textlist=[str([i[0],i[2],i[1]]) for i in textlist]
    linelist = [ErrorCorrection.toline(textlist[i],ErrorCorrection.handelfirstword(textlist[i].split(" ")[0])[1]) for i in range(len(textlist))]
    print(linelist)
    topy.makepyfile(linelist)
    import test