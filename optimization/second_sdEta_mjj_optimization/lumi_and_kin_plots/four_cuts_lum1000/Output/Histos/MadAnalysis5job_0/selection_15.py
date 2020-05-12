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
    y16_TET_0_weights = numpy.array([0.0,0.0,0.0,0.0,0.0,0.0,173.486865669,591.185742244,974.596745369,1180.73408576,1322.38897607,1366.50294192,1347.97695626,1281.14100801,1225.97305073,1124.13312958,1023.00920788,928.435981111,825.265060997,748.910420118,656.588791603,589.24104375,522.712195264,447.585753434,397.637892109,338.478437916,296.309370567,253.730903536,224.355826281,196.004248234,162.944573832,138.277692931,126.916601728,105.729718133,89.8651504173,77.9923096105,64.9935896754,57.2148256985,46.3655040992,43.1925865559,36.7444115488,28.5562378889,25.2809704249,21.6986431987,18.9351353385,16.3763373198,11.0540314409,11.6681409653,10.8493215994,6.95994361091,5.32230987893,5.62936564118,4.60584443369,3.68467614695,2.86585878096,1.73998565273,2.55880301872,2.45645009797,1.84233757348,1.22822504898,1.12587312824,1.02352120749,0.818816865989,0.307056362246,0.307056362246,0.102352120749,0.102352120749,0.102352120749,0.307056362246,0.0,0.204704241497,0.0,0.0,0.102352120749,0.102352120749,0.102352120749,0.204704241497,0.0,0.0,0.0])

    # Creating weights for histo: y16_TET_1
    y16_TET_1_weights = numpy.array([0.0,0.0,0.0,0.0,0.0,0.0,0.30426231951,0.607485489427,0.0,0.0,0.303284591063,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0])

    # Creating weights for histo: y16_TET_2
    y16_TET_2_weights = numpy.array([0.0,0.0,0.0,0.0,0.0,0.0,5.52197741463,11.0440457341,5.77023121308,3.01361006857,1.25512784341,1.25449047675,0.25136635841,0.753653951577,0.251741753945,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0])

    # Creating weights for histo: y16_TET_3
    y16_TET_3_weights = numpy.array([0.0,0.0,0.0,0.0,0.0,0.0,12.7877940472,34.5101293879,39.1891720191,29.2922671645,16.9169160944,8.25141591811,4.81351900928,1.64931182145,1.92551018378,0.687304446866,0.137592679372,0.274583894214,0.137360706224,0.0,0.2743201314,0.0,0.137399503834,0.0,0.0,0.0,0.0,0.137855426542,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0])

    # Creating weights for histo: y16_TET_4
    y16_TET_4_weights = numpy.array([0.0,0.0,0.0,0.0,0.0,0.0,0.0,2.29408019986,15.8389752909,24.7447626222,26.2756084394,18.6023700419,10.8549983353,5.32887020115,2.88656847646,1.57932106488,0.912715512392,0.394596432648,0.493628132016,0.197377780865,0.123448193124,0.12339297894,0.0246054845927,0.0493374507516,0.0245977185323,0.024704318984,0.0,0.0492511623055,0.0246357171141,0.0247223663062,0.0,0.0,0.0,0.0246698577175,0.0,0.0,0.0246572616686,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0])

    # Creating weights for histo: y16_TET_5
    y16_TET_5_weights = numpy.array([0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.37801355188,2.79134211234,6.54142920104,8.57735738164,8.28701592621,5.97412004219,4.06446828849,2.01035600632,0.951686095982,0.561042100625,0.34670816914,0.182789881787,0.0882157189614,0.075647582965,0.0567348269824,0.018916967164,0.018885418313,0.0251808144893,0.0189123258619,0.0,0.0126068168484,0.00630044659325,0.0,0.0,0.00629895417455,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0])

    # Creating weights for histo: y16_TET_6
    y16_TET_6_weights = numpy.array([0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0931335704745,0.458025689152,0.902055678909,1.71057342937,2.13300192099,2.32643868692,2.05364188921,1.77545290209,1.34582874303,0.89465382114,0.665707582287,0.49364263097,0.343658788983,0.185844863164,0.0573471527056,0.0500289457259,0.035866419615,0.0143431638312,0.0143235370115,0.0,0.0143046474785,0.0,0.00715459433209,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0])

    # Creating weights for histo: y16_TET_7
    y16_TET_7_weights = numpy.array([0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.00378083755543,0.0275346056517,0.0550804325853,0.103662936157,0.100455671653,0.0955458526422,0.0923080989402,0.0949987025148,0.122023426106,0.126819240664,0.139239764391,0.106887896969,0.102609885377,0.0707002684797,0.050186141063,0.0313237109135,0.0210157742504,0.0124156726965,0.00540197856989,0.00378193872885,0.00270210145962,0.000539834920288,0.000540730108272,0.000540552097459,0.000541879687223,0.0,0.00107762339726,0.0,0.0,0.0,0.0,0.0,0.0,0.000539568899421,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0])

    # Creating weights for histo: y16_TET_8
    y16_TET_8_weights = numpy.array([0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.00142146324715,0.00212835950115,0.00567095696553,0.00213070111084,0.00709502538338,0.00780043715781,0.00568032637398,0.00283928452654,0.00354859589034,0.00495328774787,0.00709963955719,0.00991850255968,0.0127685734135,0.00781342960217,0.0141590322339,0.00710290622892,0.00851372235352,0.00705882472125,0.00425622825911,0.00776780013756,0.0035159388246,0.00141994387358,0.00212070843627,0.000711222737972,0.00141947837286,0.0,0.00141996948726,0.0028380962747,0.00141795862809,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.000699318318018,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0])

    # Creating weights for histo: y16_TET_9
    y16_TET_9_weights = numpy.array([0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0])

    # Creating weights for histo: y16_TET_10
    y16_TET_10_weights = numpy.array([0.0,0.0,0.0,0.0,0.0,0.0,52.6685554354,0.0,26.32395418,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0])

    # Creating weights for histo: y16_TET_11
    y16_TET_11_weights = numpy.array([0.0,0.0,0.0,0.0,0.0,0.0,17.2957498379,132.445455668,126.670358804,126.703502087,34.5193626012,17.2656999286,11.5258310121,5.75321365076,0.0,0.0,5.76682929542,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0])

    # Creating weights for histo: y16_TET_12
    y16_TET_12_weights = numpy.array([0.0,0.0,0.0,0.0,0.0,0.0,0.0,8.31089414955,40.1450629633,53.3093801052,62.9921627135,65.7718375494,34.6194012491,17.9936200182,8.30346702718,6.23153357745,3.46006387012,2.77033587627,0.693159876388,0.691740423764,1.38559156204,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0])

    # Creating weights for histo: y16_TET_13
    y16_TET_13_weights = numpy.array([0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,1.51204543908,3.77859903748,10.0803347887,11.345713632,18.6548606521,16.1284846835,13.3587686138,5.79379481017,4.28660521882,1.76442131629,1.765736742,0.504376395336,0.252383918448,0.251073954714,0.0,0.0,0.252014173067,0.0,0.0,0.0,0.0,0.252437931314,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0])

    # Creating weights for histo: y16_TET_14
    y16_TET_14_weights = numpy.array([0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.282939572626,1.27348700987,1.55658682858,2.47438331145,2.54610738273,3.81953283348,4.95091061167,6.29669207656,3.53631566769,2.97076913407,2.68718742286,1.55537969269,1.13175867525,1.06056362766,0.283089526798,0.212181113868,0.0,0.0707535244092,0.0705869877487,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0])

    # Creating weights for histo: y16_TET_15
    y16_TET_15_weights = numpy.array([0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0764573940003,0.0760889385865,0.0,0.153104836535,0.11436297599,0.0762237335824,0.0,0.152929000274,0.076100137031,0.189876775473,0.265915217644,0.456933466215,0.151700953449,0.266367292049,0.113848586231,0.0767248270356,0.0760457994603,0.152740635939,0.0377789125145,0.0384553694706,0.0,0.0,0.0378163490028,0.0,0.0,0.0381124134171,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0])

    # Creating weights for histo: y16_TET_16
    y16_TET_16_weights = numpy.array([0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.00451382575002,0.0,0.0180439844608,0.00451565346312,0.00451835797802,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.00451367849351,0.0632160147112,0.0315621605344,0.00451642824408,0.00902933099417,0.0270730315291,0.0135403607955,0.00901267464722,0.00904261391595,0.00903957542714,0.00904179582425,0.00903489401771,0.0,0.0,0.00450507505625,0.0,0.0,0.0045191741448,0.0,0.0,0.0,0.0,0.00451887578194,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0])

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
    plt.ylabel(r"$\mathrm{Events}$ $(\mathcal{L}_{\mathrm{int}} = 1000.0\ \mathrm{fb}^{-1})$ ",\
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
