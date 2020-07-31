def selection_1():

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

    # Creating weights for histo: y2_P_0
    y2_P_0_weights = numpy.array([0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,3.83713442454,3.83713442454,0.0,3.83713442454,0.0,3.83713442454,0.0,11.5114040736,0.0,0.0,7.67426804909,0.0,7.67426804909,7.67426804909,3.83713442454,3.83713442454,3.83713442454,7.67426804909,19.1856721227,26.8599401718,7.67426804909,7.67426804909,11.5114040736,19.1856721227,15.3485360982,23.0228041473,11.5114040736,19.1856721227,19.1856721227,19.1856721227,15.3485360982,23.0228041473,7.67426804909,7.67426804909,23.0228041473,11.5114040736,7.67426804909,11.5114040736,38.3713442454,19.1856721227,23.0228041473,19.1856721227,19.1856721227,19.1856721227,7.67426804909,15.3485360982,34.5342082209,15.3485360982,15.3485360982,15.3485360982,19.1856721227,7.67426804909,11.5114040736,26.8599401718,19.1856721227,11.5114040736,19.1856721227,23.0228041473,30.6970721964,19.1856721227,23.0228041473,15.3485360982,23.0228041473,11.5114040736,15.3485360982,11.5114040736,19.1856721227,3.83713442454,23.0228041473,23.0228041473,11.5114040736,19.1856721227,46.0456002945,15.3485360982,11.5114040736,19.1856721227,26.8599401718,19.1856721227,15.3485360982,26.8599401718,15.3485360982,23.0228041473,11.5114040736,11.5114040736,11.5114040736,26.8599401718,30.6970721964,15.3485360982,11.5114040736,19.1856721227,7.67426804909,19.1856721227])

    # Creating a new Canvas
    fig   = plt.figure(figsize=(8,6),dpi=80)
    frame = gridspec.GridSpec(1,1)
    pad   = fig.add_subplot(frame[0])

    # Creating a new Stack
    pad.hist(x=xData, bins=xBinning, weights=y2_P_0_weights,\
             label="$signal$", histtype="stepfilled", rwidth=1.0,\
             color="#5954d8", edgecolor="#5954d8", linewidth=1, linestyle="solid",\
             bottom=None, cumulative=False, normed=False, align="mid", orientation="vertical")


    # Axis
    plt.rc('text',usetex=False)
    plt.xlabel(r"$p$ $[ a_{1} a_{2} ]$ $(GeV/c)$ ",\
               fontsize=16,color="black")
    plt.ylabel(r"$\mathrm{Events}$ $(\mathcal{L}_{\mathrm{int}} = 40.0\ \mathrm{fb}^{-1})$ ",\
               fontsize=16,color="black")

    # Boundary of y-axis
    ymax=(y2_P_0_weights).max()*1.1
    ymin=0 # linear scale
    #ymin=min([x for x in (y2_P_0_weights) if x])/100. # log scale
    plt.gca().set_ylim(ymin,ymax)

    # Log/Linear scale for X-axis
    plt.gca().set_xscale("linear")
    #plt.gca().set_xscale("log",nonposx="clip")

    # Log/Linear scale for Y-axis
    plt.gca().set_yscale("linear")
    #plt.gca().set_yscale("log",nonposy="clip")

    # Saving the image
    plt.savefig('../../HTML/MadAnalysis5job_0/selection_1.png')
    plt.savefig('../../PDF/MadAnalysis5job_0/selection_1.png')
    plt.savefig('../../DVI/MadAnalysis5job_0/selection_1.eps')

# Running!
if __name__ == '__main__':
    selection_1()
