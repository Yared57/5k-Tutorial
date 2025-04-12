if __name__ == '__main__':
    number=int(input())
    data=[[0,0]for i in range(number)]
    scores=[]
    newscore=[]
  
    #print(data)
    for i in range(number):
        data[i][0] = input()
        data[i][1] = float(input())
        scores.append(data[i][1])
    
    score=list(set(scores))
    score.sort()
    
    score.remove(score[0])
    
    

    for i in range(len(data)):
        if score[0] == data[i][1]:
            newscore.append(data[i][0])
         
    newscore.sort()
    for i in newscore:
        print(i)
           
