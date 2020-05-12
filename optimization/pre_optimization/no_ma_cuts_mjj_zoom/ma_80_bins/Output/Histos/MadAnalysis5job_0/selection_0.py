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
    xBinning = numpy.linspace(0.0,400.0,81,endpoint=True)

    # Creating data sequence: middle of each bin
    xData = numpy.array([2.5,7.5,12.5,17.5,22.5,27.5,32.5,37.5,42.5,47.5,52.5,57.5,62.5,67.5,72.5,77.5,82.5,87.5,92.5,97.5,102.5,107.5,112.5,117.5,122.5,127.5,132.5,137.5,142.5,147.5,152.5,157.5,162.5,167.5,172.5,177.5,182.5,187.5,192.5,197.5,202.5,207.5,212.5,217.5,222.5,227.5,232.5,237.5,242.5,247.5,252.5,257.5,262.5,267.5,272.5,277.5,282.5,287.5,292.5,297.5,302.5,307.5,312.5,317.5,322.5,327.5,332.5,337.5,342.5,347.5,352.5,357.5,362.5,367.5,372.5,377.5,382.5,387.5,392.5,397.5])

    # Creating weights for histo: y1_M_0
    y1_M_0_weights = numpy.array([0.0,0.0,0.0,0.0,0.0,0.0,3.14401955096,9.43206105287,15.7200977548,12.5760774038,12.5760774038,15.7200977548,9.43206105287,12.5760774038,6.28804070191,81.7445291248,100.608611231,44.0162849134,44.0162849134,44.0162849134,31.4401955096,40.8722445624,84.8885294758,50.3043256153,47.1602852643,72.312448072,53.4483259662,62.8804070191,56.5923663172,81.7445291248,78.6004887739,50.3043256153,66.0244073701,97.4646108796,69.168447721,94.3206105287,94.3206105287,56.5923663172,78.6004887739,88.0325698267,81.7445291248,88.0325698267,91.1765701777,84.8885294758,88.0325698267,81.7445291248,144.624896144,113.184692634,106.896651932,75.4564884229,97.4646108796,91.1765701777,122.616773687,113.184692634,62.8804070191,100.608611231,116.328732985,100.608611231,122.616773687,97.4646108796,116.328732985,113.184692634,116.328732985,150.912936846,106.896651932,78.6004887739,81.7445291248,110.040692283,100.608611231,141.480895793,81.7445291248,84.8885294758,106.896651932,128.904814389,138.336855442,113.184692634,84.8885294758,116.328732985,97.4646108796,97.4646108796])

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
