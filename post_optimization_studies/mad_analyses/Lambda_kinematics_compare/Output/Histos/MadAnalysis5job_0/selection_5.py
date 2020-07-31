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
    y6_PHI_0_weights = numpy.array([2032.8441017,6505.09904545,7724.80686647,4472.25534374,6098.53110511,6505.09904545,6098.53110511,6911.67098579,5285.39522442,7318.23892613,5285.39522442,5285.39522442,6911.67098579,7318.23892613,6911.67098579,5691.96316476,8537.94674715,7318.23892613,5691.96316476,4472.25534374,4878.82728408,4472.25534374,6505.09904545,9757.65056817,6505.09904545,6911.67098579,6505.09904545,5285.39522442,8537.94674715,7318.23892613,8131.37480681,5285.39522442,5285.39522442,5691.96316476,8537.94674715,6098.53110511,7318.23892613,5691.96316476,4878.82728408,6911.67098579,6505.09904545,9351.08262783,7318.23892613,6911.67098579,4472.25534374,3659.11946306,4472.25534374,6098.53110511,10164.2185085,4065.6874034,5285.39522442,9351.08262783,9757.65056817,8537.94674715,4472.25534374,8131.37480681,5691.96316476,3252.55032272,5691.96316476,4878.82728408,7318.23892613,6505.09904545,9757.65056817,1626.27536136])

    # Creating weights for histo: y6_PHI_1
    y6_PHI_1_weights = numpy.array([141.959874022,283.919803599,0.0,283.919803599,283.919803599,283.919803599,283.919803599,141.959874022,141.959874022,0.0,0.0,141.959874022,141.959874022,425.879677621,425.879677621,141.959874022,0.0,0.0,141.959874022,425.879677621,141.959874022,283.919803599,141.959874022,0.0,141.959874022,0.0,283.919803599,283.919803599,283.919803599,141.959874022,141.959874022,141.959874022,283.919803599,0.0,0.0,141.959874022,0.0,141.959874022,0.0,141.959874022,141.959874022,141.959874022,425.879677621,141.959874022,0.0,0.0,0.0,141.959874022,283.919803599,567.839496088,283.919803599,0.0,141.959874022,141.959874022,283.919803599,283.919803599,0.0,141.959874022,283.919803599,141.959874022,141.959874022,0.0,0.0,0.0])

    # Creating a new Canvas
    fig   = plt.figure(figsize=(12,6),dpi=80)
    frame = gridspec.GridSpec(1,1,right=0.7)
    pad   = fig.add_subplot(frame[0])

    # Creating a new Stack
    pad.hist(x=xData, bins=xBinning, weights=y6_PHI_0_weights+y6_PHI_1_weights,\
             label="$signal4TeV$", histtype="stepfilled", rwidth=1.0,\
             color="#ce5e60", edgecolor="#ce5e60", linewidth=1, linestyle="solid",\
             bottom=None, cumulative=False, normed=False, align="mid", orientation="vertical")

    pad.hist(x=xData, bins=xBinning, weights=y6_PHI_0_weights,\
             label="$signal1TeV$", histtype="stepfilled", rwidth=1.0,\
             color="#5954d8", edgecolor="#5954d8", linewidth=1, linestyle="solid",\
             bottom=None, cumulative=False, normed=False, align="mid", orientation="vertical")


    # Axis
    plt.rc('text',usetex=False)
    plt.xlabel(r"\phi [ j_{2} ] ",\
               fontsize=16,color="black")
    plt.ylabel(r"$\mathrm{Events}$ $(\mathcal{L}_{\mathrm{int}} = 40.0\ \mathrm{fb}^{-1})$ ",\
               fontsize=16,color="black")

    # Boundary of y-axis
    ymax=(y6_PHI_0_weights+y6_PHI_1_weights).max()*1.1
    ymin=0 # linear scale
    #ymin=min([x for x in (y6_PHI_0_weights+y6_PHI_1_weights) if x])/100. # log scale
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
    plt.savefig('../../HTML/MadAnalysis5job_0/selection_5.png')
    plt.savefig('../../PDF/MadAnalysis5job_0/selection_5.png')
    plt.savefig('../../DVI/MadAnalysis5job_0/selection_5.eps')

# Running!
if __name__ == '__main__':
    selection_5()
