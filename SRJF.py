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
    arrivalTimeList = [4,7,0,0,16]
    burstTimeList = [9,2,4,3,7]

    for i in range(5):
        temp = Process(names[i],arrivalTimeList[i],burstTimeList[i])
        allProcess.append(temp)

    temp = allProcess.copy()

    que = []
    outPut = []
    curTime = 0

    min = 0
    index = 0
    while len(temp) > 0 or len(que) > 0:

        if(len(temp) != 0):
            for i in range(len(allProcess)):
                if curTime == allProcess[i].arrivalTime:
                    que.append(allProcess[i])
                    del(temp[0])
                    min = que[0].burstTime
                    index = 0
                    for j in range(1, len(que)):
                        if min > que[j].burstTime:
                            min = que[j].burstTime
                            index = j

        #print('Current Time ' + str(curTime) + ' index is ' + str(index) + ' Process is '+ que[index].name + ' Burst Time is '+ str(que[index].burstTime))
        if len(que) > 0:
            if que[index].burstTime != 0:
                que[index].burstTime -= 1
            if que[index].burstTime == 0:
                outPut.append(que[index])
                del(que[index])
                if(len(que) > 0):
                    min = que[0].burstTime
                    index = 0
                    for i in range(1,len(que)):
                        if min > que[i].burstTime:
                            min = que[i].burstTime
                            index = i

        curTime += 1


    print('Current Time Graph ' + str(curTime))

    for i in range(len(outPut)):
        print (outPut[i].name)

    print("End Of the Program.\n")

if __name__ == '__main__':
    main()