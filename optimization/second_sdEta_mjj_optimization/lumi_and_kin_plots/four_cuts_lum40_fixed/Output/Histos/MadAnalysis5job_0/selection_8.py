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
    xBinning = numpy.linspace(-15.0,15.0,101,endpoint=True)

    # Creating data sequence: middle of each bin
    xData = numpy.array([-14.85,-14.55,-14.25,-13.95,-13.65,-13.35,-13.05,-12.75,-12.45,-12.15,-11.85,-11.55,-11.25,-10.95,-10.65,-10.35,-10.05,-9.75,-9.45,-9.15,-8.85,-8.55,-8.25,-7.95,-7.65,-7.35,-7.05,-6.75,-6.45,-6.15,-5.85,-5.55,-5.25,-4.95,-4.65,-4.35,-4.05,-3.75,-3.45,-3.15,-2.85,-2.55,-2.25,-1.95,-1.65,-1.35,-1.05,-0.75,-0.45,-0.15,0.15,0.45,0.75,1.05,1.35,1.65,1.95,2.25,2.55,2.85,3.15,3.45,3.75,4.05,4.35,4.65,4.95,5.25,5.55,5.85,6.15,6.45,6.75,7.05,7.35,7.65,7.95,8.25,8.55,8.85,9.15,9.45,9.75,10.05,10.35,10.65,10.95,11.25,11.55,11.85,12.15,12.45,12.75,13.05,13.35,13.65,13.95,14.25,14.55,14.85])

    # Creating weights for histo: y9_sdETA_0
    y9_sdETA_0_weights = numpy.array([0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0040940842475,0.0450349187226,0.176045598643,0.433972802236,0.732840928303,1.07264981685,1.65810408024,2.28040470986,3.41037167417,4.65906772966,6.14931436375,8.28642440495,10.4399144311,13.0191880671,16.0938412489,20.5318291812,25.6944684493,31.8970067643,40.2653230942,49.6857944597,64.6988206993,83.1344838018,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,82.2870045786,64.3426210258,50.4636737467,39.864091462,32.0935225842,25.3833207345,20.163361519,16.5523808287,12.9045521721,10.2024586488,8.20044848375,6.08380642379,4.44207992854,3.35714852295,2.32543946858,1.69495084647,0.974391906906,0.704182554571,0.34390304479,0.1637633299,0.0777876087026,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0])

    # Creating weights for histo: y9_sdETA_1
    y9_sdETA_1_weights = numpy.array([0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.012170493784,0.0,0.0,0.0121313846429,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0121753353338,0.0121240822392,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0])

    # Creating weights for histo: y9_sdETA_2
    y9_sdETA_2_weights = numpy.array([0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0301473762652,0.0100340930726,0.0100457330197,0.0301425500464,0.0300900359932,0.0200777063575,0.0702554482367,0.100406671428,0.100394110037,0.0803328243927,0.0501777584074,0.0100532491943,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0602281936847,0.0501755271076,0.060303066188,0.0802988177314,0.0201306542745,0.0602362511561,0.11035599577,0.0602522008174,0.0401809858895,0.0602188139616,0.0201117295469,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0])

    # Creating weights for histo: y9_sdETA_3
    y9_sdETA_3_weights = numpy.array([0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0220052378129,0.0220090281975,0.0769860409505,0.137522381837,0.153994182321,0.192441559741,0.285847440813,0.297113007997,0.324654681321,0.46767941771,0.384984927667,0.373967705827,0.296951926811,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.307900491097,0.324564167101,0.42358582988,0.456440704161,0.33006193094,0.335557013479,0.23648058716,0.247565491536,0.159567144464,0.0825033457858,0.0604944963417,0.0219703362123,0.0165348029307,0.00551421727662,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0])

    # Creating weights for histo: y9_sdETA_4
    y9_sdETA_4_weights = numpy.array([0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.00197140379939,0.00592371465157,0.00987588801941,0.0236909986236,0.0424524746535,0.0739897358908,0.124367680965,0.190481849638,0.261508417493,0.325667062006,0.380926021356,0.401643827211,0.424301484814,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.391787804274,0.396688900079,0.36218534434,0.286159116844,0.257600655972,0.178621000582,0.134208472402,0.0789445828569,0.0444167769665,0.0286113262013,0.00690509621651,0.00295772718437,0.000988438559298,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0])

    # Creating weights for histo: y9_sdETA_5
    y9_sdETA_5_weights = numpy.array([0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.000757029996663,0.00151186817838,0.0042871428253,0.0103396129409,0.0226901020647,0.0451265809715,0.0761304796025,0.105624634651,0.152262719699,0.193092535145,0.206957665226,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.213762654472,0.189035516885,0.147709162127,0.10486730217,0.0680573345548,0.0481469483831,0.0257057161427,0.0131107104159,0.00831703747558,0.00126001591727,0.000252082365669,0.000756292989884,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0])

    # Creating weights for histo: y9_sdETA_6
    y9_sdETA_6_weights = numpy.array([0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.000286823109472,0.00200131193253,0.00400920795999,0.00946025973121,0.0180342219072,0.0337704787167,0.0621342318367,0.083876120953,0.112820855969,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.097340964982,0.0790310128556,0.0483750429746,0.0326446644643,0.0240499712866,0.0088655947939,0.00286394133594,0.00229240970515,0.000572547736784,0.00028516878814,0.000286315256417,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0])

    # Creating weights for histo: y9_sdETA_7
    y9_sdETA_7_weights = numpy.array([0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,4.31994812092e-05,8.62795202088e-05,0.000215991580619,0.000518577003051,0.00118825804054,0.00211680052126,0.00408084409555,0.00755709603326,0.013149585647,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0115985594036,0.00677975355983,0.00397300412493,0.0022875287012,0.000581913225435,0.000410472750833,0.000151163923177,4.31736649281e-05,8.64054164887e-05,2.15983659715e-05,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0])

    # Creating weights for histo: y9_sdETA_8
    y9_sdETA_8_weights = numpy.array([0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,5.6897821073e-05,0.0,0.000198819151425,0.000227258054067,0.000282328053456,0.00034056226998,0.00156033174533,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.00184232125279,0.000679927898669,0.000340677048949,0.000169101940697,8.51476279606e-05,2.82164125923e-05,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0])

    # Creating weights for histo: y9_sdETA_9
    y9_sdETA_9_weights = numpy.array([0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0])

    # Creating weights for histo: y9_sdETA_10
    y9_sdETA_10_weights = numpy.array([0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,1.05462838872,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,1.0529581672,0.0,0.0,1.0521138287,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0])

    # Creating weights for histo: y9_sdETA_11
    y9_sdETA_11_weights = numpy.array([0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.230360184413,0.0,0.0,0.23002018237,1.1526883935,0.921039713543,2.07353443499,1.38215134602,2.07062435873,1.84408147348,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.922069556985,2.53441358415,2.76264418298,0.920111317366,0.23067317228,0.921552329644,0.460417640967,0.0,0.230838562063,0.230619681904,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0])

    # Creating weights for histo: y9_sdETA_12
    y9_sdETA_12_weights = numpy.array([0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0276234280355,0.138425976899,0.0553289535151,0.13828937863,0.526374944803,0.719702077599,0.914367496441,1.57806389939,1.7720595982,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,1.96623647916,1.79964160053,1.19103996065,0.581753213717,0.30443534096,0.304603059476,0.166169889146,0.0830147412951,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0])

    # Creating weights for histo: y9_sdETA_13
    y9_sdETA_13_weights = numpy.array([0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.010071237928,0.0,0.0201624848897,0.0201955419739,0.0705398851977,0.131099711031,0.11095012247,0.372948604553,0.423539294971,0.695428320723,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.564876445749,0.524269698767,0.282269447858,0.141149865737,0.100776769892,0.0705762376733,0.0201830097766,0.0201245423725,0.020104830713,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0])

    # Creating weights for histo: y9_sdETA_14
    y9_sdETA_14_weights = numpy.array([0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.00283198080757,0.0,0.00283201504984,0.0113239426636,0.00847699491002,0.0311210751141,0.059421018831,0.121587112765,0.183925302917,0.328192450261,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.288582541648,0.203725871136,0.104646619783,0.0679054816319,0.033956380499,0.0141618950907,0.00283102933441,0.00564728755774,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0])

    # Creating weights for histo: y9_sdETA_15
    y9_sdETA_15_weights = numpy.array([0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.00305428566281,0.00303458230967,0.00910681985313,0.0106569847957,0.0243862885913,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0243561975727,0.0183003505338,0.00459459124653,0.00455242245421,0.00153821481342,0.0,0.00152260672263,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0])

    # Creating weights for histo: y9_sdETA_16
    y9_sdETA_16_weights = numpy.array([0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.000180402052681,0.000360206648139,0.0,0.000542069138978,0.000903697264858,0.0025274581062,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.00288891029423,0.00108286551967,0.000542211198206,0.000541724962963,0.000180755044838,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0])

    # Creating a new Canvas
    fig   = plt.figure(figsize=(12,6),dpi=80)
    frame = gridspec.GridSpec(1,1,right=0.7)
    pad   = fig.add_subplot(frame[0])

    # Creating a new Stack
    pad.hist(x=xData, bins=xBinning, weights=y9_sdETA_0_weights+y9_sdETA_1_weights+y9_sdETA_2_weights+y9_sdETA_3_weights+y9_sdETA_4_weights+y9_sdETA_5_weights+y9_sdETA_6_weights+y9_sdETA_7_weights+y9_sdETA_8_weights+y9_sdETA_9_weights+y9_sdETA_10_weights+y9_sdETA_11_weights+y9_sdETA_12_weights+y9_sdETA_13_weights+y9_sdETA_14_weights+y9_sdETA_15_weights+y9_sdETA_16_weights,\
             label="$bg\_dip\_1600\_inf$", histtype="step", rwidth=1.0,\
             color=None, edgecolor="#e5e5e5", linewidth=1, linestyle="solid",\
             bottom=None, cumulative=False, normed=False, align="mid", orientation="vertical")

    pad.hist(x=xData, bins=xBinning, weights=y9_sdETA_0_weights+y9_sdETA_1_weights+y9_sdETA_2_weights+y9_sdETA_3_weights+y9_sdETA_4_weights+y9_sdETA_5_weights+y9_sdETA_6_weights+y9_sdETA_7_weights+y9_sdETA_8_weights+y9_sdETA_9_weights+y9_sdETA_10_weights+y9_sdETA_11_weights+y9_sdETA_12_weights+y9_sdETA_13_weights+y9_sdETA_14_weights+y9_sdETA_15_weights,\
             label="$bg\_dip\_1200\_1600$", histtype="step", rwidth=1.0,\
             color=None, edgecolor="#f2f2f2", linewidth=1, linestyle="solid",\
             bottom=None, cumulative=False, normed=False, align="mid", orientation="vertical")

    pad.hist(x=xData, bins=xBinning, weights=y9_sdETA_0_weights+y9_sdETA_1_weights+y9_sdETA_2_weights+y9_sdETA_3_weights+y9_sdETA_4_weights+y9_sdETA_5_weights+y9_sdETA_6_weights+y9_sdETA_7_weights+y9_sdETA_8_weights+y9_sdETA_9_weights+y9_sdETA_10_weights+y9_sdETA_11_weights+y9_sdETA_12_weights+y9_sdETA_13_weights+y9_sdETA_14_weights,\
             label="$bg\_dip\_800\_1200$", histtype="step", rwidth=1.0,\
             color=None, edgecolor="#ccc6aa", linewidth=1, linestyle="solid",\
             bottom=None, cumulative=False, normed=False, align="mid", orientation="vertical")

    pad.hist(x=xData, bins=xBinning, weights=y9_sdETA_0_weights+y9_sdETA_1_weights+y9_sdETA_2_weights+y9_sdETA_3_weights+y9_sdETA_4_weights+y9_sdETA_5_weights+y9_sdETA_6_weights+y9_sdETA_7_weights+y9_sdETA_8_weights+y9_sdETA_9_weights+y9_sdETA_10_weights+y9_sdETA_11_weights+y9_sdETA_12_weights+y9_sdETA_13_weights,\
             label="$bg\_dip\_600\_800$", histtype="step", rwidth=1.0,\
             color=None, edgecolor="#ccc6aa", linewidth=1, linestyle="solid",\
             bottom=None, cumulative=False, normed=False, align="mid", orientation="vertical")

    pad.hist(x=xData, bins=xBinning, weights=y9_sdETA_0_weights+y9_sdETA_1_weights+y9_sdETA_2_weights+y9_sdETA_3_weights+y9_sdETA_4_weights+y9_sdETA_5_weights+y9_sdETA_6_weights+y9_sdETA_7_weights+y9_sdETA_8_weights+y9_sdETA_9_weights+y9_sdETA_10_weights+y9_sdETA_11_weights+y9_sdETA_12_weights,\
             label="$bg\_dip\_400\_600$", histtype="step", rwidth=1.0,\
             color=None, edgecolor="#c1bfa8", linewidth=1, linestyle="solid",\
             bottom=None, cumulative=False, normed=False, align="mid", orientation="vertical")

    pad.hist(x=xData, bins=xBinning, weights=y9_sdETA_0_weights+y9_sdETA_1_weights+y9_sdETA_2_weights+y9_sdETA_3_weights+y9_sdETA_4_weights+y9_sdETA_5_weights+y9_sdETA_6_weights+y9_sdETA_7_weights+y9_sdETA_8_weights+y9_sdETA_9_weights+y9_sdETA_10_weights+y9_sdETA_11_weights,\
             label="$bg\_dip\_200\_400$", histtype="step", rwidth=1.0,\
             color=None, edgecolor="#bab5a3", linewidth=1, linestyle="solid",\
             bottom=None, cumulative=False, normed=False, align="mid", orientation="vertical")

    pad.hist(x=xData, bins=xBinning, weights=y9_sdETA_0_weights+y9_sdETA_1_weights+y9_sdETA_2_weights+y9_sdETA_3_weights+y9_sdETA_4_weights+y9_sdETA_5_weights+y9_sdETA_6_weights+y9_sdETA_7_weights+y9_sdETA_8_weights+y9_sdETA_9_weights+y9_sdETA_10_weights,\
             label="$bg\_dip\_100\_200$", histtype="step", rwidth=1.0,\
             color=None, edgecolor="#b2a596", linewidth=1, linestyle="solid",\
             bottom=None, cumulative=False, normed=False, align="mid", orientation="vertical")

    pad.hist(x=xData, bins=xBinning, weights=y9_sdETA_0_weights+y9_sdETA_1_weights+y9_sdETA_2_weights+y9_sdETA_3_weights+y9_sdETA_4_weights+y9_sdETA_5_weights+y9_sdETA_6_weights+y9_sdETA_7_weights+y9_sdETA_8_weights+y9_sdETA_9_weights,\
             label="$bg\_dip\_0\_100$", histtype="step", rwidth=1.0,\
             color=None, edgecolor="#b7a39b", linewidth=1, linestyle="solid",\
             bottom=None, cumulative=False, normed=False, align="mid", orientation="vertical")

    pad.hist(x=xData, bins=xBinning, weights=y9_sdETA_0_weights+y9_sdETA_1_weights+y9_sdETA_2_weights+y9_sdETA_3_weights+y9_sdETA_4_weights+y9_sdETA_5_weights+y9_sdETA_6_weights+y9_sdETA_7_weights+y9_sdETA_8_weights,\
             label="$bg\_vbf\_1600\_inf$", histtype="step", rwidth=1.0,\
             color=None, edgecolor="#ad998c", linewidth=1, linestyle="solid",\
             bottom=None, cumulative=False, normed=False, align="mid", orientation="vertical")

    pad.hist(x=xData, bins=xBinning, weights=y9_sdETA_0_weights+y9_sdETA_1_weights+y9_sdETA_2_weights+y9_sdETA_3_weights+y9_sdETA_4_weights+y9_sdETA_5_weights+y9_sdETA_6_weights+y9_sdETA_7_weights,\
             label="$bg\_vbf\_1200\_1600$", histtype="step", rwidth=1.0,\
             color=None, edgecolor="#9b8e82", linewidth=1, linestyle="solid",\
             bottom=None, cumulative=False, normed=False, align="mid", orientation="vertical")

    pad.hist(x=xData, bins=xBinning, weights=y9_sdETA_0_weights+y9_sdETA_1_weights+y9_sdETA_2_weights+y9_sdETA_3_weights+y9_sdETA_4_weights+y9_sdETA_5_weights+y9_sdETA_6_weights,\
             label="$bg\_vbf\_800\_1200$", histtype="step", rwidth=1.0,\
             color=None, edgecolor="#876656", linewidth=1, linestyle="solid",\
             bottom=None, cumulative=False, normed=False, align="mid", orientation="vertical")

    pad.hist(x=xData, bins=xBinning, weights=y9_sdETA_0_weights+y9_sdETA_1_weights+y9_sdETA_2_weights+y9_sdETA_3_weights+y9_sdETA_4_weights+y9_sdETA_5_weights,\
             label="$bg\_vbf\_600\_800$", histtype="step", rwidth=1.0,\
             color=None, edgecolor="#afcec6", linewidth=1, linestyle="solid",\
             bottom=None, cumulative=False, normed=False, align="mid", orientation="vertical")

    pad.hist(x=xData, bins=xBinning, weights=y9_sdETA_0_weights+y9_sdETA_1_weights+y9_sdETA_2_weights+y9_sdETA_3_weights+y9_sdETA_4_weights,\
             label="$bg\_vbf\_400\_600$", histtype="step", rwidth=1.0,\
             color=None, edgecolor="#84c1a3", linewidth=1, linestyle="solid",\
             bottom=None, cumulative=False, normed=False, align="mid", orientation="vertical")

    pad.hist(x=xData, bins=xBinning, weights=y9_sdETA_0_weights+y9_sdETA_1_weights+y9_sdETA_2_weights+y9_sdETA_3_weights,\
             label="$bg\_vbf\_200\_400$", histtype="step", rwidth=1.0,\
             color=None, edgecolor="#89a8a0", linewidth=1, linestyle="solid",\
             bottom=None, cumulative=False, normed=False, align="mid", orientation="vertical")

    pad.hist(x=xData, bins=xBinning, weights=y9_sdETA_0_weights+y9_sdETA_1_weights+y9_sdETA_2_weights,\
             label="$bg\_vbf\_100\_200$", histtype="step", rwidth=1.0,\
             color=None, edgecolor="#829e8c", linewidth=1, linestyle="solid",\
             bottom=None, cumulative=False, normed=False, align="mid", orientation="vertical")

    pad.hist(x=xData, bins=xBinning, weights=y9_sdETA_0_weights+y9_sdETA_1_weights,\
             label="$bg\_vbf\_0\_100$", histtype="step", rwidth=1.0,\
             color=None, edgecolor="#adbcc6", linewidth=1, linestyle="solid",\
             bottom=None, cumulative=False, normed=False, align="mid", orientation="vertical")

    pad.hist(x=xData, bins=xBinning, weights=y9_sdETA_0_weights,\
             label="$signal$", histtype="step", rwidth=1.0,\
             color=None, edgecolor="#7a8e99", linewidth=1, linestyle="solid",\
             bottom=None, cumulative=False, normed=False, align="mid", orientation="vertical")


    # Axis
    plt.rc('text',usetex=False)
    plt.xlabel(r"\Delta\eta ( j_{1} , j_{2} ) ",\
               fontsize=16,color="black")
    plt.ylabel(r"$\mathrm{Events}$ $(\mathcal{L}_{\mathrm{int}} = 40.0\ \mathrm{fb}^{-1})$ ",\
               fontsize=16,color="black")

    # Boundary of y-axis
    ymax=(y9_sdETA_0_weights+y9_sdETA_1_weights+y9_sdETA_2_weights+y9_sdETA_3_weights+y9_sdETA_4_weights+y9_sdETA_5_weights+y9_sdETA_6_weights+y9_sdETA_7_weights+y9_sdETA_8_weights+y9_sdETA_9_weights+y9_sdETA_10_weights+y9_sdETA_11_weights+y9_sdETA_12_weights+y9_sdETA_13_weights+y9_sdETA_14_weights+y9_sdETA_15_weights+y9_sdETA_16_weights).max()*1.1
    ymin=0 # linear scale
    #ymin=min([x for x in (y9_sdETA_0_weights+y9_sdETA_1_weights+y9_sdETA_2_weights+y9_sdETA_3_weights+y9_sdETA_4_weights+y9_sdETA_5_weights+y9_sdETA_6_weights+y9_sdETA_7_weights+y9_sdETA_8_weights+y9_sdETA_9_weights+y9_sdETA_10_weights+y9_sdETA_11_weights+y9_sdETA_12_weights+y9_sdETA_13_weights+y9_sdETA_14_weights+y9_sdETA_15_weights+y9_sdETA_16_weights) if x])/100. # log scale
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
