import requests
import json

text_jp = """乗客１０６人が死亡し、５６２人が重軽傷を負った兵庫県尼崎市のＪＲ福知山線脱線事故は２５日、発生から１５年となったが、今年は新型コロナウイルス感染拡大の影響で、ＪＲ西日本主催の追悼慰霊式が初めて開かれなかった。現場を訪れることを断念した遺族や負傷者らは、それぞれの場所で祈りをささげた。

　次男の昌毅（まさき）さん＝当時（１８）＝を亡くした上田弘志さん（６５）は体調を崩したことから自宅で昌毅さんの冥福を祈り、「現場に行けなくてごめんな」と頭を下げたという。

　ただ、うれしい報告もできた。３日前、三男の篤史（あつし）さん（３０）に長女の陽菜（ひな）ちゃんが誕生したことだ。「こんなに前向きになれた２５日は初めて」と上田さん。昌毅さんに「来年は陽菜を抱っこして現場に行くね」と約束したといい、「『じいちゃん、頑張れ』って返してくれた」とほほえんだ。

　３両目に乗車し、顔や足に重傷を負った玉置富美子さん（７０）も体調を考慮し、現場を訪れなかった。だが、「現場はたくさんの命が犠牲となり、自分にとっては人生が百八十度変わった場所。行くことで重みを感じられる」とした上で「式典がなかったら思い出す機会もなくなってしまう。ＪＲ西はこの日を忘れないように引き継いでほしい」と訴えた。

　２両目に乗っていた次女（３４）が重傷を負った三井ハルコさん（６４）は、これまで家族で追悼慰霊式に参加した後、現場近くで事故の風化防止を願う栞（しおり）を配布してきたが、今年は自宅に。「今日は１５年間で初めて静かに祈りの時間を過ごすことができた」と話した。"""

text_en = """Automatic summarization is the process of reducing a text document with a \
computer program in order to create a summary that retains the most important points \
of the original document. As the problem of information overload has grown, and as \
the quantity of data has increased, so has interest in automatic summarization. \
Technologies that can make a coherent summary take into account variables such as \
length, writing style and syntax. An example of the use of summarization technology \
is search engines such as Google. Document summarization is another."""

text_ch = """上世纪50年代，一批交大人响应党的号召，“打起背包就出发”，从上海迁至西安，在三秦大地书写了“胸怀大局、无私奉献、弘扬传统、艰苦创业”的“西迁精神”。

　　4月22日，在陕西考察的习近平总书记走进交大西迁博物馆，仔细端详一张张照片、一件件实物。他指出，“西迁精神”的核心是爱国主义，精髓是听党指挥跟党走，与党和国家、与民族和人民同呼吸、共命运，具有深刻现实意义和历史意义，并勉励广大师生大力弘扬“西迁精神”。

　　为国奋斗是最好的爱国表白。从革命战争年代的红船精神、沂蒙精神，到新中国成立初期的“西迁精神”、垦荒精神，再到当下的工匠精神、企业家精神。。。。。。这些精神背后都记录着一段段刻骨铭心的经历，蕴藏着爱国主义的力量。一直以来，习近平视这些精神为党的宝贵精神财富，大力推崇弘扬。

　　在复工复产复商复市的关键期，央视网《联播+》特推出海报，号召大家一起感悟精神的力量，为全面建成小康社会而奋斗！"""

data_en = {'language':'english', 'text':text_en}
abstract_en = requests.get('http://localhost:8383/get_abstract', params=data_en)
print(json.loads(abstract_en.text)['abstract'])
print()

data_ch = {'language':'chinese', 'text':text_ch}
abstract_ch = requests.get('http://localhost:8383/get_abstract', params=data_ch)
print(json.loads(abstract_ch.text)['abstract'])
print()

data_jp= {'language':'japanese', 'text':text_jp}
abstract_jp = requests.get('http://localhost:8383/get_abstract', params=data_jp)
print(json.loads(abstract_jp.text)['abstract'])