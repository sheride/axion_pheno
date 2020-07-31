def selection_2():

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

    # Creating weights for histo: y3_PHI_0
    y3_PHI_0_weights = numpy.array([1626.27534535,4878.82723604,6911.67091772,5691.96310871,4472.2552997,7318.23885405,4878.82723604,6505.09898138,6098.53104505,6911.67091772,7318.23885405,8944.5145994,5691.96310871,6098.53104505,6505.09898138,6098.53104505,6911.67091772,4065.68736336,5285.39517237,4878.82723604,7318.23885405,2845.98155435,5691.96310871,6505.09898138,5285.39517237,5691.96310871,8537.94666306,6098.53104505,4065.68736336,4065.68736336,6911.67091772,6505.09898138,7318.23885405,4472.2552997,6505.09898138,8944.5145994,7724.80679039,5285.39517237,6911.67091772,9757.65047207,7724.80679039,5285.39517237,7318.23885405,5691.96310871,6911.67091772,6098.53104505,7724.80679039,6911.67091772,5691.96310871,6098.53104505,7724.80679039,7724.80679039,8537.94666306,5691.96310871,6098.53104505,9351.08253574,6098.53104505,6505.09898138,7318.23885405,4878.82723604,8131.37472673,6911.67091772,9757.65047207,2439.41281802])

    # Creating weights for histo: y3_PHI_1
    y3_PHI_1_weights = numpy.array([141.959877152,283.919809859,0.0,0.0,425.879687011,283.919809859,425.879687011,283.919809859,283.919809859,141.959877152,709.799385759,141.959877152,141.959877152,0.0,0.0,141.959877152,0.0,0.0,283.919809859,0.0,141.959877152,141.959877152,0.0,0.0,141.959877152,0.0,141.959877152,141.959877152,283.919809859,0.0,0.0,141.959877152,283.919809859,141.959877152,0.0,141.959877152,283.919809859,141.959877152,141.959877152,425.879687011,141.959877152,141.959877152,141.959877152,141.959877152,141.959877152,0.0,0.0,141.959877152,141.959877152,0.0,851.759262911,141.959877152,425.879687011,0.0,0.0,283.919809859,141.959877152,141.959877152,141.959877152,283.919809859,0.0,0.0,0.0,283.919809859])

    # Creating a new Canvas
    fig   = plt.figure(figsize=(12,6),dpi=80)
    frame = gridspec.GridSpec(1,1,right=0.7)
    pad   = fig.add_subplot(frame[0])

    # Creating a new Stack
    pad.hist(x=xData, bins=xBinning, weights=y3_PHI_0_weights+y3_PHI_1_weights,\
             label="$signal4TeV$", histtype="stepfilled", rwidth=1.0,\
             color="#ce5e60", edgecolor="#ce5e60", linewidth=1, linestyle="solid",\
             bottom=None, cumulative=False, normed=False, align="mid", orientation="vertical")

    pad.hist(x=xData, bins=xBinning, weights=y3_PHI_0_weights,\
             label="$signal1TeV$", histtype="stepfilled", rwidth=1.0,\
             color="#5954d8", edgecolor="#5954d8", linewidth=1, linestyle="solid",\
             bottom=None, cumulative=False, normed=False, align="mid", orientation="vertical")


    # Axis
    plt.rc('text',usetex=False)
    plt.xlabel(r"\phi [ j_{1} ] ",\
               fontsize=16,color="black")
    plt.ylabel(r"$\mathrm{Events}$ $(\mathcal{L}_{\mathrm{int}} = 40.0\ \mathrm{fb}^{-1})$ ",\
               fontsize=16,color="black")

    # Boundary of y-axis
    ymax=(y3_PHI_0_weights+y3_PHI_1_weights).max()*1.1
    ymin=0 # linear scale
    #ymin=min([x for x in (y3_PHI_0_weights+y3_PHI_1_weights) if x])/100. # log scale
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
    plt.savefig('../../HTML/MadAnalysis5job_0/selection_2.png')
    plt.savefig('../../PDF/MadAnalysis5job_0/selection_2.png')
    plt.savefig('../../DVI/MadAnalysis5job_0/selection_2.eps')

# Running!
if __name__ == '__main__':
    selection_2()
