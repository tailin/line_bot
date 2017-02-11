# -*- coding: utf-8 -*-

horse_phrase = [
'馬勃牛溲', '馬浡牛溲', '馬不解鞍', '馬不停蹄', '馬塵不及', '馬遲枚疾', '馬齒徒長', '馬到成功', '馬耳春風', '馬耳東風',
'馬翻人仰', '馬放南山', '馬腹逃鞭', '馬革裹屍', '馬革盛屍', '馬工枚速', '馬跡蛛絲', '馬角烏白', '馬角烏頭', '馬空冀北',
'馬龍車水', '馬鹿異形', '馬鹿易形', '馬馬虎虎', '馬毛蝟磔', '馬毛蝟磔', '馬面牛頭', '馬牛襟裾', '馬牛其風', '馬前潑水',
'馬去馬歸', '馬如流水', '馬如游龍', '馬如游魚', '馬入華山', '馬上房子', '馬上功成', '馬上看花', '馬上牆頭', '馬首是瞻',
'馬首欲東', '馬瘦毛長', '馬水車龍', '馬咽車闐', '馬仰人翻', '馬中關五', '馬壯人強', '馬捉老鼠', '馬足車塵', '馬足龍沙',
'馬革裏屍',
'鞍馬勞頓', '鞍馬勞倦', '鞍馬勞困', '鞍馬勞神', '鞍馬之勞', '班馬文章', '寶馬香車', '策馬飛輿', '車馬輻輳', '車馬駢闐',
'車馬填門', '車馬盈門', '馳馬試劍', '打馬虎眼', '大馬金刀', '代馬望北', '代馬依風', '得馬生災', '得馬失馬', '得馬折足',
'放馬後炮', '放馬華陽', '肥馬輕裘', '風馬不接', '風馬雲車', '狗馬聲色', '谷馬礪兵', '歸馬放牛', '汗馬功勞', '金馬玉堂',
'裾馬襟牛', '叩馬而諫', '快馬加鞭', '老馬戀棧', '老馬識途', '立馬萬言', '六馬仰秣', '龍馬精神', '率馬以驥', '馬馬虎虎',
'買馬招兵', '買馬招軍', '牛馬襟裾', '駑馬戀棧', '駑馬鉛刀', '駑馬十駕', '駑馬十舍', '拍馬溜須', '盤馬彎弓', '跑馬觀花',
'匹馬單槍', '匹馬當先', '匹馬一麾', '匹馬只輪', '騎馬尋馬', '騎馬找馬', '求馬唐肆', '裘馬輕肥', '裘馬輕狂', '裘馬清狂',
'裘馬聲色', '犬馬戀主', '犬馬之報', '犬馬之誠', '犬馬之疾', '犬馬之決', '犬馬之勞', '犬馬之力', '犬馬之戀', '犬馬之年',
'犬馬之養', '雀馬魚龍', '戎馬倉皇', '戎馬倥傯', '戎馬倥傯', '戎馬劻勷', '戎馬生郊', '戎馬生涯', '三馬同槽', '散馬休牛',
'殺馬毀車', '善馬熟人', '失馬塞翁', '食馬留肝', '束馬縣車', '束馬懸車', '司馬稱好', '司馬青衫', '四馬攢蹄', '駟馬不追',
'駟馬高車', '駟馬高蓋', '駟馬高門', '駟馬莫追', '駟馬難追', '駟馬軒車', '駟馬仰秣', '鐵馬金戈', '萬馬奔騰', '萬馬齊喑',
'五馬分屍', '系馬埋輪', '瞎馬臨池', '下馬馮婦', '下馬看花', '信馬由韁', '野馬無韁', '一馬當先', '一馬平川', '一馬一鞍',
'衣馬輕肥', '倚馬可待', '倚馬七紙', '倚馬千言', '意馬心猿', '飲馬長江', '飲馬投錢', '躍馬彎弓', '躍馬揚鞭', '仗馬寒蟬',
'陣馬風檣', '竹馬之交', '走馬看花', '走馬上任', '走馬章台', '天馬行空', '走馬平川',
'風馬牛不相及', '駑馬戀棧豆', '死馬當活馬醫', '司馬牛之嘆',
'鞍前馬後', '兵荒馬亂', '兵強馬壯', '不識馬肝', '不食馬肝', '車塵馬跡', '車塵馬足', '車馳馬驟', '車怠馬煩', '車煩馬斃',
'車水馬龍', '車填馬隘', '車在馬前', '車轍馬跡', '風吹馬耳', '弓調馬服', '裹屍馬革', '猴年馬月', '襟裾馬牛', '龍神馬壯',
'驢前馬後', '馬去馬歸', '枚速馬工', '拿下馬來', '牛高馬大', '牛溲馬勃', '牛溲馬渤', '牛童馬走', '牛頭馬面', '乞兒馬醫',
'牆頭馬上', '秋高馬肥', '權移馬鹿', '人喊馬嘶', '人歡馬叫', '人荒馬亂', '人困馬乏', '人強馬壯', '人仰馬翻', '人語馬嘶',
'神龍馬壯', '士飽馬騰', '天粟馬角', '烏白馬角', '烏頭馬角', '效犬馬力', '獐麇馬鹿', '蛛絲馬跡', '露出馬腳',
'北叟失馬', '弊車羸馬', '避世金馬', '伯樂相馬', '持戈試馬', '窗間過馬', '吹牛拍馬', '丹書白馬', '單槍匹馬', '得馬失馬',
'鬥雞走馬', '短衣匹馬', '二童一馬', '放牛歸馬', '飛鷹走馬', '風車雨馬', '風車雲馬', '風檣陣馬', '服牛乘馬', '高車駟馬',
'高頭大馬', '膏車秣馬', '光車駿馬', '害群之馬', '寒蟬仗馬', '橫刀躍馬', '橫戈盤馬', '橫戈躍馬', '橫槍躍馬', '呼牛呼馬',
'呼牛作馬', '諱樹數馬', '毀車殺馬', '見鞍思馬', '金戈鐵馬', '僅容旋馬', '鳩車竹馬', '尻輪神馬', '厲兵秣馬', '溜須拍馬',
'盲人瞎馬', '泥車瓦馬', '騎馬尋馬', '騎馬找馬', '千軍萬馬', '敲牛宰馬', '青梅竹馬', '青絲白馬', '輕裘肥馬', '軟裘快馬',
'塞翁得馬', '塞翁失馬', '聲色犬馬', '識途老馬', '束兵秣馬', '素車白馬', '素絲良馬', '銅圍鐵馬', '童牛角馬', '土牛木馬',
'脫韁之馬', '文君司馬', '問牛知馬', '問羊知馬', '烏焉成馬', '五花殺馬', '舞刀躍馬', '洗兵牧馬', '鮮車健馬', '鮮車怒馬',
'鮮衣良馬', '鮮衣怒馬', '香車寶馬', '心猿意馬', '休牛歸馬', '休牛散馬', '朽索馭馬', '懸兵束馬', '懸車束馬', '懸崖勒馬',
'燕昭好馬', '以渴服馬', '以毛相馬', '玉堂金馬', '招兵買馬', '枕戈汗馬', '止戈散馬', '指鹿為馬',
'東風吹馬耳', '烏頭白馬生角',
'牝牡驪黃',
]

lion_phrase = [
    '河東獅吼',
    '河東獅子',
    '龍鳴獅吼',
    '人中獅子',
    '獅子搏兔，亦用全力',
    '獅子大開口',
    '獅威勝虎',
    '渴驥怒猊',
    '獅虎當道',
]

dunkey_phrase = [
    '非驢非馬',
    '倒站驢子' ,
    '驢蒙虎皮', 
    '驢鳴犬吠', 
    '驢前馬後', 
    '驢生笄角', 
    '隨驢把馬', 
    '黔驢技窮', 
    '卸磨殺驢',
    '三紙無驢', 
    '博士買驢',
    '驢頭不對馬嘴',
    '騎驢找馬',
    '卸磨殺驢',
    '借坡下驢',
    '驢年馬月',
    '騎驢倒墮',
    '騎驢索句',
    '驢唇馬嘴',
]

