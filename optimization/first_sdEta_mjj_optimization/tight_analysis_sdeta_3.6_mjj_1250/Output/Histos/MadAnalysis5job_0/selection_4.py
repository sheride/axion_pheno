def selection_4():

    # Library import
    import numpy
    import matplotlib
    import matplotlib.pyplot   as plt
    import matplotlib.gridspec as gridspec

    # Library version
    matplotlib_version = matplotlib.__version__
    numpy_version      = numpy.__version__

    # Histo binning
    xBinning = numpy.linspace(-8.0,8.0,161,endpoint=True)

    # Creating data sequence: middle of each bin
    xData = numpy.array([-7.95,-7.85,-7.75,-7.65,-7.55,-7.45,-7.35,-7.25,-7.15,-7.05,-6.95,-6.85,-6.75,-6.65,-6.55,-6.45,-6.35,-6.25,-6.15,-6.05,-5.95,-5.85,-5.75,-5.65,-5.55,-5.45,-5.35,-5.25,-5.15,-5.05,-4.95,-4.85,-4.75,-4.65,-4.55,-4.45,-4.35,-4.25,-4.15,-4.05,-3.95,-3.85,-3.75,-3.65,-3.55,-3.45,-3.35,-3.25,-3.15,-3.05,-2.95,-2.85,-2.75,-2.65,-2.55,-2.45,-2.35,-2.25,-2.15,-2.05,-1.95,-1.85,-1.75,-1.65,-1.55,-1.45,-1.35,-1.25,-1.15,-1.05,-0.95,-0.85,-0.75,-0.65,-0.55,-0.45,-0.35,-0.25,-0.15,-0.05,0.05,0.15,0.25,0.35,0.45,0.55,0.65,0.75,0.85,0.95,1.05,1.15,1.25,1.35,1.45,1.55,1.65,1.75,1.85,1.95,2.05,2.15,2.25,2.35,2.45,2.55,2.65,2.75,2.85,2.95,3.05,3.15,3.25,3.35,3.45,3.55,3.65,3.75,3.85,3.95,4.05,4.15,4.25,4.35,4.45,4.55,4.65,4.75,4.85,4.95,5.05,5.15,5.25,5.35,5.45,5.55,5.65,5.75,5.85,5.95,6.05,6.15,6.25,6.35,6.45,6.55,6.65,6.75,6.85,6.95,7.05,7.15,7.25,7.35,7.45,7.55,7.65,7.75,7.85,7.95])

    # Creating weights for histo: y5_ETA_0
    y5_ETA_0_weights = numpy.array([0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,2.804447605,3.03781020571,3.83615672392,4.38066825891,4.99068773795,5.7153431191,6.09609079394,7.21786983594,7.94661721359,8.80228048286,9.76439166121,10.7305948361,11.7663979515,12.4910493326,13.964920074,14.9556872278,15.4469788083,17.1132693853,17.1787773293,18.2555204098,17.8502047559,18.2718963958,18.6403640811,17.8788647315,17.5063050496,16.6874857489,16.0529022908,14.3415757523,13.3303366159,11.8605618711,10.1082913675,8.71221255977,6.87806212614,5.40009538832,4.39295224842,3.2466084274,2.50148546373,1.70723294202,1.25278973012,0.810628507724,0.507666366453,0.384843911343,0.188327879168,0.143292957628,0.0573171910511,0.0532230745475,0.012282253511,0.00818816900731,0.0,0.0,0.00409408450365,0.0,0.012282253511,0.0163763340146,0.0327526720292,0.0532230745475,0.131010688117,0.196516032175,0.294774028263,0.544513134986,0.769687742687,1.25278973012,1.71951533153,2.42779192667,3.20976165886,4.30697632184,5.80541104218,6.97631804223,8.24139296185,10.2393032556,12.0366057207,13.1461047732,14.6199755145,16.249418123,17.2893172349,17.4858330671,18.5666721441,18.3947202909,18.8901038679,18.3783443049,18.0917565496,17.4940210601,16.8062136475,16.200290165,15.1071710985,13.6824283152,12.8472370285,11.786865934,11.0826865354,9.87493156681,8.69174057726,7.98755717863,7.18511786391,6.3826785492,5.7071511261,4.91699580089,4.35201228338,3.9221326505,3.00505783368,2.86585875256,0.00409408450365,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0])

    # Creating weights for histo: y5_ETA_1
    y5_ETA_1_weights = numpy.array([0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,3.93611479101,4.26473215847,4.43522499762,4.3014525839,5.29733391243,5.21185718914,5.57721100316,5.68722408402,4.66509213722,4.94510140226,5.04095981651,4.74964364037,4.71473760768,4.88350016501,4.61655612987,4.20455279633,4.27712850628,3.77898357263,3.26841265209,2.49126498077,2.39286161034,2.18711828426,1.9689109211,1.66496128446,1.22724323938,0.984319280961,0.777774497949,0.534565363455,0.26743852725,0.157882569228,0.158031405507,0.121470991092,0.0607598877136,0.01214391491,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0121713711182,0.0485590777727,0.0729028613824,0.0729094300449,0.303655048152,0.413100380285,0.534653079131,0.692819262377,0.923473439896,1.27589740254,1.4218663005,1.85912614132,2.06576104317,2.80647146249,2.90368926946,3.0494194526,3.60826964192,3.63322535251,4.20463290197,4.64223399281,4.88351618613,5.22536700534,5.09121809512,4.9823304985,5.15122523013,5.17566546093,5.22562734867,5.05435347953,5.07859344623,4.59291695547,4.34908339751,4.38652877899,3.92455194238,3.65781417927,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0])

    # Creating weights for histo: y5_ETA_2
    y5_ETA_2_weights = numpy.array([0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,3.70452284952,4.51797151678,6.26551425679,8.09246333568,9.91929671609,11.3447266528,13.3430251651,14.3368006405,16.3755398999,17.5102980924,18.1124466449,20.1201249973,20.5932697562,21.606833802,22.1989041913,21.9483013064,22.6599584602,21.6260728046,21.9758499384,20.4003921434,19.7586953748,19.5175549719,18.1228966959,16.3455533358,14.7788720962,13.7048266754,11.1746912236,9.71900200495,8.64445246948,7.55034989267,5.853375648,4.71927445744,3.72487958202,2.64032626102,1.76724577616,1.16476665669,0.883729702561,0.441776011384,0.381416533055,0.170698009624,0.0401193285656,0.0301184768247,0.0100697956324,0.0,0.0100230782432,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0100325696498,0.0,0.0200494828175,0.0703875192098,0.160634391463,0.421673815518,0.522104632339,0.82335328267,1.31535069399,1.95762388884,2.43933074772,3.553301231,4.48781140503,5.69295558795,6.53545531449,8.03263896277,9.66863598193,11.5864786049,12.6602719682,14.5686603733,16.6461503558,17.9714887202,19.4062075912,19.6980611126,20.9640833509,20.9457575398,22.4602794301,21.5256052122,21.9375702733,22.3078838854,21.4264681522,21.1248133176,20.472335931,18.8441650868,18.7660272991,15.5213546279,14.2667700097,12.8610583978,11.0449891072,8.92558322201,7.51041326025,6.06385182446,4.60853036169,3.26316955075,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0])

    # Creating weights for histo: y5_ETA_3
    y5_ETA_3_weights = numpy.array([0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.308040025689,0.516998366614,0.709656430733,1.05595799183,1.55123194571,1.93579812975,3.30573370654,4.67014139023,5.7709099697,7.88199882099,9.8066781952,12.4248243868,15.1811536874,16.7658069003,19.3936056781,21.1768519144,23.5632791618,25.0156033806,26.1774481304,27.5844303818,28.1352209252,29.1622179084,28.531021647,27.9187405546,27.3534467567,25.7590353317,24.3219740617,22.24275987,20.6421490147,18.3817863304,16.5059589549,15.0048274253,12.8210801128,10.9569406541,9.13630283398,7.64553483445,6.14900209593,5.14865535069,3.91666928698,3.00868999155,2.08480261656,1.42472456604,1.08883244164,0.648938982298,0.412446558003,0.231033431798,0.154043291178,0.0660025643798,0.0275124869269,0.0164858047125,0.0110119311452,0.0385337862807,0.0275169597793,0.110038345104,0.225530279531,0.41799070126,0.610404200696,0.978992835813,1.38572990533,1.93591878708,3.00872533561,3.68016630009,5.03289744201,6.06679261183,7.58509241972,8.60273744443,11.0227659294,13.0794696076,14.7975852622,17.5234049154,19.1307839562,20.8297447523,21.995095471,24.8672192431,26.0051275292,27.2372622817,28.3708845921,29.1638185477,28.6788776548,28.3054005698,27.8429092524,26.1823272365,25.3241976987,23.8058450779,21.2251635958,18.8882749157,16.2964580217,14.4489221488,12.0947514394,9.80789289355,7.83800155311,5.88018407048,4.22423334592,3.19598144524,2.42552022155,1.41915157878,1.03408407776,0.742616600056,0.451078840476,0.324496141387,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0])

    # Creating weights for histo: y5_ETA_4
    y5_ETA_4_weights = numpy.array([0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0167754766607,0.0157879032402,0.0315818790577,0.0365119981127,0.0513258238847,0.0789506392387,0.118418262919,0.175630037537,0.193426095983,0.289158372643,0.361182626243,0.595108964623,0.833820574054,1.17535995604,1.7527430075,2.31511657194,2.94576795051,3.5999360359,4.44373166987,5.00623269831,5.75533620995,6.48651459583,6.94944940691,7.49040982134,7.46549822549,7.78019000185,7.36074125727,7.3924028334,7.11927714698,6.72157343981,6.24195206823,5.71696072827,5.22840485192,4.64413473626,3.96805045898,3.42421649298,3.00676989517,2.47605910934,2.03192483714,1.53562572332,1.24542186531,0.93551640217,0.627632726468,0.456933180759,0.28819698145,0.19338661421,0.104623531853,0.0424281153255,0.032555479538,0.00888348710434,0.0128293395878,0.0227028451767,0.0680983624602,0.112483170405,0.178604558239,0.290135877209,0.47462943249,0.68576633034,0.961185166233,1.23953928155,1.50597511222,1.94497555144,2.40685898496,2.99902024442,3.5339521729,4.04411199443,4.66187548015,5.14336472038,5.62318249875,6.19465811498,6.80427272308,6.99877156088,7.33019799736,7.60178449588,7.7399065685,7.63029153846,7.39221845151,6.91086549354,6.66314843239,5.83711759211,5.00930305751,4.32338240755,3.60307413539,2.90824583629,2.27578711442,1.70623347892,1.27997262539,0.855648583308,0.593118441936,0.426296126583,0.283251418408,0.184551795907,0.139142425932,0.0976929775805,0.0878398902811,0.0552575270627,0.0414515727516,0.0306072324107,0.0246765049377,0.00888474170281,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0])

    # Creating weights for histo: y5_ETA_5
    y5_ETA_5_weights = numpy.array([0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.00125909504944,0.00403076808609,0.0042845783041,0.0055469717621,0.00856990879258,0.00983432674686,0.0131070370057,0.0184042635463,0.0246991706542,0.0315067514369,0.0340327346461,0.0494093520076,0.0690659705511,0.0988161833973,0.119227907044,0.169635543767,0.250812323113,0.355941894148,0.486237994404,0.66775649111,0.83689795376,1.00249734812,1.23086452912,1.31459025331,1.44696350275,1.52501343559,1.57705059177,1.58809769981,1.49382298969,1.49781036714,1.34734708318,1.23766259557,1.09227255525,0.94983043757,0.791005103774,0.653124904382,0.525582039043,0.400570994344,0.322918718981,0.230139575479,0.145715960218,0.0897299960463,0.0647832807099,0.0312559019447,0.0128610367022,0.00932775056683,0.00151258638928,0.000755219131346,0.000251949241812,0.0,0.0,0.0,0.000504884165251,0.00226796636005,0.00756156161046,0.0128559474547,0.0312568461761,0.054200646526,0.103354015783,0.140911862561,0.219798640545,0.301988228166,0.405072097726,0.516498212271,0.653644231688,0.803378937045,0.931417123805,1.09682007001,1.22958901645,1.35365102851,1.49755030339,1.52909363579,1.58776801899,1.60748165151,1.56037690445,1.46990392627,1.32865730165,1.1865420641,1.028486519,0.8543170238,0.680885309455,0.498629832089,0.34231615399,0.24679433816,0.177718685236,0.119998455933,0.0854651505794,0.0678111829576,0.051931970392,0.0453727224846,0.0274824649397,0.0209192400574,0.0156289192097,0.0156310997442,0.0100868046383,0.00907838543848,0.0063026370028,0.00479003020852,0.00176425048119,0.00176501106763,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0])

    # Creating weights for histo: y5_ETA_6
    y5_ETA_6_weights = numpy.array([0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.000571063993231,0.000861051475344,0.00143071372932,0.000861317887775,0.00143062375889,0.00343227182406,0.00257613823223,0.00457075061001,0.00543813750292,0.00629209680944,0.00888042303551,0.0114557745263,0.017738719344,0.0163117883713,0.0223258015859,0.0254756962263,0.0354858559213,0.0449549434648,0.069290004614,0.0970480106529,0.135142079264,0.176674827592,0.241047868395,0.294337052424,0.352410263959,0.391404946541,0.458704425434,0.468931763743,0.471809817737,0.481049780593,0.423203894337,0.406565763233,0.328655771979,0.279925089587,0.222769976276,0.174390778351,0.1294400535,0.0896168632455,0.058415099158,0.0412256392743,0.0209068180009,0.00916353897628,0.00373175138616,0.00142987300566,0.000284898354891,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.000286303992863,0.000861330383667,0.00172023356515,0.00257590530879,0.0105976066032,0.0214652344513,0.038940450408,0.0526727866363,0.08501707518,0.128017820983,0.170366501117,0.227851705928,0.28914275977,0.340421204722,0.402607564279,0.430865575968,0.449571427419,0.463830140629,0.475241289824,0.440059753874,0.429712554962,0.359038785187,0.299765867991,0.229574639606,0.173197870456,0.135379701158,0.0933356109059,0.0598255955327,0.0509814625687,0.0380718059284,0.0234763933903,0.0220369965151,0.0188888912864,0.0137574579709,0.0154706148621,0.00630197056397,0.00744466696359,0.00628976757505,0.00601144805771,0.00285853840826,0.00429372466748,0.000860237942749,0.000855091634323,0.000572872398814,0.000571710280798,0.000286303992863,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0])

    # Creating weights for histo: y5_ETA_7
    y5_ETA_7_weights = numpy.array([0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,6.4851705081e-05,0.000129580745214,0.000151094215836,0.000172745899305,6.48132334642e-05,0.000302601058622,0.000324065999688,0.000626576914032,0.000410453554306,0.000797484766884,0.000971940138653,0.000926988694589,0.00136056214001,0.00140404009601,0.00194401019235,0.00207170746276,0.00222256188056,0.00304553430314,0.00265309950472,0.0036718618641,0.00414703117368,0.00660532516238,0.00954224755354,0.013667155033,0.0198434378515,0.0234966740889,0.029582653378,0.0326067236201,0.0331693521577,0.0327787185686,0.0292588589846,0.0240382270534,0.0205348163905,0.0128502743689,0.00993283504382,0.00621404618879,0.00302455805219,0.00136039115505,0.000540154491892,0.000151257154449,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,6.48341875038e-05,0.000539996498433,0.00177103501395,0.00321874039507,0.00645337903911,0.00889352724854,0.0138452350346,0.0191328109317,0.0253926500788,0.0292352856899,0.0324335761995,0.0337106788186,0.0326049509084,0.02997350908,0.0253047269284,0.0202097857087,0.0153558620442,0.0102799680466,0.00585119346542,0.00436242151919,0.00319434695932,0.00315379293002,0.0022450308973,0.00284766740193,0.00246206278228,0.00190086624375,0.00155498503527,0.00146743612395,0.00114438308445,0.000540125575317,0.000583166010964,0.000583064593412,0.000603241238211,0.000539986859574,0.000259101519966,0.000216086438707,0.000194604902041,0.000129670218963,0.000129670554228,0.000129657814172,6.48701027278e-05,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0])

    # Creating weights for histo: y5_ETA_8
    y5_ETA_8_weights = numpy.array([0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,2.83609323266e-05,2.84403582786e-05,0.0,2.84084809468e-05,2.84084809468e-05,0.00014151919166,5.68199178998e-05,0.000198647172926,0.000170489655409,0.000226253150215,0.000338072918116,0.000169635533052,0.000255509143354,0.000198956588034,0.000339252943856,0.000225606988084,0.000340842354155,0.000255634810748,0.000227107421115,0.00065233424181,0.00070995853501,0.00158596707169,0.00232679863914,0.00238123817002,0.00311559326186,0.00286392573805,0.00243204730953,0.00221527105535,0.00178341193742,0.00082054851526,0.000794512043506,0.000139487390543,0.000114810027991,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.00017042771297,0.000595748412853,0.000964870386886,0.00178601441111,0.00244072222181,0.00297741408968,0.00286680450175,0.00218015994205,0.00226895004598,0.00172894269794,0.00167463388491,0.000848095372428,0.000483023423797,0.000281790859632,0.000170171773349,0.000255511520042,0.000113426884528,0.000197307463441,0.000169967823785,0.00025556157904,0.000198864936991,0.000113578844036,0.00031204818126,0.000113600026271,0.000170438110981,0.000170526791164,0.000142239580737,5.69003687986e-05,5.68209428466e-05,2.84084809468e-05,0.000142108610358,0.0,2.84191760442e-05,2.83795596211e-05,2.846001052e-05,0.0,2.83795596211e-05,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0])

    # Creating weights for histo: y5_ETA_9
    y5_ETA_9_weights = numpy.array([0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,2.61044184661,10.4202956717,10.4180422915,2.60497489995,10.4224375366,2.59814015914,2.60470726297,0.0,5.21281459223,0.0,2.60491145153,2.60300492261,2.60874988872,2.61303900198,7.81121585124,7.81489585965,2.60300492261,0.0,13.0399694559,0.0,2.60491145153,5.22349315374,0.0,2.60667147227,2.60874988872,0.0,10.4310011508,2.60604506331,2.60197552005,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,2.60457267541,0.0,0.0,2.61044184661,0.0,5.21621388945,2.60966469959,0.0,5.21616389978,2.60470726297,0.0,2.60133257605,7.8155918696,0.0,0.0,10.4400492801,7.82094460911,2.6035159708,2.60470726297,0.0,10.4209378467,0.0,5.21501413749,5.21415662247,5.21675608505,5.21415662247,2.60604506331,5.22102827872,10.4298475431,7.82003710442,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0])

    # Creating weights for histo: y5_ETA_10
    y5_ETA_10_weights = numpy.array([0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,8.43199244658,7.37417326586,3.15627328046,7.37242648333,8.42784479996,7.37060659757,11.5899905786,13.6882957786,17.9047363926,17.9089917703,13.6950943793,16.8505723736,14.741898057,8.42060373229,24.2293973136,18.9630365157,9.48010813493,6.31498436139,15.8070621889,10.5403705027,15.7924299996,11.5844154952,17.9049980252,21.059929669,15.79371123,11.5888440121,28.4238569395,11.5821954654,21.0667744402,25.271884053,17.9023970891,17.8937516699,12.6357823536,7.3733498926,5.26706489752,3.15965565166,4.21191975613,5.26752660215,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,1.05407975795,0.0,5.26421387141,4.21098095671,4.21108099271,9.48257055964,6.31438029783,4.21168505628,10.5274273828,12.6333853371,13.6898078613,9.47827670655,16.851161047,17.9047787155,16.8577095577,8.4195379641,21.0647929578,24.2179316485,16.8502222476,12.6317770659,15.8025182458,14.7498009013,11.5816529624,13.7046247325,11.5831727402,11.5876897505,16.8499221395,13.6906889476,18.9571805619,17.9103268662,15.8055962767,14.747727078,22.1197957402,15.80666974,15.805076859,8.42579790942,13.6961409098,10.5363883002,6.32292183355,8.43101517178,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0])

    # Creating weights for histo: y5_ETA_11
    y5_ETA_11_weights = numpy.array([0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,2.7636220316,2.30392106087,1.61246244355,1.84179516933,3.22420521088,1.15151347048,6.45030471103,7.36958830745,8.98089458134,8.52074751125,9.67294415543,14.5112394385,14.508288497,14.971855278,18.428760285,18.4274192973,18.6564438648,20.726348733,20.2698596008,21.1918559117,21.4253837389,27.6366698735,26.2597982265,27.6360512516,33.849980938,28.0984422668,31.7867195305,33.4066288747,34.7800462295,34.7826283033,36.6203693862,37.5448209726,30.6385074258,32.9384051393,31.7874803201,26.4849957919,26.4914279221,20.496751652,15.8924222266,11.9820097678,8.98113280839,6.21977393375,5.7608448955,4.14560019057,1.15200452559,1.38244039629,0.0,0.0,0.230000568406,0.229459447194,0.0,0.460966263746,0.461235614005,0.691040951503,1.6116132794,1.38323038792,2.76498991594,7.36739431318,12.4421568379,8.52329116134,14.5138599361,14.9661570407,21.6573784598,18.6546610043,27.1796850753,33.62351539,37.0846969567,35.2425525158,32.474473333,37.5460313197,40.7715218039,35.2411423654,28.0959908336,28.0972319197,30.8599663634,34.3181739345,32.715751224,29.2505812754,29.4738230735,25.7981641586,21.4223098415,16.8202819967,21.4247920137,16.8148335136,16.3575374833,13.8241542087,13.585773466,17.2814127139,14.2837595044,9.67406612798,8.2920072792,8.29606098139,5.52895007625,5.2982925007,3.91405886952,3.45270260504,2.07207849787,1.84486560859,2.30382269615,1.8429928366,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0])

    # Creating weights for histo: y5_ETA_12
    y5_ETA_12_weights = numpy.array([0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0830918579289,0.359816305847,0.276975822085,0.221613412484,0.359909869051,0.470676776306,0.526362656063,0.692229211126,0.775463914522,0.941514364369,0.94111464328,0.913893598628,1.19079143855,2.04869176844,2.63047292587,2.85162987148,3.35036098973,4.48648258644,4.90105760378,6.0086697382,6.5073054466,7.67033223521,10.4414688975,10.9100774346,10.9941842917,12.1282803527,13.2082351733,12.9318313102,14.6207625567,14.4257109761,15.8680077704,15.9788447731,14.61984693,13.485931686,14.2323406093,11.5469958651,12.4622340501,10.3011087029,8.11314548927,7.39360520969,5.53726430767,4.54171642358,3.32318880415,2.65824488543,1.74389385815,1.68904743115,0.775146522897,0.498785363357,0.304543573806,0.0830972824403,0.110716855558,0.13854817698,0.277117359514,0.609126080986,1.30077013737,1.55044885623,2.79627292487,3.1287770081,4.34704186574,5.51032256765,8.11262996833,8.47386395677,10.1628567581,11.7408509755,13.7356784998,14.2616483596,14.9805500088,15.6739910789,16.0052055903,16.0329667778,14.8438523212,14.1495379433,13.9837133224,13.7349436901,12.876258922,11.9354370484,10.7987172166,10.0240739037,8.75034091616,7.69863202667,5.73236590152,4.5962577699,3.62750581804,3.2667504177,2.3540167412,2.18794205417,1.99418043006,1.46770697546,1.163177213,0.720175062835,0.913628143815,0.858196177358,0.498544530439,0.775235007835,0.636782625419,0.664471870807,0.24925564544,0.304651025298,0.304872545417,0.138512321344,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0])

    # Creating weights for histo: y5_ETA_13
    y5_ETA_13_weights = numpy.array([0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0201375982519,0.0201722656338,0.0503371537826,0.0807260904303,0.0403171517425,0.171408327683,0.141113295767,0.0806235992558,0.161202900964,0.171330169819,0.181533533364,0.161379484338,0.171370705108,0.181437595799,0.252078530386,0.272316016573,0.332637078997,0.514168549187,0.544494285978,0.604979067282,0.78647261149,1.06888282546,1.22012072009,1.68370183436,1.79472180375,1.97580653621,2.09723036107,2.38938603544,2.7630437355,2.81260601596,2.86360705647,2.6617030836,3.15591200752,2.3185384801,2.3291213462,1.80472516084,1.64358039282,1.4617365339,1.09892627158,0.796782410512,0.605211841791,0.504171867075,0.302527489964,0.151214107456,0.0605005281721,0.0403345309446,0.0201603295687,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0201682849227,0.0604560364438,0.171425621931,0.272116556247,0.403084560733,0.564502820595,0.736080207137,1.20955909255,1.39126277704,1.49215499213,2.18767502996,2.17761887991,2.26800104679,2.57082090057,2.78232105718,2.90372182304,2.5602119414,2.25847950139,2.41947195866,2.21760014702,2.00645740486,1.79483224421,1.64378124882,1.56276103481,0.978107441996,0.947653788452,0.725819560188,0.564608345848,0.382912610643,0.332733623377,0.322641549834,0.241772372258,0.15122891376,0.181446880079,0.191558735815,0.161246531014,0.221775306458,0.12101555924,0.181532501777,0.0705946952291,0.131024377666,0.0402771443823,0.0907135489436,0.0706058606383,0.050466745347,0.0100722003281,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0])

    # Creating weights for histo: y5_ETA_14
    y5_ETA_14_weights = numpy.array([0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.011321022953,0.0169796049691,0.0141261543475,0.0311413783472,0.0395851392527,0.0311350686464,0.0339501378197,0.0396116476909,0.0367794884621,0.0509215170935,0.0452571370778,0.0650779464627,0.0735556450944,0.101846189037,0.0593818640479,0.0876997243785,0.116003272461,0.124484818471,0.0904924979931,0.1273270309,0.152794714728,0.181128041521,0.243272746578,0.288561893845,0.367835128201,0.475264748409,0.59987518379,0.679022685814,0.713051210124,0.7779703368,0.800649094393,0.828904242453,0.695928836632,0.713026971639,0.605393094104,0.472532724902,0.370670338401,0.297114308568,0.192374159861,0.104698135334,0.0650520151313,0.0424087688432,0.00847835268601,0.0141419247521,0.00282703490529,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.00283493011081,0.00849583132675,0.0226260100322,0.0367833820092,0.0989995521231,0.132969250015,0.203706959639,0.265951542644,0.398975463908,0.427180596047,0.684739505599,0.687384963089,0.738466992816,0.876999167474,0.749710571886,0.837497362441,0.721439264836,0.554485350626,0.611061821657,0.560147152898,0.393222863502,0.331008597841,0.260215485966,0.240489129724,0.121630255957,0.127329031537,0.0763679249182,0.0933681826154,0.10461607075,0.0764064756513,0.0933156658982,0.0481139310715,0.0565862433731,0.0848853284965,0.0650554392982,0.0622776319862,0.0452686792135,0.0594268399031,0.0367983790908,0.019782331752,0.0226152296775,0.0283148670701,0.0141388468493,0.0113148632999,0.0141477766149,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0])

    # Creating weights for histo: y5_ETA_15
    y5_ETA_15_weights = numpy.array([0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.00152630680853,0.0,0.00151102038833,0.00152482248354,0.0,0.00458316304242,0.0030430423208,0.00153139322156,0.00304328222364,0.00761761613229,0.006083680886,0.00458355421405,0.00456873341809,0.00305755703382,0.00305755703382,0.00151713731999,0.00457778354611,0.00913584424206,0.00762089677415,0.00455999173658,0.00457121280808,0.00305420075756,0.00760781084211,0.00761126638851,0.0137157065522,0.0274305385818,0.0228560167689,0.0243405308473,0.0594462114274,0.0716529763553,0.0669593185532,0.0700317531088,0.0746248053483,0.0441824697232,0.0503036085431,0.0274083446141,0.0106366114428,0.0091253889688,0.00456185777891,0.00152149220661,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0030507416658,0.00913618932398,0.0106430356392,0.00757468652267,0.0243267039346,0.0442204405528,0.0441913922182,0.0654277693357,0.0488197680835,0.0700668167414,0.0625147815381,0.0701083802048,0.0410819440808,0.0487325167187,0.0167727424178,0.0228544331738,0.00458555852551,0.00152904619176,0.00611407882187,0.00458068010706,0.00457648121638,0.00911938785231,0.00454154285326,0.00306410768146,0.00304047311496,0.00455446451685,0.00609631655703,0.00150836018486,0.0045673519086,0.00150836018486,0.00610149633127,0.00152291862402,0.00151868191614,0.00153139322156,0.00303734019652,0.00151868191614,0.00304712066917,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0])

    # Creating weights for histo: y5_ETA_16
    y5_ETA_16_weights = numpy.array([0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.000180814992037,0.0,0.0,0.0,0.0,0.00018074597996,0.000721641419282,0.000542391021916,0.000541503338672,0.000540848263098,0.0,0.000360966782637,0.000361041263304,0.00018082693051,0.000180214332794,0.000723169928955,0.000360670323391,0.00036109360003,0.000361431920954,0.000361293049554,0.000902631367718,0.000361747327712,0.0,0.000180593706661,0.0,0.000902138039199,0.0012649251309,0.00289031551303,0.00379190053134,0.00433438975683,0.00523714243484,0.00613714926403,0.00270716200517,0.00487417434048,0.00216652478347,0.00126379829308,0.000541152116494,0.00018005840093,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.000181030269666,0.00144235587389,0.00108270166861,0.00253036708215,0.00451414850208,0.00523849802921,0.00487345418097,0.00559690639705,0.00632232653563,0.00342879225621,0.00288886941733,0.00216554929468,0.000361311265353,0.000541495636431,0.0,0.000360520322253,0.0,0.000361420637172,0.000180700690785,0.000721545526385,0.000722368125695,0.000361311265353,0.000361266399801,0.000541950068634,0.000361263935084,0.000904138696228,0.0,0.000722628461432,0.000361480329537,0.000180461882811,0.0,0.0,0.000540693833171,0.0,0.000542156103573,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0])

    # Creating a new Canvas
    fig   = plt.figure(figsize=(12,6),dpi=80)
    frame = gridspec.GridSpec(1,1,right=0.7)
    pad   = fig.add_subplot(frame[0])

    # Creating a new Stack
    pad.hist(x=xData, bins=xBinning, weights=y5_ETA_0_weights+y5_ETA_1_weights+y5_ETA_2_weights+y5_ETA_3_weights+y5_ETA_4_weights+y5_ETA_5_weights+y5_ETA_6_weights+y5_ETA_7_weights+y5_ETA_8_weights+y5_ETA_9_weights+y5_ETA_10_weights+y5_ETA_11_weights+y5_ETA_12_weights+y5_ETA_13_weights+y5_ETA_14_weights+y5_ETA_15_weights+y5_ETA_16_weights,\
             label="$bg\_dip\_1600\_inf$", histtype="step", rwidth=1.0,\
             color=None, edgecolor="#e5e5e5", linewidth=1, linestyle="solid",\
             bottom=None, cumulative=False, normed=False, align="mid", orientation="vertical")

    pad.hist(x=xData, bins=xBinning, weights=y5_ETA_0_weights+y5_ETA_1_weights+y5_ETA_2_weights+y5_ETA_3_weights+y5_ETA_4_weights+y5_ETA_5_weights+y5_ETA_6_weights+y5_ETA_7_weights+y5_ETA_8_weights+y5_ETA_9_weights+y5_ETA_10_weights+y5_ETA_11_weights+y5_ETA_12_weights+y5_ETA_13_weights+y5_ETA_14_weights+y5_ETA_15_weights,\
             label="$bg\_dip\_1200\_1600$", histtype="step", rwidth=1.0,\
             color=None, edgecolor="#f2f2f2", linewidth=1, linestyle="solid",\
             bottom=None, cumulative=False, normed=False, align="mid", orientation="vertical")

    pad.hist(x=xData, bins=xBinning, weights=y5_ETA_0_weights+y5_ETA_1_weights+y5_ETA_2_weights+y5_ETA_3_weights+y5_ETA_4_weights+y5_ETA_5_weights+y5_ETA_6_weights+y5_ETA_7_weights+y5_ETA_8_weights+y5_ETA_9_weights+y5_ETA_10_weights+y5_ETA_11_weights+y5_ETA_12_weights+y5_ETA_13_weights+y5_ETA_14_weights,\
             label="$bg\_dip\_800\_1200$", histtype="step", rwidth=1.0,\
             color=None, edgecolor="#ccc6aa", linewidth=1, linestyle="solid",\
             bottom=None, cumulative=False, normed=False, align="mid", orientation="vertical")

    pad.hist(x=xData, bins=xBinning, weights=y5_ETA_0_weights+y5_ETA_1_weights+y5_ETA_2_weights+y5_ETA_3_weights+y5_ETA_4_weights+y5_ETA_5_weights+y5_ETA_6_weights+y5_ETA_7_weights+y5_ETA_8_weights+y5_ETA_9_weights+y5_ETA_10_weights+y5_ETA_11_weights+y5_ETA_12_weights+y5_ETA_13_weights,\
             label="$bg\_dip\_600\_800$", histtype="step", rwidth=1.0,\
             color=None, edgecolor="#ccc6aa", linewidth=1, linestyle="solid",\
             bottom=None, cumulative=False, normed=False, align="mid", orientation="vertical")

    pad.hist(x=xData, bins=xBinning, weights=y5_ETA_0_weights+y5_ETA_1_weights+y5_ETA_2_weights+y5_ETA_3_weights+y5_ETA_4_weights+y5_ETA_5_weights+y5_ETA_6_weights+y5_ETA_7_weights+y5_ETA_8_weights+y5_ETA_9_weights+y5_ETA_10_weights+y5_ETA_11_weights+y5_ETA_12_weights,\
             label="$bg\_dip\_400\_600$", histtype="step", rwidth=1.0,\
             color=None, edgecolor="#c1bfa8", linewidth=1, linestyle="solid",\
             bottom=None, cumulative=False, normed=False, align="mid", orientation="vertical")

    pad.hist(x=xData, bins=xBinning, weights=y5_ETA_0_weights+y5_ETA_1_weights+y5_ETA_2_weights+y5_ETA_3_weights+y5_ETA_4_weights+y5_ETA_5_weights+y5_ETA_6_weights+y5_ETA_7_weights+y5_ETA_8_weights+y5_ETA_9_weights+y5_ETA_10_weights+y5_ETA_11_weights,\
             label="$bg\_dip\_200\_400$", histtype="step", rwidth=1.0,\
             color=None, edgecolor="#bab5a3", linewidth=1, linestyle="solid",\
             bottom=None, cumulative=False, normed=False, align="mid", orientation="vertical")

    pad.hist(x=xData, bins=xBinning, weights=y5_ETA_0_weights+y5_ETA_1_weights+y5_ETA_2_weights+y5_ETA_3_weights+y5_ETA_4_weights+y5_ETA_5_weights+y5_ETA_6_weights+y5_ETA_7_weights+y5_ETA_8_weights+y5_ETA_9_weights+y5_ETA_10_weights,\
             label="$bg\_dip\_100\_200$", histtype="step", rwidth=1.0,\
             color=None, edgecolor="#b2a596", linewidth=1, linestyle="solid",\
             bottom=None, cumulative=False, normed=False, align="mid", orientation="vertical")

    pad.hist(x=xData, bins=xBinning, weights=y5_ETA_0_weights+y5_ETA_1_weights+y5_ETA_2_weights+y5_ETA_3_weights+y5_ETA_4_weights+y5_ETA_5_weights+y5_ETA_6_weights+y5_ETA_7_weights+y5_ETA_8_weights+y5_ETA_9_weights,\
             label="$bg\_dip\_0\_100$", histtype="step", rwidth=1.0,\
             color=None, edgecolor="#b7a39b", linewidth=1, linestyle="solid",\
             bottom=None, cumulative=False, normed=False, align="mid", orientation="vertical")

    pad.hist(x=xData, bins=xBinning, weights=y5_ETA_0_weights+y5_ETA_1_weights+y5_ETA_2_weights+y5_ETA_3_weights+y5_ETA_4_weights+y5_ETA_5_weights+y5_ETA_6_weights+y5_ETA_7_weights+y5_ETA_8_weights,\
             label="$bg\_vbf\_1600\_inf$", histtype="step", rwidth=1.0,\
             color=None, edgecolor="#ad998c", linewidth=1, linestyle="solid",\
             bottom=None, cumulative=False, normed=False, align="mid", orientation="vertical")

    pad.hist(x=xData, bins=xBinning, weights=y5_ETA_0_weights+y5_ETA_1_weights+y5_ETA_2_weights+y5_ETA_3_weights+y5_ETA_4_weights+y5_ETA_5_weights+y5_ETA_6_weights+y5_ETA_7_weights,\
             label="$bg\_vbf\_1200\_1600$", histtype="step", rwidth=1.0,\
             color=None, edgecolor="#9b8e82", linewidth=1, linestyle="solid",\
             bottom=None, cumulative=False, normed=False, align="mid", orientation="vertical")

    pad.hist(x=xData, bins=xBinning, weights=y5_ETA_0_weights+y5_ETA_1_weights+y5_ETA_2_weights+y5_ETA_3_weights+y5_ETA_4_weights+y5_ETA_5_weights+y5_ETA_6_weights,\
             label="$bg\_vbf\_800\_1200$", histtype="step", rwidth=1.0,\
             color=None, edgecolor="#876656", linewidth=1, linestyle="solid",\
             bottom=None, cumulative=False, normed=False, align="mid", orientation="vertical")

    pad.hist(x=xData, bins=xBinning, weights=y5_ETA_0_weights+y5_ETA_1_weights+y5_ETA_2_weights+y5_ETA_3_weights+y5_ETA_4_weights+y5_ETA_5_weights,\
             label="$bg\_vbf\_600\_800$", histtype="step", rwidth=1.0,\
             color=None, edgecolor="#afcec6", linewidth=1, linestyle="solid",\
             bottom=None, cumulative=False, normed=False, align="mid", orientation="vertical")

    pad.hist(x=xData, bins=xBinning, weights=y5_ETA_0_weights+y5_ETA_1_weights+y5_ETA_2_weights+y5_ETA_3_weights+y5_ETA_4_weights,\
             label="$bg\_vbf\_400\_600$", histtype="step", rwidth=1.0,\
             color=None, edgecolor="#84c1a3", linewidth=1, linestyle="solid",\
             bottom=None, cumulative=False, normed=False, align="mid", orientation="vertical")

    pad.hist(x=xData, bins=xBinning, weights=y5_ETA_0_weights+y5_ETA_1_weights+y5_ETA_2_weights+y5_ETA_3_weights,\
             label="$bg\_vbf\_200\_400$", histtype="step", rwidth=1.0,\
             color=None, edgecolor="#89a8a0", linewidth=1, linestyle="solid",\
             bottom=None, cumulative=False, normed=False, align="mid", orientation="vertical")

    pad.hist(x=xData, bins=xBinning, weights=y5_ETA_0_weights+y5_ETA_1_weights+y5_ETA_2_weights,\
             label="$bg\_vbf\_100\_200$", histtype="step", rwidth=1.0,\
             color=None, edgecolor="#829e8c", linewidth=1, linestyle="solid",\
             bottom=None, cumulative=False, normed=False, align="mid", orientation="vertical")

    pad.hist(x=xData, bins=xBinning, weights=y5_ETA_0_weights+y5_ETA_1_weights,\
             label="$bg\_vbf\_0\_100$", histtype="step", rwidth=1.0,\
             color=None, edgecolor="#adbcc6", linewidth=1, linestyle="solid",\
             bottom=None, cumulative=False, normed=False, align="mid", orientation="vertical")

    pad.hist(x=xData, bins=xBinning, weights=y5_ETA_0_weights,\
             label="$signal$", histtype="step", rwidth=1.0,\
             color=None, edgecolor="#7a8e99", linewidth=1, linestyle="solid",\
             bottom=None, cumulative=False, normed=False, align="mid", orientation="vertical")


    # Axis
    plt.rc('text',usetex=False)
    plt.xlabel(r"\eta [ j_{2} ] ",\
               fontsize=16,color="black")
    plt.ylabel(r"$\mathrm{Events}$ $(\mathcal{L}_{\mathrm{int}} = 40.0\ \mathrm{fb}^{-1})$ ",\
               fontsize=16,color="black")

    # Boundary of y-axis
    ymax=(y5_ETA_0_weights+y5_ETA_1_weights+y5_ETA_2_weights+y5_ETA_3_weights+y5_ETA_4_weights+y5_ETA_5_weights+y5_ETA_6_weights+y5_ETA_7_weights+y5_ETA_8_weights+y5_ETA_9_weights+y5_ETA_10_weights+y5_ETA_11_weights+y5_ETA_12_weights+y5_ETA_13_weights+y5_ETA_14_weights+y5_ETA_15_weights+y5_ETA_16_weights).max()*1.1
    ymin=0 # linear scale
    #ymin=min([x for x in (y5_ETA_0_weights+y5_ETA_1_weights+y5_ETA_2_weights+y5_ETA_3_weights+y5_ETA_4_weights+y5_ETA_5_weights+y5_ETA_6_weights+y5_ETA_7_weights+y5_ETA_8_weights+y5_ETA_9_weights+y5_ETA_10_weights+y5_ETA_11_weights+y5_ETA_12_weights+y5_ETA_13_weights+y5_ETA_14_weights+y5_ETA_15_weights+y5_ETA_16_weights) if x])/100. # log scale
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
    plt.savefig('../../HTML/MadAnalysis5job_0/selection_4.png')
    plt.savefig('../../PDF/MadAnalysis5job_0/selection_4.png')
    plt.savefig('../../DVI/MadAnalysis5job_0/selection_4.eps')

# Running!
if __name__ == '__main__':
    selection_4()
