import sys
import re

filename=sys.argv[1]

with open(filename,'r',encoding='utf8') as f:
    with open(filename.replace('.halang','.cpp'),'w') as of:
        of.write('#include<cstdio>\n#include<cstdlib>\n')
        for l in f:
            l=l.replace('讲的意思不是','!=')
            l=l.replace('讲的意思是','==')
            l=l.replace('没听到','!')
            l=l.replace('excited','exit(0)')
            l=l.replace('I\'m angry!','exit(1)')
            l=l.replace('资磁','true')
            l=l.replace('吼啊','true')
            l=l.replace('没有任何的意思','false')
            l=l.replace('无可奉告','void')
            l=l.replace('什么也不说','void')
            l=l.replace('弄个','throw')
            l=l.replace('大新闻','exception')
            l=l.replace('我说','printf')
            l=l.replace('提高警惕','scanf')
            l=l.replace('你们有一个好','try')
            l=l.replace('报道上出了偏差叫','catch')
            l=l.replace('还需要','finally')
            l=l.replace('党章','stdout')
            l=l.replace('理论','stdin')
            l=l.replace('你问我','if')
            l=l.replace('我怎么','else')
            l=l.replace('中国有句古话叫','#include')
            l=l.replace('呼应','#define')
            l=l.replace('另请高明','goto')
            l=l.replace('那个','.')
            l=l.replace('你将来报道','return')
            l=l.replace('加一秒','++')
            l=l.replace('红衣','+')
            l=l.replace('续一秒','--')
            l=l.replace('续命','-')
            l=l.replace('节能','/')
            l=l.replace('经商','*')
            l=l.replace('次要','%')
            l=l.replace('请喝茶','break')
            l=l.replace('辞呈','continue')
            l=l.replace('报告','main')
            l=l.replace('语录','char')
            l=l.replace('讲话','string')
            l=l.replace('完整','int')
            l=l.replace('短板','short')
            l=l.replace('长者','long')
            l=l.replace('单独','float')
            l=l.replace('同根生','double')
            l=l.replace('井水不犯河水','static')
            l=l.replace('党','struct')
            l=l.replace('例子','template')
            l=l.replace('概念','class')
            l=l.replace('共产','public')
            l=l.replace('私有','private')
            l=l.replace('自己','this')
            l=l.replace('奋斗','while')
            l=l.replace('行程','for')

            l=re.sub('把(.*?)批判一番([,;\{\}\s])', \
                lambda x:'fprintf(stderr,{}){}'.format(x.group(1),x,group(2)),l)
            l=re.sub('(.*?)比(.*?)不知道高到哪里去了', \
                lambda x:'{}>{}'.format(x.group(1),x.group(2)),l)
            l=re.sub('(.*?)比(.*?)跑得还快', \
                lambda x:'{}>{}'.format(x.group(1),x.group(2)),l)
            l=re.sub('把(.*?)写进(.*?)([,;\{\}\s])', \
                lambda x:'{}={}{}'.format(x.group(2),x.group(1),x.group(3)),l)
            l=re.sub('钦定(.*?)是(.*?)啦', \
                lambda x:'{}={}'.format(x.group(1),x.group(2)),l)

            l=l.replace('得','')
            of.writelines([l])
