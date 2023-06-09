import emoji

# at_photo = [
#     r"https://dynamic-media-cdn.tripadvisor.com/media/photo-o/08/e9/f1/af/caption.jpg?w=1100&h=-1&s=1",
#     r"https://ysia.ru/wp-content/uploads/2021/12/maska-ooa2kl97yhsyamwg5ufzy7m4ej4fv32tfazr2p4bo8-e1639497356360.jpg",
#     r"https://dynamic-media-cdn.tripadvisor.com/media/photo-o/06/cd/1f/8c/caption.jpg?w=1200&h=-1&s=1",
#     r"https://media-cdn.tripadvisor.com/media/photo-s/11/71/d6/4b/founders-monument.jpg",
#     r"https://dynamic-media-cdn.tripadvisor.com/media/photo-o/11/87/c8/2c/front-view.jpg?w=1200&h=1200&s=1",
#     r"https://media-cdn.tripadvisor.com/media/photo-s/09/a2/99/56/caption.jpg",
#     r"https://dynamic-media-cdn.tripadvisor.com/media/photo-o/07/d3/7b/03/caption.jpg?w=1200&h=1200&s=1",
#     r"http://leninstatues.ru/sites/default/files/styles/large/public/photos/magadan.jpg?itok=0eLHNr7Z",
#     r"https://dynamic-media-cdn.tripadvisor.com/media/photo-o/16/71/89/a5/photo0jpg.jpg?w=1200&h=-1&s=1",
#     r"https://www.kolyma.ru/magadan/uploads/posts/2019-10/1571682320_muzey.jpg"
# ]
#
# at_desc = [
#     "<b>Железный мамонт.</b>\nВ Магадане есть статуя, которая символизирует связь времён. Идея автора заключалась в том, чтобы создать мамонта из металлолома.  Автор работы скульптор Юрий Руденко — это известный мастер в городе. Целых четыре года понадобилось ему, чтобы идея воплотилась в жизнь. ",
#     "<b>Маска Скорби.</b>\nМемориал в Магадане, посвящённый памяти жертв политических репрессий. Центральный монумент высотой 15 метров. Авторы: скульптор — Эрнст Неизвестный",
#     "<b>Памятник Владимиру Высоцкому.</b>\nПамятник Владимиру Высоцкому - советскому поэту, актёру театра и кино установлен на берегу бухты Нагаево в Магадане. Открытие скульптуры состоялось в День города. Скульптуру выполнили по проекту магаданского скульптора Юрия Руденко. ",
#     "<b>Монумент основателям города магадана.</b>\nНа высоком берегу Нагаевской бухты расположен памятник «Пионерам освоения Колымы и Чукотки». Его посвятили отчаянным и храбрым людям, тем, кто осваивал Колыму, возводил на берегах бухты Нагаево новый город – город с загадочным названием Магадан.",
#     "<b>Узел памяти.</b>\n«Узел памяти» – памятник магаданцам - героям фронта и тыла. В сентябре 1971 г. магаданский горисполком принял решение «О сооружении в г. Магадане памятника-монумента Вечной славы в честь Победы советского народа в Великой Отечественной войне 1941-1945 гг.». Авторами памятника стали скульптор Владимир Иванович Ролдугин и архитектор Николай Николаевич Лушик из города Санкт-Петербург.",
#     "<b>Памятник имени В. А. Козина.</b>\nСкульптурная композиция певца и композитора изображает Козина сидящим на скамье в своем стареньком пальто и валенках, с кошкой на руках, рядом с ним лежит папка со стихами, на которой написано «Певец и композитор Вадим Козин»",
#     "<b>Часовня Георгия Победоносца.</b>\nВ адрес Магаданского епархиального управления часто поступали пожелания жителей города Магадана воздвигнуть храм, памятник или часовню в память о павших в Великой Отечественной войне. Администрация города и области откликнулась на эти пожелания, и на Аллее памяти воинов-защитников в центре города была воздвигнута часовня во имя великомученика Георгия Победоносца.",
#     "<b>Памятник Ленину.</b>\nПамятник Владимиру Ленину, который изготовили из бронзы на Ленинградском заводе, открыли на центральной площади Магадана 10 октября 1987 года. На следующий день на реконструированной площади имени вождя Великой Октябрьской социалистической революции состоялся общегородской митинг.Новый памятник Владимиру Ленину торжественно открыли в Магадане в 1987 году. До этого магаданцы любовались на монумент с поднятой рукой вождя.",
#     "<b>Свято-Троицкий собор.</b>\nСвято-Троицкий собор г. Магадана (Собор Троицы Живоначальной) — кафедральный собор Магаданской и Синегорской епархии Русской Православной Церкви. Храм-памятник жертвам политических репрессий, один из крупнейших храмов на Дальнем Востоке. Общая площадь Собора с учётом прилегающей территории — более 9 тыс. кв. метров.",
#     "<b>Областной краеведческий музей.</b>\nОснован в 1934 году в Магадане на базе выставки, проходившей в городе вместе со съездом колхозников. Материалы музея рассказывают о разных периодах. Например, о давнем прошлом региона, который населяли эвены и якуты, а также о временах сталинских репрессий."
# ]
#
# at_names = [
#     "Железный мамонт",
#     "Маска Скорби",
#     "Памятник Владимиру Высоцкому",
#     "Монумент основателям города магадана",
#     "Узел памяти",
#     "Памятник имени В. А. Козина",
#     "Часовня Георгия Победоносца",
#     "Памятник Ленину",
#     "Свято-Троицкий собор",
#     "Областной краеведческий музей"
# ]
#
# at_coords = [
#     (59.56429609976189, 150.7704932596274),
#     (59.591629953479625, 150.81198529648498),
#     (59.55628159740245, 150.77870404232675),
#     (59.556261, 150.779087),
#     (59.56369767433912, 150.80543342079102),
#     (59.565247893820256, 150.8017490977041),
#     (59.5614589036509, 150.80059572089786),
#     (59.55328768018911, 150.81183262713472),
#     (59.567423593845156, 150.81276047673234),
#     (59.55890106597851, 150.81527719999997)
# ]
#
# at_coord = []
# for i in range(len(at_coords)):
#     d = dict()
#     d["lat"] = at_coords[i][0]
#     d["lon"] = at_coords[i][1]
#     at_coord.append(d)
#
# at_keys = ["name", "desc", "photo", "coord"]
# at_all = []
# for i in range(len(at_photo)):
#     d = dict()
#     d[at_keys[0]] = at_names[i]
#     d[at_keys[1]] = at_desc[i]
#     d[at_keys[2]] = at_photo[i]
#     d[at_keys[3]] = at_coord[i]
#     at_all.append(d)


