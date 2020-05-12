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
    y11_PT_0_weights = numpy.array([9.43206096502,47.1602848251,144.624894797,210.649301552,308.113911524,389.858439887,471.602848251,518.763253076,707.404472376,660.244067551,867.749288782,836.309285565,858.317287816,880.325690068,899.189691998,789.14888074,908.621692963,852.029287173,870.893289103,848.885286851,852.029287173,861.461288138,804.868882348,767.140878488,741.988475915,770.28487881,792.292881061,754.564877201,707.404472376,691.684470768,644.524065943,669.676068516,591.075660474,616.227663048,556.491656936,471.602848251,468.458847929,459.026846964,503.043251468,396.146480531,440.162845034,405.578441496,320.689992811,348.986195706,286.105789272,364.706277314,286.105789272,254.665586055,267.241667342,279.817748629,204.361260909,188.6411793,169.77705737,172.921097692,141.480894475,150.91293544,188.6411793,100.608610294,116.328731902,106.896650937,100.608610294,119.472732224,97.4646099718,81.7445283635,91.1765693285,78.6004880418,62.8804064334,59.7363661118,72.3124473985,81.7445283635,40.8722441817,25.1521585734,50.3043251468,50.3043251468,25.1521585734,37.7282358601,28.296178895,34.5842155384,28.296178895,18.86411793])

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
