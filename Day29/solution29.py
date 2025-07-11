def middle_figure(strA,strB):
    strC=(strA+strB).replace(" ","")
    middle=int(len(strC)/2)

    #print(strC[middle])
    if len(strC) % 2 != 0:
        return strC[middle]
    else:
        return "no middle figure"

print(middle_figure("abc","def"))
print(middle_figure('make love', 'not wars') )
