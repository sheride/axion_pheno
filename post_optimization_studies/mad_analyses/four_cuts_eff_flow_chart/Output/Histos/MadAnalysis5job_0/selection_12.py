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
    y13_THT_0_weights = numpy.array([1.28554254805,27.2338457148,40.2694070479,50.9917982739,60.4245905551,66.6435054662,65.2228666287,61.3825897712,55.6590744547,49.6243993928,43.4546044415,39.1967599257,32.5970973261,29.4282759191,24.1428122442,20.2452474335,17.0805180232,14.5544680902,12.0284181573,9.96909584238,8.14313333655,6.82074241865,5.3632516113,4.68363216743,3.73789894131,3.13197423713,2.50557954971,1.96516039193,1.66629223649,1.4697763973,1.09312030551,0.884322076367,0.716464613724,0.622300690777,0.474913611383,0.388938001736,0.323432655338,0.315244462038,0.212892385792,0.237456885691,0.167857462644,0.102352116246,0.0982579995964,0.0941639229465,0.0655053463976,0.0450349231483,0.0368467578486,0.0614112697477,0.0122822539495,0.0163763345994,0.0,0.0163763345994,0.0163763345994,0.0122822539495,0.0081881692997,0.00409408464985,0.0122822539495,0.0081881692997,0.0,0.00409408464985,0.0081881692997,0.0,0.0,0.00409408464985,0.0,0.0,0.00409408464985,0.00409408464985,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0])

    # Creating weights for histo: y13_THT_1
    y13_THT_1_weights = numpy.array([0.0,0.048601296,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0])

    # Creating weights for histo: y13_THT_2
    y13_THT_2_weights = numpy.array([0.0,0.0,0.341401305308,0.82324848727,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0])

    # Creating weights for histo: y13_THT_3
    y13_THT_3_weights = numpy.array([0.0,0.0,0.0,0.0,1.21010202833,1.62812376457,1.59530829634,1.61136400813,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0])

    # Creating weights for histo: y13_THT_4
    y13_THT_4_weights = numpy.array([0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,1.49309971083,1.19804434015,1.02828888808,0.717442862533,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0])

    # Creating weights for histo: y13_THT_5
    y13_THT_5_weights = numpy.array([0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.60297403431,0.445927156591,0.341043119208,0.249816835092,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0])

    # Creating weights for histo: y13_THT_6
    y13_THT_6_weights = numpy.array([0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.172666925432,0.130238205473,0.0947609835593,0.0735919704552,0.0586845150837,0.0398036397295,0.0320845638428,0.0211703427193,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0])

    # Creating weights for histo: y13_THT_7
    y13_THT_7_weights = numpy.array([0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0158503549171,0.0118519408575,0.00881390087939,0.00645611155653,0.00431790312524,0.0031531009688,0.00287133846014,0.00157555429442,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0])

    # Creating weights for histo: y13_THT_8
    y13_THT_8_weights = numpy.array([0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.00144692825635,0.000880142015735,0.000851081704725,0.000596401291866,0.000480543584776,0.000340900647453,0.000312327515974,0.00019621545395,0.000225241761878,2.81995281811e-05,0.000113534717485,2.81995281811e-05,5.6878173154e-05,5.67987781843e-05,5.67472687118e-05,8.51264489853e-05,2.83498693196e-05,0.0,0.0,0.0,0.0,0.0,0.0,2.79727320775e-05,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0])

    # Creating weights for histo: y13_THT_9
    y13_THT_9_weights = numpy.array([0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0])

    # Creating weights for histo: y13_THT_10
    y13_THT_10_weights = numpy.array([0.0,0.0,2.10674221742,1.0529581672,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0])

    # Creating weights for histo: y13_THT_11
    y13_THT_11_weights = numpy.array([0.0,0.0,0.0,0.0,3.22355653936,3.91648758464,6.91005084012,5.06774515126,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0])

    # Creating weights for histo: y13_THT_12
    y13_THT_12_weights = numpy.array([0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,4.37471893037,3.21280871714,2.60323297969,2.07636941127,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0])

    # Creating weights for histo: y13_THT_13
    y13_THT_13_weights = numpy.array([0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,1.31077572066,1.04841824069,0.816446335376,0.423625755548,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0])

    # Creating weights for histo: y13_THT_14
    y13_THT_14_weights = numpy.array([0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.424432045545,0.350834347759,0.19518284527,0.164096913508,0.115967493091,0.0990156890494,0.0565609806345,0.0650786851446,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0])

    # Creating weights for histo: y13_THT_15
    y13_THT_15_weights = numpy.array([0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.032007230665,0.018294757707,0.00762592704651,0.0136817673588,0.00911792724347,0.00608509100035,0.0091035258683,0.0091871176666,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0])

    # Creating weights for histo: y13_THT_16
    y13_THT_16_weights = numpy.array([0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.00252724631491,0.00162449497444,0.00144392114531,0.000540700508915,0.000180970247521,0.00108431958418,0.000361809215378,0.000180003628817,0.000723210424343,0.000180503377,0.0,0.000361395780686,0.0,0.0,0.0,0.000180203012211,0.0,0.0,0.000180755041269,0.000180766975784,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0])

    # Creating a new Canvas
    fig   = plt.figure(figsize=(12,6),dpi=80)
    frame = gridspec.GridSpec(1,1,right=0.7)
    pad   = fig.add_subplot(frame[0])

    # Creating a new Stack
    pad.hist(x=xData, bins=xBinning, weights=y13_THT_0_weights+y13_THT_1_weights+y13_THT_2_weights+y13_THT_3_weights+y13_THT_4_weights+y13_THT_5_weights+y13_THT_6_weights+y13_THT_7_weights+y13_THT_8_weights+y13_THT_9_weights+y13_THT_10_weights+y13_THT_11_weights+y13_THT_12_weights+y13_THT_13_weights+y13_THT_14_weights+y13_THT_15_weights+y13_THT_16_weights,\
             label="$bg\_dip\_1600\_inf$", histtype="step", rwidth=1.0,\
             color=None, edgecolor="#e5e5e5", linewidth=1, linestyle="solid",\
             bottom=None, cumulative=False, normed=False, align="mid", orientation="vertical")

    pad.hist(x=xData, bins=xBinning, weights=y13_THT_0_weights+y13_THT_1_weights+y13_THT_2_weights+y13_THT_3_weights+y13_THT_4_weights+y13_THT_5_weights+y13_THT_6_weights+y13_THT_7_weights+y13_THT_8_weights+y13_THT_9_weights+y13_THT_10_weights+y13_THT_11_weights+y13_THT_12_weights+y13_THT_13_weights+y13_THT_14_weights+y13_THT_15_weights,\
             label="$bg\_dip\_1200\_1600$", histtype="step", rwidth=1.0,\
             color=None, edgecolor="#f2f2f2", linewidth=1, linestyle="solid",\
             bottom=None, cumulative=False, normed=False, align="mid", orientation="vertical")

    pad.hist(x=xData, bins=xBinning, weights=y13_THT_0_weights+y13_THT_1_weights+y13_THT_2_weights+y13_THT_3_weights+y13_THT_4_weights+y13_THT_5_weights+y13_THT_6_weights+y13_THT_7_weights+y13_THT_8_weights+y13_THT_9_weights+y13_THT_10_weights+y13_THT_11_weights+y13_THT_12_weights+y13_THT_13_weights+y13_THT_14_weights,\
             label="$bg\_dip\_800\_1200$", histtype="step", rwidth=1.0,\
             color=None, edgecolor="#ccc6aa", linewidth=1, linestyle="solid",\
             bottom=None, cumulative=False, normed=False, align="mid", orientation="vertical")

    pad.hist(x=xData, bins=xBinning, weights=y13_THT_0_weights+y13_THT_1_weights+y13_THT_2_weights+y13_THT_3_weights+y13_THT_4_weights+y13_THT_5_weights+y13_THT_6_weights+y13_THT_7_weights+y13_THT_8_weights+y13_THT_9_weights+y13_THT_10_weights+y13_THT_11_weights+y13_THT_12_weights+y13_THT_13_weights,\
             label="$bg\_dip\_600\_800$", histtype="step", rwidth=1.0,\
             color=None, edgecolor="#ccc6aa", linewidth=1, linestyle="solid",\
             bottom=None, cumulative=False, normed=False, align="mid", orientation="vertical")

    pad.hist(x=xData, bins=xBinning, weights=y13_THT_0_weights+y13_THT_1_weights+y13_THT_2_weights+y13_THT_3_weights+y13_THT_4_weights+y13_THT_5_weights+y13_THT_6_weights+y13_THT_7_weights+y13_THT_8_weights+y13_THT_9_weights+y13_THT_10_weights+y13_THT_11_weights+y13_THT_12_weights,\
             label="$bg\_dip\_400\_600$", histtype="step", rwidth=1.0,\
             color=None, edgecolor="#c1bfa8", linewidth=1, linestyle="solid",\
             bottom=None, cumulative=False, normed=False, align="mid", orientation="vertical")

    pad.hist(x=xData, bins=xBinning, weights=y13_THT_0_weights+y13_THT_1_weights+y13_THT_2_weights+y13_THT_3_weights+y13_THT_4_weights+y13_THT_5_weights+y13_THT_6_weights+y13_THT_7_weights+y13_THT_8_weights+y13_THT_9_weights+y13_THT_10_weights+y13_THT_11_weights,\
             label="$bg\_dip\_200\_400$", histtype="step", rwidth=1.0,\
             color=None, edgecolor="#bab5a3", linewidth=1, linestyle="solid",\
             bottom=None, cumulative=False, normed=False, align="mid", orientation="vertical")

    pad.hist(x=xData, bins=xBinning, weights=y13_THT_0_weights+y13_THT_1_weights+y13_THT_2_weights+y13_THT_3_weights+y13_THT_4_weights+y13_THT_5_weights+y13_THT_6_weights+y13_THT_7_weights+y13_THT_8_weights+y13_THT_9_weights+y13_THT_10_weights,\
             label="$bg\_dip\_100\_200$", histtype="step", rwidth=1.0,\
             color=None, edgecolor="#b2a596", linewidth=1, linestyle="solid",\
             bottom=None, cumulative=False, normed=False, align="mid", orientation="vertical")

    pad.hist(x=xData, bins=xBinning, weights=y13_THT_0_weights+y13_THT_1_weights+y13_THT_2_weights+y13_THT_3_weights+y13_THT_4_weights+y13_THT_5_weights+y13_THT_6_weights+y13_THT_7_weights+y13_THT_8_weights+y13_THT_9_weights,\
             label="$bg\_dip\_0\_100$", histtype="step", rwidth=1.0,\
             color=None, edgecolor="#b7a39b", linewidth=1, linestyle="solid",\
             bottom=None, cumulative=False, normed=False, align="mid", orientation="vertical")

    pad.hist(x=xData, bins=xBinning, weights=y13_THT_0_weights+y13_THT_1_weights+y13_THT_2_weights+y13_THT_3_weights+y13_THT_4_weights+y13_THT_5_weights+y13_THT_6_weights+y13_THT_7_weights+y13_THT_8_weights,\
             label="$bg\_vbf\_1600\_inf$", histtype="step", rwidth=1.0,\
             color=None, edgecolor="#ad998c", linewidth=1, linestyle="solid",\
             bottom=None, cumulative=False, normed=False, align="mid", orientation="vertical")

    pad.hist(x=xData, bins=xBinning, weights=y13_THT_0_weights+y13_THT_1_weights+y13_THT_2_weights+y13_THT_3_weights+y13_THT_4_weights+y13_THT_5_weights+y13_THT_6_weights+y13_THT_7_weights,\
             label="$bg\_vbf\_1200\_1600$", histtype="step", rwidth=1.0,\
             color=None, edgecolor="#9b8e82", linewidth=1, linestyle="solid",\
             bottom=None, cumulative=False, normed=False, align="mid", orientation="vertical")

    pad.hist(x=xData, bins=xBinning, weights=y13_THT_0_weights+y13_THT_1_weights+y13_THT_2_weights+y13_THT_3_weights+y13_THT_4_weights+y13_THT_5_weights+y13_THT_6_weights,\
             label="$bg\_vbf\_800\_1200$", histtype="step", rwidth=1.0,\
             color=None, edgecolor="#876656", linewidth=1, linestyle="solid",\
             bottom=None, cumulative=False, normed=False, align="mid", orientation="vertical")

    pad.hist(x=xData, bins=xBinning, weights=y13_THT_0_weights+y13_THT_1_weights+y13_THT_2_weights+y13_THT_3_weights+y13_THT_4_weights+y13_THT_5_weights,\
             label="$bg\_vbf\_600\_800$", histtype="step", rwidth=1.0,\
             color=None, edgecolor="#afcec6", linewidth=1, linestyle="solid",\
             bottom=None, cumulative=False, normed=False, align="mid", orientation="vertical")

    pad.hist(x=xData, bins=xBinning, weights=y13_THT_0_weights+y13_THT_1_weights+y13_THT_2_weights+y13_THT_3_weights+y13_THT_4_weights,\
             label="$bg\_vbf\_400\_600$", histtype="step", rwidth=1.0,\
             color=None, edgecolor="#84c1a3", linewidth=1, linestyle="solid",\
             bottom=None, cumulative=False, normed=False, align="mid", orientation="vertical")

    pad.hist(x=xData, bins=xBinning, weights=y13_THT_0_weights+y13_THT_1_weights+y13_THT_2_weights+y13_THT_3_weights,\
             label="$bg\_vbf\_200\_400$", histtype="step", rwidth=1.0,\
             color=None, edgecolor="#89a8a0", linewidth=1, linestyle="solid",\
             bottom=None, cumulative=False, normed=False, align="mid", orientation="vertical")

    pad.hist(x=xData, bins=xBinning, weights=y13_THT_0_weights+y13_THT_1_weights+y13_THT_2_weights,\
             label="$bg\_vbf\_100\_200$", histtype="step", rwidth=1.0,\
             color=None, edgecolor="#829e8c", linewidth=1, linestyle="solid",\
             bottom=None, cumulative=False, normed=False, align="mid", orientation="vertical")

    pad.hist(x=xData, bins=xBinning, weights=y13_THT_0_weights+y13_THT_1_weights,\
             label="$bg\_vbf\_0\_100$", histtype="step", rwidth=1.0,\
             color=None, edgecolor="#adbcc6", linewidth=1, linestyle="solid",\
             bottom=None, cumulative=False, normed=False, align="mid", orientation="vertical")

    pad.hist(x=xData, bins=xBinning, weights=y13_THT_0_weights,\
             label="$signal$", histtype="step", rwidth=1.0,\
             color=None, edgecolor="#7a8e99", linewidth=1, linestyle="solid",\
             bottom=None, cumulative=False, normed=False, align="mid", orientation="vertical")


    # Axis
    plt.rc('text',usetex=False)
    plt.xlabel(r"THT",\
               fontsize=16,color="black")
    plt.ylabel(r"$\mathrm{Events}$ $(\mathcal{L}_{\mathrm{int}} = 40.0\ \mathrm{fb}^{-1})$ ",\
               fontsize=16,color="black")

    # Boundary of y-axis
    ymax=(y13_THT_0_weights+y13_THT_1_weights+y13_THT_2_weights+y13_THT_3_weights+y13_THT_4_weights+y13_THT_5_weights+y13_THT_6_weights+y13_THT_7_weights+y13_THT_8_weights+y13_THT_9_weights+y13_THT_10_weights+y13_THT_11_weights+y13_THT_12_weights+y13_THT_13_weights+y13_THT_14_weights+y13_THT_15_weights+y13_THT_16_weights).max()*1.1
    ymin=0 # linear scale
    #ymin=min([x for x in (y13_THT_0_weights+y13_THT_1_weights+y13_THT_2_weights+y13_THT_3_weights+y13_THT_4_weights+y13_THT_5_weights+y13_THT_6_weights+y13_THT_7_weights+y13_THT_8_weights+y13_THT_9_weights+y13_THT_10_weights+y13_THT_11_weights+y13_THT_12_weights+y13_THT_13_weights+y13_THT_14_weights+y13_THT_15_weights+y13_THT_16_weights) if x])/100. # log scale
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
