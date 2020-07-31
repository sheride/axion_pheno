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
    xBinning = numpy.linspace(-8.0,8.0,101,endpoint=True)

    # Creating data sequence: middle of each bin
    xData = numpy.array([-7.92,-7.76,-7.6,-7.44,-7.28,-7.12,-6.96,-6.8,-6.64,-6.48,-6.32,-6.16,-6.0,-5.84,-5.68,-5.52,-5.36,-5.2,-5.04,-4.88,-4.72,-4.56,-4.4,-4.24,-4.08,-3.92,-3.76,-3.6,-3.44,-3.28,-3.12,-2.96,-2.8,-2.64,-2.48,-2.32,-2.16,-2.0,-1.84,-1.68,-1.52,-1.36,-1.2,-1.04,-0.88,-0.72,-0.56,-0.4,-0.24,-0.08,0.08,0.24,0.4,0.56,0.72,0.88,1.04,1.2,1.36,1.52,1.68,1.84,2.0,2.16,2.32,2.48,2.64,2.8,2.96,3.12,3.28,3.44,3.6,3.76,3.92,4.08,4.24,4.4,4.56,4.72,4.88,5.04,5.2,5.36,5.52,5.68,5.84,6.0,6.16,6.32,6.48,6.64,6.8,6.96,7.12,7.28,7.44,7.6,7.76,7.92])

    # Creating weights for histo: y1_ETA_0
    y1_ETA_0_weights = numpy.array([0.0040940844941,0.00818816898821,0.00818816898821,0.0122822534823,0.0368467564469,0.0163763339764,0.0040940844941,0.0204704184705,0.0491289979293,0.0614112674116,0.077787613388,0.110540265341,0.188327878729,0.176045609246,0.253833222634,0.40940844941,0.470819596822,0.765593744398,1.09721466042,1.40427079748,1.76864408545,2.54652021933,3.27117319879,4.515776133,5.96507889191,7.41848164732,9.63337975063,12.3518494227,15.246366944,19.0538676836,23.5246078551,28.1836758654,34.8365621683,41.2642846641,48.3388386059,56.2322318465,66.2177032957,76.8213742154,86.0453663166,97.2385967315,108.153427385,118.888098192,128.803969701,136.480403127,142.744317763,147.059514068,152.803509149,154.756387477,155.345906972,156.754305766,156.705145808,155.763506615,155.583386769,152.365429525,149.298952151,141.376918934,134.404684905,127.95241043,118.228938757,107.915947588,96.9724769594,85.9143664288,76.3505746186,66.0867034078,56.9691912155,48.5107984586,41.2315246921,34.8611261473,28.7036234202,23.1725161566,18.9637957607,15.7049065514,12.6630011563,9.61290776816,7.87701725466,5.94051491295,4.46255217857,3.36124312166,2.55061421583,1.96516031717,1.41245879047,0.859757663762,0.765593744398,0.577265905669,0.421690838893,0.290679951081,0.266115452117,0.114634341835,0.102352112353,0.0982579958585,0.106446188847,0.0245645029646,0.0122822534823,0.0327526719528,0.0204704184705,0.00818816898821,0.00818816898821,0.0122822534823,0.0,0.0040940844941])

    # Creating a new Canvas
    fig   = plt.figure(figsize=(8,6),dpi=80)
    frame = gridspec.GridSpec(1,1)
    pad   = fig.add_subplot(frame[0])

    # Creating a new Stack
    pad.hist(x=xData, bins=xBinning, weights=y1_ETA_0_weights,\
             label="$signal$", histtype="stepfilled", rwidth=1.0,\
             color="#5954d8", edgecolor="#5954d8", linewidth=1, linestyle="solid",\
             bottom=None, cumulative=False, normed=False, align="mid", orientation="vertical")


    # Axis
    plt.rc('text',usetex=False)
    plt.xlabel(r"$\eta$ $[ a_{1} a_{2} ]$ ",\
               fontsize=16,color="black")
    plt.ylabel(r"$\mathrm{Events}$ $(\mathcal{L}_{\mathrm{int}} = 40.0\ \mathrm{fb}^{-1})$ ",\
               fontsize=16,color="black")

    # Boundary of y-axis
    ymax=(y1_ETA_0_weights).max()*1.1
    ymin=0 # linear scale
    #ymin=min([x for x in (y1_ETA_0_weights) if x])/100. # log scale
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
