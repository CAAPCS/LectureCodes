
def listSum(myList):
    counter = 0
    for num in myList:
        counter = counter + num

    # num = myList[0] # 1
    # counter = counter + num ||  counter <- 0 + 1
    # num = myList[1] # 2
    # counter = counter + num || counter <- 1 + 2
    # num = myList[2] # 3
    # counter = counter + num || counter <- 3 + 3
    # num = myList[3] # 4
    # counter = counter + num || counter <- 4 + 6

    return counter

# mean -> sum / number of things
def listMean(myList):
    myListTotal = listSum(myList)
    myListMean = myListTotal / len(myList)
    return myListMean

#median is the middle "number" of a sorted list
#if the list size is even then its the average of the two middle things
def listMedian(myList):
    if len(myList) % 2 == 0: # if the length of is divisble by two then do the following:
        sortedMyList = sorted(myList) # sort the list to least to greatest
        middle_index = int((len(sortedMyList) - 1) / 2) # to find the two middle numbers
        median = (sortedMyList[middle_index] + sortedMyList[middle_index + 1]) / 2 # take that middle index and get the two middle numbers
        return median # perfect
    else:
        sortedMyList = sorted(myList)
        middle_index = int((len(sortedMyList) - 1) / 2)
        median = sortedMyList[middle_index]
        return median

def main():
    a = [1, 2, 3, 4, 6, 5, 3, 4, 5,21, 2]


    print(a)
    a_total = listSum(a)
    a_mean = listMean(a)
    a_median = listMedian(a)
    print("total:", a_total)
    print("mean:", a_mean)
    print("median:", a_median)





if __name__ == '__main__':
    main()