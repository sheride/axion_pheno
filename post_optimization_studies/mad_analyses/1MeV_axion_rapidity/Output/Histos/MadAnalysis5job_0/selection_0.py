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
    y1_ETA_0_weights = numpy.array([0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,813.137467067,406.568733534,813.137467067,0.0,406.568733534,0.0,813.137467067,406.568733534,1626.27533413,813.137467067,4065.68733534,2032.84406767,4472.25526887,4878.8272024,6098.531003,6911.67087007,6911.67087007,12197.066006,15043.0455407,13823.3377401,12603.6339395,13010.2018731,19515.3008096,18702.1649425,16669.3212749,15856.1814078,21548.1484773,21141.5765437,22361.2843443,21954.7164108,14636.4776072,13010.2018731,15043.0455407,13823.3377401,11790.4940725,9757.6504048,9351.08247127,9351.08247127,5691.96306947,6098.531003,6098.531003,5285.39513594,4878.8272024,2845.98153473,2439.4128012,2439.4128012,2032.84406767,1626.27533413,1219.7066006,813.137467067,813.137467067,406.568733534,0.0,406.568733534,406.568733534,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0])

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
    plt.xlabel(r"$\eta$ $[ ax ]$ ",\
               fontsize=16,color="black")
    plt.ylabel(r"$\mathrm{N.}\ \mathrm{of}\ ax$ $(\mathcal{L}_{\mathrm{int}} = 40.0\ \mathrm{fb}^{-1})$ ",\
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
