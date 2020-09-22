def selection_14():

    # Library import
    import numpy
    import matplotlib
    import matplotlib.pyplot   as plt
    import matplotlib.gridspec as gridspec

    # Library version
    matplotlib_version = matplotlib.__version__
    numpy_version      = numpy.__version__

    # Histo binning
    xBinning = numpy.linspace(0.0,8000.0,81,endpoint=True)

    # Creating data sequence: middle of each bin
    xData = numpy.array([50.0,150.0,250.0,350.0,450.0,550.0,650.0,750.0,850.0,950.0,1050.0,1150.0,1250.0,1350.0,1450.0,1550.0,1650.0,1750.0,1850.0,1950.0,2050.0,2150.0,2250.0,2350.0,2450.0,2550.0,2650.0,2750.0,2850.0,2950.0,3050.0,3150.0,3250.0,3350.0,3450.0,3550.0,3650.0,3750.0,3850.0,3950.0,4050.0,4150.0,4250.0,4350.0,4450.0,4550.0,4650.0,4750.0,4850.0,4950.0,5050.0,5150.0,5250.0,5350.0,5450.0,5550.0,5650.0,5750.0,5850.0,5950.0,6050.0,6150.0,6250.0,6350.0,6450.0,6550.0,6650.0,6750.0,6850.0,6950.0,7050.0,7150.0,7250.0,7350.0,7450.0,7550.0,7650.0,7750.0,7850.0,7950.0])

    # Creating weights for histo: y15_TET_0
    y15_TET_0_weights = numpy.array([0.0,0.0,0.0,0.0,0.0,0.0,0.354738985248,1.2257186445,1.92557043349,2.48225931117,2.73976789996,2.98881489102,2.99520575341,3.06041852884,2.94174313202,2.96213513888,2.78367899981,2.58066420345,2.49614734657,2.25158395114,2.0505615531,1.92663917433,1.69048062224,1.51418674493,1.40727908802,1.30691377172,1.12417067893,1.03860946162,0.906144750027,0.816375315696,0.768265591115,0.628357263452,0.51184332903,0.506511215518,0.431744520481,0.360126454261,0.316309598641,0.247889241782,0.22970110323,0.191278391257,0.18273981542,0.135730526199,0.121800004948,0.116459618086,0.0694556046235,0.0812273413217,0.0534188965368,0.0502233054732,0.0523617064122,0.0309815818992,0.0373867927487,0.0267182691773,0.0192423830439,0.0202996810817,0.0138971041148,0.018164577492,0.0128219324456,0.00748147763841,0.00854843191362,0.00640553858606,0.00641113009105,0.00427273314884,0.00427459964836,0.00747588613342,0.00320688038812,0.00320688038812,0.0,0.0,0.0,0.00213729902482,0.0010695813633,0.0,0.0,0.0010695813633,0.0,0.00213466953867,0.00106771766153,0.0,0.00106695187714,0.0])

    # Creating weights for histo: y15_TET_1
    y15_TET_1_weights = numpy.array([0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0])

    # Creating weights for histo: y15_TET_2
    y15_TET_2_weights = numpy.array([0.0,0.0,0.0,0.0,0.0,0.0,2.10674221742,0.0,1.0529581672,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0])

    # Creating weights for histo: y15_TET_3
    y15_TET_3_weights = numpy.array([0.0,0.0,0.0,0.0,0.0,0.0,0.922291234315,5.9893732087,6.44785017911,6.90932817631,2.30289651517,1.38211962742,0.691757427557,0.921287177588,0.0,0.0,0.230663838444,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0])

    # Creating weights for histo: y15_TET_4
    y15_TET_4_weights = numpy.array([0.0,0.0,0.0,0.0,0.0,0.0,0.0,1.05249699611,4.37443061386,7.06177182363,7.58640497093,6.64708177966,3.87685718834,2.18719684138,0.775305269455,0.636986389347,0.276738243572,0.193850053287,0.0554168406615,0.0276713007323,0.0554270351828,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0])

    # Creating weights for histo: y15_TET_5
    y15_TET_5_weights = numpy.array([0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.352880098365,1.48209907111,2.96433407514,3.41790702955,3.72025339768,2.7318226374,1.92570887076,1.068443668,0.544604378229,0.231958724781,0.201573408755,0.0706242515856,0.0201651752236,0.0402676999358,0.0100664395092,0.0100941965259,0.0100798568166,0.0,0.0100846023319,0.0100700259537,0.0,0.0100968059524,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0])

    # Creating weights for histo: y15_TET_6
    y15_TET_6_weights = numpy.array([0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0763558297671,0.568694564383,1.0101021595,1.38905783472,1.45427263042,1.57028955959,1.32965234994,1.16845945813,0.845880915734,0.712970468864,0.500699579223,0.294183289325,0.20090847154,0.127300704772,0.0848686498567,0.048084273199,0.0197958531236,0.0113092728515,0.0113073529587,0.00565266459194,0.0,0.0,0.0,0.00566375687843,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0028293356393,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0])

    # Creating weights for histo: y15_TET_7
    y15_TET_7_weights = numpy.array([0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0137355339076,0.117350588284,0.182794831399,0.20416305291,0.229988777122,0.163012329488,0.140042200329,0.112707159369,0.103531337361,0.137083214468,0.120378095665,0.12026631543,0.0775906898349,0.0609344187575,0.0488390766371,0.0274176827097,0.0289559252516,0.0167883631745,0.0075990814555,0.00153784433961,0.0,0.00152268901949,0.00303836636974,0.0,0.0,0.00152412940115,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0])

    # Creating weights for histo: y15_TET_8
    y15_TET_8_weights = numpy.array([0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.00270740631055,0.0200468410733,0.0341248587687,0.0454997269637,0.0480380227995,0.0455056579213,0.0427911279144,0.0344889117346,0.0312360163751,0.0265401690787,0.0220239489233,0.0194946766159,0.0173346372342,0.0180539160524,0.018779946149,0.0117361443943,0.0110101528104,0.00884949337401,0.00541878097096,0.00613855660313,0.00577870152285,0.00397373779384,0.00361126654502,0.00234714299551,0.00180528261426,0.00144575065564,0.000360980922399,0.000540899874206,0.000360572418061,0.000180065454164,0.000541125943826,0.000361162086197,0.000180408717968,0.000181037360969,0.000180410605091,0.000180822074908,0.0,0.0,0.0,0.0,0.0,0.0,0.000180679770436,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0])

    # Creating weights for histo: y15_TET_9
    y15_TET_9_weights = numpy.array([0.0,0.0,0.0,0.0,0.0,0.0,0.0121704927804,0.0242994195771,0.0,0.0,0.0121313836425,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0])

    # Creating weights for histo: y15_TET_10
    y15_TET_10_weights = numpy.array([0.0,0.0,0.0,0.0,0.0,0.0,0.220879096585,0.441761829362,0.230809248523,0.120544402743,0.0502051137366,0.0501796190701,0.0100546543364,0.0301461580631,0.0100696701578,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0])

    # Creating weights for histo: y15_TET_11
    y15_TET_11_weights = numpy.array([0.0,0.0,0.0,0.0,0.0,0.0,0.511523586303,1.49042943279,1.7326214987,1.33674184095,0.781128930711,0.368558845657,0.203524457618,0.0824943211821,0.088002896721,0.0274928134005,0.0109788441534,0.0164797128056,0.0109794251154,0.0,0.01097305891,0.0,0.00549610720177,0.0,0.0,0.0,0.0,0.00551434453166,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0])

    # Creating weights for histo: y15_TET_12
    y15_TET_12_weights = numpy.array([0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.113479312298,0.864493808446,1.54045753963,1.67569317443,1.2838877739,0.760854213214,0.387825021836,0.198354081882,0.109546551927,0.0611909471831,0.02663522847,0.0286230369006,0.00888187531289,0.00987345472794,0.00493570324938,0.00296082110901,0.00394365085773,0.000983905570076,0.00197238578589,0.00197611107788,0.0019700401426,0.000985425508448,0.000988891464961,0.0,0.0,0.000988891464961,0.000986791128182,0.0,0.0,0.000986287287852,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0])

    # Creating weights for histo: y15_TET_13
    y15_TET_13_weights = numpy.array([0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0287367350186,0.238957543458,0.578247941085,0.76482083613,0.734529297645,0.556343800681,0.355420384804,0.178980785385,0.0930231385172,0.0534535685441,0.0305084593333,0.0181473798728,0.0103330679808,0.00605134587252,0.00529589589221,0.00176429316723,0.00151019857682,0.00151109721233,0.00100849229496,0.000505079965999,0.000757389688654,0.000252013204947,0.0,0.0,0.000251953509303,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0])

    # Creating weights for histo: y15_TET_14
    y15_TET_14_weights = numpy.array([0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.00859143176348,0.0644089065888,0.145191175581,0.255091262301,0.30036606971,0.326410878893,0.285662382481,0.224188314627,0.181248796955,0.127415359615,0.0787208294192,0.0652607704557,0.0363347708159,0.0243250649487,0.0103212647932,0.00515728412821,0.00457891950146,0.00315486765823,0.00229402075415,0.00057376723128,0.00228989765505,0.000573632160793,0.000286204064123,0.0,0.0,0.0,0.000286459708264,0.000286335535396,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0])

    # Creating weights for histo: y15_TET_15
    y15_TET_15_weights = numpy.array([0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.00105852176707,0.00848326100671,0.0199579535689,0.0318941120735,0.0391692164508,0.0403579392736,0.0386727302609,0.0344275771967,0.0330114616537,0.0314952265926,0.0275494262355,0.022201944243,0.0177744478412,0.0133885683683,0.0093061949133,0.00663039821681,0.0037993992936,0.0026783037707,0.00127432335533,0.000689766858844,0.000410462782485,0.000237498131994,0.000108118182862,0.000107991865215,6.49308749759e-05,6.47342737539e-05,6.47203176236e-05,0.0,4.32388575564e-05,0.0,0.0,0.0,0.0,2.15831428396e-05,0.0,0.0,0.0,2.15567309679e-05,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0])

    # Creating weights for histo: y15_TET_16
    y15_TET_16_weights = numpy.array([0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.000113626759745,0.001818436515,0.00334578203816,0.00615344524898,0.00740001271832,0.00787182963164,0.0081374427359,0.00677454580121,0.00637628282902,0.00634863215511,0.00495915237521,0.00533319241844,0.0050819096049,0.00529771199092,0.00428319008197,0.00402880625827,0.00357538302828,0.00246552287888,0.00180822011228,0.00133400630226,0.00150132703804,0.000824176618299,0.000819278418298,0.000454032293334,0.000369157734424,0.000253840255822,5.68172635609e-05,0.000255156848497,0.000454104769051,0.000225488438765,5.68172635609e-05,5.66034750493e-05,0.0,0.000113629314217,0.000112351617833,5.68291596775e-05,2.84547979207e-05,0.0,2.84032777854e-05,0.0,0.0,0.0,2.79785225627e-05,2.84547979207e-05,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0])

    # Creating a new Canvas
    fig   = plt.figure(figsize=(12,6),dpi=80)
    frame = gridspec.GridSpec(1,1,right=0.7)
    pad   = fig.add_subplot(frame[0])

    # Creating a new Stack
    pad.hist(x=xData, bins=xBinning, weights=y15_TET_0_weights+y15_TET_1_weights+y15_TET_2_weights+y15_TET_3_weights+y15_TET_4_weights+y15_TET_5_weights+y15_TET_6_weights+y15_TET_7_weights+y15_TET_8_weights+y15_TET_9_weights+y15_TET_10_weights+y15_TET_11_weights+y15_TET_12_weights+y15_TET_13_weights+y15_TET_14_weights+y15_TET_15_weights+y15_TET_16_weights,\
             label="$bg\_vbf\_1600\_inf$", histtype="step", rwidth=1.0,\
             color=None, edgecolor="#e5e5e5", linewidth=1, linestyle="solid",\
             bottom=None, cumulative=False, normed=False, align="mid", orientation="vertical")

    pad.hist(x=xData, bins=xBinning, weights=y15_TET_0_weights+y15_TET_1_weights+y15_TET_2_weights+y15_TET_3_weights+y15_TET_4_weights+y15_TET_5_weights+y15_TET_6_weights+y15_TET_7_weights+y15_TET_8_weights+y15_TET_9_weights+y15_TET_10_weights+y15_TET_11_weights+y15_TET_12_weights+y15_TET_13_weights+y15_TET_14_weights+y15_TET_15_weights,\
             label="$bg\_vbf\_1200\_1600$", histtype="step", rwidth=1.0,\
             color=None, edgecolor="#f2f2f2", linewidth=1, linestyle="solid",\
             bottom=None, cumulative=False, normed=False, align="mid", orientation="vertical")

    pad.hist(x=xData, bins=xBinning, weights=y15_TET_0_weights+y15_TET_1_weights+y15_TET_2_weights+y15_TET_3_weights+y15_TET_4_weights+y15_TET_5_weights+y15_TET_6_weights+y15_TET_7_weights+y15_TET_8_weights+y15_TET_9_weights+y15_TET_10_weights+y15_TET_11_weights+y15_TET_12_weights+y15_TET_13_weights+y15_TET_14_weights,\
             label="$bg\_vbf\_800\_1200$", histtype="step", rwidth=1.0,\
             color=None, edgecolor="#ccc6aa", linewidth=1, linestyle="solid",\
             bottom=None, cumulative=False, normed=False, align="mid", orientation="vertical")

    pad.hist(x=xData, bins=xBinning, weights=y15_TET_0_weights+y15_TET_1_weights+y15_TET_2_weights+y15_TET_3_weights+y15_TET_4_weights+y15_TET_5_weights+y15_TET_6_weights+y15_TET_7_weights+y15_TET_8_weights+y15_TET_9_weights+y15_TET_10_weights+y15_TET_11_weights+y15_TET_12_weights+y15_TET_13_weights,\
             label="$bg\_vbf\_600\_800$", histtype="step", rwidth=1.0,\
             color=None, edgecolor="#ccc6aa", linewidth=1, linestyle="solid",\
             bottom=None, cumulative=False, normed=False, align="mid", orientation="vertical")

    pad.hist(x=xData, bins=xBinning, weights=y15_TET_0_weights+y15_TET_1_weights+y15_TET_2_weights+y15_TET_3_weights+y15_TET_4_weights+y15_TET_5_weights+y15_TET_6_weights+y15_TET_7_weights+y15_TET_8_weights+y15_TET_9_weights+y15_TET_10_weights+y15_TET_11_weights+y15_TET_12_weights,\
             label="$bg\_vbf\_400\_600$", histtype="step", rwidth=1.0,\
             color=None, edgecolor="#c1bfa8", linewidth=1, linestyle="solid",\
             bottom=None, cumulative=False, normed=False, align="mid", orientation="vertical")

    pad.hist(x=xData, bins=xBinning, weights=y15_TET_0_weights+y15_TET_1_weights+y15_TET_2_weights+y15_TET_3_weights+y15_TET_4_weights+y15_TET_5_weights+y15_TET_6_weights+y15_TET_7_weights+y15_TET_8_weights+y15_TET_9_weights+y15_TET_10_weights+y15_TET_11_weights,\
             label="$bg\_vbf\_200\_400$", histtype="step", rwidth=1.0,\
             color=None, edgecolor="#bab5a3", linewidth=1, linestyle="solid",\
             bottom=None, cumulative=False, normed=False, align="mid", orientation="vertical")

    pad.hist(x=xData, bins=xBinning, weights=y15_TET_0_weights+y15_TET_1_weights+y15_TET_2_weights+y15_TET_3_weights+y15_TET_4_weights+y15_TET_5_weights+y15_TET_6_weights+y15_TET_7_weights+y15_TET_8_weights+y15_TET_9_weights+y15_TET_10_weights,\
             label="$bg\_vbf\_100\_200$", histtype="step", rwidth=1.0,\
             color=None, edgecolor="#b2a596", linewidth=1, linestyle="solid",\
             bottom=None, cumulative=False, normed=False, align="mid", orientation="vertical")

    pad.hist(x=xData, bins=xBinning, weights=y15_TET_0_weights+y15_TET_1_weights+y15_TET_2_weights+y15_TET_3_weights+y15_TET_4_weights+y15_TET_5_weights+y15_TET_6_weights+y15_TET_7_weights+y15_TET_8_weights+y15_TET_9_weights,\
             label="$bg\_vbf\_0\_100$", histtype="step", rwidth=1.0,\
             color=None, edgecolor="#b7a39b", linewidth=1, linestyle="solid",\
             bottom=None, cumulative=False, normed=False, align="mid", orientation="vertical")

    pad.hist(x=xData, bins=xBinning, weights=y15_TET_0_weights+y15_TET_1_weights+y15_TET_2_weights+y15_TET_3_weights+y15_TET_4_weights+y15_TET_5_weights+y15_TET_6_weights+y15_TET_7_weights+y15_TET_8_weights,\
             label="$bg\_dip\_1600\_inf$", histtype="step", rwidth=1.0,\
             color=None, edgecolor="#ad998c", linewidth=1, linestyle="solid",\
             bottom=None, cumulative=False, normed=False, align="mid", orientation="vertical")

    pad.hist(x=xData, bins=xBinning, weights=y15_TET_0_weights+y15_TET_1_weights+y15_TET_2_weights+y15_TET_3_weights+y15_TET_4_weights+y15_TET_5_weights+y15_TET_6_weights+y15_TET_7_weights,\
             label="$bg\_dip\_1200\_1600$", histtype="step", rwidth=1.0,\
             color=None, edgecolor="#9b8e82", linewidth=1, linestyle="solid",\
             bottom=None, cumulative=False, normed=False, align="mid", orientation="vertical")

    pad.hist(x=xData, bins=xBinning, weights=y15_TET_0_weights+y15_TET_1_weights+y15_TET_2_weights+y15_TET_3_weights+y15_TET_4_weights+y15_TET_5_weights+y15_TET_6_weights,\
             label="$bg\_dip\_800\_1200$", histtype="step", rwidth=1.0,\
             color=None, edgecolor="#876656", linewidth=1, linestyle="solid",\
             bottom=None, cumulative=False, normed=False, align="mid", orientation="vertical")

    pad.hist(x=xData, bins=xBinning, weights=y15_TET_0_weights+y15_TET_1_weights+y15_TET_2_weights+y15_TET_3_weights+y15_TET_4_weights+y15_TET_5_weights,\
             label="$bg\_dip\_600\_800$", histtype="step", rwidth=1.0,\
             color=None, edgecolor="#afcec6", linewidth=1, linestyle="solid",\
             bottom=None, cumulative=False, normed=False, align="mid", orientation="vertical")

    pad.hist(x=xData, bins=xBinning, weights=y15_TET_0_weights+y15_TET_1_weights+y15_TET_2_weights+y15_TET_3_weights+y15_TET_4_weights,\
             label="$bg\_dip\_400\_600$", histtype="step", rwidth=1.0,\
             color=None, edgecolor="#84c1a3", linewidth=1, linestyle="solid",\
             bottom=None, cumulative=False, normed=False, align="mid", orientation="vertical")

    pad.hist(x=xData, bins=xBinning, weights=y15_TET_0_weights+y15_TET_1_weights+y15_TET_2_weights+y15_TET_3_weights,\
             label="$bg\_dip\_200\_400$", histtype="step", rwidth=1.0,\
             color=None, edgecolor="#89a8a0", linewidth=1, linestyle="solid",\
             bottom=None, cumulative=False, normed=False, align="mid", orientation="vertical")

    pad.hist(x=xData, bins=xBinning, weights=y15_TET_0_weights+y15_TET_1_weights+y15_TET_2_weights,\
             label="$bg\_dip\_100\_200$", histtype="step", rwidth=1.0,\
             color=None, edgecolor="#829e8c", linewidth=1, linestyle="solid",\
             bottom=None, cumulative=False, normed=False, align="mid", orientation="vertical")

    pad.hist(x=xData, bins=xBinning, weights=y15_TET_0_weights+y15_TET_1_weights,\
             label="$bg\_dip\_0\_100$", histtype="step", rwidth=1.0,\
             color=None, edgecolor="#adbcc6", linewidth=1, linestyle="solid",\
             bottom=None, cumulative=False, normed=False, align="mid", orientation="vertical")

    pad.hist(x=xData, bins=xBinning, weights=y15_TET_0_weights,\
             label="$signal$", histtype="step", rwidth=1.0,\
             color=None, edgecolor="#7a8e99", linewidth=1, linestyle="solid",\
             bottom=None, cumulative=False, normed=False, align="mid", orientation="vertical")


    # Axis
    plt.rc('text',usetex=False)
    plt.xlabel(r"TET",\
               fontsize=16,color="black")
    plt.ylabel(r"$\mathrm{Events}$ $(\mathcal{L}_{\mathrm{int}} = 40.0\ \mathrm{fb}^{-1})$ ",\
               fontsize=16,color="black")

    # Boundary of y-axis
    ymax=(y15_TET_0_weights+y15_TET_1_weights+y15_TET_2_weights+y15_TET_3_weights+y15_TET_4_weights+y15_TET_5_weights+y15_TET_6_weights+y15_TET_7_weights+y15_TET_8_weights+y15_TET_9_weights+y15_TET_10_weights+y15_TET_11_weights+y15_TET_12_weights+y15_TET_13_weights+y15_TET_14_weights+y15_TET_15_weights+y15_TET_16_weights).max()*1.1
    ymin=0 # linear scale
    #ymin=min([x for x in (y15_TET_0_weights+y15_TET_1_weights+y15_TET_2_weights+y15_TET_3_weights+y15_TET_4_weights+y15_TET_5_weights+y15_TET_6_weights+y15_TET_7_weights+y15_TET_8_weights+y15_TET_9_weights+y15_TET_10_weights+y15_TET_11_weights+y15_TET_12_weights+y15_TET_13_weights+y15_TET_14_weights+y15_TET_15_weights+y15_TET_16_weights) if x])/100. # log scale
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
    plt.savefig('../../HTML/MadAnalysis5job_0/selection_14.png')
    plt.savefig('../../PDF/MadAnalysis5job_0/selection_14.png')
    plt.savefig('../../DVI/MadAnalysis5job_0/selection_14.eps')

# Running!
if __name__ == '__main__':
    selection_14()
