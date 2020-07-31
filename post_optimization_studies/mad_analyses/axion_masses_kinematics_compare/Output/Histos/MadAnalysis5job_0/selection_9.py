def selection_9():

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

    # Creating weights for histo: y10_THT_0
    y10_THT_0_weights = numpy.array([2481.65014775,47204.5499588,47204.5499588,36624.2128929,35810.339271,32554.8527909,25636.949025,29299.3703143,21160.6541139,19125.9760647,17498.2328246,14242.750348,13428.8767262,10987.2638679,6510.96895673,7324.84257858,7324.84257858,7324.84257858,3662.42128929,4476.29090753,3662.42128929,2441.6140594,2848.54966925,1627.74283972,1220.80722988,2034.67844956,406.935609841,406.935609841,0.0,406.935609841,0.0,0.0,0.0,0.0,406.935609841,0.0,0.0,406.935609841,406.935609841,406.935609841,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0])

    # Creating weights for histo: y10_THT_1
    y10_THT_1_weights = numpy.array([1746.10994152,22861.3990337,23543.8295129,30368.1303014,29685.6998222,26273.5514297,27297.1951467,19449.2506413,25591.1209505,16719.532728,17401.9632072,15354.6717696,12624.9538563,10236.4491809,7165.51402628,8530.37498468,6824.29678492,6483.08354708,4777.00935086,4094.57887166,3753.36443276,3070.93435392,3753.36443276,2388.50467543,2729.71951467,682.429678492,341.214919316,1364.85975734,682.429678492,682.429678492,682.429678492,1023.64491809,341.214919316,682.429678492,341.214919316,0.0,341.214919316,341.214919316,0.0,0.0,341.214919316,0.0,0.0,0.0,341.214919316,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0])

    # Creating weights for histo: y10_THT_2
    y10_THT_2_weights = numpy.array([729.07128429,9269.53483939,9475.6837983,7776.74196496,6952.1501295,5992.49642446,5324.2953855,3980.78179851,3497.40119155,2758.11306325,2523.5312687,2160.99591348,1684.72361544,1606.52981726,1194.23469956,980.97823177,881.458706808,653.985621186,490.489315894,504.706333743,454.946571262,326.992810593,284.341557036,298.558654889,199.039089926,199.039089926,113.736622815,106.628073888,85.3024671109,78.1939181846,106.628073888,35.5426966296,14.2170778518,49.759762481,49.759762481,63.9768603336,42.6512535563,35.5426966296,28.4341557036,0.0,7.108540926,14.2170778518,7.108540926,0.0,0.0,0.0,7.108540926,0.0,0.0,14.2170778518,0.0,7.108540926,7.108540926,0.0,0.0,0.0,0.0,0.0,0.0,0.0,7.108540926,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0])

    # Creating weights for histo: y10_THT_3
    y10_THT_3_weights = numpy.array([105.533423737,1274.1958288,1180.52600232,923.112497605,763.65925102,619.221915487,486.940203239,373.964273949,303.890662081,235.247154115,178.759229452,149.44271918,115.120945206,93.6698264773,69.3585799079,64.3533162057,40.7571015963,23.5962186075,28.6014743134,24.3112545658,22.8811786511,15.015775114,13.5856991994,9.29547945173,9.29547945173,5.00525970407,4.29021974766,3.57518458904,4.29021974766,0.0,2.14511067346,3.57518458904,0.715036757882,1.43007391558,0.0,0.715036757882,0.715036757882,0.715036757882,0.0,0.0,0.0,0.715036757882,0.715036757882,0.0,0.0,0.0,0.0,0.715036757882,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0])

    # Creating a new Canvas
    fig   = plt.figure(figsize=(12,6),dpi=80)
    frame = gridspec.GridSpec(1,1,right=0.7)
    pad   = fig.add_subplot(frame[0])

    # Creating a new Stack
    pad.hist(x=xData, bins=xBinning, weights=y10_THT_0_weights+y10_THT_1_weights+y10_THT_2_weights+y10_THT_3_weights,\
             label="$signal100GeV4TeV$", histtype="stepfilled", rwidth=1.0,\
             color="#0000ff", edgecolor="#0000ff", linewidth=1, linestyle="solid",\
             bottom=None, cumulative=False, normed=False, align="mid", orientation="vertical")

    pad.hist(x=xData, bins=xBinning, weights=y10_THT_0_weights+y10_THT_1_weights+y10_THT_2_weights,\
             label="$signal100GeV1p5TeV$", histtype="stepfilled", rwidth=1.0,\
             color="#59d354", edgecolor="#59d354", linewidth=1, linestyle="solid",\
             bottom=None, cumulative=False, normed=False, align="mid", orientation="vertical")

    pad.hist(x=xData, bins=xBinning, weights=y10_THT_0_weights+y10_THT_1_weights,\
             label="$signal100GeV1TeV$", histtype="stepfilled", rwidth=1.0,\
             color="#ce5e60", edgecolor="#ce5e60", linewidth=1, linestyle="solid",\
             bottom=None, cumulative=False, normed=False, align="mid", orientation="vertical")

    pad.hist(x=xData, bins=xBinning, weights=y10_THT_0_weights,\
             label="$signal1MeV$", histtype="stepfilled", rwidth=1.0,\
             color="#5954d8", edgecolor="#5954d8", linewidth=1, linestyle="solid",\
             bottom=None, cumulative=False, normed=False, align="mid", orientation="vertical")


    # Axis
    plt.rc('text',usetex=False)
    plt.xlabel(r"THT",\
               fontsize=16,color="black")
    plt.ylabel(r"$\mathrm{Events}$ $(\mathcal{L}_{\mathrm{int}} = 40.0\ \mathrm{fb}^{-1})$ ",\
               fontsize=16,color="black")

    # Boundary of y-axis
    ymax=(y10_THT_0_weights+y10_THT_1_weights+y10_THT_2_weights+y10_THT_3_weights).max()*1.1
    ymin=0 # linear scale
    #ymin=min([x for x in (y10_THT_0_weights+y10_THT_1_weights+y10_THT_2_weights+y10_THT_3_weights) if x])/100. # log scale
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
    plt.savefig('../../HTML/MadAnalysis5job_0/selection_9.png')
    plt.savefig('../../PDF/MadAnalysis5job_0/selection_9.png')
    plt.savefig('../../DVI/MadAnalysis5job_0/selection_9.eps')

# Running!
if __name__ == '__main__':
    selection_9()
