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
    y4_PT_0_weights = numpy.array([0.0,0.0,53667.0718078,42283.1535455,34964.9186627,23174.4204625,22361.2845866,17482.4573313,18295.5972072,17889.0292693,13010.202014,14636.4777658,12197.0661381,12197.0661381,9351.08257257,12603.6340761,9757.65051051,6911.67094494,6911.67094494,5691.96313113,5691.96313113,6911.67094494,4472.25531732,6505.09900701,3252.5503035,3659.11944144,3252.5503035,2032.84408969,2032.84408969,1219.70661381,2439.41282763,1626.27535175,2439.41282763,2439.41282763,2439.41282763,2032.84408969,1626.27535175,2032.84408969,1219.70661381,813.137475876,1219.70661381,2439.41282763,1626.27535175,1219.70661381,1219.70661381,0.0,406.568737938,406.568737938,406.568737938,406.568737938,0.0,813.137475876,406.568737938,813.137475876,406.568737938,0.0,0.0,813.137475876,0.0,0.0,406.568737938,0.0,0.0,406.568737938,0.0,0.0,0.0,0.0,0.0,0.0,406.568737938,0.0,406.568737938,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,406.568737938,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0])

    # Creating weights for histo: y4_PT_1
    y4_PT_1_weights = numpy.array([0.0,0.0,3123.11785289,1277.63889437,1703.51852582,567.839508607,283.919809859,567.839508607,283.919809859,141.959877152,283.919809859,425.879687011,425.879687011,0.0,0.0,141.959877152,141.959877152,0.0,0.0,0.0,141.959877152,0.0,141.959877152,0.0,0.0,141.959877152,0.0,141.959877152,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,141.959877152,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0])

    # Creating a new Canvas
    fig   = plt.figure(figsize=(12,6),dpi=80)
    frame = gridspec.GridSpec(1,1,right=0.7)
    pad   = fig.add_subplot(frame[0])

    # Creating a new Stack
    pad.hist(x=xData, bins=xBinning, weights=y4_PT_0_weights+y4_PT_1_weights,\
             label="$signal4TeV$", histtype="stepfilled", rwidth=1.0,\
             color="#ce5e60", edgecolor="#ce5e60", linewidth=1, linestyle="solid",\
             bottom=None, cumulative=False, normed=False, align="mid", orientation="vertical")

    pad.hist(x=xData, bins=xBinning, weights=y4_PT_0_weights,\
             label="$signal1TeV$", histtype="stepfilled", rwidth=1.0,\
             color="#5954d8", edgecolor="#5954d8", linewidth=1, linestyle="solid",\
             bottom=None, cumulative=False, normed=False, align="mid", orientation="vertical")


    # Axis
    plt.rc('text',usetex=False)
    plt.xlabel(r"p_{T} [ j_{2} ]   ( GeV ) ",\
               fontsize=16,color="black")
    plt.ylabel(r"$\mathrm{Events}$ $(\mathcal{L}_{\mathrm{int}} = 40.0\ \mathrm{fb}^{-1})$ ",\
               fontsize=16,color="black")

    # Boundary of y-axis
    ymax=(y4_PT_0_weights+y4_PT_1_weights).max()*1.1
    ymin=0 # linear scale
    #ymin=min([x for x in (y4_PT_0_weights+y4_PT_1_weights) if x])/100. # log scale
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
    plt.savefig('../../HTML/MadAnalysis5job_0/selection_3.png')
    plt.savefig('../../PDF/MadAnalysis5job_0/selection_3.png')
    plt.savefig('../../DVI/MadAnalysis5job_0/selection_3.eps')

# Running!
if __name__ == '__main__':
    selection_3()
