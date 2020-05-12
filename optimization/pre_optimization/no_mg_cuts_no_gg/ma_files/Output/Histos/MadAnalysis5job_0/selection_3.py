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
    y4_PT_0_weights = numpy.array([0.0,0.0,289.77663575,237.872529674,201.147004261,174.14383736,154.194999819,135.946484709,120.303318475,106.854041875,94.346488464,82.8104793424,72.7969053864,64.5072788888,57.3839532548,50.061034112,45.1329972266,40.2588062167,35.5449775781,32.1099824861,28.5592807226,25.4033727609,23.0516311634,20.5737734912,18.4144899246,17.0023848379,15.318807795,13.9491717938,13.0869382293,11.8170630053,10.8606811068,9.72972184561,9.04914115964,8.3945639941,7.71658965637,6.95693108556,6.26068832534,5.71224389879,5.15033200717,4.90196540805,4.51191659921,4.27048960216,3.98457759722,3.76871439926,3.22976315646,3.32504717078,2.80981369698,2.67979769386,2.44770638038,2.36173606356,2.01554545984,2.02247506824,1.80423617586,1.61860581802,1.50464404063,1.47908983546,1.32370271114,1.33285770921,1.19810111042,1.07034207696,1.0679831719,0.945035889025,0.861384102856,0.759305594514,0.763972237057,0.685055849856,0.696549765654,0.708279531983,0.60846279026,0.566639695403,0.54331008041,0.476007533006,0.496922678155,0.427295603907,0.348281478647,0.424987066929,0.359879848248,0.327454437663,0.338967661224,0.269395712041,0.290315134479,0.234563826545,0.239200887834,0.197349850685,0.248417486869,0.195107951475,0.174125648887,0.164922681214,0.160197036064,0.160215304487,0.155572886592,0.130014004384,0.125342564882,0.123060251284,0.125415918394,0.0998356497401,0.109182646136,0.10221050469,0.0998554371999,0.0882397185937])

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
