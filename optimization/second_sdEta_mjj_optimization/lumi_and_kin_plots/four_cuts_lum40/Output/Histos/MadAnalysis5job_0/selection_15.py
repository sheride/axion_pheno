def selection_15():

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

    # Creating weights for histo: y16_TET_0
    y16_TET_0_weights = numpy.array([0.0,0.0,0.0,0.0,0.0,0.0,6.93947462676,23.6474296898,38.9838698148,47.2293634303,52.8955590429,54.6601176766,53.9190782504,51.2456403205,49.0389220291,44.9653251833,40.9203683153,37.1374392445,33.0106024399,29.9564168047,26.2635516641,23.56964175,20.9084878105,17.9034301374,15.9055156843,13.5391375166,11.8523748227,10.1492361414,8.97423305124,7.84016992935,6.51778295328,5.53110771726,5.07666406913,4.22918872534,3.59460601669,3.11969238442,2.59974358702,2.28859302794,1.85462016397,1.72770346224,1.46977646195,1.14224951556,1.011238817,0.867945727949,0.75740541354,0.655053492792,0.442161257634,0.466725638614,0.433972863974,0.278397744436,0.212892395157,0.225174625647,0.184233777348,0.147387045878,0.114634351239,0.0695994261091,0.102352120749,0.0982580039187,0.0736935029391,0.0491290019594,0.0450349251294,0.0409408482995,0.0327526746396,0.0122822544898,0.0122822544898,0.00409408482995,0.00409408482995,0.00409408482995,0.0122822544898,0.0,0.00818816965989,0.0,0.0,0.00409408482995,0.00409408482995,0.00409408482995,0.00818816965989,0.0,0.0,0.0])

    # Creating weights for histo: y16_TET_1
    y16_TET_1_weights = numpy.array([0.0,0.0,0.0,0.0,0.0,0.0,0.0121704927804,0.0242994195771,0.0,0.0,0.0121313836425,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0])

    # Creating weights for histo: y16_TET_2
    y16_TET_2_weights = numpy.array([0.0,0.0,0.0,0.0,0.0,0.0,0.220879096585,0.441761829362,0.230809248523,0.120544402743,0.0502051137366,0.0501796190701,0.0100546543364,0.0301461580631,0.0100696701578,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0])

    # Creating weights for histo: y16_TET_3
    y16_TET_3_weights = numpy.array([0.0,0.0,0.0,0.0,0.0,0.0,0.511511761888,1.38040517552,1.56756688076,1.17169068658,0.676676643777,0.330056636725,0.192540760371,0.0659724728581,0.0770204073513,0.0274921778746,0.00550370717489,0.0109833557686,0.00549442824894,0.0,0.010972805256,0.0,0.00549598015337,0.0,0.0,0.0,0.0,0.00551421706168,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0])

    # Creating weights for histo: y16_TET_4
    y16_TET_4_weights = numpy.array([0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0917632079944,0.633559011637,0.989790504888,1.05102433758,0.744094801675,0.434199933413,0.213154808046,0.115462739059,0.0631728425952,0.0365086204957,0.0157838573059,0.0197451252806,0.0078951112346,0.00493792772495,0.00493571915759,0.000984219383707,0.00197349803006,0.000983908741293,0.00098817275936,0.0,0.00197004649222,0.000985428684564,0.000988894652248,0.0,0.0,0.0,0.000986794308699,0.0,0.0,0.000986290466745,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0])

    # Creating weights for histo: y16_TET_5
    y16_TET_5_weights = numpy.array([0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0151205420752,0.111653684494,0.261657168041,0.343094295266,0.331480637049,0.238964801687,0.16257873154,0.0804142402529,0.0380674438393,0.022441684025,0.0138683267656,0.00731159527149,0.00352862875846,0.0030259033186,0.0022693930793,0.000756678686561,0.000755416732519,0.00100723257957,0.000756493034476,0.0,0.000504272673936,0.00025201786373,0.0,0.0,0.000251958166982,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0])

    # Creating weights for histo: y16_TET_6
    y16_TET_6_weights = numpy.array([0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.00372534281898,0.0183210275661,0.0360822271564,0.0684229371749,0.0853200768397,0.0930575474769,0.0821456755683,0.0710181160836,0.0538331497211,0.0357861528456,0.0266283032915,0.0197457052388,0.0137463515593,0.00743379452655,0.00229388610822,0.00200115782904,0.0014346567846,0.000573726553247,0.000572941480461,0.0,0.000572185899139,0.0,0.000286183773284,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0])

    # Creating weights for histo: y16_TET_7
    y16_TET_7_weights = numpy.array([0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.000151233502217,0.00110138422607,0.00220321730341,0.00414651744629,0.00401822686611,0.00382183410569,0.00369232395761,0.00379994810059,0.00488093704425,0.00507276962655,0.00556959057563,0.00427551587877,0.00410439541507,0.00282801073919,0.00200744564252,0.00125294843654,0.000840630970017,0.00049662690786,0.000216079142796,0.000151277549154,0.000108084058385,2.15933968115e-05,2.16292043309e-05,2.16220838984e-05,2.16751874889e-05,0.0,4.31049358904e-05,0.0,0.0,0.0,0.0,0.0,0.0,2.15827559768e-05,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0])

    # Creating weights for histo: y16_TET_8
    y16_TET_8_weights = numpy.array([0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,5.6858529886e-05,8.51343800459e-05,0.000226838278621,8.52280444334e-05,0.000283801015335,0.000312017486312,0.000227213054959,0.000113571381062,0.000141943835613,0.000198131509915,0.000283985582288,0.000396740102387,0.000510742936541,0.000312537184087,0.000566361289355,0.000284116249157,0.000340548894141,0.00028235298885,0.000170249130364,0.000310712005502,0.000140637552984,5.67977549434e-05,8.48283374507e-05,2.84489095189e-05,5.67791349145e-05,0.0,5.67987794904e-05,0.000113523850988,5.67183451234e-05,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,2.79727327207e-05,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0])

    # Creating weights for histo: y16_TET_9
    y16_TET_9_weights = numpy.array([0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0])

    # Creating weights for histo: y16_TET_10
    y16_TET_10_weights = numpy.array([0.0,0.0,0.0,0.0,0.0,0.0,2.10674221742,0.0,1.0529581672,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0])

    # Creating weights for histo: y16_TET_11
    y16_TET_11_weights = numpy.array([0.0,0.0,0.0,0.0,0.0,0.0,0.691829993515,5.2978182267,5.06681435217,5.06814008347,1.38077450405,0.690627997143,0.461033240486,0.23012854603,0.0,0.0,0.230673171817,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0])

    # Creating weights for histo: y16_TET_12
    y16_TET_12_weights = numpy.array([0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.332435765982,1.60580251853,2.13237520421,2.51968650854,2.63087350198,1.38477604996,0.719744800729,0.332138681087,0.249261343098,0.138402554805,0.110813435051,0.0277263950555,0.0276696169506,0.0554236624816,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0])

    # Creating weights for histo: y16_TET_13
    y16_TET_13_weights = numpy.array([0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0604818175633,0.151143961499,0.403213391549,0.453828545279,0.746194426083,0.645139387342,0.534350744552,0.231751792407,0.171464208753,0.0705768526515,0.0706294696799,0.0201750558134,0.0100953567379,0.0100429581886,0.0,0.0,0.0100805669227,0.0,0.0,0.0,0.0,0.0100975172526,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0])

    # Creating weights for histo: y16_TET_14
    y16_TET_14_weights = numpy.array([0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.011317582905,0.0509394803948,0.0622634731433,0.0989753324578,0.101844295309,0.152781313339,0.198036424467,0.251867683062,0.141452626708,0.118830765363,0.107487496914,0.0622151877075,0.0452703470099,0.0424225451063,0.0113235810719,0.00848724455472,0.0,0.00283014097637,0.00282347950995,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0])

    # Creating weights for histo: y16_TET_15
    y16_TET_15_weights = numpy.array([0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.00305829576001,0.00304355754346,0.0,0.00612419346139,0.00457451903961,0.00304894934329,0.0,0.00611716001098,0.00304400548124,0.0075950710189,0.0106366087057,0.0182773386486,0.00606803813798,0.0106546916819,0.00455394344924,0.00306899308143,0.00304183197841,0.00610962543756,0.00151115650058,0.00153821477883,0.0,0.0,0.00151265396011,0.0,0.0,0.00152449653668,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0])

    # Creating weights for histo: y16_TET_16
    y16_TET_16_weights = numpy.array([0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.000180553030001,0.0,0.000721759378433,0.000180626138525,0.000180734319121,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.000180547139741,0.00252864058845,0.00126248642138,0.000180657129763,0.000361173239767,0.00108292126116,0.00054161443182,0.000360506985889,0.000361704556638,0.000361583017085,0.00036167183297,0.000361395760708,0.0,0.0,0.00018020300225,0.0,0.0,0.000180766965792,0.0,0.0,0.0,0.0,0.000180755031278,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0])

    # Creating a new Canvas
    fig   = plt.figure(figsize=(12,6),dpi=80)
    frame = gridspec.GridSpec(1,1,right=0.7)
    pad   = fig.add_subplot(frame[0])

    # Creating a new Stack
    pad.hist(x=xData, bins=xBinning, weights=y16_TET_0_weights+y16_TET_1_weights+y16_TET_2_weights+y16_TET_3_weights+y16_TET_4_weights+y16_TET_5_weights+y16_TET_6_weights+y16_TET_7_weights+y16_TET_8_weights+y16_TET_9_weights+y16_TET_10_weights+y16_TET_11_weights+y16_TET_12_weights+y16_TET_13_weights+y16_TET_14_weights+y16_TET_15_weights+y16_TET_16_weights,\
             label="$bg\_dip\_1600\_inf$", histtype="step", rwidth=1.0,\
             color=None, edgecolor="#e5e5e5", linewidth=1, linestyle="solid",\
             bottom=None, cumulative=False, normed=False, align="mid", orientation="vertical")

    pad.hist(x=xData, bins=xBinning, weights=y16_TET_0_weights+y16_TET_1_weights+y16_TET_2_weights+y16_TET_3_weights+y16_TET_4_weights+y16_TET_5_weights+y16_TET_6_weights+y16_TET_7_weights+y16_TET_8_weights+y16_TET_9_weights+y16_TET_10_weights+y16_TET_11_weights+y16_TET_12_weights+y16_TET_13_weights+y16_TET_14_weights+y16_TET_15_weights,\
             label="$bg\_dip\_1200\_1600$", histtype="step", rwidth=1.0,\
             color=None, edgecolor="#f2f2f2", linewidth=1, linestyle="solid",\
             bottom=None, cumulative=False, normed=False, align="mid", orientation="vertical")

    pad.hist(x=xData, bins=xBinning, weights=y16_TET_0_weights+y16_TET_1_weights+y16_TET_2_weights+y16_TET_3_weights+y16_TET_4_weights+y16_TET_5_weights+y16_TET_6_weights+y16_TET_7_weights+y16_TET_8_weights+y16_TET_9_weights+y16_TET_10_weights+y16_TET_11_weights+y16_TET_12_weights+y16_TET_13_weights+y16_TET_14_weights,\
             label="$bg\_dip\_800\_1200$", histtype="step", rwidth=1.0,\
             color=None, edgecolor="#ccc6aa", linewidth=1, linestyle="solid",\
             bottom=None, cumulative=False, normed=False, align="mid", orientation="vertical")

    pad.hist(x=xData, bins=xBinning, weights=y16_TET_0_weights+y16_TET_1_weights+y16_TET_2_weights+y16_TET_3_weights+y16_TET_4_weights+y16_TET_5_weights+y16_TET_6_weights+y16_TET_7_weights+y16_TET_8_weights+y16_TET_9_weights+y16_TET_10_weights+y16_TET_11_weights+y16_TET_12_weights+y16_TET_13_weights,\
             label="$bg\_dip\_600\_800$", histtype="step", rwidth=1.0,\
             color=None, edgecolor="#ccc6aa", linewidth=1, linestyle="solid",\
             bottom=None, cumulative=False, normed=False, align="mid", orientation="vertical")

    pad.hist(x=xData, bins=xBinning, weights=y16_TET_0_weights+y16_TET_1_weights+y16_TET_2_weights+y16_TET_3_weights+y16_TET_4_weights+y16_TET_5_weights+y16_TET_6_weights+y16_TET_7_weights+y16_TET_8_weights+y16_TET_9_weights+y16_TET_10_weights+y16_TET_11_weights+y16_TET_12_weights,\
             label="$bg\_dip\_400\_600$", histtype="step", rwidth=1.0,\
             color=None, edgecolor="#c1bfa8", linewidth=1, linestyle="solid",\
             bottom=None, cumulative=False, normed=False, align="mid", orientation="vertical")

    pad.hist(x=xData, bins=xBinning, weights=y16_TET_0_weights+y16_TET_1_weights+y16_TET_2_weights+y16_TET_3_weights+y16_TET_4_weights+y16_TET_5_weights+y16_TET_6_weights+y16_TET_7_weights+y16_TET_8_weights+y16_TET_9_weights+y16_TET_10_weights+y16_TET_11_weights,\
             label="$bg\_dip\_200\_400$", histtype="step", rwidth=1.0,\
             color=None, edgecolor="#bab5a3", linewidth=1, linestyle="solid",\
             bottom=None, cumulative=False, normed=False, align="mid", orientation="vertical")

    pad.hist(x=xData, bins=xBinning, weights=y16_TET_0_weights+y16_TET_1_weights+y16_TET_2_weights+y16_TET_3_weights+y16_TET_4_weights+y16_TET_5_weights+y16_TET_6_weights+y16_TET_7_weights+y16_TET_8_weights+y16_TET_9_weights+y16_TET_10_weights,\
             label="$bg\_dip\_100\_200$", histtype="step", rwidth=1.0,\
             color=None, edgecolor="#b2a596", linewidth=1, linestyle="solid",\
             bottom=None, cumulative=False, normed=False, align="mid", orientation="vertical")

    pad.hist(x=xData, bins=xBinning, weights=y16_TET_0_weights+y16_TET_1_weights+y16_TET_2_weights+y16_TET_3_weights+y16_TET_4_weights+y16_TET_5_weights+y16_TET_6_weights+y16_TET_7_weights+y16_TET_8_weights+y16_TET_9_weights,\
             label="$bg\_dip\_0\_100$", histtype="step", rwidth=1.0,\
             color=None, edgecolor="#b7a39b", linewidth=1, linestyle="solid",\
             bottom=None, cumulative=False, normed=False, align="mid", orientation="vertical")

    pad.hist(x=xData, bins=xBinning, weights=y16_TET_0_weights+y16_TET_1_weights+y16_TET_2_weights+y16_TET_3_weights+y16_TET_4_weights+y16_TET_5_weights+y16_TET_6_weights+y16_TET_7_weights+y16_TET_8_weights,\
             label="$bg\_vbf\_1600\_inf$", histtype="step", rwidth=1.0,\
             color=None, edgecolor="#ad998c", linewidth=1, linestyle="solid",\
             bottom=None, cumulative=False, normed=False, align="mid", orientation="vertical")

    pad.hist(x=xData, bins=xBinning, weights=y16_TET_0_weights+y16_TET_1_weights+y16_TET_2_weights+y16_TET_3_weights+y16_TET_4_weights+y16_TET_5_weights+y16_TET_6_weights+y16_TET_7_weights,\
             label="$bg\_vbf\_1200\_1600$", histtype="step", rwidth=1.0,\
             color=None, edgecolor="#9b8e82", linewidth=1, linestyle="solid",\
             bottom=None, cumulative=False, normed=False, align="mid", orientation="vertical")

    pad.hist(x=xData, bins=xBinning, weights=y16_TET_0_weights+y16_TET_1_weights+y16_TET_2_weights+y16_TET_3_weights+y16_TET_4_weights+y16_TET_5_weights+y16_TET_6_weights,\
             label="$bg\_vbf\_800\_1200$", histtype="step", rwidth=1.0,\
             color=None, edgecolor="#876656", linewidth=1, linestyle="solid",\
             bottom=None, cumulative=False, normed=False, align="mid", orientation="vertical")

    pad.hist(x=xData, bins=xBinning, weights=y16_TET_0_weights+y16_TET_1_weights+y16_TET_2_weights+y16_TET_3_weights+y16_TET_4_weights+y16_TET_5_weights,\
             label="$bg\_vbf\_600\_800$", histtype="step", rwidth=1.0,\
             color=None, edgecolor="#afcec6", linewidth=1, linestyle="solid",\
             bottom=None, cumulative=False, normed=False, align="mid", orientation="vertical")

    pad.hist(x=xData, bins=xBinning, weights=y16_TET_0_weights+y16_TET_1_weights+y16_TET_2_weights+y16_TET_3_weights+y16_TET_4_weights,\
             label="$bg\_vbf\_400\_600$", histtype="step", rwidth=1.0,\
             color=None, edgecolor="#84c1a3", linewidth=1, linestyle="solid",\
             bottom=None, cumulative=False, normed=False, align="mid", orientation="vertical")

    pad.hist(x=xData, bins=xBinning, weights=y16_TET_0_weights+y16_TET_1_weights+y16_TET_2_weights+y16_TET_3_weights,\
             label="$bg\_vbf\_200\_400$", histtype="step", rwidth=1.0,\
             color=None, edgecolor="#89a8a0", linewidth=1, linestyle="solid",\
             bottom=None, cumulative=False, normed=False, align="mid", orientation="vertical")

    pad.hist(x=xData, bins=xBinning, weights=y16_TET_0_weights+y16_TET_1_weights+y16_TET_2_weights,\
             label="$bg\_vbf\_100\_200$", histtype="step", rwidth=1.0,\
             color=None, edgecolor="#829e8c", linewidth=1, linestyle="solid",\
             bottom=None, cumulative=False, normed=False, align="mid", orientation="vertical")

    pad.hist(x=xData, bins=xBinning, weights=y16_TET_0_weights+y16_TET_1_weights,\
             label="$bg\_vbf\_0\_100$", histtype="step", rwidth=1.0,\
             color=None, edgecolor="#adbcc6", linewidth=1, linestyle="solid",\
             bottom=None, cumulative=False, normed=False, align="mid", orientation="vertical")

    pad.hist(x=xData, bins=xBinning, weights=y16_TET_0_weights,\
             label="$signal$", histtype="step", rwidth=1.0,\
             color=None, edgecolor="#7a8e99", linewidth=1, linestyle="solid",\
             bottom=None, cumulative=False, normed=False, align="mid", orientation="vertical")


    # Axis
    plt.rc('text',usetex=False)
    plt.xlabel(r"TET",\
               fontsize=16,color="black")
    plt.ylabel(r"$\mathrm{Events}$ $(\mathcal{L}_{\mathrm{int}} = 40.0\ \mathrm{fb}^{-1})$ ",\
               fontsize=16,color="black")

    # Boundary of y-axis
    ymax=(y16_TET_0_weights+y16_TET_1_weights+y16_TET_2_weights+y16_TET_3_weights+y16_TET_4_weights+y16_TET_5_weights+y16_TET_6_weights+y16_TET_7_weights+y16_TET_8_weights+y16_TET_9_weights+y16_TET_10_weights+y16_TET_11_weights+y16_TET_12_weights+y16_TET_13_weights+y16_TET_14_weights+y16_TET_15_weights+y16_TET_16_weights).max()*1.1
    ymin=0 # linear scale
    #ymin=min([x for x in (y16_TET_0_weights+y16_TET_1_weights+y16_TET_2_weights+y16_TET_3_weights+y16_TET_4_weights+y16_TET_5_weights+y16_TET_6_weights+y16_TET_7_weights+y16_TET_8_weights+y16_TET_9_weights+y16_TET_10_weights+y16_TET_11_weights+y16_TET_12_weights+y16_TET_13_weights+y16_TET_14_weights+y16_TET_15_weights+y16_TET_16_weights) if x])/100. # log scale
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
    plt.savefig('../../HTML/MadAnalysis5job_0/selection_15.png')
    plt.savefig('../../PDF/MadAnalysis5job_0/selection_15.png')
    plt.savefig('../../DVI/MadAnalysis5job_0/selection_15.eps')

# Running!
if __name__ == '__main__':
    selection_15()
