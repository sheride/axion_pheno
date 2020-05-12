def selection_9():

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

    # Creating weights for histo: y10_sdETA_0
    y10_sdETA_0_weights = numpy.array([0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.307056318563,3.37761890419,13.2034198982,32.5479601677,54.9630696228,80.4487362635,124.357806018,171.03035324,255.777875563,349.430079725,461.198577281,621.481830371,782.993582335,976.43910503,1207.03809367,1539.88718859,1927.0851337,2392.27550732,3019.89923207,3726.43458448,4852.41155245,6235.08628514,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,6171.52534339,4825.69657693,3784.77553101,2989.80685965,2407.01419381,1903.74905509,1512.25211392,1241.42856215,967.84141291,765.184398659,615.033636281,456.285481785,333.155994641,251.786139222,174.407960144,127.121313485,73.079393018,52.8136915928,25.7927283593,12.2822497425,5.83407065269,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0])

    # Creating weights for histo: y10_sdETA_1
    y10_sdETA_1_weights = numpy.array([0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.912787033803,0.0,0.0,0.909853848219,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.913150150035,0.909306167943,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0])

    # Creating weights for histo: y10_sdETA_2
    y10_sdETA_2_weights = numpy.array([0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,2.26105321989,0.752556980442,0.753429976476,2.26069125348,2.25675269949,1.50582797681,5.26915861775,7.5305003571,7.52955825275,6.02496182945,3.76333188055,0.75399368957,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,4.51711452635,3.76316453307,4.5227299641,6.02241132986,1.50979907059,4.51771883671,8.27669968272,4.51891506131,3.01357394171,4.51641104712,1.50837971601,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0])

    # Creating weights for histo: y10_sdETA_3
    y10_sdETA_3_weights = numpy.array([0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,1.65039283597,1.65067711481,5.77395307128,10.3141786378,11.5495636741,14.4331169806,21.438558061,22.2834755998,24.3491010991,35.0759563282,28.873869575,28.047577937,22.2713945109,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,23.0925368323,24.3423125326,31.768937241,34.2330528121,24.7546448205,25.1667760109,17.736044037,18.5674118652,11.9675358348,6.18775093393,4.53708722563,1.64777521592,1.2401102198,0.413566295747,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0])

    # Creating weights for histo: y10_sdETA_4
    y10_sdETA_4_weights = numpy.array([0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.147855284955,0.444278598868,0.740691601456,1.77682489677,3.18393559901,5.54923019181,9.32757607239,14.2861387229,19.6131313119,24.4250296505,28.5694516017,30.1232870408,31.8226113611,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,29.3840853206,29.7516675059,27.1639008255,21.4619337633,19.3200491979,13.3965750437,10.0656354302,5.92084371427,3.33125827249,2.14584946509,0.517882216239,0.221829538827,0.0741328919474,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0])

    # Creating weights for histo: y10_sdETA_5
    y10_sdETA_5_weights = numpy.array([0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0567772497497,0.113390113378,0.321535711897,0.775470970568,1.70175765486,3.38449357286,5.70978597019,7.92184759884,11.4197039774,14.4819401359,15.5218248919,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,16.0321990854,14.1776637664,11.0781871595,7.86504766273,5.10430009161,3.61102112873,1.9279287107,0.983303281189,0.623777810668,0.0945011937951,0.0189061774252,0.0567219742413,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0])

    # Creating weights for histo: y10_sdETA_6
    y10_sdETA_6_weights = numpy.array([0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0215117332104,0.150098394939,0.300690596999,0.70951947984,1.35256664304,2.53278590376,4.66006738776,6.29070907147,8.4615641977,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,7.30057237365,5.92732596417,3.6281282231,2.44834983482,1.8037478465,0.664919609542,0.214795600195,0.171930727886,0.0429410802588,0.0213876591105,0.0214736442312,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0])

    # Creating weights for histo: y10_sdETA_7
    y10_sdETA_7_weights = numpy.array([0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.00323996109069,0.00647096401566,0.0161993685464,0.0388932752288,0.0891193530403,0.158760039095,0.306063307166,0.566782202494,0.986218923526,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.869891955272,0.508481516987,0.29797530937,0.17156465259,0.0436434919076,0.0307854563125,0.0113372942383,0.00323802486961,0.00648040623665,0.00161987744786,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0])

    # Creating weights for histo: y10_sdETA_8
    y10_sdETA_8_weights = numpy.array([0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.00426733658047,0.0,0.0149114363569,0.017044354055,0.0211746040092,0.0255421702485,0.1170248809,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.138174093959,0.0509945924002,0.0255507786712,0.0126826455523,0.00638607209705,0.00211623094442,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0])

    # Creating weights for histo: y10_sdETA_9
    y10_sdETA_9_weights = numpy.array([0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0])

    # Creating weights for histo: y10_sdETA_10
    y10_sdETA_10_weights = numpy.array([0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,79.0971291539,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,78.97186254,0.0,0.0,78.9085371523,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0])

    # Creating weights for histo: y10_sdETA_11
    y10_sdETA_11_weights = numpy.array([0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,17.277013831,0.0,0.0,17.2515136777,86.4516295122,69.0779785157,155.515082624,103.661350952,155.296826904,138.306110511,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,69.1552167739,190.081018812,207.198313724,69.0083488024,17.300487921,69.1164247233,34.5313230725,0.0,17.3128921547,17.2964761428,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0])

    # Creating weights for histo: y10_sdETA_12
    y10_sdETA_12_weights = numpy.array([0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,2.07175710266,10.3819482674,4.14967151363,10.3717033973,39.4781208602,53.9776558199,68.5775622331,118.354792455,132.904469865,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,147.467735937,134.97312004,89.3279970489,43.6314910288,22.832650572,22.8452294607,12.4627416859,6.22610559713,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0])

    # Creating weights for histo: y10_sdETA_13
    y10_sdETA_13_weights = numpy.array([0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.755342844597,0.0,1.51218636673,1.51466564805,5.29049138983,9.8324783273,8.32125918525,27.9711453415,31.7654471228,52.1571240543,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,42.3657334311,39.3202274075,21.1702085894,10.5862399302,7.55825774188,5.2932178255,1.51372573324,1.50934067794,1.50786230347,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0])

    # Creating weights for histo: y10_sdETA_14
    y10_sdETA_14_weights = numpy.array([0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.212398560568,0.0,0.212401128738,0.849295699773,0.635774618252,2.33408063356,4.45657641233,9.1190334574,13.7943977188,24.6144337696,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,21.6436906236,15.2794403352,7.84849648369,5.09291112239,2.54672853742,1.0621421318,0.212327200081,0.42354656683,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0])

    # Creating weights for histo: y10_sdETA_15
    y10_sdETA_15_weights = numpy.array([0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.22907142471,0.227593673225,0.683011488985,0.79927385968,1.82897164435,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,1.82671481796,1.37252629004,0.34459434349,0.341431684066,0.115366111007,0.0,0.114195504197,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0])

    # Creating weights for histo: y10_sdETA_16
    y10_sdETA_16_weights = numpy.array([0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0135301539511,0.0270154986104,0.0,0.0406551854233,0.0677772948643,0.189559357965,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.216668272067,0.0812149139754,0.0406658398654,0.0406293722222,0.0135566283628,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0])

    # Creating a new Canvas
    fig   = plt.figure(figsize=(12,6),dpi=80)
    frame = gridspec.GridSpec(1,1,right=0.7)
    pad   = fig.add_subplot(frame[0])

    # Creating a new Stack
    pad.hist(x=xData, bins=xBinning, weights=y10_sdETA_0_weights+y10_sdETA_1_weights+y10_sdETA_2_weights+y10_sdETA_3_weights+y10_sdETA_4_weights+y10_sdETA_5_weights+y10_sdETA_6_weights+y10_sdETA_7_weights+y10_sdETA_8_weights+y10_sdETA_9_weights+y10_sdETA_10_weights+y10_sdETA_11_weights+y10_sdETA_12_weights+y10_sdETA_13_weights+y10_sdETA_14_weights+y10_sdETA_15_weights+y10_sdETA_16_weights,\
             label="$bg\_dip\_1600\_inf$", histtype="step", rwidth=1.0,\
             color=None, edgecolor="#e5e5e5", linewidth=1, linestyle="solid",\
             bottom=None, cumulative=False, normed=False, align="mid", orientation="vertical")

    pad.hist(x=xData, bins=xBinning, weights=y10_sdETA_0_weights+y10_sdETA_1_weights+y10_sdETA_2_weights+y10_sdETA_3_weights+y10_sdETA_4_weights+y10_sdETA_5_weights+y10_sdETA_6_weights+y10_sdETA_7_weights+y10_sdETA_8_weights+y10_sdETA_9_weights+y10_sdETA_10_weights+y10_sdETA_11_weights+y10_sdETA_12_weights+y10_sdETA_13_weights+y10_sdETA_14_weights+y10_sdETA_15_weights,\
             label="$bg\_dip\_1200\_1600$", histtype="step", rwidth=1.0,\
             color=None, edgecolor="#f2f2f2", linewidth=1, linestyle="solid",\
             bottom=None, cumulative=False, normed=False, align="mid", orientation="vertical")

    pad.hist(x=xData, bins=xBinning, weights=y10_sdETA_0_weights+y10_sdETA_1_weights+y10_sdETA_2_weights+y10_sdETA_3_weights+y10_sdETA_4_weights+y10_sdETA_5_weights+y10_sdETA_6_weights+y10_sdETA_7_weights+y10_sdETA_8_weights+y10_sdETA_9_weights+y10_sdETA_10_weights+y10_sdETA_11_weights+y10_sdETA_12_weights+y10_sdETA_13_weights+y10_sdETA_14_weights,\
             label="$bg\_dip\_800\_1200$", histtype="step", rwidth=1.0,\
             color=None, edgecolor="#ccc6aa", linewidth=1, linestyle="solid",\
             bottom=None, cumulative=False, normed=False, align="mid", orientation="vertical")

    pad.hist(x=xData, bins=xBinning, weights=y10_sdETA_0_weights+y10_sdETA_1_weights+y10_sdETA_2_weights+y10_sdETA_3_weights+y10_sdETA_4_weights+y10_sdETA_5_weights+y10_sdETA_6_weights+y10_sdETA_7_weights+y10_sdETA_8_weights+y10_sdETA_9_weights+y10_sdETA_10_weights+y10_sdETA_11_weights+y10_sdETA_12_weights+y10_sdETA_13_weights,\
             label="$bg\_dip\_600\_800$", histtype="step", rwidth=1.0,\
             color=None, edgecolor="#ccc6aa", linewidth=1, linestyle="solid",\
             bottom=None, cumulative=False, normed=False, align="mid", orientation="vertical")

    pad.hist(x=xData, bins=xBinning, weights=y10_sdETA_0_weights+y10_sdETA_1_weights+y10_sdETA_2_weights+y10_sdETA_3_weights+y10_sdETA_4_weights+y10_sdETA_5_weights+y10_sdETA_6_weights+y10_sdETA_7_weights+y10_sdETA_8_weights+y10_sdETA_9_weights+y10_sdETA_10_weights+y10_sdETA_11_weights+y10_sdETA_12_weights,\
             label="$bg\_dip\_400\_600$", histtype="step", rwidth=1.0,\
             color=None, edgecolor="#c1bfa8", linewidth=1, linestyle="solid",\
             bottom=None, cumulative=False, normed=False, align="mid", orientation="vertical")

    pad.hist(x=xData, bins=xBinning, weights=y10_sdETA_0_weights+y10_sdETA_1_weights+y10_sdETA_2_weights+y10_sdETA_3_weights+y10_sdETA_4_weights+y10_sdETA_5_weights+y10_sdETA_6_weights+y10_sdETA_7_weights+y10_sdETA_8_weights+y10_sdETA_9_weights+y10_sdETA_10_weights+y10_sdETA_11_weights,\
             label="$bg\_dip\_200\_400$", histtype="step", rwidth=1.0,\
             color=None, edgecolor="#bab5a3", linewidth=1, linestyle="solid",\
             bottom=None, cumulative=False, normed=False, align="mid", orientation="vertical")

    pad.hist(x=xData, bins=xBinning, weights=y10_sdETA_0_weights+y10_sdETA_1_weights+y10_sdETA_2_weights+y10_sdETA_3_weights+y10_sdETA_4_weights+y10_sdETA_5_weights+y10_sdETA_6_weights+y10_sdETA_7_weights+y10_sdETA_8_weights+y10_sdETA_9_weights+y10_sdETA_10_weights,\
             label="$bg\_dip\_100\_200$", histtype="step", rwidth=1.0,\
             color=None, edgecolor="#b2a596", linewidth=1, linestyle="solid",\
             bottom=None, cumulative=False, normed=False, align="mid", orientation="vertical")

    pad.hist(x=xData, bins=xBinning, weights=y10_sdETA_0_weights+y10_sdETA_1_weights+y10_sdETA_2_weights+y10_sdETA_3_weights+y10_sdETA_4_weights+y10_sdETA_5_weights+y10_sdETA_6_weights+y10_sdETA_7_weights+y10_sdETA_8_weights+y10_sdETA_9_weights,\
             label="$bg\_dip\_0\_100$", histtype="step", rwidth=1.0,\
             color=None, edgecolor="#b7a39b", linewidth=1, linestyle="solid",\
             bottom=None, cumulative=False, normed=False, align="mid", orientation="vertical")

    pad.hist(x=xData, bins=xBinning, weights=y10_sdETA_0_weights+y10_sdETA_1_weights+y10_sdETA_2_weights+y10_sdETA_3_weights+y10_sdETA_4_weights+y10_sdETA_5_weights+y10_sdETA_6_weights+y10_sdETA_7_weights+y10_sdETA_8_weights,\
             label="$bg\_vbf\_1600\_inf$", histtype="step", rwidth=1.0,\
             color=None, edgecolor="#ad998c", linewidth=1, linestyle="solid",\
             bottom=None, cumulative=False, normed=False, align="mid", orientation="vertical")

    pad.hist(x=xData, bins=xBinning, weights=y10_sdETA_0_weights+y10_sdETA_1_weights+y10_sdETA_2_weights+y10_sdETA_3_weights+y10_sdETA_4_weights+y10_sdETA_5_weights+y10_sdETA_6_weights+y10_sdETA_7_weights,\
             label="$bg\_vbf\_1200\_1600$", histtype="step", rwidth=1.0,\
             color=None, edgecolor="#9b8e82", linewidth=1, linestyle="solid",\
             bottom=None, cumulative=False, normed=False, align="mid", orientation="vertical")

    pad.hist(x=xData, bins=xBinning, weights=y10_sdETA_0_weights+y10_sdETA_1_weights+y10_sdETA_2_weights+y10_sdETA_3_weights+y10_sdETA_4_weights+y10_sdETA_5_weights+y10_sdETA_6_weights,\
             label="$bg\_vbf\_800\_1200$", histtype="step", rwidth=1.0,\
             color=None, edgecolor="#876656", linewidth=1, linestyle="solid",\
             bottom=None, cumulative=False, normed=False, align="mid", orientation="vertical")

    pad.hist(x=xData, bins=xBinning, weights=y10_sdETA_0_weights+y10_sdETA_1_weights+y10_sdETA_2_weights+y10_sdETA_3_weights+y10_sdETA_4_weights+y10_sdETA_5_weights,\
             label="$bg\_vbf\_600\_800$", histtype="step", rwidth=1.0,\
             color=None, edgecolor="#afcec6", linewidth=1, linestyle="solid",\
             bottom=None, cumulative=False, normed=False, align="mid", orientation="vertical")

    pad.hist(x=xData, bins=xBinning, weights=y10_sdETA_0_weights+y10_sdETA_1_weights+y10_sdETA_2_weights+y10_sdETA_3_weights+y10_sdETA_4_weights,\
             label="$bg\_vbf\_400\_600$", histtype="step", rwidth=1.0,\
             color=None, edgecolor="#84c1a3", linewidth=1, linestyle="solid",\
             bottom=None, cumulative=False, normed=False, align="mid", orientation="vertical")

    pad.hist(x=xData, bins=xBinning, weights=y10_sdETA_0_weights+y10_sdETA_1_weights+y10_sdETA_2_weights+y10_sdETA_3_weights,\
             label="$bg\_vbf\_200\_400$", histtype="step", rwidth=1.0,\
             color=None, edgecolor="#89a8a0", linewidth=1, linestyle="solid",\
             bottom=None, cumulative=False, normed=False, align="mid", orientation="vertical")

    pad.hist(x=xData, bins=xBinning, weights=y10_sdETA_0_weights+y10_sdETA_1_weights+y10_sdETA_2_weights,\
             label="$bg\_vbf\_100\_200$", histtype="step", rwidth=1.0,\
             color=None, edgecolor="#829e8c", linewidth=1, linestyle="solid",\
             bottom=None, cumulative=False, normed=False, align="mid", orientation="vertical")

    pad.hist(x=xData, bins=xBinning, weights=y10_sdETA_0_weights+y10_sdETA_1_weights,\
             label="$bg\_vbf\_0\_100$", histtype="step", rwidth=1.0,\
             color=None, edgecolor="#adbcc6", linewidth=1, linestyle="solid",\
             bottom=None, cumulative=False, normed=False, align="mid", orientation="vertical")

    pad.hist(x=xData, bins=xBinning, weights=y10_sdETA_0_weights,\
             label="$signal$", histtype="step", rwidth=1.0,\
             color=None, edgecolor="#7a8e99", linewidth=1, linestyle="solid",\
             bottom=None, cumulative=False, normed=False, align="mid", orientation="vertical")


    # Axis
    plt.rc('text',usetex=False)
    plt.xlabel(r"\Delta\eta ( j_{1} , j_{2} ) ",\
               fontsize=16,color="black")
    plt.ylabel(r"$\mathrm{Events}$ $(\mathcal{L}_{\mathrm{int}} = 3000.0\ \mathrm{fb}^{-1})$ ",\
               fontsize=16,color="black")

    # Boundary of y-axis
    ymax=(y10_sdETA_0_weights+y10_sdETA_1_weights+y10_sdETA_2_weights+y10_sdETA_3_weights+y10_sdETA_4_weights+y10_sdETA_5_weights+y10_sdETA_6_weights+y10_sdETA_7_weights+y10_sdETA_8_weights+y10_sdETA_9_weights+y10_sdETA_10_weights+y10_sdETA_11_weights+y10_sdETA_12_weights+y10_sdETA_13_weights+y10_sdETA_14_weights+y10_sdETA_15_weights+y10_sdETA_16_weights).max()*1.1
    ymin=0 # linear scale
    #ymin=min([x for x in (y10_sdETA_0_weights+y10_sdETA_1_weights+y10_sdETA_2_weights+y10_sdETA_3_weights+y10_sdETA_4_weights+y10_sdETA_5_weights+y10_sdETA_6_weights+y10_sdETA_7_weights+y10_sdETA_8_weights+y10_sdETA_9_weights+y10_sdETA_10_weights+y10_sdETA_11_weights+y10_sdETA_12_weights+y10_sdETA_13_weights+y10_sdETA_14_weights+y10_sdETA_15_weights+y10_sdETA_16_weights) if x])/100. # log scale
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
    plt.savefig('../../HTML/MadAnalysis5job_0/selection_9.png')
    plt.savefig('../../PDF/MadAnalysis5job_0/selection_9.png')
    plt.savefig('../../DVI/MadAnalysis5job_0/selection_9.eps')

# Running!
if __name__ == '__main__':
    selection_9()
