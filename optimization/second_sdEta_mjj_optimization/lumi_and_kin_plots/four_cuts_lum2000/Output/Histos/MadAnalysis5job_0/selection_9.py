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
    y10_sdETA_0_weights = numpy.array([0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.204704212375,2.25174593613,8.80227993214,21.6986401118,36.6420464152,53.6324908423,82.905204012,114.020235493,170.518583709,232.953386483,307.465718188,414.321220248,521.995721557,650.959403353,804.692062447,1026.59145906,1284.72342247,1594.85033822,2013.26615471,2484.28972299,3234.94103497,4156.72419009,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,4114.35022893,3217.13105129,2523.18368734,1993.2045731,1604.67612921,1269.16603673,1008.16807595,827.619041433,645.227608607,510.122932439,410.022424188,304.19032119,222.103996427,167.857426148,116.271973429,84.7475423233,48.7195953453,35.2091277285,17.1951522395,8.18816649501,3.88938043513,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0])

    # Creating weights for histo: y10_sdETA_1
    y10_sdETA_1_weights = numpy.array([0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.608524689202,0.0,0.0,0.606569232146,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.60876676669,0.606204111962,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0])

    # Creating weights for histo: y10_sdETA_2
    y10_sdETA_2_weights = numpy.array([0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,1.50736881326,0.501704653628,0.502286650984,1.50712750232,1.50450179966,1.00388531787,3.51277241183,5.0203335714,5.01970550183,4.01664121963,2.50888792037,0.502662459713,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,3.01140968424,2.50877635538,3.0151533094,4.01494088657,1.00653271373,3.01181255781,5.51779978848,3.01261004087,2.00904929447,3.01094069808,1.00558647734,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0])

    # Creating weights for histo: y10_sdETA_3
    y10_sdETA_3_weights = numpy.array([0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,1.10026189065,1.10045140987,3.84930204752,6.87611909186,7.69970911604,9.62207798707,14.2923720407,14.8556503999,16.2327340661,23.3839708855,19.2492463834,18.6983852913,14.8475963406,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,15.3950245549,16.2282083551,21.179291494,22.8220352081,16.503096547,16.7778506739,11.824029358,12.3782745768,7.97835722319,4.12516728929,3.02472481708,1.09851681061,0.826740146537,0.275710863831,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0])

    # Creating weights for histo: y10_sdETA_4
    y10_sdETA_4_weights = numpy.array([0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0985701899697,0.296185732578,0.493794400971,1.18454993118,2.12262373267,3.69948679454,6.21838404826,9.52409248191,13.0754208746,16.2833531003,19.0463010678,20.0821913606,21.2150742407,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,19.5893902137,19.834445004,18.109267217,14.3079558422,12.8800327986,8.93105002911,6.71042362012,3.94722914285,2.22083884833,1.43056631006,0.345254810826,0.147886359218,0.0494219279649,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0])

    # Creating weights for histo: y10_sdETA_5
    y10_sdETA_5_weights = numpy.array([0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0378514998332,0.0755934089189,0.214357141265,0.516980647045,1.13450510324,2.25632904858,3.80652398013,5.28123173256,7.61313598495,9.65462675727,10.3478832613,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,10.6881327236,9.45177584426,7.38545810634,5.24336510849,3.40286672774,2.40734741915,1.28528580713,0.655535520793,0.415851873779,0.0630007958634,0.0126041182835,0.0378146494942,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0])

    # Creating weights for histo: y10_sdETA_6
    y10_sdETA_6_weights = numpy.array([0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0143411554736,0.100065596626,0.200460397999,0.47301298656,0.901711095362,1.68852393584,3.10671159184,4.19380604765,5.64104279847,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,4.8670482491,3.95155064278,2.41875214873,1.63223322321,1.20249856433,0.443279739695,0.143197066797,0.114620485258,0.0286273868392,0.014258439407,0.0143157628208,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0])

    # Creating weights for histo: y10_sdETA_7
    y10_sdETA_7_weights = numpy.array([0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.00215997406046,0.00431397601044,0.010799579031,0.0259288501526,0.0594129020269,0.105840026063,0.204042204777,0.377854801663,0.65747928235,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.579927970181,0.338987677991,0.198650206247,0.11437643506,0.0290956612717,0.0205236375417,0.00755819615887,0.00215868324641,0.00432027082444,0.00107991829857,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0])

    # Creating weights for histo: y10_sdETA_8
    y10_sdETA_8_weights = numpy.array([0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.00284489105365,0.0,0.00994095757125,0.0113629027033,0.0141164026728,0.017028113499,0.0780165872664,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0921160626396,0.0339963949335,0.0170338524475,0.00845509703485,0.00425738139803,0.00141082062962,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0])

    # Creating weights for histo: y10_sdETA_9
    y10_sdETA_9_weights = numpy.array([0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0])

    # Creating weights for histo: y10_sdETA_10
    y10_sdETA_10_weights = numpy.array([0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,52.7314194359,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,52.64790836,0.0,0.0,52.6056914349,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0])

    # Creating weights for histo: y10_sdETA_11
    y10_sdETA_11_weights = numpy.array([0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,11.5180092207,0.0,0.0,11.5010091185,57.6344196748,46.0519856772,103.676721749,69.1075673012,103.531217936,92.2040736739,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,46.1034778492,126.720679208,138.132209149,46.0055658683,11.533658614,46.0776164822,23.0208820484,0.0,11.5419281031,11.5309840952,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0])

    # Creating weights for histo: y10_sdETA_12
    y10_sdETA_12_weights = numpy.array([0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,1.38117140177,6.92129884493,2.76644767576,6.91446893152,26.3187472402,35.98510388,45.7183748221,78.9031949697,88.60297991,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,98.3118239582,89.9820800266,59.5519980326,29.0876606858,15.221767048,15.2301529738,8.30849445729,4.15073706475,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0])

    # Creating weights for histo: y10_sdETA_13
    y10_sdETA_13_weights = numpy.array([0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.503561896398,0.0,1.00812424448,1.0097770987,3.52699425988,6.55498555153,5.5475061235,18.6474302277,21.1769647485,34.7714160362,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,28.2438222874,26.2134849383,14.1134723929,7.05749328683,5.03883849459,3.52881188367,1.00915048883,1.00622711863,1.00524153565,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0])

    # Creating weights for histo: y10_sdETA_14
    y10_sdETA_14_weights = numpy.array([0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.141599040379,0.0,0.141600752492,0.566197133182,0.423849745501,1.55605375571,2.97105094155,6.07935563826,9.19626514586,16.409622513,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,14.4291270824,10.1862935568,5.23233098913,3.3952740816,1.69781902495,0.708094754535,0.141551466721,0.282364377887,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0])

    # Creating weights for histo: y10_sdETA_15
    y10_sdETA_15_weights = numpy.array([0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.15271428314,0.151729115483,0.455340992656,0.532849239786,1.21931442957,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,1.21780987864,0.915017526691,0.229729562326,0.227621122711,0.076910740671,0.0,0.0761303361315,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0])

    # Creating weights for histo: y10_sdETA_16
    y10_sdETA_16_weights = numpy.array([0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.00902010263406,0.0180103324069,0.0,0.0271034569489,0.0451848632429,0.12637290531,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.144445514712,0.0541432759836,0.0271105599103,0.0270862481481,0.0090377522419,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0])

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
    plt.ylabel(r"$\mathrm{Events}$ $(\mathcal{L}_{\mathrm{int}} = 2000.0\ \mathrm{fb}^{-1})$ ",\
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
