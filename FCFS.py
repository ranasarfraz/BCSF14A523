from builtins import all


class Process:
    name = ''
    arrivalTime = 0
    burstTime = 0

    def __init__(self, name, arrivalTime , burstTime):
        self.name = name
        self.arrivalTime = arrivalTime
        self.burstTime = burstTime

def main():
    allProcess = []

    names = ['p1','p2','p3','p4','p5']
    arrivalTimeList = [9,0,2,0,3]
    burstTimeList = [5,4,7,3,7]

    for i in range(5):
        temp = Process(names[i],arrivalTimeList[i],burstTimeList[i])
        allProcess.append(temp)

    temp = allProcess.copy()

    que = []
    outPut = []
    curTime = 0


    while len(temp) > 0 or len(que) > 0:

        if(len(temp) != 0):
            for i in range(len(allProcess)):
                #print(i)
                if curTime == allProcess[i].arrivalTime:
                    outPut.append(allProcess[i])
                    que.append(allProcess[i])

                    del(temp[0])


        if len(que) > 0:
            if que[0].burstTime != 0:
                que[0].burstTime -= 1
            if que[0].burstTime == 0:
                del(que[0])
        curTime += 1


    print('Current Time Graph ' + str(curTime))

    for i in range(len(outPut)):
        print (outPut[i].name)

    print("End Of the Program.\n")

if __name__ == '__main__':
    main()