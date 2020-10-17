def selection_12():

    # Library import
    import numpy
    import matplotlib
    import matplotlib.pyplot   as plt
    import matplotlib.gridspec as gridspec

    # Library version
    matplotlib_version = matplotlib.__version__
    numpy_version      = numpy.__version__

    # Histo binning
    xBinning = numpy.linspace(0.0,4000.0,81,endpoint=True)

    # Creating data sequence: middle of each bin
    xData = numpy.array([25.0,75.0,125.0,175.0,225.0,275.0,325.0,375.0,425.0,475.0,525.0,575.0,625.0,675.0,725.0,775.0,825.0,875.0,925.0,975.0,1025.0,1075.0,1125.0,1175.0,1225.0,1275.0,1325.0,1375.0,1425.0,1475.0,1525.0,1575.0,1625.0,1675.0,1725.0,1775.0,1825.0,1875.0,1925.0,1975.0,2025.0,2075.0,2125.0,2175.0,2225.0,2275.0,2325.0,2375.0,2425.0,2475.0,2525.0,2575.0,2625.0,2675.0,2725.0,2775.0,2825.0,2875.0,2925.0,2975.0,3025.0,3075.0,3125.0,3175.0,3225.0,3275.0,3325.0,3375.0,3425.0,3475.0,3525.0,3575.0,3625.0,3675.0,3725.0,3775.0,3825.0,3875.0,3925.0,3975.0])

    # Creating weights for histo: y13_THT_0
    y13_THT_0_weights = numpy.array([11.277559974,190.789812642,279.550834567,339.653669098,361.412667119,357.167067505,333.284969678,290.297703589,257.393736582,207.507131121,176.991373897,146.210266698,112.510249764,96.8543611882,76.4220530472,65.2771740611,56.7858248336,43.2527660649,33.8326769219,29.985045272,23.4838628634,20.9629960928,16.3192935153,13.5330737688,10.0834670826,9.68543611882,8.35866223953,6.23582643267,5.83779546888,3.58228467409,2.65354385858,3.05157572237,1.99015781894,1.45944916722,1.45944916722,0.928740215504,1.19409469136,0.928740215504,1.06141760343,0.530708651716,0.265354385858,0.663386039645,0.265354385858,0.398031563787,0.265354385858,0.265354385858,0.265354385858,0.0,0.265354385858,0.265354385858,0.0,0.132677177929,0.0,0.0,0.0,0.0,0.0,0.132677177929,0.0,0.0,0.132677177929,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0])

    # Creating weights for histo: y13_THT_1
    y13_THT_1_weights = numpy.array([7.21301404942,128.069196502,177.033638879,219.749969894,236.823942289,237.622627156,221.683732123,182.480427471,166.538744654,127.42965508,115.966171099,93.2907031401,79.3405765937,63.3138214289,49.6904350514,43.9979318576,36.4633335392,28.290572702,22.5218191442,19.2330684325,16.1077207791,12.902753441,9.61691041711,7.45283234054,7.05328007346,5.60980195964,3.92774656782,3.52576023637,3.52701923519,3.60603040373,2.40492664838,2.48447199214,0.961932649579,0.641277641634,1.20203151757,0.880957143118,0.160298816785,0.881458644313,0.320737442391,0.320737442391,0.2405181146,0.240460710249,0.160298816785,0.240378335755,0.0,0.0802192978149,0.0,0.0,0.0,0.0,0.16015903794,0.160101603613,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.160101603613,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0])

    # Creating weights for histo: y13_THT_2
    y13_THT_2_weights = numpy.array([4.68762102666,86.6168289705,126.149097629,150.160142887,163.493795808,163.545905819,146.722532135,124.482387264,108.856973841,89.6377396321,75.5227965407,61.2515834151,51.5638312933,43.2823594795,35.2613177228,30.677886719,22.4484979166,19.1671631979,14.4274561598,12.656576772,10.7294453499,8.28146281377,6.97934552859,5.83348327763,4.89595907229,4.9480450837,2.29172600192,1.77087908785,2.50006464755,1.45837111941,1.19794766237,0.833354882518,0.677100748296,1.19794766237,0.364592779852,0.416677291259,0.104169352815,0.520846914074,0.312507968444,0.104169352815,0.312507968444,0.104169352815,0.104169352815,0.104169352815,0.156254044222,0.20833870563,0.0,0.0520846914074,0.0,0.104169352815,0.0,0.104169352815,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0])

    # Creating weights for histo: y13_THT_3
    y13_THT_3_weights = numpy.array([3.27167510628,62.0551109831,88.9752900859,106.720566086,116.926779537,111.983707866,106.044905858,88.6907999897,73.399284819,63.7976315724,54.0181682656,44.0253448866,35.4905520007,29.2672568964,23.043961792,19.4166725655,17.3896588801,12.4465842087,9.53052922263,8.28587080176,6.7567162847,5.54761987586,4.40964749107,3.27167510628,2.80937194995,2.70268711388,2.59600197781,1.45802839301,1.52915181706,1.17353529682,1.28022013289,0.995726736692,0.640110216445,0.568986792396,0.568986792396,0.497863368346,0.213370032148,0.248931714173,0.284493366198,0.106685016074,0.142246698099,0.142246698099,0.106685016074,0.0711233340495,0.0,0.0711233340495,0.0,0.0711233340495,0.0,0.0711233340495,0.0,0.0355616820247,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0355616820247,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0])

    # Creating weights for histo: y13_THT_4
    y13_THT_4_weights = numpy.array([0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0])

    # Creating weights for histo: y13_THT_5
    y13_THT_5_weights = numpy.array([0.0,0.0,158.005666306,78.97186254,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0])

    # Creating weights for histo: y13_THT_6
    y13_THT_6_weights = numpy.array([0.0,0.0,0.0,0.0,241.766740452,293.736568848,518.253813009,380.080886344,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0])

    # Creating weights for histo: y13_THT_7
    y13_THT_7_weights = numpy.array([0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,328.103919777,240.960653785,195.242473477,155.727705845,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0])

    # Creating weights for histo: y13_THT_8
    y13_THT_8_weights = numpy.array([0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,98.3081790494,78.6313680519,61.2334751532,31.7719316661,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0])

    # Creating weights for histo: y13_THT_9
    y13_THT_9_weights = numpy.array([0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,31.8324034158,26.3125760819,14.6387133953,12.3072685131,8.6975619818,7.4261766787,4.24207354759,4.88090138585,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0])

    # Creating weights for histo: y13_THT_10
    y13_THT_10_weights = numpy.array([0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,2.40054229988,1.37210682802,0.571944528488,1.02613255191,0.683844543261,0.456381825026,0.682764440122,0.689033824995,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0])

    # Creating weights for histo: y13_THT_11
    y13_THT_11_weights = numpy.array([0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.189543473619,0.121837123083,0.108294085898,0.0405525381686,0.0135727685641,0.0813239688136,0.0271356911534,0.0135002721612,0.0542407818257,0.013537753275,0.0,0.0271046835514,0.0,0.0,0.0,0.0135152259158,0.0,0.0,0.0135566280952,0.0135575231838,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0])

    # Creating weights for histo: y13_THT_12
    y13_THT_12_weights = numpy.array([0.0,3.6450972,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0])

    # Creating weights for histo: y13_THT_13
    y13_THT_13_weights = numpy.array([0.0,0.0,25.6050978981,61.7436365452,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0])

    # Creating weights for histo: y13_THT_14
    y13_THT_14_weights = numpy.array([0.0,0.0,0.0,0.0,90.757652125,122.109282343,119.648122225,120.85230061,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0])

    # Creating weights for histo: y13_THT_15
    y13_THT_15_weights = numpy.array([0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,111.982478312,89.8533255115,77.1216666061,53.8082146899,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0])

    # Creating weights for histo: y13_THT_16
    y13_THT_16_weights = numpy.array([0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,45.2230525732,33.4445367443,25.5782339406,18.7362626319,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0])

    # Creating weights for histo: y13_THT_17
    y13_THT_17_weights = numpy.array([0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,12.9500194074,9.76786541051,7.10707376695,5.51939778414,4.40133863128,2.98527297971,2.40634228821,1.58777570395,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0])

    # Creating weights for histo: y13_THT_18
    y13_THT_18_weights = numpy.array([0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,1.18877661878,0.888895564313,0.661042565954,0.48420836674,0.323842734393,0.23648257266,0.215350384511,0.118166572081,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0])

    # Creating weights for histo: y13_THT_19
    y13_THT_19_weights = numpy.array([0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.108519619226,0.0660106511801,0.0638311278544,0.04473009689,0.0360407688582,0.025567548559,0.0234245636981,0.0147161590463,0.0168931321408,0.00211496461359,0.00851510381137,0.00211496461359,0.00426586298655,0.00425990836383,0.00425604515339,0.0063844836739,0.00212624019897,0.0,0.0,0.0,0.0,0.0,0.0,0.00209795490581,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0])

    # Creating a new Canvas
    fig   = plt.figure(figsize=(12,6),dpi=80)
    frame = gridspec.GridSpec(1,1,right=0.7)
    pad   = fig.add_subplot(frame[0])

    # Creating a new Stack
    pad.hist(x=xData, bins=xBinning, weights=y13_THT_0_weights+y13_THT_1_weights+y13_THT_2_weights+y13_THT_3_weights+y13_THT_4_weights+y13_THT_5_weights+y13_THT_6_weights+y13_THT_7_weights+y13_THT_8_weights+y13_THT_9_weights+y13_THT_10_weights+y13_THT_11_weights+y13_THT_12_weights+y13_THT_13_weights+y13_THT_14_weights+y13_THT_15_weights+y13_THT_16_weights+y13_THT_17_weights+y13_THT_18_weights+y13_THT_19_weights,\
             label="$bg\_vbf\_1600\_inf$", histtype="step", rwidth=1.0,\
             color=None, edgecolor="#ccc6aa", linewidth=1, linestyle="solid",\
             bottom=None, cumulative=False, normed=False, align="mid", orientation="vertical")

    pad.hist(x=xData, bins=xBinning, weights=y13_THT_0_weights+y13_THT_1_weights+y13_THT_2_weights+y13_THT_3_weights+y13_THT_4_weights+y13_THT_5_weights+y13_THT_6_weights+y13_THT_7_weights+y13_THT_8_weights+y13_THT_9_weights+y13_THT_10_weights+y13_THT_11_weights+y13_THT_12_weights+y13_THT_13_weights+y13_THT_14_weights+y13_THT_15_weights+y13_THT_16_weights+y13_THT_17_weights+y13_THT_18_weights,\
             label="$bg\_vbf\_1200\_1600$", histtype="step", rwidth=1.0,\
             color=None, edgecolor="#c1bfa8", linewidth=1, linestyle="solid",\
             bottom=None, cumulative=False, normed=False, align="mid", orientation="vertical")

    pad.hist(x=xData, bins=xBinning, weights=y13_THT_0_weights+y13_THT_1_weights+y13_THT_2_weights+y13_THT_3_weights+y13_THT_4_weights+y13_THT_5_weights+y13_THT_6_weights+y13_THT_7_weights+y13_THT_8_weights+y13_THT_9_weights+y13_THT_10_weights+y13_THT_11_weights+y13_THT_12_weights+y13_THT_13_weights+y13_THT_14_weights+y13_THT_15_weights+y13_THT_16_weights+y13_THT_17_weights,\
             label="$bg\_vbf\_800\_1200$", histtype="step", rwidth=1.0,\
             color=None, edgecolor="#bab5a3", linewidth=1, linestyle="solid",\
             bottom=None, cumulative=False, normed=False, align="mid", orientation="vertical")

    pad.hist(x=xData, bins=xBinning, weights=y13_THT_0_weights+y13_THT_1_weights+y13_THT_2_weights+y13_THT_3_weights+y13_THT_4_weights+y13_THT_5_weights+y13_THT_6_weights+y13_THT_7_weights+y13_THT_8_weights+y13_THT_9_weights+y13_THT_10_weights+y13_THT_11_weights+y13_THT_12_weights+y13_THT_13_weights+y13_THT_14_weights+y13_THT_15_weights+y13_THT_16_weights,\
             label="$bg\_vbf\_600\_800$", histtype="step", rwidth=1.0,\
             color=None, edgecolor="#b2a596", linewidth=1, linestyle="solid",\
             bottom=None, cumulative=False, normed=False, align="mid", orientation="vertical")

    pad.hist(x=xData, bins=xBinning, weights=y13_THT_0_weights+y13_THT_1_weights+y13_THT_2_weights+y13_THT_3_weights+y13_THT_4_weights+y13_THT_5_weights+y13_THT_6_weights+y13_THT_7_weights+y13_THT_8_weights+y13_THT_9_weights+y13_THT_10_weights+y13_THT_11_weights+y13_THT_12_weights+y13_THT_13_weights+y13_THT_14_weights+y13_THT_15_weights,\
             label="$bg\_vbf\_400\_600$", histtype="step", rwidth=1.0,\
             color=None, edgecolor="#b7a39b", linewidth=1, linestyle="solid",\
             bottom=None, cumulative=False, normed=False, align="mid", orientation="vertical")

    pad.hist(x=xData, bins=xBinning, weights=y13_THT_0_weights+y13_THT_1_weights+y13_THT_2_weights+y13_THT_3_weights+y13_THT_4_weights+y13_THT_5_weights+y13_THT_6_weights+y13_THT_7_weights+y13_THT_8_weights+y13_THT_9_weights+y13_THT_10_weights+y13_THT_11_weights+y13_THT_12_weights+y13_THT_13_weights+y13_THT_14_weights,\
             label="$bg\_vbf\_200\_400$", histtype="step", rwidth=1.0,\
             color=None, edgecolor="#ad998c", linewidth=1, linestyle="solid",\
             bottom=None, cumulative=False, normed=False, align="mid", orientation="vertical")

    pad.hist(x=xData, bins=xBinning, weights=y13_THT_0_weights+y13_THT_1_weights+y13_THT_2_weights+y13_THT_3_weights+y13_THT_4_weights+y13_THT_5_weights+y13_THT_6_weights+y13_THT_7_weights+y13_THT_8_weights+y13_THT_9_weights+y13_THT_10_weights+y13_THT_11_weights+y13_THT_12_weights+y13_THT_13_weights,\
             label="$bg\_vbf\_100\_200$", histtype="step", rwidth=1.0,\
             color=None, edgecolor="#9b8e82", linewidth=1, linestyle="solid",\
             bottom=None, cumulative=False, normed=False, align="mid", orientation="vertical")

    pad.hist(x=xData, bins=xBinning, weights=y13_THT_0_weights+y13_THT_1_weights+y13_THT_2_weights+y13_THT_3_weights+y13_THT_4_weights+y13_THT_5_weights+y13_THT_6_weights+y13_THT_7_weights+y13_THT_8_weights+y13_THT_9_weights+y13_THT_10_weights+y13_THT_11_weights+y13_THT_12_weights,\
             label="$bg\_vbf\_0\_100$", histtype="step", rwidth=1.0,\
             color=None, edgecolor="#876656", linewidth=1, linestyle="solid",\
             bottom=None, cumulative=False, normed=False, align="mid", orientation="vertical")

    pad.hist(x=xData, bins=xBinning, weights=y13_THT_0_weights+y13_THT_1_weights+y13_THT_2_weights+y13_THT_3_weights+y13_THT_4_weights+y13_THT_5_weights+y13_THT_6_weights+y13_THT_7_weights+y13_THT_8_weights+y13_THT_9_weights+y13_THT_10_weights+y13_THT_11_weights,\
             label="$bg\_dip\_1600\_inf$", histtype="step", rwidth=1.0,\
             color=None, edgecolor="#afcec6", linewidth=1, linestyle="solid",\
             bottom=None, cumulative=False, normed=False, align="mid", orientation="vertical")

    pad.hist(x=xData, bins=xBinning, weights=y13_THT_0_weights+y13_THT_1_weights+y13_THT_2_weights+y13_THT_3_weights+y13_THT_4_weights+y13_THT_5_weights+y13_THT_6_weights+y13_THT_7_weights+y13_THT_8_weights+y13_THT_9_weights+y13_THT_10_weights,\
             label="$bg\_dip\_1200\_1600$", histtype="step", rwidth=1.0,\
             color=None, edgecolor="#84c1a3", linewidth=1, linestyle="solid",\
             bottom=None, cumulative=False, normed=False, align="mid", orientation="vertical")

    pad.hist(x=xData, bins=xBinning, weights=y13_THT_0_weights+y13_THT_1_weights+y13_THT_2_weights+y13_THT_3_weights+y13_THT_4_weights+y13_THT_5_weights+y13_THT_6_weights+y13_THT_7_weights+y13_THT_8_weights+y13_THT_9_weights,\
             label="$bg\_dip\_800\_1200$", histtype="step", rwidth=1.0,\
             color=None, edgecolor="#89a8a0", linewidth=1, linestyle="solid",\
             bottom=None, cumulative=False, normed=False, align="mid", orientation="vertical")

    pad.hist(x=xData, bins=xBinning, weights=y13_THT_0_weights+y13_THT_1_weights+y13_THT_2_weights+y13_THT_3_weights+y13_THT_4_weights+y13_THT_5_weights+y13_THT_6_weights+y13_THT_7_weights+y13_THT_8_weights,\
             label="$bg\_dip\_600\_800$", histtype="step", rwidth=1.0,\
             color=None, edgecolor="#829e8c", linewidth=1, linestyle="solid",\
             bottom=None, cumulative=False, normed=False, align="mid", orientation="vertical")

    pad.hist(x=xData, bins=xBinning, weights=y13_THT_0_weights+y13_THT_1_weights+y13_THT_2_weights+y13_THT_3_weights+y13_THT_4_weights+y13_THT_5_weights+y13_THT_6_weights+y13_THT_7_weights,\
             label="$bg\_dip\_400\_600$", histtype="step", rwidth=1.0,\
             color=None, edgecolor="#adbcc6", linewidth=1, linestyle="solid",\
             bottom=None, cumulative=False, normed=False, align="mid", orientation="vertical")

    pad.hist(x=xData, bins=xBinning, weights=y13_THT_0_weights+y13_THT_1_weights+y13_THT_2_weights+y13_THT_3_weights+y13_THT_4_weights+y13_THT_5_weights+y13_THT_6_weights,\
             label="$bg\_dip\_200\_400$", histtype="step", rwidth=1.0,\
             color=None, edgecolor="#7a8e99", linewidth=1, linestyle="solid",\
             bottom=None, cumulative=False, normed=False, align="mid", orientation="vertical")

    pad.hist(x=xData, bins=xBinning, weights=y13_THT_0_weights+y13_THT_1_weights+y13_THT_2_weights+y13_THT_3_weights+y13_THT_4_weights+y13_THT_5_weights,\
             label="$bg\_dip\_100\_200$", histtype="step", rwidth=1.0,\
             color=None, edgecolor="#758991", linewidth=1, linestyle="solid",\
             bottom=None, cumulative=False, normed=False, align="mid", orientation="vertical")

    pad.hist(x=xData, bins=xBinning, weights=y13_THT_0_weights+y13_THT_1_weights+y13_THT_2_weights+y13_THT_3_weights+y13_THT_4_weights,\
             label="$bg\_dip\_0\_100$", histtype="step", rwidth=1.0,\
             color=None, edgecolor="#688296", linewidth=1, linestyle="solid",\
             bottom=None, cumulative=False, normed=False, align="mid", orientation="vertical")

    pad.hist(x=xData, bins=xBinning, weights=y13_THT_0_weights+y13_THT_1_weights+y13_THT_2_weights+y13_THT_3_weights,\
             label="$signal\_2pt4TeVL$", histtype="step", rwidth=1.0,\
             color=None, edgecolor="#6d7a84", linewidth=1, linestyle="solid",\
             bottom=None, cumulative=False, normed=False, align="mid", orientation="vertical")

    pad.hist(x=xData, bins=xBinning, weights=y13_THT_0_weights+y13_THT_1_weights+y13_THT_2_weights,\
             label="$signal\_2pt2TeVL$", histtype="step", rwidth=1.0,\
             color=None, edgecolor="#7c99d1", linewidth=1, linestyle="solid",\
             bottom=None, cumulative=False, normed=False, align="mid", orientation="vertical")

    pad.hist(x=xData, bins=xBinning, weights=y13_THT_0_weights+y13_THT_1_weights,\
             label="$signal\_2TeVL$", histtype="step", rwidth=1.0,\
             color=None, edgecolor="#7f7f9b", linewidth=1, linestyle="solid",\
             bottom=None, cumulative=False, normed=False, align="mid", orientation="vertical")

    pad.hist(x=xData, bins=xBinning, weights=y13_THT_0_weights,\
             label="$signal\_1pt8TeVL$", histtype="step", rwidth=1.0,\
             color=None, edgecolor="#aaa5bf", linewidth=1, linestyle="solid",\
             bottom=None, cumulative=False, normed=False, align="mid", orientation="vertical")


    # Axis
    plt.rc('text',usetex=False)
    plt.xlabel(r"THT",\
               fontsize=16,color="black")
    plt.ylabel(r"$\mathrm{Events}$ $(\mathcal{L}_{\mathrm{int}} = 3000.0\ \mathrm{fb}^{-1})$ ",\
               fontsize=16,color="black")

    # Boundary of y-axis
    ymax=(y13_THT_0_weights+y13_THT_1_weights+y13_THT_2_weights+y13_THT_3_weights+y13_THT_4_weights+y13_THT_5_weights+y13_THT_6_weights+y13_THT_7_weights+y13_THT_8_weights+y13_THT_9_weights+y13_THT_10_weights+y13_THT_11_weights+y13_THT_12_weights+y13_THT_13_weights+y13_THT_14_weights+y13_THT_15_weights+y13_THT_16_weights+y13_THT_17_weights+y13_THT_18_weights+y13_THT_19_weights).max()*1.1
    ymin=0 # linear scale
    #ymin=min([x for x in (y13_THT_0_weights+y13_THT_1_weights+y13_THT_2_weights+y13_THT_3_weights+y13_THT_4_weights+y13_THT_5_weights+y13_THT_6_weights+y13_THT_7_weights+y13_THT_8_weights+y13_THT_9_weights+y13_THT_10_weights+y13_THT_11_weights+y13_THT_12_weights+y13_THT_13_weights+y13_THT_14_weights+y13_THT_15_weights+y13_THT_16_weights+y13_THT_17_weights+y13_THT_18_weights+y13_THT_19_weights) if x])/100. # log scale
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
    plt.savefig('../../HTML/MadAnalysis5job_0/selection_12.png')
    plt.savefig('../../PDF/MadAnalysis5job_0/selection_12.png')
    plt.savefig('../../DVI/MadAnalysis5job_0/selection_12.eps')

# Running!
if __name__ == '__main__':
    selection_12()
