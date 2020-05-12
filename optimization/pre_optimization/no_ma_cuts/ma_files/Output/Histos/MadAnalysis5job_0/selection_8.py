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
    y9_sdETA_0_weights = numpy.array([0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.00409408442626,0.0777876120989,0.331620790527,0.695994192464,1.16681378148,1.92831351677,2.95183462333,4.15140037622,5.98145477876,8.3724006917,10.8575105224,14.3702354562,18.3373999932,23.1438557976,28.9492667301,36.6870839757,46.5579193594,58.0950692886,74.1356552867,93.37787849,122.081493435,159.092021128,209.265017332,276.899278293,368.51667832,484.035177484,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,481.443979745,369.290477645,277.914597407,208.917017635,158.801341382,121.197174206,93.9715179719,73.1694561301,58.0950692886,45.6080801885,36.0320325475,28.8919507801,22.8982120121,18.0630962326,14.0590837278,10.6364307154,7.87701712412,5.89138685738,4.29469225114,2.92317584835,1.7932088347,1.22003693502,0.597736278233,0.319338561248,0.106446187083,0.00409408442626,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0])

    # Creating weights for histo: y9_sdETA_1
    y9_sdETA_1_weights = numpy.array([0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.194465719627,0.522598609472,1.68908977948,2.83086046781,5.0548365953,8.53051292647,14.2914017924,20.6224431684,30.876532136,42.1509968984,56.245124328,70.7654130899,83.4386555888,96.02297261,109.144527698,120.389114301,126.810655376,131.308281723,137.609613177,144.360498972,142.171129676,142.155507633,140.298967974,144.829280443,168.214758374,234.436640343,329.28231173,431.710362184,530.015875559,602.482128608,651.839373838,674.576256573,674.739687181,675.412636742,674.754908659,650.523116541,602.730879607,530.34313734,436.977794762,333.588708243,233.904809907,169.969474355,143.931653853,141.184577608,140.17603451,143.801750553,142.174334198,140.365982535,135.112169174,127.100704648,119.549850062,109.094537159,96.9016124091,82.0888709838,69.4040521501,54.3904673259,42.5895356958,30.2918591368,20.6802727685,13.548681782,9.30830242143,5.21125731177,3.21990422555,1.4941615272,0.631970137477,0.242966276032,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0])

    # Creating weights for histo: y9_sdETA_2
    y9_sdETA_2_weights = numpy.array([0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0200891513355,0.210960422995,0.813291874286,1.81715978951,4.0768251729,7.76100852958,14.9793682201,25.8632242305,42.3808226792,67.046645192,92.7604524644,120.221479498,152.045101553,181.64391502,205.503357019,225.714603827,246.70541378,263.855100505,275.662676447,280.288899841,281.154162867,277.305891096,265.570833617,251.48915306,229.467093378,207.625937302,187.196267364,184.103261954,181.785150408,182.220095901,186.932886918,193.505456268,193.124476082,185.971097893,182.557523688,181.865643836,181.972210853,188.68209009,204.904573518,233.845762293,248.059546283,270.439859568,279.901143001,283.383144883,281.333785521,277.503488412,265.418606827,248.064215563,228.809303401,204.306451154,181.666641604,154.265240862,122.321415839,94.0843379511,65.211990065,43.5628116411,25.2802997529,14.6793112005,8.30363670811,4.63876020416,2.16889334172,0.994014494921,0.240985669816,0.0301123640144,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0])

    # Creating weights for histo: y9_sdETA_3
    y9_sdETA_3_weights = numpy.array([0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.00548472661476,0.0220239359413,0.15957571917,0.418096017784,1.24830714538,2.77226215965,6.44653478053,13.1739227943,24.5589642203,39.5854247115,56.9462715288,77.0496299372,98.8034459416,118.747145551,138.53195825,159.086667613,172.763576561,184.944120998,191.252065442,193.835287927,190.826593025,181.954642028,166.26095401,150.077483175,128.03136563,108.417058778,90.8730755997,79.4305366934,67.9507034417,60.3125533895,61.1149505731,68.8689243492,77.9232438826,90.3582267562,108.692744429,129.666385479,149.477198593,168.421425998,183.260959755,190.785073612,193.969311942,192.006930616,183.797665198,172.583929944,158.192700218,138.363564937,119.96522437,98.4411057826,78.016357869,57.6292293058,38.7568849231,24.4439042586,12.8656066227,6.29268544964,2.96432478803,1.37509654431,0.418075704959,0.115543650664,0.00549235611155,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0])

    # Creating weights for histo: y9_sdETA_4
    y9_sdETA_4_weights = numpy.array([0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.000988581123071,0.00098844684425,0.0138263414802,0.0463834321174,0.187496203419,0.525004136234,1.33132961757,2.88750330892,5.37338146989,9.06618132362,14.1427745324,19.0967050402,24.2768091826,29.3222296632,33.9800092333,37.2841380374,39.9479452562,40.5325631765,40.3501043128,38.3393451048,35.1808707425,30.6452047331,25.5209766136,20.850855417,17.2375285837,14.3871700034,12.7599792498,12.7706574223,14.5352494806,16.9265147842,21.0000131331,26.1127373655,30.7785335816,35.1765417536,38.1663458834,39.9721435023,41.1577814006,39.7175869324,37.3396372779,33.43538636,29.5148977257,24.5106707806,18.9409335911,13.9106765964,9.13736513208,5.3427859403,2.9694771221,1.34801546462,0.525009347054,0.201286918924,0.056261262777,0.0108547391452,0.00295790830021,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0])

    # Creating weights for histo: y9_sdETA_5
    y9_sdETA_5_weights = numpy.array([0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.000251541979663,0.0,0.000252557070749,0.00352871523829,0.00781308058891,0.0420994934359,0.146209125266,0.385702524676,0.922642618418,1.69072140501,2.85028822734,4.31373901628,6.00978653872,7.6835005369,8.94370825305,10.2148746799,10.9732742723,11.3376484013,11.2320022694,10.4631440901,9.61346591962,8.10301630538,6.81618200306,5.53184031729,4.57997287002,4.02965274669,4.03995129407,4.64328052936,5.4768307105,6.84575331761,8.18773326037,9.48287761821,10.6953135179,11.2009425867,11.3456103707,10.9270388358,10.3241977213,9.06281371415,7.57272913726,5.96335505375,4.37784287256,2.87694041984,1.69772873829,0.88378540697,0.384409444829,0.133352065033,0.0433532035449,0.0113445100986,0.00302568521231,0.00100827740044,0.000252122443242,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0])

    # Creating weights for histo: y9_sdETA_6
    y9_sdETA_6_weights = numpy.array([0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.000286809860417,0.00114481585491,0.00830488528027,0.0274878563986,0.0813327586413,0.237313069157,0.500386994212,1.01341894538,1.67145514011,2.50439564537,3.35066967655,4.21260145373,4.9419457209,5.54091073708,5.64573756224,5.57250813451,5.19193783558,4.64609199517,3.93838046909,3.28110701843,2.70165045615,2.39508732398,2.37765917203,2.74075433478,3.22328642023,3.97882889655,4.57305250371,5.24639656186,5.53650021703,5.61827477743,5.42867939651,4.92386478799,4.21121491899,3.39101313922,2.50899010369,1.66082270785,1.00430200459,0.516844571841,0.237070550535,0.0841368277307,0.0254693437143,0.00858950177667,0.00143135570593,0.00056999483717,0.00028630203082,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0])

    # Creating weights for histo: y9_sdETA_7
    y9_sdETA_7_weights = numpy.array([0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,8.64683218038e-05,0.000129502469587,0.000561791901271,0.0011666328282,0.00391036144547,0.0113573881662,0.0360616590487,0.0938693729581,0.195748826014,0.353847953781,0.537447507319,0.736798874485,0.926206792213,1.05379315918,1.12979437226,1.14448030142,1.05212013169,0.933213223457,0.797500184148,0.683565419728,0.602565659839,0.607627070901,0.68655775847,0.79954369167,0.929337432325,1.06511920322,1.13125366127,1.13279299743,1.06110217706,0.923602116404,0.739212862041,0.538804118034,0.349594096993,0.191609885093,0.0907138805089,0.0380906868359,0.0119381994396,0.00291461169507,0.00110164459515,0.000345604814919,0.000151121530263,8.6405331816e-05,2.15983448062e-05,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0])

    # Creating weights for histo: y9_sdETA_8
    y9_sdETA_8_weights = numpy.array([0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,5.69022241353e-05,5.69022241353e-05,0.000283918767842,0.000511197972289,0.00130015418353,0.00439431805346,0.0174378042312,0.0446313136602,0.092675137998,0.164311905025,0.248514808568,0.337002135273,0.416009292175,0.459955665386,0.472977775482,0.452984790695,0.41106168331,0.364079000643,0.338184613495,0.335307937856,0.362870981011,0.410584118327,0.452566921335,0.471439350971,0.461773857442,0.420396771961,0.338622084403,0.249102409512,0.166384174721,0.0914023144605,0.0463894240028,0.01759261191,0.00546677664815,0.00144783417524,0.00045207123977,0.000170328095239,5.63633449166e-05,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0])

    # Creating weights for histo: y9_sdETA_9
    y9_sdETA_9_weights = numpy.array([0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,7.80655640546,49.5592131288,67.7372000009,122.530058974,344.090873292,664.607422803,1214.66318572,2158.2359906,3539.94725561,5411.11022735,8252.47450548,12081.1439928,17291.4916764,24084.5569554,32751.2496047,43220.2216517,55150.848531,69389.8736011,82756.6115464,96474.5330188,109026.969688,118305.859089,126183.859598,131892.351098,136530.21926,141291.55729,137714.660975,137622.145091,141568.72042,137818.404888,131177.06412,126244.229481,117881.424208,108509.24988,95882.2929353,81987.8760738,68268.3011588,55651.3417739,43194.8047776,33268.0811681,24199.8249789,17620.572905,11982.5911209,8500.03716655,5502.52637945,3255.61318372,2192.12233627,1227.71000174,664.573200386,310.179918244,171.9991018,104.19837884,46.9089368324,7.81340473417,5.21636160048,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0])

    # Creating weights for histo: y9_sdETA_10
    y9_sdETA_10_weights = numpy.array([0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,1.05142410245,2.1038412727,12.6409567157,18.9587225093,50.5763546765,113.753666329,248.555368254,441.3053277,766.738765053,1399.81622092,2206.49354907,3353.5942133,5152.51749825,7591.73212062,10472.3020896,14338.4716561,18931.7199915,24597.1737486,30938.5484693,37335.7827731,43916.3363936,49178.8262438,54327.0421155,57876.9998084,60025.658412,62362.5805095,61482.3245906,61478.1306971,62282.4732963,60088.0666252,57813.2449322,54247.9352806,49550.1204835,43954.6201002,37553.1880552,31113.2568377,24491.0874815,19113.0808753,14386.1242899,10645.0250919,7468.52014715,5218.65404423,3457.73551424,2240.29440675,1400.74195558,836.311225605,456.07706703,222.26565837,124.289534762,42.1403956449,20.0130596363,8.42314649463,2.10677892194,4.21495529536,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0])

    # Creating weights for histo: y9_sdETA_11
    y9_sdETA_11_weights = numpy.array([0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.230404669904,0.691645769606,1.38164511121,7.83116084013,14.282887816,36.8483843414,77.3845752982,135.679461468,261.89286485,464.784512468,755.019223372,1171.00491616,1752.36306329,2506.50739365,3498.774395,4702.13690463,6168.81032046,7716.47954105,9407.33228462,10983.0234409,12456.6322186,13499.4877856,14342.5741932,14800.1044324,14884.8772237,14845.7356553,14933.3402259,14365.4628084,13549.964156,12406.6399787,10960.830283,9419.71219368,7760.36635708,6215.3214313,4764.97397252,3553.88958107,2505.29975695,1728.64143618,1144.73391921,759.659576001,453.300629106,258.662868962,151.104244123,69.7898353718,29.2498712709,14.9699228187,6.67869197526,2.99595874043,0.921341111449,0.23009056141,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0])

    # Creating weights for histo: y9_sdETA_12
    y9_sdETA_12_weights = numpy.array([0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0831369042095,0.470672767517,0.858441806458,2.52038160746,5.56611895773,13.4308895394,28.4671592658,50.2300554973,89.8859557395,145.929051687,228.508734997,336.841226232,495.032523193,663.16788953,885.590359634,1100.54859342,1333.29373072,1554.37008378,1725.64972408,1856.36926897,1951.48346021,1959.45013405,1929.33350628,1928.45520242,1859.83978108,1729.13831778,1545.25080444,1340.49174441,1100.3193034,877.030070881,669.89770532,490.521742301,339.775753694,228.502887332,145.876422704,87.6128684132,49.7353122796,27.0554675861,12.4870918323,5.73211569455,2.43688041682,1.07943159869,0.166168358096,0.0554608301155,0.0553504169713,0.0553269108978,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0])

    # Creating weights for histo: y9_sdETA_13
    y9_sdETA_13_weights = numpy.array([0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0201690944339,0.0100703200698,0.0705860686607,0.161359758298,0.503894483834,1.31086913488,2.83335168592,6.01926354839,12.390762012,23.2070287948,40.6814002097,67.215123783,100.477641704,142.193008711,194.18651105,251.627775863,315.06580294,370.136483385,417.702427125,454.283702478,473.467746743,472.630016877,473.523878588,472.453368443,455.597187661,411.537936839,365.509580881,311.470694779,253.07215444,193.401757509,139.062186765,100.455553064,64.2531221553,40.297337021,23.1606669247,13.2793625003,6.20031757425,3.07505419854,1.06887777082,0.463769134787,0.19154345967,0.040295461914,0.0402770810102,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0])

    # Creating weights for histo: y9_sdETA_14
    y9_sdETA_14_weights = numpy.array([0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0028319583193,0.00849222491575,0.00848584205508,0.0452684867618,0.0735599492022,0.172557079442,0.461073385476,1.32688631316,3.08656482196,6.38267984472,13.0848605327,22.4809469971,36.4565801744,56.1384715564,80.6250718905,107.237407216,138.236679989,166.368051511,189.7507132,207.247061532,220.258094028,221.960113259,221.91594494,218.487283025,208.558991406,189.560650923,165.702641172,138.170581408,108.715314552,80.2587210808,56.2612040793,36.6261241896,22.5206638571,12.8247445324,6.17326122549,3.03596901269,1.32967299549,0.520612125028,0.158452150052,0.0792435038139,0.00566539866267,0.014150398134,0.0,0.00282706133011,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0])

    # Creating weights for histo: y9_sdETA_15
    y9_sdETA_15_weights = numpy.array([0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.00153120635241,0.00609276270288,0.00913543960286,0.0426453496927,0.140060287377,0.47678180803,1.18521295017,2.3486931185,4.72510640497,7.97506597452,12.3573410545,17.811569765,23.871839643,30.0147181975,34.2791503638,39.1304574448,41.0027238391,41.9747553568,41.8021291008,40.9431808379,38.8209732727,34.8228716686,29.978878959,23.688165023,17.3162485658,12.217328151,7.80504878675,4.53096833444,2.37953636947,1.16091115783,0.467479912712,0.152332006565,0.0396285909548,0.0182911869259,0.00457546783593,0.0,0.00304840432461,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0])

    # Creating weights for histo: y9_sdETA_16
    y9_sdETA_16_weights = numpy.array([0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.000180374718839,0.000180468882384,0.00108247715548,0.0,0.00198774391088,0.00650127067548,0.0386420615294,0.135615570047,0.399041996479,0.950515708675,1.93650738854,3.52494587609,5.62722500847,8.25810439181,10.9687127613,13.4005046068,15.3413905039,16.4555435827,16.8901940341,17.0050388976,16.4829376644,15.3076572323,13.3811558276,10.93188692,8.22410923383,5.5444227091,3.51137669742,1.92515577099,0.971054915314,0.385656523378,0.131452462998,0.034848553135,0.00649980719298,0.00180587347441,0.00108351853882,0.000361005932242,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0])

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
