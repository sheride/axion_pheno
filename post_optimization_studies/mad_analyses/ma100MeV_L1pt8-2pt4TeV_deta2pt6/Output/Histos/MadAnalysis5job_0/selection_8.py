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
    xBinning = numpy.linspace(2.6,15.0,101,endpoint=True)

    # Creating data sequence: middle of each bin
    xData = numpy.array([2.662,2.786,2.91,3.034,3.158,3.282,3.406,3.53,3.654,3.778,3.902,4.026,4.15,4.274,4.398,4.522,4.646,4.77,4.894,5.018,5.142,5.266,5.39,5.514,5.638,5.762,5.886,6.01,6.134,6.258,6.382,6.506,6.63,6.754,6.878,7.002,7.126,7.25,7.374,7.498,7.622,7.746,7.87,7.994,8.118,8.242,8.366,8.49,8.614,8.738,8.862,8.986,9.11,9.234,9.358,9.482,9.606,9.73,9.854,9.978,10.102,10.226,10.35,10.474,10.598,10.722,10.846,10.97,11.094,11.218,11.342,11.466,11.59,11.714,11.838,11.962,12.086,12.21,12.334,12.458,12.582,12.706,12.83,12.954,13.078,13.202,13.326,13.45,13.574,13.698,13.822,13.946,14.07,14.194,14.318,14.442,14.566,14.69,14.814,14.938])

    # Creating weights for histo: y9_sdETA_0
    y9_sdETA_0_weights = numpy.array([1.44529669384,1.56912908475,1.48244629111,1.44529669384,1.40107109709,1.42229949553,1.46829429215,1.45237309332,1.43114469488,1.33207910216,1.31438870346,1.26662510697,1.22416831008,1.19409471229,1.16755911424,1.15694511502,1.05257232269,1.00657752607,0.971197128665,0.84736513776,0.824367539449,0.746530345167,0.83675073854,0.679307150104,0.702304748415,0.56608915842,0.585548756991,0.525401561409,0.514787562188,0.495328363618,0.442257167516,0.348498774402,0.334346535442,0.313118177001,0.27419953986,0.263585340639,0.229973783108,0.185748066357,0.187517106227,0.155674588566,0.127370110645,0.0990656327235,0.104372712334,0.0813753540229,0.100834672594,0.0919895132433,0.0583779557121,0.0406876770115,0.0389186411414,0.0353805854013,0.0300734977911,0.0194593225707,0.0176902907006,0.0159212628306,0.00707611548025,0.00530708761019,0.00884514735032,0.00530708761019,0.00176902907006,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0])

    # Creating weights for histo: y9_sdETA_1
    y9_sdETA_1_weights = numpy.array([0.809988922934,0.835596878115,0.855968613776,0.840956998714,0.804643990209,0.814220744343,0.881574570552,0.804654381913,0.854891873421,0.806760700275,0.836751556246,0.786454112601,0.809993719105,0.809960945271,0.728759774472,0.72133290392,0.716956797705,0.675297657432,0.632578563403,0.61010970204,0.598386661454,0.536429326806,0.53745250992,0.474448011304,0.433824444253,0.400758043728,0.391112264703,0.368679774302,0.321632216022,0.280986986266,0.29387397758,0.240431884553,0.222257554532,0.193408107287,0.176285257787,0.161370685249,0.14317057581,0.152801246897,0.0854885078846,0.119673855067,0.0865637694198,0.0844286740323,0.0715944006295,0.0555584833477,0.0373941213687,0.0459358058785,0.0299166592074,0.035262399288,0.0245784770928,0.0288504664319,0.0128178425208,0.0117598711815,0.00961696602911,0.0138926883879,0.0106831588046,0.00427275672646,0.00320689808419,0.00427275672646,0.00106958726542,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0])

    # Creating weights for histo: y9_sdETA_2
    y9_sdETA_2_weights = numpy.array([0.481262543233,0.515290953361,0.529874957701,0.529180557495,0.504179750054,0.509040951501,0.575709371343,0.500707349021,0.568764569276,0.536124959562,0.551403364109,0.535430559355,0.490984946127,0.514596553154,0.513902152948,0.49654054778,0.489596145714,0.453484134966,0.451400534346,0.410427322151,0.382648793884,0.392371276778,0.35625922603,0.309035771975,0.311119172595,0.293757607428,0.250006474407,0.229172588206,0.231950469033,0.204171940766,0.157642966918,0.175699012292,0.152781725471,0.13403123989,0.12986447865,0.097224748936,0.10278043059,0.0930579476959,0.0847244252157,0.0687517804619,0.0763908627355,0.0513902152948,0.0548625363282,0.035417586541,0.0312508093009,0.0291674206808,0.0270840360608,0.0215283344073,0.0236117230273,0.0138892481337,0.0152781725471,0.00625016186017,0.0048612374468,0.0048612374468,0.00416677324012,0.00277784962674,0.000694462606686,0.0,0.000694462606686,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0])

    # Creating weights for histo: y9_sdETA_3
    y9_sdETA_3_weights = numpy.array([0.319106717228,0.321477477802,0.314839316195,0.359409926982,0.353720045605,0.361780687556,0.371263809851,0.374108730539,0.393074975129,0.409670499146,0.3921266549,0.389281734211,0.386436813523,0.364625648244,0.332857200556,0.339021242048,0.338547081933,0.319106717228,0.284493348851,0.274536066441,0.257940622425,0.24845754013,0.243241818868,0.228068815196,0.214792491983,0.207205970147,0.187291445327,0.167376920507,0.160738758901,0.135608512819,0.141298354196,0.139401753737,0.116168108114,0.0867704609996,0.0834513801963,0.0924603423766,0.0606918946882,0.0606918946882,0.053579572967,0.0606918946882,0.0374582890654,0.0450447709014,0.0398290696392,0.0355616686064,0.0222853133933,0.0213370011638,0.0146988235573,0.0137505113278,0.0151729796721,0.0118538908688,0.0109055786393,0.00663817760653,0.00521571326227,0.00426740103277,0.00331908920326,0.00142246674426,0.000948311029504,0.00142246674426,0.000948311029504,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0])

    # Creating weights for histo: y9_sdETA_4
    y9_sdETA_4_weights = numpy.array([0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0])

    # Creating weights for histo: y9_sdETA_5
    y9_sdETA_5_weights = numpy.array([0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,1.0529581672,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,1.0521138287,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0])

    # Creating weights for histo: y9_sdETA_6
    y9_sdETA_6_weights = numpy.array([0.0,0.0,0.0,0.230176951761,0.461026502416,0.229973220081,1.15216720785,0.461243606149,0.230587834986,0.461093746935,0.46101459053,0.921661833857,1.38198515073,2.07188010341,0.460679136442,0.459984020241,0.230176951761,0.459886419625,0.0,0.230663840506,0.230635905211,0.690879412445,0.0,0.230455997303,0.229943171387,0.0,0.0,0.230829223597,0.0,0.0,0.230610352294,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0])

    # Creating weights for histo: y9_sdETA_7
    y9_sdETA_7_weights = numpy.array([0.886306304061,0.80349463011,0.886186663476,1.13549956255,1.27349824553,1.38428735101,0.830111390424,1.05189541398,0.969250698275,0.581783698872,0.858285017133,0.83058302823,0.609204474695,0.498561553845,0.526425884636,0.277003424023,0.221645763666,0.249321246986,0.110606990204,0.110763638585,0.138492863994,0.166119721687,0.0830406452575,0.0831029276072,0.0553913982331,0.0552998404862,0.0277194194976,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0])

    # Creating weights for histo: y9_sdETA_8
    y9_sdETA_8_weights = numpy.array([0.665590127196,0.604992804098,0.554361404635,0.494133326914,0.433409058651,0.534416874986,0.352980679834,0.332704587861,0.302475740085,0.211846358489,0.191624454869,0.23190066051,0.221714099869,0.151221122019,0.0604935460322,0.110903653131,0.0402984635222,0.0503794691378,0.0504115816528,0.0302025485245,0.0100784752077,0.0201623813869,0.0403268016637,0.0,0.020180561488,0.0201221011763,0.0,0.0,0.0201023919079,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0])

    # Creating weights for histo: y9_sdETA_9
    y9_sdETA_9_weights = numpy.array([0.447013607192,0.424307486026,0.342306405295,0.265957981821,0.257435366571,0.240524448335,0.220715793975,0.189554963932,0.132959638556,0.104703085193,0.113165873583,0.0707450512374,0.0848773484378,0.0509023475072,0.0424307486026,0.0254694680766,0.0367668723656,0.0113259057285,0.0113262404511,0.01696860595,0.0113230163412,0.00566530361742,0.00283437043628,0.0,0.00283098627508,0.0,0.00282138473722,0.00282581731125,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0])

    # Creating weights for histo: y9_sdETA_10
    y9_sdETA_10_weights = numpy.array([0.0670638828663,0.0608414975277,0.060959157152,0.0229095776262,0.0533307517085,0.0350274083715,0.0258862751492,0.0182509582808,0.0121825382222,0.0106522329768,0.00610517702451,0.0106412408576,0.00305897892201,0.00459282730644,0.0,0.00152036578947,0.00151207326108,0.00151823565288,0.0,0.00153762426714,0.0,0.0,0.00152202216856,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0])

    # Creating weights for histo: y9_sdETA_11
    y9_sdETA_11_weights = numpy.array([0.0211291962968,0.0126353366386,0.00848508299271,0.00812712674959,0.00415275686336,0.00234700049913,0.00487592868019,0.00198571536192,0.00162497977721,0.00108367672042,0.00072249363746,0.000180606252698,0.000541865703048,0.000361161016139,0.000181227743822,0.000360674698756,0.000181227743822,0.0,0.000180814212301,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0])

    # Creating weights for histo: y9_sdETA_12
    y9_sdETA_12_weights = numpy.array([0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0121753363378,0.0,0.012124083239,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0])

    # Creating weights for histo: y9_sdETA_13
    y9_sdETA_13_weights = numpy.array([0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0401758728513,0.0300707535921,0.0201017147025,0.0200553904374,0.0301559479279,0.030147101237,0.0200884384681,0.0401541383374,0.0301172224785,0.0100696705151,0.0,0.0200768976892,0.0301238006812,0.050193256572,0.0300999381684,0.050153010533,0.0301384156956,0.0200591464589,0.0200959546432,0.0100696705151,0.020073844114,0.020068687332,0.0200509278376,0.0301524604888,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0])

    # Creating weights for histo: y9_sdETA_14
    y9_sdETA_14_weights = numpy.array([0.0110169886982,0.0,0.0164636329441,0.0275292843155,0.0385246271027,0.0714312627476,0.0769805463135,0.082542221026,0.0935202893361,0.154018010648,0.120903219992,0.126519456376,0.159578791573,0.187068204835,0.15950436344,0.21993480692,0.187037166028,0.148456092175,0.104525943182,0.137508331391,0.148519835483,0.159553359252,0.131996058757,0.109987513681,0.0715245823004,0.088026217469,0.126551267089,0.0880027758573,0.071543270587,0.0495121370602,0.0384884977695,0.0220141678127,0.0439968174238,0.0165119259142,0.0109933358277,0.0164736108641,0.0,0.00551642874557,0.00550890467889,0.0055098553439,0.0,0.00551434459535,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0])

    # Creating weights for histo: y9_sdETA_15
    y9_sdETA_15_weights = numpy.array([0.0809195939019,0.0868508146956,0.130261631883,0.135181361761,0.156935611317,0.136182190637,0.206251595441,0.165797169593,0.146030228125,0.172695750076,0.177672798441,0.149977307376,0.15888540185,0.160839601497,0.134219212844,0.14309480012,0.126325094423,0.0966898736234,0.118433581388,0.103635751878,0.0838830398244,0.0750138658058,0.0621590528261,0.0552594702718,0.0493440421241,0.0375018864711,0.0295988295729,0.0197392281805,0.0217156457557,0.0177637926354,0.0128272399818,0.0118411816396,0.00493119357551,0.000986289620331,0.0019723455576,0.0029577244954,0.0,0.0,0.000988437660678,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0])

    # Creating weights for histo: y9_sdETA_16
    y9_sdETA_16_weights = numpy.array([0.073092967269,0.0821753037345,0.0849525626579,0.0917418090191,0.0915007448811,0.0887457718871,0.0872212862793,0.0872269677909,0.0854471342447,0.0920168822057,0.0839258094778,0.0738501287209,0.0776328151504,0.0604980562404,0.0627554168385,0.0534466601311,0.0408341444185,0.037058523869,0.0315089193295,0.0244464442725,0.023694832297,0.0199148545882,0.0168850604748,0.0113390768987,0.00655471196048,0.00857246880912,0.00277389002703,0.00378108400318,0.00453697911823,0.00201537021365,0.00075551581413,0.000252127161484,0.0,0.000252078708593,0.0,0.000252302008004,0.000503980090005,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0])

    # Creating weights for histo: y9_sdETA_17
    y9_sdETA_17_weights = numpy.array([0.0575333582738,0.0606918513993,0.0598524939336,0.065268986014,0.0629982098376,0.0669901217203,0.0534895076863,0.0530065227206,0.0403558638477,0.04009485061,0.035808392782,0.0337898117609,0.0311987952269,0.0191711108763,0.0197635420408,0.0174658017283,0.0131686162332,0.0111770393396,0.0114566085419,0.00829432024186,0.00400639873218,0.00428896628247,0.0022897430517,0.00143174164047,0.000574129244645,0.000575090435615,0.00171748450024,0.000287793413833,0.000284795365815,0.0,0.000285189280151,0.0,0.000286335830812,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0])

    # Creating weights for histo: y9_sdETA_18
    y9_sdETA_18_weights = numpy.array([0.0142331036109,0.0142462803926,0.0129083886027,0.0120075644594,0.0116170598042,0.00950119305213,0.00857375968893,0.00673508732785,0.00550816298371,0.00477337299559,0.0034112847955,0.00326204014008,0.00209396119074,0.00202940543809,0.00142524287192,0.00107998520641,0.000775984195315,0.000798993270244,0.000237621296806,0.000236198631872,0.000216032916998,0.000108002963195,0.000129608568375,2.16093059116e-05,0.000107999316948,2.16148926323e-05,2.15601444455e-05,6.47894896459e-05,0.0,2.16186855673e-05,2.15990545095e-05,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0])

    # Creating weights for histo: y9_sdETA_19
    y9_sdETA_19_weights = numpy.array([0.00433236325249,0.00360634562356,0.00320768960819,0.00258161336288,0.00209537663081,0.00147283450841,0.00147418405202,0.00101770337531,0.00110572685996,0.000482710035668,0.000424935577459,0.000340758277254,0.000253986603473,0.000141956451962,0.00014215594261,8.38729622278e-05,8.52802097483e-05,5.67644393303e-05,2.8437866431e-05,2.83770731005e-05,2.82249486707e-05,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0])

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
