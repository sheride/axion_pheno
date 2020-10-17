def selection_12():

    # Library import
    import numpy
    import matplotlib
    import matplotlib.pyplot   as plt
    import matplotlib.gridspec as gridspec

    # Library version
    matplotlib_version = matplotlib.__version__
    numpy_version      = numpy.__version__

    # Histo binning
    xBinning = numpy.linspace(0.0,4000.0,81,endpoint=True)

    # Creating data sequence: middle of each bin
    xData = numpy.array([25.0,75.0,125.0,175.0,225.0,275.0,325.0,375.0,425.0,475.0,525.0,575.0,625.0,675.0,725.0,775.0,825.0,875.0,925.0,975.0,1025.0,1075.0,1125.0,1175.0,1225.0,1275.0,1325.0,1375.0,1425.0,1475.0,1525.0,1575.0,1625.0,1675.0,1725.0,1775.0,1825.0,1875.0,1925.0,1975.0,2025.0,2075.0,2125.0,2175.0,2225.0,2275.0,2325.0,2375.0,2425.0,2475.0,2525.0,2575.0,2625.0,2675.0,2725.0,2775.0,2825.0,2875.0,2925.0,2975.0,3025.0,3075.0,3125.0,3175.0,3225.0,3275.0,3325.0,3375.0,3425.0,3475.0,3525.0,3575.0,3625.0,3675.0,3725.0,3775.0,3825.0,3875.0,3925.0,3975.0])

    # Creating weights for histo: y13_THT_0
    y13_THT_0_weights = numpy.array([6.54953692064,120.438720041,174.148522755,207.253003922,228.599358333,239.035097825,244.156728498,240.963399253,234.834578281,224.026322376,213.156627063,203.163043313,187.576993424,175.937625524,161.162207828,145.649837229,132.417884668,121.089673771,108.054199317,95.3053621029,85.7662139755,75.6293516048,65.132212704,58.4097974484,51.4744642434,43.5975001074,38.5945922909,32.9243349019,27.8559037165,24.5110639311,20.867363024,17.5184312779,14.6648787608,12.7939007804,10.5994899151,9.13382003111,7.06223198281,6.46450173962,5.08071506704,4.39700565192,3.33255510377,2.65703720976,2.2599146345,1.80547501126,1.55164425593,1.28143685833,0.994853618448,0.798339511098,0.671423933437,0.515850231786,0.397122655265,0.352088128998,0.331617886149,0.245642874185,0.200608347917,0.147385740511,0.15147978108,0.0818809713947,0.0614107285461,0.0327523845579,0.0532226074068,0.0286583359882,0.0286583359882,0.016376190279,0.0122821457092,0.00818809713947,0.00409404856974,0.016376190279,0.00409404856974,0.00409404856974,0.0122821457092,0.0,0.00818809713947,0.00818809713947,0.0,0.00818809713947,0.0,0.00409404856974,0.0,0.0])

    # Creating weights for histo: y13_THT_1
    y13_THT_1_weights = numpy.array([0.697387035698,4.72642051311,6.20752461298,6.38498029653,6.16057058443,5.74834873525,5.0758076429,4.48336600295,3.97447278487,3.4117216336,3.02090312171,2.61903653292,2.27033824251,2.03833260469,1.6827292165,1.51148740507,1.26636239963,1.12066889318,0.952879232922,0.889353685585,0.715349755498,0.620062031063,0.535131555582,0.479891966493,0.41153340751,0.375627694489,0.303126037067,0.241672257691,0.21681454203,0.191266316591,0.161575151799,0.148455823961,0.116002659829,0.107026271345,0.083549535468,0.0773351065527,0.0545488804536,0.0621442891533,0.0469534717539,0.0414295128451,0.0365960835998,0.0262386994228,0.0207147643768,0.0179527968538,0.015881319223,0.0207147643768,0.0110478740692,0.0103573801998,0.00690492278465,0.0103573801998,0.00138098415922,0.00414295128451,0.0034524605969,0.00552393504601,0.00414295128451,0.00138098415922,0.00483344515383,0.00207147643768,0.00207147643768,0.00207147643768,0.000690492278465,0.00138098415922,0.00207147643768,0.0,0.000690492278465,0.0,0.0,0.000690492278465,0.0,0.0,0.0,0.000690492278465,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0])

    # Creating weights for histo: y13_THT_2
    y13_THT_2_weights = numpy.array([762.224986398,11388.0990136,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0])

    # Creating weights for histo: y13_THT_3
    y13_THT_3_weights = numpy.array([0.0413209188098,0.0,5966.60018501,3728.68649408,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0])

    # Creating weights for histo: y13_THT_4
    y13_THT_4_weights = numpy.array([0.040625382744,0.0,0.0,0.0,2394.5201845,1484.33448436,938.179026369,596.189679384,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0])

    # Creating weights for histo: y13_THT_5
    y13_THT_5_weights = numpy.array([0.0400816441714,0.0,0.0,0.0,0.0,0.0,0.0,0.0,399.620966595,269.790067979,186.469588606,130.928895176,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0])

    # Creating weights for histo: y13_THT_6
    y13_THT_6_weights = numpy.array([0.0400035834499,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,94.084707941,68.9234540406,50.9544444086,38.0741786173,0.000251409040775,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0])

    # Creating weights for histo: y13_THT_7
    y13_THT_7_weights = numpy.array([0.0998797074312,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,29.0799668306,22.5413118197,17.468181768,13.5966944884,10.8827730661,8.60671329431,6.92465312462,5.56230590083,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0])

    # Creating weights for histo: y13_THT_8
    y13_THT_8_weights = numpy.array([0.0418244418569,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,4.5220042818,3.75777511461,3.08472741312,2.5587674905,2.13211384965,1.77385739155,1.47700130531,1.24769671161,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0])

    # Creating weights for histo: y13_THT_9
    y13_THT_9_weights = numpy.array([0.145672549671,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,1.02522708926,0.87865544861,0.759714103149,0.636935305712,0.542874249045,0.475097473204,0.407101314504,0.354350662163,0.303330017021,0.264764520548,0.229441112341,0.195054961319,0.174642886642,0.150929726316,0.130602782676,0.110517538931,0.103130906388,0.0887382691061,0.0797342779455,0.0699265676265,0.0590146739483,0.055417450574,0.0459096509003,0.0411335869851,0.0361899413687,0.0327406047668,0.0280720034914,0.0268169179379,0.0225452889277,0.0212747912184,0.0168746061831,0.0162481559505,0.0143829252929,0.01298456496,0.01106405594,0.00937237518788,0.00887016907289,0.00770090941553,0.00801136675338,0.0068440430842,0.0057261213468,0.00495120019484,0.00428293611358,0.00314476589176,0.00322353103937,0.00324874404427,0.00297262463982,0.00211598264422])

    # Creating weights for histo: y13_THT_10
    y13_THT_10_weights = numpy.array([345747.075949,2365100.12405,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0])

    # Creating weights for histo: y13_THT_11
    y13_THT_11_weights = numpy.array([0.0384761291489,0.0,807538.152861,287824.608663,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0])

    # Creating weights for histo: y13_THT_12
    y13_THT_12_weights = numpy.array([0.0384230895223,0.0,0.0,0.0,124179.698296,62114.2670216,33752.3557061,19502.4805527,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0])

    # Creating weights for histo: y13_THT_13
    y13_THT_13_weights = numpy.array([0.0384714660756,0.0,0.0,0.0,0.0,0.0,0.0,0.0,12093.6861767,7850.21037283,5247.24636674,3607.49861222,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0])

    # Creating weights for histo: y13_THT_14
    y13_THT_14_weights = numpy.array([0.060682614405,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,2515.6614969,1824.11999584,1335.40709929,999.110725349,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0])

    # Creating weights for histo: y13_THT_15
    y13_THT_15_weights = numpy.array([0.0384736738888,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,746.363880819,578.362427995,448.915443776,350.861861713,276.833357679,221.60270597,175.933724064,143.426124311,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0])

    # Creating weights for histo: y13_THT_16
    y13_THT_16_weights = numpy.array([0.118137481956,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,113.635676,93.1559291879,77.0600398701,63.9634249442,53.2347222653,44.4524999942,37.1071012199,30.7769405242,0.00152851235929,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0])

    # Creating weights for histo: y13_THT_17
    y13_THT_17_weights = numpy.array([0.0385048379488,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,25.7937209577,22.1254882618,18.9622503661,16.0703060071,13.7879779435,11.8401760615,10.1848492276,8.7713635799,7.55176134271,6.63282413264,5.6643157942,4.9351650799,4.27718670806,3.77743010603,3.27304868792,2.85591153163,2.47517145846,2.23252898659,1.92585797485,1.64786998699,1.51677025493,1.31257024318,1.15060926855,1.02449552796,0.9055282853,0.792850422865,0.72066116763,0.618112002818,0.555471947394,0.488486621008,0.428759071527,0.374414113343,0.334168856719,0.289930763914,0.266646811397,0.235403523827,0.206320588696,0.192989097157,0.164460901226,0.149478129712,0.136308512513,0.12367911819,0.110472343822,0.102002896676,0.0893662634437,0.0722096627989,0.0673252085906,0.058121782224])

    # Creating a new Canvas
    fig   = plt.figure(figsize=(12,6),dpi=80)
    frame = gridspec.GridSpec(1,1,right=0.7)
    pad   = fig.add_subplot(frame[0])

    # Creating a new Stack
    pad.hist(x=xData, bins=xBinning, weights=y13_THT_0_weights+y13_THT_1_weights+y13_THT_2_weights+y13_THT_3_weights+y13_THT_4_weights+y13_THT_5_weights+y13_THT_6_weights+y13_THT_7_weights+y13_THT_8_weights+y13_THT_9_weights+y13_THT_10_weights+y13_THT_11_weights+y13_THT_12_weights+y13_THT_13_weights+y13_THT_14_weights+y13_THT_15_weights+y13_THT_16_weights+y13_THT_17_weights,\
             label="$bg\_dip\_1600\_inf$", histtype="step", rwidth=1.0,\
             color=None, edgecolor="#f2f2f2", linewidth=1, linestyle="solid",\
             bottom=None, cumulative=False, normed=False, align="mid", orientation="vertical")

    pad.hist(x=xData, bins=xBinning, weights=y13_THT_0_weights+y13_THT_1_weights+y13_THT_2_weights+y13_THT_3_weights+y13_THT_4_weights+y13_THT_5_weights+y13_THT_6_weights+y13_THT_7_weights+y13_THT_8_weights+y13_THT_9_weights+y13_THT_10_weights+y13_THT_11_weights+y13_THT_12_weights+y13_THT_13_weights+y13_THT_14_weights+y13_THT_15_weights+y13_THT_16_weights,\
             label="$bg\_dip\_1200\_1600$", histtype="step", rwidth=1.0,\
             color=None, edgecolor="#ccc6aa", linewidth=1, linestyle="solid",\
             bottom=None, cumulative=False, normed=False, align="mid", orientation="vertical")

    pad.hist(x=xData, bins=xBinning, weights=y13_THT_0_weights+y13_THT_1_weights+y13_THT_2_weights+y13_THT_3_weights+y13_THT_4_weights+y13_THT_5_weights+y13_THT_6_weights+y13_THT_7_weights+y13_THT_8_weights+y13_THT_9_weights+y13_THT_10_weights+y13_THT_11_weights+y13_THT_12_weights+y13_THT_13_weights+y13_THT_14_weights+y13_THT_15_weights,\
             label="$bg\_dip\_800\_1200$", histtype="step", rwidth=1.0,\
             color=None, edgecolor="#ccc6aa", linewidth=1, linestyle="solid",\
             bottom=None, cumulative=False, normed=False, align="mid", orientation="vertical")

    pad.hist(x=xData, bins=xBinning, weights=y13_THT_0_weights+y13_THT_1_weights+y13_THT_2_weights+y13_THT_3_weights+y13_THT_4_weights+y13_THT_5_weights+y13_THT_6_weights+y13_THT_7_weights+y13_THT_8_weights+y13_THT_9_weights+y13_THT_10_weights+y13_THT_11_weights+y13_THT_12_weights+y13_THT_13_weights+y13_THT_14_weights,\
             label="$bg\_dip\_600\_800$", histtype="step", rwidth=1.0,\
             color=None, edgecolor="#c1bfa8", linewidth=1, linestyle="solid",\
             bottom=None, cumulative=False, normed=False, align="mid", orientation="vertical")

    pad.hist(x=xData, bins=xBinning, weights=y13_THT_0_weights+y13_THT_1_weights+y13_THT_2_weights+y13_THT_3_weights+y13_THT_4_weights+y13_THT_5_weights+y13_THT_6_weights+y13_THT_7_weights+y13_THT_8_weights+y13_THT_9_weights+y13_THT_10_weights+y13_THT_11_weights+y13_THT_12_weights+y13_THT_13_weights,\
             label="$bg\_dip\_400\_600$", histtype="step", rwidth=1.0,\
             color=None, edgecolor="#bab5a3", linewidth=1, linestyle="solid",\
             bottom=None, cumulative=False, normed=False, align="mid", orientation="vertical")

    pad.hist(x=xData, bins=xBinning, weights=y13_THT_0_weights+y13_THT_1_weights+y13_THT_2_weights+y13_THT_3_weights+y13_THT_4_weights+y13_THT_5_weights+y13_THT_6_weights+y13_THT_7_weights+y13_THT_8_weights+y13_THT_9_weights+y13_THT_10_weights+y13_THT_11_weights+y13_THT_12_weights,\
             label="$bg\_dip\_200\_400$", histtype="step", rwidth=1.0,\
             color=None, edgecolor="#b2a596", linewidth=1, linestyle="solid",\
             bottom=None, cumulative=False, normed=False, align="mid", orientation="vertical")

    pad.hist(x=xData, bins=xBinning, weights=y13_THT_0_weights+y13_THT_1_weights+y13_THT_2_weights+y13_THT_3_weights+y13_THT_4_weights+y13_THT_5_weights+y13_THT_6_weights+y13_THT_7_weights+y13_THT_8_weights+y13_THT_9_weights+y13_THT_10_weights+y13_THT_11_weights,\
             label="$bg\_dip\_100\_200$", histtype="step", rwidth=1.0,\
             color=None, edgecolor="#b7a39b", linewidth=1, linestyle="solid",\
             bottom=None, cumulative=False, normed=False, align="mid", orientation="vertical")

    pad.hist(x=xData, bins=xBinning, weights=y13_THT_0_weights+y13_THT_1_weights+y13_THT_2_weights+y13_THT_3_weights+y13_THT_4_weights+y13_THT_5_weights+y13_THT_6_weights+y13_THT_7_weights+y13_THT_8_weights+y13_THT_9_weights+y13_THT_10_weights,\
             label="$bg\_dip\_0\_100$", histtype="step", rwidth=1.0,\
             color=None, edgecolor="#ad998c", linewidth=1, linestyle="solid",\
             bottom=None, cumulative=False, normed=False, align="mid", orientation="vertical")

    pad.hist(x=xData, bins=xBinning, weights=y13_THT_0_weights+y13_THT_1_weights+y13_THT_2_weights+y13_THT_3_weights+y13_THT_4_weights+y13_THT_5_weights+y13_THT_6_weights+y13_THT_7_weights+y13_THT_8_weights+y13_THT_9_weights,\
             label="$bg\_vbf\_1600\_inf$", histtype="step", rwidth=1.0,\
             color=None, edgecolor="#9b8e82", linewidth=1, linestyle="solid",\
             bottom=None, cumulative=False, normed=False, align="mid", orientation="vertical")

    pad.hist(x=xData, bins=xBinning, weights=y13_THT_0_weights+y13_THT_1_weights+y13_THT_2_weights+y13_THT_3_weights+y13_THT_4_weights+y13_THT_5_weights+y13_THT_6_weights+y13_THT_7_weights+y13_THT_8_weights,\
             label="$bg\_vbf\_1200\_1600$", histtype="step", rwidth=1.0,\
             color=None, edgecolor="#876656", linewidth=1, linestyle="solid",\
             bottom=None, cumulative=False, normed=False, align="mid", orientation="vertical")

    pad.hist(x=xData, bins=xBinning, weights=y13_THT_0_weights+y13_THT_1_weights+y13_THT_2_weights+y13_THT_3_weights+y13_THT_4_weights+y13_THT_5_weights+y13_THT_6_weights+y13_THT_7_weights,\
             label="$bg\_vbf\_800\_1200$", histtype="step", rwidth=1.0,\
             color=None, edgecolor="#afcec6", linewidth=1, linestyle="solid",\
             bottom=None, cumulative=False, normed=False, align="mid", orientation="vertical")

    pad.hist(x=xData, bins=xBinning, weights=y13_THT_0_weights+y13_THT_1_weights+y13_THT_2_weights+y13_THT_3_weights+y13_THT_4_weights+y13_THT_5_weights+y13_THT_6_weights,\
             label="$bg\_vbf\_600\_800$", histtype="step", rwidth=1.0,\
             color=None, edgecolor="#84c1a3", linewidth=1, linestyle="solid",\
             bottom=None, cumulative=False, normed=False, align="mid", orientation="vertical")

    pad.hist(x=xData, bins=xBinning, weights=y13_THT_0_weights+y13_THT_1_weights+y13_THT_2_weights+y13_THT_3_weights+y13_THT_4_weights+y13_THT_5_weights,\
             label="$bg\_vbf\_400\_600$", histtype="step", rwidth=1.0,\
             color=None, edgecolor="#89a8a0", linewidth=1, linestyle="solid",\
             bottom=None, cumulative=False, normed=False, align="mid", orientation="vertical")

    pad.hist(x=xData, bins=xBinning, weights=y13_THT_0_weights+y13_THT_1_weights+y13_THT_2_weights+y13_THT_3_weights+y13_THT_4_weights,\
             label="$bg\_vbf\_200\_400$", histtype="step", rwidth=1.0,\
             color=None, edgecolor="#829e8c", linewidth=1, linestyle="solid",\
             bottom=None, cumulative=False, normed=False, align="mid", orientation="vertical")

    pad.hist(x=xData, bins=xBinning, weights=y13_THT_0_weights+y13_THT_1_weights+y13_THT_2_weights+y13_THT_3_weights,\
             label="$bg\_vbf\_100\_200$", histtype="step", rwidth=1.0,\
             color=None, edgecolor="#adbcc6", linewidth=1, linestyle="solid",\
             bottom=None, cumulative=False, normed=False, align="mid", orientation="vertical")

    pad.hist(x=xData, bins=xBinning, weights=y13_THT_0_weights+y13_THT_1_weights+y13_THT_2_weights,\
             label="$bg\_vbf\_0\_100$", histtype="step", rwidth=1.0,\
             color=None, edgecolor="#7a8e99", linewidth=1, linestyle="solid",\
             bottom=None, cumulative=False, normed=False, align="mid", orientation="vertical")

    pad.hist(x=xData, bins=xBinning, weights=y13_THT_0_weights+y13_THT_1_weights,\
             label="$signal2$", histtype="step", rwidth=1.0,\
             color=None, edgecolor="#758991", linewidth=1, linestyle="solid",\
             bottom=None, cumulative=False, normed=False, align="mid", orientation="vertical")

    pad.hist(x=xData, bins=xBinning, weights=y13_THT_0_weights,\
             label="$signal1$", histtype="step", rwidth=1.0,\
             color=None, edgecolor="#688296", linewidth=1, linestyle="solid",\
             bottom=None, cumulative=False, normed=False, align="mid", orientation="vertical")


    # Axis
    plt.rc('text',usetex=False)
    plt.xlabel(r"THT",\
               fontsize=16,color="black")
    plt.ylabel(r"$\mathrm{Events}$ $(\mathcal{L}_{\mathrm{int}} = 40.0\ \mathrm{fb}^{-1})$ ",\
               fontsize=16,color="black")

    # Boundary of y-axis
    ymax=(y13_THT_0_weights+y13_THT_1_weights+y13_THT_2_weights+y13_THT_3_weights+y13_THT_4_weights+y13_THT_5_weights+y13_THT_6_weights+y13_THT_7_weights+y13_THT_8_weights+y13_THT_9_weights+y13_THT_10_weights+y13_THT_11_weights+y13_THT_12_weights+y13_THT_13_weights+y13_THT_14_weights+y13_THT_15_weights+y13_THT_16_weights+y13_THT_17_weights).max()*1.1
    ymin=0 # linear scale
    #ymin=min([x for x in (y13_THT_0_weights+y13_THT_1_weights+y13_THT_2_weights+y13_THT_3_weights+y13_THT_4_weights+y13_THT_5_weights+y13_THT_6_weights+y13_THT_7_weights+y13_THT_8_weights+y13_THT_9_weights+y13_THT_10_weights+y13_THT_11_weights+y13_THT_12_weights+y13_THT_13_weights+y13_THT_14_weights+y13_THT_15_weights+y13_THT_16_weights+y13_THT_17_weights) if x])/100. # log scale
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
    plt.savefig('../../HTML/MadAnalysis5job_0/selection_12.png')
    plt.savefig('../../PDF/MadAnalysis5job_0/selection_12.png')
    plt.savefig('../../DVI/MadAnalysis5job_0/selection_12.eps')

# Running!
if __name__ == '__main__':
    selection_12()
