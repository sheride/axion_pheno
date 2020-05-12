def selection_5():

    # Library import
    import numpy
    import matplotlib
    import matplotlib.pyplot   as plt
    import matplotlib.gridspec as gridspec

    # Library version
    matplotlib_version = matplotlib.__version__
    numpy_version      = numpy.__version__

    # Histo binning
    xBinning = numpy.linspace(-3.2,3.2,65,endpoint=True)

    # Creating data sequence: middle of each bin
    xData = numpy.array([-3.15,-3.05,-2.95,-2.85,-2.75,-2.65,-2.55,-2.45,-2.35,-2.25,-2.15,-2.05,-1.95,-1.85,-1.75,-1.65,-1.55,-1.45,-1.35,-1.25,-1.15,-1.05,-0.95,-0.85,-0.75,-0.65,-0.55,-0.45,-0.35,-0.25,-0.15,-0.05,0.05,0.15,0.25,0.35,0.45,0.55,0.65,0.75,0.85,0.95,1.05,1.15,1.25,1.35,1.45,1.55,1.65,1.75,1.85,1.95,2.05,2.15,2.25,2.35,2.45,2.55,2.65,2.75,2.85,2.95,3.05,3.15])

    # Creating weights for histo: y6_PHI_0
    y6_PHI_0_weights = numpy.array([26.01514117,52.7735623733,59.8348426909,59.8348426909,56.1183625238,55.7467225071,56.8616825572,66.152802975,56.8616825572,55.0034424736,54.6318024569,56.8616825572,60.5781227243,61.3214027578,55.0034424736,61.3214027578,62.0646827912,63.9229228748,57.6049625906,62.8080028246,55.7467225071,54.6318024569,58.348242624,61.6930427745,53.5168424068,57.6049625906,62.0646827912,51.2870023065,60.5781227243,62.0646827912,61.6930427745,65.7811229583,55.0034424736,63.1796428413,60.5781227243,56.4900025405,55.0034424736,62.8080028246,52.4019223566,56.1183625238,46.8272421059,60.949762741,61.3214027578,56.4900025405,62.8080028246,50.5437222731,59.4631626742,63.1796428413,61.3214027578,64.2945628915,63.1796428413,60.949762741,58.348242624,61.3214027578,61.3214027578,55.7467225071,61.3214027578,62.0646827912,63.1796428413,62.4363228079,60.2064827076,59.4631626742,69.4976031255,21.9270489861])

    # Creating a new Canvas
    fig   = plt.figure(figsize=(8,6),dpi=80)
    frame = gridspec.GridSpec(1,1)
    pad   = fig.add_subplot(frame[0])

    # Creating a new Stack
    pad.hist(x=xData, bins=xBinning, weights=y6_PHI_0_weights,\
             label="$signal$", histtype="stepfilled", rwidth=1.0,\
             color="#5954d8", edgecolor="#5954d8", linewidth=1, linestyle="solid",\
             bottom=None, cumulative=False, normed=False, align="mid", orientation="vertical")


    # Axis
    plt.rc('text',usetex=False)
    plt.xlabel(r"\phi [ j_{2} ] ",\
               fontsize=16,color="black")
    plt.ylabel(r"$\mathrm{Events}$ $(\mathcal{L}_{\mathrm{int}} = 40.0\ \mathrm{fb}^{-1})$ ",\
               fontsize=16,color="black")

    # Boundary of y-axis
    ymax=(y6_PHI_0_weights).max()*1.1
    ymin=0 # linear scale
    #ymin=min([x for x in (y6_PHI_0_weights) if x])/100. # log scale
    plt.gca().set_ylim(ymin,ymax)

    # Log/Linear scale for X-axis
    plt.gca().set_xscale("linear")
    #plt.gca().set_xscale("log",nonposx="clip")

    # Log/Linear scale for Y-axis
    plt.gca().set_yscale("linear")
    #plt.gca().set_yscale("log",nonposy="clip")

    # Saving the image
    plt.savefig('../../HTML/MadAnalysis5job_0/selection_5.png')
    plt.savefig('../../PDF/MadAnalysis5job_0/selection_5.png')
    plt.savefig('../../DVI/MadAnalysis5job_0/selection_5.eps')

# Running!
if __name__ == '__main__':
    selection_5()
