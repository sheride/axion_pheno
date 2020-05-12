def selection_3():

    # Library import
    import numpy
    import matplotlib
    import matplotlib.pyplot   as plt
    import matplotlib.gridspec as gridspec

    # Library version
    matplotlib_version = matplotlib.__version__
    numpy_version      = numpy.__version__

    # Histo binning
    xBinning = numpy.linspace(0.0,1000.0,101,endpoint=True)

    # Creating data sequence: middle of each bin
    xData = numpy.array([5.0,15.0,25.0,35.0,45.0,55.0,65.0,75.0,85.0,95.0,105.0,115.0,125.0,135.0,145.0,155.0,165.0,175.0,185.0,195.0,205.0,215.0,225.0,235.0,245.0,255.0,265.0,275.0,285.0,295.0,305.0,315.0,325.0,335.0,345.0,355.0,365.0,375.0,385.0,395.0,405.0,415.0,425.0,435.0,445.0,455.0,465.0,475.0,485.0,495.0,505.0,515.0,525.0,535.0,545.0,555.0,565.0,575.0,585.0,595.0,605.0,615.0,625.0,635.0,645.0,655.0,665.0,675.0,685.0,695.0,705.0,715.0,725.0,735.0,745.0,755.0,765.0,775.0,785.0,795.0,805.0,815.0,825.0,835.0,845.0,855.0,865.0,875.0,885.0,895.0,905.0,915.0,925.0,935.0,945.0,955.0,965.0,975.0,985.0,995.0])

    # Creating weights for histo: y4_PT_0
    y4_PT_0_weights = numpy.array([0.0,0.0,666.532051402,738.844456979,716.836455282,792.292861101,609.939647038,779.716860131,754.564858191,701.11645407,672.820051887,726.268456009,773.428859646,638.23604922,628.804048493,710.548454797,616.227647523,609.939647038,647.668049948,635.092048978,625.66004825,515.619239764,644.524049705,613.083647281,531.339240976,509.331239279,465.314835885,553.347642674,597.363646068,484.178837339,493.611238067,443.306834187,446.45083443,449.594834672,493.611238067,405.578431278,320.689984731,374.138348853,355.274227398,399.290470793,370.994308611,292.393822549,308.113903761,298.681863034,282.961781822,292.393822549,333.266065701,304.969903519,251.521579397,257.809619882,270.385700852,223.225377215,160.345012366,232.657457942,201.217255518,198.073255275,179.20913382,185.497174305,198.073255275,179.20913382,185.497174305,172.921093336,182.353134063,141.480890911,116.328728971,116.328728971,182.353134063,116.328728971,138.336850668,94.3206072739,116.328728971,110.040688486,110.040688486,78.6004860616,94.3206072739,100.608607759,100.608607759,100.608607759,110.040688486,81.7445263041,81.7445263041,94.3206072739,72.3124455767,69.1684453342,75.4564858191,69.1684453342,40.872243152,56.5923643644,56.5923643644,47.160283637,50.3043238794,15.7200972123,56.5923643644,31.4401944246,53.4483241219,50.3043238794,28.2961781822,22.0081376972,40.872243152,25.1521579397])

    # Creating a new Canvas
    fig   = plt.figure(figsize=(8,6),dpi=80)
    frame = gridspec.GridSpec(1,1)
    pad   = fig.add_subplot(frame[0])

    # Creating a new Stack
    pad.hist(x=xData, bins=xBinning, weights=y4_PT_0_weights,\
             label="$signal$", histtype="stepfilled", rwidth=1.0,\
             color="#5954d8", edgecolor="#5954d8", linewidth=1, linestyle="solid",\
             bottom=None, cumulative=False, normed=False, align="mid", orientation="vertical")


    # Axis
    plt.rc('text',usetex=False)
    plt.xlabel(r"p_{T} [ j_{2} ]   ( GeV ) ",\
               fontsize=16,color="black")
    plt.ylabel(r"$\mathrm{Events}$ $(\mathcal{L}_{\mathrm{int}} = 40.0\ \mathrm{fb}^{-1})$ ",\
               fontsize=16,color="black")

    # Boundary of y-axis
    ymax=(y4_PT_0_weights).max()*1.1
    ymin=0 # linear scale
    #ymin=min([x for x in (y4_PT_0_weights) if x])/100. # log scale
    plt.gca().set_ylim(ymin,ymax)

    # Log/Linear scale for X-axis
    plt.gca().set_xscale("linear")
    #plt.gca().set_xscale("log",nonposx="clip")

    # Log/Linear scale for Y-axis
    plt.gca().set_yscale("linear")
    #plt.gca().set_yscale("log",nonposy="clip")

    # Saving the image
    plt.savefig('../../HTML/MadAnalysis5job_0/selection_3.png')
    plt.savefig('../../PDF/MadAnalysis5job_0/selection_3.png')
    plt.savefig('../../DVI/MadAnalysis5job_0/selection_3.eps')

# Running!
if __name__ == '__main__':
    selection_3()
