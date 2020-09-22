def selection_14():

    # Library import
    import numpy
    import matplotlib
    import matplotlib.pyplot   as plt
    import matplotlib.gridspec as gridspec

    # Library version
    matplotlib_version = matplotlib.__version__
    numpy_version      = numpy.__version__

    # Histo binning
    xBinning = numpy.linspace(0.0,8000.0,81,endpoint=True)

    # Creating data sequence: middle of each bin
    xData = numpy.array([50.0,150.0,250.0,350.0,450.0,550.0,650.0,750.0,850.0,950.0,1050.0,1150.0,1250.0,1350.0,1450.0,1550.0,1650.0,1750.0,1850.0,1950.0,2050.0,2150.0,2250.0,2350.0,2450.0,2550.0,2650.0,2750.0,2850.0,2950.0,3050.0,3150.0,3250.0,3350.0,3450.0,3550.0,3650.0,3750.0,3850.0,3950.0,4050.0,4150.0,4250.0,4350.0,4450.0,4550.0,4650.0,4750.0,4850.0,4950.0,5050.0,5150.0,5250.0,5350.0,5450.0,5550.0,5650.0,5750.0,5850.0,5950.0,6050.0,6150.0,6250.0,6350.0,6450.0,6550.0,6650.0,6750.0,6850.0,6950.0,7050.0,7150.0,7250.0,7350.0,7450.0,7550.0,7650.0,7750.0,7850.0,7950.0])

    # Creating weights for histo: y15_TET_0
    y15_TET_0_weights = numpy.array([0.0,0.0,0.0,0.0,0.0,0.0,0.541322753874,1.82033104489,2.78622096259,3.2461685234,3.42660970802,3.47791130365,3.26916612144,3.18779052837,2.77383776364,2.60931817766,2.44479819168,2.147601417,1.94593223419,1.70180625499,1.5514386678,1.36038348408,1.23832029448,1.06495550926,0.932278320561,0.831443529153,0.730609137745,0.633312346036,0.59793194905,0.486483158547,0.40687676533,0.403338765632,0.332577491661,0.306042053922,0.242357019349,0.219359621308,0.196362223268,0.145060387639,0.14329134779,0.132677188695,0.0972965917094,0.0672231142719,0.0760682735183,0.0672231142719,0.0689921541212,0.0495328357793,0.0424567163823,0.0459947560808,0.0353805849852,0.0265354377389,0.0229973780404,0.0247664098897,0.0247664098897,0.00176902904926,0.00530708754779,0.0123832029448,0.00353805849852,0.0106141750956,0.00176902904926,0.00530708754779,0.00530708754779,0.00353805849852,0.0,0.0,0.00176902904926,0.00176902904926,0.00176902904926,0.00176902904926,0.00176902904926,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0])

    # Creating weights for histo: y15_TET_1
    y15_TET_1_weights = numpy.array([0.0,0.0,0.0,0.0,0.0,0.0,0.353672468828,1.2086320588,1.82300748865,2.17453114628,2.21399656217,2.18842689595,2.08907790132,2.01961873737,1.80692148074,1.70763723461,1.5216543339,1.36567637235,1.2983187372,1.09537812179,1.00122499524,0.906134614022,0.790763560615,0.688158755097,0.62082709929,0.571677384647,0.479818034014,0.437032058731,0.387875829269,0.325924175121,0.316275488052,0.255423359527,0.211562039391,0.20303206269,0.192365744872,0.152820712292,0.122872248228,0.0929587963201,0.0908125031182,0.0673181065813,0.0715961445546,0.0555761641333,0.03526097939,0.0512779821792,0.0267102791685,0.0235078658256,0.0288442022076,0.0160319109338,0.0245782186483,0.00961097306007,0.0160218269529,0.0149630888938,0.00855036848529,0.0106847231811,0.00748340896416,0.00748077905554,0.00320504445056,0.00320690816848,0.00320690816848,0.00427014025378,0.00427386928834,0.0,0.0010695906288,0.00427090764353,0.00213731753968,0.0010695906288,0.0,0.0,0.0,0.00106772691088,0.0,0.0,0.0,0.0010695906288,0.0,0.00213468803074,0.00106772691088,0.0,0.00106696111986,0.0])

    # Creating weights for histo: y15_TET_2
    y15_TET_2_weights = numpy.array([0.0,0.0,0.0,0.0,0.0,0.0,0.252089855593,0.87780059358,1.23128187153,1.50837233264,1.49517752973,1.53545633861,1.42017551319,1.32433989205,1.2347542723,1.15211305407,1.03683222865,0.931968605525,0.830576983166,0.761130967851,0.66182254595,0.604876933392,0.525708115933,0.484040106744,0.42570529388,0.381954324232,0.33750871443,0.2757015808,0.265284618503,0.207644245791,0.201394084413,0.165282036449,0.155559594305,0.131947869098,0.113891825116,0.093752420675,0.0784742573058,0.0569459325582,0.0451400499547,0.0500012910267,0.051390211333,0.0381954324232,0.0368065081169,0.0263895698196,0.0256951096665,0.0250006455133,0.0159726355224,0.0145837112161,0.00833354983778,0.0152781713693,0.00972247414408,0.00486123707204,0.00902800999093,0.00416677291889,0.00277784941259,0.00347231196574,0.00486123707204,0.00347231196574,0.00208338725945,0.000694462553149,0.0013889247063,0.00277784941259,0.000694462553149,0.000694462553149,0.0,0.0,0.0,0.0,0.0,0.0,0.000694462553149,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0])

    # Creating weights for histo: y15_TET_3
    y15_TET_3_weights = numpy.array([0.0,0.0,0.0,0.0,0.0,0.0,0.186817284884,0.603125744905,0.919387820889,1.00568384162,1.07822985905,1.09292866258,0.991459438204,0.953527029091,0.853480205054,0.781408587738,0.731622175777,0.712181771106,0.560926134766,0.497863319615,0.499285719956,0.413937699451,0.356565005667,0.321003317123,0.285441668579,0.244664258782,0.216214931947,0.195826247048,0.185869004656,0.156471357593,0.124702909961,0.126125390302,0.100046824037,0.0938828225559,0.0744424178852,0.0697008567461,0.0635368552651,0.0507346521893,0.0365099807717,0.0365099807717,0.0365099807717,0.0265527103795,0.0218111572403,0.0222853133542,0.0142246674176,0.0184920684428,0.00853480205054,0.00995726639229,0.0109055786201,0.00900895416446,0.00616402148094,0.00521571325311,0.00711233370878,0.00331908919743,0.00426740102527,0.00379324451135,0.00426740102527,0.00237077776959,0.00142246674176,0.000474155713919,0.0,0.00189662245568,0.000474155713919,0.000948311027838,0.000948311027838,0.0,0.0,0.000474155713919,0.0,0.000948311027838,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0])

    # Creating weights for histo: y15_TET_4
    y15_TET_4_weights = numpy.array([0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0])

    # Creating weights for histo: y15_TET_5
    y15_TET_5_weights = numpy.array([0.0,0.0,0.0,0.0,0.0,0.0,2.10674221742,0.0,1.0529581672,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0])

    # Creating weights for histo: y15_TET_6
    y15_TET_6_weights = numpy.array([0.0,0.0,0.0,0.0,0.0,0.0,0.691829993515,5.2978182267,5.06681435217,5.06814008347,1.38077450405,0.690627997143,0.461033240486,0.23012854603,0.0,0.0,0.230673171817,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0])

    # Creating weights for histo: y15_TET_7
    y15_TET_7_weights = numpy.array([0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.332435765982,1.60580251853,2.13237520421,2.51968650854,2.63087350198,1.38477604996,0.719744800729,0.332138681087,0.249261343098,0.138402554805,0.110813435051,0.0277263950555,0.0276696169506,0.0554236624816,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0])

    # Creating weights for histo: y15_TET_8
    y15_TET_8_weights = numpy.array([0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0604818175633,0.151143961499,0.403213391549,0.453828545279,0.746194426083,0.645139387342,0.534350744552,0.231751792407,0.171464208753,0.0705768526515,0.0706294696799,0.0201750558134,0.0100953567379,0.0100429581886,0.0,0.0,0.0100805669227,0.0,0.0,0.0,0.0,0.0100975172526,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0])

    # Creating weights for histo: y15_TET_9
    y15_TET_9_weights = numpy.array([0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.011317582905,0.0509394803948,0.0622634731433,0.0989753324578,0.101844295309,0.152781313339,0.198036424467,0.251867683062,0.141452626708,0.118830765363,0.107487496914,0.0622151877075,0.0452703470099,0.0424225451063,0.0113235810719,0.00848724455472,0.0,0.00283014097637,0.00282347950995,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0])

    # Creating weights for histo: y15_TET_10
    y15_TET_10_weights = numpy.array([0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.00305829576001,0.00304355754346,0.0,0.00612419346139,0.00457451903961,0.00304894934329,0.0,0.00611716001098,0.00304400548124,0.0075950710189,0.0106366087057,0.0182773386486,0.00606803813798,0.0106546916819,0.00455394344924,0.00306899308143,0.00304183197841,0.00610962543756,0.00151115650058,0.00153821477883,0.0,0.0,0.00151265396011,0.0,0.0,0.00152449653668,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0])

    # Creating weights for histo: y15_TET_11
    y15_TET_11_weights = numpy.array([0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.000180553030001,0.0,0.000721759378433,0.000180626138525,0.000180734319121,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.000180547139741,0.00252864058845,0.00126248642138,0.000180657129763,0.000361173239767,0.00108292126116,0.00054161443182,0.000360506985889,0.000361704556638,0.000361583017085,0.00036167183297,0.000361395760708,0.0,0.0,0.00018020300225,0.0,0.0,0.000180766965792,0.0,0.0,0.0,0.0,0.000180755031278,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0])

    # Creating weights for histo: y15_TET_12
    y15_TET_12_weights = numpy.array([0.0,0.0,0.0,0.0,0.0,0.0,0.0121704927804,0.0242994195771,0.0,0.0,0.0121313836425,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0])

    # Creating weights for histo: y15_TET_13
    y15_TET_13_weights = numpy.array([0.0,0.0,0.0,0.0,0.0,0.0,0.220879096585,0.441761829362,0.230809248523,0.120544402743,0.0502051137366,0.0501796190701,0.0100546543364,0.0301461580631,0.0100696701578,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0])

    # Creating weights for histo: y15_TET_14
    y15_TET_14_weights = numpy.array([0.0,0.0,0.0,0.0,0.0,0.0,0.511511761888,1.38040517552,1.56756688076,1.17169068658,0.676676643777,0.330056636725,0.192540760371,0.0659724728581,0.0770204073513,0.0274921778746,0.00550370717489,0.0109833557686,0.00549442824894,0.0,0.010972805256,0.0,0.00549598015337,0.0,0.0,0.0,0.0,0.00551421706168,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0])

    # Creating weights for histo: y15_TET_15
    y15_TET_15_weights = numpy.array([0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0917632079944,0.633559011637,0.989790504888,1.05102433758,0.744094801675,0.434199933413,0.213154808046,0.115462739059,0.0631728425952,0.0365086204957,0.0157838573059,0.0197451252806,0.0078951112346,0.00493792772495,0.00493571915759,0.000984219383707,0.00197349803006,0.000983908741293,0.00098817275936,0.0,0.00197004649222,0.000985428684564,0.000988894652248,0.0,0.0,0.0,0.000986794308699,0.0,0.0,0.000986290466745,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0])

    # Creating weights for histo: y15_TET_16
    y15_TET_16_weights = numpy.array([0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0151205420752,0.111653684494,0.261657168041,0.343094295266,0.331480637049,0.238964801687,0.16257873154,0.0804142402529,0.0380674438393,0.022441684025,0.0138683267656,0.00731159527149,0.00352862875846,0.0030259033186,0.0022693930793,0.000756678686561,0.000755416732519,0.00100723257957,0.000756493034476,0.0,0.000504272673936,0.00025201786373,0.0,0.0,0.000251958166982,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0])

    # Creating weights for histo: y15_TET_17
    y15_TET_17_weights = numpy.array([0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.00372534281898,0.0183210275661,0.0360822271564,0.0684229371749,0.0853200768397,0.0930575474769,0.0821456755683,0.0710181160836,0.0538331497211,0.0357861528456,0.0266283032915,0.0197457052388,0.0137463515593,0.00743379452655,0.00229388610822,0.00200115782904,0.0014346567846,0.000573726553247,0.000572941480461,0.0,0.000572185899139,0.0,0.000286183773284,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0])

    # Creating weights for histo: y15_TET_18
    y15_TET_18_weights = numpy.array([0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.000151233502217,0.00110138422607,0.00220321730341,0.00414651744629,0.00401822686611,0.00382183410569,0.00369232395761,0.00379994810059,0.00488093704425,0.00507276962655,0.00556959057563,0.00427551587877,0.00410439541507,0.00282801073919,0.00200744564252,0.00125294843654,0.000840630970017,0.00049662690786,0.000216079142796,0.000151277549154,0.000108084058385,2.15933968115e-05,2.16292043309e-05,2.16220838984e-05,2.16751874889e-05,0.0,4.31049358904e-05,0.0,0.0,0.0,0.0,0.0,0.0,2.15827559768e-05,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0])

    # Creating weights for histo: y15_TET_19
    y15_TET_19_weights = numpy.array([0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,5.6858529886e-05,8.51343800459e-05,0.000226838278621,8.52280444334e-05,0.000283801015335,0.000312017486312,0.000227213054959,0.000113571381062,0.000141943835613,0.000198131509915,0.000283985582288,0.000396740102387,0.000510742936541,0.000312537184087,0.000566361289355,0.000284116249157,0.000340548894141,0.00028235298885,0.000170249130364,0.000310712005502,0.000140637552984,5.67977549434e-05,8.48283374507e-05,2.84489095189e-05,5.67791349145e-05,0.0,5.67987794904e-05,0.000113523850988,5.67183451234e-05,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,2.79727327207e-05,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0])

    # Creating a new Canvas
    fig   = plt.figure(figsize=(12,6),dpi=80)
    frame = gridspec.GridSpec(1,1,right=0.7)
    pad   = fig.add_subplot(frame[0])

    # Creating a new Stack
    pad.hist(x=xData, bins=xBinning, weights=y15_TET_0_weights+y15_TET_1_weights+y15_TET_2_weights+y15_TET_3_weights+y15_TET_4_weights+y15_TET_5_weights+y15_TET_6_weights+y15_TET_7_weights+y15_TET_8_weights+y15_TET_9_weights+y15_TET_10_weights+y15_TET_11_weights+y15_TET_12_weights+y15_TET_13_weights+y15_TET_14_weights+y15_TET_15_weights+y15_TET_16_weights+y15_TET_17_weights+y15_TET_18_weights+y15_TET_19_weights,\
             label="$bg\_vbf\_1600\_inf$", histtype="step", rwidth=1.0,\
             color=None, edgecolor="#ccc6aa", linewidth=1, linestyle="solid",\
             bottom=None, cumulative=False, normed=False, align="mid", orientation="vertical")

    pad.hist(x=xData, bins=xBinning, weights=y15_TET_0_weights+y15_TET_1_weights+y15_TET_2_weights+y15_TET_3_weights+y15_TET_4_weights+y15_TET_5_weights+y15_TET_6_weights+y15_TET_7_weights+y15_TET_8_weights+y15_TET_9_weights+y15_TET_10_weights+y15_TET_11_weights+y15_TET_12_weights+y15_TET_13_weights+y15_TET_14_weights+y15_TET_15_weights+y15_TET_16_weights+y15_TET_17_weights+y15_TET_18_weights,\
             label="$bg\_vbf\_1200\_1600$", histtype="step", rwidth=1.0,\
             color=None, edgecolor="#c1bfa8", linewidth=1, linestyle="solid",\
             bottom=None, cumulative=False, normed=False, align="mid", orientation="vertical")

    pad.hist(x=xData, bins=xBinning, weights=y15_TET_0_weights+y15_TET_1_weights+y15_TET_2_weights+y15_TET_3_weights+y15_TET_4_weights+y15_TET_5_weights+y15_TET_6_weights+y15_TET_7_weights+y15_TET_8_weights+y15_TET_9_weights+y15_TET_10_weights+y15_TET_11_weights+y15_TET_12_weights+y15_TET_13_weights+y15_TET_14_weights+y15_TET_15_weights+y15_TET_16_weights+y15_TET_17_weights,\
             label="$bg\_vbf\_800\_1200$", histtype="step", rwidth=1.0,\
             color=None, edgecolor="#bab5a3", linewidth=1, linestyle="solid",\
             bottom=None, cumulative=False, normed=False, align="mid", orientation="vertical")

    pad.hist(x=xData, bins=xBinning, weights=y15_TET_0_weights+y15_TET_1_weights+y15_TET_2_weights+y15_TET_3_weights+y15_TET_4_weights+y15_TET_5_weights+y15_TET_6_weights+y15_TET_7_weights+y15_TET_8_weights+y15_TET_9_weights+y15_TET_10_weights+y15_TET_11_weights+y15_TET_12_weights+y15_TET_13_weights+y15_TET_14_weights+y15_TET_15_weights+y15_TET_16_weights,\
             label="$bg\_vbf\_600\_800$", histtype="step", rwidth=1.0,\
             color=None, edgecolor="#b2a596", linewidth=1, linestyle="solid",\
             bottom=None, cumulative=False, normed=False, align="mid", orientation="vertical")

    pad.hist(x=xData, bins=xBinning, weights=y15_TET_0_weights+y15_TET_1_weights+y15_TET_2_weights+y15_TET_3_weights+y15_TET_4_weights+y15_TET_5_weights+y15_TET_6_weights+y15_TET_7_weights+y15_TET_8_weights+y15_TET_9_weights+y15_TET_10_weights+y15_TET_11_weights+y15_TET_12_weights+y15_TET_13_weights+y15_TET_14_weights+y15_TET_15_weights,\
             label="$bg\_vbf\_400\_600$", histtype="step", rwidth=1.0,\
             color=None, edgecolor="#b7a39b", linewidth=1, linestyle="solid",\
             bottom=None, cumulative=False, normed=False, align="mid", orientation="vertical")

    pad.hist(x=xData, bins=xBinning, weights=y15_TET_0_weights+y15_TET_1_weights+y15_TET_2_weights+y15_TET_3_weights+y15_TET_4_weights+y15_TET_5_weights+y15_TET_6_weights+y15_TET_7_weights+y15_TET_8_weights+y15_TET_9_weights+y15_TET_10_weights+y15_TET_11_weights+y15_TET_12_weights+y15_TET_13_weights+y15_TET_14_weights,\
             label="$bg\_vbf\_200\_400$", histtype="step", rwidth=1.0,\
             color=None, edgecolor="#ad998c", linewidth=1, linestyle="solid",\
             bottom=None, cumulative=False, normed=False, align="mid", orientation="vertical")

    pad.hist(x=xData, bins=xBinning, weights=y15_TET_0_weights+y15_TET_1_weights+y15_TET_2_weights+y15_TET_3_weights+y15_TET_4_weights+y15_TET_5_weights+y15_TET_6_weights+y15_TET_7_weights+y15_TET_8_weights+y15_TET_9_weights+y15_TET_10_weights+y15_TET_11_weights+y15_TET_12_weights+y15_TET_13_weights,\
             label="$bg\_vbf\_100\_200$", histtype="step", rwidth=1.0,\
             color=None, edgecolor="#9b8e82", linewidth=1, linestyle="solid",\
             bottom=None, cumulative=False, normed=False, align="mid", orientation="vertical")

    pad.hist(x=xData, bins=xBinning, weights=y15_TET_0_weights+y15_TET_1_weights+y15_TET_2_weights+y15_TET_3_weights+y15_TET_4_weights+y15_TET_5_weights+y15_TET_6_weights+y15_TET_7_weights+y15_TET_8_weights+y15_TET_9_weights+y15_TET_10_weights+y15_TET_11_weights+y15_TET_12_weights,\
             label="$bg\_vbf\_0\_100$", histtype="step", rwidth=1.0,\
             color=None, edgecolor="#876656", linewidth=1, linestyle="solid",\
             bottom=None, cumulative=False, normed=False, align="mid", orientation="vertical")

    pad.hist(x=xData, bins=xBinning, weights=y15_TET_0_weights+y15_TET_1_weights+y15_TET_2_weights+y15_TET_3_weights+y15_TET_4_weights+y15_TET_5_weights+y15_TET_6_weights+y15_TET_7_weights+y15_TET_8_weights+y15_TET_9_weights+y15_TET_10_weights+y15_TET_11_weights,\
             label="$bg\_dip\_1600\_inf$", histtype="step", rwidth=1.0,\
             color=None, edgecolor="#afcec6", linewidth=1, linestyle="solid",\
             bottom=None, cumulative=False, normed=False, align="mid", orientation="vertical")

    pad.hist(x=xData, bins=xBinning, weights=y15_TET_0_weights+y15_TET_1_weights+y15_TET_2_weights+y15_TET_3_weights+y15_TET_4_weights+y15_TET_5_weights+y15_TET_6_weights+y15_TET_7_weights+y15_TET_8_weights+y15_TET_9_weights+y15_TET_10_weights,\
             label="$bg\_dip\_1200\_1600$", histtype="step", rwidth=1.0,\
             color=None, edgecolor="#84c1a3", linewidth=1, linestyle="solid",\
             bottom=None, cumulative=False, normed=False, align="mid", orientation="vertical")

    pad.hist(x=xData, bins=xBinning, weights=y15_TET_0_weights+y15_TET_1_weights+y15_TET_2_weights+y15_TET_3_weights+y15_TET_4_weights+y15_TET_5_weights+y15_TET_6_weights+y15_TET_7_weights+y15_TET_8_weights+y15_TET_9_weights,\
             label="$bg\_dip\_800\_1200$", histtype="step", rwidth=1.0,\
             color=None, edgecolor="#89a8a0", linewidth=1, linestyle="solid",\
             bottom=None, cumulative=False, normed=False, align="mid", orientation="vertical")

    pad.hist(x=xData, bins=xBinning, weights=y15_TET_0_weights+y15_TET_1_weights+y15_TET_2_weights+y15_TET_3_weights+y15_TET_4_weights+y15_TET_5_weights+y15_TET_6_weights+y15_TET_7_weights+y15_TET_8_weights,\
             label="$bg\_dip\_600\_800$", histtype="step", rwidth=1.0,\
             color=None, edgecolor="#829e8c", linewidth=1, linestyle="solid",\
             bottom=None, cumulative=False, normed=False, align="mid", orientation="vertical")

    pad.hist(x=xData, bins=xBinning, weights=y15_TET_0_weights+y15_TET_1_weights+y15_TET_2_weights+y15_TET_3_weights+y15_TET_4_weights+y15_TET_5_weights+y15_TET_6_weights+y15_TET_7_weights,\
             label="$bg\_dip\_400\_600$", histtype="step", rwidth=1.0,\
             color=None, edgecolor="#adbcc6", linewidth=1, linestyle="solid",\
             bottom=None, cumulative=False, normed=False, align="mid", orientation="vertical")

    pad.hist(x=xData, bins=xBinning, weights=y15_TET_0_weights+y15_TET_1_weights+y15_TET_2_weights+y15_TET_3_weights+y15_TET_4_weights+y15_TET_5_weights+y15_TET_6_weights,\
             label="$bg\_dip\_200\_400$", histtype="step", rwidth=1.0,\
             color=None, edgecolor="#7a8e99", linewidth=1, linestyle="solid",\
             bottom=None, cumulative=False, normed=False, align="mid", orientation="vertical")

    pad.hist(x=xData, bins=xBinning, weights=y15_TET_0_weights+y15_TET_1_weights+y15_TET_2_weights+y15_TET_3_weights+y15_TET_4_weights+y15_TET_5_weights,\
             label="$bg\_dip\_100\_200$", histtype="step", rwidth=1.0,\
             color=None, edgecolor="#758991", linewidth=1, linestyle="solid",\
             bottom=None, cumulative=False, normed=False, align="mid", orientation="vertical")

    pad.hist(x=xData, bins=xBinning, weights=y15_TET_0_weights+y15_TET_1_weights+y15_TET_2_weights+y15_TET_3_weights+y15_TET_4_weights,\
             label="$bg\_dip\_0\_100$", histtype="step", rwidth=1.0,\
             color=None, edgecolor="#688296", linewidth=1, linestyle="solid",\
             bottom=None, cumulative=False, normed=False, align="mid", orientation="vertical")

    pad.hist(x=xData, bins=xBinning, weights=y15_TET_0_weights+y15_TET_1_weights+y15_TET_2_weights+y15_TET_3_weights,\
             label="$signal\_2pt4TeVL$", histtype="step", rwidth=1.0,\
             color=None, edgecolor="#6d7a84", linewidth=1, linestyle="solid",\
             bottom=None, cumulative=False, normed=False, align="mid", orientation="vertical")

    pad.hist(x=xData, bins=xBinning, weights=y15_TET_0_weights+y15_TET_1_weights+y15_TET_2_weights,\
             label="$signal\_2pt2TeVL$", histtype="step", rwidth=1.0,\
             color=None, edgecolor="#7c99d1", linewidth=1, linestyle="solid",\
             bottom=None, cumulative=False, normed=False, align="mid", orientation="vertical")

    pad.hist(x=xData, bins=xBinning, weights=y15_TET_0_weights+y15_TET_1_weights,\
             label="$signal\_2TeVL$", histtype="step", rwidth=1.0,\
             color=None, edgecolor="#7f7f9b", linewidth=1, linestyle="solid",\
             bottom=None, cumulative=False, normed=False, align="mid", orientation="vertical")

    pad.hist(x=xData, bins=xBinning, weights=y15_TET_0_weights,\
             label="$signal\_1pt8TeVL$", histtype="step", rwidth=1.0,\
             color=None, edgecolor="#aaa5bf", linewidth=1, linestyle="solid",\
             bottom=None, cumulative=False, normed=False, align="mid", orientation="vertical")


    # Axis
    plt.rc('text',usetex=False)
    plt.xlabel(r"TET",\
               fontsize=16,color="black")
    plt.ylabel(r"$\mathrm{Events}$ $(\mathcal{L}_{\mathrm{int}} = 40.0\ \mathrm{fb}^{-1})$ ",\
               fontsize=16,color="black")

    # Boundary of y-axis
    ymax=(y15_TET_0_weights+y15_TET_1_weights+y15_TET_2_weights+y15_TET_3_weights+y15_TET_4_weights+y15_TET_5_weights+y15_TET_6_weights+y15_TET_7_weights+y15_TET_8_weights+y15_TET_9_weights+y15_TET_10_weights+y15_TET_11_weights+y15_TET_12_weights+y15_TET_13_weights+y15_TET_14_weights+y15_TET_15_weights+y15_TET_16_weights+y15_TET_17_weights+y15_TET_18_weights+y15_TET_19_weights).max()*1.1
    ymin=0 # linear scale
    #ymin=min([x for x in (y15_TET_0_weights+y15_TET_1_weights+y15_TET_2_weights+y15_TET_3_weights+y15_TET_4_weights+y15_TET_5_weights+y15_TET_6_weights+y15_TET_7_weights+y15_TET_8_weights+y15_TET_9_weights+y15_TET_10_weights+y15_TET_11_weights+y15_TET_12_weights+y15_TET_13_weights+y15_TET_14_weights+y15_TET_15_weights+y15_TET_16_weights+y15_TET_17_weights+y15_TET_18_weights+y15_TET_19_weights) if x])/100. # log scale
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
    plt.savefig('../../HTML/MadAnalysis5job_0/selection_14.png')
    plt.savefig('../../PDF/MadAnalysis5job_0/selection_14.png')
    plt.savefig('../../DVI/MadAnalysis5job_0/selection_14.eps')

# Running!
if __name__ == '__main__':
    selection_14()
