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
    y15_TET_0_weights = numpy.array([0.764646248397,19.1519558657,48.4776139176,82.6629252469,116.017124567,147.819698805,173.067696061,193.284101692,207.560044438,215.121771737,219.784886904,218.216861979,213.254869686,207.310326839,199.269604145,187.355918688,176.322464768,161.956442889,149.764360108,137.2734402,124.233885568,112.471678654,101.176227253,90.1836929393,80.8861023299,70.4217229385,62.9541947342,54.6063949931,46.9546285602,41.0182856344,35.2497530953,30.2140735103,26.3820463529,22.5090755891,19.5695518508,16.5031093328,13.8337869967,11.520653236,9.88712494138,8.63025302543,7.0949837861,5.6088460744,4.75728226166,3.93438017336,3.20563957975,2.86173968614,2.23125614785,1.87916793296,1.5516442819,1.16270962126,1.06445256594,0.912972822329,0.790151203183,0.532226082974,0.548602325527,0.409404863824,0.388934580634,0.290677405316,0.237454797018,0.180138108083,0.180138108083,0.135103581062,0.122821459147,0.0736928514886,0.0409404863824,0.0245642878295,0.0368464337442,0.0409404863824,0.0286583364677,0.00818809727649,0.0204702391913,0.0245642878295,0.016376190553,0.00818809727649,0.00818809727649,0.00818809727649,0.00818809727649,0.00818809727649,0.0,0.0])

    # Creating weights for histo: y15_TET_1
    y15_TET_1_weights = numpy.array([0.428785448138,0.674610846387,1.63232356559,2.40360340236,2.98568823782,3.37512592052,3.73211019785,3.94271012902,3.87089901538,3.84949368781,3.65063226471,3.50770007001,3.33645824482,3.13138215369,2.88901924744,2.65908527956,2.41257979157,2.23719458921,2.00795105162,1.84568561564,1.67237210187,1.56258374282,1.33541189382,1.22148055532,1.09512067616,0.988094435987,0.910759084594,0.77058940648,0.653895949101,0.595204204123,0.552393548969,0.467463066667,0.423962378936,0.35284149673,0.310031000662,0.270672934446,0.234767337855,0.19057582212,0.18021845302,0.153289245633,0.141550896638,0.111859729461,0.0945974211124,0.0828590721168,0.0835495421787,0.0662872338306,0.0497154353158,0.0435010059013,0.0290006692752,0.0379770704116,0.0290006692752,0.0227862398607,0.0262387015303,0.0193337821682,0.0103573810317,0.0124288588289,0.0138098427014,0.0138098427014,0.00897639715932,0.00483344554205,0.00552393548969,0.00897639715932,0.0034524608742,0.00276196854027,0.00207147660406,0.000690492333925,0.0,0.000690492333925,0.0,0.00138098427014,0.00138098427014,0.0,0.000690492333925,0.0,0.0,0.0,0.0,0.0,0.0,0.0])

    # Creating weights for histo: y15_TET_2
    y15_TET_2_weights = numpy.array([3641.51760949,8256.74774226,225.716499455,18.9302280709,4.61717246905,1.72550681794,0.510565662399,0.255039969066,0.0849663768864,0.0850132829657,0.0728805509075,0.0364969032285,0.0121245365126,0.0,0.0,0.0,0.0,0.0,0.0121541542367,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0])

    # Creating weights for histo: y15_TET_3
    y15_TET_3_weights = numpy.array([0.041320929045,4521.95173794,4486.54383385,600.595984785,65.1201313377,13.2426181143,4.13707620854,1.63664555575,0.913939201082,0.522091591321,0.180783527232,0.150561523691,0.120503233672,0.0502272420913,0.0602470302127,0.0201252221323,0.0100611214467,0.0100272961341,0.0,0.0,0.0100569934858,0.0100272961341,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0])

    # Creating weights for histo: y15_TET_4
    y15_TET_4_weights = numpy.array([0.0406253837685,0.0,1421.6877425,2299.17734422,1167.28712055,351.872170842,118.267479716,38.501639019,10.0162655563,3.36071984085,1.51272760251,0.693150297857,0.363098183139,0.170485113616,0.121005711833,0.0549836537791,0.0384950414566,0.0274877440385,0.0164749906313,0.00550226135222,0.0219745625831,0.00548800996759,0.00549592785489,0.0,0.00550872485077,0.0,0.0,0.00551416458966,0.0,0.00550038039695,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0])

    # Creating weights for histo: y15_TET_5
    y15_TET_5_weights = numpy.array([0.0400816433891,0.0,0.0,0.0,181.122052433,366.364858541,238.988401973,101.991629523,52.4567305406,25.7566323847,12.1429302648,5.14529659452,1.54830057554,0.592055173279,0.301948647409,0.15591554862,0.0878350335678,0.0483508872367,0.0404632206342,0.0167748010483,0.0148071490845,0.00690789888705,0.00394684543677,0.0069045881433,0.000983878088026,0.00296024460271,0.00197605588195,0.00196998511624,0.000985397983943,0.00197460091829,0.000987628527398,0.0,0.00197700501526,0.000986763565534,0.0,0.0,0.000986259739276,0.000987913908699,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0])

    # Creating weights for histo: y15_TET_6
    y15_TET_6_weights = numpy.array([0.0400035889772,0.0,0.0,0.0,0.0,0.0,38.0691434257,85.8798248269,62.3960779502,27.6443201483,14.8607012483,9.34026197449,6.34632536933,3.78306700307,2.08887860663,0.990755286977,0.311782572004,0.14265455845,0.0763780923659,0.0431023869901,0.0239409638966,0.0133561582662,0.00831779024203,0.00680807479582,0.00277346842555,0.00226632012604,0.00251748505964,0.00126041828016,0.00100923294473,0.00100916933902,0.000251969765815,0.0,0.0,0.00025191008046,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0])

    # Creating weights for histo: y15_TET_7
    y15_TET_7_weights = numpy.array([0.0998797003429,0.0,0.0,0.0,0.0,0.0,0.0,0.0,10.9845497084,26.9500001931,24.7194267973,19.4315957017,13.1003713165,6.76498993821,4.08371838371,2.74146605351,2.01775971836,1.36978616719,0.911139482137,0.624675212742,0.391574469886,0.244884250263,0.159297434919,0.0866777214072,0.0368855933126,0.0166134300287,0.00744314913241,0.00686018128542,0.00429731112289,0.0022917616979,0.00143097347042,0.00228764265906,0.000859933656764,0.000859354254622,0.0,0.000286188501543,0.0,0.000286177614656,0.000286053564068,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0])

    # Creating weights for histo: y15_TET_8
    y15_TET_8_weights = numpy.array([0.0418244443129,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,1.5696839424,4.28414475008,4.33300824837,3.69408381674,2.62397947783,1.36737408632,0.788786852785,0.498701290165,0.340844670201,0.246868238839,0.190161569804,0.156366373188,0.133255439994,0.103833407276,0.0717518417921,0.0538261777307,0.0371336153961,0.0246453884069,0.0167459052309,0.00866141999031,0.00454817410214,0.00213401489584,0.00114106996479,0.000689768735608,0.000538854847927,0.000258760601335,0.00017245326738,0.000151093021776,6.46016602657e-05,0.000129461419177,8.61844537378e-05,8.63469417039e-05,0.0,0.0,2.16113553851e-05,0.0,2.15389279949e-05,0.0,0.0,0.0,2.15125702301e-05,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,2.15963864165e-05,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0])

    # Creating weights for histo: y15_TET_9
    y15_TET_9_weights = numpy.array([0.145672552342,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.340067911921,0.975958028751,1.04723225814,0.943031661745,0.797470111887,0.655026683013,0.532944780815,0.432989665282,0.344297223133,0.275693754316,0.220226162233,0.178389733563,0.14425100674,0.114190820038,0.0958933568904,0.0808723025211,0.0669064709864,0.0551491810179,0.0415379601774,0.0331772879773,0.0294737818429,0.0221669777227,0.0162754989865,0.0131249090484,0.0121473981503,0.00872644578196,0.00701159869287,0.00570284152121,0.00410948534077,0.0031685921521,0.00289402124181,0.00261659806296,0.00180681599829,0.00147185653143,0.00161139626932,0.00086248333498,0.000969607433831,0.000834105884766,0.000530228716076,0.000389114840587,0.000278473914977,0.000222933486618,0.000223967907412,0.000167056554663,0.000194544819618,0.000165170532128,0.000166607009167,2.55754386696e-05,2.78128816701e-05,0.0,2.78595114541e-05,5.56257487729e-05,0.0,2.78699998778e-05,2.78311490081e-05,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0])

    # Creating weights for histo: y15_TET_10
    y15_TET_10_weights = numpy.array([987695.918834,1670279.12646,48725.1871461,3351.93433209,586.430440792,127.74573639,54.7817524831,13.0350410553,7.83026469345,2.60657639302,0.0,0.0,2.60342100665,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0])

    # Creating weights for histo: y15_TET_11
    y15_TET_11_weights = numpy.array([0.0384761158901,650881.214455,384420.645275,52373.3041885,6235.17385595,962.623939664,310.709603022,96.9164109843,54.7743677245,11.5929768413,7.37354361112,3.16392256006,2.10767430284,1.05572421252,1.0523583219,0.0,0.0,0.0,0.0,0.0,0.0,1.05322788212,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0])

    # Creating weights for histo: y15_TET_12
    y15_TET_12_weights = numpy.array([0.0384230889341,0.0,81851.745779,95686.939527,42845.0869702,12480.6031168,4444.54854705,1659.38946872,385.386271625,112.863750896,41.4623552688,19.8141337708,9.67103000776,4.37863373798,2.99428442447,1.61300242615,0.230649730024,0.691089588726,0.691041175634,0.230574843423,0.0,0.230728804741,0.0,0.0,0.230621796438,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0])

    # Creating weights for histo: y15_TET_13
    y15_TET_13_weights = numpy.array([0.0384714617155,0.0,0.0,0.0,6721.84920532,11259.8581921,6110.63385731,2131.44785844,1249.0102442,693.657766888,366.325181512,179.409007179,51.4216866867,18.9957112553,7.22715261922,4.12617198908,1.71709675075,1.19041628443,0.470521365365,0.526095315387,0.360067182721,0.138408816285,0.138530847762,0.0829310449185,0.0,0.0,0.0,0.0277272826906,0.0,0.0,0.0,0.0,0.0,0.0,0.0276981867241,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0])

    # Creating weights for histo: y15_TET_14
    y15_TET_14_weights = numpy.array([0.0606826172395,0.0,0.0,0.0,0.0,0.0,1256.86868431,2527.99596319,1586.64472674,560.395838736,253.704920286,152.882936317,135.953578394,94.0755333151,57.6670188489,30.4264402635,9.98099799616,3.45829021996,1.83480507629,0.957711876886,0.574867550661,0.272205957995,0.261972198693,0.0503334638729,0.110992936762,0.0403494378141,0.0403333144427,0.0301924359549,0.020148449402,0.0100965194946,0.0100965194946,0.0,0.0,0.0100986980006,0.0100819738712,0.0,0.0,0.0101023510941,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0])

    # Creating weights for histo: y15_TET_15
    y15_TET_15_weights = numpy.array([0.0384736822675,0.0,0.0,0.0,0.0,0.0,0.0,0.0,347.025188632,780.843387934,660.975937671,492.534309336,304.19824769,131.250081529,67.8838883611,43.1894399767,36.1448895167,26.2402093643,17.6372016093,12.0834178476,8.57816529836,5.91836422216,3.71174349518,2.3424016617,0.817590371341,0.328148268796,0.214982510774,0.144292967608,0.0792248526305,0.0622158300684,0.0282839198242,0.00849379251314,0.0169765546216,0.00565600064067,0.0169887546262,0.00848283520843,0.00282507939838,0.0,0.00283244749327,0.0,0.00282873362872,0.0,0.0,0.00282925302343,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0])

    # Creating weights for histo: y15_TET_16
    y15_TET_16_weights = numpy.array([0.118137476929,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,47.6750758257,120.352790896,115.211755058,94.6988006724,63.0940603433,28.4011354848,14.570296697,8.35726957915,5.09015638994,3.3599633392,2.44751554102,2.02847718486,2.16108059583,1.73287713421,1.35379169137,0.948690249629,0.679445843123,0.483074421122,0.325926531662,0.217720399869,0.0913931132342,0.044167137027,0.024415047062,0.00758381288532,0.0121644151656,0.00607866109577,0.0045462679854,0.00152028165623,0.00304478909,0.0,0.00152851229424,0.00151660758069,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0])

    # Creating weights for histo: y15_TET_17
    y15_TET_17_weights = numpy.array([0.0385048379542,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,9.71144379784,27.5034820849,28.4230199705,24.5288139316,20.0002060331,16.0641144314,12.7489633981,10.0590462225,7.8879085791,6.28390484348,4.94966985304,3.95110463796,3.07923497158,2.47242644891,1.96570855716,1.601229077,1.30212542102,1.06385209308,0.831302509302,0.677874591796,0.549358919398,0.424056860776,0.340829423635,0.273667937606,0.224933981411,0.169136043159,0.134130717402,0.109214583305,0.0839402001966,0.0749150127236,0.0546945436156,0.0456772496344,0.0335775047576,0.0232891545242,0.0212999137353,0.0166102015947,0.014084261122,0.0115498803889,0.00722385414375,0.00523374699602,0.00505379848632,0.00361137529754,0.00216495415144,0.00306632391437,0.0021673033316,0.000721916425448,0.000360913277578,0.000542129251024,0.00180484381525,0.000902779425045,0.000541718019355,0.00054043118767,0.0,0.0,0.00018043205345,0.0,0.000180533398184,0.0,0.0,0.000180232983438,0.000180033566882,0.0,0.0,0.0])

    # Creating a new Canvas
    fig   = plt.figure(figsize=(12,6),dpi=80)
    frame = gridspec.GridSpec(1,1,right=0.7)
    pad   = fig.add_subplot(frame[0])

    # Creating a new Stack
    pad.hist(x=xData, bins=xBinning, weights=y15_TET_0_weights+y15_TET_1_weights+y15_TET_2_weights+y15_TET_3_weights+y15_TET_4_weights+y15_TET_5_weights+y15_TET_6_weights+y15_TET_7_weights+y15_TET_8_weights+y15_TET_9_weights+y15_TET_10_weights+y15_TET_11_weights+y15_TET_12_weights+y15_TET_13_weights+y15_TET_14_weights+y15_TET_15_weights+y15_TET_16_weights+y15_TET_17_weights,\
             label="$bg\_dip\_1600\_inf$", histtype="step", rwidth=1.0,\
             color=None, edgecolor="#f2f2f2", linewidth=1, linestyle="solid",\
             bottom=None, cumulative=False, normed=False, align="mid", orientation="vertical")

    pad.hist(x=xData, bins=xBinning, weights=y15_TET_0_weights+y15_TET_1_weights+y15_TET_2_weights+y15_TET_3_weights+y15_TET_4_weights+y15_TET_5_weights+y15_TET_6_weights+y15_TET_7_weights+y15_TET_8_weights+y15_TET_9_weights+y15_TET_10_weights+y15_TET_11_weights+y15_TET_12_weights+y15_TET_13_weights+y15_TET_14_weights+y15_TET_15_weights+y15_TET_16_weights,\
             label="$bg\_dip\_1200\_1600$", histtype="step", rwidth=1.0,\
             color=None, edgecolor="#ccc6aa", linewidth=1, linestyle="solid",\
             bottom=None, cumulative=False, normed=False, align="mid", orientation="vertical")

    pad.hist(x=xData, bins=xBinning, weights=y15_TET_0_weights+y15_TET_1_weights+y15_TET_2_weights+y15_TET_3_weights+y15_TET_4_weights+y15_TET_5_weights+y15_TET_6_weights+y15_TET_7_weights+y15_TET_8_weights+y15_TET_9_weights+y15_TET_10_weights+y15_TET_11_weights+y15_TET_12_weights+y15_TET_13_weights+y15_TET_14_weights+y15_TET_15_weights,\
             label="$bg\_dip\_800\_1200$", histtype="step", rwidth=1.0,\
             color=None, edgecolor="#ccc6aa", linewidth=1, linestyle="solid",\
             bottom=None, cumulative=False, normed=False, align="mid", orientation="vertical")

    pad.hist(x=xData, bins=xBinning, weights=y15_TET_0_weights+y15_TET_1_weights+y15_TET_2_weights+y15_TET_3_weights+y15_TET_4_weights+y15_TET_5_weights+y15_TET_6_weights+y15_TET_7_weights+y15_TET_8_weights+y15_TET_9_weights+y15_TET_10_weights+y15_TET_11_weights+y15_TET_12_weights+y15_TET_13_weights+y15_TET_14_weights,\
             label="$bg\_dip\_600\_800$", histtype="step", rwidth=1.0,\
             color=None, edgecolor="#c1bfa8", linewidth=1, linestyle="solid",\
             bottom=None, cumulative=False, normed=False, align="mid", orientation="vertical")

    pad.hist(x=xData, bins=xBinning, weights=y15_TET_0_weights+y15_TET_1_weights+y15_TET_2_weights+y15_TET_3_weights+y15_TET_4_weights+y15_TET_5_weights+y15_TET_6_weights+y15_TET_7_weights+y15_TET_8_weights+y15_TET_9_weights+y15_TET_10_weights+y15_TET_11_weights+y15_TET_12_weights+y15_TET_13_weights,\
             label="$bg\_dip\_400\_600$", histtype="step", rwidth=1.0,\
             color=None, edgecolor="#bab5a3", linewidth=1, linestyle="solid",\
             bottom=None, cumulative=False, normed=False, align="mid", orientation="vertical")

    pad.hist(x=xData, bins=xBinning, weights=y15_TET_0_weights+y15_TET_1_weights+y15_TET_2_weights+y15_TET_3_weights+y15_TET_4_weights+y15_TET_5_weights+y15_TET_6_weights+y15_TET_7_weights+y15_TET_8_weights+y15_TET_9_weights+y15_TET_10_weights+y15_TET_11_weights+y15_TET_12_weights,\
             label="$bg\_dip\_200\_400$", histtype="step", rwidth=1.0,\
             color=None, edgecolor="#b2a596", linewidth=1, linestyle="solid",\
             bottom=None, cumulative=False, normed=False, align="mid", orientation="vertical")

    pad.hist(x=xData, bins=xBinning, weights=y15_TET_0_weights+y15_TET_1_weights+y15_TET_2_weights+y15_TET_3_weights+y15_TET_4_weights+y15_TET_5_weights+y15_TET_6_weights+y15_TET_7_weights+y15_TET_8_weights+y15_TET_9_weights+y15_TET_10_weights+y15_TET_11_weights,\
             label="$bg\_dip\_100\_200$", histtype="step", rwidth=1.0,\
             color=None, edgecolor="#b7a39b", linewidth=1, linestyle="solid",\
             bottom=None, cumulative=False, normed=False, align="mid", orientation="vertical")

    pad.hist(x=xData, bins=xBinning, weights=y15_TET_0_weights+y15_TET_1_weights+y15_TET_2_weights+y15_TET_3_weights+y15_TET_4_weights+y15_TET_5_weights+y15_TET_6_weights+y15_TET_7_weights+y15_TET_8_weights+y15_TET_9_weights+y15_TET_10_weights,\
             label="$bg\_dip\_0\_100$", histtype="step", rwidth=1.0,\
             color=None, edgecolor="#ad998c", linewidth=1, linestyle="solid",\
             bottom=None, cumulative=False, normed=False, align="mid", orientation="vertical")

    pad.hist(x=xData, bins=xBinning, weights=y15_TET_0_weights+y15_TET_1_weights+y15_TET_2_weights+y15_TET_3_weights+y15_TET_4_weights+y15_TET_5_weights+y15_TET_6_weights+y15_TET_7_weights+y15_TET_8_weights+y15_TET_9_weights,\
             label="$bg\_vbf\_1600\_inf$", histtype="step", rwidth=1.0,\
             color=None, edgecolor="#9b8e82", linewidth=1, linestyle="solid",\
             bottom=None, cumulative=False, normed=False, align="mid", orientation="vertical")

    pad.hist(x=xData, bins=xBinning, weights=y15_TET_0_weights+y15_TET_1_weights+y15_TET_2_weights+y15_TET_3_weights+y15_TET_4_weights+y15_TET_5_weights+y15_TET_6_weights+y15_TET_7_weights+y15_TET_8_weights,\
             label="$bg\_vbf\_1200\_1600$", histtype="step", rwidth=1.0,\
             color=None, edgecolor="#876656", linewidth=1, linestyle="solid",\
             bottom=None, cumulative=False, normed=False, align="mid", orientation="vertical")

    pad.hist(x=xData, bins=xBinning, weights=y15_TET_0_weights+y15_TET_1_weights+y15_TET_2_weights+y15_TET_3_weights+y15_TET_4_weights+y15_TET_5_weights+y15_TET_6_weights+y15_TET_7_weights,\
             label="$bg\_vbf\_800\_1200$", histtype="step", rwidth=1.0,\
             color=None, edgecolor="#afcec6", linewidth=1, linestyle="solid",\
             bottom=None, cumulative=False, normed=False, align="mid", orientation="vertical")

    pad.hist(x=xData, bins=xBinning, weights=y15_TET_0_weights+y15_TET_1_weights+y15_TET_2_weights+y15_TET_3_weights+y15_TET_4_weights+y15_TET_5_weights+y15_TET_6_weights,\
             label="$bg\_vbf\_600\_800$", histtype="step", rwidth=1.0,\
             color=None, edgecolor="#84c1a3", linewidth=1, linestyle="solid",\
             bottom=None, cumulative=False, normed=False, align="mid", orientation="vertical")

    pad.hist(x=xData, bins=xBinning, weights=y15_TET_0_weights+y15_TET_1_weights+y15_TET_2_weights+y15_TET_3_weights+y15_TET_4_weights+y15_TET_5_weights,\
             label="$bg\_vbf\_400\_600$", histtype="step", rwidth=1.0,\
             color=None, edgecolor="#89a8a0", linewidth=1, linestyle="solid",\
             bottom=None, cumulative=False, normed=False, align="mid", orientation="vertical")

    pad.hist(x=xData, bins=xBinning, weights=y15_TET_0_weights+y15_TET_1_weights+y15_TET_2_weights+y15_TET_3_weights+y15_TET_4_weights,\
             label="$bg\_vbf\_200\_400$", histtype="step", rwidth=1.0,\
             color=None, edgecolor="#829e8c", linewidth=1, linestyle="solid",\
             bottom=None, cumulative=False, normed=False, align="mid", orientation="vertical")

    pad.hist(x=xData, bins=xBinning, weights=y15_TET_0_weights+y15_TET_1_weights+y15_TET_2_weights+y15_TET_3_weights,\
             label="$bg\_vbf\_100\_200$", histtype="step", rwidth=1.0,\
             color=None, edgecolor="#adbcc6", linewidth=1, linestyle="solid",\
             bottom=None, cumulative=False, normed=False, align="mid", orientation="vertical")

    pad.hist(x=xData, bins=xBinning, weights=y15_TET_0_weights+y15_TET_1_weights+y15_TET_2_weights,\
             label="$bg\_vbf\_0\_100$", histtype="step", rwidth=1.0,\
             color=None, edgecolor="#7a8e99", linewidth=1, linestyle="solid",\
             bottom=None, cumulative=False, normed=False, align="mid", orientation="vertical")

    pad.hist(x=xData, bins=xBinning, weights=y15_TET_0_weights+y15_TET_1_weights,\
             label="$signal2$", histtype="step", rwidth=1.0,\
             color=None, edgecolor="#758991", linewidth=1, linestyle="solid",\
             bottom=None, cumulative=False, normed=False, align="mid", orientation="vertical")

    pad.hist(x=xData, bins=xBinning, weights=y15_TET_0_weights,\
             label="$signal1$", histtype="step", rwidth=1.0,\
             color=None, edgecolor="#688296", linewidth=1, linestyle="solid",\
             bottom=None, cumulative=False, normed=False, align="mid", orientation="vertical")


    # Axis
    plt.rc('text',usetex=False)
    plt.xlabel(r"TET",\
               fontsize=16,color="black")
    plt.ylabel(r"$\mathrm{Events}$ $(\mathcal{L}_{\mathrm{int}} = 40.0\ \mathrm{fb}^{-1})$ ",\
               fontsize=16,color="black")

    # Boundary of y-axis
    ymax=(y15_TET_0_weights+y15_TET_1_weights+y15_TET_2_weights+y15_TET_3_weights+y15_TET_4_weights+y15_TET_5_weights+y15_TET_6_weights+y15_TET_7_weights+y15_TET_8_weights+y15_TET_9_weights+y15_TET_10_weights+y15_TET_11_weights+y15_TET_12_weights+y15_TET_13_weights+y15_TET_14_weights+y15_TET_15_weights+y15_TET_16_weights+y15_TET_17_weights).max()*1.1
    ymin=0 # linear scale
    #ymin=min([x for x in (y15_TET_0_weights+y15_TET_1_weights+y15_TET_2_weights+y15_TET_3_weights+y15_TET_4_weights+y15_TET_5_weights+y15_TET_6_weights+y15_TET_7_weights+y15_TET_8_weights+y15_TET_9_weights+y15_TET_10_weights+y15_TET_11_weights+y15_TET_12_weights+y15_TET_13_weights+y15_TET_14_weights+y15_TET_15_weights+y15_TET_16_weights+y15_TET_17_weights) if x])/100. # log scale
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