at_all = [
    {'name': 'Железный мамонт',
     'desc': '<b>Железный мамонт.</b>\nВ Магадане есть статуя, которая символизирует связь времён. Идея автора заключалась в том, чтобы создать мамонта из металлолома.  Автор работы скульптор Юрий Руденко — это известный мастер в городе. Целых четыре года понадобилось ему, чтобы идея воплотилась в жизнь. ',
     'photo': 'https://dynamic-media-cdn.tripadvisor.com/media/photo-o/08/e9/f1/af/caption.jpg?w=1100&h=-1&s=1',
     'coord': {'lat': 59.56429609976189, 'lon': 150.7704932596274}},
    {'name': 'Маска Скорби',
     'desc': '<b>Маска Скорби.</b>\nМемориал в Магадане, посвящённый памяти жертв политических репрессий. Центральный монумент высотой 15 метров. Авторы: скульптор — Эрнст Неизвестный',
     'photo': 'https://ysia.ru/wp-content/uploads/2021/12/maska-ooa2kl97yhsyamwg5ufzy7m4ej4fv32tfazr2p4bo8-e1639497356360.jpg',
     'coord': {'lat': 59.591629953479625,
               'lon': 150.81198529648498}},
    {'name': 'Памятник Владимиру Высоцкому',
     'desc': '<b>Памятник Владимиру Высоцкому.</b>\nПамятник Владимиру Высоцкому - советскому поэту, актёру театра и кино установлен на берегу бухты Нагаево в Магадане. Открытие скульптуры состоялось в День города. Скульптуру выполнили по проекту магаданского скульптора Юрия Руденко. ',
     'photo': 'https://dynamic-media-cdn.tripadvisor.com/media/photo-o/06/cd/1f/8c/caption.jpg?w=1200&h=-1&s=1',
     'coord': {'lat': 59.55628159740245, 'lon': 150.77870404232675}},
    {'name': 'Монумент основателям города магадана',
     'desc': '<b>Монумент основателям города магадана.</b>\nНа высоком берегу Нагаевской бухты расположен памятник «Пионерам освоения Колымы и Чукотки». Его посвятили отчаянным и храбрым людям, тем, кто осваивал Колыму, возводил на берегах бухты Нагаево новый город – город с загадочным названием Магадан.',
     'photo': 'https://media-cdn.tripadvisor.com/media/photo-s/11/71/d6/4b/founders-monument.jpg',
     'coord': {'lat': 59.556261, 'lon': 150.779087}},
    {'name': 'Узел памяти',
     'desc': '<b>Узел памяти.</b>\n«Узел памяти» – памятник магаданцам - героям фронта и тыла. В сентябре 1971 г. магаданский горисполком принял решение «О сооружении в г. Магадане памятника-монумента Вечной славы в честь Победы советского народа в Великой Отечественной войне 1941-1945 гг.». Авторами памятника стали скульптор Владимир Иванович Ролдугин и архитектор Николай Николаевич Лушик из города Санкт-Петербург.',
     'photo': 'https://dynamic-media-cdn.tripadvisor.com/media/photo-o/11/87/c8/2c/front-view.jpg?w=1200&h=1200&s=1',
     'coord': {'lat': 59.56369767433912, 'lon': 150.80543342079102}},
    {'name': 'Памятник имени В. А. Козина',
     'desc': '<b>Памятник имени В. А. Козина.</b>\nСкульптурная композиция певца и композитора изображает Козина сидящим на скамье в своем стареньком пальто и валенках, с кошкой на руках, рядом с ним лежит папка со стихами, на которой написано «Певец и композитор Вадим Козин»',
     'photo': 'https://media-cdn.tripadvisor.com/media/photo-s/09/a2/99/56/caption.jpg',
     'coord': {'lat': 59.565247893820256,
               'lon': 150.8017490977041}},
    {'name': 'Часовня Георгия Победоносца',
     'desc': '<b>Часовня Георгия Победоносца.</b>\nВ адрес Магаданского епархиального управления часто поступали пожелания жителей города Магадана воздвигнуть храм, памятник или часовню в память о павших в Великой Отечественной войне. Администрация города и области откликнулась на эти пожелания, и на Аллее памяти воинов-защитников в центре города была воздвигнута часовня во имя великомученика Георгия Победоносца.',
     'photo': 'https://dynamic-media-cdn.tripadvisor.com/media/photo-o/07/d3/7b/03/caption.jpg?w=1200&h=1200&s=1',
     'coord': {'lat': 59.5614589036509, 'lon': 150.80059572089786}},
    {'name': 'Памятник Ленину',
     'desc': '<b>Памятник Ленину.</b>\nПамятник Владимиру Ленину, который изготовили из бронзы на Ленинградском заводе, открыли на центральной площади Магадана 10 октября 1987 года. На следующий день на реконструированной площади имени вождя Великой Октябрьской социалистической революции состоялся общегородской митинг.Новый памятник Владимиру Ленину торжественно открыли в Магадане в 1987 году. До этого магаданцы любовались на монумент с поднятой рукой вождя.',
     'photo': 'http://leninstatues.ru/sites/default/files/styles/large/public/photos/magadan.jpg?itok=0eLHNr7Z',
     'coord': {'lat': 59.55328768018911,
               'lon': 150.81183262713472}},
    {'name': 'Свято-Троицкий собор',
     'desc': '<b>Свято-Троицкий собор.</b>\nСвято-Троицкий собор г. Магадана (Собор Троицы Живоначальной) — кафедральный собор Магаданской и Синегорской епархии Русской Православной Церкви. Храм-памятник жертвам политических репрессий, один из крупнейших храмов на Дальнем Востоке. Общая площадь Собора с учётом прилегающей территории — более 9 тыс. кв. метров.',
     'photo': 'https://dynamic-media-cdn.tripadvisor.com/media/photo-o/16/71/89/a5/photo0jpg.jpg?w=1200&h=-1&s=1',
     'coord': {'lat': 59.567423593845156, 'lon': 150.81276047673234}},
    {'name': 'Областной краеведческий музей',
     'desc': '<b>Областной краеведческий музей.</b>\nОснован в 1934 году в Магадане на базе выставки, проходившей в городе вместе со съездом колхозников. Материалы музея рассказывают о разных периодах. Например, о давнем прошлом региона, который населяли эвены и якуты, а также о временах сталинских репрессий.',
     'photo': 'https://www.kolyma.ru/magadan/uploads/posts/2019-10/1571682320_muzey.jpg',
     'coord': {'lat': 59.55890106597851,
               'lon': 150.81527719999997}},
    {'name': 'Парк Маяк',
     'desc': '<b>Парк маяк.</b>\nПарк «Маяк» — самое масштабное общественное пространство в Магаданской области. В нём можно играть в пляжный волейбол, проводить флешмобы и спортивные соревнования, а также там расположены площадки для детского отдыха, дорожки для катания на роликах и скейтах.',
     'photo': 'https://avatars.mds.yandex.net/get-altay/5265775/2a0000017bf77fce4eeb08b71c3607f80131/XXXL',
     'coord': {'lat': 59.561852,
               'lon': 150.775449}},
    {'name': 'Стела «Город трудовой доблести»',
     'desc': '<b>Стела «Город трудовой доблести».</b>\nЭто памятник подвигу людей, которые в годы Великой Отечественной войны своим трудом вносили вклад в дело Победы.',
     'photo': 'https://cdn.regnum.ru/uploads/pictures/news/2022/09/26/regnum_picture_1664161054110727_normal.jpg',
     'coord': {'lat': 59.573291989474754,
               'lon': 150.813937469687}},
]

