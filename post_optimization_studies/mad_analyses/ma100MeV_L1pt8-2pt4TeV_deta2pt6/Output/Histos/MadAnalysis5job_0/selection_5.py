def selection_5():

    # Library import
    import numpy
    import matplotlib
    import matplotlib.pyplot   as plt
    import matplotlib.gridspec as gridspec

    # Library version
    matplotlib_version = matplotlib.__version__
    numpy_version      = numpy.__version__

    # Histo binning
    xBinning = numpy.linspace(-3.2,3.2,65,endpoint=True)

    # Creating data sequence: middle of each bin
    xData = numpy.array([-3.15,-3.05,-2.95,-2.85,-2.75,-2.65,-2.55,-2.45,-2.35,-2.25,-2.15,-2.05,-1.95,-1.85,-1.75,-1.65,-1.55,-1.45,-1.35,-1.25,-1.15,-1.05,-0.95,-0.85,-0.75,-0.65,-0.55,-0.45,-0.35,-0.25,-0.15,-0.05,0.05,0.15,0.25,0.35,0.45,0.55,0.65,0.75,0.85,0.95,1.05,1.15,1.25,1.35,1.45,1.55,1.65,1.75,1.85,1.95,2.05,2.15,2.25,2.35,2.45,2.55,2.65,2.75,2.85,2.95,3.05,3.15])

    # Creating weights for histo: y6_PHI_0
    y6_PHI_0_weights = numpy.array([0.495328359752,1.11979550901,1.10741231002,1.11802630915,1.10564311016,1.2011707024,1.16225230556,1.16755910513,1.13925470743,1.15340710628,1.16225230556,1.11448830944,1.11802630915,1.19940190254,1.14102390729,1.08618391174,1.1728663047,1.20470870211,1.17109750484,1.07026271303,1.11979550901,1.11802630915,1.132178708,1.13925470743,1.14809990671,1.14986910657,1.17109750484,1.10918150987,1.17463550455,1.09856711074,1.18524950369,1.1728663047,1.16579030527,1.15163790642,1.12156470887,1.20293990225,1.13925470743,1.09679791088,1.10741231002,1.15340710628,1.10210511045,1.15163790642,1.13571670772,1.08087671217,1.09149111131,1.15517590614,1.19940190254,1.06318671361,1.19055670326,1.11448830944,1.11448830944,1.09149111131,1.17109750484,1.20647790197,1.10564311016,1.13040950815,1.144561907,1.13394790786,1.18348070384,1.11448830944,1.13571670772,1.07380071275,1.21001590168,0.428105165214])

    # Creating weights for histo: y6_PHI_1
    y6_PHI_1_weights = numpy.array([0.279952490153,0.732001580976,0.72447838738,0.729839307303,0.707395625999,0.681735712487,0.749095133741,0.713807706691,0.728767762808,0.668937130682,0.728788546215,0.719144645759,0.712734963153,0.781140349324,0.697796889486,0.691311267509,0.671084216481,0.69778529874,0.706368446084,0.699939578795,0.746966832945,0.724487580041,0.702045897142,0.730904057223,0.708465571771,0.744806957357,0.720226581958,0.711651428231,0.722346089775,0.699882024745,0.700965559667,0.707346065568,0.681739309616,0.718091886267,0.704220161243,0.719147843206,0.74369024892,0.728713006524,0.679638586801,0.722393651802,0.741577535678,0.708462374324,0.729831713366,0.685018291726,0.663583405016,0.724515557704,0.7320031797,0.648646530392,0.707340869716,0.705267724884,0.733042350042,0.724460801421,0.692432772116,0.686046670683,0.692423579456,0.731980797569,0.674279665283,0.705254535414,0.696688974029,0.710667014173,0.752309367546,0.694563870679,0.741538766631,0.295997719884])

    # Creating weights for histo: y6_PHI_2
    y6_PHI_2_weights = numpy.array([0.187504837156,0.488901696882,0.441678087524,0.491679297432,0.486818096469,0.471540093441,0.456956090551,0.472928893716,0.470150893166,0.491679297432,0.452789289726,0.477095694542,0.493762897845,0.472234493579,0.459734091102,0.465289692203,0.450011689175,0.457650890689,0.46320649179,0.474317693992,0.445150488212,0.48056809523,0.465289692203,0.466678892478,0.498624098808,0.464595292065,0.47779009468,0.486123696331,0.490290497157,0.471540093441,0.484040095918,0.461122891377,0.45140048945,0.479178894955,0.458345290827,0.470845293304,0.483345695781,0.470150893166,0.466678892478,0.471540093441,0.464595292065,0.489596097019,0.500707299221,0.463900891927,0.488206896744,0.482651295643,0.4486228889,0.509040900872,0.481262495368,0.465289692203,0.46598409234,0.466678892478,0.488901696882,0.47779009468,0.476401294405,0.484734896056,0.467373292616,0.4486228889,0.461817291515,0.493762897845,0.472234493579,0.455567290276,0.454178490001,0.187504837156])

    # Creating weights for histo: y6_PHI_3
    y6_PHI_3_weights = numpy.array([0.136082639852,0.327167375811,0.340917859838,0.315787612478,0.31104609109,0.316735932756,0.328589816227,0.318158413173,0.3233741347,0.322899974561,0.330960616922,0.333331377616,0.320055013728,0.320529173867,0.327167375811,0.317210092895,0.315313492339,0.338072939005,0.328589816227,0.341866180115,0.333331377616,0.342340340254,0.337124618727,0.321951654283,0.326693215672,0.316735932756,0.333805537755,0.328115656089,0.31910673345,0.322899974561,0.347556061782,0.323848294839,0.324796575117,0.332857217477,0.321951654283,0.324322414978,0.346607741504,0.335228018171,0.327167375811,0.342814500393,0.340917859838,0.350875142754,0.31104609109,0.299192167618,0.315313492339,0.319580893589,0.317210092895,0.333331377616,0.330960616922,0.328589816227,0.334753858033,0.322425814422,0.323848294839,0.323848294839,0.331908937199,0.325270735255,0.310097770812,0.317684253034,0.325270735255,0.307726970118,0.330012296644,0.328115656089,0.330486456783,0.131341118463])

    # Creating weights for histo: y6_PHI_4
    y6_PHI_4_weights = numpy.array([0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0])

    # Creating weights for histo: y6_PHI_5
    y6_PHI_5_weights = numpy.array([0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,1.05462838872,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,1.0521138287,0.0,0.0,0.0,1.0529581672,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0])

    # Creating weights for histo: y6_PHI_6
    y6_PHI_6_weights = numpy.array([0.459442979787,0.230587829834,0.0,0.461123708475,0.690123184376,0.690865948106,0.691074982492,1.15160232816,0.230350860154,0.69022693306,0.229469726419,0.461390765274,0.461119865931,0.230754711514,0.460486230447,0.0,0.460806698606,0.460768657422,0.230587829834,0.0,0.0,0.460467017728,0.460752134483,0.460862031238,1.15236661013,0.46067912615,0.460948488475,0.690883239553,0.0,0.230587829834,0.0,0.690292640561,0.460579220009,0.230663835352,0.230176946618,0.0,0.0,0.23082921844,0.230119231609,0.230176946618,0.230010871872,0.69090398929,0.460467017728,0.230742914905,0.0,1.15171414619,0.691240980387,0.920008750893,0.23082921844,0.0,0.0,0.921808598441,0.691039631089,0.230635900058,0.69126134587,0.230635900058,0.460432050579,0.46105492694,0.920813763833,0.229694015705,0.230488999606,0.230587829834,0.461256276239,0.460772499966])

    # Creating weights for histo: y6_PHI_7
    y6_PHI_7_weights = numpy.array([0.193953242887,0.33211469419,0.636920712446,0.581157042171,0.609248344512,0.36005542635,0.387592804309,0.387800155682,0.304521112084,0.415347497278,0.554104035481,0.470721470074,0.443295692549,0.415374810724,0.443125656729,0.637069205266,0.609225647422,0.470719931289,0.498349213223,0.276888752578,0.581567513256,0.332161550214,0.415312489903,0.637171919211,0.471043076286,0.470662996218,0.442992167069,0.553904378036,0.332261263528,0.442882143892,0.415257093618,0.415482910419,0.470872655769,0.5260385078,0.470554896522,0.359854383998,0.608975594746,0.470909971323,0.747760600485,0.581389398811,0.637162686497,0.360117285535,0.52615468612,0.470594904951,0.664543454541,0.498468469115,0.332273419935,0.470659149254,0.525963107301,0.249182377479,0.637073436926,0.359864155288,0.304529190708,0.387608576862,0.249170990465,0.581519426203,0.470678768771,0.332382673719,0.415368655581,0.636746829662,0.276993505414,0.63682338425,0.470990757572,0.138371995656])

    # Creating weights for histo: y6_PHI_8
    y6_PHI_8_weights = numpy.array([0.0503702740897,0.201606912833,0.181546788562,0.100889411387,0.181510561864,0.181170989669,0.13104567966,0.221776020604,0.110940651274,0.231762028162,0.110734881203,0.201639923425,0.2319181003,0.22193640111,0.251983200433,0.21166452425,0.191564411044,0.181565296338,0.241923101086,0.141181145102,0.242160850167,0.141225199679,0.171437416051,0.171379040702,0.181573913074,0.171358833851,0.171334561356,0.262177405311,0.181436409394,0.161258563525,0.191555005452,0.14115207879,0.211744138031,0.151254290915,0.191554337959,0.171289899967,0.181481131465,0.161275675634,0.191444262197,0.252034658121,0.2519904215,0.191573027779,0.171471154818,0.161285445313,0.151211389281,0.151156654806,0.242026380549,0.302511979979,0.261938503286,0.181447453379,0.181549701261,0.282420483508,0.151303564078,0.181473000179,0.141051529982,0.201676453529,0.221905392998,0.191587591276,0.121100207167,0.161319972936,0.221784940745,0.181588901339,0.21170184321,0.0705538300626])

    # Creating weights for histo: y6_PHI_9
    y6_PHI_9_weights = numpy.array([0.0509131957296,0.0933602560775,0.0763766611791,0.0848608408032,0.0707191563707,0.101857209024,0.118843804884,0.104687115645,0.110378400506,0.0509520158587,0.0905484321736,0.115994930649,0.116055411564,0.0933687203276,0.0961863922589,0.0792155706836,0.113179220885,0.0933706824947,0.0933684510106,0.104692309616,0.101849745095,0.104690039658,0.0764224835516,0.0707040746158,0.0990092581619,0.0764199442766,0.0848567240997,0.101831046797,0.118813641375,0.0763662347619,0.0933597559172,0.132993568828,0.090535543429,0.107506942112,0.0989553562779,0.107498439388,0.118838533965,0.0962057061389,0.0849067016495,0.0905600897545,0.132995761839,0.104731514484,0.0820245475215,0.124454448526,0.101854900593,0.0877163325431,0.0990056031448,0.124485073722,0.0763475364638,0.0989745932101,0.0819926911618,0.0905353510597,0.0820039255302,0.130128150831,0.0764131344026,0.0990369593443,0.121690139845,0.0848462207347,0.0735495246772,0.121638315549,0.104696503268,0.101828699891,0.110300221614,0.0339694751442])

    # Creating weights for histo: y6_PHI_10
    y6_PHI_10_weights = numpy.array([0.00912998963203,0.00914403459212,0.0183063200711,0.00759778703516,0.0121602441178,0.0121703926884,0.0152422078745,0.00610502917941,0.0152322128912,0.00760511432675,0.0152244508296,0.0198053549182,0.0167240173247,0.0274654700081,0.0106791328987,0.0136703136156,0.0137342531546,0.0106388304321,0.0106286145194,0.0167629930341,0.0106784393934,0.013705343315,0.0015226671937,0.0137628676342,0.00455922702537,0.0213047560117,0.01826205151,0.0213112893756,0.0137371240541,0.0198064063999,0.0122021497987,0.007601469584,0.013693682501,0.0121891657718,0.00609380904264,0.018313326011,0.0182463856141,0.0106802540854,0.0182655013152,0.0106476959587,0.00762241888012,0.0137506161002,0.00910841417265,0.0107169496154,0.0121796433645,0.00917645567177,0.0229213677791,0.0182575502232,0.00611752054575,0.0121513360593,0.0106440015955,0.0121668129248,0.0167522301147,0.00911429183722,0.0152741303865,0.0106545305898,0.0122008856578,0.0060847722072,0.0060821364143,0.0121679234786,0.0182683485858,0.0197938004339,0.0152128136445,0.00913477328306])

    # Creating weights for histo: y6_PHI_11
    y6_PHI_11_weights = numpy.array([0.000361498075422,0.0025275048878,0.00234682380282,0.00216647930431,0.00379168557445,0.00270802268598,0.00198417960037,0.0023476906863,0.00198739565722,0.00252758845675,0.00289046796165,0.00270956620841,0.000902097975151,0.00288932341358,0.00306979692406,0.00180620969252,0.00198718423161,0.00252847112976,0.00198616022309,0.00198789244962,0.00162485774524,0.00307122298782,0.00162694465843,0.00271012307803,0.00270913103367,0.00216609149815,0.00180594897278,0.00234850365433,0.00198414185956,0.002164339631,0.00216570561755,0.00180520493952,0.00180477977765,0.00252648935171,0.00216539752924,0.00180700648591,0.00270697364529,0.00252562246823,0.00162390844813,0.000902973716171,0.00198606240506,0.00126568107672,0.00126484692762,0.00198529796094,0.00198723237041,0.0014454983591,0.00162334387631,0.00162491243091,0.00252868717669,0.00180701303278,0.0016254531259,0.00162393425053,0.00288858977829,0.0023457924772,0.00216758264557,0.00216732000029,0.00216595324352,0.0014436740912,0.00198733904599,0.00180504242293,0.00180715552363,0.00180491957272,0.00162447109441,0.000901844187406])

    # Creating weights for histo: y6_PHI_12
    y6_PHI_12_weights = numpy.array([0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0121313846429,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0242945760233,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0121753353338,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0])

    # Creating weights for histo: y6_PHI_13
    y6_PHI_13_weights = numpy.array([0.0,0.0200698970219,0.0100299570107,0.050250317505,0.0100407292302,0.0100299570107,0.0,0.0100584804597,0.0,0.040135757044,0.0100367004945,0.0,0.0301512400403,0.0401515579521,0.0100184162323,0.0200696201754,0.0201006435066,0.0502126746512,0.0200560918874,0.0100262836301,0.0300849497764,0.0200748224096,0.0100696700149,0.0200856359495,0.0,0.0100459438605,0.0100184162323,0.0200698970219,0.0100187054749,0.0100584804597,0.0100299570107,0.0201156386676,0.0200646452033,0.0201072671613,0.0,0.0301018415422,0.0501547848177,0.0,0.0200629841246,0.0201027343171,0.0100584804597,0.0,0.0100584804597,0.0300858299002,0.0401631689751,0.0100184162323,0.0100367004945,0.0100568565693,0.0200707936738,0.0100153626572,0.0200777065712,0.0301217331666,0.0301422074082,0.0201043829998,0.0200795287993,0.0100329196809,0.0200975857995,0.0200759008711,0.0200666575052,0.0401428269587,0.020107903495,0.0401912668243,0.0100609844739,0.0200794007062])

    # Creating weights for histo: y6_PHI_14
    y6_PHI_14_weights = numpy.array([0.0549453092886,0.115545247181,0.164966420858,0.0879930657527,0.120993938994,0.148522881944,0.121005639486,0.110015261323,0.0880563621666,0.0604731825582,0.115485932185,0.131950393854,0.104489175629,0.0935093197833,0.093560184424,0.10453471817,0.10992121049,0.110024199199,0.120957537462,0.099010013784,0.11004418754,0.109937989321,0.0769755895741,0.0990243143859,0.126472938331,0.0879935532732,0.0989759686012,0.126567395432,0.148470229729,0.0935735099848,0.0989495612399,0.115488451041,0.0769762396015,0.115546831623,0.0770224321705,0.115479513165,0.0714914306443,0.0935098073038,0.137528806751,0.0934986349586,0.131967172685,0.143024219279,0.115472200357,0.110061413265,0.0935560811263,0.0880256077473,0.0714980934247,0.0935464932228,0.0935994704524,0.131970869716,0.121074908026,0.0990157421501,0.0989776342963,0.109971912624,0.0715135722011,0.0880577434747,0.11556255416,0.0990331710086,0.110035818438,0.0989953069151,0.143001996469,0.109988000801,0.0934824249014,0.0220203308043])

    # Creating weights for histo: y6_PHI_15
    y6_PHI_15_weights = numpy.array([0.0543069028843,0.0996853489195,0.113488843416,0.129276198936,0.0947471406868,0.112502845166,0.1233495474,0.104606962848,0.118397871327,0.117424499178,0.132190543451,0.109530701169,0.0996617000326,0.0897936608849,0.1046166629,0.112502684835,0.0887947559549,0.113490406647,0.113486839273,0.109574792314,0.0907878360374,0.122391727401,0.108548310377,0.117428066553,0.103629502248,0.0996534429637,0.0947468601068,0.105599614852,0.10163690316,0.10262963533,0.0927599928675,0.113497501313,0.122372407463,0.104603716137,0.113492170293,0.0977082618977,0.102658214408,0.11251887831,0.0898059262397,0.0966993362531,0.111526667217,0.107576301046,0.103614711673,0.0907854310659,0.103606935599,0.103613068276,0.108532918559,0.115482404492,0.115466611846,0.109540842132,0.0789447140109,0.114460131256,0.0996699571016,0.113504475731,0.0898058059911,0.0838641634655,0.102637531653,0.123333514256,0.102632481213,0.126328585649,0.107576982454,0.10064417099,0.0779569921986,0.0542823320918])

    # Creating weights for histo: y6_PHI_16
    y6_PHI_16_weights = numpy.array([0.0209221536774,0.0438571067964,0.0541935364767,0.0471344986429,0.0511652108864,0.0521757997216,0.0458777243178,0.047388846304,0.0476517162323,0.0514258802292,0.0488938866724,0.0489041293972,0.0514333622196,0.0441106542447,0.0511725728448,0.043616482786,0.0458680817527,0.0473874059209,0.0519214120498,0.0484035962462,0.0446185893648,0.048650341885,0.0506686387891,0.0501606636584,0.0463883801616,0.0468855524186,0.0488996882157,0.0486479012358,0.0489046895462,0.048645860693,0.0413430380079,0.0476357119748,0.0426040934718,0.049918239169,0.0486438601608,0.0509190654072,0.0546976705856,0.0499108772106,0.0506609167349,0.0478925803065,0.0514265604102,0.044867535589,0.0483913929999,0.0501691859255,0.0494099039425,0.0494080634529,0.0453751106133,0.0446166288432,0.0471420606545,0.0461311517342,0.0456282179445,0.050163624446,0.0481573707456,0.0461303915319,0.0526796937667,0.0456251771356,0.0441190564798,0.0511716926107,0.0514330421344,0.0431101480917,0.0501624241267,0.048905049642,0.0476451944974,0.0201656204256])

    # Creating weights for histo: y6_PHI_17
    y6_PHI_17_weights = numpy.array([0.0111596028653,0.0297807229035,0.0226244293467,0.0246211250795,0.0294793584481,0.0231795986013,0.0209003243273,0.0303493292356,0.0243439653598,0.0252000791611,0.0217688354323,0.0246268338379,0.0263402811752,0.0260633314098,0.0234682258269,0.024052308793,0.0260498943323,0.0280497293823,0.0297548285353,0.0223453500445,0.0257678256802,0.030625189238,0.0240468399825,0.0269143863114,0.0272009439871,0.0246332124506,0.027749854603,0.0288958753516,0.0229131465527,0.0266340072919,0.0243219601458,0.0243242196543,0.0254827576805,0.0200469699259,0.0246473393781,0.021471540092,0.0237685005193,0.0303419208469,0.0217533388027,0.0249146212462,0.0243555428418,0.0220492244497,0.0234785135894,0.0280660658293,0.029507792264,0.0240533385691,0.0237554033679,0.0257524290289,0.0194646965662,0.0269202850285,0.0246313428572,0.0243132620375,0.0251814532121,0.0286196554274,0.0289276084498,0.0266243893837,0.0220565828493,0.0231965549134,0.0217562881613,0.0257654162043,0.026060741973,0.0234758841613,0.022338441547,0.00973010877019])

    # Creating weights for histo: y6_PHI_18
    y6_PHI_18_weights = numpy.array([0.00162030783856,0.00354273991526,0.00429872380897,0.0041251565936,0.00382356797654,0.00377818519621,0.00390888721797,0.00317491324348,0.00375870627521,0.0042986399872,0.00364905608987,0.00388836262045,0.00371597310089,0.0036487157735,0.00412447176978,0.00390924387959,0.00377883481489,0.00401803908291,0.00453420848614,0.00399588331383,0.00367258569769,0.00373654589593,0.0037804349724,0.00321919502491,0.00364914116896,0.00375473815283,0.0040365108854,0.00315336518219,0.00349886466939,0.00369239361912,0.00373696751941,0.00421186769546,0.00386583594006,0.00368594395337,0.00349766727547,0.00401678301376,0.00362222180894,0.00384273591878,0.00345389177749,0.00328360827979,0.00334577804512,0.00380000400179,0.00388871006167,0.0033866009214,0.00347790838977,0.00379812094583,0.00367219760292,0.00347599976817,0.00401314808289,0.00362841372277,0.00381851142853,0.00375751516792,0.00360438914742,0.004037603083,0.00384456574793,0.0035624866468,0.00390652805438,0.00341303956359,0.00418849525345,0.00382132616342,0.00369370794441,0.00354081327198,0.00390964748139,0.00155505971889])

    # Creating weights for histo: y6_PHI_19
    y6_PHI_19_weights = numpy.array([0.000198439362762,0.000511161280941,0.00062309513129,0.000822093412484,0.000878604031765,0.000369290315634,0.00065174879842,0.000768243114236,0.000538787714514,0.000451854732728,0.000708717335726,0.000624607612395,0.000567739332847,0.000677134508242,0.000737970321452,0.000963366841556,0.000708097519989,0.000764843262277,0.000652727759725,0.00082098612125,0.000393823611721,0.000709978801112,0.000818310798686,0.000877778501962,0.000823567127256,0.000736461256537,0.000652348859666,0.000850873775715,0.000905538761075,0.000681823749229,0.000936789772513,0.000881862037563,0.000681327956051,0.000567366373989,0.000736182317176,0.000621152804332,0.000679946329886,0.000765969416823,0.000622206624762,0.000567070947796,0.000735465808402,0.000594495677613,0.000596332399733,0.000682324295367,0.000791300913191,0.000879998134451,0.000737217422825,0.000907013218497,0.000652743206846,0.000710367949742,0.000539195132335,0.000596679811429,0.000679511434013,0.00062138763028,0.000710039995477,0.000766114530644,0.000654153350773,0.00107755270394,0.00102218264661,0.000852072412906,0.000652654831489,0.000650908861206,0.000564995092358,0.000170276438789])

    # Creating a new Canvas
    fig   = plt.figure(figsize=(12,6),dpi=80)
    frame = gridspec.GridSpec(1,1,right=0.7)
    pad   = fig.add_subplot(frame[0])

    # Creating a new Stack
    pad.hist(x=xData, bins=xBinning, weights=y6_PHI_0_weights+y6_PHI_1_weights+y6_PHI_2_weights+y6_PHI_3_weights+y6_PHI_4_weights+y6_PHI_5_weights+y6_PHI_6_weights+y6_PHI_7_weights+y6_PHI_8_weights+y6_PHI_9_weights+y6_PHI_10_weights+y6_PHI_11_weights+y6_PHI_12_weights+y6_PHI_13_weights+y6_PHI_14_weights+y6_PHI_15_weights+y6_PHI_16_weights+y6_PHI_17_weights+y6_PHI_18_weights+y6_PHI_19_weights,\
             label="$bg\_vbf\_1600\_inf$", histtype="step", rwidth=1.0,\
             color=None, edgecolor="#ccc6aa", linewidth=1, linestyle="solid",\
             bottom=None, cumulative=False, normed=False, align="mid", orientation="vertical")

    pad.hist(x=xData, bins=xBinning, weights=y6_PHI_0_weights+y6_PHI_1_weights+y6_PHI_2_weights+y6_PHI_3_weights+y6_PHI_4_weights+y6_PHI_5_weights+y6_PHI_6_weights+y6_PHI_7_weights+y6_PHI_8_weights+y6_PHI_9_weights+y6_PHI_10_weights+y6_PHI_11_weights+y6_PHI_12_weights+y6_PHI_13_weights+y6_PHI_14_weights+y6_PHI_15_weights+y6_PHI_16_weights+y6_PHI_17_weights+y6_PHI_18_weights,\
             label="$bg\_vbf\_1200\_1600$", histtype="step", rwidth=1.0,\
             color=None, edgecolor="#c1bfa8", linewidth=1, linestyle="solid",\
             bottom=None, cumulative=False, normed=False, align="mid", orientation="vertical")

    pad.hist(x=xData, bins=xBinning, weights=y6_PHI_0_weights+y6_PHI_1_weights+y6_PHI_2_weights+y6_PHI_3_weights+y6_PHI_4_weights+y6_PHI_5_weights+y6_PHI_6_weights+y6_PHI_7_weights+y6_PHI_8_weights+y6_PHI_9_weights+y6_PHI_10_weights+y6_PHI_11_weights+y6_PHI_12_weights+y6_PHI_13_weights+y6_PHI_14_weights+y6_PHI_15_weights+y6_PHI_16_weights+y6_PHI_17_weights,\
             label="$bg\_vbf\_800\_1200$", histtype="step", rwidth=1.0,\
             color=None, edgecolor="#bab5a3", linewidth=1, linestyle="solid",\
             bottom=None, cumulative=False, normed=False, align="mid", orientation="vertical")

    pad.hist(x=xData, bins=xBinning, weights=y6_PHI_0_weights+y6_PHI_1_weights+y6_PHI_2_weights+y6_PHI_3_weights+y6_PHI_4_weights+y6_PHI_5_weights+y6_PHI_6_weights+y6_PHI_7_weights+y6_PHI_8_weights+y6_PHI_9_weights+y6_PHI_10_weights+y6_PHI_11_weights+y6_PHI_12_weights+y6_PHI_13_weights+y6_PHI_14_weights+y6_PHI_15_weights+y6_PHI_16_weights,\
             label="$bg\_vbf\_600\_800$", histtype="step", rwidth=1.0,\
             color=None, edgecolor="#b2a596", linewidth=1, linestyle="solid",\
             bottom=None, cumulative=False, normed=False, align="mid", orientation="vertical")

    pad.hist(x=xData, bins=xBinning, weights=y6_PHI_0_weights+y6_PHI_1_weights+y6_PHI_2_weights+y6_PHI_3_weights+y6_PHI_4_weights+y6_PHI_5_weights+y6_PHI_6_weights+y6_PHI_7_weights+y6_PHI_8_weights+y6_PHI_9_weights+y6_PHI_10_weights+y6_PHI_11_weights+y6_PHI_12_weights+y6_PHI_13_weights+y6_PHI_14_weights+y6_PHI_15_weights,\
             label="$bg\_vbf\_400\_600$", histtype="step", rwidth=1.0,\
             color=None, edgecolor="#b7a39b", linewidth=1, linestyle="solid",\
             bottom=None, cumulative=False, normed=False, align="mid", orientation="vertical")

    pad.hist(x=xData, bins=xBinning, weights=y6_PHI_0_weights+y6_PHI_1_weights+y6_PHI_2_weights+y6_PHI_3_weights+y6_PHI_4_weights+y6_PHI_5_weights+y6_PHI_6_weights+y6_PHI_7_weights+y6_PHI_8_weights+y6_PHI_9_weights+y6_PHI_10_weights+y6_PHI_11_weights+y6_PHI_12_weights+y6_PHI_13_weights+y6_PHI_14_weights,\
             label="$bg\_vbf\_200\_400$", histtype="step", rwidth=1.0,\
             color=None, edgecolor="#ad998c", linewidth=1, linestyle="solid",\
             bottom=None, cumulative=False, normed=False, align="mid", orientation="vertical")

    pad.hist(x=xData, bins=xBinning, weights=y6_PHI_0_weights+y6_PHI_1_weights+y6_PHI_2_weights+y6_PHI_3_weights+y6_PHI_4_weights+y6_PHI_5_weights+y6_PHI_6_weights+y6_PHI_7_weights+y6_PHI_8_weights+y6_PHI_9_weights+y6_PHI_10_weights+y6_PHI_11_weights+y6_PHI_12_weights+y6_PHI_13_weights,\
             label="$bg\_vbf\_100\_200$", histtype="step", rwidth=1.0,\
             color=None, edgecolor="#9b8e82", linewidth=1, linestyle="solid",\
             bottom=None, cumulative=False, normed=False, align="mid", orientation="vertical")

    pad.hist(x=xData, bins=xBinning, weights=y6_PHI_0_weights+y6_PHI_1_weights+y6_PHI_2_weights+y6_PHI_3_weights+y6_PHI_4_weights+y6_PHI_5_weights+y6_PHI_6_weights+y6_PHI_7_weights+y6_PHI_8_weights+y6_PHI_9_weights+y6_PHI_10_weights+y6_PHI_11_weights+y6_PHI_12_weights,\
             label="$bg\_vbf\_0\_100$", histtype="step", rwidth=1.0,\
             color=None, edgecolor="#876656", linewidth=1, linestyle="solid",\
             bottom=None, cumulative=False, normed=False, align="mid", orientation="vertical")

    pad.hist(x=xData, bins=xBinning, weights=y6_PHI_0_weights+y6_PHI_1_weights+y6_PHI_2_weights+y6_PHI_3_weights+y6_PHI_4_weights+y6_PHI_5_weights+y6_PHI_6_weights+y6_PHI_7_weights+y6_PHI_8_weights+y6_PHI_9_weights+y6_PHI_10_weights+y6_PHI_11_weights,\
             label="$bg\_dip\_1600\_inf$", histtype="step", rwidth=1.0,\
             color=None, edgecolor="#afcec6", linewidth=1, linestyle="solid",\
             bottom=None, cumulative=False, normed=False, align="mid", orientation="vertical")

    pad.hist(x=xData, bins=xBinning, weights=y6_PHI_0_weights+y6_PHI_1_weights+y6_PHI_2_weights+y6_PHI_3_weights+y6_PHI_4_weights+y6_PHI_5_weights+y6_PHI_6_weights+y6_PHI_7_weights+y6_PHI_8_weights+y6_PHI_9_weights+y6_PHI_10_weights,\
             label="$bg\_dip\_1200\_1600$", histtype="step", rwidth=1.0,\
             color=None, edgecolor="#84c1a3", linewidth=1, linestyle="solid",\
             bottom=None, cumulative=False, normed=False, align="mid", orientation="vertical")

    pad.hist(x=xData, bins=xBinning, weights=y6_PHI_0_weights+y6_PHI_1_weights+y6_PHI_2_weights+y6_PHI_3_weights+y6_PHI_4_weights+y6_PHI_5_weights+y6_PHI_6_weights+y6_PHI_7_weights+y6_PHI_8_weights+y6_PHI_9_weights,\
             label="$bg\_dip\_800\_1200$", histtype="step", rwidth=1.0,\
             color=None, edgecolor="#89a8a0", linewidth=1, linestyle="solid",\
             bottom=None, cumulative=False, normed=False, align="mid", orientation="vertical")

    pad.hist(x=xData, bins=xBinning, weights=y6_PHI_0_weights+y6_PHI_1_weights+y6_PHI_2_weights+y6_PHI_3_weights+y6_PHI_4_weights+y6_PHI_5_weights+y6_PHI_6_weights+y6_PHI_7_weights+y6_PHI_8_weights,\
             label="$bg\_dip\_600\_800$", histtype="step", rwidth=1.0,\
             color=None, edgecolor="#829e8c", linewidth=1, linestyle="solid",\
             bottom=None, cumulative=False, normed=False, align="mid", orientation="vertical")

    pad.hist(x=xData, bins=xBinning, weights=y6_PHI_0_weights+y6_PHI_1_weights+y6_PHI_2_weights+y6_PHI_3_weights+y6_PHI_4_weights+y6_PHI_5_weights+y6_PHI_6_weights+y6_PHI_7_weights,\
             label="$bg\_dip\_400\_600$", histtype="step", rwidth=1.0,\
             color=None, edgecolor="#adbcc6", linewidth=1, linestyle="solid",\
             bottom=None, cumulative=False, normed=False, align="mid", orientation="vertical")

    pad.hist(x=xData, bins=xBinning, weights=y6_PHI_0_weights+y6_PHI_1_weights+y6_PHI_2_weights+y6_PHI_3_weights+y6_PHI_4_weights+y6_PHI_5_weights+y6_PHI_6_weights,\
             label="$bg\_dip\_200\_400$", histtype="step", rwidth=1.0,\
             color=None, edgecolor="#7a8e99", linewidth=1, linestyle="solid",\
             bottom=None, cumulative=False, normed=False, align="mid", orientation="vertical")

    pad.hist(x=xData, bins=xBinning, weights=y6_PHI_0_weights+y6_PHI_1_weights+y6_PHI_2_weights+y6_PHI_3_weights+y6_PHI_4_weights+y6_PHI_5_weights,\
             label="$bg\_dip\_100\_200$", histtype="step", rwidth=1.0,\
             color=None, edgecolor="#758991", linewidth=1, linestyle="solid",\
             bottom=None, cumulative=False, normed=False, align="mid", orientation="vertical")

    pad.hist(x=xData, bins=xBinning, weights=y6_PHI_0_weights+y6_PHI_1_weights+y6_PHI_2_weights+y6_PHI_3_weights+y6_PHI_4_weights,\
             label="$bg\_dip\_0\_100$", histtype="step", rwidth=1.0,\
             color=None, edgecolor="#688296", linewidth=1, linestyle="solid",\
             bottom=None, cumulative=False, normed=False, align="mid", orientation="vertical")

    pad.hist(x=xData, bins=xBinning, weights=y6_PHI_0_weights+y6_PHI_1_weights+y6_PHI_2_weights+y6_PHI_3_weights,\
             label="$signal\_2pt4TeVL$", histtype="step", rwidth=1.0,\
             color=None, edgecolor="#6d7a84", linewidth=1, linestyle="solid",\
             bottom=None, cumulative=False, normed=False, align="mid", orientation="vertical")

    pad.hist(x=xData, bins=xBinning, weights=y6_PHI_0_weights+y6_PHI_1_weights+y6_PHI_2_weights,\
             label="$signal\_2pt2TeVL$", histtype="step", rwidth=1.0,\
             color=None, edgecolor="#7c99d1", linewidth=1, linestyle="solid",\
             bottom=None, cumulative=False, normed=False, align="mid", orientation="vertical")

    pad.hist(x=xData, bins=xBinning, weights=y6_PHI_0_weights+y6_PHI_1_weights,\
             label="$signal\_2TeVL$", histtype="step", rwidth=1.0,\
             color=None, edgecolor="#7f7f9b", linewidth=1, linestyle="solid",\
             bottom=None, cumulative=False, normed=False, align="mid", orientation="vertical")

    pad.hist(x=xData, bins=xBinning, weights=y6_PHI_0_weights,\
             label="$signal\_1pt8TeVL$", histtype="step", rwidth=1.0,\
             color=None, edgecolor="#aaa5bf", linewidth=1, linestyle="solid",\
             bottom=None, cumulative=False, normed=False, align="mid", orientation="vertical")


    # Axis
    plt.rc('text',usetex=False)
    plt.xlabel(r"\phi [ j_{2} ] ",\
               fontsize=16,color="black")
    plt.ylabel(r"$\mathrm{Events}$ $(\mathcal{L}_{\mathrm{int}} = 40.0\ \mathrm{fb}^{-1})$ ",\
               fontsize=16,color="black")

    # Boundary of y-axis
    ymax=(y6_PHI_0_weights+y6_PHI_1_weights+y6_PHI_2_weights+y6_PHI_3_weights+y6_PHI_4_weights+y6_PHI_5_weights+y6_PHI_6_weights+y6_PHI_7_weights+y6_PHI_8_weights+y6_PHI_9_weights+y6_PHI_10_weights+y6_PHI_11_weights+y6_PHI_12_weights+y6_PHI_13_weights+y6_PHI_14_weights+y6_PHI_15_weights+y6_PHI_16_weights+y6_PHI_17_weights+y6_PHI_18_weights+y6_PHI_19_weights).max()*1.1
    ymin=0 # linear scale
    #ymin=min([x for x in (y6_PHI_0_weights+y6_PHI_1_weights+y6_PHI_2_weights+y6_PHI_3_weights+y6_PHI_4_weights+y6_PHI_5_weights+y6_PHI_6_weights+y6_PHI_7_weights+y6_PHI_8_weights+y6_PHI_9_weights+y6_PHI_10_weights+y6_PHI_11_weights+y6_PHI_12_weights+y6_PHI_13_weights+y6_PHI_14_weights+y6_PHI_15_weights+y6_PHI_16_weights+y6_PHI_17_weights+y6_PHI_18_weights+y6_PHI_19_weights) if x])/100. # log scale
    plt.gca().set_ylim(ymin,ymax)

    # Log/Linear scale for X-axis
    plt.gca().set_xscale("linear")
    #plt.gca().set_xscale("log",nonposx="clip")

    # Log/Linear scale for Y-axis
    plt.gca().set_yscale("linear")
    #plt.gca().set_yscale("log",nonposy="clip")

    # Legend
    plt.legend(bbox_to_anchor=(1.05,1), loc=2, borderaxespad=0.)

    # Saving the image
    plt.savefig('../../HTML/MadAnalysis5job_0/selection_5.png')
    plt.savefig('../../PDF/MadAnalysis5job_0/selection_5.png')
    plt.savefig('../../DVI/MadAnalysis5job_0/selection_5.eps')

# Running!
if __name__ == '__main__':
    selection_5()
