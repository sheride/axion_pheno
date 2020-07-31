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
    y13_THT_0_weights = numpy.array([2481.65014775,47204.5499588,47204.5499588,36624.2128929,35810.339271,32554.8527909,25636.949025,29299.3703143,21160.6541139,19125.9760647,17498.2328246,14242.750348,13428.8767262,10987.2638679,6510.96895673,7324.84257858,7324.84257858,7324.84257858,3662.42128929,4476.29090753,3662.42128929,2441.6140594,2848.54966925,1627.74283972,1220.80722988,2034.67844956,406.935609841,406.935609841,0.0,406.935609841,0.0,0.0,0.0,0.0,406.935609841,0.0,0.0,406.935609841,406.935609841,406.935609841,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0])

    # Creating weights for histo: y13_THT_1
    y13_THT_1_weights = numpy.array([670.387849719,2728.77864902,1773.7057748,955.072340275,682.194528768,955.072340275,818.633434522,409.316770656,0.0,0.0,0.0,272.877864902,272.877864902,136.438905754,0.0,0.0,136.438905754,0.0,136.438905754,0.0,0.0,0.0,0.0,0.0,0.0,0.0,272.877864902,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0])

    # Creating a new Canvas
    fig   = plt.figure(figsize=(12,6),dpi=80)
    frame = gridspec.GridSpec(1,1,right=0.7)
    pad   = fig.add_subplot(frame[0])

    # Creating a new Stack
    pad.hist(x=xData, bins=xBinning, weights=y13_THT_0_weights+y13_THT_1_weights,\
             label="$signal4TeV$", histtype="stepfilled", rwidth=1.0,\
             color="#ce5e60", edgecolor="#ce5e60", linewidth=1, linestyle="solid",\
             bottom=None, cumulative=False, normed=False, align="mid", orientation="vertical")

    pad.hist(x=xData, bins=xBinning, weights=y13_THT_0_weights,\
             label="$signal1TeV$", histtype="stepfilled", rwidth=1.0,\
             color="#5954d8", edgecolor="#5954d8", linewidth=1, linestyle="solid",\
             bottom=None, cumulative=False, normed=False, align="mid", orientation="vertical")


    # Axis
    plt.rc('text',usetex=False)
    plt.xlabel(r"THT",\
               fontsize=16,color="black")
    plt.ylabel(r"$\mathrm{Events}$ $(\mathcal{L}_{\mathrm{int}} = 40.0\ \mathrm{fb}^{-1})$ ",\
               fontsize=16,color="black")

    # Boundary of y-axis
    ymax=(y13_THT_0_weights+y13_THT_1_weights).max()*1.1
    ymin=0 # linear scale
    #ymin=min([x for x in (y13_THT_0_weights+y13_THT_1_weights) if x])/100. # log scale
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
