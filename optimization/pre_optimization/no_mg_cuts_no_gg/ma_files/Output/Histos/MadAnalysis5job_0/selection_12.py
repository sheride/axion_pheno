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
    y13_THT_0_weights = numpy.array([8.17647734094,161.263020047,216.312877984,222.794864733,214.334523902,197.032210297,177.074462708,154.949203988,134.422186421,113.9044828,97.8141813947,84.1555794005,72.0609608268,62.7450561065,54.0407138744,45.7302356333,39.6517386182,35.0029243184,30.0295529786,26.4881788496,22.9506662107,20.0674682713,17.0794544616,15.0466597654,12.7875761556,11.2203548396,9.79195529039,8.55450362622,7.31199524888,6.51090795061,5.6404657326,5.01800632732,4.17268378168,3.88459863522,3.25797753501,2.88644862647,2.37787959316,2.07592825963,1.86236827229,1.56746835539,1.38399521178,1.25632459688,1.03796572878,0.949757063857,0.74076650641,0.631570683012,0.557267379693,0.448243044828,0.436527060145,0.371609456181,0.341342449546,0.25308745474,0.25306506929,0.227563245316,0.174121542088,0.176486165098,0.118429061852,0.111486534451,0.0580393547829,0.0580673765689,0.0742807179985,0.0464392947493,0.0510597314943,0.0348351493711,0.0464062762111,0.0301832250927,0.0348406537932,0.0232250598566,0.0139462510242,0.0255424495678,0.016245008846,0.00697689306321,0.0115974057589,0.009284924857,0.00928627597877,0.00928863044838,0.00464149505728,0.00696555643195,0.00232833939398,0.00232582382908])

    # Creating a new Canvas
    fig   = plt.figure(figsize=(8,6),dpi=80)
    frame = gridspec.GridSpec(1,1)
    pad   = fig.add_subplot(frame[0])

    # Creating a new Stack
    pad.hist(x=xData, bins=xBinning, weights=y13_THT_0_weights,\
             label="$signal$", histtype="stepfilled", rwidth=1.0,\
             color="#5954d8", edgecolor="#5954d8", linewidth=1, linestyle="solid",\
             bottom=None, cumulative=False, normed=False, align="mid", orientation="vertical")


    # Axis
    plt.rc('text',usetex=False)
    plt.xlabel(r"THT",\
               fontsize=16,color="black")
    plt.ylabel(r"$\mathrm{Events}$ $(\mathcal{L}_{\mathrm{int}} = 40.0\ \mathrm{fb}^{-1})$ ",\
               fontsize=16,color="black")

    # Boundary of y-axis
    ymax=(y13_THT_0_weights).max()*1.1
    ymin=0 # linear scale
    #ymin=min([x for x in (y13_THT_0_weights) if x])/100. # log scale
    plt.gca().set_ylim(ymin,ymax)

    # Log/Linear scale for X-axis
    plt.gca().set_xscale("linear")
    #plt.gca().set_xscale("log",nonposx="clip")

    # Log/Linear scale for Y-axis
    plt.gca().set_yscale("linear")
    #plt.gca().set_yscale("log",nonposy="clip")

    # Saving the image
    plt.savefig('../../HTML/MadAnalysis5job_0/selection_12.png')
    plt.savefig('../../PDF/MadAnalysis5job_0/selection_12.png')
    plt.savefig('../../DVI/MadAnalysis5job_0/selection_12.eps')

# Running!
if __name__ == '__main__':
    selection_12()