host_photo = [
    r"http://kolyma.ru/uploads/posts/2019-10/1571786224_m2016_hotel-11.jpg",
    r"https://cf.bstatic.com/xdata/images/hotel/max1024x768/38962205.jpg?k=a0b7b656a4da4cc36bd1b9cdbae291192ccd0382a5d6997c1286cbb04554d852&o=&hp=1",
    r"https://cf.bstatic.com/xdata/images/hotel/max1280x900/116558770.jpg?k=de7632ccb02b90de8609cc94b6a1b11c3edb7c972d2d1eeae511ca94a3e58e39&o=&hp=1",
    r"http://tophotels.ru/icache/hotel_photos/1/2008/85040/797404_740x550.jpg",
    r"https://cdn.worldota.net/t/1024x768/content/0a/48/0a48dda1c934aebf3177f7a7de16ef8b1189f849.jpeg"
]

host_name = [
    "Магадан",
    "ВМ-центральная",
    "Отель Silver house",
    "Golden House",
    "Океан"
]

host_desc = [
    f"<b>Магадан</b>\nул. Пролетарская, 8\n84132604557\nhttp://www.magadanhotel.ru/\n{4 * emoji.emojize(':star:')}",
    f"<b>ВМ-центральная</b>\nпр. Ленина, 13\n84132601088\nhttps://hotel-vm-central-magadan.nochi.com/\n{4 * emoji.emojize(':star:')}",
    f"<b>Отель Silver house</b>\nнаб. реки Магаданки ул., 9\n89140340911\nhttps://hotel-silverhouse.ru/\n{5 * emoji.emojize(':star:')}",
    f"<b>Golden House</b>\nул. Транспортная, 1\n84132201111\nhttps://golden-house-hotel-magadan.nochi.com\n {5 * emoji.emojize(':star:')}",
    f"<b>Океан</b>\nул. Портовая, 36; 84132630645; http://otelivmagadane.ru/hotel-ocean/;\n{4 * emoji.emojize(':star:')}"
]

