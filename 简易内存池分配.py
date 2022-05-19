'''
有一个简易内存池，内存按照大小粒度分类，每个粒度有若干个可用内存资源，用户会进行一系列内存申请
需要按需分配内存池中的资源，返回申请结果成功失败列表。
分配规则如下
1.分配的内存要大于等于内存的申请量，存在满足需求的内存就必须分配，优先分配粒度小的，但内存不能拆分使用
2.需要按申请顺序分配，先申请的先分配，有可用内存分配则申请结果为true，没有可用则返回false
注释：不考虑内存释放
输入描述
输入为两行字符串，第一行为内存池资源列表，包含内存粒度数据信息，粒度数据间用逗号分割
一个粒度信息内用冒号分割，冒号前为内存粒度大小，冒号后为数量
资源列表不大于1024，每个粒度的数量不大于4096
第二行为申请列表
申请的内存大小间用逗号分割，申请列表不大于100000
示例一：
输入：
64:2,128:1,32:4,1:128
50,36,64,128,127
输出：
true,true,true,false,false

说明:
内存池资源包含：64k共2个、128k共1个、32k共4个、1k共128个的内存资源
针对50,36,64,128,127的内存申请序列，分配的内存依次是，64,64,128,null,null
第三次申请内存时已经将128分配出去，因此输出的结果是true,true,true,false,false
'''
s=input('').split(",")
ask=input('')
dict=[]
for i in s:
    size=i.split(":")[0]
    num=int(i.split(":")[1])
    for n in range(num):
        dict.append(size)
        n+=1
result=[]
ask=ask.split(",")
for s in ask:
    flag="false"
    for i in range(len(dict)):
        if int(s)<=int(dict[i]):
            dict[i]=0
            flag="true"
            break
    result.append(flag)
print(','.join(result))
        
