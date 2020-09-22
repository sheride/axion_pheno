def selection_6():

    # Library import
    import numpy
    import matplotlib
    import matplotlib.pyplot   as plt
    import matplotlib.gridspec as gridspec

    # Library version
    matplotlib_version = matplotlib.__version__
    numpy_version      = numpy.__version__

    # Histo binning
    xBinning = numpy.linspace(0.0,15.0,76,endpoint=True)

    # Creating data sequence: middle of each bin
    xData = numpy.array([0.1,0.3,0.5,0.7,0.9,1.1,1.3,1.5,1.7,1.9,2.1,2.3,2.5,2.7,2.9,3.1,3.3,3.5,3.7,3.9,4.1,4.3,4.5,4.7,4.9,5.1,5.3,5.5,5.7,5.9,6.1,6.3,6.5,6.7,6.9,7.1,7.3,7.5,7.7,7.9,8.1,8.3,8.5,8.7,8.9,9.1,9.3,9.5,9.7,9.9,10.1,10.3,10.5,10.7,10.9,11.1,11.3,11.5,11.7,11.9,12.1,12.3,12.5,12.7,12.9,13.1,13.3,13.5,13.7,13.9,14.1,14.3,14.5,14.7,14.9])

    # Creating weights for histo: y7_DELTAR_0
    y7_DELTAR_0_weights = numpy.array([0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.889821550095,1.99192708828,3.01973303064,3.54159660137,3.89894058133,4.01038777508,3.88125018232,3.57697699939,3.08518702697,2.89766983748,2.63408465227,2.36165386755,1.95477749037,1.81679309811,1.52844111428,1.24362753025,1.14456193581,0.92520234811,0.792525155551,0.633312364481,0.498866372021,0.399800617577,0.313118182439,0.291889823629,0.201669348689,0.18044098988,0.132677192559,0.0937585547416,0.040687677718,0.024766410611,0.0212283508094,0.0106141754047,0.00353805860157,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0])

    # Creating weights for histo: y7_DELTAR_1
    y7_DELTAR_1_weights = numpy.array([0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.555707683708,1.29939747811,1.83155628862,2.27604321859,2.42569061425,2.6169916856,2.54954332267,2.28877189634,2.18953241471,1.85396806607,1.60392370924,1.56338154964,1.36465478344,1.17756116619,1.01086213052,0.851690308982,0.756535579027,0.612292285846,0.516100780368,0.388953811651,0.350493276683,0.278914878085,0.220105685011,0.176284493007,0.146392623964,0.104722001759,0.0673214238786,0.0619850675177,0.0363260763574,0.0277817350873,0.0128212761165,0.00641568204712,0.00106772690986,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0])

    # Creating weights for histo: y7_DELTAR_2
    y7_DELTAR_2_weights = numpy.array([0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.341675519321,0.812520988628,1.23961548778,1.45003753663,1.67990438999,1.73685040321,1.7049051958,1.55142916017,1.46392673985,1.30836710374,1.18822507585,1.05141624409,0.939607818132,0.820160190402,0.656961352515,0.568070131878,0.522235721238,0.421538497861,0.353481362061,0.289590827229,0.246534137233,0.22778365288,0.163198677887,0.118753067569,0.0854188598301,0.0763908577343,0.0520846920916,0.0479178911242,0.0194449485142,0.0180560241917,0.00555569728976,0.00138892472244,0.000694462561221,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0])

    # Creating weights for histo: y7_DELTAR_3
    y7_DELTAR_3_weights = numpy.array([0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.236603630191,0.548123762607,0.883825862197,1.09909272606,1.16120714449,1.24513276938,1.19250115377,1.07917832015,0.97154468822,0.916542671903,0.818392642786,0.739208619295,0.634420188208,0.562348566827,0.476526541367,0.427214126738,0.361306587186,0.310097771994,0.233758709347,0.201990299923,0.166902769514,0.146039923324,0.115693954322,0.0848738651788,0.062114378427,0.059269457583,0.0440964530817,0.0260785597365,0.0199145339079,0.0109055792353,0.00379324472531,0.00331908938465,0.000474155740664,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0])

    # Creating weights for histo: y7_DELTAR_4
    y7_DELTAR_4_weights = numpy.array([0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0])

    # Creating weights for histo: y7_DELTAR_5
    y7_DELTAR_5_weights = numpy.array([0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,1.0529581672,0.0,0.0,0.0,1.0521138287,0.0,1.05462838872,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0])

    # Creating weights for histo: y7_DELTAR_6
    y7_DELTAR_6_weights = numpy.array([0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.460540223078,0.461016717805,1.38163834565,2.76536711978,1.38236653719,4.14433209946,2.53295143703,0.690788239096,1.61159739067,1.3832088569,0.690965387539,0.690784012127,0.230465320669,0.0,0.461458243967,0.0,0.230360184413,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0])

    # Creating weights for histo: y7_DELTAR_7
    y7_DELTAR_7_weights = numpy.array([0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.525788722102,0.830934494971,1.35684977532,1.52284879879,1.85491724136,1.60630299698,1.24655522799,1.10780200164,0.858689987152,0.553686928898,0.304478553194,0.138431945359,0.193781750681,0.0830468652927,0.0552968355042,0.02771791323,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0])

    # Creating weights for histo: y7_DELTAR_8
    y7_DELTAR_8_weights = numpy.array([0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.20152539658,0.231967957427,0.393278166664,0.453863425926,0.413352988485,0.645125407205,0.413398322878,0.312568806426,0.201600529082,0.141095318098,0.0302722746709,0.0604623708924,0.0504291960467,0.0301716832966,0.0201542085948,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0])

    # Creating weights for histo: y7_DELTAR_9
    y7_DELTAR_9_weights = numpy.array([0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0594504139488,0.0933353246716,0.155640889157,0.138622908449,0.282903331025,0.26593794489,0.209369382748,0.104673014378,0.0905212648482,0.0197882643018,0.0169763090309,0.0113135162088,0.0113285173973,0.00282347952324,0.00565245858451,0.0,0.0,0.00283198083794,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0])

    # Creating weights for histo: y7_DELTAR_10
    y7_DELTAR_10_weights = numpy.array([0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0136881402288,0.0197592221531,0.0167628609754,0.00759898478221,0.0167790056467,0.0137200513654,0.00916855176561,0.00458510202668,0.00152260679112,0.00151881882101,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0])

    # Creating weights for histo: y7_DELTAR_11
    y7_DELTAR_11_weights = numpy.array([0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.000541741113055,0.00108418443755,0.00162474942344,0.00108258713751,0.00162513248286,0.00180581294981,0.00126438482902,0.000180755038415,0.00036094919314,0.0,0.000180003625974,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0])

    # Creating weights for histo: y7_DELTAR_12
    y7_DELTAR_12_weights = numpy.array([0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0243067199767,0.0,0.0,0.0242945760233,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0])

    # Creating weights for histo: y7_DELTAR_13
    y7_DELTAR_13_weights = numpy.array([0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0301235473445,0.0301201301501,0.0602001795444,0.07029003463,0.170647867166,0.0702986705867,0.110519502419,0.070259953403,0.080279563865,0.0903759888888,0.110412193426,0.0903980539647,0.0100457331979,0.0602205091649,0.0702763989089,0.0100369732801,0.0100340932506,0.0201103993878,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0])

    # Creating weights for histo: y7_DELTAR_14
    y7_DELTAR_14_weights = numpy.array([0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.115514678532,0.137468441067,0.32449557438,0.401432017002,0.505913588194,0.588625228483,0.544406103719,0.506126060997,0.594246616965,0.407111297214,0.390549671913,0.313482576798,0.285907750787,0.253083830895,0.275016427402,0.120956216709,0.104539828553,0.0605001072115,0.0660036809464,0.0384954040172,0.00551421768798,0.00550877789671,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0])

    # Creating weights for histo: y7_DELTAR_15
    y7_DELTAR_15_weights = numpy.array([0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0868390655213,0.199335150448,0.307919946725,0.387786392682,0.495404910669,0.496345255327,0.522048810971,0.443091124353,0.411545086299,0.287165425818,0.235871989614,0.155924856794,0.146079536407,0.101652219522,0.0651206312155,0.0384886074746,0.0286232536578,0.0138174027603,0.00986914966675,0.00197291163428,0.00197407403816,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0])

    # Creating weights for histo: y7_DELTAR_16
    y7_DELTAR_16_weights = numpy.array([0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0363016452016,0.0746097333537,0.127303637754,0.163844650115,0.207199014107,0.222824918288,0.227387318367,0.179241530038,0.131321845148,0.0965403664611,0.0620102382963,0.0491625936153,0.0274789978195,0.0166353474019,0.0103369482515,0.00352911856957,0.00201570634945,0.000756662697875,0.000756519057574,0.0,0.000504354307369,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0])

    # Creating weights for histo: y7_DELTAR_17
    y7_DELTAR_17_weights = numpy.array([0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0114511954272,0.0331991204441,0.047528882664,0.0718684875137,0.085902275404,0.106799386691,0.0916263185676,0.0658524988544,0.0434946203898,0.0294804568192,0.0163342720103,0.0108731127544,0.00515766010433,0.000859006658699,0.000858866099384,0.00142981713639,0.000285168757298,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0])

    # Creating weights for histo: y7_DELTAR_18
    y7_DELTAR_18_weights = numpy.array([0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.00129592372255,0.00295905220822,0.00386564921218,0.00611157314405,0.00848027570987,0.0116604938285,0.00958793251804,0.00509809128351,0.0026786190709,0.00151253490312,0.000970509904428,0.000302351663836,0.000172841392388,0.000129582942606,6.47735549708e-05,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0])

    # Creating weights for histo: y7_DELTAR_19
    y7_DELTAR_19_weights = numpy.array([0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.000169965676692,0.000311772196928,0.000595852074499,0.000763864132964,0.000934732747442,0.00133389450317,0.000623547215073,0.000511421229446,0.000311011359367,0.000113616167064,2.84292656694e-05,8.50337984264e-05,0.0,2.84489102457e-05,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0])

    # Creating a new Canvas
    fig   = plt.figure(figsize=(12,6),dpi=80)
    frame = gridspec.GridSpec(1,1,right=0.7)
    pad   = fig.add_subplot(frame[0])

    # Creating a new Stack
    pad.hist(x=xData, bins=xBinning, weights=y7_DELTAR_0_weights+y7_DELTAR_1_weights+y7_DELTAR_2_weights+y7_DELTAR_3_weights+y7_DELTAR_4_weights+y7_DELTAR_5_weights+y7_DELTAR_6_weights+y7_DELTAR_7_weights+y7_DELTAR_8_weights+y7_DELTAR_9_weights+y7_DELTAR_10_weights+y7_DELTAR_11_weights+y7_DELTAR_12_weights+y7_DELTAR_13_weights+y7_DELTAR_14_weights+y7_DELTAR_15_weights+y7_DELTAR_16_weights+y7_DELTAR_17_weights+y7_DELTAR_18_weights+y7_DELTAR_19_weights,\
             label="$bg\_vbf\_1600\_inf$", histtype="step", rwidth=1.0,\
             color=None, edgecolor="#ccc6aa", linewidth=1, linestyle="solid",\
             bottom=None, cumulative=False, normed=False, align="mid", orientation="vertical")

    pad.hist(x=xData, bins=xBinning, weights=y7_DELTAR_0_weights+y7_DELTAR_1_weights+y7_DELTAR_2_weights+y7_DELTAR_3_weights+y7_DELTAR_4_weights+y7_DELTAR_5_weights+y7_DELTAR_6_weights+y7_DELTAR_7_weights+y7_DELTAR_8_weights+y7_DELTAR_9_weights+y7_DELTAR_10_weights+y7_DELTAR_11_weights+y7_DELTAR_12_weights+y7_DELTAR_13_weights+y7_DELTAR_14_weights+y7_DELTAR_15_weights+y7_DELTAR_16_weights+y7_DELTAR_17_weights+y7_DELTAR_18_weights,\
             label="$bg\_vbf\_1200\_1600$", histtype="step", rwidth=1.0,\
             color=None, edgecolor="#c1bfa8", linewidth=1, linestyle="solid",\
             bottom=None, cumulative=False, normed=False, align="mid", orientation="vertical")

    pad.hist(x=xData, bins=xBinning, weights=y7_DELTAR_0_weights+y7_DELTAR_1_weights+y7_DELTAR_2_weights+y7_DELTAR_3_weights+y7_DELTAR_4_weights+y7_DELTAR_5_weights+y7_DELTAR_6_weights+y7_DELTAR_7_weights+y7_DELTAR_8_weights+y7_DELTAR_9_weights+y7_DELTAR_10_weights+y7_DELTAR_11_weights+y7_DELTAR_12_weights+y7_DELTAR_13_weights+y7_DELTAR_14_weights+y7_DELTAR_15_weights+y7_DELTAR_16_weights+y7_DELTAR_17_weights,\
             label="$bg\_vbf\_800\_1200$", histtype="step", rwidth=1.0,\
             color=None, edgecolor="#bab5a3", linewidth=1, linestyle="solid",\
             bottom=None, cumulative=False, normed=False, align="mid", orientation="vertical")

    pad.hist(x=xData, bins=xBinning, weights=y7_DELTAR_0_weights+y7_DELTAR_1_weights+y7_DELTAR_2_weights+y7_DELTAR_3_weights+y7_DELTAR_4_weights+y7_DELTAR_5_weights+y7_DELTAR_6_weights+y7_DELTAR_7_weights+y7_DELTAR_8_weights+y7_DELTAR_9_weights+y7_DELTAR_10_weights+y7_DELTAR_11_weights+y7_DELTAR_12_weights+y7_DELTAR_13_weights+y7_DELTAR_14_weights+y7_DELTAR_15_weights+y7_DELTAR_16_weights,\
             label="$bg\_vbf\_600\_800$", histtype="step", rwidth=1.0,\
             color=None, edgecolor="#b2a596", linewidth=1, linestyle="solid",\
             bottom=None, cumulative=False, normed=False, align="mid", orientation="vertical")

    pad.hist(x=xData, bins=xBinning, weights=y7_DELTAR_0_weights+y7_DELTAR_1_weights+y7_DELTAR_2_weights+y7_DELTAR_3_weights+y7_DELTAR_4_weights+y7_DELTAR_5_weights+y7_DELTAR_6_weights+y7_DELTAR_7_weights+y7_DELTAR_8_weights+y7_DELTAR_9_weights+y7_DELTAR_10_weights+y7_DELTAR_11_weights+y7_DELTAR_12_weights+y7_DELTAR_13_weights+y7_DELTAR_14_weights+y7_DELTAR_15_weights,\
             label="$bg\_vbf\_400\_600$", histtype="step", rwidth=1.0,\
             color=None, edgecolor="#b7a39b", linewidth=1, linestyle="solid",\
             bottom=None, cumulative=False, normed=False, align="mid", orientation="vertical")

    pad.hist(x=xData, bins=xBinning, weights=y7_DELTAR_0_weights+y7_DELTAR_1_weights+y7_DELTAR_2_weights+y7_DELTAR_3_weights+y7_DELTAR_4_weights+y7_DELTAR_5_weights+y7_DELTAR_6_weights+y7_DELTAR_7_weights+y7_DELTAR_8_weights+y7_DELTAR_9_weights+y7_DELTAR_10_weights+y7_DELTAR_11_weights+y7_DELTAR_12_weights+y7_DELTAR_13_weights+y7_DELTAR_14_weights,\
             label="$bg\_vbf\_200\_400$", histtype="step", rwidth=1.0,\
             color=None, edgecolor="#ad998c", linewidth=1, linestyle="solid",\
             bottom=None, cumulative=False, normed=False, align="mid", orientation="vertical")

    pad.hist(x=xData, bins=xBinning, weights=y7_DELTAR_0_weights+y7_DELTAR_1_weights+y7_DELTAR_2_weights+y7_DELTAR_3_weights+y7_DELTAR_4_weights+y7_DELTAR_5_weights+y7_DELTAR_6_weights+y7_DELTAR_7_weights+y7_DELTAR_8_weights+y7_DELTAR_9_weights+y7_DELTAR_10_weights+y7_DELTAR_11_weights+y7_DELTAR_12_weights+y7_DELTAR_13_weights,\
             label="$bg\_vbf\_100\_200$", histtype="step", rwidth=1.0,\
             color=None, edgecolor="#9b8e82", linewidth=1, linestyle="solid",\
             bottom=None, cumulative=False, normed=False, align="mid", orientation="vertical")

    pad.hist(x=xData, bins=xBinning, weights=y7_DELTAR_0_weights+y7_DELTAR_1_weights+y7_DELTAR_2_weights+y7_DELTAR_3_weights+y7_DELTAR_4_weights+y7_DELTAR_5_weights+y7_DELTAR_6_weights+y7_DELTAR_7_weights+y7_DELTAR_8_weights+y7_DELTAR_9_weights+y7_DELTAR_10_weights+y7_DELTAR_11_weights+y7_DELTAR_12_weights,\
             label="$bg\_vbf\_0\_100$", histtype="step", rwidth=1.0,\
             color=None, edgecolor="#876656", linewidth=1, linestyle="solid",\
             bottom=None, cumulative=False, normed=False, align="mid", orientation="vertical")

    pad.hist(x=xData, bins=xBinning, weights=y7_DELTAR_0_weights+y7_DELTAR_1_weights+y7_DELTAR_2_weights+y7_DELTAR_3_weights+y7_DELTAR_4_weights+y7_DELTAR_5_weights+y7_DELTAR_6_weights+y7_DELTAR_7_weights+y7_DELTAR_8_weights+y7_DELTAR_9_weights+y7_DELTAR_10_weights+y7_DELTAR_11_weights,\
             label="$bg\_dip\_1600\_inf$", histtype="step", rwidth=1.0,\
             color=None, edgecolor="#afcec6", linewidth=1, linestyle="solid",\
             bottom=None, cumulative=False, normed=False, align="mid", orientation="vertical")

    pad.hist(x=xData, bins=xBinning, weights=y7_DELTAR_0_weights+y7_DELTAR_1_weights+y7_DELTAR_2_weights+y7_DELTAR_3_weights+y7_DELTAR_4_weights+y7_DELTAR_5_weights+y7_DELTAR_6_weights+y7_DELTAR_7_weights+y7_DELTAR_8_weights+y7_DELTAR_9_weights+y7_DELTAR_10_weights,\
             label="$bg\_dip\_1200\_1600$", histtype="step", rwidth=1.0,\
             color=None, edgecolor="#84c1a3", linewidth=1, linestyle="solid",\
             bottom=None, cumulative=False, normed=False, align="mid", orientation="vertical")

    pad.hist(x=xData, bins=xBinning, weights=y7_DELTAR_0_weights+y7_DELTAR_1_weights+y7_DELTAR_2_weights+y7_DELTAR_3_weights+y7_DELTAR_4_weights+y7_DELTAR_5_weights+y7_DELTAR_6_weights+y7_DELTAR_7_weights+y7_DELTAR_8_weights+y7_DELTAR_9_weights,\
             label="$bg\_dip\_800\_1200$", histtype="step", rwidth=1.0,\
             color=None, edgecolor="#89a8a0", linewidth=1, linestyle="solid",\
             bottom=None, cumulative=False, normed=False, align="mid", orientation="vertical")

    pad.hist(x=xData, bins=xBinning, weights=y7_DELTAR_0_weights+y7_DELTAR_1_weights+y7_DELTAR_2_weights+y7_DELTAR_3_weights+y7_DELTAR_4_weights+y7_DELTAR_5_weights+y7_DELTAR_6_weights+y7_DELTAR_7_weights+y7_DELTAR_8_weights,\
             label="$bg\_dip\_600\_800$", histtype="step", rwidth=1.0,\
             color=None, edgecolor="#829e8c", linewidth=1, linestyle="solid",\
             bottom=None, cumulative=False, normed=False, align="mid", orientation="vertical")

    pad.hist(x=xData, bins=xBinning, weights=y7_DELTAR_0_weights+y7_DELTAR_1_weights+y7_DELTAR_2_weights+y7_DELTAR_3_weights+y7_DELTAR_4_weights+y7_DELTAR_5_weights+y7_DELTAR_6_weights+y7_DELTAR_7_weights,\
             label="$bg\_dip\_400\_600$", histtype="step", rwidth=1.0,\
             color=None, edgecolor="#adbcc6", linewidth=1, linestyle="solid",\
             bottom=None, cumulative=False, normed=False, align="mid", orientation="vertical")

    pad.hist(x=xData, bins=xBinning, weights=y7_DELTAR_0_weights+y7_DELTAR_1_weights+y7_DELTAR_2_weights+y7_DELTAR_3_weights+y7_DELTAR_4_weights+y7_DELTAR_5_weights+y7_DELTAR_6_weights,\
             label="$bg\_dip\_200\_400$", histtype="step", rwidth=1.0,\
             color=None, edgecolor="#7a8e99", linewidth=1, linestyle="solid",\
             bottom=None, cumulative=False, normed=False, align="mid", orientation="vertical")

    pad.hist(x=xData, bins=xBinning, weights=y7_DELTAR_0_weights+y7_DELTAR_1_weights+y7_DELTAR_2_weights+y7_DELTAR_3_weights+y7_DELTAR_4_weights+y7_DELTAR_5_weights,\
             label="$bg\_dip\_100\_200$", histtype="step", rwidth=1.0,\
             color=None, edgecolor="#758991", linewidth=1, linestyle="solid",\
             bottom=None, cumulative=False, normed=False, align="mid", orientation="vertical")

    pad.hist(x=xData, bins=xBinning, weights=y7_DELTAR_0_weights+y7_DELTAR_1_weights+y7_DELTAR_2_weights+y7_DELTAR_3_weights+y7_DELTAR_4_weights,\
             label="$bg\_dip\_0\_100$", histtype="step", rwidth=1.0,\
             color=None, edgecolor="#688296", linewidth=1, linestyle="solid",\
             bottom=None, cumulative=False, normed=False, align="mid", orientation="vertical")

    pad.hist(x=xData, bins=xBinning, weights=y7_DELTAR_0_weights+y7_DELTAR_1_weights+y7_DELTAR_2_weights+y7_DELTAR_3_weights,\
             label="$signal\_2pt4TeVL$", histtype="step", rwidth=1.0,\
             color=None, edgecolor="#6d7a84", linewidth=1, linestyle="solid",\
             bottom=None, cumulative=False, normed=False, align="mid", orientation="vertical")

    pad.hist(x=xData, bins=xBinning, weights=y7_DELTAR_0_weights+y7_DELTAR_1_weights+y7_DELTAR_2_weights,\
             label="$signal\_2pt2TeVL$", histtype="step", rwidth=1.0,\
             color=None, edgecolor="#7c99d1", linewidth=1, linestyle="solid",\
             bottom=None, cumulative=False, normed=False, align="mid", orientation="vertical")

    pad.hist(x=xData, bins=xBinning, weights=y7_DELTAR_0_weights+y7_DELTAR_1_weights,\
             label="$signal\_2TeVL$", histtype="step", rwidth=1.0,\
             color=None, edgecolor="#7f7f9b", linewidth=1, linestyle="solid",\
             bottom=None, cumulative=False, normed=False, align="mid", orientation="vertical")

    pad.hist(x=xData, bins=xBinning, weights=y7_DELTAR_0_weights,\
             label="$signal\_1pt8TeVL$", histtype="step", rwidth=1.0,\
             color=None, edgecolor="#aaa5bf", linewidth=1, linestyle="solid",\
             bottom=None, cumulative=False, normed=False, align="mid", orientation="vertical")


    # Axis
    plt.rc('text',usetex=False)
    plt.xlabel(r"\Delta R [ j_{1} , j_{2} ] ",\
               fontsize=16,color="black")
    plt.ylabel(r"$\mathrm{Events}$ $(\mathcal{L}_{\mathrm{int}} = 40.0\ \mathrm{fb}^{-1})$ ",\
               fontsize=16,color="black")

    # Boundary of y-axis
    ymax=(y7_DELTAR_0_weights+y7_DELTAR_1_weights+y7_DELTAR_2_weights+y7_DELTAR_3_weights+y7_DELTAR_4_weights+y7_DELTAR_5_weights+y7_DELTAR_6_weights+y7_DELTAR_7_weights+y7_DELTAR_8_weights+y7_DELTAR_9_weights+y7_DELTAR_10_weights+y7_DELTAR_11_weights+y7_DELTAR_12_weights+y7_DELTAR_13_weights+y7_DELTAR_14_weights+y7_DELTAR_15_weights+y7_DELTAR_16_weights+y7_DELTAR_17_weights+y7_DELTAR_18_weights+y7_DELTAR_19_weights).max()*1.1
    ymin=0 # linear scale
    #ymin=min([x for x in (y7_DELTAR_0_weights+y7_DELTAR_1_weights+y7_DELTAR_2_weights+y7_DELTAR_3_weights+y7_DELTAR_4_weights+y7_DELTAR_5_weights+y7_DELTAR_6_weights+y7_DELTAR_7_weights+y7_DELTAR_8_weights+y7_DELTAR_9_weights+y7_DELTAR_10_weights+y7_DELTAR_11_weights+y7_DELTAR_12_weights+y7_DELTAR_13_weights+y7_DELTAR_14_weights+y7_DELTAR_15_weights+y7_DELTAR_16_weights+y7_DELTAR_17_weights+y7_DELTAR_18_weights+y7_DELTAR_19_weights) if x])/100. # log scale
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
    plt.savefig('../../HTML/MadAnalysis5job_0/selection_6.png')
    plt.savefig('../../PDF/MadAnalysis5job_0/selection_6.png')
    plt.savefig('../../DVI/MadAnalysis5job_0/selection_6.eps')

# Running!
if __name__ == '__main__':
    selection_6()