host_coords = [
    (59.56429609976189, 150.7704932596274),
    (59.591629953479625, 150.81198529648498),
    (59.55628159740245, 150.77870404232675),
    (59.556261, 150.779087),
    (59.56369767433912, 150.80543342079102),
    (59.565247893820256, 150.8017490977041),
    (59.5614589036509, 150.80059572089786),
    (59.55328768018911, 150.81183262713472),
    (59.567423593845156, 150.81276047673234),
    (59.55890106597851, 150.81527719999997)
]
host_coord = []
for i in range(len(host_coords)):
    d = dict()
    d["lat"] = host_coords[i][0]
    d["lon"] = host_coords[i][1]
    host_coord.append(d)

hostel_keys = ["name", "desc", "photo", "coord"]
host_all = []
for i in range(len(host_desc)):
    info = dict()
    info[hostel_keys[0]] = host_name[i]
    info[hostel_keys[1]] = host_desc[i]
    info[hostel_keys[2]] = host_photo[i]
    info[hostel_keys[3]] = host_coord[i]
    host_all.append(info)
# print(host_all)

host_all = [
    {'name': 'Магадан', 'desc': '<b>Магадан</b>\nул. Пролетарская, 8\n84132604557\nhttp://www.magadanhotel.ru/\n⭐⭐⭐⭐',
     'photo': 'http://kolyma.ru/uploads/posts/2019-10/1571786224_m2016_hotel-11.jpg',
     'coord': {'lat': 59.56429609976189, 'lon': 150.7704932596274}},
    {'name': 'ВМ-центральная',
     'desc': '<b>ВМ-центральная</b>\nпр. Ленина, 13\n84132601088\nhttps://hotel-vm-central-magadan.nochi.com/\n⭐⭐⭐⭐',
     'photo': 'https://cf.bstatic.com/xdata/images/hotel/max1024x768/38962205.jpg?k=a0b7b656a4da4cc36bd1b9cdbae291192ccd0382a5d6997c1286cbb04554d852&o=&hp=1',
     'coord': {'lat': 59.591629953479625,
               'lon': 150.81198529648498}},
    {'name': 'Отель Silver house',
     'desc': '<b>Отель Silver house</b>\nнаб. реки Магаданки ул., 9\n89140340911\nhttps://hotel-silverhouse.ru/\n⭐⭐⭐⭐⭐',
     'photo': 'https://cf.bstatic.com/xdata/images/hotel/max1280x900/116558770.jpg?k=de7632ccb02b90de8609cc94b6a1b11c3edb7c972d2d1eeae511ca94a3e58e39&o=&hp=1',
     'coord': {'lat': 59.55628159740245, 'lon': 150.77870404232675}},
    {'name': 'Golden House',
     'desc': '<b>Golden House</b>\nул. Транспортная, 1\n84132201111\nhttps://golden-house-hotel-magadan.nochi.com\n ⭐⭐⭐⭐⭐',
     'photo': 'http://tophotels.ru/icache/hotel_photos/1/2008/85040/797404_740x550.jpg',
     'coord': {'lat': 59.556261, 'lon': 150.779087}},
    {'name': 'Океан',
     'desc': '<b>Океан</b>\nул. Портовая, 36; 84132630645; http://otelivmagadane.ru/hotel-ocean/;\n⭐⭐⭐⭐',
     'photo': 'https://cdn.worldota.net/t/1024x768/content/0a/48/0a48dda1c934aebf3177f7a7de16ef8b1189f849.jpeg',
     'coord': {'lat': 59.56369767433912, 'lon': 150.80543342079102}}
]

