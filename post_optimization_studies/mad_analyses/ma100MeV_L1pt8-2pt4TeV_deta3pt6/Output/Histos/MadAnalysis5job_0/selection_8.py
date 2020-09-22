def selection_8():

    # Library import
    import numpy
    import matplotlib
    import matplotlib.pyplot   as plt
    import matplotlib.gridspec as gridspec

    # Library version
    matplotlib_version = matplotlib.__version__
    numpy_version      = numpy.__version__

    # Histo binning
    xBinning = numpy.linspace(3.6,15.0,101,endpoint=True)

    # Creating data sequence: middle of each bin
    xData = numpy.array([3.657,3.771,3.885,3.999,4.113,4.227,4.341,4.455,4.569,4.683,4.797,4.911,5.025,5.139,5.253,5.367,5.481,5.595,5.709,5.823,5.937,6.051,6.165,6.279,6.393,6.507,6.621,6.735,6.849,6.963,7.077,7.191,7.305,7.419,7.533,7.647,7.761,7.875,7.989,8.103,8.217,8.331,8.445,8.559,8.673,8.787,8.901,9.015,9.129,9.243,9.357,9.471,9.585,9.699,9.813,9.927,10.041,10.155,10.269,10.383,10.497,10.611,10.725,10.839,10.953,11.067,11.181,11.295,11.409,11.523,11.637,11.751,11.865,11.979,12.093,12.207,12.321,12.435,12.549,12.663,12.777,12.891,13.005,13.119,13.233,13.347,13.461,13.575,13.689,13.803,13.917,14.031,14.145,14.259,14.373,14.487,14.601,14.715,14.829,14.943])

    # Creating weights for histo: y9_sdETA_0
    y9_sdETA_0_weights = numpy.array([1.26485585594,1.26662505574,1.21355386178,1.16225226763,1.12687147166,1.08264587669,1.11625747287,1.0791078771,1.02249868354,0.918126295432,0.955275891201,0.886283499058,0.765989512759,0.744761115177,0.675769123035,0.77660391155,0.643926726661,0.624467128877,0.594393932303,0.530708739556,0.516556341168,0.520094740765,0.440488349831,0.44225714963,0.410414753257,0.321963323331,0.29896592595,0.290120766957,0.247664091793,0.268892449375,0.198131257434,0.198131257434,0.196362217636,0.14329134368,0.132677184889,0.123832025896,0.088451469926,0.0937585493215,0.0760682713363,0.0849133903289,0.0955275891201,0.0548399137541,0.044225714963,0.0371496117689,0.0371496117689,0.0300734965748,0.0265354369778,0.0141522343882,0.0159212621867,0.0141522343882,0.00707611519408,0.00353805839704,0.0088451469926,0.00707611519408,0.00176902899852,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0])

    # Creating weights for histo: y9_sdETA_1
    y9_sdETA_1_weights = numpy.array([0.784372259713,0.753332942473,0.735214550391,0.762986066217,0.751217025071,0.723427123865,0.719131339913,0.651851241688,0.665725009136,0.641090598653,0.620809526355,0.575953596218,0.562013881212,0.553511842114,0.479794462876,0.530000138845,0.437025273343,0.421000416461,0.362269200084,0.353730789909,0.363332634431,0.332331087156,0.282099551751,0.254288427422,0.271424360765,0.216926657857,0.193403203931,0.193401245489,0.169899734114,0.136774555571,0.153878114658,0.139958103983,0.0993890448854,0.0918838530854,0.106863501127,0.0790814336912,0.0716013019631,0.0683922138605,0.0491504351061,0.0363254136853,0.0470010643063,0.0235026065036,0.0341940205893,0.0213727441904,0.0288528559343,0.0213693468919,0.00961623307992,0.0128276353423,0.00854663963081,0.0138953622756,0.00961360317125,0.00427277025242,0.00320690823604,0.00427277025242,0.00106959065133,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0])

    # Creating weights for histo: y9_sdETA_2
    y9_sdETA_2_weights = numpy.array([0.51876335166,0.495151744757,0.497929745569,0.497929745569,0.463900935621,0.457650933794,0.468762137042,0.477790139681,0.470150937448,0.447928130951,0.398621436537,0.400704917146,0.381259871461,0.352786903137,0.364592786588,0.345147820904,0.28472960324,0.281257282225,0.271534799383,0.248617552683,0.227089226389,0.226394746186,0.195838417253,0.179865772584,0.14236480162,0.163893127914,0.139586960808,0.132642318778,0.117364154311,0.102085989845,0.08264102416,0.0958358280175,0.0798631833479,0.0743074617237,0.0673628596935,0.0611126978662,0.0465289736027,0.0520846952269,0.0347231221513,0.027084035918,0.027778496121,0.0243061871059,0.0222227984968,0.0201394098877,0.0187504854817,0.0118058634514,0.0138892480605,0.00347231221513,0.00486123742118,0.00416677321815,0.00416677321815,0.00208338740908,0.00138892480605,0.0,0.000694462603025,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0])

    # Creating weights for histo: y9_sdETA_3
    y9_sdETA_3_weights = numpy.array([0.356565023559,0.373634628517,0.36889306714,0.36272902535,0.354668383009,0.3357021775,0.320055012956,0.32953813571,0.305830368824,0.304407888411,0.277381040562,0.254621553951,0.258414795053,0.236603628718,0.228542986377,0.222853144725,0.223801425,0.185869013983,0.203886899216,0.181127452606,0.166428608337,0.153626404619,0.141298361038,0.126125396631,0.123280435805,0.130392797871,0.107633311261,0.0862963050636,0.0810806235488,0.0758649020339,0.0730199812077,0.0450447730826,0.0578469768009,0.0521571351483,0.0497863344598,0.0331908936398,0.0431481725318,0.0360358264661,0.034613358053,0.021337002197,0.0175437570953,0.0156471365445,0.0151729804068,0.0109055791674,0.0123280435805,0.0109055791674,0.00853480247882,0.00568986565254,0.00616402179026,0.00331908936398,0.00284493362627,0.00142246681314,0.000948311075424,0.000474155737712,0.00189662255085,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0])

    # Creating weights for histo: y9_sdETA_4
    y9_sdETA_4_weights = numpy.array([0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0])

    # Creating weights for histo: y9_sdETA_5
    y9_sdETA_5_weights = numpy.array([0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,1.0529581672,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,1.0521138287,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0])

    # Creating weights for histo: y9_sdETA_6
    y9_sdETA_6_weights = numpy.array([0.23059715627,0.461112386191,0.230360177005,0.691774637787,1.38219088138,1.84211203079,0.920428310466,0.460551736365,0.230020174972,0.460138646192,0.229952466611,0.0,0.230673164862,0.230645228438,0.690907340558,0.0,0.230465313257,0.0,0.229952466611,0.0,0.0,0.230838554639,0.0,0.0,0.230619674488,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0])

    # Creating weights for histo: y9_sdETA_7
    y9_sdETA_7_weights = numpy.array([0.91384050047,0.554062353954,0.747483349572,0.747725310461,0.581238908595,0.49836595783,0.526385721164,0.387815220248,0.221762693878,0.249246258034,0.166205588752,0.110557354,0.110729227013,0.110826665317,0.110868710349,0.138278109069,0.0276831145718,0.0554152752696,0.110685220136,0.0,0.0277179123174,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0])

    # Creating weights for histo: y9_sdETA_8
    y9_sdETA_8_weights = numpy.array([0.262182322463,0.191670592855,0.181611577053,0.181468716064,0.201638393676,0.161341763234,0.120973034723,0.0806120743534,0.0705980288115,0.0302362005952,0.0604708961129,0.0403323881713,0.0302062143528,0.0100796984807,0.0100795224837,0.0504170024294,0.0,0.0201830108996,0.0100795224837,0.0100450210086,0.0,0.010012643635,0.0100921881967,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0])

    # Creating weights for histo: y9_sdETA_9
    y9_sdETA_9_weights = numpy.array([0.121642005754,0.10187144924,0.104667041066,0.0735893446158,0.0679060916113,0.0678662705582,0.0282866022872,0.03678408414,0.0282986140097,0.0311159631356,0.00566743231172,0.0141469542924,0.0113139114394,0.0113231876286,0.00566538931856,0.00283441331285,0.0,0.00283102910045,0.0,0.00282142741735,0.00282586005844,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0])

    # Creating weights for histo: y9_sdETA_10
    y9_sdETA_10_weights = numpy.array([0.0121872169607,0.0106563239972,0.00303761383335,0.00915251531391,0.0076228751579,0.00306125525669,0.00153333593818,0.0,0.00303360366741,0.0,0.00151881873561,0.0,0.00153821479612,0.0,0.0,0.00152260670551,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0])

    # Creating weights for histo: y9_sdETA_11
    y9_sdETA_11_weights = numpy.array([0.00144396078159,0.000902635834474,0.000902943051981,0.000180547147582,0.000541688372338,0.000361042822758,0.000181168435318,0.0,0.000360556664527,0.000181168435318,0.0,0.000180755039128,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0])

    # Creating weights for histo: y9_sdETA_12
    y9_sdETA_12_weights = numpy.array([0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0121753363378,0.0,0.0,0.012124083239,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0])

    # Creating weights for histo: y9_sdETA_13
    y9_sdETA_13_weights = numpy.array([0.0,0.0,0.0,0.0,0.0,0.0,0.0100568570688,0.0501713567767,0.0200794017035,0.0200777075684,0.0100184167299,0.0301559479279,0.030147101237,0.0200884384681,0.0401541383374,0.0301172224785,0.0,0.0100696705151,0.0100584809593,0.0200730714231,0.0301047065389,0.0401576918891,0.0300999381684,0.050153010533,0.0301384156956,0.0200591464589,0.0100262841281,0.0201393410301,0.0100153631547,0.0301271641592,0.0200509278376,0.0200939795296,0.0100584809593,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0])

    # Creating weights for histo: y9_sdETA_14
    y9_sdETA_14_weights = numpy.array([0.0880083837672,0.132010361546,0.10439925811,0.104526335527,0.18701765808,0.154076493863,0.165019736437,0.137499756609,0.21448360563,0.142987567267,0.137461649634,0.0935197979989,0.132012799093,0.126557854685,0.148465383984,0.137538676099,0.115474615698,0.0659982743917,0.0769952242378,0.0880737912616,0.0990298715801,0.0990466093986,0.0550064840188,0.0384810164906,0.0330127305795,0.0220136600681,0.0384987171399,0.0164906228027,0.0110140045455,0.0219703367438,0.0,0.00551630151219,0.00550877761904,0.00550972826213,0.0,0.00551421741004,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0])

    # Creating weights for histo: y9_sdETA_15
    y9_sdETA_15_weights = numpy.array([0.138132422995,0.154929199354,0.163860950548,0.152944534994,0.142093013644,0.143075325101,0.139158184308,0.130283350822,0.119394351966,0.108560467089,0.0838788646159,0.116448780415,0.0898177063618,0.0789530378227,0.0700714704105,0.0532833118734,0.0611837302328,0.0394612393126,0.0384948968804,0.0335560671967,0.0286149046886,0.0148089093761,0.0187501319712,0.0148006122173,0.012829311494,0.00789720771968,0.00690275114645,0.00197192601644,0.00197234728765,0.00197209155879,0.000985635530986,0.0,0.000988438527688,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0])

    # Creating weights for histo: y9_sdETA_16
    y9_sdETA_16_weights = numpy.array([0.0801557610904,0.0854663305328,0.0763641776742,0.0685538671355,0.073851993088,0.0610092711211,0.0572129663808,0.0534381876779,0.0426006681052,0.0365545763727,0.0345352580194,0.0264702080345,0.0231856628262,0.0216781160082,0.0176463372251,0.0151233376055,0.0131040312556,0.00781172693596,0.00807054352561,0.00403376734087,0.0030243398292,0.00378194591313,0.00352765539288,0.00176394192848,0.000755526700727,0.000252130794508,0.0,0.0,0.000252082340918,0.000252305643547,0.000503987352101,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0])

    # Creating weights for histo: y9_sdETA_17
    y9_sdETA_17_weights = numpy.array([0.0389260031169,0.0358018373867,0.0326397426349,0.0343628239,0.0271982376438,0.0243259290152,0.0151663901852,0.0180442971934,0.0166066633073,0.0105892450106,0.010036534989,0.0088736325837,0.00800976662419,0.0040061104569,0.00400220758657,0.00228957829618,0.00114437376832,0.000573715741641,0.00114913738952,0.000575049055722,0.00114231136527,0.000287772706027,0.000284774873731,0.0,0.000285168759723,0.0,0.000286315227885,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0])

    # Creating weights for histo: y9_sdETA_18
    y9_sdETA_18_weights = numpy.array([0.0050109188725,0.00440616414616,0.00321834372092,0.00306549751686,0.00220213198371,0.00200921522601,0.00144556915272,0.00112318962127,0.000948659418907,0.000691015465288,0.000626243845253,0.000259269415301,0.000192942029157,0.000216026015785,0.000107999513019,0.000129604428005,2.16086155982e-05,2.16292015664e-05,8.63666443678e-05,2.16142021404e-05,2.15594557025e-05,6.47874199332e-05,2.16179949542e-05,0.0,2.15983645236e-05,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0])

    # Creating weights for histo: y9_sdETA_19
    y9_sdETA_19_weights = numpy.array([0.00104856559702,0.000397288422255,0.00045328392216,0.000312226970837,0.000282454230415,0.000141798218465,0.00011367591924,0.000113632160691,0.000112307183909,2.83973975057e-05,5.67472649421e-05,2.84292624007e-05,2.83684874635e-05,2.82164090598e-05,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0])

    # Creating a new Canvas
    fig   = plt.figure(figsize=(12,6),dpi=80)
    frame = gridspec.GridSpec(1,1,right=0.7)
    pad   = fig.add_subplot(frame[0])

    # Creating a new Stack
    pad.hist(x=xData, bins=xBinning, weights=y9_sdETA_0_weights+y9_sdETA_1_weights+y9_sdETA_2_weights+y9_sdETA_3_weights+y9_sdETA_4_weights+y9_sdETA_5_weights+y9_sdETA_6_weights+y9_sdETA_7_weights+y9_sdETA_8_weights+y9_sdETA_9_weights+y9_sdETA_10_weights+y9_sdETA_11_weights+y9_sdETA_12_weights+y9_sdETA_13_weights+y9_sdETA_14_weights+y9_sdETA_15_weights+y9_sdETA_16_weights+y9_sdETA_17_weights+y9_sdETA_18_weights+y9_sdETA_19_weights,\
             label="$bg\_vbf\_1600\_inf$", histtype="step", rwidth=1.0,\
             color=None, edgecolor="#ccc6aa", linewidth=1, linestyle="solid",\
             bottom=None, cumulative=False, normed=False, align="mid", orientation="vertical")

    pad.hist(x=xData, bins=xBinning, weights=y9_sdETA_0_weights+y9_sdETA_1_weights+y9_sdETA_2_weights+y9_sdETA_3_weights+y9_sdETA_4_weights+y9_sdETA_5_weights+y9_sdETA_6_weights+y9_sdETA_7_weights+y9_sdETA_8_weights+y9_sdETA_9_weights+y9_sdETA_10_weights+y9_sdETA_11_weights+y9_sdETA_12_weights+y9_sdETA_13_weights+y9_sdETA_14_weights+y9_sdETA_15_weights+y9_sdETA_16_weights+y9_sdETA_17_weights+y9_sdETA_18_weights,\
             label="$bg\_vbf\_1200\_1600$", histtype="step", rwidth=1.0,\
             color=None, edgecolor="#c1bfa8", linewidth=1, linestyle="solid",\
             bottom=None, cumulative=False, normed=False, align="mid", orientation="vertical")

    pad.hist(x=xData, bins=xBinning, weights=y9_sdETA_0_weights+y9_sdETA_1_weights+y9_sdETA_2_weights+y9_sdETA_3_weights+y9_sdETA_4_weights+y9_sdETA_5_weights+y9_sdETA_6_weights+y9_sdETA_7_weights+y9_sdETA_8_weights+y9_sdETA_9_weights+y9_sdETA_10_weights+y9_sdETA_11_weights+y9_sdETA_12_weights+y9_sdETA_13_weights+y9_sdETA_14_weights+y9_sdETA_15_weights+y9_sdETA_16_weights+y9_sdETA_17_weights,\
             label="$bg\_vbf\_800\_1200$", histtype="step", rwidth=1.0,\
             color=None, edgecolor="#bab5a3", linewidth=1, linestyle="solid",\
             bottom=None, cumulative=False, normed=False, align="mid", orientation="vertical")

    pad.hist(x=xData, bins=xBinning, weights=y9_sdETA_0_weights+y9_sdETA_1_weights+y9_sdETA_2_weights+y9_sdETA_3_weights+y9_sdETA_4_weights+y9_sdETA_5_weights+y9_sdETA_6_weights+y9_sdETA_7_weights+y9_sdETA_8_weights+y9_sdETA_9_weights+y9_sdETA_10_weights+y9_sdETA_11_weights+y9_sdETA_12_weights+y9_sdETA_13_weights+y9_sdETA_14_weights+y9_sdETA_15_weights+y9_sdETA_16_weights,\
             label="$bg\_vbf\_600\_800$", histtype="step", rwidth=1.0,\
             color=None, edgecolor="#b2a596", linewidth=1, linestyle="solid",\
             bottom=None, cumulative=False, normed=False, align="mid", orientation="vertical")

    pad.hist(x=xData, bins=xBinning, weights=y9_sdETA_0_weights+y9_sdETA_1_weights+y9_sdETA_2_weights+y9_sdETA_3_weights+y9_sdETA_4_weights+y9_sdETA_5_weights+y9_sdETA_6_weights+y9_sdETA_7_weights+y9_sdETA_8_weights+y9_sdETA_9_weights+y9_sdETA_10_weights+y9_sdETA_11_weights+y9_sdETA_12_weights+y9_sdETA_13_weights+y9_sdETA_14_weights+y9_sdETA_15_weights,\
             label="$bg\_vbf\_400\_600$", histtype="step", rwidth=1.0,\
             color=None, edgecolor="#b7a39b", linewidth=1, linestyle="solid",\
             bottom=None, cumulative=False, normed=False, align="mid", orientation="vertical")

    pad.hist(x=xData, bins=xBinning, weights=y9_sdETA_0_weights+y9_sdETA_1_weights+y9_sdETA_2_weights+y9_sdETA_3_weights+y9_sdETA_4_weights+y9_sdETA_5_weights+y9_sdETA_6_weights+y9_sdETA_7_weights+y9_sdETA_8_weights+y9_sdETA_9_weights+y9_sdETA_10_weights+y9_sdETA_11_weights+y9_sdETA_12_weights+y9_sdETA_13_weights+y9_sdETA_14_weights,\
             label="$bg\_vbf\_200\_400$", histtype="step", rwidth=1.0,\
             color=None, edgecolor="#ad998c", linewidth=1, linestyle="solid",\
             bottom=None, cumulative=False, normed=False, align="mid", orientation="vertical")

    pad.hist(x=xData, bins=xBinning, weights=y9_sdETA_0_weights+y9_sdETA_1_weights+y9_sdETA_2_weights+y9_sdETA_3_weights+y9_sdETA_4_weights+y9_sdETA_5_weights+y9_sdETA_6_weights+y9_sdETA_7_weights+y9_sdETA_8_weights+y9_sdETA_9_weights+y9_sdETA_10_weights+y9_sdETA_11_weights+y9_sdETA_12_weights+y9_sdETA_13_weights,\
             label="$bg\_vbf\_100\_200$", histtype="step", rwidth=1.0,\
             color=None, edgecolor="#9b8e82", linewidth=1, linestyle="solid",\
             bottom=None, cumulative=False, normed=False, align="mid", orientation="vertical")

    pad.hist(x=xData, bins=xBinning, weights=y9_sdETA_0_weights+y9_sdETA_1_weights+y9_sdETA_2_weights+y9_sdETA_3_weights+y9_sdETA_4_weights+y9_sdETA_5_weights+y9_sdETA_6_weights+y9_sdETA_7_weights+y9_sdETA_8_weights+y9_sdETA_9_weights+y9_sdETA_10_weights+y9_sdETA_11_weights+y9_sdETA_12_weights,\
             label="$bg\_vbf\_0\_100$", histtype="step", rwidth=1.0,\
             color=None, edgecolor="#876656", linewidth=1, linestyle="solid",\
             bottom=None, cumulative=False, normed=False, align="mid", orientation="vertical")

    pad.hist(x=xData, bins=xBinning, weights=y9_sdETA_0_weights+y9_sdETA_1_weights+y9_sdETA_2_weights+y9_sdETA_3_weights+y9_sdETA_4_weights+y9_sdETA_5_weights+y9_sdETA_6_weights+y9_sdETA_7_weights+y9_sdETA_8_weights+y9_sdETA_9_weights+y9_sdETA_10_weights+y9_sdETA_11_weights,\
             label="$bg\_dip\_1600\_inf$", histtype="step", rwidth=1.0,\
             color=None, edgecolor="#afcec6", linewidth=1, linestyle="solid",\
             bottom=None, cumulative=False, normed=False, align="mid", orientation="vertical")

    pad.hist(x=xData, bins=xBinning, weights=y9_sdETA_0_weights+y9_sdETA_1_weights+y9_sdETA_2_weights+y9_sdETA_3_weights+y9_sdETA_4_weights+y9_sdETA_5_weights+y9_sdETA_6_weights+y9_sdETA_7_weights+y9_sdETA_8_weights+y9_sdETA_9_weights+y9_sdETA_10_weights,\
             label="$bg\_dip\_1200\_1600$", histtype="step", rwidth=1.0,\
             color=None, edgecolor="#84c1a3", linewidth=1, linestyle="solid",\
             bottom=None, cumulative=False, normed=False, align="mid", orientation="vertical")

    pad.hist(x=xData, bins=xBinning, weights=y9_sdETA_0_weights+y9_sdETA_1_weights+y9_sdETA_2_weights+y9_sdETA_3_weights+y9_sdETA_4_weights+y9_sdETA_5_weights+y9_sdETA_6_weights+y9_sdETA_7_weights+y9_sdETA_8_weights+y9_sdETA_9_weights,\
             label="$bg\_dip\_800\_1200$", histtype="step", rwidth=1.0,\
             color=None, edgecolor="#89a8a0", linewidth=1, linestyle="solid",\
             bottom=None, cumulative=False, normed=False, align="mid", orientation="vertical")

    pad.hist(x=xData, bins=xBinning, weights=y9_sdETA_0_weights+y9_sdETA_1_weights+y9_sdETA_2_weights+y9_sdETA_3_weights+y9_sdETA_4_weights+y9_sdETA_5_weights+y9_sdETA_6_weights+y9_sdETA_7_weights+y9_sdETA_8_weights,\
             label="$bg\_dip\_600\_800$", histtype="step", rwidth=1.0,\
             color=None, edgecolor="#829e8c", linewidth=1, linestyle="solid",\
             bottom=None, cumulative=False, normed=False, align="mid", orientation="vertical")

    pad.hist(x=xData, bins=xBinning, weights=y9_sdETA_0_weights+y9_sdETA_1_weights+y9_sdETA_2_weights+y9_sdETA_3_weights+y9_sdETA_4_weights+y9_sdETA_5_weights+y9_sdETA_6_weights+y9_sdETA_7_weights,\
             label="$bg\_dip\_400\_600$", histtype="step", rwidth=1.0,\
             color=None, edgecolor="#adbcc6", linewidth=1, linestyle="solid",\
             bottom=None, cumulative=False, normed=False, align="mid", orientation="vertical")

    pad.hist(x=xData, bins=xBinning, weights=y9_sdETA_0_weights+y9_sdETA_1_weights+y9_sdETA_2_weights+y9_sdETA_3_weights+y9_sdETA_4_weights+y9_sdETA_5_weights+y9_sdETA_6_weights,\
             label="$bg\_dip\_200\_400$", histtype="step", rwidth=1.0,\
             color=None, edgecolor="#7a8e99", linewidth=1, linestyle="solid",\
             bottom=None, cumulative=False, normed=False, align="mid", orientation="vertical")

    pad.hist(x=xData, bins=xBinning, weights=y9_sdETA_0_weights+y9_sdETA_1_weights+y9_sdETA_2_weights+y9_sdETA_3_weights+y9_sdETA_4_weights+y9_sdETA_5_weights,\
             label="$bg\_dip\_100\_200$", histtype="step", rwidth=1.0,\
             color=None, edgecolor="#758991", linewidth=1, linestyle="solid",\
             bottom=None, cumulative=False, normed=False, align="mid", orientation="vertical")

    pad.hist(x=xData, bins=xBinning, weights=y9_sdETA_0_weights+y9_sdETA_1_weights+y9_sdETA_2_weights+y9_sdETA_3_weights+y9_sdETA_4_weights,\
             label="$bg\_dip\_0\_100$", histtype="step", rwidth=1.0,\
             color=None, edgecolor="#688296", linewidth=1, linestyle="solid",\
             bottom=None, cumulative=False, normed=False, align="mid", orientation="vertical")

    pad.hist(x=xData, bins=xBinning, weights=y9_sdETA_0_weights+y9_sdETA_1_weights+y9_sdETA_2_weights+y9_sdETA_3_weights,\
             label="$signal\_2pt4TeVL$", histtype="step", rwidth=1.0,\
             color=None, edgecolor="#6d7a84", linewidth=1, linestyle="solid",\
             bottom=None, cumulative=False, normed=False, align="mid", orientation="vertical")

    pad.hist(x=xData, bins=xBinning, weights=y9_sdETA_0_weights+y9_sdETA_1_weights+y9_sdETA_2_weights,\
             label="$signal\_2pt2TeVL$", histtype="step", rwidth=1.0,\
             color=None, edgecolor="#7c99d1", linewidth=1, linestyle="solid",\
             bottom=None, cumulative=False, normed=False, align="mid", orientation="vertical")

    pad.hist(x=xData, bins=xBinning, weights=y9_sdETA_0_weights+y9_sdETA_1_weights,\
             label="$signal\_2TeVL$", histtype="step", rwidth=1.0,\
             color=None, edgecolor="#7f7f9b", linewidth=1, linestyle="solid",\
             bottom=None, cumulative=False, normed=False, align="mid", orientation="vertical")

    pad.hist(x=xData, bins=xBinning, weights=y9_sdETA_0_weights,\
             label="$signal\_1pt8TeVL$", histtype="step", rwidth=1.0,\
             color=None, edgecolor="#aaa5bf", linewidth=1, linestyle="solid",\
             bottom=None, cumulative=False, normed=False, align="mid", orientation="vertical")


    # Axis
    plt.rc('text',usetex=False)
    plt.xlabel(r"\Delta\eta ( j_{1} , j_{2} ) ",\
               fontsize=16,color="black")
    plt.ylabel(r"$\mathrm{Events}$ $(\mathcal{L}_{\mathrm{int}} = 40.0\ \mathrm{fb}^{-1})$ ",\
               fontsize=16,color="black")

    # Boundary of y-axis
    ymax=(y9_sdETA_0_weights+y9_sdETA_1_weights+y9_sdETA_2_weights+y9_sdETA_3_weights+y9_sdETA_4_weights+y9_sdETA_5_weights+y9_sdETA_6_weights+y9_sdETA_7_weights+y9_sdETA_8_weights+y9_sdETA_9_weights+y9_sdETA_10_weights+y9_sdETA_11_weights+y9_sdETA_12_weights+y9_sdETA_13_weights+y9_sdETA_14_weights+y9_sdETA_15_weights+y9_sdETA_16_weights+y9_sdETA_17_weights+y9_sdETA_18_weights+y9_sdETA_19_weights).max()*1.1
    ymin=0 # linear scale
    #ymin=min([x for x in (y9_sdETA_0_weights+y9_sdETA_1_weights+y9_sdETA_2_weights+y9_sdETA_3_weights+y9_sdETA_4_weights+y9_sdETA_5_weights+y9_sdETA_6_weights+y9_sdETA_7_weights+y9_sdETA_8_weights+y9_sdETA_9_weights+y9_sdETA_10_weights+y9_sdETA_11_weights+y9_sdETA_12_weights+y9_sdETA_13_weights+y9_sdETA_14_weights+y9_sdETA_15_weights+y9_sdETA_16_weights+y9_sdETA_17_weights+y9_sdETA_18_weights+y9_sdETA_19_weights) if x])/100. # log scale
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
    plt.savefig('../../HTML/MadAnalysis5job_0/selection_8.png')
    plt.savefig('../../PDF/MadAnalysis5job_0/selection_8.png')
    plt.savefig('../../DVI/MadAnalysis5job_0/selection_8.eps')

# Running!
if __name__ == '__main__':
    selection_8()
