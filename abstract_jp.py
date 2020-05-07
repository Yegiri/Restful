# -*- coding: utf-8 -*-

from __future__ import absolute_import
from __future__ import division, print_function, unicode_literals

from sumy.parsers.html import HtmlParser
from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer
from sumy.summarizers.lsa import LsaSummarizer as Summarizer
from sumy.nlp.stemmers import Stemmer
from sumy.utils import get_stop_words


LANGUAGE = "japanese"
SENTENCES_COUNT = 3

text = """乗客１０６人が死亡し、５６２人が重軽傷を負った兵庫県尼崎市のＪＲ福知山線脱線事故は２５日、発生から１５年となったが、今年は新型コロナウイルス感染拡大の影響で、ＪＲ西日本主催の追悼慰霊式が初めて開かれなかった。現場を訪れることを断念した遺族や負傷者らは、それぞれの場所で祈りをささげた。

　次男の昌毅（まさき）さん＝当時（１８）＝を亡くした上田弘志さん（６５）は体調を崩したことから自宅で昌毅さんの冥福を祈り、「現場に行けなくてごめんな」と頭を下げたという。

　ただ、うれしい報告もできた。３日前、三男の篤史（あつし）さん（３０）に長女の陽菜（ひな）ちゃんが誕生したことだ。「こんなに前向きになれた２５日は初めて」と上田さん。昌毅さんに「来年は陽菜を抱っこして現場に行くね」と約束したといい、「『じいちゃん、頑張れ』って返してくれた」とほほえんだ。

　３両目に乗車し、顔や足に重傷を負った玉置富美子さん（７０）も体調を考慮し、現場を訪れなかった。だが、「現場はたくさんの命が犠牲となり、自分にとっては人生が百八十度変わった場所。行くことで重みを感じられる」とした上で「式典がなかったら思い出す機会もなくなってしまう。ＪＲ西はこの日を忘れないように引き継いでほしい」と訴えた。


　２両目に乗っていた次女（３４）が重傷を負った三井ハルコさん（６４）は、これまで家族で追悼慰霊式に参加した後、現場近くで事故の風化防止を願う栞（しおり）を配布してきたが、今年は自宅に。「今日は１５年間で初めて静かに祈りの時間を過ごすことができた」と話した。"""

if __name__ == "__main__":
    parser = PlaintextParser.from_string(text, Tokenizer(LANGUAGE))
    stemmer = Stemmer(LANGUAGE)

    summarizer = Summarizer(stemmer)
    summarizer.stop_words = get_stop_words(LANGUAGE)

    for sentence in summarizer(parser.document, SENTENCES_COUNT):
        print(sentence)