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
    xBinning = numpy.linspace(2.0,15.0,101,endpoint=True)

    # Creating data sequence: middle of each bin
    xData = numpy.array([2.065,2.195,2.325,2.455,2.585,2.715,2.845,2.975,3.105,3.235,3.365,3.495,3.625,3.755,3.885,4.015,4.145,4.275,4.405,4.535,4.665,4.795,4.925,5.055,5.185,5.315,5.445,5.575,5.705,5.835,5.965,6.095,6.225,6.355,6.485,6.615,6.745,6.875,7.005,7.135,7.265,7.395,7.525,7.655,7.785,7.915,8.045,8.175,8.305,8.435,8.565,8.695,8.825,8.955,9.085,9.215,9.345,9.475,9.605,9.735,9.865,9.995,10.125,10.255,10.385,10.515,10.645,10.775,10.905,11.035,11.165,11.295,11.425,11.555,11.685,11.815,11.945,12.075,12.205,12.335,12.465,12.595,12.725,12.855,12.985,13.115,13.245,13.375,13.505,13.635,13.765,13.895,14.025,14.155,14.285,14.415,14.545,14.675,14.805,14.935])

    # Creating weights for histo: y9_sdETA_0
    y9_sdETA_0_weights = numpy.array([1.83625218913,1.84863538771,1.87693978446,1.6858846064,1.57620501899,1.51251982631,1.65581140985,1.4612182322,1.54436262265,1.47537023057,1.49659862814,1.52844102448,1.52667222468,1.43645183504,1.39576383972,1.28608425231,1.29846745089,1.27370105373,1.20647786145,1.22063025983,1.04018908055,1.10741227283,0.967659088878,0.866824300457,0.880976698832,0.76952751163,0.815522306348,0.681076321788,0.688152320975,0.603239130726,0.587317532555,0.571396334383,0.500635142509,0.474099945556,0.389186395307,0.336115521402,0.337884561199,0.290120766684,0.279506607903,0.2246666942,0.210514455825,0.178671939482,0.153905542326,0.136215224358,0.09552758903,0.113217866998,0.0778372710615,0.113217866998,0.0742992314678,0.047763794515,0.0459947547181,0.0406876753276,0.0318425243433,0.0229973773591,0.0194593217654,0.0176902899685,0.00707611518741,0.00530708739055,0.00884514698426,0.00530708739055,0.00176902899685,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0])

    # Creating weights for histo: y9_sdETA_1
    y9_sdETA_1_weights = numpy.array([0.916842127511,0.91468226388,0.877349876327,0.866695641535,0.845285653564,0.89439936981,0.832425592091,0.911504018951,0.84950346276,0.863374311636,0.900778241674,0.874099689234,0.878407825815,0.873033346494,0.834587054437,0.847377172139,0.854857958147,0.838807661385,0.781116840489,0.749102977241,0.738325241734,0.706284999692,0.641138172867,0.653867539409,0.572777130032,0.589843010341,0.5321174174,0.48511320527,0.421035918616,0.409289761647,0.405006405146,0.346220024998,0.318396433084,0.288522169758,0.25858659572,0.234015389132,0.213703318517,0.188045985094,0.168854973232,0.152782534271,0.146387395484,0.0929616258066,0.125027127542,0.092975214882,0.0812221035044,0.0705206666591,0.0427343647673,0.0523410816855,0.0320553259158,0.0352588105537,0.0267148712418,0.0309902381666,0.0213680656736,0.0117598059956,0.0128219321257,0.0106857294728,0.012822263859,0.00534045067713,0.00320688030811,0.00427273304224,0.00106958133661,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0])

    # Creating weights for histo: y9_sdETA_2
    y9_sdETA_2_weights = numpy.array([0.480568113724,0.485429314874,0.474317712245,0.490290516025,0.499318518161,0.52640252457,0.568764534595,0.531263725721,0.543764128679,0.540986128021,0.582654137882,0.538902927528,0.575709336238,0.570153734924,0.571542535252,0.563903333445,0.522235723584,0.543069728515,0.531263725721,0.518068922598,0.527096924735,0.463206509615,0.457650908301,0.419455299262,0.415288498276,0.391676812688,0.338203200034,0.339592120363,0.303480071817,0.292368669187,0.23681169604,0.25764554097,0.217366731439,0.168754359935,0.190282685029,0.157642957305,0.146531554676,0.132642311389,0.100002583665,0.111808466459,0.0923635018573,0.0875022607069,0.0777797784062,0.065279455448,0.0541680528186,0.0534736126542,0.034723120217,0.0340286560527,0.0291674189023,0.0243061857519,0.0243061857519,0.0187504844372,0.0173615601085,0.00555569731473,0.00694462564341,0.00416677298604,0.00486123715039,0.00277784945736,0.000694462564341,0.0,0.000694462564341,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0])

    # Creating weights for histo: y9_sdETA_3
    y9_sdETA_3_weights = numpy.array([0.270268676245,0.276432717983,0.292079842398,0.287812441194,0.326219052029,0.346133577647,0.332857213901,0.341866176443,0.37932446701,0.387385109284,0.380746947411,0.390230070086,0.405402914367,0.421998519049,0.415360117176,0.412989716507,0.404928914233,0.382643547946,0.349452658583,0.362254862194,0.345659417513,0.325270731761,0.290657361996,0.281174279321,0.270268676245,0.270742836378,0.238026107149,0.2204823422,0.231387945276,0.205309377919,0.192033014174,0.158367964677,0.157893804543,0.146039921199,0.142246680129,0.12470291518,0.0934086663512,0.0881929448798,0.09577942702,0.0611660572553,0.0644851781917,0.0606918971216,0.055950375784,0.0426740120386,0.0483638536438,0.0374582905672,0.0270268676245,0.0218111581531,0.0222853142868,0.0170696008154,0.0137505118791,0.0137505118791,0.0123280434778,0.00806064627396,0.0037932446701,0.00474155733762,0.00426740120386,0.00142246680129,0.000948311067525,0.00189662253505,0.000474155733762,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0])

    # Creating weights for histo: y9_sdETA_4
    y9_sdETA_4_weights = numpy.array([0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0])

    # Creating weights for histo: y9_sdETA_5
    y9_sdETA_5_weights = numpy.array([0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,1.0529581672,0.0,0.0,0.0,0.0,0.0,0.0,0.0,1.0521138287,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0])

    # Creating weights for histo: y9_sdETA_6
    y9_sdETA_6_weights = numpy.array([0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.230176952104,0.230513213126,0.230513213126,0.690779891586,0.922114871163,0.461076840429,0.461093747622,0.230350865644,1.15232590663,1.38198515279,2.0718801065,0.460679137129,0.459984020926,0.460120046982,0.229943171729,0.0,0.230663840849,0.460991535953,0.460523898353,0.0,0.230455997646,0.229943171729,0.0,0.0,0.230829223941,0.0,0.230610352637,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0])

    # Creating weights for histo: y9_sdETA_7
    y9_sdETA_7_weights = numpy.array([0.221683504684,0.609043462463,0.747717049454,0.913816594462,1.07987074499,0.831168255319,1.08033584603,1.05246440662,1.19057094735,1.41212984805,1.02390397138,1.02418903331,1.07964146441,0.720399961243,0.858414174224,0.858272989706,0.609150024074,0.526228933371,0.581751379684,0.221683081515,0.277069959916,0.221632570542,0.138291965627,0.110697163239,0.138637156001,0.138291965627,0.0830621213403,0.0554186545345,0.110691969803,0.0,0.0277196025764,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0])

    # Creating weights for histo: y9_sdETA_8
    y9_sdETA_8_weights = numpy.array([0.725924270072,0.705428134528,0.84682082419,0.716004807997,0.594843488107,0.756168131012,0.604999194315,0.524414154369,0.443604703736,0.544414984336,0.463873455061,0.31266822913,0.383084515735,0.221902966502,0.201752064164,0.21175781937,0.251962347051,0.15122883214,0.0907180502114,0.0806878999013,0.0403005181691,0.0604666401399,0.0503821652094,0.0201514727713,0.0201578021479,0.0504134540547,0.0,0.0201815904089,0.0100788130817,0.0100443140349,0.0,0.0100119389399,0.0100914779032,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0])

    # Creating weights for histo: y9_sdETA_9
    y9_sdETA_9_weights = numpy.array([0.659185425098,0.594187238473,0.611085758956,0.531915376754,0.492325568676,0.452610717471,0.384723880727,0.322533931874,0.237658543596,0.288616695609,0.257487844113,0.195233257583,0.149937443084,0.124521485,0.113159912632,0.0820679969525,0.0848794281328,0.0509035947346,0.0452638419333,0.0254632128429,0.0367730519843,0.0113301846199,0.0197965199809,0.0113257330846,0.0113275837229,0.0,0.00283443988503,0.00283105564091,0.0,0.00282145386779,0.00282588655043,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0])

    # Creating weights for histo: y9_sdETA_10
    y9_sdETA_10_weights = numpy.array([0.146207140434,0.130996047101,0.105137767423,0.105073428795,0.0868661286625,0.068457470483,0.0624659667242,0.0473130558348,0.0366048393678,0.0502411310394,0.0259137562363,0.0197699312177,0.0167550313589,0.0121722068049,0.00610250532167,0.0121668895629,0.00305941699056,0.00459348503349,0.0,0.00152058351716,0.00151228980122,0.00151845307553,0.0,0.00153784446638,0.0,0.0,0.00152224013346,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0])

    # Creating weights for histo: y9_sdETA_11
    y9_sdETA_11_weights = numpy.array([0.0550716318208,0.0462233371756,0.0375578430986,0.0317709775239,0.0241933326512,0.0171553201394,0.011011195281,0.00884972731792,0.00613879469963,0.00234657351681,0.0048755355158,0.00252912182673,0.00216592927517,0.00108380459975,0.000903277821868,0.000180614086187,0.000541889205552,0.000361176680884,0.000181235604268,0.000360690342408,0.000181235604268,0.0,0.00018082205481,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0])

    # Creating weights for histo: y9_sdETA_12
    y9_sdETA_12_weights = numpy.array([0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0121753363378,0.0,0.012124083239,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0])

    # Creating weights for histo: y9_sdETA_13
    y9_sdETA_13_weights = numpy.array([0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0401758729938,0.0300707536987,0.0301386885169,0.0100184167655,0.0301559480349,0.030147101344,0.0301194125649,0.0501794144266,0.0100609850093,0.0100696705508,0.010058480995,0.0200730714943,0.0401416845208,0.0501877198207,0.050131276197,0.0401930705313,0.02005914653,0.0100262841637,0.0201393411016,0.0200738441852,0.0200686874032,0.0300916576733,0.0201117308312,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0])

    # Creating weights for histo: y9_sdETA_14
    y9_sdETA_14_weights = numpy.array([0.0,0.0,0.0,0.0,0.0055005599861,0.00551642877911,0.0,0.0274856229574,0.0275147929354,0.0715134103899,0.0769069311826,0.0880229272406,0.0880452719312,0.154023821204,0.120909070973,0.137487571978,0.176101959968,0.198054724705,0.170486861098,0.225479988559,0.181531354146,0.142944145425,0.110025906591,0.181555852052,0.142968115184,0.154055469411,0.126460751548,0.0990229340409,0.082494241383,0.0990863117088,0.115516728355,0.0935475504271,0.0495273317508,0.0549820769958,0.0164977391674,0.0440160341252,0.0220091586732,0.0109933358945,0.0164736109642,0.0,0.00551642877911,0.00550890471238,0.00550985537739,0.00551434462887,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0])

    # Creating weights for histo: y9_sdETA_15
    y9_sdETA_15_weights = numpy.array([0.0147974058684,0.0434205352634,0.0542829240594,0.0710526704412,0.071055075407,0.0838700559388,0.106598946837,0.146036778564,0.16678818633,0.147051553885,0.18157175162,0.193432361556,0.158874486023,0.173655365768,0.185578264317,0.157877186787,0.167755864404,0.166767383376,0.146063714181,0.146046198013,0.125336075494,0.102629671026,0.131257261633,0.0937642055023,0.090790024376,0.0680980096206,0.0582093914784,0.0552586988514,0.0444134253953,0.0355302513066,0.0305896058,0.0217145845453,0.0157910816225,0.0167748809837,0.0108563162574,0.0069027288407,0.0019719196443,0.00197234091415,0.00295771753209,0.0,0.000988435333619,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0])

    # Creating weights for histo: y9_sdETA_16
    y9_sdETA_16_weights = numpy.array([0.0529420344005,0.0655388556212,0.0746055917205,0.0690717814872,0.0811707922479,0.0821708543319,0.082938335464,0.0940123175977,0.0940146382058,0.0927693518564,0.0957983456581,0.0932779651476,0.0902413293432,0.0952892922516,0.0856892563917,0.0793927262741,0.0814160165132,0.0627670092096,0.0672927552618,0.0544517500483,0.0405853961239,0.0388190292161,0.0294929931627,0.0257092135561,0.0226854771322,0.0196628850083,0.0148660679172,0.00957656971019,0.0095821911834,0.00428650335434,0.00327587250058,0.00554602943552,0.00226743982288,0.0012594120513,0.000252126154137,0.0,0.0,0.000252077701439,0.000252300999958,0.000503978076407,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0])

    # Creating weights for histo: y9_sdETA_17
    y9_sdETA_17_weights = numpy.array([0.0500945737966,0.0587269292573,0.0589836132203,0.0669867660429,0.0606630465813,0.061269714139,0.0647213606061,0.0644220959389,0.0664096220399,0.069008384701,0.0635241219767,0.0569905983176,0.0432311721536,0.0415274640921,0.0380868052262,0.0366566074543,0.0329217728103,0.0197414102303,0.0217620591001,0.0166100038512,0.0151739773517,0.0106088939603,0.0105863488821,0.00801620397339,0.00371691555594,0.00429195001951,0.00171626032126,0.000573756542556,0.00114921911267,0.00085988507751,0.000857597676875,0.000572588397575,0.0,0.000285189040056,0.0,0.000286335589752,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0])

    # Creating weights for histo: y9_sdETA_18
    y9_sdETA_18_weights = numpy.array([0.0154157575643,0.0160200454505,0.0173619337037,0.0158482132106,0.0153303820873,0.0150514690248,0.0144424410835,0.0131050372326,0.0123285776332,0.0109251105727,0.00902732825946,0.00762239433835,0.00613260881901,0.00494626646211,0.00379997987674,0.00349944738479,0.00222358043094,0.00215895264913,0.00146835384801,0.00114316971619,0.000756038385492,0.000712624760547,0.000302530314156,0.000279319131379,0.000151181986083,0.000108015967205,6.48095887048e-05,2.16295927404e-05,8.63682063481e-05,2.16145930432e-05,4.31515179139e-05,4.31969486817e-05,2.16183859255e-05,2.15987551399e-05,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0])

    # Creating weights for histo: y9_sdETA_19
    y9_sdETA_19_weights = numpy.array([0.00632607866534,0.00683612652883,0.00569980381019,0.00452647837625,0.00552498584435,0.00369222494408,0.00382897682138,0.00278148735233,0.00263666067017,0.00149880378317,0.00167256283125,0.00133394959483,0.00113100020886,0.000510242716233,0.000510091527133,0.000340646417926,0.000282397475669,0.000141942891177,0.000142142362768,0.000112278921499,5.68580767979e-05,5.67590167493e-05,2.84351498247e-05,2.83743623016e-05,2.82222524039e-05,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0])

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
