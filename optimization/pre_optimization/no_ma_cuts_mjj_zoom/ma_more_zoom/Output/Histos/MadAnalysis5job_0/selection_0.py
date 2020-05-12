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
    xBinning = numpy.linspace(50.0,110.0,31,endpoint=True)

    # Creating data sequence: middle of each bin
    xData = numpy.array([51.0,53.0,55.0,57.0,59.0,61.0,63.0,65.0,67.0,69.0,71.0,73.0,75.0,77.0,79.0,81.0,83.0,85.0,87.0,89.0,91.0,93.0,95.0,97.0,99.0,101.0,103.0,105.0,107.0,109.0])

    # Creating weights for histo: y1_M_0
    y1_M_0_weights = numpy.array([0.0,9.43206029823,3.14401929941,6.28804019882,9.43206029823,0.0,3.14401929941,9.43206029823,3.14401929941,6.28804019882,3.14401929941,3.14401929941,3.14401929941,22.0081366959,56.5923617894,66.0244020876,18.8641165965,15.720096497,25.1521567953,18.8641165965,28.2961768947,9.43206029823,12.5760763976,15.720096497,22.0081366959,6.28804019882,25.1521567953,3.14401929941,15.720096497,22.0081366959])

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
