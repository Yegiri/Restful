# coding:utf-8

from textrank4zh import TextRank4Keyword, TextRank4Sentence


if __name__ == '__main__':
    text = """上世纪50年代，一批交大人响应党的号召，“打起背包就出发”，从上海迁至西安，在三秦大地书写了“胸怀大局、无私奉献、弘扬传统、艰苦创业”的“西迁精神”。

　　4月22日，在陕西考察的习近平总书记走进交大西迁博物馆，仔细端详一张张照片、一件件实物。他指出，“西迁精神”的核心是爱国主义，精髓是听党指挥跟党走，与党和国家、与民族和人民同呼吸、共命运，具有深刻现实意义和历史意义，并勉励广大师生大力弘扬“西迁精神”。

　　为国奋斗是最好的爱国表白。从革命战争年代的红船精神、沂蒙精神，到新中国成立初期的“西迁精神”、垦荒精神，再到当下的工匠精神、企业家精神。。。。。。这些精神背后都记录着一段段刻骨铭心的经历，蕴藏着爱国主义的力量。一直以来，习近平视这些精神为党的宝贵精神财富，大力推崇弘扬。

　　在复工复产复商复市的关键期，央视网《联播+》特推出海报，号召大家一起感悟精神的力量，为全面建成小康社会而奋斗！"""

    tr4s = TextRank4Sentence()
    tr4s.analyze(text=text, lower=True, source='all_filters')

    print()
    print('摘要：')
    for item in tr4s.get_key_sentences(num=3):
        print(item.index, item.weight, item.sentence)  # index是语句在文本中位置，weight是权重