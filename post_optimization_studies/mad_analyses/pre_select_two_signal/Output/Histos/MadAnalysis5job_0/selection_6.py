def selection_6():

    # Library import
    import numpy
    import matplotlib
    import matplotlib.pyplot   as plt
    import matplotlib.gridspec as gridspec

    # Library version
    matplotlib_version = matplotlib.__version__
    numpy_version      = numpy.__version__

    # Histo binning
    xBinning = numpy.linspace(0.0,15.0,76,endpoint=True)

    # Creating data sequence: middle of each bin
    xData = numpy.array([0.1,0.3,0.5,0.7,0.9,1.1,1.3,1.5,1.7,1.9,2.1,2.3,2.5,2.7,2.9,3.1,3.3,3.5,3.7,3.9,4.1,4.3,4.5,4.7,4.9,5.1,5.3,5.5,5.7,5.9,6.1,6.3,6.5,6.7,6.9,7.1,7.3,7.5,7.7,7.9,8.1,8.3,8.5,8.7,8.9,9.1,9.3,9.5,9.7,9.9,10.1,10.3,10.5,10.7,10.9,11.1,11.3,11.5,11.7,11.9,12.1,12.3,12.5,12.7,12.9,13.1,13.3,13.5,13.7,13.9,14.1,14.3,14.5,14.7,14.9])

    # Creating weights for histo: y7_DELTAR_0
    y7_DELTAR_0_weights = numpy.array([0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,106.208708076,196.29087011,253.366460711,299.961260383,337.450787936,373.417316807,397.674735812,418.931237414,344.406621916,262.320252961,201.527185578,160.856540778,129.356688042,105.856628381,86.1231654603,72.0231376639,60.2690278371,50.0051567205,42.038043616,35.8232329949,29.9072821152,25.3792260342,20.8225099781,17.5799967845,15.0866989424,11.6067299544,9.80123551702,7.49626951197,6.10018672028,4.73275990379,3.57413530658,2.72666004007,1.92012553813,1.44930554562,0.925262799184,0.552701521636,0.364373484634,0.13101068661,0.0163763338263,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0])

    # Creating weights for histo: y7_DELTAR_1
    y7_DELTAR_1_weights = numpy.array([0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.548625334741,1.12016787511,1.62643079945,2.2243629463,2.87576870628,3.28133480589,3.85912774779,4.40636508219,4.6584531441,4.48136510061,4.28483305234,3.94037976774,3.75912492323,3.45425604835,3.22786119275,2.88549110867,2.63826264795,2.34728297649,2.12019372071,1.8562980559,1.62087519808,1.41739794811,1.17780828927,1.02919345277,0.915301424795,0.738213381303,0.619460552137,0.500012922802,0.406954899947,0.384037694318,0.281951749246,0.215977813043,0.164587600422,0.128475551553,0.0944469031959,0.0701406972263,0.0409732900629,0.0284729589929,0.00972247438781,0.00347231205279,0.00208338731167,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0])

    # Creating weights for histo: y7_DELTAR_2
    y7_DELTAR_2_weights = numpy.array([0.0,0.0,3.80346529445,5.44328076242,7.25370336625,10.9365560698,18.224696028,32.6490575793,71.640168137,136.547515902,245.738630447,426.469771825,733.192173659,1211.74103188,1721.6709705,2044.9595481,1025.284732,565.668588855,369.475469794,285.402157821,256.987463156,246.989675739,240.353671981,234.045370627,225.802018814,220.455073987,207.092258334,195.559545054,185.409622967,178.036539149,161.177149642,145.665341645,128.953440252,117.744343612,101.205366224,85.1257169729,72.5636712496,59.9167056998,46.2966871198,35.5311283364,26.0041292274,19.6490218284,14.6537211901,9.94105937036,7.26601273544,4.83562733069,3.34138407295,1.82220202523,1.05748576939,0.425183957471,0.255061906091,0.048651690156,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0])

    # Creating weights for histo: y7_DELTAR_3
    y7_DELTAR_3_weights = numpy.array([0.0,0.0,2.17855089296,3.72465443151,18.8550853774,43.9159412862,68.7524610213,91.8172989329,100.237622158,98.2021466797,101.524607933,112.210936838,134.496831423,212.639668905,378.529763425,576.870527,505.554920548,501.082328875,504.777258175,509.688266308,504.453714265,499.709230009,483.689880972,464.643350985,451.447470066,428.251892316,398.038469482,369.243268113,341.892113873,312.424370911,280.293733475,250.51128931,214.588700723,180.620515693,148.243232843,118.88527994,89.3875792086,65.1906681811,44.4765854457,30.8924229094,20.0703584501,13.4845457217,8.34367678894,5.14110033075,3.20267934763,1.76731253442,0.883624036782,0.371539024957,0.110484749503,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0])

    # Creating weights for histo: y7_DELTAR_4
    y7_DELTAR_4_weights = numpy.array([0.0,0.0,6.27035340591,17.0294671262,17.9971781795,9.86751888062,6.30885433223,5.20876460597,6.35840543473,9.2513740574,13.9984850532,22.5959202474,40.2844450685,77.2638474446,172.551507243,362.40669661,361.007589929,366.66938332,367.963472701,370.31740398,363.618437803,348.27262752,329.101262495,312.526120112,288.097958778,262.073981377,236.068123015,208.630088695,181.035605005,156.060500577,128.980378213,105.305335136,81.3801193204,62.6479987987,44.3559352929,30.2406921282,18.2291628155,10.4627089947,6.08308135773,3.44855401164,1.95232481347,0.792079471894,0.324676235697,0.176061035071,0.0275332811513,0.0164857334575,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0])

    # Creating weights for histo: y7_DELTAR_5
    y7_DELTAR_5_weights = numpy.array([0.0,0.0,2.15825875953,0.822983700951,0.470774749636,0.357270782054,0.517144234479,0.79536996185,1.11911621122,1.60855611849,2.56769093315,3.99161687262,6.82405795149,13.2719548158,31.54641318,85.0800261203,86.8294186814,86.1723743486,85.4711182113,82.3001738405,78.0545579465,71.9156907731,65.4876230835,58.152271446,50.7102984124,42.8029991429,35.3414534672,28.4700211443,21.8035504179,15.7146309595,10.7035896827,6.96813712758,4.25928427594,2.35359236389,1.23651879416,0.560519902752,0.259549546843,0.101647908831,0.0335517532084,0.0128315362999,0.000987667662253,0.000986323671496,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0])

    # Creating weights for histo: y7_DELTAR_6
    y7_DELTAR_6_weights = numpy.array([0.0,0.0,0.166864637719,0.0801695517407,0.0604966852149,0.0922630233327,0.126792084872,0.18073950998,0.295678022605,0.430544504861,0.624129992583,1.01185950619,1.76506542861,3.44689026579,8.5328267865,27.2688375599,27.5877804576,26.3514346197,25.190995559,23.2315108364,21.146054952,18.8754692716,16.1034595527,13.5030202756,10.8988920859,8.36518131563,6.13429745636,4.31329499047,2.82763027791,1.68768988803,0.968978498612,0.476194197338,0.208732554689,0.0826807729477,0.0267190095476,0.00907671332907,0.00327711466798,0.000504083496383,0.000504337559232,0.000251541984564,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0])

    # Creating weights for histo: y7_DELTAR_7
    y7_DELTAR_7_weights = numpy.array([0.0,0.0,0.0260628621204,0.0263388794764,0.0249199557316,0.0366595154025,0.0541441567632,0.090187089119,0.126800440016,0.180636170302,0.273406032525,0.440072391729,0.78900707341,1.55566584792,4.05313558371,15.7287607139,15.6981309946,14.1111536563,12.8958315735,11.4667712311,9.68266305875,8.00078657284,6.23181432023,4.70749695033,3.36936108947,2.2660454123,1.38927469635,0.809907358326,0.410813312404,0.200961548182,0.0735794334021,0.027483815184,0.0100306232675,0.00286039991994,0.00143093571302,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0])

    # Creating weights for histo: y7_DELTAR_8
    y7_DELTAR_8_weights = numpy.array([0.0,0.0,0.00222494636072,0.00259152671815,0.00399414863175,0.00557153360633,0.00893884510288,0.0116833310422,0.0174252184103,0.0255880880466,0.0420477659107,0.0680626729438,0.126317599369,0.267415047193,0.782551487312,3.75849147699,3.61965911226,3.06057037062,2.53501132961,2.01994642902,1.52943044092,1.09714813114,0.727797136231,0.444742425151,0.239862396549,0.117786164961,0.0529282281559,0.0188474342755,0.00654274031783,0.00159827728264,0.000626337154784,0.000237723041973,6.47734891491e-05,4.32688832001e-05,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0])

    # Creating weights for histo: y7_DELTAR_9
    y7_DELTAR_9_weights = numpy.array([0.0,0.0,0.00031204174528,0.000596577177178,0.000907172863031,0.0012498475166,0.00212951332377,0.00269294636746,0.00348263915304,0.00552912508447,0.0108297065501,0.0179724189316,0.0355705077542,0.0859228672158,0.292804462415,1.92345356789,1.72205214886,1.2494041059,0.905775510474,0.601716642854,0.384017281713,0.215347918235,0.115560031875,0.0524788003918,0.0193568819884,0.00654326743897,0.00187024873815,0.00059551839676,0.000141957358155,0.000113491474901,0.0,2.84511078463e-05,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0])

    # Creating weights for histo: y7_DELTAR_10
    y7_DELTAR_10_weights = numpy.array([0.0,0.0,23922.6952189,21233.6362186,21313.4090542,23134.149237,26770.5462282,31411.9094512,38537.0548583,50140.3379462,67513.7510391,96509.7886527,143621.058285,220991.249576,319151.212354,410662.451893,279885.450753,211426.738066,166395.806788,131342.863017,102571.616687,80669.6166888,61439.9259337,48075.4189045,36387.610295,27282.8596369,20357.2847465,14928.3791428,11033.3645096,7746.77059496,5620.15507457,3810.65983919,2512.84855076,1686.36952045,1165.06215329,654.201851438,414.453834131,208.582547702,143.334974271,88.5729567583,65.1565571862,15.6315075131,2.60827218146,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0])

    # Creating weights for histo: y7_DELTAR_11
    y7_DELTAR_11_weights = numpy.array([0.0,0.0,7050.19607418,6327.04191875,6114.97328531,6663.94235985,7631.79286814,8681.68593083,10091.1841719,13189.797901,17548.8265876,25986.3586784,41043.3624709,74378.5031799,142972.665761,214210.058377,137684.512745,97097.4766333,72412.9524171,54111.533622,40549.2910733,30397.3993357,22808.6265773,16723.1298201,12605.3038579,8936.86701664,6457.42582537,4503.56794463,3210.27209504,2163.33784322,1418.76366694,979.52492177,601.413516377,326.483118247,230.689134395,130.593331946,56.8867366251,28.4423102203,18.9643771168,12.6358769544,2.10484996283,2.10712967082,1.05142402608,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0])

    # Creating weights for histo: y7_DELTAR_12
    y7_DELTAR_12_weights = numpy.array([0.0,0.0,1240.77669141,1088.80311166,1054.5258991,1148.45568203,1247.52416512,1426.65862234,1666.99294659,2103.65297393,2741.30364817,3933.46479342,6260.10407964,11920.9121528,28650.8430705,59123.2927158,35806.2352056,23474.3192558,16571.7815993,11942.0832593,8521.08988185,6115.64874019,4342.44753736,3036.68169665,2113.54038017,1427.63264693,993.425547791,623.720009309,407.914967081,234.481147284,148.796530548,85.686960542,49.2869123007,24.6442092423,11.7491226479,5.98716970944,2.30385441116,1.61207332884,0.0,0.230404691069,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0])

    # Creating weights for histo: y7_DELTAR_13
    y7_DELTAR_13_weights = numpy.array([0.0,0.0,104.536134156,92.9864951501,90.4101754194,94.3708914275,104.090865224,117.6581411,138.705965809,174.36872179,223.494149688,319.032689063,521.055443026,1048.09474035,2847.67871321,8553.29532973,5043.0880694,3097.07240314,2056.651954,1403.34848354,962.665736998,645.177908763,427.994467086,286.549139406,179.106023132,114.225984782,69.4464493699,40.7921971387,21.3496911921,11.3807068815,5.56627714081,2.60314743389,1.05230352047,0.498288789447,0.221571806678,0.0554093212851,0.0,0.0276409749514,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0])

    # Creating weights for histo: y7_DELTAR_14
    y7_DELTAR_14_weights = numpy.array([0.0,0.0,17.4412268964,15.6479327086,14.9112097987,15.868564244,17.2401777903,19.6494294943,23.3193782144,28.6322909329,38.2302057097,55.4690727456,94.4802757389,195.743584583,577.641067599,2175.7638516,1291.22545909,753.755436221,487.588350605,315.98595089,207.124392468,133.151295465,83.2955348792,49.31098432,30.0054397611,15.8803610344,8.70110383861,4.64761015061,1.97639202578,1.00805030239,0.393204500277,0.211687395844,0.0302186012096,0.0201784220911,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0])

    # Creating weights for histo: y7_DELTAR_15
    y7_DELTAR_15_weights = numpy.array([0.0,0.0,5.20569050425,4.64832324132,4.16155603688,4.71938883699,5.07287775115,5.66696089191,6.89153910553,8.68558085368,11.97012642,18.002137707,31.783869323,69.587919133,221.631204791,1038.29678514,620.115902393,348.412673768,213.528741947,132.985001855,82.0197237666,49.1317541718,29.2762168037,15.7413391579,7.84283545782,3.87033368113,1.86729998542,0.752527370149,0.265962001089,0.118844098694,0.036795727078,0.0226352944399,0.0169645900135,0.0,0.00282706141938,0.00283195840873,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0])

    # Creating weights for histo: y7_DELTAR_16
    y7_DELTAR_16_weights = numpy.array([0.0,0.0,0.461721635668,0.414196774259,0.425134772486,0.435821198882,0.441724333699,0.475219073016,0.627590660822,0.865205987381,1.2282058259,1.84640608656,3.61931751246,9.21152774203,32.8721787935,198.789131394,119.815191334,62.8626961887,35.8039418623,20.7399883386,11.4534806104,5.95634657249,2.92169192405,1.4031870924,0.575638064265,0.173603116072,0.0609456101156,0.0137336123699,0.0106506462401,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0])

    # Creating weights for histo: y7_DELTAR_17
    y7_DELTAR_17_weights = numpy.array([0.0,0.0,0.0572362909096,0.0577787036541,0.0518208288207,0.0613940055256,0.064642281449,0.0751126883234,0.0994859071727,0.126014411766,0.211267260636,0.382621046351,0.842287193824,2.33311154889,9.92480527912,80.4032152417,48.168246664,22.951973448,11.5936449216,5.77188934445,2.74595180956,1.20504015893,0.456496707029,0.145171933856,0.0429785459716,0.00740329079971,0.00270790858795,0.000360835302667,0.000360624137581,0.00036055858898,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0])

    # Creating a new Canvas
    fig   = plt.figure(figsize=(12,6),dpi=80)
    frame = gridspec.GridSpec(1,1,right=0.7)
    pad   = fig.add_subplot(frame[0])

    # Creating a new Stack
    pad.hist(x=xData, bins=xBinning, weights=y7_DELTAR_0_weights+y7_DELTAR_1_weights+y7_DELTAR_2_weights+y7_DELTAR_3_weights+y7_DELTAR_4_weights+y7_DELTAR_5_weights+y7_DELTAR_6_weights+y7_DELTAR_7_weights+y7_DELTAR_8_weights+y7_DELTAR_9_weights+y7_DELTAR_10_weights+y7_DELTAR_11_weights+y7_DELTAR_12_weights+y7_DELTAR_13_weights+y7_DELTAR_14_weights+y7_DELTAR_15_weights+y7_DELTAR_16_weights+y7_DELTAR_17_weights,\
             label="$bg\_dip\_1600\_inf$", histtype="step", rwidth=1.0,\
             color=None, edgecolor="#f2f2f2", linewidth=1, linestyle="solid",\
             bottom=None, cumulative=False, normed=False, align="mid", orientation="vertical")

    pad.hist(x=xData, bins=xBinning, weights=y7_DELTAR_0_weights+y7_DELTAR_1_weights+y7_DELTAR_2_weights+y7_DELTAR_3_weights+y7_DELTAR_4_weights+y7_DELTAR_5_weights+y7_DELTAR_6_weights+y7_DELTAR_7_weights+y7_DELTAR_8_weights+y7_DELTAR_9_weights+y7_DELTAR_10_weights+y7_DELTAR_11_weights+y7_DELTAR_12_weights+y7_DELTAR_13_weights+y7_DELTAR_14_weights+y7_DELTAR_15_weights+y7_DELTAR_16_weights,\
             label="$bg\_dip\_1200\_1600$", histtype="step", rwidth=1.0,\
             color=None, edgecolor="#ccc6aa", linewidth=1, linestyle="solid",\
             bottom=None, cumulative=False, normed=False, align="mid", orientation="vertical")

    pad.hist(x=xData, bins=xBinning, weights=y7_DELTAR_0_weights+y7_DELTAR_1_weights+y7_DELTAR_2_weights+y7_DELTAR_3_weights+y7_DELTAR_4_weights+y7_DELTAR_5_weights+y7_DELTAR_6_weights+y7_DELTAR_7_weights+y7_DELTAR_8_weights+y7_DELTAR_9_weights+y7_DELTAR_10_weights+y7_DELTAR_11_weights+y7_DELTAR_12_weights+y7_DELTAR_13_weights+y7_DELTAR_14_weights+y7_DELTAR_15_weights,\
             label="$bg\_dip\_800\_1200$", histtype="step", rwidth=1.0,\
             color=None, edgecolor="#ccc6aa", linewidth=1, linestyle="solid",\
             bottom=None, cumulative=False, normed=False, align="mid", orientation="vertical")

    pad.hist(x=xData, bins=xBinning, weights=y7_DELTAR_0_weights+y7_DELTAR_1_weights+y7_DELTAR_2_weights+y7_DELTAR_3_weights+y7_DELTAR_4_weights+y7_DELTAR_5_weights+y7_DELTAR_6_weights+y7_DELTAR_7_weights+y7_DELTAR_8_weights+y7_DELTAR_9_weights+y7_DELTAR_10_weights+y7_DELTAR_11_weights+y7_DELTAR_12_weights+y7_DELTAR_13_weights+y7_DELTAR_14_weights,\
             label="$bg\_dip\_600\_800$", histtype="step", rwidth=1.0,\
             color=None, edgecolor="#c1bfa8", linewidth=1, linestyle="solid",\
             bottom=None, cumulative=False, normed=False, align="mid", orientation="vertical")

    pad.hist(x=xData, bins=xBinning, weights=y7_DELTAR_0_weights+y7_DELTAR_1_weights+y7_DELTAR_2_weights+y7_DELTAR_3_weights+y7_DELTAR_4_weights+y7_DELTAR_5_weights+y7_DELTAR_6_weights+y7_DELTAR_7_weights+y7_DELTAR_8_weights+y7_DELTAR_9_weights+y7_DELTAR_10_weights+y7_DELTAR_11_weights+y7_DELTAR_12_weights+y7_DELTAR_13_weights,\
             label="$bg\_dip\_400\_600$", histtype="step", rwidth=1.0,\
             color=None, edgecolor="#bab5a3", linewidth=1, linestyle="solid",\
             bottom=None, cumulative=False, normed=False, align="mid", orientation="vertical")

    pad.hist(x=xData, bins=xBinning, weights=y7_DELTAR_0_weights+y7_DELTAR_1_weights+y7_DELTAR_2_weights+y7_DELTAR_3_weights+y7_DELTAR_4_weights+y7_DELTAR_5_weights+y7_DELTAR_6_weights+y7_DELTAR_7_weights+y7_DELTAR_8_weights+y7_DELTAR_9_weights+y7_DELTAR_10_weights+y7_DELTAR_11_weights+y7_DELTAR_12_weights,\
             label="$bg\_dip\_200\_400$", histtype="step", rwidth=1.0,\
             color=None, edgecolor="#b2a596", linewidth=1, linestyle="solid",\
             bottom=None, cumulative=False, normed=False, align="mid", orientation="vertical")

    pad.hist(x=xData, bins=xBinning, weights=y7_DELTAR_0_weights+y7_DELTAR_1_weights+y7_DELTAR_2_weights+y7_DELTAR_3_weights+y7_DELTAR_4_weights+y7_DELTAR_5_weights+y7_DELTAR_6_weights+y7_DELTAR_7_weights+y7_DELTAR_8_weights+y7_DELTAR_9_weights+y7_DELTAR_10_weights+y7_DELTAR_11_weights,\
             label="$bg\_dip\_100\_200$", histtype="step", rwidth=1.0,\
             color=None, edgecolor="#b7a39b", linewidth=1, linestyle="solid",\
             bottom=None, cumulative=False, normed=False, align="mid", orientation="vertical")

    pad.hist(x=xData, bins=xBinning, weights=y7_DELTAR_0_weights+y7_DELTAR_1_weights+y7_DELTAR_2_weights+y7_DELTAR_3_weights+y7_DELTAR_4_weights+y7_DELTAR_5_weights+y7_DELTAR_6_weights+y7_DELTAR_7_weights+y7_DELTAR_8_weights+y7_DELTAR_9_weights+y7_DELTAR_10_weights,\
             label="$bg\_dip\_0\_100$", histtype="step", rwidth=1.0,\
             color=None, edgecolor="#ad998c", linewidth=1, linestyle="solid",\
             bottom=None, cumulative=False, normed=False, align="mid", orientation="vertical")

    pad.hist(x=xData, bins=xBinning, weights=y7_DELTAR_0_weights+y7_DELTAR_1_weights+y7_DELTAR_2_weights+y7_DELTAR_3_weights+y7_DELTAR_4_weights+y7_DELTAR_5_weights+y7_DELTAR_6_weights+y7_DELTAR_7_weights+y7_DELTAR_8_weights+y7_DELTAR_9_weights,\
             label="$bg\_vbf\_1600\_inf$", histtype="step", rwidth=1.0,\
             color=None, edgecolor="#9b8e82", linewidth=1, linestyle="solid",\
             bottom=None, cumulative=False, normed=False, align="mid", orientation="vertical")

    pad.hist(x=xData, bins=xBinning, weights=y7_DELTAR_0_weights+y7_DELTAR_1_weights+y7_DELTAR_2_weights+y7_DELTAR_3_weights+y7_DELTAR_4_weights+y7_DELTAR_5_weights+y7_DELTAR_6_weights+y7_DELTAR_7_weights+y7_DELTAR_8_weights,\
             label="$bg\_vbf\_1200\_1600$", histtype="step", rwidth=1.0,\
             color=None, edgecolor="#876656", linewidth=1, linestyle="solid",\
             bottom=None, cumulative=False, normed=False, align="mid", orientation="vertical")

    pad.hist(x=xData, bins=xBinning, weights=y7_DELTAR_0_weights+y7_DELTAR_1_weights+y7_DELTAR_2_weights+y7_DELTAR_3_weights+y7_DELTAR_4_weights+y7_DELTAR_5_weights+y7_DELTAR_6_weights+y7_DELTAR_7_weights,\
             label="$bg\_vbf\_800\_1200$", histtype="step", rwidth=1.0,\
             color=None, edgecolor="#afcec6", linewidth=1, linestyle="solid",\
             bottom=None, cumulative=False, normed=False, align="mid", orientation="vertical")

    pad.hist(x=xData, bins=xBinning, weights=y7_DELTAR_0_weights+y7_DELTAR_1_weights+y7_DELTAR_2_weights+y7_DELTAR_3_weights+y7_DELTAR_4_weights+y7_DELTAR_5_weights+y7_DELTAR_6_weights,\
             label="$bg\_vbf\_600\_800$", histtype="step", rwidth=1.0,\
             color=None, edgecolor="#84c1a3", linewidth=1, linestyle="solid",\
             bottom=None, cumulative=False, normed=False, align="mid", orientation="vertical")

    pad.hist(x=xData, bins=xBinning, weights=y7_DELTAR_0_weights+y7_DELTAR_1_weights+y7_DELTAR_2_weights+y7_DELTAR_3_weights+y7_DELTAR_4_weights+y7_DELTAR_5_weights,\
             label="$bg\_vbf\_400\_600$", histtype="step", rwidth=1.0,\
             color=None, edgecolor="#89a8a0", linewidth=1, linestyle="solid",\
             bottom=None, cumulative=False, normed=False, align="mid", orientation="vertical")

    pad.hist(x=xData, bins=xBinning, weights=y7_DELTAR_0_weights+y7_DELTAR_1_weights+y7_DELTAR_2_weights+y7_DELTAR_3_weights+y7_DELTAR_4_weights,\
             label="$bg\_vbf\_200\_400$", histtype="step", rwidth=1.0,\
             color=None, edgecolor="#829e8c", linewidth=1, linestyle="solid",\
             bottom=None, cumulative=False, normed=False, align="mid", orientation="vertical")

    pad.hist(x=xData, bins=xBinning, weights=y7_DELTAR_0_weights+y7_DELTAR_1_weights+y7_DELTAR_2_weights+y7_DELTAR_3_weights,\
             label="$bg\_vbf\_100\_200$", histtype="step", rwidth=1.0,\
             color=None, edgecolor="#adbcc6", linewidth=1, linestyle="solid",\
             bottom=None, cumulative=False, normed=False, align="mid", orientation="vertical")

    pad.hist(x=xData, bins=xBinning, weights=y7_DELTAR_0_weights+y7_DELTAR_1_weights+y7_DELTAR_2_weights,\
             label="$bg\_vbf\_0\_100$", histtype="step", rwidth=1.0,\
             color=None, edgecolor="#7a8e99", linewidth=1, linestyle="solid",\
             bottom=None, cumulative=False, normed=False, align="mid", orientation="vertical")

    pad.hist(x=xData, bins=xBinning, weights=y7_DELTAR_0_weights+y7_DELTAR_1_weights,\
             label="$signal2$", histtype="step", rwidth=1.0,\
             color=None, edgecolor="#758991", linewidth=1, linestyle="solid",\
             bottom=None, cumulative=False, normed=False, align="mid", orientation="vertical")

    pad.hist(x=xData, bins=xBinning, weights=y7_DELTAR_0_weights,\
             label="$signal1$", histtype="step", rwidth=1.0,\
             color=None, edgecolor="#688296", linewidth=1, linestyle="solid",\
             bottom=None, cumulative=False, normed=False, align="mid", orientation="vertical")


    # Axis
    plt.rc('text',usetex=False)
    plt.xlabel(r"\Delta R [ j_{1} , j_{2} ] ",\
               fontsize=16,color="black")
    plt.ylabel(r"$\mathrm{Events}$ $(\mathcal{L}_{\mathrm{int}} = 40.0\ \mathrm{fb}^{-1})$ ",\
               fontsize=16,color="black")

    # Boundary of y-axis
    ymax=(y7_DELTAR_0_weights+y7_DELTAR_1_weights+y7_DELTAR_2_weights+y7_DELTAR_3_weights+y7_DELTAR_4_weights+y7_DELTAR_5_weights+y7_DELTAR_6_weights+y7_DELTAR_7_weights+y7_DELTAR_8_weights+y7_DELTAR_9_weights+y7_DELTAR_10_weights+y7_DELTAR_11_weights+y7_DELTAR_12_weights+y7_DELTAR_13_weights+y7_DELTAR_14_weights+y7_DELTAR_15_weights+y7_DELTAR_16_weights+y7_DELTAR_17_weights).max()*1.1
    ymin=0 # linear scale
    #ymin=min([x for x in (y7_DELTAR_0_weights+y7_DELTAR_1_weights+y7_DELTAR_2_weights+y7_DELTAR_3_weights+y7_DELTAR_4_weights+y7_DELTAR_5_weights+y7_DELTAR_6_weights+y7_DELTAR_7_weights+y7_DELTAR_8_weights+y7_DELTAR_9_weights+y7_DELTAR_10_weights+y7_DELTAR_11_weights+y7_DELTAR_12_weights+y7_DELTAR_13_weights+y7_DELTAR_14_weights+y7_DELTAR_15_weights+y7_DELTAR_16_weights+y7_DELTAR_17_weights) if x])/100. # log scale
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
    plt.savefig('../../HTML/MadAnalysis5job_0/selection_6.png')
    plt.savefig('../../PDF/MadAnalysis5job_0/selection_6.png')
    plt.savefig('../../DVI/MadAnalysis5job_0/selection_6.eps')

# Running!
if __name__ == '__main__':
    selection_6()
