from builtins import all


class Process:
    name = ''
    arrivalTime = 0
    burstTime = 0
    periority = 0
    def __init__(self, name, arrivalTime , burstTime, periority):
        self.name = name
        self.arrivalTime = arrivalTime
        self.burstTime = burstTime
        self.periority = periority

def main():
    allProcess = []

    names = ['p1','p2','p3','p4','p5']
    arrivalTimeList = [2,4,0,3,0]
    burstTimeList = [6,8,7,3,7]
    peroirityList = [4,1,3,2,5]

    for i in range(5):
        temp = Process(names[i],arrivalTimeList[i],burstTimeList[i], peroirityList[i])
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
                if len(outPut) == 0 and len(que) != 0:
                    min = que[0].periority
                    index = 0
                    for j in range(1,len(que)):
                        if min > que[j].periority:
                            min = que[j].periority
                            index = j
        print('Current Time ' + str(curTime) + ' index is ' + str(index) + ' Process is '+ que[index].name + ' Burst Time is '+ str(que[index].burstTime ) + ' Periority is '+ str(que[index].periority))
        if len(que) > 0:
            if que[index].burstTime != 0:
                que[index].burstTime -= 1
            if que[index].burstTime == 0:
                outPut.append(que[index])
                del(que[index])
                if(len(que) > 0):
                    min = que[0].periority
                    index = 0
                    for i in range(1,len(que)):
                        if min > que[i].periority:
                            min = que[i].periority
                            index = i

        curTime += 1


    print('Current Time Graph ' + str(curTime))

    for i in range(len(outPut)):
        print (outPut[i].name)

    print("End Of the Program.\n")

if __name__ == '__main__':
    main()