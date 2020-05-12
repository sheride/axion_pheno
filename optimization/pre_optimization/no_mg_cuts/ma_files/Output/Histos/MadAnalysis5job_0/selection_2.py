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
    y3_PHI_0_weights = numpy.array([257.809615257,569.067633677,474.746828095,528.195231258,474.746828095,493.611229211,455.882826978,493.611229211,493.611229211,547.059232374,550.20323256,512.475230328,443.306826234,512.475230328,443.306826234,509.331230141,477.890828281,465.314827537,512.475230328,493.611229211,490.467229025,462.170827351,525.051231072,499.899229583,477.890828281,474.746828095,521.907230886,506.187229955,540.771232002,493.611229211,503.043229769,531.339231444,525.051231072,550.20323256,474.746828095,509.331230141,515.619230514,474.746828095,474.746828095,553.347632746,503.043229769,531.339231444,503.043229769,484.178828653,562.779633304,493.611229211,521.907230886,446.45082642,515.619230514,452.738826792,440.162826048,449.594826606,462.170827351,512.475230328,452.738826792,459.026827165,503.043229769,534.48323163,462.170827351,531.339231444,427.586825304,556.491632932,600.507635537,216.937332838])

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
