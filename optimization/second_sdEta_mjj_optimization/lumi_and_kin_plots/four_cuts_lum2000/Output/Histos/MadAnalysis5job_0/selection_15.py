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
    y16_TET_0_weights = numpy.array([0.0,0.0,0.0,0.0,0.0,0.0,346.973731338,1182.37148449,1949.19349074,2361.46817151,2644.77795215,2733.00588383,2695.95391252,2562.28201602,2451.94610146,2248.26625917,2046.01841577,1856.87196222,1650.53012199,1497.82084024,1313.17758321,1178.4820875,1045.42439053,895.171506868,795.275784217,676.956875832,592.618741135,507.461807072,448.711652562,392.008496467,325.889147664,276.555385863,253.833203457,211.459436267,179.730300835,155.984619221,129.987179351,114.429651397,92.7310081983,86.3851731119,73.4888230975,57.1124757778,50.5619408498,43.3972863974,37.870270677,32.7526746396,22.1080628817,23.3362819307,21.6986431987,13.9198872218,10.6446197579,11.2587312824,9.21168886738,7.3693522939,5.73171756193,3.47997130546,5.11760603743,4.91290019594,3.68467514695,2.45645009797,2.25174625647,2.04704241497,1.63763373198,0.614112724492,0.614112724492,0.204704241497,0.204704241497,0.204704241497,0.614112724492,0.0,0.409408482995,0.0,0.0,0.204704241497,0.204704241497,0.204704241497,0.409408482995,0.0,0.0,0.0])

    # Creating weights for histo: y16_TET_1
    y16_TET_1_weights = numpy.array([0.0,0.0,0.0,0.0,0.0,0.0,0.60852463902,1.21497097885,0.0,0.0,0.606569182125,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0])

    # Creating weights for histo: y16_TET_2
    y16_TET_2_weights = numpy.array([0.0,0.0,0.0,0.0,0.0,0.0,11.0439548293,22.0880914681,11.5404624262,6.02722013714,2.51025568683,2.5089809535,0.502732716821,1.50730790315,0.503483507891,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0])

    # Creating weights for histo: y16_TET_3
    y16_TET_3_weights = numpy.array([0.0,0.0,0.0,0.0,0.0,0.0,25.5755880944,69.0202587759,78.3783440382,58.5845343291,33.8338321889,16.5028318362,9.62703801856,3.29862364291,3.85102036756,1.37460889373,0.275185358744,0.549167788429,0.274721412447,0.0,0.548640262801,0.0,0.274799007668,0.0,0.0,0.0,0.0,0.275710853084,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0])

    # Creating weights for histo: y16_TET_4
    y16_TET_4_weights = numpy.array([0.0,0.0,0.0,0.0,0.0,0.0,0.0,4.58816039972,31.6779505818,49.4895252444,52.5512168788,37.2047400837,21.7099966706,10.6577404023,5.77313695293,3.15864212976,1.82543102478,0.789192865296,0.987256264031,0.39475556173,0.246896386248,0.24678595788,0.0492109691854,0.0986749015031,0.0491954370647,0.049408637968,0.0,0.0985023246109,0.0492714342282,0.0494447326124,0.0,0.0,0.0,0.049339715435,0.0,0.0,0.0493145233372,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0])

    # Creating weights for histo: y16_TET_5
    y16_TET_5_weights = numpy.array([0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.756027103759,5.58268422468,13.0828584021,17.1547147633,16.5740318524,11.9482400844,8.12893657698,4.02071201264,1.90337219196,1.12208420125,0.69341633828,0.365579763574,0.176431437923,0.15129516593,0.113469653965,0.0378339343281,0.037770836626,0.0503616289787,0.0378246517238,0.0,0.0252136336968,0.0126008931865,0.0,0.0,0.0125979083491,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0])

    # Creating weights for histo: y16_TET_6
    y16_TET_6_weights = numpy.array([0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.186267140949,0.916051378303,1.80411135782,3.42114685875,4.26600384198,4.65287737385,4.10728377842,3.55090580418,2.69165748605,1.78930764228,1.33141516457,0.98728526194,0.687317577967,0.371689726327,0.114694305411,0.100057891452,0.0717328392299,0.0286863276623,0.028647074023,0.0,0.028609294957,0.0,0.0143091886642,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0])

    # Creating weights for histo: y16_TET_7
    y16_TET_7_weights = numpy.array([0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.00756167511086,0.0550692113033,0.110160865171,0.207325872315,0.200911343305,0.191091705284,0.18461619788,0.18999740503,0.244046852212,0.253638481328,0.278479528781,0.213775793939,0.205219770754,0.141400536959,0.100372282126,0.0626474218271,0.0420315485008,0.024831345393,0.0108039571398,0.0075638774577,0.00540420291925,0.00107966984058,0.00108146021654,0.00108110419492,0.00108375937445,0.0,0.00215524679452,0.0,0.0,0.0,0.0,0.0,0.0,0.00107913779884,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0])

    # Creating weights for histo: y16_TET_8
    y16_TET_8_weights = numpy.array([0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0028429264943,0.0042567190023,0.0113419139311,0.00426140222167,0.0141900507668,0.0156008743156,0.011360652748,0.00567856905308,0.00709719178067,0.00990657549575,0.0141992791144,0.0198370051194,0.0255371468271,0.0156268592043,0.0283180644677,0.0142058124578,0.017027444707,0.0141176494425,0.00851245651822,0.0155356002751,0.00703187764921,0.00283988774717,0.00424141687253,0.00142244547594,0.00283895674573,0.0,0.00283993897452,0.00567619254939,0.00283591725617,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.00139863663604,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0])

    # Creating weights for histo: y16_TET_9
    y16_TET_9_weights = numpy.array([0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0])

    # Creating weights for histo: y16_TET_10
    y16_TET_10_weights = numpy.array([0.0,0.0,0.0,0.0,0.0,0.0,105.337110871,0.0,52.64790836,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0])

    # Creating weights for histo: y16_TET_11
    y16_TET_11_weights = numpy.array([0.0,0.0,0.0,0.0,0.0,0.0,34.5914996758,264.890911335,253.340717609,253.407004173,69.0387252025,34.5313998571,23.0516620243,11.5064273015,0.0,0.0,11.5336585908,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0])

    # Creating weights for histo: y16_TET_12
    y16_TET_12_weights = numpy.array([0.0,0.0,0.0,0.0,0.0,0.0,0.0,16.6217882991,80.2901259266,106.61876021,125.984325427,131.543675099,69.2388024982,35.9872400364,16.6069340544,12.4630671549,6.92012774024,5.54067175255,1.38631975278,1.38348084753,2.77118312408,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0])

    # Creating weights for histo: y16_TET_13
    y16_TET_13_weights = numpy.array([0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,3.02409087816,7.55719807496,20.1606695775,22.6914272639,37.3097213042,32.2569693671,26.7175372276,11.5875896203,8.57321043764,3.52884263258,3.53147348399,1.00875279067,0.504767836896,0.502147909429,0.0,0.0,0.504028346134,0.0,0.0,0.0,0.0,0.504875862629,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0])

    # Creating weights for histo: y16_TET_14
    y16_TET_14_weights = numpy.array([0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.565879145251,2.54697401974,3.11317365717,4.94876662289,5.09221476547,7.63906566696,9.90182122333,12.5933841531,7.07263133539,5.94153826814,5.37437484572,3.11075938537,2.26351735049,2.12112725532,0.566179053596,0.424362227736,0.0,0.141507048818,0.141173975497,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0])

    # Creating weights for histo: y16_TET_15
    y16_TET_15_weights = numpy.array([0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.152914788001,0.152177877173,0.0,0.30620967307,0.228725951981,0.152447467165,0.0,0.305858000549,0.152200274062,0.379753550945,0.531830435287,0.913866932431,0.303401906899,0.532734584097,0.227697172462,0.153449654071,0.152091598921,0.305481271878,0.075557825029,0.0769107389413,0.0,0.0,0.0756326980056,0.0,0.0,0.0762248268342,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0])

    # Creating weights for histo: y16_TET_16
    y16_TET_16_weights = numpy.array([0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.00902765150004,0.0,0.0360879689217,0.00903130692623,0.00903671595604,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.00902735698703,0.126432029422,0.0631243210689,0.00903285648815,0.0180586619883,0.0541460630581,0.027080721591,0.0180253492944,0.0180852278319,0.0180791508543,0.0180835916485,0.0180697880354,0.0,0.0,0.00901015011249,0.0,0.0,0.00903834828959,0.0,0.0,0.0,0.0,0.00903775156388,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0])

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
    plt.ylabel(r"$\mathrm{Events}$ $(\mathcal{L}_{\mathrm{int}} = 2000.0\ \mathrm{fb}^{-1})$ ",\
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
