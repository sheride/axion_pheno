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
    y7_DELTAR_0_weights = numpy.array([0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,1293.93525193,2424.10784917,3133.40721983,3574.34082861,3753.86466932,3865.22457052,3428.38495811,2826.35149227,2317.25194398,1969.66365238,1654.41933209,1395.46856185,1166.81396473,997.932914568,843.790651333,726.290555587,599.783267832,499.887556467,427.831820399,326.707910123,278.192953169,210.435813287,167.243331611,135.104760126,100.509750821,75.3311331612,55.6795305974,42.9878818583,28.6585945722,15.5575181963,10.0305051003,4.09408436746,0.409408436746,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0])

    # Creating weights for histo: y7_DELTAR_1
    y7_DELTAR_1_weights = numpy.array([0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,1.21533599884,0.0,0.0,1.21472880116,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0])

    # Creating weights for histo: y7_DELTAR_2
    y7_DELTAR_2_weights = numpy.array([0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,1.50617736722,1.50600650751,3.01000897722,3.5145017315,8.53239335828,3.51493352933,5.52597512093,3.51299767015,4.01397819325,4.51879944444,5.5206096713,4.51990269823,0.502286659894,3.01102545825,3.51381994545,0.501848664006,0.501704662528,1.00551996939,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0])

    # Creating weights for histo: y7_DELTAR_3
    y7_DELTAR_3_weights = numpy.array([0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,5.77573392661,6.87342205336,16.224778719,20.0716008501,25.2956794097,29.4312614241,27.2203051859,25.3063030499,29.7123308483,20.3555648607,19.5274835957,15.6741288399,14.2953875394,12.6541915448,13.7508213701,6.04781083543,5.22699142767,3.02500536057,3.30018404732,1.92477020086,0.275710884399,0.275438894836,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0])

    # Creating weights for histo: y7_DELTAR_4
    y7_DELTAR_4_weights = numpy.array([0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,4.34195327607,9.96675752242,15.3959973363,19.3893196341,24.7702455335,24.8172627664,26.1024405486,22.1545562177,20.5772543149,14.3582712909,11.7935994807,7.79624283972,7.30397682036,5.0826109761,3.25603156077,1.92443037373,1.43116268289,0.690870138013,0.493457483337,0.0986455817141,0.0987037019082,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0])

    # Creating weights for histo: y7_DELTAR_5
    y7_DELTAR_5_weights = numpy.array([0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,1.81508226008,3.73048666768,6.36518188768,8.19223250574,10.3599507054,11.1412459144,11.3693659184,8.96207650191,6.56609225738,4.82701832305,3.10051191482,2.45812968077,1.37394989098,0.831767370095,0.516847412577,0.176455928478,0.100785317473,0.0378331348938,0.0378259528787,0.0,0.0252177153685,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0])

    # Creating weights for histo: y7_DELTAR_6
    y7_DELTAR_6_weights = numpy.array([0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.572559771359,1.65995602221,2.3764441332,3.59342437569,4.2951137702,5.33996933454,4.58131592838,3.29262494272,2.17473101949,1.47402284096,0.816713600515,0.543655637722,0.257883005217,0.042950332935,0.0429433049692,0.0714908568197,0.0142584378649,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0])

    # Creating weights for histo: y7_DELTAR_7
    y7_DELTAR_7_weights = numpy.array([0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0647961861273,0.147952610411,0.193282460609,0.305578657202,0.424013785493,0.583024691423,0.479396625902,0.254904564176,0.133930953545,0.0756267451562,0.0485254952214,0.0151175831918,0.0086420696194,0.0064791471303,0.00323867774854,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0])

    # Creating weights for histo: y7_DELTAR_8
    y7_DELTAR_8_weights = numpy.array([0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.00849828383461,0.0155886098464,0.029792603725,0.0381932066482,0.0467366373721,0.0666947251586,0.0311773607537,0.0255710614723,0.0155505679683,0.0056808083532,0.00142146328347,0.00425168992132,0.0,0.00142244551229,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0])

    # Creating weights for histo: y7_DELTAR_9
    y7_DELTAR_9_weights = numpy.array([0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0])

    # Creating weights for histo: y7_DELTAR_10
    y7_DELTAR_10_weights = numpy.array([0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,52.64790836,0.0,0.0,0.0,52.6056914349,0.0,52.7314194359,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0])

    # Creating weights for histo: y7_DELTAR_11
    y7_DELTAR_11_weights = numpy.array([0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,23.0270111539,23.0508358903,69.0819172826,138.268355989,69.1183268595,207.216604973,126.647571851,34.5394119548,80.5798695337,69.1604428451,34.5482693769,34.5392006063,11.5232660335,0.0,23.0729121984,0.0,11.5180092207,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0])

    # Creating weights for histo: y7_DELTAR_12
    y7_DELTAR_12_weights = numpy.array([0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,26.2894361051,41.5467247486,67.8424887658,76.1424399396,92.7458620679,80.3151498492,62.3277613993,55.390100082,42.9344993576,27.6843464449,15.2239276597,6.92159726796,9.68908753407,4.15234326463,2.76484177521,1.3858956615,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0])

    # Creating weights for histo: y7_DELTAR_13
    y7_DELTAR_13_weights = numpy.array([0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,10.076269829,11.5983978714,19.6639083332,22.6931712963,20.6676494243,32.2562703602,20.6699161439,15.6284403213,10.0800264541,7.05476590491,1.51361373355,3.02311854462,2.52145980234,1.50858416483,1.00771042974,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0])

    # Creating weights for histo: y7_DELTAR_14
    y7_DELTAR_14_weights = numpy.array([0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,2.97252069744,4.66676623358,7.78204445787,6.93114542243,14.1451665512,13.2968972445,10.4684691374,5.2336507189,4.52606324241,0.98941321509,0.848815451544,0.565675810441,0.566425869864,0.141173976162,0.282622929225,0.0,0.0,0.141599041897,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0])

    # Creating weights for histo: y7_DELTAR_15
    y7_DELTAR_15_weights = numpy.array([0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.68440701144,0.987961107655,0.838143048768,0.379949239111,0.838950282335,0.686002568271,0.458427588281,0.229255101334,0.0761303395559,0.0759409410505,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0])

    # Creating weights for histo: y7_DELTAR_16
    y7_DELTAR_16_weights = numpy.array([0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0270870556527,0.0542092218775,0.0812374711719,0.0541293568756,0.0812566241429,0.0902906474903,0.0632192414511,0.00903775192073,0.018047459657,0.0,0.00900018129868,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0])

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
    plt.ylabel(r"$\mathrm{Events}$ $(\mathcal{L}_{\mathrm{int}} = 2000.0\ \mathrm{fb}^{-1})$ ",\
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
