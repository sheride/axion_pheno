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
    y10_sdETA_0_weights = numpy.array([0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.102352106188,1.12587296806,4.40113996607,10.8493200559,18.3210232076,26.8162454212,41.452602006,57.0101177465,85.2592918543,116.476693242,153.732859094,207.160610124,260.997860778,325.479701677,402.346031224,513.295729531,642.361711234,797.425169108,1006.63307736,1242.14486149,1617.47051748,2078.36209505,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,2057.17511446,1608.56552564,1261.59184367,996.602286549,802.338064605,634.583018363,504.084037974,413.809520717,322.613804303,255.06146622,205.011212094,152.095160595,111.051998214,83.9287130739,58.1359867146,42.3737711617,24.3597976727,17.6045638643,8.59757611976,4.09408324751,1.94469021756,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0])

    # Creating weights for histo: y10_sdETA_1
    y10_sdETA_1_weights = numpy.array([0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.304262344601,0.0,0.0,0.303284616073,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.304383383345,0.303102055981,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0])

    # Creating weights for histo: y10_sdETA_2
    y10_sdETA_2_weights = numpy.array([0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.75368440663,0.250852326814,0.251143325492,0.753563751161,0.75225089983,0.501942658936,1.75638620592,2.5101667857,2.50985275092,2.00832060982,1.25444396018,0.251331229857,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,1.50570484212,1.25438817769,1.5075766547,2.00747044329,0.503266356863,1.5059062789,2.75889989424,1.50630502044,1.00452464724,1.50547034904,0.502793238672,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0])

    # Creating weights for histo: y10_sdETA_3
    y10_sdETA_3_weights = numpy.array([0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.550130945323,0.550225704937,1.92465102376,3.43805954593,3.84985455802,4.81103899353,7.14618602033,7.42782519993,8.11636703303,11.6919854427,9.62462319168,9.34919264567,7.42379817029,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,7.69751227743,8.11410417754,10.589645747,11.411017604,8.25154827351,8.38892533696,5.91201467899,6.1891372884,3.98917861159,2.06258364464,1.51236240854,0.549258405307,0.413370073268,0.137855431916,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0])

    # Creating weights for histo: y10_sdETA_4
    y10_sdETA_4_weights = numpy.array([0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0492850949849,0.148092866289,0.246897200485,0.592274965589,1.06131186634,1.84974339727,3.10919202413,4.76204624096,6.53771043731,8.14167655016,9.5231505339,10.0410956803,10.6075371204,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,9.79469510686,9.91722250198,9.0546336085,7.15397792109,6.44001639929,4.46552501455,3.35521181006,1.97361457142,1.11041942416,0.715283155032,0.172627405413,0.0739431796091,0.0247109639825,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0])

    # Creating weights for histo: y10_sdETA_5
    y10_sdETA_5_weights = numpy.array([0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0189257499166,0.0377967044595,0.107178570632,0.258490323523,0.567252551618,1.12816452429,1.90326199006,2.64061586628,3.80656799247,4.82731337864,5.17394163064,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,5.34406636181,4.72588792213,3.69272905317,2.62168255424,1.70143336387,1.20367370958,0.642642903566,0.327767760396,0.207925936889,0.0315003979317,0.00630205914174,0.0189073247471,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0])

    # Creating weights for histo: y10_sdETA_6
    y10_sdETA_6_weights = numpy.array([0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.00717057773681,0.0500327983132,0.100230199,0.23650649328,0.450855547681,0.844261967918,1.55335579592,2.09690302382,2.82052139923,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,2.43352412455,1.97577532139,1.20937607437,0.816116611607,0.601249282166,0.221639869847,0.0715985333985,0.0573102426288,0.0143136934196,0.0071292197035,0.00715788141041,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0])

    # Creating weights for histo: y10_sdETA_7
    y10_sdETA_7_weights = numpy.array([0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.00107998703023,0.00215698800522,0.00539978951548,0.0129644250763,0.0297064510134,0.0529200130315,0.102021102389,0.188927400831,0.328739641175,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.289963985091,0.169493838996,0.0993251031233,0.05718821753,0.0145478306359,0.0102618187708,0.00377909807944,0.0010793416232,0.00216013541222,0.000539959149287,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0])

    # Creating weights for histo: y10_sdETA_8
    y10_sdETA_8_weights = numpy.array([0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.00142244552682,0.0,0.00497047878563,0.00568145135167,0.00705820133639,0.00851405674949,0.0390082936332,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0460580313198,0.0169981974667,0.00851692622373,0.00422754851742,0.00212869069902,0.000705410314808,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0])

    # Creating weights for histo: y10_sdETA_9
    y10_sdETA_9_weights = numpy.array([0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0])

    # Creating weights for histo: y10_sdETA_10
    y10_sdETA_10_weights = numpy.array([0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,26.365709718,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,26.32395418,0.0,0.0,26.3028457174,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0])

    # Creating weights for histo: y10_sdETA_11
    y10_sdETA_11_weights = numpy.array([0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,5.75900461033,0.0,0.0,5.75050455924,28.8172098374,23.0259928386,51.8383608747,34.5537836506,51.7656089681,46.102036837,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,23.0517389246,63.3603396039,69.0661045746,23.0027829341,5.76682930701,23.0388082411,11.5104410242,0.0,5.77096405157,5.76549204761,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0])

    # Creating weights for histo: y10_sdETA_12
    y10_sdETA_12_weights = numpy.array([0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.690585700887,3.46064942246,1.38322383788,3.45723446576,13.1593736201,17.99255194,22.859187411,39.4515974849,44.301489955,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,49.1559119791,44.9910400133,29.7759990163,14.5438303429,7.61088352401,7.6150764869,4.15424722864,2.07536853238,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0])

    # Creating weights for histo: y10_sdETA_13
    y10_sdETA_13_weights = numpy.array([0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.251780948199,0.0,0.504062122242,0.504888549349,1.76349712994,3.27749277577,2.77375306175,9.32371511383,10.5884823743,17.3857080181,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,14.1219111437,13.1067424692,7.05673619645,3.52874664341,2.51941924729,1.76440594183,0.504575244415,0.503113559314,0.502620767824,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0])

    # Creating weights for histo: y10_sdETA_14
    y10_sdETA_14_weights = numpy.array([0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0707995201894,0.0,0.0708003762459,0.283098566591,0.211924872751,0.778026877853,1.48552547078,3.03967781913,4.59813257293,8.20481125652,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,7.2145635412,5.0931467784,2.61616549456,1.6976370408,0.848909512475,0.354047377267,0.0707757333603,0.141182188943,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0])

    # Creating weights for histo: y10_sdETA_15
    y10_sdETA_15_weights = numpy.array([0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0763571415701,0.0758645577416,0.227670496328,0.266424619893,0.609657214783,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.608904939318,0.457508763346,0.114864781163,0.113810561355,0.0384553703355,0.0,0.0380651680658,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0])

    # Creating weights for histo: y10_sdETA_16
    y10_sdETA_16_weights = numpy.array([0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.00451005131703,0.00900516620347,0.0,0.0135517284744,0.0225924316214,0.0631864526551,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0722227573558,0.0270716379918,0.0135552799551,0.0135431240741,0.00451887612095,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0])

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
    plt.ylabel(r"$\mathrm{Events}$ $(\mathcal{L}_{\mathrm{int}} = 1000.0\ \mathrm{fb}^{-1})$ ",\
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
