import os
import variable
#文档文段
#历史学科内容控制
def difficulty():
    if variable.difficulty == 1: variable.cache=variable.cache.replace('$difficulty$', '低难度的')
    if variable.difficulty == 2: variable.cache=variable.cache.replace('$difficulty$', '中等难度的')
    if variable.difficulty == 3: variable.cache=variable.cache.replace('$difficulty$', '高难度的')
def difficulty2():
    if variable.difficulty == 1: variable.cache=variable.cache.replace('$difficulty1$', ' ')
    if variable.difficulty == 2: variable.cache=variable.cache.replace('$difficulty1$', 'Please use complex Tem-8 vocabulary as much as possible.')
    if variable.difficulty == 3: variable.cache=variable.cache.replace('$difficulty1$', 'Please use complex Tem-8 vocabulary as much as possible.')
    if variable.difficulty == 1: variable.cache=variable.cache.replace('$difficulty2$', ' ')
    if variable.difficulty == 2: variable.cache=variable.cache.replace('$difficulty2$', 'You have to use a lot of CET-6 vocabulary.')
    if variable.difficulty == 3: variable.cache=variable.cache.replace('$difficulty2$', 'You have to use a lot of TEM-8 vocabulary.')
def select_History():
    #材料题
    if variable.type==1:
        # 读取历史回答
        with open('data/history1a.tls', encoding='utf-8') as file_obj:
            variable.answer = file_obj.read()
        # 读取通式模板
        with open('data/history1.tls', encoding='utf-8') as file_obj:
            variable.cache = file_obj.read()
        #难度的更改
        difficulty()
        if len(variable.content) != 0:
            variable.cache=variable.cache.replace('$content2$', '要求必须根据如下一段资料出题：$content$')
            variable.cache=variable.cache.replace('$content$', variable.content)
        if len(variable.content) == 0:
            variable.cache=variable.cache.replace('$content2$', '要求根据一段资料出题  资料不超过300字符')
    #年份题
    if variable.type == 2:
        # 读取历史回答
        with open('data/history2a.tls', encoding='utf-8') as file_obj:
            variable.answer = file_obj.read()
        # 读取通式模板
        with open('data/history2.tls', encoding='utf-8') as file_obj:
            variable.cache = file_obj.read()
        difficulty()
        if len(variable.content) != 0:
            variable.cache=variable.cache.replace('$content$', "内容为"+ variable.content)
        if len(variable.content) == 0:
            variable.cache=variable.cache.replace('$content$',' ')
    #政策题
    if variable.type == 3:
        # 读取历史回答
        with open('data/history3a.tls', encoding='utf-8') as file_obj:
            variable.answer = file_obj.read()
        # 读取通式模板
        with open('data/history3.tls', encoding='utf-8') as file_obj:
            variable.cache = file_obj.read()
        difficulty()
        if len(variable.content) != 0:
            variable.cache=variable.cache.replace('$content$', "内容为" + variable.content)
        if len(variable.content) == 0:
            variable.cache=variable.cache.replace('$content$', '')
    #意义题
    if variable.type == 4:
        # 读取历史回答
        with open('data/history4a.tls', encoding='utf-8') as file_obj:
            variable.answer = file_obj.read()
        # 读取通式模板
        with open('data/history4.tls', encoding='utf-8') as file_obj:
            variable.cache = file_obj.read()
        difficulty()
        if len(variable.content) != 0:
            variable.cache=variable.cache.replace('$content$', "内容为" + variable.content)
        if len(variable.content) == 0:
            variable.cache=variable.cache.replace('$content$', '')
    if variable.ctype == 2:
        # 读取历史回答
        with open('data/history5a.tls', encoding='utf-8') as file_obj:
            variable.answer = file_obj.read()
        # 读取通式模板
        with open('data/history5.tls', encoding='utf-8') as file_obj:
            variable.cache = file_obj.read()
        difficulty()
        if len(variable.content) != 0:
            variable.cache=variable.cache.replace('$content$', "内容为" + variable.content)
            #print(variable.cache)
        if len(variable.content) == 0:
            variable.cache=variable.cache.replace('$content$', '')
        if len(variable.num) != 0:
            variable.cache = variable.cache.replace('$num$', variable.num)
    #variable.update(variable.cache)
    print(variable.cache)
def select_English():
    if variable.type==1:
        with open('data/english1a.tls', encoding='utf-8') as file_obj:
            variable.answer = file_obj.read()
        # 读取通式模板
        with open('data/english1.tls', encoding='utf-8') as file_obj:
            variable.cache = file_obj.read()
        if len(variable.content) != 0:
            variable.cache=variable.cache.replace('$content$', "考察" + variable.content)
        if len(variable.content) == 0:
            variable.cache=variable.cache.replace('$content$', '')
    if variable.type == 4:
        with open('data/english4a.tls', encoding='utf-8') as file_obj:
            variable.answer = file_obj.read()
        # 读取通式模板
        with open('data/english4.tls', encoding='utf-8') as file_obj:
            variable.cache = file_obj.read()
    if variable.type == 5:
        with open('data/english5a.tls', encoding='utf-8') as file_obj:
            variable.answer = file_obj.read()
        # 读取通式模板
        with open('data/english5.tls', encoding='utf-8') as file_obj:
            variable.cache = file_obj.read()

        if len(variable.content) != 0:
            variable.cache = variable.cache.replace('$content$', "内容关于" + variable.content)
        if len(variable.content) == 0:
            variable.cache = variable.cache.replace('$content$', " ")
        if variable.rcqtype == 1:
            variable.cache = variable.cache.replace('$rcqtype$', "narrative essay")
        if variable.rcqtype == 2:
            variable.cache = variable.cache.replace('$rcqtype$', "fantasy novel")
        if variable.rcqtype == 11:
            variable.cache = variable.cache.replace('$rcqtype$', "expository text")
        if variable.rcqtype == 21:
            variable.cache = variable.cache.replace('$rcqtype$', "argumentative essay")
        if variable.rcqtype == 31:
            variable.cache = variable.cache.replace('$rcqtype$', "practical writing")

    if variable.type == 6:
        with open('data/english6a.tls', encoding='utf-8') as file_obj:
            variable.answer = file_obj.read()
        # 读取通式模板
        with open('data/english6.tls', encoding='utf-8') as file_obj:
            variable.cache = file_obj.read()
        difficulty2()
        if len(variable.content) != 0:
            variable.cache = variable.cache.replace('$content$', "内容关于" + variable.content)
        if len(variable.content) == 0:
            variable.cache = variable.cache.replace('$content$', " ")