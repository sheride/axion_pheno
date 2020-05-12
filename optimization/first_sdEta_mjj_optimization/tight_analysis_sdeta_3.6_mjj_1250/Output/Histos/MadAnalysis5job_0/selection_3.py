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
    y4_PT_0_weights = numpy.array([0.0,0.0,62.1563866737,57.4850306814,55.3110725465,51.7573955954,50.1934769371,47.8639189357,45.8824006358,43.0656830523,40.4618452863,37.0555522086,34.2551986112,31.0331573755,28.8059752863,26.3331494078,23.4386318911,22.1449010011,19.5205912525,17.0068254092,15.3200628563,12.478769294,11.5780700667,10.0714473593,8.63851658869,7.63956144573,6.6324143098,5.95279889287,5.36734339515,4.92927577099,4.02448454724,3.56185294415,3.07056296565,2.89451751668,2.42779191711,2.10845339108,1.805490851,1.5434694758,1.48615232497,1.20366056733,1.08083827271,0.953921581595,0.806534508044,0.732840971268,0.622300666105,0.499478371479,0.421690838215,0.388937986315,0.38074979334,0.294774027102,0.200610107889,0.278397721152,0.237456876277,0.147387033551,0.135104764089,0.0736934967756,0.0941639192132,0.0982579957007,0.0736934967756,0.0859757662381,0.0900698427257,0.0450349213628,0.0818816897506,0.0573171908254,0.0286585874127,0.0245645029252,0.0204704184377,0.0,0.00409408448753,0.0204704184377,0.00818816897506,0.0122822534626,0.0122822534626,0.0,0.00818816897506,0.00818816897506,0.00409408448753,0.00818816897506,0.00409408448753,0.0,0.00409408448753,0.0,0.0,0.0,0.00409408448753,0.0,0.0,0.0,0.0,0.0,0.00818816897506,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0])

    # Creating weights for histo: y4_PT_1
    y4_PT_1_weights = numpy.array([0.0,0.0,86.7660679685,82.4601893322,34.9599375194,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0])

    # Creating weights for histo: y4_PT_2
    y4_PT_2_weights = numpy.array([0.0,0.0,35.6312612778,88.2039272872,170.078156537,208.714545095,181.81580769,141.363283712,93.1016914686,31.9877222338,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0])

    # Creating weights for histo: y4_PT_3
    y4_PT_3_weights = numpy.array([0.0,0.0,4.0316664942,8.38809699775,14.8345130007,24.6244165109,38.002376263,60.3068449821,92.812536802,139.611611817,154.124940715,131.824745784,113.745566466,94.8423423294,79.3755768384,66.3833426997,51.9067391277,38.7448859825,25.7356704429,8.57472178023,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0])

    # Creating weights for histo: y4_PT_4
    y4_PT_4_weights = numpy.array([0.0,0.0,0.246688728464,0.508208975172,0.898053199621,1.23165092935,1.68854081517,2.21246874661,2.69313828357,3.31781367774,4.00954836152,4.57597351091,5.50265680765,6.40860515929,8.04079366057,9.79340357222,12.4560022037,16.440085824,22.5545297323,31.3858647197,32.5642573433,26.3032619053,21.1205236959,17.0527467344,13.4605227127,10.7268568907,8.17015358391,5.66858847643,3.52311969656,1.16052080846,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0])

    # Creating weights for histo: y4_PT_5
    y4_PT_5_weights = numpy.array([0.0,0.0,0.0388157005969,0.0960459479602,0.1401694859,0.190829146327,0.236458773521,0.289146851263,0.303510652892,0.331489672618,0.344843946737,0.375364589603,0.387670806766,0.421207269032,0.416420895538,0.479427543124,0.509673358608,0.536160252503,0.588867174866,0.655635544728,0.732531597633,0.82279212716,0.906210979286,1.07436140538,1.28831426104,1.57020057221,1.95437676219,2.52930732016,3.42273076427,4.6366887951,4.93967507943,4.06721717552,3.34127599369,2.7718683898,2.2909240748,1.81978696428,1.39697490179,1.03202142472,0.640796706632,0.207964027353,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0])

    # Creating weights for histo: y4_PT_6
    y4_PT_6_weights = numpy.array([0.0,0.0,0.0168929879925,0.0320832855871,0.0400560652731,0.0503997457448,0.0589423781445,0.0618332880252,0.066707396113,0.0709971462544,0.0609620343693,0.0698712862767,0.0689811188369,0.0641342417995,0.0666936206404,0.068990885627,0.0646783829634,0.0698467143524,0.0664028262122,0.0741484305611,0.0707443993215,0.0758682653245,0.0753137475709,0.0796177730206,0.0873141835374,0.0973682791833,0.0847636617856,0.102248095395,0.140516418223,0.13509370044,0.139693588652,0.175534209363,0.199871910595,0.220436052035,0.271768181345,0.314079375453,0.385711433039,0.493369450423,0.667119346214,0.914254623348,0.94797674032,0.834883009425,0.704927820174,0.612867576465,0.509311810846,0.429451957387,0.391714660033,0.321260815219,0.260794687866,0.245068856279,0.215607738896,0.169782299771,0.148557675404,0.121075107756,0.101621601297,0.0907371185641,0.0646838011827,0.0500830298359,0.0331983691065,0.0117298648918,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0])

    # Creating weights for histo: y4_PT_7
    y4_PT_7_weights = numpy.array([0.0,0.0,0.00222482651644,0.0032612774022,0.00362855560608,0.00412502300354,0.0036469637293,0.00405653933713,0.00328201477639,0.00349806810026,0.00367223471935,0.0029161995835,0.00308607774898,0.00321624759158,0.00291551103378,0.00248217480303,0.00267353295384,0.00254677820051,0.00252690958078,0.00207322530189,0.00235459948954,0.00226653301648,0.00215979649472,0.00218108286473,0.00177042183768,0.00198736528913,0.00183613789464,0.00205197413466,0.00211493222101,0.00222478670376,0.00190101998084,0.00200695983003,0.0018771483015,0.00242001674189,0.00224439758882,0.0022681045694,0.00200839937251,0.00270048655322,0.00272085681264,0.00254825923198,0.00261359979256,0.00315383053852,0.00328345892875,0.00349960612672,0.00377640688583,0.00419049725088,0.00526812617583,0.00481637385932,0.00596135283717,0.0068466316471,0.0076658800895,0.00867899949105,0.00984728774183,0.0119837070725,0.0144902124483,0.0178785601717,0.0205296609887,0.0254601673074,0.0334436603376,0.0459473041694,0.049667316612,0.0432744069611,0.0377057998667,0.0321944014895,0.0290663155023,0.0236041591167,0.0206235434648,0.0182028909774,0.0160607805297,0.0141662755786,0.011444023227,0.00948014364379,0.0081203773851,0.00704023858537,0.00571901937673,0.00544281999854,0.00362715126639,0.00295886829301,0.00155472682788,0.000475274482465,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0])

    # Creating weights for histo: y4_PT_8
    y4_PT_8_weights = numpy.array([0.0,0.0,0.00036776640761,0.0005963381889,0.000454603328163,0.000369282140725,0.000453122057032,0.000255674349028,0.000226574620203,0.000454098876021,0.00034066131464,0.000341069213811,0.000198649718232,0.000255383798854,0.000284158515521,8.51066170261e-05,0.000141541116058,0.000141914642371,0.000226618886027,0.000223514782254,0.000113431842473,0.000113737009282,0.000170120246113,0.000112606983008,0.000113568160415,5.68199236417e-05,0.000141951287937,0.000142100885626,0.000142118309724,0.000168936506678,0.000196451875507,5.6859554923e-05,5.67880463067e-05,2.84403611527e-05,2.8379562489e-05,2.8460013396e-05,0.000113799219104,5.6827677588e-05,0.0,0.000142110154712,5.68012963453e-05,8.51994861307e-05,0.000113648611322,0.00011364087223,0.0,0.000113601062697,0.000141375787662,0.000113696174802,2.8379562489e-05,5.66335021345e-05,0.000112029106044,0.000113667238619,0.000142209247769,8.25402835975e-05,0.000199100397796,0.000226993660101,0.000198781921532,5.67880463067e-05,0.00019663517761,0.00017039579344,0.000113482153999,0.000170250518354,0.000312480770108,0.00022679921727,0.000227163741875,0.00028397432216,0.000454573916642,0.000284106822545,0.000311817971092,0.000368797296263,0.00048253194371,0.000424689583514,0.000794836838866,0.000680979197787,0.000908479835262,0.00113211062963,0.00147631068496,0.00141940979051,0.00238387356407,0.00249345524539,0.00365417942249,0.00294967843533,0.00272105288146,0.00232084229863,0.00164633512081,0.00155661512852,0.00147589461592,0.00113345628097,0.000850290181453,0.000879283850552,0.000793366411377,0.00070603231729,0.000481075627809,0.000568099861127,0.000369143252988,0.000339079776962,0.000312343516345,0.000253556719541,0.000198659076443,0.000141938156733])

    # Creating weights for histo: y4_PT_9
    y4_PT_9_weights = numpy.array([0.0,0.0,86.014448275,117.297211694,26.0677184924,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0])

    # Creating weights for histo: y4_PT_10
    y4_PT_10_weights = numpy.array([0.0,0.0,66.3498008361,89.5332978868,190.63491279,217.005210542,167.439873123,133.772179976,95.8262548842,29.4779238078,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0])

    # Creating weights for histo: y4_PT_11
    y4_PT_11_weights = numpy.array([0.0,0.0,23.725431171,25.7960161273,30.4088179565,36.4002781276,42.8420604218,52.7420464251,103.435762911,154.084024139,181.255125203,175.060837756,163.777636358,147.878747509,135.202417397,118.853817363,95.3552551874,85.9130493506,52.5172676796,16.5823046095,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0])

    # Creating weights for histo: y4_PT_12
    y4_PT_12_weights = numpy.array([0.0,0.0,4.2365053501,4.43102988698,4.34713846339,3.65543317041,3.90475604993,4.59706996545,4.43055283771,4.90001164479,5.67565144968,6.92295833815,9.22244741943,9.22059308272,13.4574369839,16.3649792287,23.1764734644,33.9767959908,50.5659152832,73.6315555815,77.1456005795,60.0888191092,47.4916404692,38.6843875016,29.3259002477,24.0620962106,17.1127001093,12.3229099305,7.8089504128,2.46480819979,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0])

    # Creating weights for histo: y4_PT_13
    y4_PT_13_weights = numpy.array([0.0,0.0,1.14915002991,0.977984906705,0.927475991591,0.726061710457,0.685405055732,0.584634563602,0.685902037825,0.645253878522,0.443655246764,0.493976959222,0.514181071401,0.423387965066,0.382946669249,0.433562080525,0.564383423202,0.766157667435,0.594766687412,0.695527955943,0.96810776687,1.01840733055,1.29064368377,1.56261303806,2.17790599613,2.58075094242,3.13581986535,4.63770763846,6.46261192654,8.52884380119,10.2437293611,7.87416850145,6.53345766443,5.49490769213,4.37514999633,3.39708195587,2.90366247827,1.96595011192,1.19993140529,0.362997723089,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0])

    # Creating weights for histo: y4_PT_14
    y4_PT_14_weights = numpy.array([0.0,0.0,0.412994165815,0.464011945394,0.39326904032,0.319700928171,0.212211517438,0.203660218275,0.147157615723,0.107496682278,0.0961969697173,0.076366310626,0.0594012176118,0.0678635653811,0.0622122278599,0.0509155932018,0.0735384103858,0.067903193381,0.0735104014694,0.0650854117466,0.0565903227851,0.0735485289916,0.0848465871798,0.0707325940989,0.0707172045844,0.065092721766,0.11318460837,0.0876659847132,0.090514853167,0.144296628026,0.217857083892,0.183897619312,0.220617924322,0.294256328079,0.325403281933,0.464016946986,0.644995714027,0.902478066163,1.19674674433,1.6521497953,1.86154491616,1.61838019886,1.34944304633,1.18261993948,0.990321415031,0.814849016285,0.729998543253,0.611062603991,0.557343964614,0.481052754819,0.373445575827,0.336655825632,0.234850532086,0.257432990269,0.217821303271,0.14427796824,0.138667451406,0.0820649709044,0.0735712285255,0.0282965233646,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0])

    # Creating weights for histo: y4_PT_15
    y4_PT_15_weights = numpy.array([0.0,0.0,0.028929790339,0.03351869463,0.018261180529,0.0137372272761,0.0106524169585,0.0151973729379,0.00302549758744,0.00457205554733,0.00610253174364,0.00760703343366,0.00304241369295,0.0015143507066,0.00152311484231,0.0,0.00456256106698,0.0015263068502,0.0,0.0,0.00152149224814,0.0,0.0,0.00457346896511,0.00152179124037,0.0,0.0015290462335,0.0,0.00305498909317,0.00306963143963,0.0,0.00305287251185,0.0,0.0,0.00609306089904,0.00152246958636,0.0045839573287,0.0030710377667,0.00152311484231,0.00304774000897,0.00152435926449,0.00305318450374,0.0015186819576,0.00303516342697,0.00608448939469,0.0015263068502,0.00609605200307,0.00305755711729,0.00612640621364,0.0106922384683,0.01374626795,0.00914497143591,0.0136943756633,0.0137394135828,0.0304809572699,0.0396111752714,0.0350190328828,0.0457264644105,0.0640451743523,0.0866859646155,0.123442071412,0.101942025118,0.0822698258313,0.0746693962259,0.0776987428951,0.0518756353957,0.0426390328883,0.0456571053053,0.0228312943995,0.0334297060352,0.0152323065748,0.0213545209883,0.00911847812494,0.00611568858328,0.0228137803095,0.0106543976342,0.00609968009053,0.00606007484783,0.00152246958636,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0])

    # Creating weights for histo: y4_PT_16
    y4_PT_16_weights = numpy.array([0.0,0.0,0.00433472474085,0.00270897507299,0.00252830399996,0.00198441567041,0.000721894812436,0.000181228522689,0.00036139016952,0.000903269485141,0.0,0.000361503353946,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.00018026277725,0.000180686053883,0.0,0.000180546912906,0.0,0.0,0.000181030267016,0.0,0.0,0.0,0.0,0.0,0.000180717055401,0.0,0.00018046188017,0.0,0.0,0.0,0.0,0.0,0.0,0.000180794270363,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.000180686053883,0.000180686053883,0.0,0.000179945329403,0.0,0.0,0.000180058398295,0.000360900384039,0.0,0.000361195919011,0.00036053903342,0.000541882666096,0.000542625932315,0.000360875698358,0.00126268645615,0.000722283005363,0.00144470002971,0.00126336771933,0.000902665244364,0.00144403571146,0.00216691448513,0.0030686770269,0.00487509853801,0.00631960370103,0.00957420472906,0.00397149477563,0.00433204821224,0.00361279026188,0.00360794670786,0.00487305359313,0.00216739934118,0.0019854716476,0.00234637476593,0.00180321429812,0.00090351210572,0.00144474970916,0.000722783651003,0.00126446836951,0.000903647665155,0.000361610299557,0.000722200206276,0.000542046723821,0.000902889764678,0.000541384331128])

    # Creating a new Canvas
    fig   = plt.figure(figsize=(12,6),dpi=80)
    frame = gridspec.GridSpec(1,1,right=0.7)
    pad   = fig.add_subplot(frame[0])

    # Creating a new Stack
    pad.hist(x=xData, bins=xBinning, weights=y4_PT_0_weights+y4_PT_1_weights+y4_PT_2_weights+y4_PT_3_weights+y4_PT_4_weights+y4_PT_5_weights+y4_PT_6_weights+y4_PT_7_weights+y4_PT_8_weights+y4_PT_9_weights+y4_PT_10_weights+y4_PT_11_weights+y4_PT_12_weights+y4_PT_13_weights+y4_PT_14_weights+y4_PT_15_weights+y4_PT_16_weights,\
             label="$bg\_dip\_1600\_inf$", histtype="step", rwidth=1.0,\
             color=None, edgecolor="#e5e5e5", linewidth=1, linestyle="solid",\
             bottom=None, cumulative=False, normed=False, align="mid", orientation="vertical")

    pad.hist(x=xData, bins=xBinning, weights=y4_PT_0_weights+y4_PT_1_weights+y4_PT_2_weights+y4_PT_3_weights+y4_PT_4_weights+y4_PT_5_weights+y4_PT_6_weights+y4_PT_7_weights+y4_PT_8_weights+y4_PT_9_weights+y4_PT_10_weights+y4_PT_11_weights+y4_PT_12_weights+y4_PT_13_weights+y4_PT_14_weights+y4_PT_15_weights,\
             label="$bg\_dip\_1200\_1600$", histtype="step", rwidth=1.0,\
             color=None, edgecolor="#f2f2f2", linewidth=1, linestyle="solid",\
             bottom=None, cumulative=False, normed=False, align="mid", orientation="vertical")

    pad.hist(x=xData, bins=xBinning, weights=y4_PT_0_weights+y4_PT_1_weights+y4_PT_2_weights+y4_PT_3_weights+y4_PT_4_weights+y4_PT_5_weights+y4_PT_6_weights+y4_PT_7_weights+y4_PT_8_weights+y4_PT_9_weights+y4_PT_10_weights+y4_PT_11_weights+y4_PT_12_weights+y4_PT_13_weights+y4_PT_14_weights,\
             label="$bg\_dip\_800\_1200$", histtype="step", rwidth=1.0,\
             color=None, edgecolor="#ccc6aa", linewidth=1, linestyle="solid",\
             bottom=None, cumulative=False, normed=False, align="mid", orientation="vertical")

    pad.hist(x=xData, bins=xBinning, weights=y4_PT_0_weights+y4_PT_1_weights+y4_PT_2_weights+y4_PT_3_weights+y4_PT_4_weights+y4_PT_5_weights+y4_PT_6_weights+y4_PT_7_weights+y4_PT_8_weights+y4_PT_9_weights+y4_PT_10_weights+y4_PT_11_weights+y4_PT_12_weights+y4_PT_13_weights,\
             label="$bg\_dip\_600\_800$", histtype="step", rwidth=1.0,\
             color=None, edgecolor="#ccc6aa", linewidth=1, linestyle="solid",\
             bottom=None, cumulative=False, normed=False, align="mid", orientation="vertical")

    pad.hist(x=xData, bins=xBinning, weights=y4_PT_0_weights+y4_PT_1_weights+y4_PT_2_weights+y4_PT_3_weights+y4_PT_4_weights+y4_PT_5_weights+y4_PT_6_weights+y4_PT_7_weights+y4_PT_8_weights+y4_PT_9_weights+y4_PT_10_weights+y4_PT_11_weights+y4_PT_12_weights,\
             label="$bg\_dip\_400\_600$", histtype="step", rwidth=1.0,\
             color=None, edgecolor="#c1bfa8", linewidth=1, linestyle="solid",\
             bottom=None, cumulative=False, normed=False, align="mid", orientation="vertical")

    pad.hist(x=xData, bins=xBinning, weights=y4_PT_0_weights+y4_PT_1_weights+y4_PT_2_weights+y4_PT_3_weights+y4_PT_4_weights+y4_PT_5_weights+y4_PT_6_weights+y4_PT_7_weights+y4_PT_8_weights+y4_PT_9_weights+y4_PT_10_weights+y4_PT_11_weights,\
             label="$bg\_dip\_200\_400$", histtype="step", rwidth=1.0,\
             color=None, edgecolor="#bab5a3", linewidth=1, linestyle="solid",\
             bottom=None, cumulative=False, normed=False, align="mid", orientation="vertical")

    pad.hist(x=xData, bins=xBinning, weights=y4_PT_0_weights+y4_PT_1_weights+y4_PT_2_weights+y4_PT_3_weights+y4_PT_4_weights+y4_PT_5_weights+y4_PT_6_weights+y4_PT_7_weights+y4_PT_8_weights+y4_PT_9_weights+y4_PT_10_weights,\
             label="$bg\_dip\_100\_200$", histtype="step", rwidth=1.0,\
             color=None, edgecolor="#b2a596", linewidth=1, linestyle="solid",\
             bottom=None, cumulative=False, normed=False, align="mid", orientation="vertical")

    pad.hist(x=xData, bins=xBinning, weights=y4_PT_0_weights+y4_PT_1_weights+y4_PT_2_weights+y4_PT_3_weights+y4_PT_4_weights+y4_PT_5_weights+y4_PT_6_weights+y4_PT_7_weights+y4_PT_8_weights+y4_PT_9_weights,\
             label="$bg\_dip\_0\_100$", histtype="step", rwidth=1.0,\
             color=None, edgecolor="#b7a39b", linewidth=1, linestyle="solid",\
             bottom=None, cumulative=False, normed=False, align="mid", orientation="vertical")

    pad.hist(x=xData, bins=xBinning, weights=y4_PT_0_weights+y4_PT_1_weights+y4_PT_2_weights+y4_PT_3_weights+y4_PT_4_weights+y4_PT_5_weights+y4_PT_6_weights+y4_PT_7_weights+y4_PT_8_weights,\
             label="$bg\_vbf\_1600\_inf$", histtype="step", rwidth=1.0,\
             color=None, edgecolor="#ad998c", linewidth=1, linestyle="solid",\
             bottom=None, cumulative=False, normed=False, align="mid", orientation="vertical")

    pad.hist(x=xData, bins=xBinning, weights=y4_PT_0_weights+y4_PT_1_weights+y4_PT_2_weights+y4_PT_3_weights+y4_PT_4_weights+y4_PT_5_weights+y4_PT_6_weights+y4_PT_7_weights,\
             label="$bg\_vbf\_1200\_1600$", histtype="step", rwidth=1.0,\
             color=None, edgecolor="#9b8e82", linewidth=1, linestyle="solid",\
             bottom=None, cumulative=False, normed=False, align="mid", orientation="vertical")

    pad.hist(x=xData, bins=xBinning, weights=y4_PT_0_weights+y4_PT_1_weights+y4_PT_2_weights+y4_PT_3_weights+y4_PT_4_weights+y4_PT_5_weights+y4_PT_6_weights,\
             label="$bg\_vbf\_800\_1200$", histtype="step", rwidth=1.0,\
             color=None, edgecolor="#876656", linewidth=1, linestyle="solid",\
             bottom=None, cumulative=False, normed=False, align="mid", orientation="vertical")

    pad.hist(x=xData, bins=xBinning, weights=y4_PT_0_weights+y4_PT_1_weights+y4_PT_2_weights+y4_PT_3_weights+y4_PT_4_weights+y4_PT_5_weights,\
             label="$bg\_vbf\_600\_800$", histtype="step", rwidth=1.0,\
             color=None, edgecolor="#afcec6", linewidth=1, linestyle="solid",\
             bottom=None, cumulative=False, normed=False, align="mid", orientation="vertical")

    pad.hist(x=xData, bins=xBinning, weights=y4_PT_0_weights+y4_PT_1_weights+y4_PT_2_weights+y4_PT_3_weights+y4_PT_4_weights,\
             label="$bg\_vbf\_400\_600$", histtype="step", rwidth=1.0,\
             color=None, edgecolor="#84c1a3", linewidth=1, linestyle="solid",\
             bottom=None, cumulative=False, normed=False, align="mid", orientation="vertical")

    pad.hist(x=xData, bins=xBinning, weights=y4_PT_0_weights+y4_PT_1_weights+y4_PT_2_weights+y4_PT_3_weights,\
             label="$bg\_vbf\_200\_400$", histtype="step", rwidth=1.0,\
             color=None, edgecolor="#89a8a0", linewidth=1, linestyle="solid",\
             bottom=None, cumulative=False, normed=False, align="mid", orientation="vertical")

    pad.hist(x=xData, bins=xBinning, weights=y4_PT_0_weights+y4_PT_1_weights+y4_PT_2_weights,\
             label="$bg\_vbf\_100\_200$", histtype="step", rwidth=1.0,\
             color=None, edgecolor="#829e8c", linewidth=1, linestyle="solid",\
             bottom=None, cumulative=False, normed=False, align="mid", orientation="vertical")

    pad.hist(x=xData, bins=xBinning, weights=y4_PT_0_weights+y4_PT_1_weights,\
             label="$bg\_vbf\_0\_100$", histtype="step", rwidth=1.0,\
             color=None, edgecolor="#adbcc6", linewidth=1, linestyle="solid",\
             bottom=None, cumulative=False, normed=False, align="mid", orientation="vertical")

    pad.hist(x=xData, bins=xBinning, weights=y4_PT_0_weights,\
             label="$signal$", histtype="step", rwidth=1.0,\
             color=None, edgecolor="#7a8e99", linewidth=1, linestyle="solid",\
             bottom=None, cumulative=False, normed=False, align="mid", orientation="vertical")


    # Axis
    plt.rc('text',usetex=False)
    plt.xlabel(r"p_{T} [ j_{2} ]   ( GeV ) ",\
               fontsize=16,color="black")
    plt.ylabel(r"$\mathrm{Events}$ $(\mathcal{L}_{\mathrm{int}} = 40.0\ \mathrm{fb}^{-1})$ ",\
               fontsize=16,color="black")

    # Boundary of y-axis
    ymax=(y4_PT_0_weights+y4_PT_1_weights+y4_PT_2_weights+y4_PT_3_weights+y4_PT_4_weights+y4_PT_5_weights+y4_PT_6_weights+y4_PT_7_weights+y4_PT_8_weights+y4_PT_9_weights+y4_PT_10_weights+y4_PT_11_weights+y4_PT_12_weights+y4_PT_13_weights+y4_PT_14_weights+y4_PT_15_weights+y4_PT_16_weights).max()*1.1
    ymin=0 # linear scale
    #ymin=min([x for x in (y4_PT_0_weights+y4_PT_1_weights+y4_PT_2_weights+y4_PT_3_weights+y4_PT_4_weights+y4_PT_5_weights+y4_PT_6_weights+y4_PT_7_weights+y4_PT_8_weights+y4_PT_9_weights+y4_PT_10_weights+y4_PT_11_weights+y4_PT_12_weights+y4_PT_13_weights+y4_PT_14_weights+y4_PT_15_weights+y4_PT_16_weights) if x])/100. # log scale
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