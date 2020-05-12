def selection_0():

    # Library import
    import numpy
    import matplotlib
    import matplotlib.pyplot   as plt
    import matplotlib.gridspec as gridspec

    # Library version
    matplotlib_version = matplotlib.__version__
    numpy_version      = numpy.__version__

    # Histo binning
    xBinning = numpy.linspace(0.0,2000.0,201,endpoint=True)

    # Creating data sequence: middle of each bin
    xData = numpy.array([5.0,15.0,25.0,35.0,45.0,55.0,65.0,75.0,85.0,95.0,105.0,115.0,125.0,135.0,145.0,155.0,165.0,175.0,185.0,195.0,205.0,215.0,225.0,235.0,245.0,255.0,265.0,275.0,285.0,295.0,305.0,315.0,325.0,335.0,345.0,355.0,365.0,375.0,385.0,395.0,405.0,415.0,425.0,435.0,445.0,455.0,465.0,475.0,485.0,495.0,505.0,515.0,525.0,535.0,545.0,555.0,565.0,575.0,585.0,595.0,605.0,615.0,625.0,635.0,645.0,655.0,665.0,675.0,685.0,695.0,705.0,715.0,725.0,735.0,745.0,755.0,765.0,775.0,785.0,795.0,805.0,815.0,825.0,835.0,845.0,855.0,865.0,875.0,885.0,895.0,905.0,915.0,925.0,935.0,945.0,955.0,965.0,975.0,985.0,995.0,1005.0,1015.0,1025.0,1035.0,1045.0,1055.0,1065.0,1075.0,1085.0,1095.0,1105.0,1115.0,1125.0,1135.0,1145.0,1155.0,1165.0,1175.0,1185.0,1195.0,1205.0,1215.0,1225.0,1235.0,1245.0,1255.0,1265.0,1275.0,1285.0,1295.0,1305.0,1315.0,1325.0,1335.0,1345.0,1355.0,1365.0,1375.0,1385.0,1395.0,1405.0,1415.0,1425.0,1435.0,1445.0,1455.0,1465.0,1475.0,1485.0,1495.0,1505.0,1515.0,1525.0,1535.0,1545.0,1555.0,1565.0,1575.0,1585.0,1595.0,1605.0,1615.0,1625.0,1635.0,1645.0,1655.0,1665.0,1675.0,1685.0,1695.0,1705.0,1715.0,1725.0,1735.0,1745.0,1755.0,1765.0,1775.0,1785.0,1795.0,1805.0,1815.0,1825.0,1835.0,1845.0,1855.0,1865.0,1875.0,1885.0,1895.0,1905.0,1915.0,1925.0,1935.0,1945.0,1955.0,1965.0,1975.0,1985.0,1995.0])

    # Creating weights for histo: y1_PT_0
    y1_PT_0_weights = numpy.array([0.0,0.0,10.7777003493,30.8465249998,31.2181690118,36.4211971804,42.3675213732,46.0839614936,49.8004016141,52.0302816863,53.5168417345,58.7198819031,60.2064819513,56.8616818429,59.8348419393,60.5781219634,68.0110022043,59.8348419393,63.9229220718,63.5512820597,63.1796420477,58.3482418911,66.152802144,68.0110022043,59.4631619272,51.6586416743,62.8080020356,63.5512820597,57.604961867,50.5437216381,55.0034417827,61.3214019875,49.428761602,56.4900018309,58.7198819031,52.0302816863,61.6930419995,49.428761602,55.0034417827,57.233321855,50.5437216381,47.5705615418,41.9958813611,52.4019216984,46.0839614936,39.0227092647,39.3943572768,35.6779091563,45.7123214816,43.4824414093,45.3406814695,37.5361332166,39.0227092647,35.6779091563,30.8465249998,35.6779091563,30.8465249998,25.6434968311,40.880921325,28.2450089154,28.9883009395,29.3599449516,27.1300768793,25.6434968311,25.2718528191,27.1300768793,21.1837566866,25.2718528191,22.2986927227,17.0956645541,21.5554006986,21.5554006986,16.724020542,17.4673085661,17.0956645541,17.8389525782,20.0688246504,14.8657964818,21.1837566866,17.0956645541,13.3792164336,11.1493443614,14.1225044577,14.1225044577,12.6359244095,15.9807285179,12.2642803975,10.4060563373,10.7777003493,11.5209923734,9.29112030113,7.80454025295,7.80454025295,9.66276831318,8.91947628908,9.66276831318,9.66276831318,5.94631619272,6.31796420477,7.06125222886,5.20302816863,7.4328962409,8.91947628908,6.31796420477,6.68960821681,6.31796420477,6.68960821681,8.91947628908,5.94631619272,3.34480370841,5.94631619272,4.83138415659,4.0880921325,5.20302816863,3.71644852045,4.45974014454,4.45974014454,7.06125222886,5.94631619272,4.0880921325,3.71644852045,3.34480370841,2.60151408432,4.0880921325,2.60151408432,2.22986927227,2.60151408432,1.48657964818,4.45974014454,2.60151408432,2.22986927227,1.85822446023,1.11493443614,2.60151408432,2.97315889636,2.22986927227,1.48657964818,1.85822446023,1.11493443614,3.71644852045,1.11493443614,2.97315889636,1.48657964818,1.85822446023,2.22986927227,1.48657964818,1.85822446023,0.74328962409,0.74328962409,2.22986927227,1.11493443614,1.11493443614,1.11493443614,2.97315889636,0.74328962409,0.371644852045,0.74328962409,0.371644852045,1.11493443614,0.74328962409,1.48657964818,0.74328962409,1.48657964818,0.74328962409,0.371644852045,0.74328962409,0.371644852045,0.371644852045,1.11493443614,1.11493443614,0.74328962409,0.371644852045,0.371644852045,1.85822446023,0.0,0.371644852045,0.371644852045,0.0,0.0,0.0,0.74328962409,0.0,0.371644852045,0.371644852045,0.371644852045,0.0,0.74328962409,0.371644852045,0.371644852045,0.0,0.371644852045,0.74328962409,0.74328962409,0.0,0.0,0.371644852045,0.0,0.371644852045,0.74328962409,0.0])

    # Creating a new Canvas
    fig   = plt.figure(figsize=(8,6),dpi=80)
    frame = gridspec.GridSpec(1,1)
    pad   = fig.add_subplot(frame[0])

    # Creating a new Stack
    pad.hist(x=xData, bins=xBinning, weights=y1_PT_0_weights,\
             label="$signal$", histtype="stepfilled", rwidth=1.0,\
             color="#5954d8", edgecolor="#5954d8", linewidth=1, linestyle="solid",\
             bottom=None, cumulative=False, normed=False, align="mid", orientation="vertical")


    # Axis
    plt.rc('text',usetex=False)
    plt.xlabel(r"p_{T} [ j_{1} ]   ( GeV ) ",\
               fontsize=16,color="black")
    plt.ylabel(r"$\mathrm{Events}$ $(\mathcal{L}_{\mathrm{int}} = 40.0\ \mathrm{fb}^{-1})$ ",\
               fontsize=16,color="black")

    # Boundary of y-axis
    ymax=(y1_PT_0_weights).max()*1.1
    ymin=0 # linear scale
    #ymin=min([x for x in (y1_PT_0_weights) if x])/100. # log scale
    plt.gca().set_ylim(ymin,ymax)

    # Log/Linear scale for X-axis
    plt.gca().set_xscale("linear")
    #plt.gca().set_xscale("log",nonposx="clip")

    # Log/Linear scale for Y-axis
    plt.gca().set_yscale("linear")
    #plt.gca().set_yscale("log",nonposy="clip")

    # Saving the image
    plt.savefig('../../HTML/MadAnalysis5job_0/selection_0.png')
    plt.savefig('../../PDF/MadAnalysis5job_0/selection_0.png')
    plt.savefig('../../DVI/MadAnalysis5job_0/selection_0.eps')

# Running!
if __name__ == '__main__':
    selection_0()
