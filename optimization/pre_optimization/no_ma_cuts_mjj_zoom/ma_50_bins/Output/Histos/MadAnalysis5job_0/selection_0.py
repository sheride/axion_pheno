def selection_0():

    # Library import
    import numpy
    import matplotlib
    import matplotlib.pyplot   as plt
    import matplotlib.gridspec as gridspec

    # Library version
    matplotlib_version = matplotlib.__version__
    numpy_version      = numpy.__version__

    # Histo binning
    xBinning = numpy.linspace(0.0,400.0,51,endpoint=True)

    # Creating data sequence: middle of each bin
    xData = numpy.array([4.0,12.0,20.0,28.0,36.0,44.0,52.0,60.0,68.0,76.0,84.0,92.0,100.0,108.0,116.0,124.0,132.0,140.0,148.0,156.0,164.0,172.0,180.0,188.0,196.0,204.0,212.0,220.0,228.0,236.0,244.0,252.0,260.0,268.0,276.0,284.0,292.0,300.0,308.0,316.0,324.0,332.0,340.0,348.0,356.0,364.0,372.0,380.0,388.0,396.0])

    # Creating weights for histo: y1_M_0
    y1_M_0_weights = numpy.array([0.0,0.0,0.0,0.0,12.5760774243,25.1521588486,15.7200977804,18.8641181365,22.0081384925,84.888529614,125.760774243,69.1684478337,69.1684478337,69.1684478337,106.896652107,94.3206106823,84.888529614,103.75265175,106.896652107,113.184692819,135.192855311,125.760774243,144.624896379,94.3206106823,144.624896379,147.768936736,138.336855667,119.472733531,160.34501816,207.505303501,150.912937092,141.480896023,188.641181365,157.200977804,132.048814955,172.921099584,176.06509994,194.929222077,147.768936736,242.089507418,157.200977804,135.192855311,166.633058872,191.785221721,135.192855311,176.06509994,223.225385281,154.056977448,172.921099584,157.200977804])

    # Creating a new Canvas
    fig   = plt.figure(figsize=(8,6),dpi=80)
    frame = gridspec.GridSpec(1,1)
    pad   = fig.add_subplot(frame[0])

    # Creating a new Stack
    pad.hist(x=xData, bins=xBinning, weights=y1_M_0_weights,\
             label="$signal$", histtype="stepfilled", rwidth=1.0,\
             color="#5954d8", edgecolor="#5954d8", linewidth=1, linestyle="solid",\
             bottom=None, cumulative=False, normed=False, align="mid", orientation="vertical")


    # Axis
    plt.rc('text',usetex=False)
    plt.xlabel(r"M [ j_{1} , j_{2} ]   ( GeV ) ",\
               fontsize=16,color="black")
    plt.ylabel(r"$\mathrm{Events}$ $(\mathcal{L}_{\mathrm{int}} = 40.0\ \mathrm{fb}^{-1})$ ",\
               fontsize=16,color="black")

    # Boundary of y-axis
    ymax=(y1_M_0_weights).max()*1.1
    ymin=0 # linear scale
    #ymin=min([x for x in (y1_M_0_weights) if x])/100. # log scale
    plt.gca().set_ylim(ymin,ymax)

    # Log/Linear scale for X-axis
    plt.gca().set_xscale("linear")
    #plt.gca().set_xscale("log",nonposx="clip")

    # Log/Linear scale for Y-axis
    plt.gca().set_yscale("linear")
    #plt.gca().set_yscale("log",nonposy="clip")

    # Saving the image
    plt.savefig('../../HTML/MadAnalysis5job_0/selection_0.png')
    plt.savefig('../../PDF/MadAnalysis5job_0/selection_0.png')
    plt.savefig('../../DVI/MadAnalysis5job_0/selection_0.eps')

# Running!
if __name__ == '__main__':
    selection_0()
