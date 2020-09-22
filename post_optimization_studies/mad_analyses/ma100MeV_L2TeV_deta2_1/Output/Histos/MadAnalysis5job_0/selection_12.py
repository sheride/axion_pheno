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
    y13_THT_0_weights = numpy.array([0.0961726875221,1.7075744941,2.36042807017,2.92997421644,3.15762520957,3.26552327116,3.38210555157,3.23123403601,3.19824535535,2.87124862549,2.88513346358,2.62128876628,2.43846973309,2.27079372653,1.98116855396,1.83688014629,1.58260455647,1.37743429125,1.2331342929,1.1005956397,0.964949084912,0.839904407358,0.721308145974,0.626158236248,0.546046637342,0.506488038193,0.416709810214,0.411436049749,0.345197458439,0.301305622746,0.239396750808,0.199825721652,0.179541468006,0.145334286894,0.135715819105,0.0982950613622,0.112222745005,0.0908299025455,0.0737256924874,0.0641102222893,0.0587847833684,0.0416752176157,0.0395285832784,0.0427466363105,0.0224473987102,0.0171005889691,0.0149614246267,0.0138915127206,0.0138926118371,0.0106879280575,0.0138907453375,0.00640926763943,0.0042764621852,0.0042764621852,0.00320874451516,0.00213466955569,0.00320501671191,0.00106771767004,0.00213729904187,0.00213543534009,0.0,0.0,0.00213466955569,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0])

    # Creating weights for histo: y13_THT_1
    y13_THT_1_weights = numpy.array([0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0])

    # Creating weights for histo: y13_THT_2
    y13_THT_2_weights = numpy.array([0.0,0.0,2.10674221742,1.0529581672,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0])

    # Creating weights for histo: y13_THT_3
    y13_THT_3_weights = numpy.array([0.0,0.0,0.0,0.0,3.22342548202,4.60765578583,8.98151967748,8.98496643929,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0])

    # Creating weights for histo: y13_THT_4
    y13_THT_4_weights = numpy.array([0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,9.02711406973,8.86140116235,8.64014542471,8.27897468936,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0])

    # Creating weights for histo: y13_THT_5
    y13_THT_5_weights = numpy.array([0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,5.93868606446,5.24247161878,4.35503353442,3.29694319592,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0])

    # Creating weights for histo: y13_THT_6
    y13_THT_6_weights = numpy.array([0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,2.917169605,2.18695967575,1.63799841374,1.38634969601,1.17671893199,0.90527069302,0.690283850891,0.537588108596,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0])

    # Creating weights for histo: y13_THT_7
    y13_THT_7_weights = numpy.array([0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.484456854097,0.370163096165,0.286335952118,0.254322020871,0.164493719571,0.1462365563,0.124920324742,0.0898731788205,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0])

    # Creating weights for histo: y13_THT_8
    y13_THT_8_weights = numpy.array([0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0839630587784,0.0637371468554,0.0577883582928,0.0456793849082,0.0384583174516,0.0317786770625,0.0294324558743,0.0241942691558,0.0223881347929,0.0160664777361,0.0130018712853,0.0101124591476,0.00866599112227,0.0088514644773,0.00595629468958,0.00577698721925,0.00487366777955,0.00234731071269,0.00198435615998,0.00270809931065,0.00180619675351,0.00126433834366,0.00234585262153,0.00198673971154,0.00144498605626,0.000540737690018,0.000903537036508,0.000722332430134,0.000722575060201,0.000721777076871,0.000180916723875,0.000180374773034,0.000360817405462,0.0,0.000180065438956,0.0,0.00036144604841,0.000180553972669,0.0,0.0,0.0,0.000180600765611,0.0,0.0,0.000180408702731,0.0,0.0,0.0])

    # Creating weights for histo: y13_THT_9
    y13_THT_9_weights = numpy.array([0.0,0.048601296,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0])

    # Creating weights for histo: y13_THT_10
    y13_THT_10_weights = numpy.array([0.0,0.0,0.341401305308,0.82324848727,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0])

    # Creating weights for histo: y13_THT_11
    y13_THT_11_weights = numpy.array([0.0,0.0,0.0,0.0,1.21012991523,1.67217788677,1.79336451685,2.0072677979,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0])

    # Creating weights for histo: y13_THT_12
    y13_THT_12_weights = numpy.array([0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,2.07337972426,1.89079029513,1.74079817622,1.38850672919,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0])

    # Creating weights for histo: y13_THT_13
    y13_THT_13_weights = numpy.array([0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,1.2147598904,0.979820731833,0.812176805907,0.653653269699,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0])

    # Creating weights for histo: y13_THT_14
    y13_THT_14_weights = numpy.array([0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.51281702612,0.415987887697,0.337546330751,0.26056915377,0.214982316571,0.164910759487,0.138866851267,0.107338341683,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0])

    # Creating weights for histo: y13_THT_15
    y13_THT_15_weights = numpy.array([0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0898510852111,0.0727207087841,0.0575521118549,0.0470725237441,0.0386569511308,0.0305299980285,0.0277666001142,0.0208156292337,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0])

    # Creating weights for histo: y13_THT_16
    y13_THT_16_weights = numpy.array([0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0173761262713,0.0142691325862,0.012246118624,0.00998732097176,0.00744545071229,0.0064645379868,0.00575304184036,0.0042509173569,0.00337526669251,0.002719694172,0.00241086001346,0.001472419392,0.00184092319057,0.00129968689826,0.00107679467694,0.000909641327885,0.00107530342975,0.000792237802789,0.00051091931574,0.000427576702119,0.000567105814635,0.000341092385185,0.000226846454593,0.000198119042663,0.000141884662273,0.000170466142574,0.000198700482035,0.000142140822332,5.67883294868e-05,0.000142004900668,2.84351476794e-05,8.52720566856e-05,2.84351476794e-05,8.52643041607e-05,2.83743601609e-05,0.0,0.0,0.0,2.83743601609e-05,0.0,0.0,2.83557362791e-05,0.0,0.0,0.0,0.0,0.0,0.0])

    # Creating a new Canvas
    fig   = plt.figure(figsize=(12,6),dpi=80)
    frame = gridspec.GridSpec(1,1,right=0.7)
    pad   = fig.add_subplot(frame[0])

    # Creating a new Stack
    pad.hist(x=xData, bins=xBinning, weights=y13_THT_0_weights+y13_THT_1_weights+y13_THT_2_weights+y13_THT_3_weights+y13_THT_4_weights+y13_THT_5_weights+y13_THT_6_weights+y13_THT_7_weights+y13_THT_8_weights+y13_THT_9_weights+y13_THT_10_weights+y13_THT_11_weights+y13_THT_12_weights+y13_THT_13_weights+y13_THT_14_weights+y13_THT_15_weights+y13_THT_16_weights,\
             label="$bg\_vbf\_1600\_inf$", histtype="step", rwidth=1.0,\
             color=None, edgecolor="#e5e5e5", linewidth=1, linestyle="solid",\
             bottom=None, cumulative=False, normed=False, align="mid", orientation="vertical")

    pad.hist(x=xData, bins=xBinning, weights=y13_THT_0_weights+y13_THT_1_weights+y13_THT_2_weights+y13_THT_3_weights+y13_THT_4_weights+y13_THT_5_weights+y13_THT_6_weights+y13_THT_7_weights+y13_THT_8_weights+y13_THT_9_weights+y13_THT_10_weights+y13_THT_11_weights+y13_THT_12_weights+y13_THT_13_weights+y13_THT_14_weights+y13_THT_15_weights,\
             label="$bg\_vbf\_1200\_1600$", histtype="step", rwidth=1.0,\
             color=None, edgecolor="#f2f2f2", linewidth=1, linestyle="solid",\
             bottom=None, cumulative=False, normed=False, align="mid", orientation="vertical")

    pad.hist(x=xData, bins=xBinning, weights=y13_THT_0_weights+y13_THT_1_weights+y13_THT_2_weights+y13_THT_3_weights+y13_THT_4_weights+y13_THT_5_weights+y13_THT_6_weights+y13_THT_7_weights+y13_THT_8_weights+y13_THT_9_weights+y13_THT_10_weights+y13_THT_11_weights+y13_THT_12_weights+y13_THT_13_weights+y13_THT_14_weights,\
             label="$bg\_vbf\_800\_1200$", histtype="step", rwidth=1.0,\
             color=None, edgecolor="#ccc6aa", linewidth=1, linestyle="solid",\
             bottom=None, cumulative=False, normed=False, align="mid", orientation="vertical")

    pad.hist(x=xData, bins=xBinning, weights=y13_THT_0_weights+y13_THT_1_weights+y13_THT_2_weights+y13_THT_3_weights+y13_THT_4_weights+y13_THT_5_weights+y13_THT_6_weights+y13_THT_7_weights+y13_THT_8_weights+y13_THT_9_weights+y13_THT_10_weights+y13_THT_11_weights+y13_THT_12_weights+y13_THT_13_weights,\
             label="$bg\_vbf\_600\_800$", histtype="step", rwidth=1.0,\
             color=None, edgecolor="#ccc6aa", linewidth=1, linestyle="solid",\
             bottom=None, cumulative=False, normed=False, align="mid", orientation="vertical")

    pad.hist(x=xData, bins=xBinning, weights=y13_THT_0_weights+y13_THT_1_weights+y13_THT_2_weights+y13_THT_3_weights+y13_THT_4_weights+y13_THT_5_weights+y13_THT_6_weights+y13_THT_7_weights+y13_THT_8_weights+y13_THT_9_weights+y13_THT_10_weights+y13_THT_11_weights+y13_THT_12_weights,\
             label="$bg\_vbf\_400\_600$", histtype="step", rwidth=1.0,\
             color=None, edgecolor="#c1bfa8", linewidth=1, linestyle="solid",\
             bottom=None, cumulative=False, normed=False, align="mid", orientation="vertical")

    pad.hist(x=xData, bins=xBinning, weights=y13_THT_0_weights+y13_THT_1_weights+y13_THT_2_weights+y13_THT_3_weights+y13_THT_4_weights+y13_THT_5_weights+y13_THT_6_weights+y13_THT_7_weights+y13_THT_8_weights+y13_THT_9_weights+y13_THT_10_weights+y13_THT_11_weights,\
             label="$bg\_vbf\_200\_400$", histtype="step", rwidth=1.0,\
             color=None, edgecolor="#bab5a3", linewidth=1, linestyle="solid",\
             bottom=None, cumulative=False, normed=False, align="mid", orientation="vertical")

    pad.hist(x=xData, bins=xBinning, weights=y13_THT_0_weights+y13_THT_1_weights+y13_THT_2_weights+y13_THT_3_weights+y13_THT_4_weights+y13_THT_5_weights+y13_THT_6_weights+y13_THT_7_weights+y13_THT_8_weights+y13_THT_9_weights+y13_THT_10_weights,\
             label="$bg\_vbf\_100\_200$", histtype="step", rwidth=1.0,\
             color=None, edgecolor="#b2a596", linewidth=1, linestyle="solid",\
             bottom=None, cumulative=False, normed=False, align="mid", orientation="vertical")

    pad.hist(x=xData, bins=xBinning, weights=y13_THT_0_weights+y13_THT_1_weights+y13_THT_2_weights+y13_THT_3_weights+y13_THT_4_weights+y13_THT_5_weights+y13_THT_6_weights+y13_THT_7_weights+y13_THT_8_weights+y13_THT_9_weights,\
             label="$bg\_vbf\_0\_100$", histtype="step", rwidth=1.0,\
             color=None, edgecolor="#b7a39b", linewidth=1, linestyle="solid",\
             bottom=None, cumulative=False, normed=False, align="mid", orientation="vertical")

    pad.hist(x=xData, bins=xBinning, weights=y13_THT_0_weights+y13_THT_1_weights+y13_THT_2_weights+y13_THT_3_weights+y13_THT_4_weights+y13_THT_5_weights+y13_THT_6_weights+y13_THT_7_weights+y13_THT_8_weights,\
             label="$bg\_dip\_1600\_inf$", histtype="step", rwidth=1.0,\
             color=None, edgecolor="#ad998c", linewidth=1, linestyle="solid",\
             bottom=None, cumulative=False, normed=False, align="mid", orientation="vertical")

    pad.hist(x=xData, bins=xBinning, weights=y13_THT_0_weights+y13_THT_1_weights+y13_THT_2_weights+y13_THT_3_weights+y13_THT_4_weights+y13_THT_5_weights+y13_THT_6_weights+y13_THT_7_weights,\
             label="$bg\_dip\_1200\_1600$", histtype="step", rwidth=1.0,\
             color=None, edgecolor="#9b8e82", linewidth=1, linestyle="solid",\
             bottom=None, cumulative=False, normed=False, align="mid", orientation="vertical")

    pad.hist(x=xData, bins=xBinning, weights=y13_THT_0_weights+y13_THT_1_weights+y13_THT_2_weights+y13_THT_3_weights+y13_THT_4_weights+y13_THT_5_weights+y13_THT_6_weights,\
             label="$bg\_dip\_800\_1200$", histtype="step", rwidth=1.0,\
             color=None, edgecolor="#876656", linewidth=1, linestyle="solid",\
             bottom=None, cumulative=False, normed=False, align="mid", orientation="vertical")

    pad.hist(x=xData, bins=xBinning, weights=y13_THT_0_weights+y13_THT_1_weights+y13_THT_2_weights+y13_THT_3_weights+y13_THT_4_weights+y13_THT_5_weights,\
             label="$bg\_dip\_600\_800$", histtype="step", rwidth=1.0,\
             color=None, edgecolor="#afcec6", linewidth=1, linestyle="solid",\
             bottom=None, cumulative=False, normed=False, align="mid", orientation="vertical")

    pad.hist(x=xData, bins=xBinning, weights=y13_THT_0_weights+y13_THT_1_weights+y13_THT_2_weights+y13_THT_3_weights+y13_THT_4_weights,\
             label="$bg\_dip\_400\_600$", histtype="step", rwidth=1.0,\
             color=None, edgecolor="#84c1a3", linewidth=1, linestyle="solid",\
             bottom=None, cumulative=False, normed=False, align="mid", orientation="vertical")

    pad.hist(x=xData, bins=xBinning, weights=y13_THT_0_weights+y13_THT_1_weights+y13_THT_2_weights+y13_THT_3_weights,\
             label="$bg\_dip\_200\_400$", histtype="step", rwidth=1.0,\
             color=None, edgecolor="#89a8a0", linewidth=1, linestyle="solid",\
             bottom=None, cumulative=False, normed=False, align="mid", orientation="vertical")

    pad.hist(x=xData, bins=xBinning, weights=y13_THT_0_weights+y13_THT_1_weights+y13_THT_2_weights,\
             label="$bg\_dip\_100\_200$", histtype="step", rwidth=1.0,\
             color=None, edgecolor="#829e8c", linewidth=1, linestyle="solid",\
             bottom=None, cumulative=False, normed=False, align="mid", orientation="vertical")

    pad.hist(x=xData, bins=xBinning, weights=y13_THT_0_weights+y13_THT_1_weights,\
             label="$bg\_dip\_0\_100$", histtype="step", rwidth=1.0,\
             color=None, edgecolor="#adbcc6", linewidth=1, linestyle="solid",\
             bottom=None, cumulative=False, normed=False, align="mid", orientation="vertical")

    pad.hist(x=xData, bins=xBinning, weights=y13_THT_0_weights,\
             label="$signal$", histtype="step", rwidth=1.0,\
             color=None, edgecolor="#7a8e99", linewidth=1, linestyle="solid",\
             bottom=None, cumulative=False, normed=False, align="mid", orientation="vertical")


    # Axis
    plt.rc('text',usetex=False)
    plt.xlabel(r"THT",\
               fontsize=16,color="black")
    plt.ylabel(r"$\mathrm{Events}$ $(\mathcal{L}_{\mathrm{int}} = 40.0\ \mathrm{fb}^{-1})$ ",\
               fontsize=16,color="black")

    # Boundary of y-axis
    ymax=(y13_THT_0_weights+y13_THT_1_weights+y13_THT_2_weights+y13_THT_3_weights+y13_THT_4_weights+y13_THT_5_weights+y13_THT_6_weights+y13_THT_7_weights+y13_THT_8_weights+y13_THT_9_weights+y13_THT_10_weights+y13_THT_11_weights+y13_THT_12_weights+y13_THT_13_weights+y13_THT_14_weights+y13_THT_15_weights+y13_THT_16_weights).max()*1.1
    ymin=0 # linear scale
    #ymin=min([x for x in (y13_THT_0_weights+y13_THT_1_weights+y13_THT_2_weights+y13_THT_3_weights+y13_THT_4_weights+y13_THT_5_weights+y13_THT_6_weights+y13_THT_7_weights+y13_THT_8_weights+y13_THT_9_weights+y13_THT_10_weights+y13_THT_11_weights+y13_THT_12_weights+y13_THT_13_weights+y13_THT_14_weights+y13_THT_15_weights+y13_THT_16_weights) if x])/100. # log scale
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
