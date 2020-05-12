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
    y6_PHI_0_weights = numpy.array([11.2914822789,27.606408233,26.685241026,27.4631163564,27.8070200603,27.1355886383,27.2952565009,27.5490922823,26.9390728075,26.7753089485,27.7947360709,27.9134639686,26.9800127723,27.4385523775,27.778360085,26.6688610401,27.5409042894,27.4262683881,27.0700846947,27.3362004656,27.3280084727,27.3607644445,27.0782726877,27.4958683282,27.4794923423,27.5736562612,27.3443884586,27.5449962859,27.5449962859,26.3781812904,27.8684280074,27.59822024,27.5572802753,26.9718247793,26.2103254349,26.8981328428,27.2420365467,27.3812324268,27.4876803352,27.0618967018,27.7087601449,27.6514441942,27.0946486736,26.7957809309,26.9267888181,26.4600652199,27.1355886383,27.0823646842,27.184716596,27.0864606806,27.3976084128,27.4999603246,27.2747885185,27.3689524374,26.6893330225,27.278880515,27.1642486137,27.2911645044,27.4631163564,27.0823646842,27.1683406101,27.1233046489,26.7261809908,11.2710142965])

    # Creating weights for histo: y6_PHI_1
    y6_PHI_1_weights = numpy.array([1.60371454156,3.02537259123,2.98873627611,3.15940575106,3.24454683314,3.15918826424,3.18313864945,3.02598339675,3.74249070998,3.60950893671,3.3779655827,3.02600302263,3.22045145672,3.45066465655,3.159660487,3.28124563067,3.08647877666,3.15905568941,3.45110443652,3.57203191287,3.54664803721,3.43867444414,3.18355760196,3.48720885019,3.28038489555,3.69304750543,3.48660725682,3.1841247499,3.22031127185,3.68110455535,2.8428566935,2.97718263944,2.9763343207,3.49972896142,3.31707568251,3.21983704645,3.53600319904,3.00060953429,3.31707768515,3.0857750486,3.12226517092,3.06195803928,3.18266562564,2.94032723539,3.28003923971,3.21960954643,3.45098788281,3.0861187018,3.14678751042,2.98939434396,3.2685432791,3.20742708047,2.96473542435,3.23172352206,2.8431903335,3.17076272838,3.48622315027,3.53597836629,3.24415792025,2.87858861593,3.20830543883,3.62145268785,3.17100745111,1.3730479438])

    # Creating weights for histo: y6_PHI_2
    y6_PHI_2_weights = numpy.array([5.96423965157,15.0807709193,15.1700364218,15.5128551234,15.8123488798,15.5913441397,14.1873307979,15.401441628,15.4523448231,14.7290640958,14.447623433,15.2209933341,14.9401642203,15.1405539721,14.9096074277,15.0607550838,14.5379136934,15.2014444246,15.3713517613,14.9591305054,14.8596050278,14.8894221766,15.2300756641,14.8090943811,15.0494455583,15.0501438812,14.930222416,15.0402475298,14.7990203499,14.6682521531,15.0796883122,15.3903552352,14.9799603623,15.2206379745,15.2003659495,16.003536471,15.0895350785,15.4619891171,15.0805395224,15.4416757712,14.7982476494,14.8485268992,15.0503463535,15.8126092013,15.4622948916,14.869071642,15.2703676566,15.320113867,14.8588819124,15.0904276096,15.4817198385,15.3422701242,14.6988130778,15.9036804264,14.1672571132,14.8997730577,15.2826151661,15.0309999163,15.622165386,15.6312725085,15.2109564917,15.5014918807,15.4521258224,6.32523954152])

    # Creating weights for histo: y6_PHI_3
    y6_PHI_3_weights = numpy.array([7.63474892917,18.0967387772,18.0195099613,18.4035293344,18.4974104868,18.5205831941,18.3977930331,18.3428269163,18.0301131811,17.8927303895,18.5637882682,18.5097605973,18.7184693395,18.1576036967,17.6385374904,18.4049471596,18.7073542401,18.6290407269,18.1301775139,18.2617508785,18.5257832406,17.87097957,18.6514171771,18.354632647,18.2323015525,19.1027730902,18.3434728596,18.0467939554,18.1338906721,18.4812822175,18.601825796,17.9645763448,18.5581494677,17.78826633,18.3656258703,18.1330741023,19.1737130998,18.3605314497,18.123762769,17.6663130514,18.085534302,17.8262916702,18.304285634,17.6348080821,18.5254663628,18.3269586494,18.0084557999,17.6058259478,18.6186893843,18.49357139,18.0580309309,18.2886651818,18.3066987806,18.3217504778,18.7946378334,18.1020525747,18.2224092765,17.525257727,18.0791236196,18.0914290422,18.6177265632,18.41505475,17.9527584266,7.62853324856])

    # Creating weights for histo: y6_PHI_4
    y6_PHI_4_weights = numpy.array([2.274607791,5.69413024704,5.49875743426,5.61019633584,5.6438300249,5.61117035401,5.63587754735,5.56692668104,5.58859157073,5.5066297457,5.69504414063,5.52937286949,5.52944101068,5.47980215889,5.4395307164,5.6091702097,5.52445868729,5.51847829591,5.64973826678,5.59267603374,5.48701710828,5.5225387091,5.54312937298,5.54698937091,5.66947916997,5.5885675209,5.62884698,5.44433266605,5.47308824766,5.50568779397,5.45919947009,5.55009580745,5.41384950489,5.4849568394,5.651750436,5.62589285906,5.54610353545,5.73070202382,5.67429314453,5.52843492607,5.65089265869,5.68333588109,5.51145574518,5.59639173268,5.51743613656,5.70202660831,5.47503227569,5.47591009453,5.59157374981,5.4701180935,5.47106806183,5.56872641009,5.47121236082,5.58945335635,5.53915714252,5.46221371561,5.59150160032,5.59526940722,5.49977955209,5.56582439711,5.60733841422,5.65753041212,5.50751157284,2.29133725448])

    # Creating weights for histo: y6_PHI_5
    y6_PHI_5_weights = numpy.array([0.73628572975,1.78269756229,1.76814240933,1.75672522236,1.81168383794,1.71624454089,1.74839558907,1.75671001865,1.76359649966,1.79026380924,1.80063874179,1.76152759464,1.77238224429,1.78012773499,1.77914789581,1.76679728098,1.76099426445,1.78795524571,1.76145597715,1.76501444579,1.75523925963,1.74464547365,1.78397427394,1.78548544282,1.76728339965,1.7841703218,1.76502804911,1.78017254593,1.75091300358,1.77790199168,1.7615163919,1.74842639659,1.74310869852,1.78443478636,1.78700461366,1.76878016501,1.76701133323,1.78094273393,1.76855330964,1.76068658934,1.75867089731,1.78773719248,1.78399307853,1.7305344291,1.77218059507,1.76704974261,1.73980829288,1.77132318577,1.79476930905,1.79402832817,1.76303196186,1.81594967924,1.7531879589,1.76403900768,1.80838623298,1.74308789344,1.7809663397,1.77204776264,1.76054495477,1.75194325507,1.80086319658,1.77105432014,1.77490125919,0.734560908715])

    # Creating weights for histo: y6_PHI_6
    y6_PHI_6_weights = numpy.array([0.267108060138,0.640205990393,0.653850316547,0.641613518562,0.636154648482,0.634993037877,0.61462566542,0.63031800504,0.642303087405,0.640539278668,0.643039640498,0.634501802549,0.664223439273,0.674588764612,0.640127416732,0.659343775032,0.623557171404,0.643973227541,0.660787691003,0.652213465252,0.639590896584,0.65617603692,0.636210129884,0.665653359935,0.647912906883,0.629533767931,0.62672990784,0.636151149655,0.645348466534,0.624141175634,0.642139142362,0.637574872395,0.641624814775,0.649612037301,0.642866398572,0.657950542071,0.641354305455,0.656558708641,0.636492835115,0.644153267188,0.634740822424,0.659348073591,0.62843953474,0.65077384784,0.64850070984,0.630447061777,0.645544900685,0.640985529076,0.636741651707,0.634443122219,0.649948224605,0.63848876604,0.644697384789,0.650151156578,0.642761533725,0.6613717952,0.629976319579,0.650717566706,0.639850609524,0.615249656246,0.637882169383,0.634803801313,0.631918968365,0.25342854578])

    # Creating weights for histo: y6_PHI_7
    y6_PHI_7_weights = numpy.array([0.0303409491163,0.0708834225298,0.0737393886703,0.072141611672,0.0720054915489,0.0729045632852,0.0741319912912,0.0708263845103,0.0717770041995,0.0743601014604,0.0714501566504,0.0727240616319,0.0713364158826,0.0709747839424,0.0746530027966,0.0723600408842,0.0712174784106,0.0711546150532,0.0737460521862,0.0726200856389,0.0702820716537,0.0707916420281,0.0720102691641,0.0703783783171,0.0713231307597,0.0721915670866,0.0728969777734,0.070767041501,0.0736860805433,0.0709611216394,0.0719959782275,0.0709268401552,0.0695761999689,0.0677683336304,0.0714153722594,0.0715408475206,0.0717549182067,0.0700786039206,0.0725904560432,0.0716363998237,0.069921152165,0.0706892166646,0.0711009297461,0.0697878399385,0.0712636201148,0.07075865972,0.0701185850158,0.0710510162404,0.071873268954,0.0711539445108,0.0714880842093,0.0716040042402,0.073673424054,0.0706788232562,0.071946860991,0.0723814982435,0.0724426852446,0.0704077983684,0.0728587987611,0.0726401600043,0.0716937731145,0.0710403294696,0.0722103422759,0.0294366136216])

    # Creating weights for histo: y6_PHI_8
    y6_PHI_8_weights = numpy.array([0.00526955831863,0.011648666237,0.0121021948197,0.0124174208187,0.0129193951041,0.0126853727932,0.0122742919305,0.0124423156402,0.0125159323775,0.0125896367308,0.013147572389,0.0132767376643,0.0132927075349,0.0117320113194,0.0131542549645,0.013064699542,0.0122463750998,0.0130742942355,0.012724265383,0.0130987064265,0.0122765996466,0.0135168916095,0.0133762709147,0.0119584184642,0.0128373315913,0.0125559907054,0.0136386555612,0.0127060412569,0.0125300994377,0.0123575761271,0.0129320756625,0.0130197362036,0.0131059755837,0.012409131455,0.0141157528454,0.0118501874705,0.0129751530295,0.012665720081,0.0128526822099,0.0122667480452,0.0124508485467,0.0140884419016,0.0136112970969,0.0124492135432,0.0125560263458,0.013009602449,0.0124197344749,0.0120799685734,0.0127645509184,0.0122776361883,0.0120711297535,0.0124530107311,0.0138591107587,0.0120947459755,0.0118467466866,0.0132386024332,0.0130705891186,0.0130988178027,0.0133301017427,0.0115164047017,0.012674653942,0.0124344658414,0.0137544957809,0.0046175498169])

    # Creating weights for histo: y6_PHI_9
    y6_PHI_9_weights = numpy.array([0.0,0.0,2.61083973183,5.20668102666,7.821905621,2.60874977939,5.21745187633,0.0,7.81331893506,5.21633672231,5.21479473348,2.60954230781,2.60491134235,2.61218253108,2.60667136302,5.21075326151,2.60300481352,2.60667136302,0.0,5.2027126165,7.8220825075,7.83931740511,0.0,0.0,2.60457256625,7.81332662578,5.22348139874,7.82039439504,0.0,5.20914590158,2.60457256625,5.20858063385,2.61802247732,5.20592733636,0.0,5.22201631709,0.0,10.4382107611,7.81849094249,5.21774796895,0.0,7.81102710129,7.80838918523,5.20800383005,0.0,2.60457256625,2.60135630825,5.21822863878,0.0,2.60399268616,7.81356119266,0.0,2.60399268616,2.59814005025,5.20757699524,2.60667136302,2.601975411,5.21795177296,2.60701167727,0.0,2.60604495409,2.61044173721,0.0,2.61802247732])

    # Creating weights for histo: y6_PHI_10
    y6_PHI_10_weights = numpy.array([8.42942602695,22.1166904844,15.8050420223,13.6836593138,14.7400856716,14.7442756411,14.7492582035,23.1814159828,14.7395508637,14.7411437447,21.0481751604,12.6471978336,7.37679718972,17.908129685,16.8521688794,16.8440313354,13.6890343251,13.6957328898,12.6390448994,11.5831764347,13.6983569111,20.0139721854,15.8098168177,16.8505067428,15.8015792376,20.0069619701,16.8512108423,13.6995304103,9.48364005006,16.8446892645,11.5832418428,15.8040839852,12.6373365922,13.6923432083,17.8987686237,17.9021660003,17.9090569418,16.8537155899,9.47689146743,32.6370959702,10.5383003876,15.8024372387,9.47584493694,15.7881167002,10.5289431739,18.952205444,16.8578978643,20.0096321619,22.1162287797,15.7954847365,12.6470554747,15.7928453251,14.747211313,17.9097456512,12.6466553306,17.909272404,14.7444911032,15.7972584518,14.7449412652,20.0072197552,12.6396258777,10.5355994156,21.0599524759,6.32348733817])

    # Creating weights for histo: y6_PHI_11
    y6_PHI_11_weights = numpy.array([11.9721350571,29.0186062139,25.8030289992,26.4931842946,27.1803617519,25.7939686865,25.8002663338,28.7912184932,25.8028906738,29.2574557297,24.8752037961,25.3413180767,27.1719776967,27.4109232718,25.1041553621,27.4039032585,25.7944605101,26.4904101022,21.6535133678,24.6445308475,22.5707374671,22.8016448004,25.7936036611,26.719442358,25.3300560849,28.7898544512,29.2601569171,26.7147546644,25.3345708718,25.1127469054,23.9548058976,25.1052350686,23.7241905846,25.7933808036,27.1769958342,25.7968081992,24.6414761619,25.1090543861,28.3290080623,30.179010182,27.407887798,26.2612894718,26.2515298474,27.414946235,22.1128535469,26.4913361138,24.1852828853,29.023247799,24.8788886306,26.4893457652,24.1904931414,26.4864793558,28.10451749,28.1025963041,29.7100986547,24.416566771,24.8748810368,27.1838237289,27.413374705,26.0247838028,23.9603811791,23.2640627193,25.7946142049,11.7465686206])

    # Creating weights for histo: y6_PHI_12
    y6_PHI_12_weights = numpy.array([7.53238984894,18.1360790649,17.0303915954,16.1707326201,16.7799119595,16.3657865001,17.0859404598,17.6659623199,17.1130397188,16.8085462276,17.1418317197,16.1989206199,18.0833270717,16.8360417421,17.3888604704,17.8876884263,16.3653825503,17.278893801,16.1703863774,16.255939092,17.5563996003,17.416440622,16.9196401093,16.5305249115,16.9464431384,17.4738322668,17.0877486159,15.8390244557,16.8071150913,16.0887462049,16.3946631381,17.5002505819,16.4210737589,17.3901800397,17.0846478205,18.1937092324,17.7502647138,17.1408853231,16.3938090729,16.9469009482,17.1683962262,16.504725986,16.2816033676,16.4486962291,16.3664212783,17.0026421696,16.8351492055,16.78148544,17.3364893442,16.9191822995,17.3352505649,16.8364456919,16.7260366013,17.999821036,16.8083346349,16.946623954,16.2002940491,16.5310981355,17.9421908685,17.08548265,16.9456083089,16.1696861978,17.4451095144,7.75291180033])

    # Creating weights for histo: y6_PHI_13
    y6_PHI_13_weights = numpy.array([3.49824308635,8.4998060037,8.25731000694,8.44923265376,8.27714733367,7.84343261481,8.26802665393,8.60950296157,8.45831085528,8.66010665309,8.50879924879,8.257771199,8.71050402185,8.21665228621,8.60985492393,8.62072327883,8.18697821839,9.11436869171,8.65126511591,8.59053947242,8.40808339939,8.44866223201,8.32793914301,8.50895702502,8.36873643502,8.39760948506,8.47826348003,8.60935125365,8.64076692832,8.48901653691,8.36711012619,8.28707509951,8.51935811955,8.35788021675,8.73164603663,8.176886608,8.9119478573,8.43828541074,8.43814583946,9.11434441844,7.95455562707,8.13586478828,8.78058700943,8.43772712562,8.70075830551,8.56039814423,8.81194806924,8.66053750356,8.28755449652,8.5806541848,8.44815249342,8.58963529326,8.81107423166,8.55975490268,8.62036524815,8.25720684556,8.31780505441,8.09591706058,7.51115587503,8.62015285707,8.54914748538,8.48910149334,7.69246503624,3.50882076889])

    # Creating weights for histo: y6_PHI_14
    y6_PHI_14_weights = numpy.array([1.2448393556,2.93649206256,3.19416930385,3.20593851505,3.11777600422,3.14010634151,3.00171519192,2.82097219537,3.12056883534,3.0243144628,3.10928555137,3.066929857,2.9511256666,2.9789481742,3.08937792487,3.20261012518,3.14885495521,3.08376686975,3.24513472062,3.18858787375,3.03308231353,3.20540641897,3.04152852122,3.06672594455,2.97050273598,3.07536490722,3.04702530842,3.0216197405,3.17695332173,3.11184984665,2.97063470197,3.03281261046,3.27053490218,3.06395119623,2.86297238954,3.06702257945,3.23348324002,3.23666196584,2.89455958271,3.07514829833,3.06400544463,3.03864912349,3.03854947571,3.01864569661,3.12055652365,3.08098942825,3.01881882983,2.84882625169,3.13203679474,3.06094214095,3.04688449341,3.2254179254,3.14314232861,3.15178090654,3.03550617854,3.03017367553,3.12882536598,3.10639345721,3.13754435467,3.11217225917,3.19989885904,2.99892505398,3.07519908407,1.12310169757])

    # Creating weights for histo: y6_PHI_15
    y6_PHI_15_weights = numpy.array([0.169093984973,0.358210676452,0.359349635378,0.34729905055,0.306161116089,0.318306230137,0.364101028406,0.350386847486,0.351854295448,0.333510900516,0.351798995855,0.371702359223,0.33209048084,0.370500656527,0.352073721398,0.344341940259,0.330410932943,0.334929311446,0.345558885791,0.39283105759,0.320042968211,0.32446409978,0.389929365054,0.328845410916,0.342692169065,0.3245570929,0.324337312466,0.34851044249,0.37172079242,0.325791171853,0.300129442953,0.345945864781,0.339811154796,0.395935751624,0.316811368701,0.336769322692,0.376148541035,0.389834835835,0.373148419949,0.367109775283,0.362618219446,0.356453850918,0.324364135131,0.36254259607,0.33507465012,0.298474827137,0.344371362478,0.347443562093,0.345748416875,0.293957393926,0.38527368286,0.370188119297,0.342641477772,0.374772550092,0.338117663839,0.364271181,0.315452747502,0.328930014567,0.364251448025,0.347269746492,0.350360379305,0.330562061532,0.344130431131,0.147771501706])

    # Creating weights for histo: y6_PHI_16
    y6_PHI_16_weights = numpy.array([0.0247340761053,0.0586833118481,0.0695083921561,0.072043705454,0.0628368028865,0.0646398018892,0.0646346027081,0.0650022040726,0.0613992870633,0.0611973277594,0.0640967377885,0.0626626880861,0.0646371830424,0.0650075187911,0.0662648733588,0.0662700340276,0.0650085586274,0.0689763811295,0.0630217781985,0.063565073374,0.0713246009303,0.0689748406313,0.0612188947331,0.0604918951566,0.0668015829048,0.0662701495649,0.0684377074484,0.0604953227649,0.0651794768941,0.0660815925947,0.0639103760282,0.0648177294224,0.0641034774678,0.0601189790735,0.0720532950548,0.0669834772206,0.0655420331272,0.0718605787396,0.0657251598416,0.061393818295,0.0691566194098,0.0622950867216,0.0633735124324,0.0615621947398,0.0597566154026,0.0619302967662,0.0640869941379,0.0653651069178,0.0635561769973,0.0574309638993,0.0695202539917,0.0646454247074,0.0684214551932,0.0707816908794,0.0624733608669,0.0622921597752,0.0646392627149,0.0664470757743,0.0669878676403,0.0612063396734,0.0659114830895,0.0594078081152,0.0702323492489,0.0236560432216])

    # Creating a new Canvas
    fig   = plt.figure(figsize=(12,6),dpi=80)
    frame = gridspec.GridSpec(1,1,right=0.7)
    pad   = fig.add_subplot(frame[0])

    # Creating a new Stack
    pad.hist(x=xData, bins=xBinning, weights=y6_PHI_0_weights+y6_PHI_1_weights+y6_PHI_2_weights+y6_PHI_3_weights+y6_PHI_4_weights+y6_PHI_5_weights+y6_PHI_6_weights+y6_PHI_7_weights+y6_PHI_8_weights+y6_PHI_9_weights+y6_PHI_10_weights+y6_PHI_11_weights+y6_PHI_12_weights+y6_PHI_13_weights+y6_PHI_14_weights+y6_PHI_15_weights+y6_PHI_16_weights,\
             label="$bg\_dip\_1600\_inf$", histtype="step", rwidth=1.0,\
             color=None, edgecolor="#e5e5e5", linewidth=1, linestyle="solid",\
             bottom=None, cumulative=False, normed=False, align="mid", orientation="vertical")

    pad.hist(x=xData, bins=xBinning, weights=y6_PHI_0_weights+y6_PHI_1_weights+y6_PHI_2_weights+y6_PHI_3_weights+y6_PHI_4_weights+y6_PHI_5_weights+y6_PHI_6_weights+y6_PHI_7_weights+y6_PHI_8_weights+y6_PHI_9_weights+y6_PHI_10_weights+y6_PHI_11_weights+y6_PHI_12_weights+y6_PHI_13_weights+y6_PHI_14_weights+y6_PHI_15_weights,\
             label="$bg\_dip\_1200\_1600$", histtype="step", rwidth=1.0,\
             color=None, edgecolor="#f2f2f2", linewidth=1, linestyle="solid",\
             bottom=None, cumulative=False, normed=False, align="mid", orientation="vertical")

    pad.hist(x=xData, bins=xBinning, weights=y6_PHI_0_weights+y6_PHI_1_weights+y6_PHI_2_weights+y6_PHI_3_weights+y6_PHI_4_weights+y6_PHI_5_weights+y6_PHI_6_weights+y6_PHI_7_weights+y6_PHI_8_weights+y6_PHI_9_weights+y6_PHI_10_weights+y6_PHI_11_weights+y6_PHI_12_weights+y6_PHI_13_weights+y6_PHI_14_weights,\
             label="$bg\_dip\_800\_1200$", histtype="step", rwidth=1.0,\
             color=None, edgecolor="#ccc6aa", linewidth=1, linestyle="solid",\
             bottom=None, cumulative=False, normed=False, align="mid", orientation="vertical")

    pad.hist(x=xData, bins=xBinning, weights=y6_PHI_0_weights+y6_PHI_1_weights+y6_PHI_2_weights+y6_PHI_3_weights+y6_PHI_4_weights+y6_PHI_5_weights+y6_PHI_6_weights+y6_PHI_7_weights+y6_PHI_8_weights+y6_PHI_9_weights+y6_PHI_10_weights+y6_PHI_11_weights+y6_PHI_12_weights+y6_PHI_13_weights,\
             label="$bg\_dip\_600\_800$", histtype="step", rwidth=1.0,\
             color=None, edgecolor="#ccc6aa", linewidth=1, linestyle="solid",\
             bottom=None, cumulative=False, normed=False, align="mid", orientation="vertical")

    pad.hist(x=xData, bins=xBinning, weights=y6_PHI_0_weights+y6_PHI_1_weights+y6_PHI_2_weights+y6_PHI_3_weights+y6_PHI_4_weights+y6_PHI_5_weights+y6_PHI_6_weights+y6_PHI_7_weights+y6_PHI_8_weights+y6_PHI_9_weights+y6_PHI_10_weights+y6_PHI_11_weights+y6_PHI_12_weights,\
             label="$bg\_dip\_400\_600$", histtype="step", rwidth=1.0,\
             color=None, edgecolor="#c1bfa8", linewidth=1, linestyle="solid",\
             bottom=None, cumulative=False, normed=False, align="mid", orientation="vertical")

    pad.hist(x=xData, bins=xBinning, weights=y6_PHI_0_weights+y6_PHI_1_weights+y6_PHI_2_weights+y6_PHI_3_weights+y6_PHI_4_weights+y6_PHI_5_weights+y6_PHI_6_weights+y6_PHI_7_weights+y6_PHI_8_weights+y6_PHI_9_weights+y6_PHI_10_weights+y6_PHI_11_weights,\
             label="$bg\_dip\_200\_400$", histtype="step", rwidth=1.0,\
             color=None, edgecolor="#bab5a3", linewidth=1, linestyle="solid",\
             bottom=None, cumulative=False, normed=False, align="mid", orientation="vertical")

    pad.hist(x=xData, bins=xBinning, weights=y6_PHI_0_weights+y6_PHI_1_weights+y6_PHI_2_weights+y6_PHI_3_weights+y6_PHI_4_weights+y6_PHI_5_weights+y6_PHI_6_weights+y6_PHI_7_weights+y6_PHI_8_weights+y6_PHI_9_weights+y6_PHI_10_weights,\
             label="$bg\_dip\_100\_200$", histtype="step", rwidth=1.0,\
             color=None, edgecolor="#b2a596", linewidth=1, linestyle="solid",\
             bottom=None, cumulative=False, normed=False, align="mid", orientation="vertical")

    pad.hist(x=xData, bins=xBinning, weights=y6_PHI_0_weights+y6_PHI_1_weights+y6_PHI_2_weights+y6_PHI_3_weights+y6_PHI_4_weights+y6_PHI_5_weights+y6_PHI_6_weights+y6_PHI_7_weights+y6_PHI_8_weights+y6_PHI_9_weights,\
             label="$bg\_dip\_0\_100$", histtype="step", rwidth=1.0,\
             color=None, edgecolor="#b7a39b", linewidth=1, linestyle="solid",\
             bottom=None, cumulative=False, normed=False, align="mid", orientation="vertical")

    pad.hist(x=xData, bins=xBinning, weights=y6_PHI_0_weights+y6_PHI_1_weights+y6_PHI_2_weights+y6_PHI_3_weights+y6_PHI_4_weights+y6_PHI_5_weights+y6_PHI_6_weights+y6_PHI_7_weights+y6_PHI_8_weights,\
             label="$bg\_vbf\_1600\_inf$", histtype="step", rwidth=1.0,\
             color=None, edgecolor="#ad998c", linewidth=1, linestyle="solid",\
             bottom=None, cumulative=False, normed=False, align="mid", orientation="vertical")

    pad.hist(x=xData, bins=xBinning, weights=y6_PHI_0_weights+y6_PHI_1_weights+y6_PHI_2_weights+y6_PHI_3_weights+y6_PHI_4_weights+y6_PHI_5_weights+y6_PHI_6_weights+y6_PHI_7_weights,\
             label="$bg\_vbf\_1200\_1600$", histtype="step", rwidth=1.0,\
             color=None, edgecolor="#9b8e82", linewidth=1, linestyle="solid",\
             bottom=None, cumulative=False, normed=False, align="mid", orientation="vertical")

    pad.hist(x=xData, bins=xBinning, weights=y6_PHI_0_weights+y6_PHI_1_weights+y6_PHI_2_weights+y6_PHI_3_weights+y6_PHI_4_weights+y6_PHI_5_weights+y6_PHI_6_weights,\
             label="$bg\_vbf\_800\_1200$", histtype="step", rwidth=1.0,\
             color=None, edgecolor="#876656", linewidth=1, linestyle="solid",\
             bottom=None, cumulative=False, normed=False, align="mid", orientation="vertical")

    pad.hist(x=xData, bins=xBinning, weights=y6_PHI_0_weights+y6_PHI_1_weights+y6_PHI_2_weights+y6_PHI_3_weights+y6_PHI_4_weights+y6_PHI_5_weights,\
             label="$bg\_vbf\_600\_800$", histtype="step", rwidth=1.0,\
             color=None, edgecolor="#afcec6", linewidth=1, linestyle="solid",\
             bottom=None, cumulative=False, normed=False, align="mid", orientation="vertical")

    pad.hist(x=xData, bins=xBinning, weights=y6_PHI_0_weights+y6_PHI_1_weights+y6_PHI_2_weights+y6_PHI_3_weights+y6_PHI_4_weights,\
             label="$bg\_vbf\_400\_600$", histtype="step", rwidth=1.0,\
             color=None, edgecolor="#84c1a3", linewidth=1, linestyle="solid",\
             bottom=None, cumulative=False, normed=False, align="mid", orientation="vertical")

    pad.hist(x=xData, bins=xBinning, weights=y6_PHI_0_weights+y6_PHI_1_weights+y6_PHI_2_weights+y6_PHI_3_weights,\
             label="$bg\_vbf\_200\_400$", histtype="step", rwidth=1.0,\
             color=None, edgecolor="#89a8a0", linewidth=1, linestyle="solid",\
             bottom=None, cumulative=False, normed=False, align="mid", orientation="vertical")

    pad.hist(x=xData, bins=xBinning, weights=y6_PHI_0_weights+y6_PHI_1_weights+y6_PHI_2_weights,\
             label="$bg\_vbf\_100\_200$", histtype="step", rwidth=1.0,\
             color=None, edgecolor="#829e8c", linewidth=1, linestyle="solid",\
             bottom=None, cumulative=False, normed=False, align="mid", orientation="vertical")

    pad.hist(x=xData, bins=xBinning, weights=y6_PHI_0_weights+y6_PHI_1_weights,\
             label="$bg\_vbf\_0\_100$", histtype="step", rwidth=1.0,\
             color=None, edgecolor="#adbcc6", linewidth=1, linestyle="solid",\
             bottom=None, cumulative=False, normed=False, align="mid", orientation="vertical")

    pad.hist(x=xData, bins=xBinning, weights=y6_PHI_0_weights,\
             label="$signal$", histtype="step", rwidth=1.0,\
             color=None, edgecolor="#7a8e99", linewidth=1, linestyle="solid",\
             bottom=None, cumulative=False, normed=False, align="mid", orientation="vertical")


    # Axis
    plt.rc('text',usetex=False)
    plt.xlabel(r"\phi [ j_{2} ] ",\
               fontsize=16,color="black")
    plt.ylabel(r"$\mathrm{Events}$ $(\mathcal{L}_{\mathrm{int}} = 40.0\ \mathrm{fb}^{-1})$ ",\
               fontsize=16,color="black")

    # Boundary of y-axis
    ymax=(y6_PHI_0_weights+y6_PHI_1_weights+y6_PHI_2_weights+y6_PHI_3_weights+y6_PHI_4_weights+y6_PHI_5_weights+y6_PHI_6_weights+y6_PHI_7_weights+y6_PHI_8_weights+y6_PHI_9_weights+y6_PHI_10_weights+y6_PHI_11_weights+y6_PHI_12_weights+y6_PHI_13_weights+y6_PHI_14_weights+y6_PHI_15_weights+y6_PHI_16_weights).max()*1.1
    ymin=0 # linear scale
    #ymin=min([x for x in (y6_PHI_0_weights+y6_PHI_1_weights+y6_PHI_2_weights+y6_PHI_3_weights+y6_PHI_4_weights+y6_PHI_5_weights+y6_PHI_6_weights+y6_PHI_7_weights+y6_PHI_8_weights+y6_PHI_9_weights+y6_PHI_10_weights+y6_PHI_11_weights+y6_PHI_12_weights+y6_PHI_13_weights+y6_PHI_14_weights+y6_PHI_15_weights+y6_PHI_16_weights) if x])/100. # log scale
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
