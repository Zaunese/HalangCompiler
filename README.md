# HalangCompiler

Compile _Halang_ to _C++_.

Usage: `main.py xxx.halang`

The source code must use **UTF-8** encoding.

| Halang | C++ |
| :----------: | :----------: |
|a��b��֪���ߵ�����ȥ��|a>b|
|a��b�ܵû���|a>b|
|������˼����|!=|
|������˼��|==|
|û����|!|
|excited|exit(0)|
|I'm angry!|exit(1)|
|�ʴš���|True|
|û���κε���˼|False|
|�޿ɷ��|void|
|ʲôҲ��˵|void|
|Ū��|throw|
|������|exception|
|��˵(a)|printf(a)|
|��߾���(a)|scanf(a)|
|����|stdout|
|����|stdin|
|��aд��b|b=a|
|��a����һ��|fprintf(stderr,a)|
|������(a){b}����ô{c}|if(a){b}else{c}|
|������һ����{a}�����ϳ���ƫ���(b)��{c}����Ҫ{d}|try{a}catch(b){c}finally{d}|
|�й��о�Ż���|#include|
|��Ӧ|#define|
|�ն�a��b��|a=b|
|�������|goto|
|ʶ����ʶ��(a)|assert(a)|
|a�Ǹ�b|a.b|
|�㽫������|return|
|��һ��|++|
|����|+|
|��һ��|--|
|����|-|
|����|/|
|����|*|
|��Ҫ|%|
|��Ȳ�|break|
|�ǳ�|continue|
|����|main|
|��¼|char|
|����|string|
|����|int|
|�̰�|short|
|����|long|
|����|float|
|ͬ����|double|
|��ˮ������ˮ|static|
|��|struct|
|����|template|
|����|class|
|����|public|
|˽��|private|
|�Լ�|this|
|�ܶ�(a){b}|while(a){b}|
|�г�|for|