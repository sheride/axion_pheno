def selection_14():

    # Library import
    import numpy
    import matplotlib
    import matplotlib.pyplot   as plt
    import matplotlib.gridspec as gridspec

    # Library version
    matplotlib_version = matplotlib.__version__
    numpy_version      = numpy.__version__

    # Histo binning
    xBinning = numpy.linspace(0.0,8000.0,81,endpoint=True)

    # Creating data sequence: middle of each bin
    xData = numpy.array([50.0,150.0,250.0,350.0,450.0,550.0,650.0,750.0,850.0,950.0,1050.0,1150.0,1250.0,1350.0,1450.0,1550.0,1650.0,1750.0,1850.0,1950.0,2050.0,2150.0,2250.0,2350.0,2450.0,2550.0,2650.0,2750.0,2850.0,2950.0,3050.0,3150.0,3250.0,3350.0,3450.0,3550.0,3650.0,3750.0,3850.0,3950.0,4050.0,4150.0,4250.0,4350.0,4450.0,4550.0,4650.0,4750.0,4850.0,4950.0,5050.0,5150.0,5250.0,5350.0,5450.0,5550.0,5650.0,5750.0,5850.0,5950.0,6050.0,6150.0,6250.0,6350.0,6450.0,6550.0,6650.0,6750.0,6850.0,6950.0,7050.0,7150.0,7250.0,7350.0,7450.0,7550.0,7650.0,7750.0,7850.0,7950.0])

    # Creating weights for histo: y15_TET_0
    y15_TET_0_weights = numpy.array([0.0,0.0,0.0,0.0,0.0,0.0,0.544861149246,1.85571142714,2.98258332217,3.66896645823,4.22797960616,4.52517557848,4.52694757831,4.46679958392,4.2350556055,4.02984762462,3.81225804489,3.48321847554,3.2302472991,2.91712892827,2.71545974705,2.43772217293,2.12283500226,1.89463022351,1.75133903686,1.55143865548,1.3515382741,1.21532308679,1.07556989981,0.925202313817,0.773065927989,0.737685131284,0.610315143149,0.597931944302,0.479406755343,0.408645561935,0.344960687867,0.283044653634,0.265354375282,0.233511858248,0.205207380885,0.130908147806,0.134446227476,0.118524948959,0.113217869454,0.0955275911016,0.0796063125847,0.0778372727494,0.0583779545621,0.0459947557156,0.0513018352212,0.0371496125395,0.0371496125395,0.0106141750113,0.0176902903521,0.0194593221874,0.00884514717607,0.0176902903521,0.0106141750113,0.0123832028465,0.0106141750113,0.00530708750564,0.0,0.00176902903521,0.00176902903521,0.00176902903521,0.00353805847043,0.00353805847043,0.00176902903521,0.0,0.0,0.0,0.0,0.00176902903521,0.0,0.0,0.0,0.0,0.0,0.0])

    # Creating weights for histo: y15_TET_1
    y15_TET_1_weights = numpy.array([0.0,0.0,0.0,0.0,0.0,0.0,0.354740947551,1.22572542478,1.92344559003,2.46624583778,2.67243842102,2.83708697152,2.77511444816,2.7825876818,2.605162132,2.54963566234,2.35090632072,2.14574211646,2.0259913212,1.80703173068,1.5953611209,1.50773947488,1.31862685561,1.13912456381,1.04397492786,0.96813507568,0.820699183209,0.757591166386,0.661435133913,0.580229565526,0.54920073783,0.449890423622,0.362243957417,0.379346703199,0.315264983745,0.260742432594,0.226532184829,0.18485258033,0.160251341077,0.133564686745,0.126098607395,0.09832146367,0.0897440715522,0.0801227128998,0.0512950478736,0.0534386964615,0.0427378796098,0.0331258575035,0.0363398755468,0.0149509916645,0.0267038366147,0.0181680752604,0.0138964136018,0.0138897269402,0.00962069518204,0.0149596447562,0.00961324113309,0.00427462329408,0.00641379545576,0.00533785045166,0.00534344198757,0.00213731084768,0.00320689812756,0.00747592748764,0.00320689812756,0.00213917495944,0.0,0.0,0.0,0.0010677235678,0.00106958727988,0.0,0.0,0.00106958727988,0.0,0.00213468134698,0.0010677235678,0.0,0.00106695777918,0.0])

    # Creating weights for histo: y15_TET_2
    y15_TET_2_weights = numpy.array([0.0,0.0,0.0,0.0,0.0,0.0,0.254173223525,0.894467423552,1.30628392648,1.67643241899,1.80976885231,1.92157768025,1.87852086949,1.80074085005,1.76324004068,1.62573640632,1.5000387749,1.40698075164,1.28058872005,1.17364149332,1.06599986642,1.00072025011,0.850021812443,0.784048195955,0.71112937773,0.617376954299,0.579181744753,0.473623318371,0.422927705701,0.369454012337,0.352786888171,0.294452073592,0.266673546649,0.218755654673,0.204171931028,0.161809760441,0.136114634019,0.115280748812,0.0979191844727,0.0902801025634,0.0847244211749,0.0666683766622,0.063890535968,0.0465289716288,0.0506957726702,0.0416677304139,0.0284729591162,0.027084034769,0.0166670961656,0.0243061860748,0.0187504846863,0.0118058629506,0.0152781718184,0.0118058629506,0.00763908590921,0.00833355008278,0.00694462573565,0.00902801025634,0.00416677304139,0.00208338732069,0.00347231206782,0.00416677304139,0.00138892474713,0.00138892474713,0.000694462573565,0.0,0.0,0.000694462573565,0.0,0.0,0.000694462573565,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0])

    # Creating weights for histo: y15_TET_3
    y15_TET_3_weights = numpy.array([0.0,0.0,0.0,0.0,0.0,0.0,0.189188084465,0.612134943872,0.968225827564,1.12943866545,1.27595269989,1.36556792095,1.31104030814,1.28306510156,1.18064747749,1.09435105721,1.0734882523,1.01990863971,0.870075404496,0.785675784659,0.753433377081,0.644851751561,0.577047335625,0.537692526375,0.464672509213,0.418205298292,0.355616683581,0.323374116003,0.302037110988,0.24656089795,0.223801412601,0.199619486917,0.176385881456,0.153626396107,0.128021990089,0.11521978708,0.10858162552,0.0938828220655,0.0687525761591,0.0692266962705,0.0564244932616,0.0502604918128,0.0436223302527,0.0360358244696,0.0275010224636,0.0275010224636,0.0194403765691,0.016121287789,0.0180179122348,0.0170696000119,0.0146988234547,0.00853480200595,0.0090089541174,0.00616402144874,0.00711233367163,0.00711233367163,0.00663817756019,0.00616402144874,0.00284493346865,0.00142246673433,0.000948311022884,0.00237077775721,0.000474155711442,0.00237077775721,0.00142246673433,0.0,0.000474155711442,0.000948311022884,0.000474155711442,0.000948311022884,0.0,0.000474155711442,0.000474155711442,0.0,0.0,0.000474155711442,0.0,0.0,0.0,0.0])

    # Creating weights for histo: y15_TET_4
    y15_TET_4_weights = numpy.array([0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0])

    # Creating weights for histo: y15_TET_5
    y15_TET_5_weights = numpy.array([0.0,0.0,0.0,0.0,0.0,0.0,2.10674221742,0.0,1.0529581672,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0])

    # Creating weights for histo: y15_TET_6
    y15_TET_6_weights = numpy.array([0.0,0.0,0.0,0.0,0.0,0.0,0.922291234315,5.9893732087,6.44785017911,6.90932817631,2.30289651517,1.38211962742,0.691757427557,0.921287177588,0.0,0.0,0.230663838444,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0])

    # Creating weights for histo: y15_TET_7
    y15_TET_7_weights = numpy.array([0.0,0.0,0.0,0.0,0.0,0.0,0.0,1.02480538793,4.0143644543,5.76017818883,6.11889217752,5.45639499658,3.32312814542,1.8824628906,0.636878325356,0.609342527701,0.276736420637,0.166185067151,0.0554164756187,0.0276711184554,0.0554266700728,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0])

    # Creating weights for histo: y15_TET_8
    y15_TET_8_weights = numpy.array([0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.262053014808,0.836861009384,1.6130929675,1.98618730631,2.33920404419,1.71367090442,1.39142683552,0.745869494308,0.45382981459,0.181504558598,0.161339576688,0.0605296493316,0.0201641445096,0.04026564171,0.0100659249776,0.0100936805755,0.0100793415991,0.0,0.0100840868719,0.0100695112387,0.0,0.0100962898687,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0])

    # Creating weights for histo: y15_TET_9
    y15_TET_9_weights = numpy.array([0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0537387902378,0.271568679699,0.469674289648,0.661946261768,0.673391851033,0.797951364639,0.743985617088,0.707341956514,0.497924877183,0.387632241158,0.35359041399,0.19515208697,0.127322090807,0.0905388470611,0.0452874677719,0.022647400445,0.0141415874481,0.00566017457456,0.00848569116701,0.00282509261049,0.0,0.0,0.0,0.00283618462496,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.00282926625506,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0])

    # Creating weights for histo: y15_TET_10
    y15_TET_10_weights = numpy.array([0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0122131959683,0.0533809011079,0.057928748392,0.0852734273012,0.071508646067,0.0609432636597,0.0395203168971,0.0381299509455,0.04418689891,0.0670396717231,0.0624615677583,0.0685304364533,0.0516674231069,0.0335101657744,0.0289637716616,0.0183119550975,0.0137090763341,0.0122270424461,0.0045615590778,0.00153762418836,0.0,0.00152247103781,0.00151207318361,0.0,0.0,0.00152391121328,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0])

    # Creating weights for histo: y15_TET_11
    y15_TET_11_weights = numpy.array([0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.00036148614673,0.0061395762983,0.00902818540986,0.0120970261874,0.0128225741762,0.00884837736528,0.00938565258299,0.00667963586418,0.00704210947248,0.00505649181648,0.00505619913257,0.00451258884883,0.00451319732325,0.00505612211049,0.00812662271388,0.00451167228608,0.00342954441848,0.00379062392715,0.00252970624686,0.00306962871344,0.00180551615731,0.00180647546731,0.00198603896678,0.00144459646946,0.000903822908902,0.000181029499223,0.000180562475844,0.000180262012712,0.000180612155085,0.0,0.000180826160933,0.0,0.000180400883521,0.0,0.000180402770562,0.000180814222511,0.0,0.0,0.0,0.0,0.0,0.0,0.000180671924219,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0])

    # Creating weights for histo: y15_TET_12
    y15_TET_12_weights = numpy.array([0.0,0.0,0.0,0.0,0.0,0.0,0.0121704927804,0.0242994195771,0.0,0.0,0.0121313836425,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0])

    # Creating weights for histo: y15_TET_13
    y15_TET_13_weights = numpy.array([0.0,0.0,0.0,0.0,0.0,0.0,0.220879096585,0.441761829362,0.230809248523,0.120544402743,0.0502051137366,0.0501796190701,0.0100546543364,0.0301461580631,0.0100696701578,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0])

    # Creating weights for histo: y15_TET_14
    y15_TET_14_weights = numpy.array([0.0,0.0,0.0,0.0,0.0,0.0,0.511523586303,1.49042943279,1.7326214987,1.33674184095,0.781128930711,0.368558845657,0.203524457618,0.0824943211821,0.088002896721,0.0274928134005,0.0109788441534,0.0164797128056,0.0109794251154,0.0,0.01097305891,0.0,0.00549610720177,0.0,0.0,0.0,0.0,0.00551434453166,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0])

    # Creating weights for histo: y15_TET_15
    y15_TET_15_weights = numpy.array([0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.113479585678,0.851660557796,1.45754905412,1.57601715208,1.19016912473,0.704597347849,0.351305741328,0.186514844602,0.101653458637,0.0542766810795,0.0256513866999,0.0256610987768,0.00888189670997,0.0098734785138,0.00493571513984,0.00296082824184,0.00295823247586,0.000983907940375,0.00197239053751,0.00197611583847,0.00197004488857,0.000985427882409,0.000988893847272,0.0,0.0,0.000988893847272,0.000986793505433,0.0,0.0,0.000986289663888,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0])

    # Creating weights for histo: y15_TET_16
    y15_TET_16_weights = numpy.array([0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0249558108504,0.200386739847,0.477175816812,0.634998226694,0.604714165546,0.460040055538,0.299457871048,0.151753514435,0.073613354735,0.0418569416696,0.0254685313286,0.0138656108109,0.00781322776022,0.00529554559222,0.0042875052675,0.00126062996017,0.00151020479313,0.00151110343233,0.00100849644614,0.0,0.000757392806235,0.000252014242288,0.0,0.0,0.000251954546398,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0])

    # Creating weights for histo: y15_TET_17
    y15_TET_17_weights = numpy.array([0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.00801812572735,0.0466628789016,0.105404170251,0.181509314247,0.217618958912,0.244512708413,0.207214622284,0.160658450169,0.140588416228,0.093059275774,0.0601022252901,0.0495136787352,0.0289011328131,0.0177342120783,0.00688145100093,0.002861269556,0.0031526911598,0.001719701894,0.00143263334323,0.000286470880782,0.00171590172069,0.000286335810166,0.000286204338766,0.0,0.0,0.0,0.000286459983153,0.000286335810166,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0])

    # Creating weights for histo: y15_TET_18
    y15_TET_18_weights = numpy.array([0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.000626426043355,0.0049873112655,0.0119880423099,0.0188320601803,0.0220647094591,0.0228037701625,0.0226930122718,0.0201713308315,0.0204709307792,0.0196421011553,0.018414451759,0.0151183452122,0.0117275200696,0.00924385180025,0.00619748382353,0.00477259342927,0.00246060554857,0.00181450066917,0.000820755073179,0.000517093541757,0.000324162156062,8.62982383433e-05,0.000108119684464,8.63523452933e-05,4.3290757001e-05,4.31203054395e-05,4.31063072046e-05,0.0,0.0,0.0,0.0,0.0,0.0,2.15834425975e-05,0.0,0.0,0.0,2.1557030359e-05,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0])

    # Creating weights for histo: y15_TET_19
    y15_TET_19_weights = numpy.array([0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.000767829159296,0.00155644449951,0.00298045964124,0.00325630512169,0.00314158945303,0.00388401968339,0.00249366144214,0.00272132972823,0.00266693209702,0.00139088997869,0.00249683404317,0.00190166389217,0.00278036892228,0.00227127488323,0.00223838736821,0.00187379669151,0.00133237138233,0.00101617133761,0.00079499411006,0.00067866763343,0.000510093348965,0.00027968453564,0.000368942011894,0.000198966346776,8.51547654382e-05,2.84059932703e-05,0.000142007969057,0.000255665301978,0.000111852678435,2.84166874311e-05,0.0,0.0,2.84378678106e-05,2.84378678106e-05,5.68345928082e-05,0.0,0.0,0.0,0.0,0.0,0.0,2.79811974389e-05,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0])

    # Creating a new Canvas
    fig   = plt.figure(figsize=(12,6),dpi=80)
    frame = gridspec.GridSpec(1,1,right=0.7)
    pad   = fig.add_subplot(frame[0])

    # Creating a new Stack
    pad.hist(x=xData, bins=xBinning, weights=y15_TET_0_weights+y15_TET_1_weights+y15_TET_2_weights+y15_TET_3_weights+y15_TET_4_weights+y15_TET_5_weights+y15_TET_6_weights+y15_TET_7_weights+y15_TET_8_weights+y15_TET_9_weights+y15_TET_10_weights+y15_TET_11_weights+y15_TET_12_weights+y15_TET_13_weights+y15_TET_14_weights+y15_TET_15_weights+y15_TET_16_weights+y15_TET_17_weights+y15_TET_18_weights+y15_TET_19_weights,\
             label="$bg\_vbf\_1600\_inf$", histtype="step", rwidth=1.0,\
             color=None, edgecolor="#ccc6aa", linewidth=1, linestyle="solid",\
             bottom=None, cumulative=False, normed=False, align="mid", orientation="vertical")

    pad.hist(x=xData, bins=xBinning, weights=y15_TET_0_weights+y15_TET_1_weights+y15_TET_2_weights+y15_TET_3_weights+y15_TET_4_weights+y15_TET_5_weights+y15_TET_6_weights+y15_TET_7_weights+y15_TET_8_weights+y15_TET_9_weights+y15_TET_10_weights+y15_TET_11_weights+y15_TET_12_weights+y15_TET_13_weights+y15_TET_14_weights+y15_TET_15_weights+y15_TET_16_weights+y15_TET_17_weights+y15_TET_18_weights,\
             label="$bg\_vbf\_1200\_1600$", histtype="step", rwidth=1.0,\
             color=None, edgecolor="#c1bfa8", linewidth=1, linestyle="solid",\
             bottom=None, cumulative=False, normed=False, align="mid", orientation="vertical")

    pad.hist(x=xData, bins=xBinning, weights=y15_TET_0_weights+y15_TET_1_weights+y15_TET_2_weights+y15_TET_3_weights+y15_TET_4_weights+y15_TET_5_weights+y15_TET_6_weights+y15_TET_7_weights+y15_TET_8_weights+y15_TET_9_weights+y15_TET_10_weights+y15_TET_11_weights+y15_TET_12_weights+y15_TET_13_weights+y15_TET_14_weights+y15_TET_15_weights+y15_TET_16_weights+y15_TET_17_weights,\
             label="$bg\_vbf\_800\_1200$", histtype="step", rwidth=1.0,\
             color=None, edgecolor="#bab5a3", linewidth=1, linestyle="solid",\
             bottom=None, cumulative=False, normed=False, align="mid", orientation="vertical")

    pad.hist(x=xData, bins=xBinning, weights=y15_TET_0_weights+y15_TET_1_weights+y15_TET_2_weights+y15_TET_3_weights+y15_TET_4_weights+y15_TET_5_weights+y15_TET_6_weights+y15_TET_7_weights+y15_TET_8_weights+y15_TET_9_weights+y15_TET_10_weights+y15_TET_11_weights+y15_TET_12_weights+y15_TET_13_weights+y15_TET_14_weights+y15_TET_15_weights+y15_TET_16_weights,\
             label="$bg\_vbf\_600\_800$", histtype="step", rwidth=1.0,\
             color=None, edgecolor="#b2a596", linewidth=1, linestyle="solid",\
             bottom=None, cumulative=False, normed=False, align="mid", orientation="vertical")

    pad.hist(x=xData, bins=xBinning, weights=y15_TET_0_weights+y15_TET_1_weights+y15_TET_2_weights+y15_TET_3_weights+y15_TET_4_weights+y15_TET_5_weights+y15_TET_6_weights+y15_TET_7_weights+y15_TET_8_weights+y15_TET_9_weights+y15_TET_10_weights+y15_TET_11_weights+y15_TET_12_weights+y15_TET_13_weights+y15_TET_14_weights+y15_TET_15_weights,\
             label="$bg\_vbf\_400\_600$", histtype="step", rwidth=1.0,\
             color=None, edgecolor="#b7a39b", linewidth=1, linestyle="solid",\
             bottom=None, cumulative=False, normed=False, align="mid", orientation="vertical")

    pad.hist(x=xData, bins=xBinning, weights=y15_TET_0_weights+y15_TET_1_weights+y15_TET_2_weights+y15_TET_3_weights+y15_TET_4_weights+y15_TET_5_weights+y15_TET_6_weights+y15_TET_7_weights+y15_TET_8_weights+y15_TET_9_weights+y15_TET_10_weights+y15_TET_11_weights+y15_TET_12_weights+y15_TET_13_weights+y15_TET_14_weights,\
             label="$bg\_vbf\_200\_400$", histtype="step", rwidth=1.0,\
             color=None, edgecolor="#ad998c", linewidth=1, linestyle="solid",\
             bottom=None, cumulative=False, normed=False, align="mid", orientation="vertical")

    pad.hist(x=xData, bins=xBinning, weights=y15_TET_0_weights+y15_TET_1_weights+y15_TET_2_weights+y15_TET_3_weights+y15_TET_4_weights+y15_TET_5_weights+y15_TET_6_weights+y15_TET_7_weights+y15_TET_8_weights+y15_TET_9_weights+y15_TET_10_weights+y15_TET_11_weights+y15_TET_12_weights+y15_TET_13_weights,\
             label="$bg\_vbf\_100\_200$", histtype="step", rwidth=1.0,\
             color=None, edgecolor="#9b8e82", linewidth=1, linestyle="solid",\
             bottom=None, cumulative=False, normed=False, align="mid", orientation="vertical")

    pad.hist(x=xData, bins=xBinning, weights=y15_TET_0_weights+y15_TET_1_weights+y15_TET_2_weights+y15_TET_3_weights+y15_TET_4_weights+y15_TET_5_weights+y15_TET_6_weights+y15_TET_7_weights+y15_TET_8_weights+y15_TET_9_weights+y15_TET_10_weights+y15_TET_11_weights+y15_TET_12_weights,\
             label="$bg\_vbf\_0\_100$", histtype="step", rwidth=1.0,\
             color=None, edgecolor="#876656", linewidth=1, linestyle="solid",\
             bottom=None, cumulative=False, normed=False, align="mid", orientation="vertical")

    pad.hist(x=xData, bins=xBinning, weights=y15_TET_0_weights+y15_TET_1_weights+y15_TET_2_weights+y15_TET_3_weights+y15_TET_4_weights+y15_TET_5_weights+y15_TET_6_weights+y15_TET_7_weights+y15_TET_8_weights+y15_TET_9_weights+y15_TET_10_weights+y15_TET_11_weights,\
             label="$bg\_dip\_1600\_inf$", histtype="step", rwidth=1.0,\
             color=None, edgecolor="#afcec6", linewidth=1, linestyle="solid",\
             bottom=None, cumulative=False, normed=False, align="mid", orientation="vertical")

    pad.hist(x=xData, bins=xBinning, weights=y15_TET_0_weights+y15_TET_1_weights+y15_TET_2_weights+y15_TET_3_weights+y15_TET_4_weights+y15_TET_5_weights+y15_TET_6_weights+y15_TET_7_weights+y15_TET_8_weights+y15_TET_9_weights+y15_TET_10_weights,\
             label="$bg\_dip\_1200\_1600$", histtype="step", rwidth=1.0,\
             color=None, edgecolor="#84c1a3", linewidth=1, linestyle="solid",\
             bottom=None, cumulative=False, normed=False, align="mid", orientation="vertical")

    pad.hist(x=xData, bins=xBinning, weights=y15_TET_0_weights+y15_TET_1_weights+y15_TET_2_weights+y15_TET_3_weights+y15_TET_4_weights+y15_TET_5_weights+y15_TET_6_weights+y15_TET_7_weights+y15_TET_8_weights+y15_TET_9_weights,\
             label="$bg\_dip\_800\_1200$", histtype="step", rwidth=1.0,\
             color=None, edgecolor="#89a8a0", linewidth=1, linestyle="solid",\
             bottom=None, cumulative=False, normed=False, align="mid", orientation="vertical")

    pad.hist(x=xData, bins=xBinning, weights=y15_TET_0_weights+y15_TET_1_weights+y15_TET_2_weights+y15_TET_3_weights+y15_TET_4_weights+y15_TET_5_weights+y15_TET_6_weights+y15_TET_7_weights+y15_TET_8_weights,\
             label="$bg\_dip\_600\_800$", histtype="step", rwidth=1.0,\
             color=None, edgecolor="#829e8c", linewidth=1, linestyle="solid",\
             bottom=None, cumulative=False, normed=False, align="mid", orientation="vertical")

    pad.hist(x=xData, bins=xBinning, weights=y15_TET_0_weights+y15_TET_1_weights+y15_TET_2_weights+y15_TET_3_weights+y15_TET_4_weights+y15_TET_5_weights+y15_TET_6_weights+y15_TET_7_weights,\
             label="$bg\_dip\_400\_600$", histtype="step", rwidth=1.0,\
             color=None, edgecolor="#adbcc6", linewidth=1, linestyle="solid",\
             bottom=None, cumulative=False, normed=False, align="mid", orientation="vertical")

    pad.hist(x=xData, bins=xBinning, weights=y15_TET_0_weights+y15_TET_1_weights+y15_TET_2_weights+y15_TET_3_weights+y15_TET_4_weights+y15_TET_5_weights+y15_TET_6_weights,\
             label="$bg\_dip\_200\_400$", histtype="step", rwidth=1.0,\
             color=None, edgecolor="#7a8e99", linewidth=1, linestyle="solid",\
             bottom=None, cumulative=False, normed=False, align="mid", orientation="vertical")

    pad.hist(x=xData, bins=xBinning, weights=y15_TET_0_weights+y15_TET_1_weights+y15_TET_2_weights+y15_TET_3_weights+y15_TET_4_weights+y15_TET_5_weights,\
             label="$bg\_dip\_100\_200$", histtype="step", rwidth=1.0,\
             color=None, edgecolor="#758991", linewidth=1, linestyle="solid",\
             bottom=None, cumulative=False, normed=False, align="mid", orientation="vertical")

    pad.hist(x=xData, bins=xBinning, weights=y15_TET_0_weights+y15_TET_1_weights+y15_TET_2_weights+y15_TET_3_weights+y15_TET_4_weights,\
             label="$bg\_dip\_0\_100$", histtype="step", rwidth=1.0,\
             color=None, edgecolor="#688296", linewidth=1, linestyle="solid",\
             bottom=None, cumulative=False, normed=False, align="mid", orientation="vertical")

    pad.hist(x=xData, bins=xBinning, weights=y15_TET_0_weights+y15_TET_1_weights+y15_TET_2_weights+y15_TET_3_weights,\
             label="$signal\_2pt4TeVL$", histtype="step", rwidth=1.0,\
             color=None, edgecolor="#6d7a84", linewidth=1, linestyle="solid",\
             bottom=None, cumulative=False, normed=False, align="mid", orientation="vertical")

    pad.hist(x=xData, bins=xBinning, weights=y15_TET_0_weights+y15_TET_1_weights+y15_TET_2_weights,\
             label="$signal\_2pt2TeVL$", histtype="step", rwidth=1.0,\
             color=None, edgecolor="#7c99d1", linewidth=1, linestyle="solid",\
             bottom=None, cumulative=False, normed=False, align="mid", orientation="vertical")

    pad.hist(x=xData, bins=xBinning, weights=y15_TET_0_weights+y15_TET_1_weights,\
             label="$signal\_2TeVL$", histtype="step", rwidth=1.0,\
             color=None, edgecolor="#7f7f9b", linewidth=1, linestyle="solid",\
             bottom=None, cumulative=False, normed=False, align="mid", orientation="vertical")

    pad.hist(x=xData, bins=xBinning, weights=y15_TET_0_weights,\
             label="$signal\_1pt8TeVL$", histtype="step", rwidth=1.0,\
             color=None, edgecolor="#aaa5bf", linewidth=1, linestyle="solid",\
             bottom=None, cumulative=False, normed=False, align="mid", orientation="vertical")


    # Axis
    plt.rc('text',usetex=False)
    plt.xlabel(r"TET",\
               fontsize=16,color="black")
    plt.ylabel(r"$\mathrm{Events}$ $(\mathcal{L}_{\mathrm{int}} = 40.0\ \mathrm{fb}^{-1})$ ",\
               fontsize=16,color="black")

    # Boundary of y-axis
    ymax=(y15_TET_0_weights+y15_TET_1_weights+y15_TET_2_weights+y15_TET_3_weights+y15_TET_4_weights+y15_TET_5_weights+y15_TET_6_weights+y15_TET_7_weights+y15_TET_8_weights+y15_TET_9_weights+y15_TET_10_weights+y15_TET_11_weights+y15_TET_12_weights+y15_TET_13_weights+y15_TET_14_weights+y15_TET_15_weights+y15_TET_16_weights+y15_TET_17_weights+y15_TET_18_weights+y15_TET_19_weights).max()*1.1
    ymin=0 # linear scale
    #ymin=min([x for x in (y15_TET_0_weights+y15_TET_1_weights+y15_TET_2_weights+y15_TET_3_weights+y15_TET_4_weights+y15_TET_5_weights+y15_TET_6_weights+y15_TET_7_weights+y15_TET_8_weights+y15_TET_9_weights+y15_TET_10_weights+y15_TET_11_weights+y15_TET_12_weights+y15_TET_13_weights+y15_TET_14_weights+y15_TET_15_weights+y15_TET_16_weights+y15_TET_17_weights+y15_TET_18_weights+y15_TET_19_weights) if x])/100. # log scale
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
    plt.savefig('../../HTML/MadAnalysis5job_0/selection_14.png')
    plt.savefig('../../PDF/MadAnalysis5job_0/selection_14.png')
    plt.savefig('../../DVI/MadAnalysis5job_0/selection_14.eps')

# Running!
if __name__ == '__main__':
    selection_14()
