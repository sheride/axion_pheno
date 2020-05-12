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
    y6_PHI_0_weights = numpy.array([15.3910857629,36.9518534351,37.3577721805,37.1142345247,37.300492482,37.2157901629,36.7033109511,37.3788588167,37.0395218745,37.0523417498,37.0468932028,36.9444661169,36.8012888568,36.7400676562,37.0068665701,36.5754639753,37.2020948424,36.5804688034,37.0703263519,36.9986557737,36.8273643312,37.2402666507,37.0405532208,36.8457686673,36.8382734175,36.70583735,37.212004562,37.1171206955,37.1538094437,36.8892611036,36.9903330483,37.0237838486,36.4770023762,36.7267840748,36.8895249364,36.8684143154,37.2094861581,36.4531894678,36.67983383,36.9980481588,36.7996938676,36.8982713932,36.9846806306,36.7642843087,37.2603059506,37.2567002358,36.7192528478,37.060568536,36.9286561366,37.3161385662,36.7192488503,36.7635567698,37.0675081379,36.6637680118,36.7962520489,37.0986164228,36.9796318303,36.9368869203,36.8219717488,36.8703650791,37.0931199062,37.4858110348,36.8196452232,15.3470296838])

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