cafe_photo = [
    r"https://lh3.googleusercontent.com/p/AF1QipOwZ72-AVsNCC5jH_2SmawbTHLmdJ4DKOqBIHLp=s1360-w1360-h1020",
    r"https://lh3.googleusercontent.com/p/AF1QipNKtq3QcXIHzA65Z6Xlg2m_lV4ihQ0R1OvqaR5L=s1360-w1360-h1020",
    r"https://avatars.mds.yandex.net/get-altay/2436798/2a00000182b9e3513660208eaae249ab885c/XXL_height",
    r"https://lh3.googleusercontent.com/p/AF1QipPeN_POZHJPfZ1YWUcY61PvQN0Ob5g_RYgnfZQr=s1360-w1360-h1020",
    r"https://lh3.googleusercontent.com/p/AF1QipNlUXdfqKq_vrQeN1wO2q7a3I4DZUM3NnsQ4tYf=s1360-w1360-h1020"
]

cafe_name = [
    "Чайная ложка",
    "Додо Пицца",
    "Казбеги",
    "Pinokio Pizza Bar",
    "ДА-ДА КАФЕ"
]

cafe_desc = [
    f"<b>Чайная ложка</b>\nул. Парковая, 1/28\n8413264315\nhttps://magadan.fudstor.ru/catalog/TEASPOON\n{4 * emoji.emojize(':star:')}",
    f"<b>Додо Пицца</b>\nул. Скуридина, 1/23\n88003020060\nhttps://dodopizza.ru/magadan\n{4 * emoji.emojize(':star:')}",
    f"<b>Казбеги</b>\nул. Пролетарская, 8\n89246909967\nhttps://restaurantguru.ru/Kazbegi-Magadan\n{4 * emoji.emojize(':star:')}",
    f"<b>Pinokio Pizza Bar</b>\n2й километр осн. трассы\n84132685858\nhttps://pinokiopizza.com/#!/Dop_nachinki_k_PIZZA\n{4 * emoji.emojize(':star:')}",
    f"<b>ДА-ДА КАФЕ</b>\nул. Пушкина, 7\n84132661248\nhttps://restaurantguru.ru/Da-Da-Kafe-Magadan\n{4 * emoji.emojize(':star:')}"
]

