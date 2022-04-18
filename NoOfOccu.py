class NoOfOccu():


    input_list = ["Alaska", "Alabama", "Arizona", "Arkansas", "Colorado", "Montana", "Nevada"]
   # s=sum(map(lambda x: x[0] == 'A', input_list))
    c = 0
    for i in input_list:

        count = sum(map(lambda x: 1 if 'a' in x else 0, i))
        count1 = sum(map(lambda x: 1 if 'A' in x else 0, i))
           # v=sum(map(lambda x: x[s] == 'a', input_list))
        #print count
        c=count+count1
        print (i+" -",c)


  #countt=countofval();
  #print(countt)
