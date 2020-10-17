def selection_1():

    # Library import
    import numpy
    import matplotlib
    import matplotlib.pyplot   as plt
    import matplotlib.gridspec as gridspec

    # Library version
    matplotlib_version = matplotlib.__version__
    numpy_version      = numpy.__version__

    # Histo binning
    xBinning = numpy.linspace(-8.0,8.0,161,endpoint=True)

    # Creating data sequence: middle of each bin
    xData = numpy.array([-7.95,-7.85,-7.75,-7.65,-7.55,-7.45,-7.35,-7.25,-7.15,-7.05,-6.95,-6.85,-6.75,-6.65,-6.55,-6.45,-6.35,-6.25,-6.15,-6.05,-5.95,-5.85,-5.75,-5.65,-5.55,-5.45,-5.35,-5.25,-5.15,-5.05,-4.95,-4.85,-4.75,-4.65,-4.55,-4.45,-4.35,-4.25,-4.15,-4.05,-3.95,-3.85,-3.75,-3.65,-3.55,-3.45,-3.35,-3.25,-3.15,-3.05,-2.95,-2.85,-2.75,-2.65,-2.55,-2.45,-2.35,-2.25,-2.15,-2.05,-1.95,-1.85,-1.75,-1.65,-1.55,-1.45,-1.35,-1.25,-1.15,-1.05,-0.95,-0.85,-0.75,-0.65,-0.55,-0.45,-0.35,-0.25,-0.15,-0.05,0.05,0.15,0.25,0.35,0.45,0.55,0.65,0.75,0.85,0.95,1.05,1.15,1.25,1.35,1.45,1.55,1.65,1.75,1.85,1.95,2.05,2.15,2.25,2.35,2.45,2.55,2.65,2.75,2.85,2.95,3.05,3.15,3.25,3.35,3.45,3.55,3.65,3.75,3.85,3.95,4.05,4.15,4.25,4.35,4.45,4.55,4.65,4.75,4.85,4.95,5.05,5.15,5.25,5.35,5.45,5.55,5.65,5.75,5.85,5.95,6.05,6.15,6.25,6.35,6.45,6.55,6.65,6.75,6.85,6.95,7.05,7.15,7.25,7.35,7.45,7.55,7.65,7.75,7.85,7.95])

    # Creating weights for histo: y2_ETA_0
    y2_ETA_0_weights = numpy.array([0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.42169082985,0.671429810635,0.736934953136,0.753311338762,1.12996700814,1.44111753502,1.84233758284,2.09617096003,2.56699054676,3.10740967239,3.51681811302,4.16777634163,4.68363188882,5.66211902993,6.16569058791,7.72553721871,8.8227522556,10.3457509188,11.7623016753,13.6496760186,15.8932340493,18.1490720692,21.2237293703,24.8142422187,29.2563223195,33.8007583305,39.7085211448,45.1004404119,51.0613951795,57.5546294799,64.1420236977,70.5778980484,77.3945720649,84.1948460958,90.9664401519,96.4361553507,100.595751699,102.798349766,103.846428846,103.621269044,100.644871656,96.8660349733,91.4495597278,83.662606563,79.0035306526,70.4059781993,62.5248651172,55.2005515463,47.5118382953,40.3881245483,39.6880491628,47.2989584821,54.0951125166,61.7305858144,69.8368986989,78.090571454,85.586804874,91.5887596056,96.0185557172,100.460631818,104.063428656,103.26098936,101.934510524,100.194512052,97.1362347362,90.6716804106,85.3288851004,78.0660114755,71.621897132,63.1348645817,56.5638703496,50.4186357437,45.3010402358,39.458781364,34.1774139999,28.687246819,25.0967339707,21.0927214853,18.3783438679,15.5042943907,13.612828051,11.6967977328,10.0591631703,8.57301247482,7.30384558886,6.70611011354,5.60070708384,4.47074007569,3.9548849285,3.38580742802,2.77988275989,2.49739100785,1.99791304628,1.70313890503,1.39198837815,1.17500216861,0.872040034544,0.70008818548,0.573171896884,0.474913583132,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0])

    # Creating weights for histo: y2_ETA_1
    y2_ETA_1_weights = numpy.array([0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0208338728701,0.0270840343312,0.0361120444416,0.0388898930909,0.0611126942857,0.0638905349351,0.0923635015909,0.0881967406169,0.11597522711,0.140281392792,0.147920474578,0.157642956851,0.180560242208,0.245839697468,0.261117861039,0.298618829805,0.357648123604,0.379870928799,0.393760172045,0.506957718507,0.520152521591,0.625016146104,0.655572553247,0.747936174838,0.795159385877,0.852105399188,0.936829818993,0.981969829545,1.11391786039,1.14725186818,1.24169869026,1.30489470503,1.3257287099,1.32364550942,1.40628632873,1.43059273442,1.43337033506,1.38753592435,1.35767391737,1.34309031396,1.29864470357,1.18336387662,1.14100186672,1.1173898612,0.960441424513,0.917385014448,0.836132595454,0.750019375325,0.636127748701,0.575709334578,0.552792129221,0.642377750162,0.68612896039,0.777797781818,0.899328610227,0.999331433604,1.07363905097,1.12572346315,1.20697548214,1.24030988994,1.32086750877,1.38406352354,1.4069807289,1.33267351153,1.37989672256,1.30489470503,1.33406231185,1.29378350244,1.31392270714,1.20628108198,1.17016907354,1.11530666071,0.97433062776,0.943079820454,0.895162209253,0.827104593344,0.70418496461,0.661822554708,0.595154139123,0.572931333929,0.472928910552,0.428483300162,0.360426004253,0.352786882468,0.320841635,0.274312664123,0.228478133409,0.192366084968,0.188199323993,0.143059273442,0.120141988084,0.107641665162,0.0770853380195,0.0798631786688,0.055556972987,0.0458345307143,0.0347231201169,0.0256951100065,0.0187504843831,0.0159726357338,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0])

    # Creating weights for histo: y2_ETA_2
    y2_ETA_2_weights = numpy.array([0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,8.99075850164,10.9590118256,13.8399850523,18.191164829,21.8959645245,25.7728310165,29.6113754338,34.7617068616,39.1605258601,42.3797603939,47.7037528679,51.9900010221,57.3108290309,63.2108342936,67.3133031241,74.1824759406,79.3261740083,85.1151025351,89.9749200302,95.9555190155,101.783222256,108.3648293,112.232446741,121.601667275,125.295559579,128.714784311,137.748691699,142.172013272,147.445814924,153.793972556,160.175817724,164.525154901,168.719994071,173.992954536,177.897423978,182.519265675,181.974176521,188.962557547,191.03548257,192.495743085,197.586686713,200.301837955,202.98205991,204.441759634,204.130440343,208.453740781,206.457323716,208.898808798,206.117684465,210.02948425,208.455983946,208.960335617,209.092321857,211.486339961,205.233837303,208.363733775,202.842903552,201.478818746,201.375753314,198.986061315,192.377576345,191.393667991,188.91368859,188.321372797,182.586760914,178.122621745,175.0684321,168.321231393,166.723376724,160.881613645,151.558818619,148.596478579,140.479384871,137.033402383,132.157842674,128.042956322,119.617948128,112.53387207,108.560585523,100.22518377,96.4162090769,89.0016266546,84.5803079076,77.8728432711,73.7643659622,67.0800940521,62.3298712016,57.7634677313,52.0266126834,49.0764097694,43.5246959669,39.0898020646,33.364206905,29.6103419756,26.344585797,21.6290038268,17.0595720835,13.913264454,11.3606665847,8.21360188686,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0])

    # Creating weights for histo: y2_ETA_3
    y2_ETA_3_weights = numpy.array([0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.753178395376,1.50573077668,2.74073009537,4.74896339948,7.41890721208,11.0443179126,15.5421071122,21.8856130574,27.9534000927,34.5965333137,43.2314986834,50.8127976643,60.6926632921,67.5104317122,74.8583493419,84.3347561324,91.6645751375,95.9150660526,104.770128052,110.612058302,117.150207104,120.409488413,125.260085094,129.438305474,131.327628335,134.557943581,134.16212914,133.592353033,136.729406645,136.685854247,137.51062262,135.039333939,136.193555129,135.00160781,133.964035974,134.633726406,134.896776279,131.392709005,133.533305237,131.671130313,132.265988304,129.445867228,128.753863423,129.841764311,127.276924748,129.1160012,126.81578171,127.358037991,128.119047967,128.063181893,127.110028984,127.286635198,126.692397023,127.758356427,128.673328676,128.041860225,129.940315041,129.434214689,130.541288549,132.016119849,130.774793863,130.751571427,132.657009502,134.123163379,134.357247189,134.735417537,135.242013742,135.349613784,136.724324154,135.751502421,136.694820917,136.685441036,136.962870638,134.808597135,132.258633155,133.71610961,127.790338928,127.838354001,121.114136462,115.934334891,110.479128449,106.044841456,100.603229643,90.3397806085,84.7997833502,76.1228977644,67.7426147526,59.6103820687,51.7472321323,43.9865584267,35.9640496875,28.0022581149,21.1653001942,16.3552436064,10.8636167818,7.41003558033,4.67877131357,2.93144083994,1.30507611884,0.602412307033,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0])

    # Creating weights for histo: y2_ETA_4
    y2_ETA_4_weights = numpy.array([0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0660560846429,0.175996847238,0.390645748357,1.08367290628,2.22767286833,3.58632209714,5.84136283941,8.94974490862,12.9640992378,17.4964752654,22.6622213933,28.734183535,35.8959814938,41.4545329483,48.6918296111,55.1573608416,61.0583580695,67.5715838105,72.7978702788,76.6378065141,80.9602535689,82.7600510202,85.1684206764,87.7350272309,88.829035302,88.2101035569,88.3684217066,87.6634042137,88.0063659329,86.4101436031,85.5603363012,84.8158713043,83.5881236005,83.7284852138,81.7731321569,81.0107106236,80.9683786985,78.908577101,78.6878985818,78.8380103506,77.8230191646,77.4383349051,75.7397359426,76.3546457486,75.1633392509,76.0243186059,75.2068493197,75.5249075168,76.0285436732,75.6478813528,76.6065247653,77.7702058224,78.3249084182,78.545058804,80.2274481329,81.4501176308,80.3480656814,83.1436790129,83.9919831658,83.7713046466,85.4670598138,86.3123982943,88.1871906915,87.3882873265,88.6220882518,89.0508107136,89.8413045696,88.0655575019,86.2064466047,85.6901352461,82.5990515778,80.7294186378,76.9521271516,71.7996168598,67.7153579783,61.7417627177,55.6310965212,49.6128942992,42.8917464924,34.7728570209,28.515109729,22.7781832425,17.480180318,12.9045664134,8.91060615947,5.86861046143,3.53172041391,1.8209187256,0.929446978093,0.439938390675,0.220110531966,0.016500399381,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0])

    # Creating weights for histo: y2_ETA_5
    y2_ETA_5_weights = numpy.array([0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.00394318335012,0.0256540889584,0.082906469605,0.219071887769,0.460869363664,0.922723572291,1.58782140238,2.42168646606,3.6001029672,4.86020388043,6.28616879891,8.06743547715,9.62287724543,11.0782311882,12.5654793571,14.0824452329,15.5369293696,16.4960489156,17.117030341,17.874671531,18.2896572204,18.6985462504,18.881702562,18.864751364,18.8429180285,18.7638819155,18.6751055775,18.2378456372,18.1382788936,17.6251133405,17.4525911099,17.2854280072,16.9291201584,16.7042973292,16.3808096291,16.3551323119,16.3079423251,15.9965317023,16.0937415519,16.1012491409,15.9239650226,16.1347026047,16.012448753,16.2593133504,16.6567866765,16.7351213331,16.7063375656,17.1315845618,17.2008764417,17.1771872527,17.8859669853,17.9498356041,18.2890880385,18.3288345695,18.5547556792,18.8744474973,18.8211368013,18.8825362932,19.0186629508,18.3039268503,17.8195049815,16.9728469541,16.3106920347,15.4650962129,14.0773546627,12.6753555074,11.2650070154,9.70843089172,7.90872993596,6.18554786643,4.72894332689,3.61100760995,2.44848972118,1.62929191305,0.911815322057,0.463810270255,0.203290919669,0.0582180858674,0.0197326254451,0.000987667624166,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0])

    # Creating weights for histo: y2_ETA_6
    y2_ETA_6_weights = numpy.array([0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.00100772285518,0.00806880377802,0.0312642610577,0.0942781992383,0.19409280788,0.381389574793,0.596163057933,0.92434623239,1.32465644711,1.73427256359,2.22510756916,2.72192605472,3.18709191115,3.68389559304,4.10134244642,4.39018589039,4.71766689117,5.01458433221,5.11265658989,5.21323346707,5.33192282429,5.44641914438,5.34269748935,5.32861400587,5.36721555377,5.19662936013,5.16861443078,4.98172820541,4.99673591749,4.88502428618,4.85475679967,4.75740071913,4.72572088329,4.66418166187,4.61860238807,4.62299147368,4.58986728058,4.63942353807,4.71833105545,4.69262469711,4.83359956654,4.84565054729,4.91774037834,5.02291039162,5.04777654213,5.16371321849,5.2625456642,5.30160332491,5.25945289922,5.38512798432,5.43682477126,5.3232806867,5.2744606113,5.14868150047,4.92309770345,4.73575536527,4.41442788653,4.02216286175,3.64754180111,3.2470743475,2.72192325402,2.20813577127,1.75471802067,1.36070616382,0.921386300266,0.606985734868,0.373332942025,0.198371786263,0.084688987395,0.0355418991099,0.00907110769285,0.00176577275501,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0])

    # Creating weights for histo: y2_ETA_7
    y2_ETA_7_weights = numpy.array([0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.000859030164652,0.0068648665917,0.0240619463563,0.0489575329964,0.103647422582,0.194084577682,0.330680244949,0.494406009099,0.688268861177,0.93644298988,1.1669444484,1.3987426718,1.67069642159,1.93000441448,2.11111364586,2.27625023662,2.4436950529,2.56892603342,2.61674298913,2.69557253899,2.75198361106,2.73948180586,2.71393437794,2.71877675315,2.6377539392,2.62941773629,2.61001124787,2.51358160346,2.52670719935,2.50020509176,2.52326235522,2.47053704645,2.4568006555,2.46763302085,2.4410449421,2.45557806572,2.48915180053,2.53174151016,2.53759754525,2.60685830579,2.61893625321,2.69238760765,2.6573333696,2.73672273163,2.74416923306,2.73959976628,2.70209834935,2.61365102659,2.54073949102,2.44318322463,2.27249949513,2.12518292511,1.87218181603,1.65882740407,1.39254175243,1.14323640329,0.898664565893,0.676002876854,0.488771699611,0.343330000504,0.192702641371,0.111964231995,0.0446823874607,0.0177499342621,0.00429240774366,0.00172155135794,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0])

    # Creating weights for histo: y2_ETA_8
    y2_ETA_8_weights = numpy.array([0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,2.16141822287e-05,0.000129634651091,0.000950176507274,0.00468590184757,0.013649662021,0.0286313757756,0.0517811222982,0.0847568625944,0.127933334702,0.170215122679,0.229957584253,0.280987017654,0.334122739,0.385633042072,0.42969061963,0.480281260505,0.505251363178,0.532069675057,0.55018296348,0.563261243871,0.570091655132,0.56881802525,0.566105222937,0.56081372873,0.5541673002,0.549282328199,0.54681260102,0.547997801845,0.532066322297,0.52724211908,0.535455124939,0.540009850033,0.542441858657,0.546649573043,0.549852716574,0.552459487837,0.563493841628,0.564182414809,0.568308824754,0.562777608174,0.561511102907,0.551072702289,0.526959229916,0.501301811347,0.476434386964,0.42908502727,0.38855996005,0.34059792529,0.280342281817,0.22708028713,0.177335924906,0.12740510729,0.0866339893609,0.0510251586319,0.0278561924099,0.0129331058631,0.00518175416587,0.00105852850547,0.000129615749904,2.15937261989e-05,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0])

    # Creating weights for histo: y2_ETA_9
    y2_ETA_9_weights = numpy.array([0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.000141111589386,0.000255667298387,0.00198671787852,0.00487793285992,0.0119700016505,0.021994124951,0.035356930937,0.0514445600054,0.0708149137943,0.0946930296621,0.118348281868,0.142480326881,0.166694535051,0.186714101023,0.206416032818,0.223848788426,0.239488150879,0.239821377196,0.24933332541,0.246291521535,0.253397973704,0.249847866047,0.24966298781,0.252102192577,0.249854399897,0.251589879387,0.249111917014,0.255924939948,0.256469476894,0.255155430688,0.256051310534,0.249206360837,0.249500532555,0.246291521535,0.241536661153,0.236835111041,0.225021614388,0.207752502007,0.186609113943,0.166938960416,0.144239951915,0.117448734156,0.094677764214,0.0717837797083,0.0530764037351,0.0347349381763,0.0202653575057,0.0121571607958,0.00551811793619,0.00203876889855,0.000625737992837,5.67516643062e-05,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0])

    # Creating weights for histo: y2_ETA_10
    y2_ETA_10_weights = numpy.array([0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,1115.69499686,1602.97337314,1728.18358196,2299.23958732,2650.88222245,3289.37484529,3714.52300125,4488.60445362,4999.4951437,5538.94809327,6287.1039503,6803.1164672,7533.14213392,8557.21141721,9107.3002324,10272.2082177,11542.4481866,12224.7547311,13348.5573645,14562.7802364,16400.3894183,17519.3124734,19247.1561383,20940.585126,22525.2214363,24877.1550855,25836.3978835,28106.9860023,30198.2563492,32061.5515695,33710.6990574,36032.4477663,38027.0609354,40295.1265929,42432.7971533,43691.9129143,46009.1550308,48260.9900344,48734.4898506,50603.6874764,51816.5068448,52661.9543402,54719.490613,55916.5445985,55544.0585891,56870.6578792,57050.5370525,58054.3689675,57990.0000628,58134.6955158,58273.3539808,58327.840682,58161.6504753,56745.0731464,56863.3135179,55878.0155409,55756.4682842,54569.2580499,53353.6316744,52465.1562194,50022.4831787,48693.4998552,47508.558298,45841.9266159,43587.515318,42018.0137753,40214.4924274,37951.6985601,35770.4309482,34250.4480886,31847.2538738,29464.4277646,27742.0827576,26279.155203,23863.3525271,22526.055848,20803.210963,19152.7791732,17758.338749,16193.9205809,14713.6780218,13664.0495922,12535.1597389,11552.2342597,10512.9840662,9646.97620446,8492.5348953,7744.07911148,6904.86086493,6115.02287369,5674.25353043,4814.19421677,4279.84771316,3683.24563521,3263.25122135,2703.14600474,2241.69094107,1842.8102201,1532.66168816,1107.77154614,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0])

    # Creating weights for histo: y2_ETA_11
    y2_ETA_11_weights = numpy.array([0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,11.5875658513,47.3974978239,85.31379544,124.285684481,220.112377904,331.779098872,468.672204039,709.86955413,895.259649761,1195.36388781,1485.11036346,1793.65317674,2195.9295074,2483.4035854,3006.98077968,3435.60938177,3861.11372567,4301.4032752,4803.80092307,5346.15213885,6154.02682545,6651.02627843,7403.07216396,7999.27066237,8597.70462138,9532.89282959,10282.845616,11087.5575683,11828.8840163,13103.0465438,13979.6395204,14747.1143165,15815.2220121,16548.4223106,17569.1890297,18387.3252885,19102.2417508,20031.5161846,20608.799839,21264.7901754,21989.5218873,22560.3877306,23377.8698959,23568.2303323,24015.0338833,24427.628346,24689.8313306,25031.3181384,25057.1971539,25022.7379711,24905.7860595,25156.3038568,24894.4356141,24898.7872595,24742.4281404,24050.3934065,23816.81663,23259.8214159,22630.1487225,22054.4348923,21572.3141419,20772.8156993,19851.1826162,19298.1081152,18205.1756488,17582.5325364,16500.5041928,15623.6611217,14551.4057041,14091.401008,12938.8921697,11800.2808938,11282.2542597,10225.7317137,9428.43410318,8743.83679674,8004.62268596,7326.11614397,6660.85691845,6062.39217857,5534.8196275,4773.24706303,4275.05485138,3841.13155506,3363.02847754,3014.32471025,2644.65955597,2215.92245131,1840.01724537,1479.83606157,1185.93455337,908.910965142,701.449062666,513.906230013,343.369750505,249.602143311,140.065766283,106.358175356,44.2408427603,16.8506365772,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0])

    # Creating weights for histo: y2_ETA_12
    y2_ETA_12_weights = numpy.array([0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.921956664991,1.84421072445,6.21730032776,10.3686543059,20.4978983799,33.8558973336,59.4230650194,96.7439575621,149.025367221,199.688551372,287.462377092,360.238914828,471.244589352,597.043218036,701.149725119,844.156504541,984.656563663,1152.38320165,1326.72321638,1501.55005126,1660.91275799,1898.63852297,2088.96137712,2265.78275293,2474.98247123,2756.41561733,3001.69036051,3280.39277989,3477.24063774,3767.47727489,4000.70485247,4199.77471577,4434.91614587,4658.91104686,4812.89529395,5039.32621681,5202.12471339,5394.3783262,5477.93695035,5630.56486348,5699.40745643,5850.89804705,5926.12270993,5956.88036782,5991.86071979,6051.62394414,6083.59577067,6012.52464036,5911.88312465,5901.22841067,5757.5223316,5773.32189303,5621.77751013,5502.50465361,5381.33369802,5183.24746501,5053.09319848,4848.07928812,4678.25321424,4417.33375455,4177.77751509,3926.00658549,3739.54025367,3501.53246344,3292.63167654,3024.97242825,2775.03466276,2516.89165324,2303.41083782,2085.24048819,1898.4164377,1702.87611651,1519.05252262,1278.36011333,1146.86910861,934.705051392,828.00690905,716.09936851,567.317987707,470.780054581,356.575391521,281.927343477,205.466572405,143.744502135,99.0300142416,54.1381270892,32.9440336374,22.1153554278,9.44055686777,4.60670179571,1.38373458132,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0])

    # Creating weights for histo: y2_ETA_13
    y2_ETA_13_weights = numpy.array([0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.11064231932,0.249445607379,1.32901647767,2.79714313039,5.7040623178,10.3292574087,16.4491540958,25.8920747941,39.7618508734,54.3024156604,70.7244665992,91.2464230547,118.377279473,142.471735939,172.597443111,197.851468426,233.02197911,261.275702585,301.55341752,332.820688888,377.044538839,415.604309879,454.70902942,489.764625796,521.396260542,561.298878557,596.494895832,627.060101179,648.448704642,679.176259631,708.017173291,726.215721715,752.334778235,767.318649875,781.023344838,797.114040928,802.446187917,811.961338817,815.158703436,813.981091464,817.232316154,801.856420144,802.665860062,776.707999039,770.260563874,751.445317641,728.628652878,707.124634978,677.686643965,654.484879697,615.789111978,595.665835459,550.805013231,521.63863086,489.445697236,450.531026801,412.673937324,373.692172631,333.479782267,302.054854778,266.056899523,227.484279009,198.871462748,171.322190525,140.947534413,115.308640422,93.5412852483,69.726747263,53.9966828168,38.6262497564,25.5307622048,16.4484693035,11.3252993885,5.51080853736,2.98993294479,1.24599271771,0.33227474013,0.0554234360869,0.0277207434524,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0])

    # Creating weights for histo: y2_ETA_14
    y2_ETA_14_weights = numpy.array([0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0100724500281,0.0302515510659,0.0907642229189,0.393252122779,1.08869686157,1.94587443793,3.93175176638,6.05850000112,10.1729776118,14.4684473513,18.4398876699,25.2450516567,32.8663362643,40.9124084722,50.2799517528,59.0593425243,68.8391848283,79.8074080827,90.1123046334,101.433217926,111.90232288,121.688621863,130.438514591,144.061440372,151.865830093,159.434769479,167.374118361,175.626167134,181.851765267,187.895071439,194.769917802,197.899768813,200.762189508,206.982022749,205.138713632,207.477196649,206.677515073,204.904416276,205.701609845,200.65411295,198.82415411,191.415660776,188.153884758,178.621362399,176.72829316,166.369267306,158.438899519,147.560001752,141.986443271,130.005722893,121.268573611,108.602923355,100.015357855,88.5097859625,78.9332076899,68.3781754999,58.3467593678,47.7365419885,41.1347816042,32.5036456556,26.3864517697,18.2091584783,14.3765731742,9.88018177011,6.09009282415,3.73057159185,2.05706282442,1.06860833609,0.534393614899,0.151252506244,0.0403616367378,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0])

    # Creating weights for histo: y2_ETA_15
    y2_ETA_15_weights = numpy.array([0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0226387064306,0.0650710139662,0.263116522434,0.622371623281,1.31820424042,2.35401171782,3.69201167543,5.72907338518,8.18748661968,11.4328577147,14.84205172,19.3094347671,24.0107175325,28.6956487863,34.9940048607,41.0254427055,46.2054861915,51.6206836528,56.8585537789,62.6346771962,67.670519586,73.0270055017,76.9022368277,82.0039854281,86.1218347136,88.5877196271,91.7494479305,93.7564132402,95.9066177924,98.7970648981,100.127077623,99.6729288133,99.4617057562,100.729929004,98.7574750027,97.089159119,95.5472692763,91.924736136,88.8082919015,85.9923307409,81.7349357308,77.8700154758,73.2309184712,68.4716667112,62.6067449668,57.8481087932,51.8779217875,45.7309076105,39.8173545466,34.9061299131,29.768788881,23.8975150552,19.5614442655,15.3538232571,11.1870464011,8.02631457807,5.75470101329,3.72340965584,2.2577590251,1.23342338356,0.602481644443,0.263080087418,0.0650914437373,0.0254628087203,0.0028319925674,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0])

    # Creating weights for histo: y2_ETA_16
    y2_ETA_16_weights = numpy.array([0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.00759008992182,0.030481064537,0.102136390749,0.210179224876,0.371623940554,0.706827629861,1.20352838164,1.73767835953,2.44070050757,3.45807046115,4.30899888459,5.60839279485,6.80543513713,7.70093868582,9.54194937715,10.4912058736,11.9729521392,12.9953807072,14.4426927093,15.4097731113,15.9646491104,17.5827203667,17.8936106844,18.3929140052,19.1768397161,19.3599589579,19.8070927329,19.8758643653,19.9052754637,20.0538789086,19.7254293735,19.2408729594,18.234857415,17.9170190355,16.9468663613,15.9100335631,15.1942650302,14.0111211749,13.120906661,11.6012012902,10.5212846004,9.23112404989,7.95791062568,6.70663795181,5.40820826238,4.40511019499,3.25519414555,2.41732406077,1.70864893181,1.09059862586,0.665624796054,0.388710028113,0.191831969563,0.0685070743185,0.0212694352361,0.00457936474976,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0])

    # Creating weights for histo: y2_ETA_17
    y2_ETA_17_weights = numpy.array([0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.000180693070939,0.00288738675524,0.0120957872613,0.0398997720441,0.0926213072737,0.180027417454,0.336392863911,0.562468721293,0.838501171728,1.23035825271,1.65846733696,2.15154503314,2.68841089747,3.37812172396,3.93114905717,4.56262252121,5.1755559721,5.77268381145,6.29243578787,6.91064932975,7.34332024316,7.69121315295,8.01851717403,8.27681799286,8.3803824909,8.51443749249,8.49124129407,8.35310394642,8.18035523645,8.01170042636,7.7113129304,7.28534322656,6.8954714752,6.28616977179,5.77076973033,5.20873466202,4.55211240574,3.93389116132,3.33751817086,2.66812125242,2.15933807772,1.64328216499,1.18770351327,0.835274577832,0.561740831288,0.343058410724,0.174963305679,0.0976865744305,0.0357507412454,0.013902464172,0.00252810217431,0.000541594453477,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0])

    # Creating a new Canvas
    fig   = plt.figure(figsize=(12,6),dpi=80)
    frame = gridspec.GridSpec(1,1,right=0.7)
    pad   = fig.add_subplot(frame[0])

    # Creating a new Stack
    pad.hist(x=xData, bins=xBinning, weights=y2_ETA_0_weights+y2_ETA_1_weights+y2_ETA_2_weights+y2_ETA_3_weights+y2_ETA_4_weights+y2_ETA_5_weights+y2_ETA_6_weights+y2_ETA_7_weights+y2_ETA_8_weights+y2_ETA_9_weights+y2_ETA_10_weights+y2_ETA_11_weights+y2_ETA_12_weights+y2_ETA_13_weights+y2_ETA_14_weights+y2_ETA_15_weights+y2_ETA_16_weights+y2_ETA_17_weights,\
             label="$bg\_dip\_1600\_inf$", histtype="step", rwidth=1.0,\
             color=None, edgecolor="#f2f2f2", linewidth=1, linestyle="solid",\
             bottom=None, cumulative=False, normed=False, align="mid", orientation="vertical")

    pad.hist(x=xData, bins=xBinning, weights=y2_ETA_0_weights+y2_ETA_1_weights+y2_ETA_2_weights+y2_ETA_3_weights+y2_ETA_4_weights+y2_ETA_5_weights+y2_ETA_6_weights+y2_ETA_7_weights+y2_ETA_8_weights+y2_ETA_9_weights+y2_ETA_10_weights+y2_ETA_11_weights+y2_ETA_12_weights+y2_ETA_13_weights+y2_ETA_14_weights+y2_ETA_15_weights+y2_ETA_16_weights,\
             label="$bg\_dip\_1200\_1600$", histtype="step", rwidth=1.0,\
             color=None, edgecolor="#ccc6aa", linewidth=1, linestyle="solid",\
             bottom=None, cumulative=False, normed=False, align="mid", orientation="vertical")

    pad.hist(x=xData, bins=xBinning, weights=y2_ETA_0_weights+y2_ETA_1_weights+y2_ETA_2_weights+y2_ETA_3_weights+y2_ETA_4_weights+y2_ETA_5_weights+y2_ETA_6_weights+y2_ETA_7_weights+y2_ETA_8_weights+y2_ETA_9_weights+y2_ETA_10_weights+y2_ETA_11_weights+y2_ETA_12_weights+y2_ETA_13_weights+y2_ETA_14_weights+y2_ETA_15_weights,\
             label="$bg\_dip\_800\_1200$", histtype="step", rwidth=1.0,\
             color=None, edgecolor="#ccc6aa", linewidth=1, linestyle="solid",\
             bottom=None, cumulative=False, normed=False, align="mid", orientation="vertical")

    pad.hist(x=xData, bins=xBinning, weights=y2_ETA_0_weights+y2_ETA_1_weights+y2_ETA_2_weights+y2_ETA_3_weights+y2_ETA_4_weights+y2_ETA_5_weights+y2_ETA_6_weights+y2_ETA_7_weights+y2_ETA_8_weights+y2_ETA_9_weights+y2_ETA_10_weights+y2_ETA_11_weights+y2_ETA_12_weights+y2_ETA_13_weights+y2_ETA_14_weights,\
             label="$bg\_dip\_600\_800$", histtype="step", rwidth=1.0,\
             color=None, edgecolor="#c1bfa8", linewidth=1, linestyle="solid",\
             bottom=None, cumulative=False, normed=False, align="mid", orientation="vertical")

    pad.hist(x=xData, bins=xBinning, weights=y2_ETA_0_weights+y2_ETA_1_weights+y2_ETA_2_weights+y2_ETA_3_weights+y2_ETA_4_weights+y2_ETA_5_weights+y2_ETA_6_weights+y2_ETA_7_weights+y2_ETA_8_weights+y2_ETA_9_weights+y2_ETA_10_weights+y2_ETA_11_weights+y2_ETA_12_weights+y2_ETA_13_weights,\
             label="$bg\_dip\_400\_600$", histtype="step", rwidth=1.0,\
             color=None, edgecolor="#bab5a3", linewidth=1, linestyle="solid",\
             bottom=None, cumulative=False, normed=False, align="mid", orientation="vertical")

    pad.hist(x=xData, bins=xBinning, weights=y2_ETA_0_weights+y2_ETA_1_weights+y2_ETA_2_weights+y2_ETA_3_weights+y2_ETA_4_weights+y2_ETA_5_weights+y2_ETA_6_weights+y2_ETA_7_weights+y2_ETA_8_weights+y2_ETA_9_weights+y2_ETA_10_weights+y2_ETA_11_weights+y2_ETA_12_weights,\
             label="$bg\_dip\_200\_400$", histtype="step", rwidth=1.0,\
             color=None, edgecolor="#b2a596", linewidth=1, linestyle="solid",\
             bottom=None, cumulative=False, normed=False, align="mid", orientation="vertical")

    pad.hist(x=xData, bins=xBinning, weights=y2_ETA_0_weights+y2_ETA_1_weights+y2_ETA_2_weights+y2_ETA_3_weights+y2_ETA_4_weights+y2_ETA_5_weights+y2_ETA_6_weights+y2_ETA_7_weights+y2_ETA_8_weights+y2_ETA_9_weights+y2_ETA_10_weights+y2_ETA_11_weights,\
             label="$bg\_dip\_100\_200$", histtype="step", rwidth=1.0,\
             color=None, edgecolor="#b7a39b", linewidth=1, linestyle="solid",\
             bottom=None, cumulative=False, normed=False, align="mid", orientation="vertical")

    pad.hist(x=xData, bins=xBinning, weights=y2_ETA_0_weights+y2_ETA_1_weights+y2_ETA_2_weights+y2_ETA_3_weights+y2_ETA_4_weights+y2_ETA_5_weights+y2_ETA_6_weights+y2_ETA_7_weights+y2_ETA_8_weights+y2_ETA_9_weights+y2_ETA_10_weights,\
             label="$bg\_dip\_0\_100$", histtype="step", rwidth=1.0,\
             color=None, edgecolor="#ad998c", linewidth=1, linestyle="solid",\
             bottom=None, cumulative=False, normed=False, align="mid", orientation="vertical")

    pad.hist(x=xData, bins=xBinning, weights=y2_ETA_0_weights+y2_ETA_1_weights+y2_ETA_2_weights+y2_ETA_3_weights+y2_ETA_4_weights+y2_ETA_5_weights+y2_ETA_6_weights+y2_ETA_7_weights+y2_ETA_8_weights+y2_ETA_9_weights,\
             label="$bg\_vbf\_1600\_inf$", histtype="step", rwidth=1.0,\
             color=None, edgecolor="#9b8e82", linewidth=1, linestyle="solid",\
             bottom=None, cumulative=False, normed=False, align="mid", orientation="vertical")

    pad.hist(x=xData, bins=xBinning, weights=y2_ETA_0_weights+y2_ETA_1_weights+y2_ETA_2_weights+y2_ETA_3_weights+y2_ETA_4_weights+y2_ETA_5_weights+y2_ETA_6_weights+y2_ETA_7_weights+y2_ETA_8_weights,\
             label="$bg\_vbf\_1200\_1600$", histtype="step", rwidth=1.0,\
             color=None, edgecolor="#876656", linewidth=1, linestyle="solid",\
             bottom=None, cumulative=False, normed=False, align="mid", orientation="vertical")

    pad.hist(x=xData, bins=xBinning, weights=y2_ETA_0_weights+y2_ETA_1_weights+y2_ETA_2_weights+y2_ETA_3_weights+y2_ETA_4_weights+y2_ETA_5_weights+y2_ETA_6_weights+y2_ETA_7_weights,\
             label="$bg\_vbf\_800\_1200$", histtype="step", rwidth=1.0,\
             color=None, edgecolor="#afcec6", linewidth=1, linestyle="solid",\
             bottom=None, cumulative=False, normed=False, align="mid", orientation="vertical")

    pad.hist(x=xData, bins=xBinning, weights=y2_ETA_0_weights+y2_ETA_1_weights+y2_ETA_2_weights+y2_ETA_3_weights+y2_ETA_4_weights+y2_ETA_5_weights+y2_ETA_6_weights,\
             label="$bg\_vbf\_600\_800$", histtype="step", rwidth=1.0,\
             color=None, edgecolor="#84c1a3", linewidth=1, linestyle="solid",\
             bottom=None, cumulative=False, normed=False, align="mid", orientation="vertical")

    pad.hist(x=xData, bins=xBinning, weights=y2_ETA_0_weights+y2_ETA_1_weights+y2_ETA_2_weights+y2_ETA_3_weights+y2_ETA_4_weights+y2_ETA_5_weights,\
             label="$bg\_vbf\_400\_600$", histtype="step", rwidth=1.0,\
             color=None, edgecolor="#89a8a0", linewidth=1, linestyle="solid",\
             bottom=None, cumulative=False, normed=False, align="mid", orientation="vertical")

    pad.hist(x=xData, bins=xBinning, weights=y2_ETA_0_weights+y2_ETA_1_weights+y2_ETA_2_weights+y2_ETA_3_weights+y2_ETA_4_weights,\
             label="$bg\_vbf\_200\_400$", histtype="step", rwidth=1.0,\
             color=None, edgecolor="#829e8c", linewidth=1, linestyle="solid",\
             bottom=None, cumulative=False, normed=False, align="mid", orientation="vertical")

    pad.hist(x=xData, bins=xBinning, weights=y2_ETA_0_weights+y2_ETA_1_weights+y2_ETA_2_weights+y2_ETA_3_weights,\
             label="$bg\_vbf\_100\_200$", histtype="step", rwidth=1.0,\
             color=None, edgecolor="#adbcc6", linewidth=1, linestyle="solid",\
             bottom=None, cumulative=False, normed=False, align="mid", orientation="vertical")

    pad.hist(x=xData, bins=xBinning, weights=y2_ETA_0_weights+y2_ETA_1_weights+y2_ETA_2_weights,\
             label="$bg\_vbf\_0\_100$", histtype="step", rwidth=1.0,\
             color=None, edgecolor="#7a8e99", linewidth=1, linestyle="solid",\
             bottom=None, cumulative=False, normed=False, align="mid", orientation="vertical")

    pad.hist(x=xData, bins=xBinning, weights=y2_ETA_0_weights+y2_ETA_1_weights,\
             label="$signal2$", histtype="step", rwidth=1.0,\
             color=None, edgecolor="#758991", linewidth=1, linestyle="solid",\
             bottom=None, cumulative=False, normed=False, align="mid", orientation="vertical")

    pad.hist(x=xData, bins=xBinning, weights=y2_ETA_0_weights,\
             label="$signal1$", histtype="step", rwidth=1.0,\
             color=None, edgecolor="#688296", linewidth=1, linestyle="solid",\
             bottom=None, cumulative=False, normed=False, align="mid", orientation="vertical")


    # Axis
    plt.rc('text',usetex=False)
    plt.xlabel(r"\eta [ j_{1} ] ",\
               fontsize=16,color="black")
    plt.ylabel(r"$\mathrm{Events}$ $(\mathcal{L}_{\mathrm{int}} = 40.0\ \mathrm{fb}^{-1})$ ",\
               fontsize=16,color="black")

    # Boundary of y-axis
    ymax=(y2_ETA_0_weights+y2_ETA_1_weights+y2_ETA_2_weights+y2_ETA_3_weights+y2_ETA_4_weights+y2_ETA_5_weights+y2_ETA_6_weights+y2_ETA_7_weights+y2_ETA_8_weights+y2_ETA_9_weights+y2_ETA_10_weights+y2_ETA_11_weights+y2_ETA_12_weights+y2_ETA_13_weights+y2_ETA_14_weights+y2_ETA_15_weights+y2_ETA_16_weights+y2_ETA_17_weights).max()*1.1
    ymin=0 # linear scale
    #ymin=min([x for x in (y2_ETA_0_weights+y2_ETA_1_weights+y2_ETA_2_weights+y2_ETA_3_weights+y2_ETA_4_weights+y2_ETA_5_weights+y2_ETA_6_weights+y2_ETA_7_weights+y2_ETA_8_weights+y2_ETA_9_weights+y2_ETA_10_weights+y2_ETA_11_weights+y2_ETA_12_weights+y2_ETA_13_weights+y2_ETA_14_weights+y2_ETA_15_weights+y2_ETA_16_weights+y2_ETA_17_weights) if x])/100. # log scale
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
    plt.savefig('../../HTML/MadAnalysis5job_0/selection_1.png')
    plt.savefig('../../PDF/MadAnalysis5job_0/selection_1.png')
    plt.savefig('../../DVI/MadAnalysis5job_0/selection_1.eps')

# Running!
if __name__ == '__main__':
    selection_1()