cafe_coords = [
    (59.56380075002988, 150.81499261534213),
    (59.559582342375755, 150.80505999260498),
    (59.56766776923208, 150.80905122328923),
    (59.57144854847713, 150.811473),
    (59.567949692542975, 150.80250828465785)
]

cafe_coord = []
for i in range(len(cafe_coords)):
    d = dict()
    d["lat"] = host_coords[i][0]
    d["lon"] = host_coords[i][1]
    cafe_coord.append(d)

cafe_keys = ["name", "desc", "photo", "coord"]
cafe_all = []
for i in range(len(cafe_desc)):
    info = dict()
    info[cafe_keys[0]] = cafe_name[i]
    info[cafe_keys[1]] = cafe_desc[i]
    info[cafe_keys[2]] = cafe_photo[i]
    info[cafe_keys[3]] = cafe_coord[i]
    cafe_all.append(info)
print(cafe_all)

cafe_all = [
    {'name': 'Чайная ложка',
     'desc': '<b>Чайная ложка</b>\nул. Парковая, 1/28\n8413264315\nhttps://magadan.fudstor.ru/catalog/TEASPOON\n⭐⭐⭐⭐',
     'photo': 'https://lh3.googleusercontent.com/p/AF1QipOwZ72-AVsNCC5jH_2SmawbTHLmdJ4DKOqBIHLp=s1360-w1360-h1020',
     'coord': {'lat': 59.56429609976189, 'lon': 150.7704932596274}},
    {'name': 'Додо Пицца',
     'desc': '<b>Додо Пицца</b>\nул. Скуридина, 1/23\n88003020060\nhttps://dodopizza.ru/magadan\n⭐⭐⭐⭐',
     'photo': 'https://lh3.googleusercontent.com/p/AF1QipNKtq3QcXIHzA65Z6Xlg2m_lV4ihQ0R1OvqaR5L=s1360-w1360-h1020',
     'coord': {'lat': 59.591629953479625,
               'lon': 150.81198529648498}},
    {'name': 'Казбеги',
     'desc': '<b>Казбеги</b>\nул. Пролетарская, 8\n89246909967\nhttps://restaurantguru.ru/Kazbegi-Magadan\n⭐⭐⭐⭐',
     'photo': 'https://avatars.mds.yandex.net/get-altay/2436798/2a00000182b9e3513660208eaae249ab885c/XXL_height',
     'coord': {'lat': 59.55628159740245, 'lon': 150.77870404232675}},
    {'name': 'Pinokio Pizza Bar',
     'desc': '<b>Pinokio Pizza Bar</b>\n2й километр осн. трассы\n84132685858\nhttps://pinokiopizza.com/#!/Dop_nachinki_k_PIZZA\n⭐⭐⭐⭐',
     'photo': 'https://lh3.googleusercontent.com/p/AF1QipPeN_POZHJPfZ1YWUcY61PvQN0Ob5g_RYgnfZQr=s1360-w1360-h1020',
     'coord': {'lat': 59.556261,
               'lon': 150.779087}},
    {'name': 'ДА-ДА КАФЕ',
     'desc': '<b>ДА-ДА КАФЕ</b>\nул. Пушкина, 7\n84132661248\nhttps://restaurantguru.ru/Da-Da-Kafe-Magadan\n⭐⭐⭐⭐',
     'photo': 'https://lh3.googleusercontent.com/p/AF1QipNlUXdfqKq_vrQeN1wO2q7a3I4DZUM3NnsQ4tYf=s1360-w1360-h1020',
     'coord': {'lat': 59.56369767433912, 'lon': 150.80543342079102}}
]

interesting_facts = [
    "Положением на сегодня в Магадане проживает чуть более 90 000 человек.",
    "Магадан был основан в 1929 г.",
    "Продукты в местных магазинах стоят дороже, чем в Москве, по причине дорогой доставки.",
    "Летом здесь можно наблюдать белые ночи.",
    "Магаданская область относится к числу наименее густонаселенных регионов РФ.",
    "Магадан часто называют «столицей Колымы».",
    "Интересен факт, что попасть в Магадан можно только на самолете или на автомобиле. Здесь нет железнодорожного сообщения, а в местный порт приходят исключительно грузовые судна.",
    "Магаданцы называют центральную часть РФ материком.",
    "Изначально город основывался как рабочий поселок, для исследования и добычи полезных ископаемых.",
    "Несмотря на суровые погодные условия в Магадане установлено множество фонтанов."
]

fact_indexes = []
