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
    y3_PHI_0_weights = numpy.array([15.3442714055,36.9467605991,36.8800188974,37.242189368,37.4603910803,37.1257951341,36.6245687916,37.073136507,36.8290951708,37.0121271723,36.7945210825,37.1697432815,37.2322116915,36.7751333697,36.9375744209,36.7524597393,36.952389032,36.8680704698,36.609750183,36.7966717195,36.6687128148,37.0859723722,37.1349773148,37.3138119764,37.133042541,36.9583932268,36.4706903137,37.0221967906,36.8820735952,37.1057958089,36.6659305781,37.2280423338,37.0660090242,36.7870018479,36.2733154021,36.8073529502,37.2628682625,37.2205870587,37.6740916453,36.2318017119,36.9312784111,36.8658758607,36.8942258935,37.0399135624,37.0902696487,36.9866193382,36.1732388267,37.0174597927,36.4685476716,37.0658491255,37.1856452035,37.0997676293,37.5922555099,37.1126474665,37.1886153211,37.2931530692,36.9055627087,36.7313571133,37.3311290016,36.8613787108,37.1822873315,36.5363726868,36.6469226246,15.4905586943])

    # Creating a new Canvas
    fig   = plt.figure(figsize=(8,6),dpi=80)
    frame = gridspec.GridSpec(1,1)
    pad   = fig.add_subplot(frame[0])

    # Creating a new Stack
    pad.hist(x=xData, bins=xBinning, weights=y3_PHI_0_weights,\
             label="$signal$", histtype="stepfilled", rwidth=1.0,\
             color="#5954d8", edgecolor="#5954d8", linewidth=1, linestyle="solid",\
             bottom=None, cumulative=False, normed=False, align="mid", orientation="vertical")


    # Axis
    plt.rc('text',usetex=False)
    plt.xlabel(r"\phi [ j_{1} ] ",\
               fontsize=16,color="black")
    plt.ylabel(r"$\mathrm{Events}$ $(\mathcal{L}_{\mathrm{int}} = 40.0\ \mathrm{fb}^{-1})$ ",\
               fontsize=16,color="black")

    # Boundary of y-axis
    ymax=(y3_PHI_0_weights).max()*1.1
    ymin=0 # linear scale
    #ymin=min([x for x in (y3_PHI_0_weights) if x])/100. # log scale
    plt.gca().set_ylim(ymin,ymax)

    # Log/Linear scale for X-axis
    plt.gca().set_xscale("linear")
    #plt.gca().set_xscale("log",nonposx="clip")

    # Log/Linear scale for Y-axis
    plt.gca().set_yscale("linear")
    #plt.gca().set_yscale("log",nonposy="clip")

    # Saving the image
    plt.savefig('../../HTML/MadAnalysis5job_0/selection_2.png')
    plt.savefig('../../PDF/MadAnalysis5job_0/selection_2.png')
    plt.savefig('../../DVI/MadAnalysis5job_0/selection_2.eps')

# Running!
if __name__ == '__main__':
    selection_2()
