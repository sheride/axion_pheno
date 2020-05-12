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
    xBinning = numpy.linspace(-8.0,8.0,101,endpoint=True)

    # Creating data sequence: middle of each bin
    xData = numpy.array([-7.92,-7.76,-7.6,-7.44,-7.28,-7.12,-6.96,-6.8,-6.64,-6.48,-6.32,-6.16,-6.0,-5.84,-5.68,-5.52,-5.36,-5.2,-5.04,-4.88,-4.72,-4.56,-4.4,-4.24,-4.08,-3.92,-3.76,-3.6,-3.44,-3.28,-3.12,-2.96,-2.8,-2.64,-2.48,-2.32,-2.16,-2.0,-1.84,-1.68,-1.52,-1.36,-1.2,-1.04,-0.88,-0.72,-0.56,-0.4,-0.24,-0.08,0.08,0.24,0.4,0.56,0.72,0.88,1.04,1.2,1.36,1.52,1.68,1.84,2.0,2.16,2.32,2.48,2.64,2.8,2.96,3.12,3.28,3.44,3.6,3.76,3.92,4.08,4.24,4.4,4.56,4.72,4.88,5.04,5.2,5.36,5.52,5.68,5.84,6.0,6.16,6.32,6.48,6.64,6.8,6.96,7.12,7.28,7.44,7.6,7.76,7.92])

    # Creating weights for histo: y10_sdETA_0
    y10_sdETA_0_weights = numpy.array([0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,22.0916763836,40.3922441335,35.6758483214,32.044395546,28.1713909851,26.0547488645,22.4519560637,21.2728611106,18.52572755,17.5881843825,15.2095224946,13.956731607,12.6343407813,11.2628259991,10.5054186717,9.61700346053,8.33146060203,7.74600512189,7.04182574717,6.37039434337,5.50654311043,5.17082740854,4.28241219741,3.84434458639,3.34486662991,3.00505773164,2.69800120429,2.223087626])

    # Creating weights for histo: y10_sdETA_1
    y10_sdETA_1_weights = numpy.array([0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.644172887547,3.91333399002,6.9501295767,9.79327628555,10.9726153107,11.2996491787,10.2795353412,9.71984596919,8.17677994739,7.24148367272])

    # Creating weights for histo: y10_sdETA_2
    y10_sdETA_2_weights = numpy.array([0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.662754313473,7.36933241212,16.8768826742,24.8597028633,32.9320903091,39.4572897542,43.3812785466,44.2076145873,46.6465827242,45.3603446867,40.7429534308,31.5163855208,26.9170101922,20.5415536803,15.2095540575,11.2955236103,8.47409717118,6.38575782077,4.66903829144])

    # Creating weights for histo: y10_sdETA_3
    y10_sdETA_3_weights = numpy.array([0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.291536785339,3.87227105074,9.25193869613,16.07136371,22.088969664,29.3777396914,35.9494636392,41.7948220452,49.719980523,54.12860612,52.8306252335,48.3158048935,41.7136525362,36.4626596877,31.072447725,25.5384666055,20.1650532373,16.4516294531,12.2380706799,8.69660600359,5.7975098336,4.13088206259,2.85468044219,1.94141662163,1.16046072568,0.885411060131,0.467632653767,0.225502546022])

    # Creating weights for histo: y10_sdETA_4
    y10_sdETA_4_weights = numpy.array([0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,8.31910091163,16.8698974436,16.2683722595,15.1756422594,13.8751782406,12.4412739946,11.0253589871,9.29903742411,7.98161429922,6.63260178287,5.23729343206,4.0716765529,3.02466879994,2.21946679571,1.61352246379,1.01049657318,0.690820429241,0.44799456883,0.243754582908,0.157864226021,0.0829021712088,0.0503376010896,0.0128240062676,0.00789518338335,0.00394714757233,0.00197022806036,0.0,0.0])

    # Creating weights for histo: y10_sdETA_5
    y10_sdETA_5_weights = numpy.array([0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,2.16209978871,3.98233789334,3.52678664624,3.09273748778,2.60421733167,2.1920335512,1.74889135623,1.37509581771,1.03652574322,0.745142874876,0.519015656767,0.346860033477,0.227361921796,0.130339018103,0.0710893650958,0.039070297706,0.0199094089058,0.0115970283979,0.00630153392135,0.00226916572258,0.00126035879706,0.000504370454642,0.000755979140157,0.000252122091792,0.0,0.0,0.0,0.0])

    # Creating weights for histo: y10_sdETA_6
    y10_sdETA_6_weights = numpy.array([0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.757801323999,1.31918122267,1.05552731652,0.842588672683,0.648478466347,0.485541326017,0.34591900715,0.225023660071,0.14975779389,0.0979009673338,0.0512255698704,0.0271876227665,0.0145912093428,0.00859080699702,0.00515475610633,0.0017188171778,0.000569216350578,0.000569993487968,0.0,0.000286301353131,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0])

    # Creating weights for histo: y10_sdETA_7
    y10_sdETA_7_weights = numpy.array([0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0643296314281,0.0984671238263,0.0671363000682,0.0435057945916,0.0284634596304,0.0167314489324,0.00867745989312,0.00472931544587,0.00192257220931,0.0011215757503,0.000604806247598,0.000431904781183,0.000151239383951,0.000172771593242,8.64014073849e-05,8.63438675766e-05,2.16172449975e-05,0.0,2.15976152479e-05,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0])

    # Creating weights for histo: y10_sdETA_8
    y10_sdETA_8_weights = numpy.array([0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.00700371696988,0.00830171500248,0.00510904270934,0.0022068977061,0.00130513661909,0.000568267949524,0.000424047729026,5.67887549836e-05,0.000113580452121,5.68589357542e-05,2.82370391286e-05,2.81631435173e-05,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0])

    # Creating weights for histo: y10_sdETA_9
    y10_sdETA_9_weights = numpy.array([0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,5.21372681349,7.82912472841,10.4207614034,13.0433553817,39.0918935478,13.0232248654,10.419107578,10.4330112495,2.60449843645])

    # Creating weights for histo: y10_sdETA_10
    y10_sdETA_10_weights = numpy.array([0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,1.05238923318,18.9496204359,29.4832167291,42.1437813166,48.4376198867,49.5090957578,55.8105143453,47.3996192197,62.1406369585,53.7138507302,31.5995345216,16.8601289794,15.8029089279,8.42471615248,6.31932205018,2.10407895003,0.0,3.16002078734,3.16190540285])

    # Creating weights for histo: y10_sdETA_11
    y10_sdETA_11_weights = numpy.array([0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,1.38083353168,18.4267088703,38.9315845919,50.9075336514,58.0450651134,74.6179739024,84.9993557978,80.6222979425,87.7417700159,83.6169672374,69.3334125583,58.5089224306,34.5514105315,26.0264607773,14.2829053096,13.1221861382,7.37202685925,3.68731293712,2.99227700234,2.76534925743,0.921450331968,1.15181819829,0.0,0.0,0.230097590283,0.0,0.0,0.0])

    # Creating weights for histo: y10_sdETA_12
    y10_sdETA_12_weights = numpy.array([0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,38.9332171624,66.2363747776,50.4255861855,38.2401902466,29.4073104259,21.2418660887,16.1732351404,10.6886818605,7.30950864128,5.3158506487,3.57220425408,2.13253113937,1.32894015618,0.91361644556,0.553595158676,0.276956775591,0.0276984205974,0.110836216797,0.0,0.0553508597156,0.0,0.0276411938149,0.0276861634863,0.0,0.0,0.0,0.0,0.0])

    # Creating weights for histo: y10_sdETA_13
    y10_sdETA_13_weights = numpy.array([0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,6.58325110175,11.5135187288,8.60097393345,5.82747972258,4.315238553,2.66117803224,1.9756767757,1.28039351422,0.695775365328,0.413384883469,0.221796176542,0.241899437587,0.0907137908915,0.0705727877277,0.0100433721581,0.0201712818095,0.0301952307321,0.0100789116426,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0])

    # Creating weights for histo: y10_sdETA_14
    y10_sdETA_14_weights = numpy.array([0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,2.02278221684,3.01301154384,2.13027547918,1.36376377765,0.96195193315,0.568683825104,0.345169568796,0.223509524107,0.10469137693,0.0594176915783,0.0537829883174,0.019797565187,0.00283431906706,0.00849898830914,0.00565621745651,0.00282576609704,0.0,0.00282698954379,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0])

    # Creating weights for histo: y10_sdETA_15
    y10_sdETA_15_weights = numpy.array([0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.18409652559,0.202787789776,0.143069319471,0.0701257270632,0.0381396853571,0.0106563416458,0.010669139381,0.00762451102707,0.00151715620158,0.00305892697777,0.0,0.00152248849276,0.0,0.00152632580425,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0])

    # Creating weights for histo: y10_sdETA_16
    y10_sdETA_16_weights = numpy.array([0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0139029420888,0.0166115524095,0.0066803034538,0.00307040062161,0.000902981664435,0.000902687814978,0.000541096237976,0.000722822678131,0.000180820513449,0.000180182440343,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0])

    # Creating a new Canvas
    fig   = plt.figure(figsize=(12,6),dpi=80)
    frame = gridspec.GridSpec(1,1,right=0.7)
    pad   = fig.add_subplot(frame[0])

    # Creating a new Stack
    pad.hist(x=xData, bins=xBinning, weights=y10_sdETA_0_weights+y10_sdETA_1_weights+y10_sdETA_2_weights+y10_sdETA_3_weights+y10_sdETA_4_weights+y10_sdETA_5_weights+y10_sdETA_6_weights+y10_sdETA_7_weights+y10_sdETA_8_weights+y10_sdETA_9_weights+y10_sdETA_10_weights+y10_sdETA_11_weights+y10_sdETA_12_weights+y10_sdETA_13_weights+y10_sdETA_14_weights+y10_sdETA_15_weights+y10_sdETA_16_weights,\
             label="$bg\_dip\_1600\_inf$", histtype="step", rwidth=1.0,\
             color=None, edgecolor="#e5e5e5", linewidth=4, linestyle="dashdot",\
             bottom=None, cumulative=False, normed=False, align="mid", orientation="vertical")

    pad.hist(x=xData, bins=xBinning, weights=y10_sdETA_0_weights+y10_sdETA_1_weights+y10_sdETA_2_weights+y10_sdETA_3_weights+y10_sdETA_4_weights+y10_sdETA_5_weights+y10_sdETA_6_weights+y10_sdETA_7_weights+y10_sdETA_8_weights+y10_sdETA_9_weights+y10_sdETA_10_weights+y10_sdETA_11_weights+y10_sdETA_12_weights+y10_sdETA_13_weights+y10_sdETA_14_weights+y10_sdETA_15_weights,\
             label="$bg\_dip\_1200\_1600$", histtype="step", rwidth=1.0,\
             color=None, edgecolor="#f2f2f2", linewidth=4, linestyle="dashdot",\
             bottom=None, cumulative=False, normed=False, align="mid", orientation="vertical")

    pad.hist(x=xData, bins=xBinning, weights=y10_sdETA_0_weights+y10_sdETA_1_weights+y10_sdETA_2_weights+y10_sdETA_3_weights+y10_sdETA_4_weights+y10_sdETA_5_weights+y10_sdETA_6_weights+y10_sdETA_7_weights+y10_sdETA_8_weights+y10_sdETA_9_weights+y10_sdETA_10_weights+y10_sdETA_11_weights+y10_sdETA_12_weights+y10_sdETA_13_weights+y10_sdETA_14_weights,\
             label="$bg\_dip\_800\_1200$", histtype="step", rwidth=1.0,\
             color=None, edgecolor="#ccc6aa", linewidth=4, linestyle="dashdot",\
             bottom=None, cumulative=False, normed=False, align="mid", orientation="vertical")

    pad.hist(x=xData, bins=xBinning, weights=y10_sdETA_0_weights+y10_sdETA_1_weights+y10_sdETA_2_weights+y10_sdETA_3_weights+y10_sdETA_4_weights+y10_sdETA_5_weights+y10_sdETA_6_weights+y10_sdETA_7_weights+y10_sdETA_8_weights+y10_sdETA_9_weights+y10_sdETA_10_weights+y10_sdETA_11_weights+y10_sdETA_12_weights+y10_sdETA_13_weights,\
             label="$bg\_dip\_600\_800$", histtype="step", rwidth=1.0,\
             color=None, edgecolor="#ccc6aa", linewidth=4, linestyle="dashdot",\
             bottom=None, cumulative=False, normed=False, align="mid", orientation="vertical")

    pad.hist(x=xData, bins=xBinning, weights=y10_sdETA_0_weights+y10_sdETA_1_weights+y10_sdETA_2_weights+y10_sdETA_3_weights+y10_sdETA_4_weights+y10_sdETA_5_weights+y10_sdETA_6_weights+y10_sdETA_7_weights+y10_sdETA_8_weights+y10_sdETA_9_weights+y10_sdETA_10_weights+y10_sdETA_11_weights+y10_sdETA_12_weights,\
             label="$bg\_dip\_400\_600$", histtype="step", rwidth=1.0,\
             color=None, edgecolor="#c1bfa8", linewidth=4, linestyle="dashdot",\
             bottom=None, cumulative=False, normed=False, align="mid", orientation="vertical")

    pad.hist(x=xData, bins=xBinning, weights=y10_sdETA_0_weights+y10_sdETA_1_weights+y10_sdETA_2_weights+y10_sdETA_3_weights+y10_sdETA_4_weights+y10_sdETA_5_weights+y10_sdETA_6_weights+y10_sdETA_7_weights+y10_sdETA_8_weights+y10_sdETA_9_weights+y10_sdETA_10_weights+y10_sdETA_11_weights,\
             label="$bg\_dip\_200\_400$", histtype="step", rwidth=1.0,\
             color=None, edgecolor="#bab5a3", linewidth=4, linestyle="dashdot",\
             bottom=None, cumulative=False, normed=False, align="mid", orientation="vertical")

    pad.hist(x=xData, bins=xBinning, weights=y10_sdETA_0_weights+y10_sdETA_1_weights+y10_sdETA_2_weights+y10_sdETA_3_weights+y10_sdETA_4_weights+y10_sdETA_5_weights+y10_sdETA_6_weights+y10_sdETA_7_weights+y10_sdETA_8_weights+y10_sdETA_9_weights+y10_sdETA_10_weights,\
             label="$bg\_dip\_100\_200$", histtype="step", rwidth=1.0,\
             color=None, edgecolor="#b2a596", linewidth=4, linestyle="dashdot",\
             bottom=None, cumulative=False, normed=False, align="mid", orientation="vertical")

    pad.hist(x=xData, bins=xBinning, weights=y10_sdETA_0_weights+y10_sdETA_1_weights+y10_sdETA_2_weights+y10_sdETA_3_weights+y10_sdETA_4_weights+y10_sdETA_5_weights+y10_sdETA_6_weights+y10_sdETA_7_weights+y10_sdETA_8_weights+y10_sdETA_9_weights,\
             label="$bg\_dip\_0\_100$", histtype="step", rwidth=1.0,\
             color=None, edgecolor="#b7a39b", linewidth=4, linestyle="dashdot",\
             bottom=None, cumulative=False, normed=False, align="mid", orientation="vertical")

    pad.hist(x=xData, bins=xBinning, weights=y10_sdETA_0_weights+y10_sdETA_1_weights+y10_sdETA_2_weights+y10_sdETA_3_weights+y10_sdETA_4_weights+y10_sdETA_5_weights+y10_sdETA_6_weights+y10_sdETA_7_weights+y10_sdETA_8_weights,\
             label="$bg\_vbf\_1600\_inf$", histtype="step", rwidth=1.0,\
             color=None, edgecolor="#ad998c", linewidth=4, linestyle="dashdot",\
             bottom=None, cumulative=False, normed=False, align="mid", orientation="vertical")

    pad.hist(x=xData, bins=xBinning, weights=y10_sdETA_0_weights+y10_sdETA_1_weights+y10_sdETA_2_weights+y10_sdETA_3_weights+y10_sdETA_4_weights+y10_sdETA_5_weights+y10_sdETA_6_weights+y10_sdETA_7_weights,\
             label="$bg\_vbf\_1200\_1600$", histtype="step", rwidth=1.0,\
             color=None, edgecolor="#9b8e82", linewidth=4, linestyle="dashdot",\
             bottom=None, cumulative=False, normed=False, align="mid", orientation="vertical")

    pad.hist(x=xData, bins=xBinning, weights=y10_sdETA_0_weights+y10_sdETA_1_weights+y10_sdETA_2_weights+y10_sdETA_3_weights+y10_sdETA_4_weights+y10_sdETA_5_weights+y10_sdETA_6_weights,\
             label="$bg\_vbf\_800\_1200$", histtype="step", rwidth=1.0,\
             color=None, edgecolor="#876656", linewidth=4, linestyle="dashdot",\
             bottom=None, cumulative=False, normed=False, align="mid", orientation="vertical")

    pad.hist(x=xData, bins=xBinning, weights=y10_sdETA_0_weights+y10_sdETA_1_weights+y10_sdETA_2_weights+y10_sdETA_3_weights+y10_sdETA_4_weights+y10_sdETA_5_weights,\
             label="$bg\_vbf\_600\_800$", histtype="step", rwidth=1.0,\
             color=None, edgecolor="#afcec6", linewidth=4, linestyle="dashdot",\
             bottom=None, cumulative=False, normed=False, align="mid", orientation="vertical")

    pad.hist(x=xData, bins=xBinning, weights=y10_sdETA_0_weights+y10_sdETA_1_weights+y10_sdETA_2_weights+y10_sdETA_3_weights+y10_sdETA_4_weights,\
             label="$bg\_vbf\_400\_600$", histtype="step", rwidth=1.0,\
             color=None, edgecolor="#84c1a3", linewidth=4, linestyle="dashdot",\
             bottom=None, cumulative=False, normed=False, align="mid", orientation="vertical")

    pad.hist(x=xData, bins=xBinning, weights=y10_sdETA_0_weights+y10_sdETA_1_weights+y10_sdETA_2_weights+y10_sdETA_3_weights,\
             label="$bg\_vbf\_200\_400$", histtype="step", rwidth=1.0,\
             color=None, edgecolor="#89a8a0", linewidth=4, linestyle="dashdot",\
             bottom=None, cumulative=False, normed=False, align="mid", orientation="vertical")

    pad.hist(x=xData, bins=xBinning, weights=y10_sdETA_0_weights+y10_sdETA_1_weights+y10_sdETA_2_weights,\
             label="$bg\_vbf\_100\_200$", histtype="step", rwidth=1.0,\
             color=None, edgecolor="#829e8c", linewidth=4, linestyle="dashdot",\
             bottom=None, cumulative=False, normed=False, align="mid", orientation="vertical")

    pad.hist(x=xData, bins=xBinning, weights=y10_sdETA_0_weights+y10_sdETA_1_weights,\
             label="$bg\_vbf\_0\_100$", histtype="step", rwidth=1.0,\
             color=None, edgecolor="#adbcc6", linewidth=4, linestyle="dashdot",\
             bottom=None, cumulative=False, normed=False, align="mid", orientation="vertical")

    pad.hist(x=xData, bins=xBinning, weights=y10_sdETA_0_weights,\
             label="$signal$", histtype="step", rwidth=1.0,\
             color=None, edgecolor="#7a8e99", linewidth=3, linestyle="dashed",\
             bottom=None, cumulative=False, normed=False, align="mid", orientation="vertical")


    # Axis
    plt.rc('text',usetex=False)
    plt.xlabel(r"\Delta\eta ( j_{1} , j_{2} ) ",\
               fontsize=16,color="black")
    plt.ylabel(r"$\mathrm{Events}$ $(\mathcal{L}_{\mathrm{int}} = 40.0\ \mathrm{fb}^{-1})$ ",\
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
