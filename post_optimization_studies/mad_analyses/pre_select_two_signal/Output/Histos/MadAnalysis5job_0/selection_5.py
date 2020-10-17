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
    y6_PHI_0_weights = numpy.array([27.0004849037,65.5954238895,65.0795443308,65.0140643868,65.9515835849,64.8421045339,65.6035838826,65.755063753,65.2515041837,63.8963853429,66.0826234728,65.7591837495,64.5063848211,65.2269442047,66.1235434378,64.2116250732,66.0171035288,65.5954238895,64.4040249087,64.5063848211,65.5872238966,65.697783802,64.7151846425,65.2719841662,65.2187442118,65.3743440787,65.4685039981,66.0211835253,65.9597835779,64.8543845234,65.9270236059,65.3088241347,64.5473447861,64.7725045935,63.6548255495,64.9035044814,64.9403444499,65.6363438545,65.0877443238,64.9567444359,65.8451436759,65.3088241347,65.0017843973,65.5463039316,64.8052645654,63.4828656966,65.1287042888,65.0017843973,65.722343781,65.2474241872,65.4152640437,65.624063865,64.3958649157,65.3989040576,63.9127453289,65.0672643413,65.1573442643,65.705943795,65.0345043694,64.8953444884,64.621024723,65.8083037074,64.5923447476,27.0332368757])

    # Creating weights for histo: y6_PHI_1
    y6_PHI_1_weights = numpy.array([0.436816895216,1.10558424099,1.06669423252,1.11183424236,1.15419665159,1.08891703736,1.07919463524,1.09586183887,1.12155664447,1.11669544342,1.06599983236,1.12780704584,1.13127904659,1.10905624175,1.09100023781,1.1069730413,1.08613903675,1.11044544205,1.13058464644,1.15766865235,1.0611386313,1.11877904387,1.09308383827,1.06044423115,1.14725185008,1.10141744008,1.09725063918,1.08752823706,1.1083618416,1.09586183887,1.0854446366,1.06877743297,1.12016784417,1.09725063918,1.0840558363,1.12850144599,1.10558424099,1.11183424236,1.1069730413,1.08058343554,1.09863943948,1.11530664311,1.12711264569,1.12989024629,1.1111398422,1.12016784417,1.05280502949,1.13475144735,1.09863943948,1.09238943812,1.10350064054,1.10766744145,1.14100184871,1.12989024629,1.06183303146,1.10280624039,1.14239064902,1.09586183887,1.1111398422,1.14100184871,1.1069730413,1.082667036,1.12294584478,0.460428500363])

    # Creating weights for histo: y6_PHI_2
    y6_PHI_2_weights = numpy.array([80.5883944672,193.62685769,191.269571435,192.484726082,192.933799748,193.457658941,194.319515066,195.460685317,195.913924862,195.688206361,190.895363408,192.992963231,193.506728181,195.931229279,192.568203873,193.272157189,193.823134647,192.837303587,193.411193376,193.730243573,194.657912562,193.677008455,193.878092195,193.70344576,195.01437555,193.531443055,194.084783848,191.96234898,192.116726816,193.460062333,193.376304145,193.369534593,189.532239969,191.625233292,194.147672587,193.774946651,194.513428688,189.933125639,192.445070125,191.927619976,192.656007769,193.156834462,193.716584299,190.043761753,195.633208757,192.850321957,192.815512839,193.845846695,195.955183079,191.78349661,192.505074795,196.810029312,192.97662017,194.208919009,191.331739157,192.420675703,192.825647139,194.553044588,195.51051563,192.156623111,193.472640081,195.204964481,192.869068409,81.5662943354])

    # Creating weights for histo: y6_PHI_3
    y6_PHI_3_weights = numpy.array([63.7252167506,153.004328184,156.222288474,153.772651998,154.906832488,154.837247821,152.887265618,155.614827552,154.97815264,152.798218731,153.573691088,156.715496662,155.63499223,153.650920151,152.739460182,155.862671278,154.585561237,155.190294968,154.639113332,154.467548286,152.991973187,153.64463935,153.893185534,155.720940037,153.712695138,155.170460859,152.087992329,155.550986512,155.169758401,153.532617953,153.483363248,156.143199963,153.012799002,155.089843468,154.295817955,154.395938886,155.631314656,154.524612671,153.501709799,154.334370505,154.702541161,152.367240061,154.28784299,154.875345839,154.507712357,154.56779318,153.359028174,153.303699273,153.614144407,154.938938953,154.083758268,152.701114237,154.548785492,154.94778166,153.898185382,151.404955186,152.901108173,153.705339989,154.436350884,155.007903804,156.814791172,156.51570933,153.765957986,64.3669328324])

    # Creating weights for histo: y6_PHI_4
    y6_PHI_4_weights = numpy.array([36.4557013487,86.8948481875,85.2114432178,87.0495912802,86.3230015685,86.6970012825,85.803683912,86.0414252032,86.4608443916,86.3004949596,85.8610879525,86.6689695855,85.7124793326,85.9464424386,85.7135355995,85.2903382259,86.7092296025,86.3652116166,87.4724636486,86.3777649418,85.3167042713,85.7726459171,87.0972045395,86.4266782218,85.3961680385,86.8564163247,84.8971225804,86.5489207961,86.2270031626,85.4157089751,87.3347833281,86.6033591642,87.0857887324,85.8491846376,86.1235702632,86.6086404985,88.0221692896,85.361392484,85.6585690979,84.0569435573,85.279247424,84.9529015949,85.0233870939,85.5135355351,87.5550962163,86.1022417981,86.7086608435,85.1674456411,86.5256422999,86.4704320445,86.7141046803,85.2065275144,86.6918418253,86.5096764203,86.2457722119,86.2737226576,85.9697615604,84.7930802962,86.8944013054,86.543395708,85.8118902929,86.1950307777,86.4099810805,35.6861906401])

    # Creating weights for histo: y6_PHI_5
    y6_PHI_5_weights = numpy.array([6.46295201864,15.8076318107,15.6713528338,15.5359917628,15.8765749679,15.7521085192,15.5564702855,15.5726358525,15.7570748315,15.710794733,15.6711844842,15.8014589931,15.5775380317,15.7004011512,15.6345444028,15.6068228402,15.4915995845,15.5416795733,15.8516472066,15.6547423428,15.5856989775,15.6693727221,15.7915664517,15.728411313,15.6711684509,15.6525056986,15.9593989481,15.6711724592,15.6522852408,15.5577409239,15.5102543202,15.6879392747,15.5081579672,15.4647638614,15.8674560329,15.7063735526,15.7856181003,15.9536189462,15.8804349831,15.8123856819,15.731413547,15.7995871062,15.6396069148,15.7798621483,15.7107065499,15.889205194,15.7383679876,15.5556726292,15.9437985546,15.6966333275,15.5654809958,15.6877348502,15.6358110329,15.8504968179,15.9236206561,15.7048263399,15.7886604175,15.9286711432,15.7381314965,15.7758257669,15.6900957525,15.7185227799,15.5870417657,6.41730924355])

    # Creating weights for histo: y6_PHI_6
    y6_PHI_6_weights = numpy.array([1.66742449255,4.03200144879,4.04641301397,4.02537180873,4.059708303,3.99554643044,3.97129002981,4.00645112807,3.99497748969,4.07733266296,4.04410844385,3.98401797849,3.97478409419,3.98079158034,4.02340332176,3.97696623401,3.99895967481,4.00319832338,4.00220207693,3.961120314,3.97480289884,4.01333683148,4.03096119145,4.05340274311,4.02167489417,4.03999942735,3.98833424626,4.00273820956,3.96968443262,4.03292167644,4.00504678066,3.97757398436,3.98756605623,4.03119324885,4.0332097477,3.99033914224,4.01954236662,4.08045743598,4.04608893379,3.98500422247,4.00540686974,3.99898288056,4.05167831651,3.96190610839,4.01387296411,4.0281604986,4.01505725708,3.96618596716,4.02259512182,4.03800693444,3.97626286001,4.04255205883,3.97578634213,4.03178939633,4.06646197374,3.97147047445,4.03581039106,4.00925182092,3.99167987392,4.00376646393,4.05216643727,4.04656505158,3.99241685623,1.6690076842])

    # Creating weights for histo: y6_PHI_7
    y6_PHI_7_weights = numpy.array([0.761298669107,1.80171748784,1.88436975635,1.80329295923,1.81653851509,1.80190142612,1.80817432144,1.84953644362,1.83278706337,1.7925145756,1.8077294707,1.82604732469,1.83908994863,1.88554336258,1.7807385267,1.83033088747,1.8012046599,1.82546052157,1.86083265352,1.86242611888,1.81128527765,1.8474731359,1.81141423438,1.85735282107,1.82802965958,1.80091175817,1.83667575864,1.79969116771,1.81262582787,1.79875448198,1.8308467144,1.83119459768,1.82233357073,1.82587338305,1.80580011803,1.85416489069,1.82368511726,1.85045813438,1.83814826458,1.82631223581,1.81775010857,1.86208523325,1.83352081718,1.83045884454,1.83953379971,1.80172448549,1.83884303148,1.82821859619,1.83655879788,1.7920287386,1.82441487241,1.83199732835,1.83604297095,1.84806993566,1.85553443118,1.88304220177,1.79068019107,1.80283311352,1.8014135898,1.80303004745,1.80967281866,1.83133655005,1.84676237438,0.73207497424])

    # Creating weights for histo: y6_PHI_8
    y6_PHI_8_weights = numpy.array([0.136536812237,0.33202898397,0.329271212741,0.326079300938,0.331289742192,0.329742066042,0.331368699701,0.324996024025,0.32759634124,0.330854386243,0.328310395404,0.331781508336,0.327865358359,0.327306201729,0.332183294771,0.329845833979,0.328984928905,0.324380960114,0.334556043368,0.326025614861,0.321404756539,0.330089202481,0.326573539744,0.323388207734,0.326740926311,0.32791284183,0.331877648743,0.325334024192,0.332107187108,0.32585856357,0.329033879208,0.325821515566,0.323613177962,0.321487066809,0.327641352049,0.328769304496,0.331438688576,0.321009843263,0.32901166717,0.328978726298,0.332552307972,0.330748103735,0.323835256435,0.32593664098,0.325850181669,0.329957899998,0.322574115578,0.326376481246,0.326780237428,0.324898207238,0.325478947264,0.327201176507,0.329980070127,0.327266178151,0.32732736603,0.329528243742,0.329173479773,0.325100504424,0.330537718015,0.331005763379,0.329633478511,0.324604589238,0.325907513873,0.134396116576])

    # Creating weights for histo: y6_PHI_9
    y6_PHI_9_weights = numpy.array([0.0500384734469,0.121028446771,0.123341206602,0.122444005175,0.122696256299,0.124937737777,0.122862186367,0.117652718791,0.120380214693,0.120987179574,0.122815335699,0.12618579205,0.121663046863,0.120808181808,0.124423419906,0.123036491641,0.123369821892,0.120732730701,0.120430673828,0.123175335934,0.120655586733,0.120268723468,0.121711085504,0.121030481174,0.124225251233,0.123493875926,0.120931419112,0.12341750414,0.121687029059,0.121514223601,0.12238882385,0.121494013218,0.121409800813,0.119469633725,0.122079431246,0.11990541176,0.123351631062,0.123039817964,0.120011408612,0.12116185609,0.123251039485,0.122711907838,0.120299209814,0.122015874714,0.124000412577,0.120528250924,0.123040649545,0.122454102942,0.121145016579,0.120118741933,0.121874699025,0.12142463562,0.123140602586,0.121794005989,0.122127900527,0.121329122626,0.123339053402,0.120640261887,0.121209152247,0.119362092509,0.123084426333,0.120622457148,0.1215965204,0.0510892500268])

    # Creating weights for histo: y6_PHI_10
    y6_PHI_10_weights = numpy.array([17797.6670459,42899.3357667,43400.3673087,42624.5951399,42341.3950395,43117.9362515,43206.7222707,42675.8134065,42768.7907103,43235.3306719,43600.5492127,43551.3304579,43702.1782507,42972.9331859,42817.9710128,43490.7298662,43206.8376272,43235.7920977,42938.3262489,43688.5277367,43457.2380417,43456.8535202,43003.3488382,42593.4488966,42875.4954324,43660.4576656,43294.2009168,43249.019638,43240.2140952,43174.7685323,42904.2576422,43271.014269,43404.9046627,42875.9568582,43142.2380116,42932.9429477,43133.3171123,43352.1867622,43665.341089,42335.5503124,43045.8384663,43530.5662958,42844.5799021,43305.3135887,43143.8145498,43407.0195311,43173.1919941,43679.2992202,43696.5642365,43297.9692277,42819.3937425,43433.3208031,43275.4747187,43379.2955294,42968.6265448,42583.9512151,43154.1581788,42878.6100567,43458.9299364,43420.2470714,42985.7762047,42273.2962781,42604.907638,18188.5639339])

    # Creating weights for histo: y6_PHI_11
    y6_PHI_11_weights = numpy.array([7362.15292613,17261.7268121,17453.0837813,17067.6688217,17627.0303212,17584.6835403,17416.1198048,17485.5460555,17419.4056626,17231.907845,17179.1648254,17434.8999827,17463.5992957,17368.9327322,17522.3061087,17289.0948525,17622.9441608,17431.2409069,17732.4663414,17383.6382925,17272.0191653,17800.792176,17377.3782332,17446.9391502,17451.2099958,17322.6113716,17363.8308031,17147.5836536,17316.0050275,17523.5758195,17704.8251207,17645.8028039,17265.6513729,17459.466964,17657.3186966,17397.97833,17320.3759109,17580.7397414,17536.2575377,17254.9896493,17509.0318588,17459.5670018,17388.7132883,17397.2934557,17505.6036395,17199.384009,17202.4082294,17464.3380366,17434.1727847,17527.0001912,17349.9024598,17519.4242498,17416.0043766,17539.4702909,17455.3038514,17349.0021194,17407.9590269,17462.7682123,17294.5084379,17783.7280315,17437.5048138,17497.6429372,17383.3381791,7194.71269241])

    # Creating weights for histo: y6_PHI_12
    y6_PHI_12_weights = numpy.array([1603.78535709,3813.89771211,3817.09258939,3768.7636828,3873.12109256,3828.45851417,3821.91314624,3829.55049748,3803.28218965,3779.14175077,3835.03116247,3798.51542507,3841.28297824,3822.93174151,3815.53914515,3770.32212203,3798.43819473,3840.21097492,3769.8391442,3798.6237781,3829.62503821,3751.98279645,3784.14865946,3817.09258939,3814.98508465,3836.42438256,3851.00093807,3803.51080684,3800.77854319,3770.31021089,3779.15827268,3801.90472302,3846.40554033,3809.07600256,3798.69063422,3774.71503026,3835.99634969,3865.20594261,3795.19221479,3816.38560512,3824.23120933,3815.38891099,3828.89768973,3822.68737086,3798.22494675,3768.11932812,3773.1650441,3823.33403093,3793.33100186,3777.22405594,3802.39653816,3846.19805582,3833.48117631,3872.00298157,3825.67553208,3847.92709343,3798.05050607,3782.35314996,3858.79697654,3843.05120737,3833.25063797,3777.43000353,3787.69357079,1603.36808268])

    # Creating weights for histo: y6_PHI_13
    y6_PHI_13_weights = numpy.array([192.176376098,456.238245605,468.145167699,459.857257435,458.704651987,458.477285559,455.992797582,456.148607064,449.92276796,458.680799672,461.580010169,459.002805933,457.765178522,462.713764593,461.227996156,454.822495255,449.708097119,460.854053401,458.261460574,455.675792613,461.800451732,458.149123861,458.760820344,456.562944869,455.39802855,462.966906911,456.194388121,457.839428472,458.399188461,452.935469315,458.589622272,464.413819156,452.575376291,454.049603285,455.241449639,465.185172268,456.238630319,458.953947158,457.494339325,456.628731095,464.481528956,452.532288237,459.694138373,465.799946468,454.744013443,460.166568109,454.218493068,461.801605876,455.98048671,460.145408797,462.941131021,464.917795503,462.746080634,458.25876757,453.439060947,460.941383653,459.27364513,455.548067309,458.097187367,455.907775618,457.01152229,454.653990187,464.880093456,186.138277802])

    # Creating weights for histo: y6_PHI_14
    y6_PHI_14_weights = numpy.array([43.7235957659,109.046884031,107.865384506,106.254430838,106.676360279,106.555965052,106.266749503,104.662653024,106.445339801,105.575083782,105.718417212,106.316934409,108.602744584,104.863453328,106.173783028,105.024809632,106.707672747,106.797544385,108.020793868,104.926867145,105.991187647,106.154182394,104.492072892,105.647175278,107.513786753,106.386841314,105.633218171,106.000290108,106.366573166,106.555297538,106.871274324,107.376339581,106.165287397,108.06697369,105.995132047,105.164016613,106.768901972,105.910297104,105.667443426,106.322942033,105.295880941,105.318879827,105.327982289,107.615006126,104.911757058,105.630001967,106.033180337,106.344545209,105.800157318,106.436115973,105.114195806,105.8321373,108.460017985,107.797237409,105.599357013,105.688621821,107.320025685,105.184163395,105.285382768,106.251882149,106.080088356,105.519619449,105.817694727,44.4112867454])

    # Creating weights for histo: y6_PHI_15
    y6_PHI_15_weights = numpy.array([19.4617075968,46.4491041394,46.9726218292,47.0179058978,46.3618063046,46.8328837349,47.08327347,46.7887154166,46.4371771545,47.0653829926,46.8566992306,47.4115733485,46.1751682277,47.3822175759,46.8202642154,46.2535015867,47.2671414085,46.6130039968,47.1000866713,47.2843778254,46.5063536671,47.2123927003,46.9559240503,46.7489716249,46.4465648459,47.2077758029,46.9332243048,46.4405244051,46.9759306057,46.831844933,46.6812186557,46.6359730613,47.495600881,47.4700155746,46.0052279296,46.7553583329,46.8341533817,47.0075563528,46.5998843133,46.885477891,46.6867974067,47.1491412061,46.7858298557,46.9333012531,47.0517246711,46.6761015944,46.4459877337,47.195848818,47.2188948308,46.5709132822,46.6793718967,47.2048517679,46.8990592642,47.1683782785,46.245075749,47.0873902035,46.5227436528,46.6876053637,46.5850332934,46.8252273801,46.8736278544,46.4122459086,46.5873802162,19.578053411])

    # Creating weights for histo: y6_PHI_16
    y6_PHI_16_weights = numpy.array([3.37250063165,8.25672229013,8.2337062442,8.11600985657,8.29328942008,8.33759867616,8.06025047804,8.10211373274,7.97310429327,8.22374735545,8.25594004234,8.33496597515,8.05392632372,8.24645735579,7.95051363889,7.97133773671,8.36229265541,8.10671977787,8.03189222328,8.24514218693,8.23497887391,8.12531293336,8.27727224673,8.18259663159,8.29691706465,8.25677191914,8.20394656063,8.16875486335,8.35178075765,7.98309508639,8.01798428302,8.06749867733,8.47724999414,8.14188075243,7.99221737176,8.21876082122,8.27851297207,8.30820293869,8.37569485239,8.15095577208,8.17011966122,8.10565275407,7.94147052361,8.22931053156,8.27704182631,8.05309799185,8.23185342769,8.10649999223,8.27864058953,8.27906125451,8.07588834393,8.19656838059,8.0680150554,8.25650604942,8.0735014247,8.15648704382,8.21485194557,8.06830455798,8.00502283894,8.37224327265,8.0029585083,8.27870203498,8.14181812534,3.28224436202])

    # Creating weights for histo: y6_PHI_17
    y6_PHI_17_weights = numpy.array([1.23326939808,2.97563314129,3.0007672981,2.99082640056,2.97966118435,3.00934831229,2.9826455333,2.96497475218,3.01858789361,2.93802972832,2.96807617973,2.9617158077,3.00977310735,2.97730959902,2.96540378363,2.98323015605,2.96065478287,3.01371719273,2.98167270255,2.99891252658,3.01866954053,2.97657862802,2.99533277132,3.02870594957,2.94585435312,2.98789096273,3.00148440454,2.95925484631,2.99590160387,3.02705221433,2.99944361668,3.04169281639,3.01711170191,2.95746130997,2.95778635714,2.9845257232,2.95665677972,2.95846918727,3.01572755555,2.98343119233,2.9852936664,2.97673653008,2.98337265303,3.00169314336,2.97054176264,3.01254486621,2.9747153837,2.98163881138,2.97853391768,2.96609123529,3.0036480479,2.95980249687,3.00675140108,3.03758851818,2.99427829366,2.98101606105,3.0099579683,2.96157831737,3.00060207863,2.99461682027,3.04516435096,2.98087125331,3.02766687699,1.22543398972])

    # Creating a new Canvas
    fig   = plt.figure(figsize=(12,6),dpi=80)
    frame = gridspec.GridSpec(1,1,right=0.7)
    pad   = fig.add_subplot(frame[0])

    # Creating a new Stack
    pad.hist(x=xData, bins=xBinning, weights=y6_PHI_0_weights+y6_PHI_1_weights+y6_PHI_2_weights+y6_PHI_3_weights+y6_PHI_4_weights+y6_PHI_5_weights+y6_PHI_6_weights+y6_PHI_7_weights+y6_PHI_8_weights+y6_PHI_9_weights+y6_PHI_10_weights+y6_PHI_11_weights+y6_PHI_12_weights+y6_PHI_13_weights+y6_PHI_14_weights+y6_PHI_15_weights+y6_PHI_16_weights+y6_PHI_17_weights,\
             label="$bg\_dip\_1600\_inf$", histtype="step", rwidth=1.0,\
             color=None, edgecolor="#f2f2f2", linewidth=1, linestyle="solid",\
             bottom=None, cumulative=False, normed=False, align="mid", orientation="vertical")

    pad.hist(x=xData, bins=xBinning, weights=y6_PHI_0_weights+y6_PHI_1_weights+y6_PHI_2_weights+y6_PHI_3_weights+y6_PHI_4_weights+y6_PHI_5_weights+y6_PHI_6_weights+y6_PHI_7_weights+y6_PHI_8_weights+y6_PHI_9_weights+y6_PHI_10_weights+y6_PHI_11_weights+y6_PHI_12_weights+y6_PHI_13_weights+y6_PHI_14_weights+y6_PHI_15_weights+y6_PHI_16_weights,\
             label="$bg\_dip\_1200\_1600$", histtype="step", rwidth=1.0,\
             color=None, edgecolor="#ccc6aa", linewidth=1, linestyle="solid",\
             bottom=None, cumulative=False, normed=False, align="mid", orientation="vertical")

    pad.hist(x=xData, bins=xBinning, weights=y6_PHI_0_weights+y6_PHI_1_weights+y6_PHI_2_weights+y6_PHI_3_weights+y6_PHI_4_weights+y6_PHI_5_weights+y6_PHI_6_weights+y6_PHI_7_weights+y6_PHI_8_weights+y6_PHI_9_weights+y6_PHI_10_weights+y6_PHI_11_weights+y6_PHI_12_weights+y6_PHI_13_weights+y6_PHI_14_weights+y6_PHI_15_weights,\
             label="$bg\_dip\_800\_1200$", histtype="step", rwidth=1.0,\
             color=None, edgecolor="#ccc6aa", linewidth=1, linestyle="solid",\
             bottom=None, cumulative=False, normed=False, align="mid", orientation="vertical")

    pad.hist(x=xData, bins=xBinning, weights=y6_PHI_0_weights+y6_PHI_1_weights+y6_PHI_2_weights+y6_PHI_3_weights+y6_PHI_4_weights+y6_PHI_5_weights+y6_PHI_6_weights+y6_PHI_7_weights+y6_PHI_8_weights+y6_PHI_9_weights+y6_PHI_10_weights+y6_PHI_11_weights+y6_PHI_12_weights+y6_PHI_13_weights+y6_PHI_14_weights,\
             label="$bg\_dip\_600\_800$", histtype="step", rwidth=1.0,\
             color=None, edgecolor="#c1bfa8", linewidth=1, linestyle="solid",\
             bottom=None, cumulative=False, normed=False, align="mid", orientation="vertical")

    pad.hist(x=xData, bins=xBinning, weights=y6_PHI_0_weights+y6_PHI_1_weights+y6_PHI_2_weights+y6_PHI_3_weights+y6_PHI_4_weights+y6_PHI_5_weights+y6_PHI_6_weights+y6_PHI_7_weights+y6_PHI_8_weights+y6_PHI_9_weights+y6_PHI_10_weights+y6_PHI_11_weights+y6_PHI_12_weights+y6_PHI_13_weights,\
             label="$bg\_dip\_400\_600$", histtype="step", rwidth=1.0,\
             color=None, edgecolor="#bab5a3", linewidth=1, linestyle="solid",\
             bottom=None, cumulative=False, normed=False, align="mid", orientation="vertical")

    pad.hist(x=xData, bins=xBinning, weights=y6_PHI_0_weights+y6_PHI_1_weights+y6_PHI_2_weights+y6_PHI_3_weights+y6_PHI_4_weights+y6_PHI_5_weights+y6_PHI_6_weights+y6_PHI_7_weights+y6_PHI_8_weights+y6_PHI_9_weights+y6_PHI_10_weights+y6_PHI_11_weights+y6_PHI_12_weights,\
             label="$bg\_dip\_200\_400$", histtype="step", rwidth=1.0,\
             color=None, edgecolor="#b2a596", linewidth=1, linestyle="solid",\
             bottom=None, cumulative=False, normed=False, align="mid", orientation="vertical")

    pad.hist(x=xData, bins=xBinning, weights=y6_PHI_0_weights+y6_PHI_1_weights+y6_PHI_2_weights+y6_PHI_3_weights+y6_PHI_4_weights+y6_PHI_5_weights+y6_PHI_6_weights+y6_PHI_7_weights+y6_PHI_8_weights+y6_PHI_9_weights+y6_PHI_10_weights+y6_PHI_11_weights,\
             label="$bg\_dip\_100\_200$", histtype="step", rwidth=1.0,\
             color=None, edgecolor="#b7a39b", linewidth=1, linestyle="solid",\
             bottom=None, cumulative=False, normed=False, align="mid", orientation="vertical")

    pad.hist(x=xData, bins=xBinning, weights=y6_PHI_0_weights+y6_PHI_1_weights+y6_PHI_2_weights+y6_PHI_3_weights+y6_PHI_4_weights+y6_PHI_5_weights+y6_PHI_6_weights+y6_PHI_7_weights+y6_PHI_8_weights+y6_PHI_9_weights+y6_PHI_10_weights,\
             label="$bg\_dip\_0\_100$", histtype="step", rwidth=1.0,\
             color=None, edgecolor="#ad998c", linewidth=1, linestyle="solid",\
             bottom=None, cumulative=False, normed=False, align="mid", orientation="vertical")

    pad.hist(x=xData, bins=xBinning, weights=y6_PHI_0_weights+y6_PHI_1_weights+y6_PHI_2_weights+y6_PHI_3_weights+y6_PHI_4_weights+y6_PHI_5_weights+y6_PHI_6_weights+y6_PHI_7_weights+y6_PHI_8_weights+y6_PHI_9_weights,\
             label="$bg\_vbf\_1600\_inf$", histtype="step", rwidth=1.0,\
             color=None, edgecolor="#9b8e82", linewidth=1, linestyle="solid",\
             bottom=None, cumulative=False, normed=False, align="mid", orientation="vertical")

    pad.hist(x=xData, bins=xBinning, weights=y6_PHI_0_weights+y6_PHI_1_weights+y6_PHI_2_weights+y6_PHI_3_weights+y6_PHI_4_weights+y6_PHI_5_weights+y6_PHI_6_weights+y6_PHI_7_weights+y6_PHI_8_weights,\
             label="$bg\_vbf\_1200\_1600$", histtype="step", rwidth=1.0,\
             color=None, edgecolor="#876656", linewidth=1, linestyle="solid",\
             bottom=None, cumulative=False, normed=False, align="mid", orientation="vertical")

    pad.hist(x=xData, bins=xBinning, weights=y6_PHI_0_weights+y6_PHI_1_weights+y6_PHI_2_weights+y6_PHI_3_weights+y6_PHI_4_weights+y6_PHI_5_weights+y6_PHI_6_weights+y6_PHI_7_weights,\
             label="$bg\_vbf\_800\_1200$", histtype="step", rwidth=1.0,\
             color=None, edgecolor="#afcec6", linewidth=1, linestyle="solid",\
             bottom=None, cumulative=False, normed=False, align="mid", orientation="vertical")

    pad.hist(x=xData, bins=xBinning, weights=y6_PHI_0_weights+y6_PHI_1_weights+y6_PHI_2_weights+y6_PHI_3_weights+y6_PHI_4_weights+y6_PHI_5_weights+y6_PHI_6_weights,\
             label="$bg\_vbf\_600\_800$", histtype="step", rwidth=1.0,\
             color=None, edgecolor="#84c1a3", linewidth=1, linestyle="solid",\
             bottom=None, cumulative=False, normed=False, align="mid", orientation="vertical")

    pad.hist(x=xData, bins=xBinning, weights=y6_PHI_0_weights+y6_PHI_1_weights+y6_PHI_2_weights+y6_PHI_3_weights+y6_PHI_4_weights+y6_PHI_5_weights,\
             label="$bg\_vbf\_400\_600$", histtype="step", rwidth=1.0,\
             color=None, edgecolor="#89a8a0", linewidth=1, linestyle="solid",\
             bottom=None, cumulative=False, normed=False, align="mid", orientation="vertical")

    pad.hist(x=xData, bins=xBinning, weights=y6_PHI_0_weights+y6_PHI_1_weights+y6_PHI_2_weights+y6_PHI_3_weights+y6_PHI_4_weights,\
             label="$bg\_vbf\_200\_400$", histtype="step", rwidth=1.0,\
             color=None, edgecolor="#829e8c", linewidth=1, linestyle="solid",\
             bottom=None, cumulative=False, normed=False, align="mid", orientation="vertical")

    pad.hist(x=xData, bins=xBinning, weights=y6_PHI_0_weights+y6_PHI_1_weights+y6_PHI_2_weights+y6_PHI_3_weights,\
             label="$bg\_vbf\_100\_200$", histtype="step", rwidth=1.0,\
             color=None, edgecolor="#adbcc6", linewidth=1, linestyle="solid",\
             bottom=None, cumulative=False, normed=False, align="mid", orientation="vertical")

    pad.hist(x=xData, bins=xBinning, weights=y6_PHI_0_weights+y6_PHI_1_weights+y6_PHI_2_weights,\
             label="$bg\_vbf\_0\_100$", histtype="step", rwidth=1.0,\
             color=None, edgecolor="#7a8e99", linewidth=1, linestyle="solid",\
             bottom=None, cumulative=False, normed=False, align="mid", orientation="vertical")

    pad.hist(x=xData, bins=xBinning, weights=y6_PHI_0_weights+y6_PHI_1_weights,\
             label="$signal2$", histtype="step", rwidth=1.0,\
             color=None, edgecolor="#758991", linewidth=1, linestyle="solid",\
             bottom=None, cumulative=False, normed=False, align="mid", orientation="vertical")

    pad.hist(x=xData, bins=xBinning, weights=y6_PHI_0_weights,\
             label="$signal1$", histtype="step", rwidth=1.0,\
             color=None, edgecolor="#688296", linewidth=1, linestyle="solid",\
             bottom=None, cumulative=False, normed=False, align="mid", orientation="vertical")


    # Axis
    plt.rc('text',usetex=False)
    plt.xlabel(r"\phi [ j_{2} ] ",\
               fontsize=16,color="black")
    plt.ylabel(r"$\mathrm{Events}$ $(\mathcal{L}_{\mathrm{int}} = 40.0\ \mathrm{fb}^{-1})$ ",\
               fontsize=16,color="black")

    # Boundary of y-axis
    ymax=(y6_PHI_0_weights+y6_PHI_1_weights+y6_PHI_2_weights+y6_PHI_3_weights+y6_PHI_4_weights+y6_PHI_5_weights+y6_PHI_6_weights+y6_PHI_7_weights+y6_PHI_8_weights+y6_PHI_9_weights+y6_PHI_10_weights+y6_PHI_11_weights+y6_PHI_12_weights+y6_PHI_13_weights+y6_PHI_14_weights+y6_PHI_15_weights+y6_PHI_16_weights+y6_PHI_17_weights).max()*1.1
    ymin=0 # linear scale
    #ymin=min([x for x in (y6_PHI_0_weights+y6_PHI_1_weights+y6_PHI_2_weights+y6_PHI_3_weights+y6_PHI_4_weights+y6_PHI_5_weights+y6_PHI_6_weights+y6_PHI_7_weights+y6_PHI_8_weights+y6_PHI_9_weights+y6_PHI_10_weights+y6_PHI_11_weights+y6_PHI_12_weights+y6_PHI_13_weights+y6_PHI_14_weights+y6_PHI_15_weights+y6_PHI_16_weights+y6_PHI_17_weights) if x])/100. # log scale
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
