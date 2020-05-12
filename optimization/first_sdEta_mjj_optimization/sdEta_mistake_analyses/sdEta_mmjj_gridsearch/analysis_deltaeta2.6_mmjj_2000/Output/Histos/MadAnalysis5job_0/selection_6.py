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
    y7_DELTAR_1_weights = numpy.array([0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0485729053353,0.77773071928,2.72191551768,7.78648410534,20.92014004,44.5525684517,88.4046713014,145.092755237,191.986778273,221.756746615,238.531790226,242.541792568,239.745097431,234.044436218,225.801117315,220.454193835,207.091431533,195.558764296,185.408882732,178.03582835,161.176506153,145.664760086,128.952925414,117.743873527,101.204962169,85.1253771145,72.5633815443,59.9164664866,46.2965022836,35.5309864809,26.0040254077,19.6489433811,14.6536626861,9.94101968139,7.2659837264,4.83560802479,3.34137073271,1.82219475022,1.05748154746,0.425182259955,0.255060887775,0.0486514959176,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0])

    # Creating weights for histo: y7_DELTAR_2
    y7_DELTAR_2_weights = numpy.array([0.0,0.0,0.0,0.0,0.0,0.0,0.301065617111,1.42556583629,3.91508658006,7.98143551265,16.7370252218,32.9929906598,64.0747913751,133.65317609,281.462864792,480.355672947,489.239287697,500.128213503,504.767328941,509.68825401,504.453702093,499.709217951,483.689869301,464.643339774,451.447459173,428.251881983,398.038459878,369.243259204,341.892105623,312.424363372,280.293726712,250.511283266,214.588695546,180.620511335,148.243229266,118.885277072,89.3875770517,65.1906666081,44.4765843725,30.892422164,20.0703579659,13.4845453964,8.34367658762,5.14110020671,3.20267927035,1.76731249178,0.883624015461,0.371539015992,0.110484746837,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0])

    # Creating weights for histo: y7_DELTAR_3
    y7_DELTAR_3_weights = numpy.array([0.0,0.0,0.0,0.0824868914374,0.462082659552,1.42998230494,2.72791864876,4.06463298939,5.97334797086,9.14134439507,13.9654901883,22.5794608144,40.2844487785,77.2638545603,172.551523135,362.406729986,361.007623176,366.669417089,367.96350659,370.317438085,363.618471291,348.272659595,329.101292804,312.526148895,288.097985311,262.074005514,236.068144756,208.630107909,181.035621678,156.060514949,128.980390091,105.305344834,81.3801268152,62.6480045684,44.3559393779,30.2406949132,18.2291644944,10.4627099583,6.08308191796,3.44855432924,1.95232499327,0.792079544842,0.324676265598,0.176061051285,0.0275332836871,0.0164857349758,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0])

    # Creating weights for histo: y7_DELTAR_4
    y7_DELTAR_4_weights = numpy.array([0.0,0.0,0.0345308579793,0.173671421931,0.241827866128,0.336542777947,0.513200440691,0.795369954677,1.11911620113,1.60855610399,2.56769090999,3.99161683662,6.82405788995,13.2719546961,31.5464128955,85.080025353,86.8294178983,86.1723735714,85.4711174404,82.3001730982,78.0545572426,71.9156901245,65.4876224929,58.1522709216,50.7102979551,42.8029987568,35.3414531485,28.4700208875,21.8035502213,15.7146308177,10.7035895861,6.96813706473,4.25928423753,2.35359234267,1.23651878301,0.560519897697,0.259549544502,0.101647907915,0.0335517529058,0.0128315361842,0.000987667653345,0.000986323662601,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0])

    # Creating weights for histo: y7_DELTAR_5
    y7_DELTAR_5_weights = numpy.array([0.0,0.0,0.0257116480221,0.0378142017046,0.057975420775,0.0922630221412,0.126792083235,0.180739507646,0.295678018787,0.430544499301,0.624129984523,1.01185949313,1.76506540581,3.44689022127,8.53282667631,27.2688372078,27.5877801013,26.3514342794,25.1909952337,23.2315105364,21.1460546789,18.8754690278,16.1034593447,13.5030201012,10.8988919452,8.3651812076,6.13429737714,4.31329493477,2.82763024139,1.68768986623,0.968978486099,0.476194191189,0.208732551994,0.0826807718799,0.0267190092025,0.00907671321185,0.00327711462565,0.000504083489874,0.000504337552719,0.000251541981316,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0])

    # Creating weights for histo: y7_DELTAR_6
    y7_DELTAR_6_weights = numpy.array([0.0,0.0,0.0105965838232,0.0220445819147,0.0246335330716,0.036659517193,0.0541441594077,0.0901870935238,0.126800446209,0.180636179124,0.273406045878,0.440072413223,0.789007111946,1.5556659239,4.05313578167,15.7287614821,15.6981317614,14.1111543455,12.8958322034,11.4667717911,9.68266353166,8.00078696361,6.2318146246,4.70749718025,3.36936125403,2.26604552297,1.3892747642,0.809907397883,0.410813332469,0.200961557997,0.0735794369958,0.0274838165264,0.0100306237574,0.00286040005965,0.00143093578291,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0])

    # Creating weights for histo: y7_DELTAR_7
    y7_DELTAR_7_weights = numpy.array([0.0,0.0,0.0015120887282,0.0025699127657,0.00399414868973,0.00557153368721,0.00893884523264,0.0116833312118,0.0174252186633,0.025588088418,0.042047766521,0.0680626739318,0.126317601203,0.267415051074,0.782551498671,3.75849153154,3.6196591648,3.06057041504,2.53501136641,2.01994645834,1.52943046313,1.09714814706,0.727797146796,0.444742431606,0.239862400031,0.11778616667,0.0529282289242,0.0188474345491,0.0065427404128,0.00159827730584,0.000626337163876,0.000237723045424,6.47734900894e-05,4.32688838282e-05,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0])

    # Creating weights for histo: y7_DELTAR_8
    y7_DELTAR_8_weights = numpy.array([0.0,0.0,0.00031204174528,0.000596577177178,0.000907172863031,0.0012498475166,0.00212951332377,0.00269294636746,0.00348263915304,0.00552912508447,0.0108297065501,0.0179724189316,0.0355705077542,0.0859228672158,0.292804462415,1.92345356789,1.72205214886,1.2494041059,0.905775510474,0.601716642854,0.384017281713,0.215347918235,0.115560031875,0.0524788003918,0.0193568819884,0.00654326743897,0.00187024873815,0.00059551839676,0.000141957358155,0.000113491474901,0.0,2.84511078463e-05,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0])

    # Creating weights for histo: y7_DELTAR_9
    y7_DELTAR_9_weights = numpy.array([0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,52.1293724655,623.023856931,1855.82327085,4566.51833926,9386.42858355,19413.5543961,38106.0119859,64902.3270658,83204.3916249,89502.006032,85263.5805681,75039.2721871,60592.6882406,48059.7903435,36387.5974335,27282.8499936,20357.2775511,14928.3738663,11033.3606097,7746.76785681,5620.15308809,3810.65849228,2512.84766258,1686.36892439,1165.06174149,654.201620206,414.453687639,208.582473977,143.334923608,88.5729254516,65.1565341562,15.6315019881,2.60827125955,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0])

    # Creating weights for histo: y7_DELTAR_10
    y7_DELTAR_10_weights = numpy.array([0.0,0.0,0.0,0.0,0.0,4.20992814798,127.4648631,629.762222343,1568.32017551,3495.7659018,6676.35404169,12275.5619029,21963.0595621,44475.1038477,96967.2038093,163208.238756,128648.926673,96752.0069688,72410.9088154,54111.5591095,40549.3101727,30397.4136534,22808.6373206,16723.137697,12605.3097952,8936.87122606,6457.42886693,4503.57006589,3210.27360713,2163.33886219,1418.7643352,979.525383143,601.413799653,326.483272026,230.689243054,130.593393458,56.8867634198,28.4423236171,18.9643860493,12.6358829062,2.10485095425,2.10713066331,1.05142452132,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0])

    # Creating weights for histo: y7_DELTAR_11
    y7_DELTAR_11_weights = numpy.array([0.0,0.0,0.0,23.4958481084,143.978089129,410.689887727,791.21498257,1152.34488444,1536.86367229,2040.99460325,2711.3509986,3923.78993543,6256.64995607,11920.9123616,28650.8435723,59123.2937514,35806.2358328,23474.319667,16571.7818896,11942.0834685,8521.0900311,6115.64884732,4342.44761342,3036.68174984,2113.54041719,1427.63267193,993.425565193,623.720020234,407.914974226,234.481151391,148.796533155,85.6869620429,49.286913164,24.644209674,11.7491228537,5.98716981431,2.30385445151,1.61207335708,0.0,0.230404695105,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0])

    # Creating weights for histo: y7_DELTAR_12
    y7_DELTAR_12_weights = numpy.array([0.0,0.0,9.66472600856,43.7500050963,64.6575651774,83.7935902555,102.179998422,117.602717167,138.705981699,174.368741766,223.494175291,319.032725612,521.055502718,1048.09486042,2847.67903945,8553.2963096,5043.08864714,3097.07275794,2056.65218962,1403.34864431,962.665847282,645.177982676,427.994516118,286.549172234,179.106043651,114.225997868,69.4464573257,40.7922018119,21.3496936379,11.3807081853,5.56627777849,2.60314773211,1.05230364103,0.498288846531,0.221571832062,0.0554093276329,0.0,0.0276409781179,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0])

    # Creating weights for histo: y7_DELTAR_13
    y7_DELTAR_13_weights = numpy.array([0.0,0.0,7.87346431067,11.3535897502,13.5102053263,15.7677732554,17.2401750961,19.6494264235,23.3193745701,28.6322864583,38.2301997352,55.469064077,94.4802609738,195.743553993,577.640977327,2175.76351158,1291.2252573,753.755318426,487.588274406,315.985901509,207.1243601,133.151274656,83.295521862,49.3109766138,30.0054350719,15.8803585527,8.70110247882,4.6476094243,1.97639171691,1.00805014485,0.393204438829,0.211687362762,0.0302185964871,0.0201784189377,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0])

    # Creating weights for histo: y7_DELTAR_14
    y7_DELTAR_14_weights = numpy.array([0.0,0.0,3.66388129673,3.92687516306,4.08518088053,4.71938868855,5.07287759159,5.66696071368,6.89153888877,8.6855805805,11.9701260435,18.0021371408,31.7838683233,69.5879169443,221.631197821,1038.29675249,620.115882889,348.41266281,213.528735231,132.984997673,82.0197211869,49.1317526265,29.2762158829,15.7413386628,7.84283521114,3.8703335594,1.86729992669,0.752527346481,0.265961992723,0.118844094956,0.0367957259207,0.0226352937279,0.0169645894799,0.0,0.00282706133047,0.00283195831966,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0])

    # Creating weights for histo: y7_DELTAR_15
    y7_DELTAR_15_weights = numpy.array([0.0,0.0,0.417498927285,0.406566599605,0.425134824592,0.435821252297,0.441724387838,0.475219131261,0.627590737741,0.865206093423,1.22820597643,1.84640631286,3.61931795606,9.21152887102,32.8721828224,198.789155758,119.815206019,62.8627038934,35.8039462505,20.7399908805,11.4534820142,5.95634730251,2.92169228214,1.40318726438,0.575638134817,0.17360313735,0.0609456175852,0.0137336140531,0.0106506475455,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0])

    # Creating weights for histo: y7_DELTAR_16
    y7_DELTAR_16_weights = numpy.array([0.0,0.0,0.0543461063394,0.0577787040255,0.0518208291538,0.0613940059203,0.0646422818645,0.0751126888062,0.0994859078122,0.126014412576,0.211267261994,0.38262104881,0.842287199238,2.33311156389,9.92480534291,80.4032157585,48.1682469736,22.9519735956,11.5936449961,5.77188938155,2.74595182721,1.20504016668,0.456496709964,0.145171934789,0.0429785462478,0.00740329084729,0.00270790860536,0.000360835304987,0.000360624139899,0.000360558591298,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0])

    # Creating a new Canvas
    fig   = plt.figure(figsize=(12,6),dpi=80)
    frame = gridspec.GridSpec(1,1,right=0.7)
    pad   = fig.add_subplot(frame[0])

    # Creating a new Stack
    pad.hist(x=xData, bins=xBinning, weights=y7_DELTAR_0_weights+y7_DELTAR_1_weights+y7_DELTAR_2_weights+y7_DELTAR_3_weights+y7_DELTAR_4_weights+y7_DELTAR_5_weights+y7_DELTAR_6_weights+y7_DELTAR_7_weights+y7_DELTAR_8_weights+y7_DELTAR_9_weights+y7_DELTAR_10_weights+y7_DELTAR_11_weights+y7_DELTAR_12_weights+y7_DELTAR_13_weights+y7_DELTAR_14_weights+y7_DELTAR_15_weights+y7_DELTAR_16_weights,\
             label="$bg\_dip\_1600\_inf$", histtype="step", rwidth=1.0,\
             color=None, edgecolor="#e5e5e5", linewidth=4, linestyle="dashdot",\
             bottom=None, cumulative=False, normed=False, align="mid", orientation="vertical")

    pad.hist(x=xData, bins=xBinning, weights=y7_DELTAR_0_weights+y7_DELTAR_1_weights+y7_DELTAR_2_weights+y7_DELTAR_3_weights+y7_DELTAR_4_weights+y7_DELTAR_5_weights+y7_DELTAR_6_weights+y7_DELTAR_7_weights+y7_DELTAR_8_weights+y7_DELTAR_9_weights+y7_DELTAR_10_weights+y7_DELTAR_11_weights+y7_DELTAR_12_weights+y7_DELTAR_13_weights+y7_DELTAR_14_weights+y7_DELTAR_15_weights,\
             label="$bg\_dip\_1200\_1600$", histtype="step", rwidth=1.0,\
             color=None, edgecolor="#f2f2f2", linewidth=4, linestyle="dashdot",\
             bottom=None, cumulative=False, normed=False, align="mid", orientation="vertical")

    pad.hist(x=xData, bins=xBinning, weights=y7_DELTAR_0_weights+y7_DELTAR_1_weights+y7_DELTAR_2_weights+y7_DELTAR_3_weights+y7_DELTAR_4_weights+y7_DELTAR_5_weights+y7_DELTAR_6_weights+y7_DELTAR_7_weights+y7_DELTAR_8_weights+y7_DELTAR_9_weights+y7_DELTAR_10_weights+y7_DELTAR_11_weights+y7_DELTAR_12_weights+y7_DELTAR_13_weights+y7_DELTAR_14_weights,\
             label="$bg\_dip\_800\_1200$", histtype="step", rwidth=1.0,\
             color=None, edgecolor="#ccc6aa", linewidth=4, linestyle="dashdot",\
             bottom=None, cumulative=False, normed=False, align="mid", orientation="vertical")

    pad.hist(x=xData, bins=xBinning, weights=y7_DELTAR_0_weights+y7_DELTAR_1_weights+y7_DELTAR_2_weights+y7_DELTAR_3_weights+y7_DELTAR_4_weights+y7_DELTAR_5_weights+y7_DELTAR_6_weights+y7_DELTAR_7_weights+y7_DELTAR_8_weights+y7_DELTAR_9_weights+y7_DELTAR_10_weights+y7_DELTAR_11_weights+y7_DELTAR_12_weights+y7_DELTAR_13_weights,\
             label="$bg\_dip\_600\_800$", histtype="step", rwidth=1.0,\
             color=None, edgecolor="#ccc6aa", linewidth=4, linestyle="dashdot",\
             bottom=None, cumulative=False, normed=False, align="mid", orientation="vertical")

    pad.hist(x=xData, bins=xBinning, weights=y7_DELTAR_0_weights+y7_DELTAR_1_weights+y7_DELTAR_2_weights+y7_DELTAR_3_weights+y7_DELTAR_4_weights+y7_DELTAR_5_weights+y7_DELTAR_6_weights+y7_DELTAR_7_weights+y7_DELTAR_8_weights+y7_DELTAR_9_weights+y7_DELTAR_10_weights+y7_DELTAR_11_weights+y7_DELTAR_12_weights,\
             label="$bg\_dip\_400\_600$", histtype="step", rwidth=1.0,\
             color=None, edgecolor="#c1bfa8", linewidth=4, linestyle="dashdot",\
             bottom=None, cumulative=False, normed=False, align="mid", orientation="vertical")

    pad.hist(x=xData, bins=xBinning, weights=y7_DELTAR_0_weights+y7_DELTAR_1_weights+y7_DELTAR_2_weights+y7_DELTAR_3_weights+y7_DELTAR_4_weights+y7_DELTAR_5_weights+y7_DELTAR_6_weights+y7_DELTAR_7_weights+y7_DELTAR_8_weights+y7_DELTAR_9_weights+y7_DELTAR_10_weights+y7_DELTAR_11_weights,\
             label="$bg\_dip\_200\_400$", histtype="step", rwidth=1.0,\
             color=None, edgecolor="#bab5a3", linewidth=4, linestyle="dashdot",\
             bottom=None, cumulative=False, normed=False, align="mid", orientation="vertical")

    pad.hist(x=xData, bins=xBinning, weights=y7_DELTAR_0_weights+y7_DELTAR_1_weights+y7_DELTAR_2_weights+y7_DELTAR_3_weights+y7_DELTAR_4_weights+y7_DELTAR_5_weights+y7_DELTAR_6_weights+y7_DELTAR_7_weights+y7_DELTAR_8_weights+y7_DELTAR_9_weights+y7_DELTAR_10_weights,\
             label="$bg\_dip\_100\_200$", histtype="step", rwidth=1.0,\
             color=None, edgecolor="#b2a596", linewidth=4, linestyle="dashdot",\
             bottom=None, cumulative=False, normed=False, align="mid", orientation="vertical")

    pad.hist(x=xData, bins=xBinning, weights=y7_DELTAR_0_weights+y7_DELTAR_1_weights+y7_DELTAR_2_weights+y7_DELTAR_3_weights+y7_DELTAR_4_weights+y7_DELTAR_5_weights+y7_DELTAR_6_weights+y7_DELTAR_7_weights+y7_DELTAR_8_weights+y7_DELTAR_9_weights,\
             label="$bg\_dip\_0\_100$", histtype="step", rwidth=1.0,\
             color=None, edgecolor="#b7a39b", linewidth=4, linestyle="dashdot",\
             bottom=None, cumulative=False, normed=False, align="mid", orientation="vertical")

    pad.hist(x=xData, bins=xBinning, weights=y7_DELTAR_0_weights+y7_DELTAR_1_weights+y7_DELTAR_2_weights+y7_DELTAR_3_weights+y7_DELTAR_4_weights+y7_DELTAR_5_weights+y7_DELTAR_6_weights+y7_DELTAR_7_weights+y7_DELTAR_8_weights,\
             label="$bg\_vbf\_1600\_inf$", histtype="step", rwidth=1.0,\
             color=None, edgecolor="#ad998c", linewidth=4, linestyle="dashdot",\
             bottom=None, cumulative=False, normed=False, align="mid", orientation="vertical")

    pad.hist(x=xData, bins=xBinning, weights=y7_DELTAR_0_weights+y7_DELTAR_1_weights+y7_DELTAR_2_weights+y7_DELTAR_3_weights+y7_DELTAR_4_weights+y7_DELTAR_5_weights+y7_DELTAR_6_weights+y7_DELTAR_7_weights,\
             label="$bg\_vbf\_1200\_1600$", histtype="step", rwidth=1.0,\
             color=None, edgecolor="#9b8e82", linewidth=4, linestyle="dashdot",\
             bottom=None, cumulative=False, normed=False, align="mid", orientation="vertical")

    pad.hist(x=xData, bins=xBinning, weights=y7_DELTAR_0_weights+y7_DELTAR_1_weights+y7_DELTAR_2_weights+y7_DELTAR_3_weights+y7_DELTAR_4_weights+y7_DELTAR_5_weights+y7_DELTAR_6_weights,\
             label="$bg\_vbf\_800\_1200$", histtype="step", rwidth=1.0,\
             color=None, edgecolor="#876656", linewidth=4, linestyle="dashdot",\
             bottom=None, cumulative=False, normed=False, align="mid", orientation="vertical")

    pad.hist(x=xData, bins=xBinning, weights=y7_DELTAR_0_weights+y7_DELTAR_1_weights+y7_DELTAR_2_weights+y7_DELTAR_3_weights+y7_DELTAR_4_weights+y7_DELTAR_5_weights,\
             label="$bg\_vbf\_600\_800$", histtype="step", rwidth=1.0,\
             color=None, edgecolor="#afcec6", linewidth=4, linestyle="dashdot",\
             bottom=None, cumulative=False, normed=False, align="mid", orientation="vertical")

    pad.hist(x=xData, bins=xBinning, weights=y7_DELTAR_0_weights+y7_DELTAR_1_weights+y7_DELTAR_2_weights+y7_DELTAR_3_weights+y7_DELTAR_4_weights,\
             label="$bg\_vbf\_400\_600$", histtype="step", rwidth=1.0,\
             color=None, edgecolor="#84c1a3", linewidth=4, linestyle="dashdot",\
             bottom=None, cumulative=False, normed=False, align="mid", orientation="vertical")

    pad.hist(x=xData, bins=xBinning, weights=y7_DELTAR_0_weights+y7_DELTAR_1_weights+y7_DELTAR_2_weights+y7_DELTAR_3_weights,\
             label="$bg\_vbf\_200\_400$", histtype="step", rwidth=1.0,\
             color=None, edgecolor="#89a8a0", linewidth=4, linestyle="dashdot",\
             bottom=None, cumulative=False, normed=False, align="mid", orientation="vertical")

    pad.hist(x=xData, bins=xBinning, weights=y7_DELTAR_0_weights+y7_DELTAR_1_weights+y7_DELTAR_2_weights,\
             label="$bg\_vbf\_100\_200$", histtype="step", rwidth=1.0,\
             color=None, edgecolor="#829e8c", linewidth=4, linestyle="dashdot",\
             bottom=None, cumulative=False, normed=False, align="mid", orientation="vertical")

    pad.hist(x=xData, bins=xBinning, weights=y7_DELTAR_0_weights+y7_DELTAR_1_weights,\
             label="$bg\_vbf\_0\_100$", histtype="step", rwidth=1.0,\
             color=None, edgecolor="#adbcc6", linewidth=4, linestyle="dashdot",\
             bottom=None, cumulative=False, normed=False, align="mid", orientation="vertical")

    pad.hist(x=xData, bins=xBinning, weights=y7_DELTAR_0_weights,\
             label="$signal$", histtype="step", rwidth=1.0,\
             color=None, edgecolor="#7a8e99", linewidth=3, linestyle="dashed",\
             bottom=None, cumulative=False, normed=False, align="mid", orientation="vertical")


    # Axis
    plt.rc('text',usetex=False)
    plt.xlabel(r"\Delta R [ j_{1} , j_{2} ] ",\
               fontsize=16,color="black")
    plt.ylabel(r"$\mathrm{Events}$ $(\mathcal{L}_{\mathrm{int}} = 40.0\ \mathrm{fb}^{-1})$ ",\
               fontsize=16,color="black")

    # Boundary of y-axis
    ymax=(y7_DELTAR_0_weights+y7_DELTAR_1_weights+y7_DELTAR_2_weights+y7_DELTAR_3_weights+y7_DELTAR_4_weights+y7_DELTAR_5_weights+y7_DELTAR_6_weights+y7_DELTAR_7_weights+y7_DELTAR_8_weights+y7_DELTAR_9_weights+y7_DELTAR_10_weights+y7_DELTAR_11_weights+y7_DELTAR_12_weights+y7_DELTAR_13_weights+y7_DELTAR_14_weights+y7_DELTAR_15_weights+y7_DELTAR_16_weights).max()*1.1
    ymin=0 # linear scale
    #ymin=min([x for x in (y7_DELTAR_0_weights+y7_DELTAR_1_weights+y7_DELTAR_2_weights+y7_DELTAR_3_weights+y7_DELTAR_4_weights+y7_DELTAR_5_weights+y7_DELTAR_6_weights+y7_DELTAR_7_weights+y7_DELTAR_8_weights+y7_DELTAR_9_weights+y7_DELTAR_10_weights+y7_DELTAR_11_weights+y7_DELTAR_12_weights+y7_DELTAR_13_weights+y7_DELTAR_14_weights+y7_DELTAR_15_weights+y7_DELTAR_16_weights) if x])/100. # log scale
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
