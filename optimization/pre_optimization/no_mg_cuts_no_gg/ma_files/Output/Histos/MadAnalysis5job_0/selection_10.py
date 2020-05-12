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
    y11_PT_0_weights = numpy.array([3.9429591079,21.008505637,38.5109452805,52.4016698866,62.7317630806,70.2628301871,75.2544267099,78.2856656301,80.6983365744,80.7519825757,80.9702042753,80.6252628856,77.842026791,76.4049375615,74.530165718,71.1247239528,68.4662088149,65.3787655148,63.1495782858,60.1743438722,57.6857210632,54.5605416788,51.9945279172,49.9076504978,46.9455677492,44.7397257249,42.610235312,39.8179689404,38.5244886972,36.3504745017,34.1063687275,32.1769395237,30.289647615,28.7622476209,27.3358516145,24.9303601202,24.0083964245,22.3503792104,21.4835325837,20.4929803566,18.8507171583,18.2101910985,17.1741317121,16.3387811244,15.2447105032,14.371519897,13.182389521,12.2113968979,11.5896069638,11.1949930546,10.7675679398,9.66916406485,9.30667779436,8.81012848775,8.143411027,7.50044651257,6.98951831873,6.56941656267,6.36030908674,6.14664050147,5.53382487986,5.31982450487,4.66493954515,4.58857993886,4.08941229164,3.92673938732,3.85231455484,3.63646775004,3.35096029342,2.92599601903,2.9537772124,2.6239610369,2.38934772557,2.2709987305,2.13854347542,2.08061978517,1.80429530874,1.73685285111,1.62319888052,1.49313051272])

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
