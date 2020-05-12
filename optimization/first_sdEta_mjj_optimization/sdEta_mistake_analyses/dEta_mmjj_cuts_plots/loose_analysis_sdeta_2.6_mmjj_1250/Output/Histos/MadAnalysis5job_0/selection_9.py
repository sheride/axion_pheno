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
    y10_sdETA_0_weights = numpy.array([0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,74.6515387976,90.1762860698,78.5408956089,68.3671039498,60.6497502768,52.379717057,45.4443227429,40.3922468848,35.6758507515,32.0443977287,28.1713929039,26.0547506392,22.451957593,21.2728625596,18.5257288118,17.5881855805,15.2095235306,13.9567325577,12.6343416418,11.2628267663,10.5054193872,9.61700411558,8.33146116953,7.74600564951,7.04182622682,6.37039477729,5.50654348551,5.17082776074,4.2824124891,3.84434484825,3.34486685774,3.00505793633,2.69800138807,2.22308777742])

    # Creating weights for histo: y10_sdETA_1
    y10_sdETA_1_weights = numpy.array([0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.644172887547,3.91333399002,6.9501295767,9.79327628555,10.9726153107,11.2996491787,10.2795353412,9.71984596919,8.17677994739,7.24148367272])

    # Creating weights for histo: y10_sdETA_2
    y10_sdETA_2_weights = numpy.array([0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.662754313473,7.36933241212,16.8768826742,24.8597028633,32.9320903091,39.4572897542,43.3812785466,44.2076145873,46.6465827242,45.3603446867,40.7429534308,31.5163855208,26.9170101922,20.5415536803,15.2095540575,11.2955236103,8.47409717118,6.38575782077,4.66903829144])

    # Creating weights for histo: y10_sdETA_3
    y10_sdETA_3_weights = numpy.array([0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.291536785339,3.87227105074,9.25193869613,16.07136371,22.088969664,29.3777396914,35.9494636392,41.7948220452,49.719980523,54.12860612,52.8306252335,48.3158048935,41.7136525362,36.4626596877,31.072447725,25.5384666055,20.1650532373,16.4516294531,12.2380706799,8.69660600359,5.7975098336,4.13088206259,2.85468044219,1.94141662163,1.16046072568,0.885411060131,0.467632653767,0.225502546022])

    # Creating weights for histo: y10_sdETA_4
    y10_sdETA_4_weights = numpy.array([0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.711500428681,2.93878262634,5.48485290477,8.69114784055,12.302012476,15.9150335767,16.8699067315,16.2683812162,15.1756506146,13.8751858798,12.4412808443,11.0253650572,9.29904254382,7.9816186936,6.63260543453,5.23729631552,4.07167879461,3.02467046521,2.21946801767,1.61352335214,1.01049712952,0.690820809581,0.447994815479,0.24375471711,0.157864312935,0.0829022168517,0.0503376288036,0.012824013328,0.00789518773014,0.00394714974548,0.0019702291451,0.0,0.0])

    # Creating weights for histo: y10_sdETA_5
    y10_sdETA_5_weights = numpy.array([0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,3.397718364,5.4106607767,5.48633552911,5.35253837381,5.15551355051,4.77815604028,4.41115709692,3.98234523616,3.52679314909,3.09274319031,2.60422213344,2.19203759298,1.74889458091,1.37509835317,1.03652765442,0.745144248805,0.519016613752,0.346860673034,0.227362341017,0.130339258429,0.0710894961737,0.0390703697456,0.0199094456157,0.011597049781,0.0063015455404,0.00226916990658,0.00126036112097,0.000504371384623,0.000755980534066,0.000252122556666,0.0,0.0,0.0,0.0])

    # Creating weights for histo: y10_sdETA_6
    y10_sdETA_6_weights = numpy.array([0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,2.09709540312,2.64875968168,2.44127640399,2.28410546192,2.02707759432,1.82321811635,1.56914027165,1.31919005979,1.05553438744,0.842594317139,0.648482810469,0.485544578633,0.345921324443,0.225025167492,0.14975879711,0.0979016231672,0.0512259130278,0.0271878048949,0.0145913070885,0.00859086454637,0.00515479063776,0.00171882869207,0.000569220163728,0.000569997306324,0.0,0.000286303271048,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0])

    # Creating weights for histo: y10_sdETA_7
    y10_sdETA_7_weights = numpy.array([0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.343094041166,0.407974670325,0.353066888414,0.298788161474,0.24195172468,0.187157055319,0.141744399295,0.0984693986295,0.0671378510617,0.0435067996694,0.0284641171978,0.0167318354649,0.00867766036118,0.00472942470326,0.00192261662488,0.00112160166112,0.000604820219928,0.000431914759116,0.000151242877908,0.000172775584639,8.64034034439e-05,8.63458623063e-05,2.16177444025e-05,0.0,2.15981141994e-05,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0])

    # Creating weights for histo: y10_sdETA_8
    y10_sdETA_8_weights = numpy.array([0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0861137746276,0.099158511999,0.0693098476982,0.052268949757,0.0358661180969,0.0258495037218,0.0157463197785,0.00829733889165,0.00510634956255,0.00220573437673,0.00130444863805,0.000567968396537,0.000423824199326,5.6758819737e-05,0.000113520580077,5.6828963513e-05,2.82221544436e-05,2.81482977852e-05,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0])

    # Creating weights for histo: y10_sdETA_9
    y10_sdETA_9_weights = numpy.array([0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,5.21372681349,7.82912472841,10.4207614034,13.0433553817,39.0918935478,13.0232248654,10.419107578,10.4330112495,2.60449843645])

    # Creating weights for histo: y10_sdETA_10
    y10_sdETA_10_weights = numpy.array([0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,1.05238923318,18.9496204359,29.4832167291,42.1437813166,48.4376198867,49.5090957578,55.8105143453,47.3996192197,62.1406369585,53.7138507302,31.5995345216,16.8601289794,15.8029089279,8.42471615248,6.31932205018,2.10407895003,0.0,3.16002078734,3.16190540285])

    # Creating weights for histo: y10_sdETA_11
    y10_sdETA_11_weights = numpy.array([0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,1.38083353168,18.4267088703,38.9315845919,50.9075336514,58.0450651134,74.6179739024,84.9993557978,80.6222979425,87.7417700159,83.6169672374,69.3334125583,58.5089224306,34.5514105315,26.0264607773,14.2829053096,13.1221861382,7.37202685925,3.68731293712,2.99227700234,2.76534925743,0.921450331968,1.15181819829,0.0,0.0,0.230097590283,0.0,0.0,0.0])

    # Creating weights for histo: y10_sdETA_12
    y10_sdETA_12_weights = numpy.array([0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,7.58690975991,24.8114915443,41.2340323528,57.0151696704,69.3658858992,77.3972600172,66.235772847,50.4251279373,38.2398427345,29.4070431837,21.2416730508,16.1730881643,10.6885847259,7.30944221529,5.3158023403,3.57217179126,2.13251175975,1.32892807929,0.913608142967,0.553590127817,0.276954258714,0.0276981688849,0.11083520956,0.0,0.0553503567084,0.0,0.0276409426225,0.0276859118851,0.0,0.0,0.0,0.0,0.0])

    # Creating weights for histo: y10_sdETA_13
    y10_sdETA_13_weights = numpy.array([0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,36.4855902643,51.9809279449,42.3249583353,33.0890646649,26.9181263618,20.4869867413,14.5579175142,11.5142860451,8.60154714376,5.82786809388,4.31552614127,2.66135538596,1.97580844431,1.2804788458,0.695821735148,0.413412433428,0.221810958107,0.24191555893,0.0907198364953,0.0705774910381,0.0100440414968,0.0201726261208,0.0301972430877,0.0100795833498,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0])

    # Creating weights for histo: y10_sdETA_14
    y10_sdETA_14_weights = numpy.array([0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,19.0290147395,20.0728940102,15.8938334889,12.2450575737,9.31646917292,6.64268900821,4.55787756109,3.01306228066,2.1303113514,1.36378674239,0.961968131689,0.568693401306,0.345175381189,0.223513287838,0.104693139853,0.059418692127,0.053783893982,0.0197978985629,0.00283436679483,0.00849913142563,0.0056563127029,0.00282581368079,0.0,0.00282703714814,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0])

    # Creating weights for histo: y10_sdETA_15
    y10_sdETA_15_weights = numpy.array([0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,2.57695534102,2.59577149536,1.88572367722,1.33013964917,0.875695552283,0.658086756846,0.379168845586,0.202744210739,0.143038573915,0.0701106570646,0.0381314891497,0.010654051601,0.010666846586,0.00762287252184,0.00151683016515,0.00305826961524,0.0,0.00152216131042,0.0,0.00152599779727,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0])

    # Creating weights for histo: y10_sdETA_16
    y10_sdETA_16_weights = numpy.array([0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.595848946221,0.568234190918,0.378809070398,0.224975218508,0.124585866095,0.0711461037443,0.0348501085007,0.016611918674,0.00668045074635,0.0030704683202,0.00090300157408,0.000902707718145,0.000541108168489,0.00072283861549,0.000180824500321,0.000180186413146,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0])

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
