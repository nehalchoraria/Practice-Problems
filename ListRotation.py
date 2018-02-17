def rotatelist(listt,no_of_times):
    no_of_times = no_of_times % len(listt)
    listlength = len(listt)

    for i in range(no_of_times):
        for l in range(listlength-1,0,-1):
            temp = listt[l]
            listt[l] = listt[(l-1)%listlength]
            listt[(l-1)%listlength] = temp
    return listt
	
rotatelist([1,2,3,4,5],12)
    