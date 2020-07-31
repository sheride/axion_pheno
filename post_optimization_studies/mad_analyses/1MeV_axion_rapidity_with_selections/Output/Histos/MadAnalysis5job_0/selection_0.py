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
    y1_ETA_0_weights = numpy.array([0.0,0.0,0.0,0.0,0.00818816896832,0.00409408448416,0.00409408448416,0.00409408448416,0.0122822534525,0.0163763339367,0.0122822534525,0.0204704184208,0.0450349213258,0.0777876131991,0.0777876131991,0.110540265072,0.110540265072,0.212892377176,0.302962219828,0.39303206248,0.556795521846,0.749217356602,1.03170911401,1.30601287845,1.73589170928,2.13711176473,2.80854158814,3.47587741505,4.55262009039,5.64574315166,6.55463037114,7.72553736561,9.42048791006,10.8902626479,12.6548131325,14.3333876911,15.9423623093,17.444893019,18.8450678166,20.4499504384,21.3752136438,22.0998650215,22.4273927402,23.2298320511,22.5870606031,22.5624966242,22.6853205187,22.3373208176,21.7354933344,22.1612769688,22.0834890356,21.98522912,22.5051806734,22.619812575,23.4672878472,22.3987327649,22.7221644871,22.3168528352,22.2063129301,21.2810497247,19.8849669236,19.0333956549,17.6004688854,15.9792102777,14.0345199477,12.8226689884,11.4143061978,9.62519173427,7.99574513357,6.43180647662,5.64164715518,4.64269201304,3.55775894474,2.75941243033,2.34181598894,1.77273847764,1.32238926438,0.941639191358,0.741029363633,0.540419135909,0.405314451932,0.274303644439,0.19651603124,0.151481109914,0.143292956946,0.0777876131991,0.0532230742941,0.0409408448416,0.0409408448416,0.0204704184208,0.0163763339367,0.00409408448416,0.00818816896832,0.00409408448416,0.00818816896832,0.0,0.0,0.0,0.0,0.0])

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
