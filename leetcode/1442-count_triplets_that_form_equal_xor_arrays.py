def countTriplets(arr):

    lst = []
    i, j, k = 0, 1, 1
    b = arr[j]
    a = arr[i]
    while k < len(arr):

        if a == b:
            lst.append((i, j, k))

        if k < len(arr) - 1:
            k += 1
            b ^= arr[k]
        elif j < len(arr) - 1:
            j += 1
            k = j
            a ^= arr[j-1]
            b = arr[j]
        elif i < len(arr) - 1:
            i += 1
            j, k = i+1, i+1
            a, b = arr[i], arr[min(j, len(arr)-1)]

    return lst

def countTripletsNaive(arr):
    lst = []
    i, j, k = 0, 1, 1
    while k < len(arr):
        a = arr[i]
        i_tmp = i + 1
        while i_tmp < j:
            a = a ^ arr[i_tmp]
            i_tmp += 1
        
        b = arr[j]
        j_tmp = j + 1
        while j_tmp <= k:
            b = b ^ arr[j_tmp]
            j_tmp += 1

        if a == b:
            lst.append((i, j, k))

        if k < len(arr) - 1:
            k += 1
        elif j < len(arr) - 1:
            j += 1
            k = j
        else:
            i += 1
            j, k = i+1, i+1

    return len(lst)

print(countTriplets(arr = [1]))
print(countTriplets(arr = [2,3,1,6,7]))
print(countTriplets(arr = [723,875,440,136,304,271,63,294,281,169,432,185,265,758,1023,760,263,13,266,458,192,774,966,855,145,115,226,233,11,710,717,281,980,386,598,564,98,604,574,717,243,309,454,676,866,944,210,301,511,700,835,696,507,794,737,999,262,36,290,981,759,52,707,734,29,273,268,853,601,293,892,66,830,145,943,959,16,989,973,609,428,289,141,985,852,974,154,522,656,894,494,520,998,934,64,967,903,708,323,927,732,878,434,972,638,550,88,805,893,514,383,686,977,165,884,691,455,39,480,698,858,400,714,230,556,566,26,851,841,240,953,938,19,385,402,931,561,502,967,104,943,948,27,248,227,677,582,541,91,703,740,871,387,788,663,210,581,335,778,514,264,538,786,369,611,349,830,246,968,152,848,471,647,488,879,900,235,726,573,200,757,236,537,420,957,793,164,120,220,276,456,772,716,112,700,40,660,498,870,559,329,411,210,783,989,732,257,988,733,743,58,8,50,266,312,461,245,849,932,758,338,62,364,474,182,680,542,201,727,782,473,567,1006,39,969,575,502,788,738,297,971,499,568]))
