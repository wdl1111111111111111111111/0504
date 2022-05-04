while True:
    try:
        n = int(input())
        for i in range(n):
            each_name = input()
            beauty = 0
            
            # 字典放名字中每种字母对应出现到次数
            dict1 = {}
            for c in each_name:
                dict1[c] = each_name.count(c)
                
            # 每种字母的出现次数从大到小排列
            times_list = sorted(dict1.values(), reverse=True)
            
            # 次数从大到小以此乘以26,25,24...
            for j in range(len(times_list)):
                beauty += (26 - j) * times_list[j]
            print(beauty)
        
    except:
        break