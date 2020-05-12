def selection_6():

    # Library import
    import numpy
    import matplotlib
    import matplotlib.pyplot   as plt
    import matplotlib.gridspec as gridspec

    # Library version
    matplotlib_version = matplotlib.__version__
    numpy_version      = numpy.__version__

    # Histo binning
    xBinning = numpy.linspace(0.0,15.0,76,endpoint=True)

    # Creating data sequence: middle of each bin
    xData = numpy.array([0.1,0.3,0.5,0.7,0.9,1.1,1.3,1.5,1.7,1.9,2.1,2.3,2.5,2.7,2.9,3.1,3.3,3.5,3.7,3.9,4.1,4.3,4.5,4.7,4.9,5.1,5.3,5.5,5.7,5.9,6.1,6.3,6.5,6.7,6.9,7.1,7.3,7.5,7.7,7.9,8.1,8.3,8.5,8.7,8.9,9.1,9.3,9.5,9.7,9.9,10.1,10.3,10.5,10.7,10.9,11.1,11.3,11.5,11.7,11.9,12.1,12.3,12.5,12.7,12.9,13.1,13.3,13.5,13.7,13.9,14.1,14.3,14.5,14.7,14.9])

    # Creating weights for histo: y7_DELTAR_0
    y7_DELTAR_0_weights = numpy.array([0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,646.967625967,1212.05392459,1566.70360992,1787.1704143,1876.93233466,1932.61228526,1714.19247905,1413.17574614,1158.62597199,984.831826192,827.209666045,697.734280924,583.406982363,498.966457284,421.895325666,363.145277793,299.891633916,249.943778233,213.9159102,163.353955062,139.096476584,105.217906644,83.6216658053,67.552380063,50.2548754105,37.6655665806,27.8397652987,21.4939409291,14.3292972861,7.77875909817,5.01525255013,2.04704218373,0.204704218373,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0])

    # Creating weights for histo: y7_DELTAR_1
    y7_DELTAR_1_weights = numpy.array([0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.607667999418,0.0,0.0,0.607364400582,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0])

    # Creating weights for histo: y7_DELTAR_2
    y7_DELTAR_2_weights = numpy.array([0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.753088683611,0.753003253753,1.50500448861,1.75725086575,4.26619667914,1.75746676467,2.76298756046,1.75649883507,2.00698909662,2.25939972222,2.76030483565,2.25995134912,0.251143329947,1.50551272912,1.75690997272,0.250924332003,0.250852331264,0.502759984696,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0])

    # Creating weights for histo: y7_DELTAR_3
    y7_DELTAR_3_weights = numpy.array([0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,2.8878669633,3.43671102668,8.1123893595,10.0358004251,12.6478397049,14.7156307121,13.610152593,12.6531515249,14.8561654241,10.1777824303,9.76374179783,7.83706441996,7.14769376968,6.32709577239,6.87541068504,3.02390541772,2.61349571383,1.51250268029,1.65009202366,0.96238510043,0.1378554422,0.137719447418,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0])

    # Creating weights for histo: y7_DELTAR_4
    y7_DELTAR_4_weights = numpy.array([0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,2.17097663803,4.98337876121,7.69799866813,9.69465981705,12.3851227667,12.4086313832,13.0512202743,11.0772781088,10.2886271575,7.17913564546,5.89679974034,3.89812141986,3.65198841018,2.54130548805,1.62801578039,0.962215186866,0.715581341446,0.345435069006,0.246728741669,0.0493227908571,0.0493518509541,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0])

    # Creating weights for histo: y7_DELTAR_5
    y7_DELTAR_5_weights = numpy.array([0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.907541130041,1.86524333384,3.18259094384,4.09611625287,5.17997535268,5.57062295721,5.68468295918,4.48103825096,3.28304612869,2.41350916153,1.55025595741,1.22906484038,0.686974945489,0.415883685047,0.258423706288,0.0882279642391,0.0503926587363,0.0189165674469,0.0189129764394,0.0,0.0126088576842,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0])

    # Creating weights for histo: y7_DELTAR_6
    y7_DELTAR_6_weights = numpy.array([0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.286279885679,0.829978011103,1.1882220666,1.79671218784,2.1475568851,2.66998466727,2.29065796419,1.64631247136,1.08736550974,0.73701142048,0.408356800257,0.271827818861,0.128941502608,0.0214751664675,0.0214716524846,0.0357454284099,0.00712921893245,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0])

    # Creating weights for histo: y7_DELTAR_7
    y7_DELTAR_7_weights = numpy.array([0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0323980930637,0.0739763052056,0.0966412303045,0.152789328601,0.212006892747,0.291512345711,0.239698312951,0.127452282088,0.0669654767724,0.0378133725781,0.0242627476107,0.0075587915959,0.0043210348097,0.00323957356515,0.00161933887427,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0])

    # Creating weights for histo: y7_DELTAR_8
    y7_DELTAR_8_weights = numpy.array([0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.00424914191731,0.00779430492321,0.0148963018625,0.0190966033241,0.023368318686,0.0333473625793,0.0155886803768,0.0127855307362,0.00777528398417,0.0028404041766,0.000710731641734,0.00212584496066,0.0,0.000711222756144,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0])

    # Creating weights for histo: y7_DELTAR_9
    y7_DELTAR_9_weights = numpy.array([0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0])

    # Creating weights for histo: y7_DELTAR_10
    y7_DELTAR_10_weights = numpy.array([0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,26.32395418,0.0,0.0,0.0,26.3028457174,0.0,26.365709718,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0])

    # Creating weights for histo: y7_DELTAR_11
    y7_DELTAR_11_weights = numpy.array([0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,11.513505577,11.5254179451,34.5409586413,69.1341779946,34.5591634298,103.608302486,63.3237859257,17.2697059774,40.2899347669,34.5802214225,17.2741346885,17.2696003032,5.76163301673,0.0,11.5364560992,0.0,5.75900461033,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0])

    # Creating weights for histo: y7_DELTAR_12
    y7_DELTAR_12_weights = numpy.array([0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,13.1447180526,20.7733623743,33.9212443829,38.0712199698,46.372931034,40.1575749246,31.1638806997,27.695050041,21.4672496788,13.8421732224,7.61196382986,3.46079863398,4.84454376704,2.07617163232,1.38242088761,0.69294783075,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0])

    # Creating weights for histo: y7_DELTAR_13
    y7_DELTAR_13_weights = numpy.array([0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,5.03813491451,5.79919893569,9.83195416659,11.3465856482,10.3338247121,16.1281351801,10.334958072,7.81422016066,5.04001322705,3.52738295246,0.756806866773,1.51155927231,1.26072990117,0.754292082415,0.503855214871,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0])

    # Creating weights for histo: y7_DELTAR_14
    y7_DELTAR_14_weights = numpy.array([0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,1.48626034872,2.33338311679,3.89102222894,3.46557271122,7.07258327562,6.64844862226,5.23423456869,2.61682535945,2.2630316212,0.494706607545,0.424407725772,0.282837905221,0.283212934932,0.070586988081,0.141311464613,0.0,0.0,0.0707995209485,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0])

    # Creating weights for histo: y7_DELTAR_15
    y7_DELTAR_15_weights = numpy.array([0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.34220350572,0.493980553828,0.419071524384,0.189974619555,0.419475141168,0.343001284135,0.22921379414,0.114627550667,0.0380651697779,0.0379704705253,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0])

    # Creating weights for histo: y7_DELTAR_16
    y7_DELTAR_16_weights = numpy.array([0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0135435278264,0.0271046109388,0.0406187355859,0.0270646784378,0.0406283120715,0.0451453237452,0.0316096207256,0.00451887596037,0.00902372982849,0.0,0.00450009064934,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0])

    # Creating a new Canvas
    fig   = plt.figure(figsize=(12,6),dpi=80)
    frame = gridspec.GridSpec(1,1,right=0.7)
    pad   = fig.add_subplot(frame[0])

    # Creating a new Stack
    pad.hist(x=xData, bins=xBinning, weights=y7_DELTAR_0_weights+y7_DELTAR_1_weights+y7_DELTAR_2_weights+y7_DELTAR_3_weights+y7_DELTAR_4_weights+y7_DELTAR_5_weights+y7_DELTAR_6_weights+y7_DELTAR_7_weights+y7_DELTAR_8_weights+y7_DELTAR_9_weights+y7_DELTAR_10_weights+y7_DELTAR_11_weights+y7_DELTAR_12_weights+y7_DELTAR_13_weights+y7_DELTAR_14_weights+y7_DELTAR_15_weights+y7_DELTAR_16_weights,\
             label="$bg\_dip\_1600\_inf$", histtype="step", rwidth=1.0,\
             color=None, edgecolor="#e5e5e5", linewidth=1, linestyle="solid",\
             bottom=None, cumulative=False, normed=False, align="mid", orientation="vertical")

    pad.hist(x=xData, bins=xBinning, weights=y7_DELTAR_0_weights+y7_DELTAR_1_weights+y7_DELTAR_2_weights+y7_DELTAR_3_weights+y7_DELTAR_4_weights+y7_DELTAR_5_weights+y7_DELTAR_6_weights+y7_DELTAR_7_weights+y7_DELTAR_8_weights+y7_DELTAR_9_weights+y7_DELTAR_10_weights+y7_DELTAR_11_weights+y7_DELTAR_12_weights+y7_DELTAR_13_weights+y7_DELTAR_14_weights+y7_DELTAR_15_weights,\
             label="$bg\_dip\_1200\_1600$", histtype="step", rwidth=1.0,\
             color=None, edgecolor="#f2f2f2", linewidth=1, linestyle="solid",\
             bottom=None, cumulative=False, normed=False, align="mid", orientation="vertical")

    pad.hist(x=xData, bins=xBinning, weights=y7_DELTAR_0_weights+y7_DELTAR_1_weights+y7_DELTAR_2_weights+y7_DELTAR_3_weights+y7_DELTAR_4_weights+y7_DELTAR_5_weights+y7_DELTAR_6_weights+y7_DELTAR_7_weights+y7_DELTAR_8_weights+y7_DELTAR_9_weights+y7_DELTAR_10_weights+y7_DELTAR_11_weights+y7_DELTAR_12_weights+y7_DELTAR_13_weights+y7_DELTAR_14_weights,\
             label="$bg\_dip\_800\_1200$", histtype="step", rwidth=1.0,\
             color=None, edgecolor="#ccc6aa", linewidth=1, linestyle="solid",\
             bottom=None, cumulative=False, normed=False, align="mid", orientation="vertical")

    pad.hist(x=xData, bins=xBinning, weights=y7_DELTAR_0_weights+y7_DELTAR_1_weights+y7_DELTAR_2_weights+y7_DELTAR_3_weights+y7_DELTAR_4_weights+y7_DELTAR_5_weights+y7_DELTAR_6_weights+y7_DELTAR_7_weights+y7_DELTAR_8_weights+y7_DELTAR_9_weights+y7_DELTAR_10_weights+y7_DELTAR_11_weights+y7_DELTAR_12_weights+y7_DELTAR_13_weights,\
             label="$bg\_dip\_600\_800$", histtype="step", rwidth=1.0,\
             color=None, edgecolor="#ccc6aa", linewidth=1, linestyle="solid",\
             bottom=None, cumulative=False, normed=False, align="mid", orientation="vertical")

    pad.hist(x=xData, bins=xBinning, weights=y7_DELTAR_0_weights+y7_DELTAR_1_weights+y7_DELTAR_2_weights+y7_DELTAR_3_weights+y7_DELTAR_4_weights+y7_DELTAR_5_weights+y7_DELTAR_6_weights+y7_DELTAR_7_weights+y7_DELTAR_8_weights+y7_DELTAR_9_weights+y7_DELTAR_10_weights+y7_DELTAR_11_weights+y7_DELTAR_12_weights,\
             label="$bg\_dip\_400\_600$", histtype="step", rwidth=1.0,\
             color=None, edgecolor="#c1bfa8", linewidth=1, linestyle="solid",\
             bottom=None, cumulative=False, normed=False, align="mid", orientation="vertical")

    pad.hist(x=xData, bins=xBinning, weights=y7_DELTAR_0_weights+y7_DELTAR_1_weights+y7_DELTAR_2_weights+y7_DELTAR_3_weights+y7_DELTAR_4_weights+y7_DELTAR_5_weights+y7_DELTAR_6_weights+y7_DELTAR_7_weights+y7_DELTAR_8_weights+y7_DELTAR_9_weights+y7_DELTAR_10_weights+y7_DELTAR_11_weights,\
             label="$bg\_dip\_200\_400$", histtype="step", rwidth=1.0,\
             color=None, edgecolor="#bab5a3", linewidth=1, linestyle="solid",\
             bottom=None, cumulative=False, normed=False, align="mid", orientation="vertical")

    pad.hist(x=xData, bins=xBinning, weights=y7_DELTAR_0_weights+y7_DELTAR_1_weights+y7_DELTAR_2_weights+y7_DELTAR_3_weights+y7_DELTAR_4_weights+y7_DELTAR_5_weights+y7_DELTAR_6_weights+y7_DELTAR_7_weights+y7_DELTAR_8_weights+y7_DELTAR_9_weights+y7_DELTAR_10_weights,\
             label="$bg\_dip\_100\_200$", histtype="step", rwidth=1.0,\
             color=None, edgecolor="#b2a596", linewidth=1, linestyle="solid",\
             bottom=None, cumulative=False, normed=False, align="mid", orientation="vertical")

    pad.hist(x=xData, bins=xBinning, weights=y7_DELTAR_0_weights+y7_DELTAR_1_weights+y7_DELTAR_2_weights+y7_DELTAR_3_weights+y7_DELTAR_4_weights+y7_DELTAR_5_weights+y7_DELTAR_6_weights+y7_DELTAR_7_weights+y7_DELTAR_8_weights+y7_DELTAR_9_weights,\
             label="$bg\_dip\_0\_100$", histtype="step", rwidth=1.0,\
             color=None, edgecolor="#b7a39b", linewidth=1, linestyle="solid",\
             bottom=None, cumulative=False, normed=False, align="mid", orientation="vertical")

    pad.hist(x=xData, bins=xBinning, weights=y7_DELTAR_0_weights+y7_DELTAR_1_weights+y7_DELTAR_2_weights+y7_DELTAR_3_weights+y7_DELTAR_4_weights+y7_DELTAR_5_weights+y7_DELTAR_6_weights+y7_DELTAR_7_weights+y7_DELTAR_8_weights,\
             label="$bg\_vbf\_1600\_inf$", histtype="step", rwidth=1.0,\
             color=None, edgecolor="#ad998c", linewidth=1, linestyle="solid",\
             bottom=None, cumulative=False, normed=False, align="mid", orientation="vertical")

    pad.hist(x=xData, bins=xBinning, weights=y7_DELTAR_0_weights+y7_DELTAR_1_weights+y7_DELTAR_2_weights+y7_DELTAR_3_weights+y7_DELTAR_4_weights+y7_DELTAR_5_weights+y7_DELTAR_6_weights+y7_DELTAR_7_weights,\
             label="$bg\_vbf\_1200\_1600$", histtype="step", rwidth=1.0,\
             color=None, edgecolor="#9b8e82", linewidth=1, linestyle="solid",\
             bottom=None, cumulative=False, normed=False, align="mid", orientation="vertical")

    pad.hist(x=xData, bins=xBinning, weights=y7_DELTAR_0_weights+y7_DELTAR_1_weights+y7_DELTAR_2_weights+y7_DELTAR_3_weights+y7_DELTAR_4_weights+y7_DELTAR_5_weights+y7_DELTAR_6_weights,\
             label="$bg\_vbf\_800\_1200$", histtype="step", rwidth=1.0,\
             color=None, edgecolor="#876656", linewidth=1, linestyle="solid",\
             bottom=None, cumulative=False, normed=False, align="mid", orientation="vertical")

    pad.hist(x=xData, bins=xBinning, weights=y7_DELTAR_0_weights+y7_DELTAR_1_weights+y7_DELTAR_2_weights+y7_DELTAR_3_weights+y7_DELTAR_4_weights+y7_DELTAR_5_weights,\
             label="$bg\_vbf\_600\_800$", histtype="step", rwidth=1.0,\
             color=None, edgecolor="#afcec6", linewidth=1, linestyle="solid",\
             bottom=None, cumulative=False, normed=False, align="mid", orientation="vertical")

    pad.hist(x=xData, bins=xBinning, weights=y7_DELTAR_0_weights+y7_DELTAR_1_weights+y7_DELTAR_2_weights+y7_DELTAR_3_weights+y7_DELTAR_4_weights,\
             label="$bg\_vbf\_400\_600$", histtype="step", rwidth=1.0,\
             color=None, edgecolor="#84c1a3", linewidth=1, linestyle="solid",\
             bottom=None, cumulative=False, normed=False, align="mid", orientation="vertical")

    pad.hist(x=xData, bins=xBinning, weights=y7_DELTAR_0_weights+y7_DELTAR_1_weights+y7_DELTAR_2_weights+y7_DELTAR_3_weights,\
             label="$bg\_vbf\_200\_400$", histtype="step", rwidth=1.0,\
             color=None, edgecolor="#89a8a0", linewidth=1, linestyle="solid",\
             bottom=None, cumulative=False, normed=False, align="mid", orientation="vertical")

    pad.hist(x=xData, bins=xBinning, weights=y7_DELTAR_0_weights+y7_DELTAR_1_weights+y7_DELTAR_2_weights,\
             label="$bg\_vbf\_100\_200$", histtype="step", rwidth=1.0,\
             color=None, edgecolor="#829e8c", linewidth=1, linestyle="solid",\
             bottom=None, cumulative=False, normed=False, align="mid", orientation="vertical")

    pad.hist(x=xData, bins=xBinning, weights=y7_DELTAR_0_weights+y7_DELTAR_1_weights,\
             label="$bg\_vbf\_0\_100$", histtype="step", rwidth=1.0,\
             color=None, edgecolor="#adbcc6", linewidth=1, linestyle="solid",\
             bottom=None, cumulative=False, normed=False, align="mid", orientation="vertical")

    pad.hist(x=xData, bins=xBinning, weights=y7_DELTAR_0_weights,\
             label="$signal$", histtype="step", rwidth=1.0,\
             color=None, edgecolor="#7a8e99", linewidth=1, linestyle="solid",\
             bottom=None, cumulative=False, normed=False, align="mid", orientation="vertical")


    # Axis
    plt.rc('text',usetex=False)
    plt.xlabel(r"\Delta R [ j_{1} , j_{2} ] ",\
               fontsize=16,color="black")
    plt.ylabel(r"$\mathrm{Events}$ $(\mathcal{L}_{\mathrm{int}} = 1000.0\ \mathrm{fb}^{-1})$ ",\
               fontsize=16,color="black")

    # Boundary of y-axis
    ymax=(y7_DELTAR_0_weights+y7_DELTAR_1_weights+y7_DELTAR_2_weights+y7_DELTAR_3_weights+y7_DELTAR_4_weights+y7_DELTAR_5_weights+y7_DELTAR_6_weights+y7_DELTAR_7_weights+y7_DELTAR_8_weights+y7_DELTAR_9_weights+y7_DELTAR_10_weights+y7_DELTAR_11_weights+y7_DELTAR_12_weights+y7_DELTAR_13_weights+y7_DELTAR_14_weights+y7_DELTAR_15_weights+y7_DELTAR_16_weights).max()*1.1
    ymin=0 # linear scale
    #ymin=min([x for x in (y7_DELTAR_0_weights+y7_DELTAR_1_weights+y7_DELTAR_2_weights+y7_DELTAR_3_weights+y7_DELTAR_4_weights+y7_DELTAR_5_weights+y7_DELTAR_6_weights+y7_DELTAR_7_weights+y7_DELTAR_8_weights+y7_DELTAR_9_weights+y7_DELTAR_10_weights+y7_DELTAR_11_weights+y7_DELTAR_12_weights+y7_DELTAR_13_weights+y7_DELTAR_14_weights+y7_DELTAR_15_weights+y7_DELTAR_16_weights) if x])/100. # log scale
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
    plt.savefig('../../HTML/MadAnalysis5job_0/selection_6.png')
    plt.savefig('../../PDF/MadAnalysis5job_0/selection_6.png')
    plt.savefig('../../DVI/MadAnalysis5job_0/selection_6.eps')

# Running!
if __name__ == '__main__':
    selection_6()
