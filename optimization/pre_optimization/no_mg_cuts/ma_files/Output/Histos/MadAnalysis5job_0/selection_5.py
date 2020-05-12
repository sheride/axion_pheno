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
    y6_PHI_0_weights = numpy.array([238.945492924,493.611226699,547.05922959,440.162823808,474.746825679,487.323226359,550.20322976,424.442822958,465.314825168,521.907228229,512.475227719,430.730823298,521.907228229,490.467226529,465.314825168,600.507632481,525.0512284,547.05922959,537.62722908,543.91522942,531.33922874,490.467226529,427.586823128,433.874823468,569.06763078,565.92363061,496.755226869,509.331227549,462.170824998,496.755226869,528.19522857,433.874823468,521.907228229,481.034826019,443.306823978,490.467226529,543.91522942,518.763228059,506.187227379,462.170824998,465.314825168,496.755226869,537.62722908,528.19522857,509.331227549,449.594824318,503.043227209,481.034826019,474.746825679,559.63563027,534.48322891,575.35563112,418.154422618,499.899227039,543.91522942,437.018823638,506.187227379,477.890825849,528.19522857,455.882824658,515.619227889,512.475227719,503.043227209,191.785210373])

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
