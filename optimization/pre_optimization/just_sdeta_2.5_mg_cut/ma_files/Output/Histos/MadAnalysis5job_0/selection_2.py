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
    y3_PHI_0_weights = numpy.array([23.0419811851,60.9497631347,59.4631630582,55.0034428289,64.2945633067,63.1796432494,59.4631630582,65.0378433449,65.0378433449,53.8885227715,60.2064830965,66.5244434214,53.1452027333,58.71988302,55.375082848,57.9766029818,59.0915230391,70.9841636508,60.2064830965,62.064683192,55.0034428289,55.0034428289,59.8348430773,61.3214031538,59.0915230391,53.8885227715,63.5512832685,60.9497631347,57.2333229435,52.7735627142,52.4019226951,63.1796432494,60.9497631347,56.8616829244,58.3482430009,61.6930431729,52.0302826759,56.4900029053,56.8616829244,60.9497631347,52.7735627142,62.4363232111,59.8348430773,60.5781231156,63.1796432494,55.7467228671,61.6930431729,55.7467228671,57.2333229435,59.8348430773,60.9497631347,58.71988302,60.5781231156,61.6930431729,61.6930431729,62.064683192,66.1528034023,55.7467228671,56.4900029053,61.3214031538,49.4287625421,56.8616829244,59.8348430773,23.4136252042])

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
