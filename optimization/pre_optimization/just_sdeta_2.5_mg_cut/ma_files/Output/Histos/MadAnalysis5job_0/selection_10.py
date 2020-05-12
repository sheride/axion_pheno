def selection_10():

    # Library import
    import numpy
    import matplotlib
    import matplotlib.pyplot   as plt
    import matplotlib.gridspec as gridspec

    # Library version
    matplotlib_version = matplotlib.__version__
    numpy_version      = numpy.__version__

    # Histo binning
    xBinning = numpy.linspace(0.0,2000.0,81,endpoint=True)

    # Creating data sequence: middle of each bin
    xData = numpy.array([12.5,37.5,62.5,87.5,112.5,137.5,162.5,187.5,212.5,237.5,262.5,287.5,312.5,337.5,362.5,387.5,412.5,437.5,462.5,487.5,512.5,537.5,562.5,587.5,612.5,637.5,662.5,687.5,712.5,737.5,762.5,787.5,812.5,837.5,862.5,887.5,912.5,937.5,962.5,987.5,1012.5,1037.5,1062.5,1087.5,1112.5,1137.5,1162.5,1187.5,1212.5,1237.5,1262.5,1287.5,1312.5,1337.5,1362.5,1387.5,1412.5,1437.5,1462.5,1487.5,1512.5,1537.5,1562.5,1587.5,1612.5,1637.5,1662.5,1687.5,1712.5,1737.5,1762.5,1787.5,1812.5,1837.5,1862.5,1887.5,1912.5,1937.5,1962.5,1987.5])

    # Creating weights for histo: y11_PT_0
    y11_PT_0_weights = numpy.array([1.48657968142,15.9807288752,33.8196818522,46.0839625239,56.8616831142,74.7006040912,82.5051645186,103.688925679,115.95320635,113.723326228,128.589127042,122.271166696,118.554726493,124.872686839,122.271166696,119.298006534,119.669646554,117.439766432,121.156246635,115.20992631,110.006886025,104.80384574,101.087405536,89.194764885,106.290445821,87.7082048036,69.8692438266,86.9648847628,78.4170842947,73.5856840301,60.9497633381,59.0915232363,61.6930433788,64.2945635212,48.6854826664,43.8540824018,44.9690424628,45.3406824832,41.2525622593,36.0495539743,36.0495539743,28.2450095469,27.1300774858,19.3255330584,28.6166535673,22.2986932212,21.5554011805,23.7852733027,18.9538890381,16.7240209159,14.1225047735,11.8926366513,13.3792167327,14.1225047735,11.1493446106,9.66276852921,11.520992631,10.0344125496,9.29112050885,10.4060565699,6.31796434602,6.68960836637,5.57467230531,4.8313842646,4.8313842646,2.60151414248,4.08809222389,2.60151414248,5.94631632566,2.97315896283,3.71644860354,3.71644860354,2.97315896283,2.60151414248,1.85822450177,3.71644860354,0.743289640708,2.60151414248,1.48657968142,1.48657968142])

    # Creating a new Canvas
    fig   = plt.figure(figsize=(8,6),dpi=80)
    frame = gridspec.GridSpec(1,1)
    pad   = fig.add_subplot(frame[0])

    # Creating a new Stack
    pad.hist(x=xData, bins=xBinning, weights=y11_PT_0_weights,\
             label="$signal$", histtype="stepfilled", rwidth=1.0,\
             color="#5954d8", edgecolor="#5954d8", linewidth=1, linestyle="solid",\
             bottom=None, cumulative=False, normed=False, align="mid", orientation="vertical")


    # Axis
    plt.rc('text',usetex=False)
    plt.xlabel(r"p_{T} [ a_{1} ] ",\
               fontsize=16,color="black")
    plt.ylabel(r"$\mathrm{Events}$ $(\mathcal{L}_{\mathrm{int}} = 40.0\ \mathrm{fb}^{-1})$ ",\
               fontsize=16,color="black")

    # Boundary of y-axis
    ymax=(y11_PT_0_weights).max()*1.1
    ymin=0 # linear scale
    #ymin=min([x for x in (y11_PT_0_weights) if x])/100. # log scale
    plt.gca().set_ylim(ymin,ymax)

    # Log/Linear scale for X-axis
    plt.gca().set_xscale("linear")
    #plt.gca().set_xscale("log",nonposx="clip")

    # Log/Linear scale for Y-axis
    plt.gca().set_yscale("linear")
    #plt.gca().set_yscale("log",nonposy="clip")

    # Saving the image
    plt.savefig('../../HTML/MadAnalysis5job_0/selection_10.png')
    plt.savefig('../../PDF/MadAnalysis5job_0/selection_10.png')
    plt.savefig('../../DVI/MadAnalysis5job_0/selection_10.eps')

# Running!
if __name__ == '__main__':
    selection_10()
