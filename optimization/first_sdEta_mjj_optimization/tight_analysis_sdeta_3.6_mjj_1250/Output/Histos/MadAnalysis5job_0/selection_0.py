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
    y1_PT_0_weights = numpy.array([0.0,0.0,2.49739105176,6.51778239346,8.020309101,8.85140838609,10.0878233225,10.1451392732,11.0458384985,11.6558579737,12.0079496709,12.8513289454,12.9618688503,13.6210162833,14.5176235121,14.3170116846,14.9474991423,15.0948870155,15.1726749486,15.6721545189,16.2494180224,16.5073458005,16.974073399,16.7693695751,17.0109173673,16.5360057759,16.511441797,16.4500298498,15.9546462759,15.5206706492,15.5247666457,14.8328672409,14.4603035614,14.0713678959,13.7029002129,13.40403247,13.0028088151,12.4787692659,11.9629137096,11.700893935,11.3447062414,11.221882347,10.194267231,10.1287632873,9.88311949862,9.50236782614,8.98651626987,8.47884870656,8.19635694956,7.79922929117,7.87701722425,7.58633747429,7.17692982646,7.0950458969,6.65288627724,6.42361847446,6.00602283367,6.14931471041,5.76856303793,5.47379129149,5.30593143588,5.14626357323,4.91699577044,4.80645586553,4.55262008387,4.29060030926,4.15549642548,3.9999201593,3.84025069665,3.87300346847,3.79112193891,3.50453578543,3.18110326364,3.06646896225,3.24660840729,3.05828056929,2.93136427846,2.80854158412,2.53833221655,2.41960351868,2.41141552572,2.49739105176,2.30496921728,2.20261730533,2.31315761024,2.12892376872,1.8873727765,1.96516030959,1.76045608567,1.66219817019,1.56803425119,1.71132692793,1.56803425119,1.52709348641,1.62944539836,1.37561201671,1.46568193923,1.26916610827,1.15453180688,1.36742402375,1.25688371884,1.13406142449,1.08902626323,1.12587303153,0.962109572401,0.925262804096,0.970297965358,0.880228042835,0.908886818183,0.814722899182,0.945733586488,0.683712211876,0.720558580181,0.667335825963,0.687806208355,0.671429822442,0.524042749223,0.65095944005,0.605924278789,0.618206668224,0.552701524571,0.577265903441,0.48310198444,0.548607128093,0.405314451352,0.474913591483,0.442161219657,0.442161219657,0.438066823178,0.466725598526,0.282491797003,0.302962219394,0.380749792482,0.298868142916,0.347997140656,0.327526718264,0.245645028698,0.294774026438,0.262021374611,0.225174606307,0.286585873481,0.286585873481,0.26611545109,0.204704183915,0.184233761524,0.237456875742,0.180139685045,0.19242195448,0.212892376872,0.208798300393,0.122822534349,0.159669262654,0.122822534349,0.176045608567,0.155575186175,0.19242195448,0.139198840262,0.139198840262,0.159669262654,0.118728417871,0.139198840262,0.126916610827,0.102352111958,0.0900698425227,0.114634341392,0.122822534349,0.110540264914,0.094163919001,0.0695994201311,0.126916610827,0.0695994201311,0.102352111958,0.0573171906962,0.0982579954793,0.0736934966095,0.0655053436528,0.0736934966095,0.0655053436528,0.0777876130877,0.0614112671745,0.0573171906962,0.0614112671745,0.0573171906962,0.0736934966095,0.0450349212613,0.0327526718264,0.0204704183915,0.040940844783,0.0573171906962,0.0491289977396,0.0532230742179,0.0450349212613,0.0450349212613,0.0655053436528,0.0327526718264,0.0368467563047,0.0204704183915,0.040940844783,0.0245645028698,0.0163763339132])

    # Creating weights for histo: y1_PT_1
    y1_PT_1_weights = numpy.array([0.0,0.0,9.5003405497,37.7149885443,70.5920931415,61.5797681611,21.1302654833,3.66873894005,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0])

    # Creating weights for histo: y1_PT_2
    y1_PT_2_weights = numpy.array([0.0,0.0,0.0,0.0,0.0,50.5825011813,128.26220269,167.882067704,170.636352306,167.623770881,125.701258487,68.7232354044,36.5963707434,19.9793481162,9.81895684085,3.7548953395,1.15479588346,0.180639724236,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0])

    # Creating weights for histo: y1_PT_3
    y1_PT_3_weights = numpy.array([0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,35.6478763898,87.2796158396,113.315274884,121.594764937,117.891397271,112.168867704,102.790664649,94.0545048667,84.6723205267,77.0778147568,60.8502157557,42.4952288808,27.9357723753,20.3459263348,14.3777311219,10.1536153372,7.2218777327,5.60497194772,4.07037721517,2.9427056406,1.93018991371,1.35332719682,0.885564304424,0.638070923362,0.29142386347,0.225467851816,0.0550268134069,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0])

    # Creating weights for histo: y1_PT_4
    y1_PT_4_weights = numpy.array([0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,7.66883542744,19.4241626558,24.7357438195,26.0925539979,25.7712525294,24.1972044152,22.0542740518,20.2459086277,18.4077334627,16.4576344849,13.5336624549,10.5249909984,8.22548033117,6.59797349514,5.28058095715,4.35100765699,3.70770927958,2.93974149119,2.56092008936,2.05659835558,1.74085600091,1.37753470236,1.12404608548,0.930606239547,0.770701450263,0.66415036533,0.521088059617,0.430277976906,0.386819407015,0.295039475586,0.227961185345,0.144085865676,0.115463343695,0.0759780030194,0.0503444316505,0.0197350746059,0.00592250649118,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0])

    # Creating weights for histo: y1_PT_5
    y1_PT_5_weights = numpy.array([0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,1.09350323638,2.69113324288,3.58478789295,3.87900441046,3.86737515993,3.74536525321,3.58052404781,3.27957107908,3.08063511646,2.82141957829,2.36319485956,1.81951319387,1.45752406413,1.23015433191,1.02543415149,0.870671416486,0.791785280142,0.679559771747,0.622865074905,0.558881391407,0.532384496564,0.480200105276,0.445649636364,0.416422472285,0.3758456062,0.336037248489,0.298204695082,0.289652038679,0.239726000951,0.20570626213,0.174426354889,0.159555389761,0.130071002632,0.123511674828,0.109151354868,0.0910109083334,0.0695760942931,0.0615019151735,0.0529424571036,0.0501635759522,0.0307560588371,0.0252140724013,0.0184046913053,0.0143689540769,0.00756310184588,0.00453796433283,0.00227024927701,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0])

    # Creating weights for histo: y1_PT_6
    y1_PT_6_weights = numpy.array([0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.199296396201,0.504722410221,0.645792044119,0.747168524176,0.7621425026,0.726126940025,0.674805308176,0.653343462155,0.60874921918,0.545902575318,0.526505350706,0.486719827225,0.429775443436,0.392499595086,0.380511235363,0.335513924867,0.283706652637,0.27603697347,0.249388532154,0.24741118206,0.20416649552,0.179233690317,0.161498519429,0.134543079016,0.109354857762,0.113662541932,0.105929483597,0.089911608277,0.0879021087498,0.085288957628,0.0741654136619,0.0778742946444,0.0678630251012,0.0669770862874,0.0758690837077,0.0580964651281,0.0615457714264,0.0569493721492,0.0480979813825,0.0495145158027,0.044074963649,0.0449309323132,0.0432416875262,0.0337765384868,0.0254864232427,0.0291966437849,0.0243218160203,0.0246275155444,0.0191946511926,0.0217567890813,0.0180317434117,0.0163235748445,0.0100225558337,0.0128812062659,0.0128731589109,0.0111627910665,0.00829475871786,0.00973949686814,0.00773060214218,0.00772881273031,0.00830435556361,0.00716177310222,0.00715599900003,0.00429680674584,0.00429128656019,0.0080180946505,0.00315529793157,0.00314173938793,0.00313871038349,0.00257474874374,0.00229087304666,0.00171471941412,0.00114768878307,0.000860686513619,0.000572345184286,0.000858832423013,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0])

    # Creating weights for histo: y1_PT_7
    y1_PT_7_weights = numpy.array([0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.00920128767439,0.0248952223031,0.0328904918343,0.0360948129386,0.0377889596302,0.0397111826635,0.0368808324986,0.0365098998949,0.0324777223947,0.0314607306447,0.0275556771132,0.0258895920718,0.0220277960601,0.0224344972097,0.0197385001573,0.017988087678,0.0166505116912,0.0164516662349,0.013729078506,0.0133008366034,0.0107141358227,0.00956345310777,0.00708478297468,0.00682549349518,0.00546229490848,0.00453624369123,0.005075973658,0.0038227691125,0.0036473519491,0.00332748140693,0.00358491477758,0.00310829921689,0.00306738016794,0.00276436631264,0.00267841116499,0.00267890609941,0.00224438678563,0.00257001675518,0.00205202492839,0.00235402796081,0.00244021947003,0.0019653024438,0.00239614725716,0.002224626707,0.00222345118537,0.00222380949945,0.00190052386787,0.00209498909163,0.00207158007651,0.00246223629874,0.00259093265865,0.00237258066766,0.00233254629827,0.00243924510718,0.00272124876583,0.00261045972835,0.0027435459596,0.00308923984135,0.00250508144304,0.00250563965866,0.00200815094074,0.00207075616366,0.00239693051917,0.00181361740682,0.00177176506493,0.00220191839498,0.0013387460604,0.00157492407214,0.00118811962151,0.00116619918137,0.00120958535898,0.00103713444945,0.00129557696665,0.000928991907201,0.000647815514038,0.000820525415496,0.000927357911176,0.000626292781582,0.000453509121904,0.000518268001036,0.000626325050803,0.000496938045746,0.000367032805376,0.00040865670632,0.00054006271693,0.000408870018446,0.000389055920304,0.00015116055737,0.000237622457519,0.000172658773601,0.000194418077167,0.00015125832892,6.47314293406e-05,8.64803397032e-05,8.64321873197e-05,6.47888015016e-05,4.31127692895e-05,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0])

    # Creating weights for histo: y1_PT_8
    y1_PT_8_weights = numpy.array([0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.000736207480356,0.00149871747505,0.00178641413032,0.00269539052356,0.00286381009652,0.00192880747898,0.0019251859999,0.00260733570074,0.0023531028193,0.00235195903796,0.00240924762838,0.00169969322392,0.00161351152871,0.00133131512476,0.00093681840754,0.00113503615797,0.00116297517087,0.000908684654725,0.000823008897081,0.000567167888789,0.00070992724747,0.000596514049816,0.000537422741184,0.000850699546038,0.000511299221195,0.000653594828536,0.000454373967028,0.000255729898105,0.000340490927769,0.000283661929486,0.000283538935857,0.000226455928991,0.000227009697407,0.000112038045699,5.67880449705e-05,0.000141913762628,0.000169812015323,0.00019678549853,0.000113728049461,0.000141981795336,0.00011362224226,8.52468544983e-05,0.000142095698131,0.000113600035077,8.52799350311e-05,5.67801127727e-05,0.000226744696642,0.000113618662373,5.68012950088e-05,8.52876889773e-05,2.84403604835e-05,0.000198978884912,8.5009274776e-05,2.84600127264e-05,8.51783018899e-05,8.52575495965e-05,2.84191782474e-05,0.000167868775403,8.5299587274e-05,0.000170249474547,0.000198889907637,0.000141997823128,0.000227028859458,5.6848858487e-05,0.000113151256875,0.000170395937974,8.41957194544e-05,0.000113650138641,8.52004942186e-05,0.000253157726996,0.000113781109031,0.000113618261307,0.000142067980002,0.00025553842614,0.000198876984394,0.000169797903735,8.49522936696e-05,0.000255514362169,8.52892189705e-05,0.000198851434992,0.000142037454409,0.00025561641123,0.000198828856452,8.52787318326e-05,8.51818669226e-05,0.000170345878973,0.000142087959039,0.000197429878194,8.53603859362e-05,0.000142069004949,8.50484752816e-05,5.68791909738e-05,0.000142019391576,0.000113607967275,0.000198770181955,5.67880449705e-05,5.68395745476e-05,0.000198851434992,8.36206054048e-05,8.51965281197e-05,8.52680367344e-05,2.7011822163e-05,2.84084831492e-05,2.83795618213e-05,2.83795618213e-05,2.83609345253e-05,5.42899374161e-05,2.84600127264e-05,0.0,5.59682954046e-05,8.51622295341e-05,8.48325085701e-05,2.83609345253e-05,2.83795618213e-05,0.0,8.50738612855e-05,2.83795618213e-05,0.0,0.0,0.0])

    # Creating weights for histo: y1_PT_9
    y1_PT_9_weights = numpy.array([0.0,0.0,7.8239519814,39.0832674502,80.8249853855,67.7762210908,26.0509574466,7.819995107,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0])

    # Creating weights for histo: y1_PT_10
    y1_PT_10_weights = numpy.array([0.0,0.0,0.0,0.0,0.0,69.5296755906,112.681858675,145.352115767,174.839188861,157.97015664,136.901805511,76.8958264579,50.5570401887,32.6575448253,14.7566374154,10.5286081761,5.26311712246,2.1058786148,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0])

    # Creating weights for histo: y1_PT_11
    y1_PT_11_weights = numpy.array([0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,32.0165772446,95.5802246557,136.367038273,146.702134299,156.86701326,155.935276556,139.118983282,141.643767277,130.836828011,141.66240278,104.340716774,78.5544068546,51.8290213006,34.7805181371,23.0348567352,17.0449105459,12.2096239378,8.75328767176,9.21196310419,5.52806237647,5.06808053767,4.38032674912,3.45429097159,3.9164295336,1.61172237013,0.690556414448,0.461397368515,0.230478670056,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0])

    # Creating weights for histo: y1_PT_12
    y1_PT_12_weights = numpy.array([0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,19.1630970663,47.3514802176,61.8919782483,64.5207116886,57.8749162264,51.5583231826,48.6275868226,42.0323431867,38.1295921553,31.8728803274,28.161706868,18.1920326461,14.2045207443,10.4126259438,8.75086353386,6.95107617161,5.23327971671,6.11956787776,4.62454570404,4.37502589039,3.35083011579,3.35012492936,2.43688810522,2.13242222659,1.60556909217,1.52297264012,1.35691181425,1.13532438531,1.13549596913,1.19085483556,0.886389726362,0.913821209406,0.775295740196,0.442825919487,0.553838345628,0.221373795543,0.166023893028,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0])

    # Creating weights for histo: y1_PT_13
    y1_PT_13_weights = numpy.array([0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,2.17768872351,5.44472698287,7.29970199729,8.11591770353,7.68206265886,7.24818334155,6.77503697816,6.25080886636,5.96854670768,4.62844027919,4.36577462779,2.98437802955,2.15733673064,1.73413676342,1.38123821933,1.34074722591,0.937604339114,0.806609813185,0.755847856666,0.605001536074,0.655304557854,0.544546183672,0.63497987169,0.453707324789,0.524289339508,0.433713535245,0.615002890942,0.695674188128,0.514175845092,0.503948633409,0.574582773599,0.463785502529,0.463843574794,0.372919701027,0.302520701934,0.36282890152,0.29239761983,0.292222856899,0.201585946292,0.201653848972,0.141187634569,0.0908259337079,0.141212028561,0.0503907066531,0.100855566189,0.0402908898645,0.0705850487971,0.0100417930682,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0])

    # Creating weights for histo: y1_PT_14
    y1_PT_14_weights = numpy.array([0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.34226009762,0.930842062746,1.38347729354,1.44288851224,1.44852530647,1.45691259158,1.32689082013,1.16569989655,1.25325892105,0.961997364311,0.956220140765,0.860065303241,0.718631052964,0.642261744081,0.523360435427,0.551739083933,0.438508811179,0.461239892795,0.430068816978,0.31404384696,0.288595361915,0.248947857222,0.161337393278,0.130133614744,0.118799083807,0.116000923902,0.121678885083,0.10743131152,0.104687130335,0.0565803176017,0.0848516242479,0.0877175364877,0.110341276243,0.0763833902885,0.10186477042,0.0961818461211,0.152736232392,0.181032008365,0.130121303133,0.11318702822,0.115965604968,0.132996987714,0.13298840806,0.107498448274,0.0990039751936,0.0905538623869,0.0792151378073,0.0905407813001,0.0594158355514,0.0650461661864,0.0678981124423,0.042433853145,0.0537583424242,0.0622274997545,0.0481017726679,0.0311277120138,0.0679159258047,0.0424378544186,0.0594096027982,0.0424171170485,0.0254524170663,0.0339625566723,0.0254636937327,0.0254514860007,0.0311145847584,0.00566126740548,0.0254745587296,0.0282912668458,0.0254663753555,0.00848388124775,0.0141444676672,0.0141320714137,0.0113100077466,0.011308761196,0.00564882113605,0.0169856143317,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0])

    # Creating weights for histo: y1_PT_15
    y1_PT_15_weights = numpy.array([0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0212883637772,0.0503059717192,0.077668722758,0.0853025494078,0.092905555042,0.0716450105403,0.0745600782607,0.0731873021932,0.0883357367793,0.0669831901281,0.0396527255212,0.0457436223529,0.0563666857005,0.0365932197442,0.0334475853011,0.0349724455897,0.045697639005,0.0243695553531,0.0274337882797,0.024379600546,0.0152505173821,0.00611247745148,0.00916084842756,0.00913001559417,0.00608564615023,0.00758510864576,0.00913999697059,0.00610824547078,0.00304025091483,0.00305794818122,0.00306059538501,0.00454154281726,0.0,0.0,0.00303272056548,0.00457880102878,0.00151713730796,0.00152081266679,0.00153205973752,0.0,0.00305112926789,0.00459350600946,0.0,0.00152630679644,0.0,0.0015186819041,0.00304490597542,0.00152149219455,0.00455327914798,0.00304903041346,0.0,0.00151102037635,0.00152179118676,0.0,0.00458129578199,0.00606068325488,0.00609707048908,0.00915839976406,0.00915044278946,0.00913217708333,0.00915068151052,0.00912177262702,0.00610204699584,0.0045708428724,0.00153551882926,0.00605058015435,0.00304328219952,0.00761529385966,0.0060871600199,0.00304260385355,0.0030696313315,0.00303581921206,0.0015083601729,0.00610000132184,0.0030208778739,0.0,0.0,0.00304918168225,0.0,0.0,0.00607141033915,0.00459580340418,0.0015186819041,0.00304563513825,0.0,0.00152081266679,0.0045902088226,0.00153205973752,0.0,0.00153139320943,0.00455866809855,0.0,0.0,0.0,0.0,0.0,0.0015380762172,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0])

    # Creating weights for histo: y1_PT_16
    y1_PT_16_weights = numpy.array([0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.00144443900893,0.00451397925289,0.0046934722788,0.00577796322601,0.00343032784996,0.00541595404457,0.00415459653566,0.00361053487362,0.00288777544205,0.00415193926249,0.00415342964614,0.00324855650115,0.00379047231883,0.00343297010376,0.00198467881896,0.00198655508488,0.0036132949717,0.00144514376399,0.00252737487367,0.000903635394855,0.00072284300088,0.00090233102033,0.000542282444361,0.000722286899074,0.00108285576143,0.000541737125693,0.000901890452141,0.00072191102971,0.000903613058356,0.000180717066058,0.0,0.000361249316841,0.000360621699727,0.000180672701149,0.000541211832852,0.000180593714667,0.0,0.000180262787879,0.0,0.000361008660319,0.000181030277691,0.000180546923552,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.000180461890811,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.000180909660596,0.000180672701149,0.0,0.000181030277691,0.000361401320568,0.000542521598946,0.000540643792573,0.00090236491019,0.000722662383327,0.000180593714667,0.000361172448475,0.0010833436984,0.00126271117778,0.000360931406841,0.000902634488628,0.000180367730914,0.000722868803387,0.000180563252303,0.000180063338347,0.000180546923552,0.000360272788207,0.0,0.000180546923552,0.000361214040577,0.0,0.00036115696697,0.000180546923552,0.000361230484861,0.0,0.000362055471902,0.0,0.0,0.000180546923552,0.000180745987973,0.000181030277691,0.0,0.0,0.000181228533376,0.0,0.000180700698795,0.000180063338347,0.0,0.0,0.0,0.000180593714667,0.0,0.000181030277691,0.00036170297884])

    # Creating a new Canvas
    fig   = plt.figure(figsize=(12,6),dpi=80)
    frame = gridspec.GridSpec(1,1,right=0.7)
    pad   = fig.add_subplot(frame[0])

    # Creating a new Stack
    pad.hist(x=xData, bins=xBinning, weights=y1_PT_0_weights+y1_PT_1_weights+y1_PT_2_weights+y1_PT_3_weights+y1_PT_4_weights+y1_PT_5_weights+y1_PT_6_weights+y1_PT_7_weights+y1_PT_8_weights+y1_PT_9_weights+y1_PT_10_weights+y1_PT_11_weights+y1_PT_12_weights+y1_PT_13_weights+y1_PT_14_weights+y1_PT_15_weights+y1_PT_16_weights,\
             label="$bg\_dip\_1600\_inf$", histtype="step", rwidth=1.0,\
             color=None, edgecolor="#e5e5e5", linewidth=1, linestyle="solid",\
             bottom=None, cumulative=False, normed=False, align="mid", orientation="vertical")

    pad.hist(x=xData, bins=xBinning, weights=y1_PT_0_weights+y1_PT_1_weights+y1_PT_2_weights+y1_PT_3_weights+y1_PT_4_weights+y1_PT_5_weights+y1_PT_6_weights+y1_PT_7_weights+y1_PT_8_weights+y1_PT_9_weights+y1_PT_10_weights+y1_PT_11_weights+y1_PT_12_weights+y1_PT_13_weights+y1_PT_14_weights+y1_PT_15_weights,\
             label="$bg\_dip\_1200\_1600$", histtype="step", rwidth=1.0,\
             color=None, edgecolor="#f2f2f2", linewidth=1, linestyle="solid",\
             bottom=None, cumulative=False, normed=False, align="mid", orientation="vertical")

    pad.hist(x=xData, bins=xBinning, weights=y1_PT_0_weights+y1_PT_1_weights+y1_PT_2_weights+y1_PT_3_weights+y1_PT_4_weights+y1_PT_5_weights+y1_PT_6_weights+y1_PT_7_weights+y1_PT_8_weights+y1_PT_9_weights+y1_PT_10_weights+y1_PT_11_weights+y1_PT_12_weights+y1_PT_13_weights+y1_PT_14_weights,\
             label="$bg\_dip\_800\_1200$", histtype="step", rwidth=1.0,\
             color=None, edgecolor="#ccc6aa", linewidth=1, linestyle="solid",\
             bottom=None, cumulative=False, normed=False, align="mid", orientation="vertical")

    pad.hist(x=xData, bins=xBinning, weights=y1_PT_0_weights+y1_PT_1_weights+y1_PT_2_weights+y1_PT_3_weights+y1_PT_4_weights+y1_PT_5_weights+y1_PT_6_weights+y1_PT_7_weights+y1_PT_8_weights+y1_PT_9_weights+y1_PT_10_weights+y1_PT_11_weights+y1_PT_12_weights+y1_PT_13_weights,\
             label="$bg\_dip\_600\_800$", histtype="step", rwidth=1.0,\
             color=None, edgecolor="#ccc6aa", linewidth=1, linestyle="solid",\
             bottom=None, cumulative=False, normed=False, align="mid", orientation="vertical")

    pad.hist(x=xData, bins=xBinning, weights=y1_PT_0_weights+y1_PT_1_weights+y1_PT_2_weights+y1_PT_3_weights+y1_PT_4_weights+y1_PT_5_weights+y1_PT_6_weights+y1_PT_7_weights+y1_PT_8_weights+y1_PT_9_weights+y1_PT_10_weights+y1_PT_11_weights+y1_PT_12_weights,\
             label="$bg\_dip\_400\_600$", histtype="step", rwidth=1.0,\
             color=None, edgecolor="#c1bfa8", linewidth=1, linestyle="solid",\
             bottom=None, cumulative=False, normed=False, align="mid", orientation="vertical")

    pad.hist(x=xData, bins=xBinning, weights=y1_PT_0_weights+y1_PT_1_weights+y1_PT_2_weights+y1_PT_3_weights+y1_PT_4_weights+y1_PT_5_weights+y1_PT_6_weights+y1_PT_7_weights+y1_PT_8_weights+y1_PT_9_weights+y1_PT_10_weights+y1_PT_11_weights,\
             label="$bg\_dip\_200\_400$", histtype="step", rwidth=1.0,\
             color=None, edgecolor="#bab5a3", linewidth=1, linestyle="solid",\
             bottom=None, cumulative=False, normed=False, align="mid", orientation="vertical")

    pad.hist(x=xData, bins=xBinning, weights=y1_PT_0_weights+y1_PT_1_weights+y1_PT_2_weights+y1_PT_3_weights+y1_PT_4_weights+y1_PT_5_weights+y1_PT_6_weights+y1_PT_7_weights+y1_PT_8_weights+y1_PT_9_weights+y1_PT_10_weights,\
             label="$bg\_dip\_100\_200$", histtype="step", rwidth=1.0,\
             color=None, edgecolor="#b2a596", linewidth=1, linestyle="solid",\
             bottom=None, cumulative=False, normed=False, align="mid", orientation="vertical")

    pad.hist(x=xData, bins=xBinning, weights=y1_PT_0_weights+y1_PT_1_weights+y1_PT_2_weights+y1_PT_3_weights+y1_PT_4_weights+y1_PT_5_weights+y1_PT_6_weights+y1_PT_7_weights+y1_PT_8_weights+y1_PT_9_weights,\
             label="$bg\_dip\_0\_100$", histtype="step", rwidth=1.0,\
             color=None, edgecolor="#b7a39b", linewidth=1, linestyle="solid",\
             bottom=None, cumulative=False, normed=False, align="mid", orientation="vertical")

    pad.hist(x=xData, bins=xBinning, weights=y1_PT_0_weights+y1_PT_1_weights+y1_PT_2_weights+y1_PT_3_weights+y1_PT_4_weights+y1_PT_5_weights+y1_PT_6_weights+y1_PT_7_weights+y1_PT_8_weights,\
             label="$bg\_vbf\_1600\_inf$", histtype="step", rwidth=1.0,\
             color=None, edgecolor="#ad998c", linewidth=1, linestyle="solid",\
             bottom=None, cumulative=False, normed=False, align="mid", orientation="vertical")

    pad.hist(x=xData, bins=xBinning, weights=y1_PT_0_weights+y1_PT_1_weights+y1_PT_2_weights+y1_PT_3_weights+y1_PT_4_weights+y1_PT_5_weights+y1_PT_6_weights+y1_PT_7_weights,\
             label="$bg\_vbf\_1200\_1600$", histtype="step", rwidth=1.0,\
             color=None, edgecolor="#9b8e82", linewidth=1, linestyle="solid",\
             bottom=None, cumulative=False, normed=False, align="mid", orientation="vertical")

    pad.hist(x=xData, bins=xBinning, weights=y1_PT_0_weights+y1_PT_1_weights+y1_PT_2_weights+y1_PT_3_weights+y1_PT_4_weights+y1_PT_5_weights+y1_PT_6_weights,\
             label="$bg\_vbf\_800\_1200$", histtype="step", rwidth=1.0,\
             color=None, edgecolor="#876656", linewidth=1, linestyle="solid",\
             bottom=None, cumulative=False, normed=False, align="mid", orientation="vertical")

    pad.hist(x=xData, bins=xBinning, weights=y1_PT_0_weights+y1_PT_1_weights+y1_PT_2_weights+y1_PT_3_weights+y1_PT_4_weights+y1_PT_5_weights,\
             label="$bg\_vbf\_600\_800$", histtype="step", rwidth=1.0,\
             color=None, edgecolor="#afcec6", linewidth=1, linestyle="solid",\
             bottom=None, cumulative=False, normed=False, align="mid", orientation="vertical")

    pad.hist(x=xData, bins=xBinning, weights=y1_PT_0_weights+y1_PT_1_weights+y1_PT_2_weights+y1_PT_3_weights+y1_PT_4_weights,\
             label="$bg\_vbf\_400\_600$", histtype="step", rwidth=1.0,\
             color=None, edgecolor="#84c1a3", linewidth=1, linestyle="solid",\
             bottom=None, cumulative=False, normed=False, align="mid", orientation="vertical")

    pad.hist(x=xData, bins=xBinning, weights=y1_PT_0_weights+y1_PT_1_weights+y1_PT_2_weights+y1_PT_3_weights,\
             label="$bg\_vbf\_200\_400$", histtype="step", rwidth=1.0,\
             color=None, edgecolor="#89a8a0", linewidth=1, linestyle="solid",\
             bottom=None, cumulative=False, normed=False, align="mid", orientation="vertical")

    pad.hist(x=xData, bins=xBinning, weights=y1_PT_0_weights+y1_PT_1_weights+y1_PT_2_weights,\
             label="$bg\_vbf\_100\_200$", histtype="step", rwidth=1.0,\
             color=None, edgecolor="#829e8c", linewidth=1, linestyle="solid",\
             bottom=None, cumulative=False, normed=False, align="mid", orientation="vertical")

    pad.hist(x=xData, bins=xBinning, weights=y1_PT_0_weights+y1_PT_1_weights,\
             label="$bg\_vbf\_0\_100$", histtype="step", rwidth=1.0,\
             color=None, edgecolor="#adbcc6", linewidth=1, linestyle="solid",\
             bottom=None, cumulative=False, normed=False, align="mid", orientation="vertical")

    pad.hist(x=xData, bins=xBinning, weights=y1_PT_0_weights,\
             label="$signal$", histtype="step", rwidth=1.0,\
             color=None, edgecolor="#7a8e99", linewidth=1, linestyle="solid",\
             bottom=None, cumulative=False, normed=False, align="mid", orientation="vertical")


    # Axis
    plt.rc('text',usetex=False)
    plt.xlabel(r"p_{T} [ j_{1} ]   ( GeV ) ",\
               fontsize=16,color="black")
    plt.ylabel(r"$\mathrm{Events}$ $(\mathcal{L}_{\mathrm{int}} = 40.0\ \mathrm{fb}^{-1})$ ",\
               fontsize=16,color="black")

    # Boundary of y-axis
    ymax=(y1_PT_0_weights+y1_PT_1_weights+y1_PT_2_weights+y1_PT_3_weights+y1_PT_4_weights+y1_PT_5_weights+y1_PT_6_weights+y1_PT_7_weights+y1_PT_8_weights+y1_PT_9_weights+y1_PT_10_weights+y1_PT_11_weights+y1_PT_12_weights+y1_PT_13_weights+y1_PT_14_weights+y1_PT_15_weights+y1_PT_16_weights).max()*1.1
    ymin=0 # linear scale
    #ymin=min([x for x in (y1_PT_0_weights+y1_PT_1_weights+y1_PT_2_weights+y1_PT_3_weights+y1_PT_4_weights+y1_PT_5_weights+y1_PT_6_weights+y1_PT_7_weights+y1_PT_8_weights+y1_PT_9_weights+y1_PT_10_weights+y1_PT_11_weights+y1_PT_12_weights+y1_PT_13_weights+y1_PT_14_weights+y1_PT_15_weights+y1_PT_16_weights) if x])/100. # log scale
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
    plt.savefig('../../HTML/MadAnalysis5job_0/selection_0.png')
    plt.savefig('../../PDF/MadAnalysis5job_0/selection_0.png')
    plt.savefig('../../DVI/MadAnalysis5job_0/selection_0.eps')

# Running!
if __name__ == '__main__':
    selection_0()
