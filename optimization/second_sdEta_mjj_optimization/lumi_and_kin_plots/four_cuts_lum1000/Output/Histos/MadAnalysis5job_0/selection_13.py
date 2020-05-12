def selection_13():

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

    # Creating weights for histo: y14_THT_0
    y14_THT_0_weights = numpy.array([32.1385637013,680.84614287,1006.7351762,1274.79495685,1510.61476388,1666.08763666,1630.57166572,1534.56474428,1391.47686137,1240.60998482,1086.36511104,979.918998141,814.927433152,735.706897978,603.570306104,506.131185838,427.012950579,363.861702255,300.710453931,249.22739606,203.578333414,170.518560466,134.081290283,117.090804186,93.4474735328,78.2993559284,62.6394887427,49.1290097982,41.6573059122,36.7444099324,27.3280076377,22.1080519092,17.9116153431,15.5575172694,11.8728402846,9.72345004339,8.08581638345,7.88111155096,5.3223096448,5.93642214228,4.19643656609,2.55880290616,2.45644998991,2.35409807366,1.63763365994,1.12587307871,0.921168946216,1.53528174369,0.307056348739,0.409408364985,0.0,0.409408364985,0.409408364985,0.307056348739,0.204704232492,0.102352116246,0.307056348739,0.204704232492,0.0,0.102352116246,0.204704232492,0.0,0.0,0.102352116246,0.0,0.0,0.102352116246,0.102352116246,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0])

    # Creating weights for histo: y14_THT_1
    y14_THT_1_weights = numpy.array([0.0,1.2150324,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0])

    # Creating weights for histo: y14_THT_2
    y14_THT_2_weights = numpy.array([0.0,0.0,8.5350326327,20.5812121817,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0])

    # Creating weights for histo: y14_THT_3
    y14_THT_3_weights = numpy.array([0.0,0.0,0.0,0.0,30.2525507083,40.7030941142,39.8827074085,40.2841002032,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0])

    # Creating weights for histo: y14_THT_4
    y14_THT_4_weights = numpy.array([0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,37.3274927708,29.9511085038,25.707222202,17.9360715633,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0])

    # Creating weights for histo: y14_THT_5
    y14_THT_5_weights = numpy.array([0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,15.0743508577,11.1481789148,8.52607798019,6.24542087729,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0])

    # Creating weights for histo: y14_THT_6
    y14_THT_6_weights = numpy.array([0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,4.31667313581,3.25595513684,2.36902458898,1.83979926138,1.46711287709,0.995090993238,0.802114096071,0.529258567982,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0])

    # Creating weights for histo: y14_THT_7
    y14_THT_7_weights = numpy.array([0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.396258872927,0.296298521438,0.220347521985,0.161402788913,0.107947578131,0.0788275242199,0.0717834615036,0.0393888573604,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0])

    # Creating weights for histo: y14_THT_8
    y14_THT_8_weights = numpy.array([0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0361732064088,0.0220035503934,0.0212770426181,0.0149100322967,0.0120135896194,0.00852251618632,0.00780818789935,0.00490538634876,0.00563104404695,0.000704988204529,0.00283836793712,0.000704988204529,0.00142195432885,0.00141996945461,0.0014186817178,0.00212816122463,0.000708746732991,0.0,0.0,0.0,0.0,0.0,0.0,0.000699318301938,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0])

    # Creating weights for histo: y14_THT_9
    y14_THT_9_weights = numpy.array([0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0])

    # Creating weights for histo: y14_THT_10
    y14_THT_10_weights = numpy.array([0.0,0.0,52.6685554354,26.32395418,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0])

    # Creating weights for histo: y14_THT_11
    y14_THT_11_weights = numpy.array([0.0,0.0,0.0,0.0,80.588913484,97.9121896161,172.751271003,126.693628781,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0])

    # Creating weights for histo: y14_THT_12
    y14_THT_12_weights = numpy.array([0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,109.367973259,80.3202179284,65.0808244924,51.9092352817,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0])

    # Creating weights for histo: y14_THT_13
    y14_THT_13_weights = numpy.array([0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,32.7693930165,26.2104560173,20.4111583844,10.5906438887,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0])

    # Creating weights for histo: y14_THT_14
    y14_THT_14_weights = numpy.array([0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,10.6108011386,8.77085869396,4.87957113175,4.10242283769,2.89918732727,2.47539222623,1.41402451586,1.62696712862,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0])

    # Creating weights for histo: y14_THT_15
    y14_THT_15_weights = numpy.array([0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.800180766626,0.457368942675,0.190648176163,0.342044183969,0.227948181087,0.152127275009,0.227588146707,0.229677941665,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0])

    # Creating weights for histo: y14_THT_16
    y14_THT_16_weights = numpy.array([0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0631811578728,0.0406123743611,0.0360980286327,0.0135175127229,0.00452425618802,0.0271079896045,0.00904523038446,0.00450009072042,0.0180802606086,0.00451258442501,0.0,0.00903489451714,0.0,0.0,0.0,0.00450507530528,0.0,0.0,0.00451887603174,0.00451917439461,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0])

    # Creating a new Canvas
    fig   = plt.figure(figsize=(12,6),dpi=80)
    frame = gridspec.GridSpec(1,1,right=0.7)
    pad   = fig.add_subplot(frame[0])

    # Creating a new Stack
    pad.hist(x=xData, bins=xBinning, weights=y14_THT_0_weights+y14_THT_1_weights+y14_THT_2_weights+y14_THT_3_weights+y14_THT_4_weights+y14_THT_5_weights+y14_THT_6_weights+y14_THT_7_weights+y14_THT_8_weights+y14_THT_9_weights+y14_THT_10_weights+y14_THT_11_weights+y14_THT_12_weights+y14_THT_13_weights+y14_THT_14_weights+y14_THT_15_weights+y14_THT_16_weights,\
             label="$bg\_dip\_1600\_inf$", histtype="step", rwidth=1.0,\
             color=None, edgecolor="#e5e5e5", linewidth=1, linestyle="solid",\
             bottom=None, cumulative=False, normed=False, align="mid", orientation="vertical")

    pad.hist(x=xData, bins=xBinning, weights=y14_THT_0_weights+y14_THT_1_weights+y14_THT_2_weights+y14_THT_3_weights+y14_THT_4_weights+y14_THT_5_weights+y14_THT_6_weights+y14_THT_7_weights+y14_THT_8_weights+y14_THT_9_weights+y14_THT_10_weights+y14_THT_11_weights+y14_THT_12_weights+y14_THT_13_weights+y14_THT_14_weights+y14_THT_15_weights,\
             label="$bg\_dip\_1200\_1600$", histtype="step", rwidth=1.0,\
             color=None, edgecolor="#f2f2f2", linewidth=1, linestyle="solid",\
             bottom=None, cumulative=False, normed=False, align="mid", orientation="vertical")

    pad.hist(x=xData, bins=xBinning, weights=y14_THT_0_weights+y14_THT_1_weights+y14_THT_2_weights+y14_THT_3_weights+y14_THT_4_weights+y14_THT_5_weights+y14_THT_6_weights+y14_THT_7_weights+y14_THT_8_weights+y14_THT_9_weights+y14_THT_10_weights+y14_THT_11_weights+y14_THT_12_weights+y14_THT_13_weights+y14_THT_14_weights,\
             label="$bg\_dip\_800\_1200$", histtype="step", rwidth=1.0,\
             color=None, edgecolor="#ccc6aa", linewidth=1, linestyle="solid",\
             bottom=None, cumulative=False, normed=False, align="mid", orientation="vertical")

    pad.hist(x=xData, bins=xBinning, weights=y14_THT_0_weights+y14_THT_1_weights+y14_THT_2_weights+y14_THT_3_weights+y14_THT_4_weights+y14_THT_5_weights+y14_THT_6_weights+y14_THT_7_weights+y14_THT_8_weights+y14_THT_9_weights+y14_THT_10_weights+y14_THT_11_weights+y14_THT_12_weights+y14_THT_13_weights,\
             label="$bg\_dip\_600\_800$", histtype="step", rwidth=1.0,\
             color=None, edgecolor="#ccc6aa", linewidth=1, linestyle="solid",\
             bottom=None, cumulative=False, normed=False, align="mid", orientation="vertical")

    pad.hist(x=xData, bins=xBinning, weights=y14_THT_0_weights+y14_THT_1_weights+y14_THT_2_weights+y14_THT_3_weights+y14_THT_4_weights+y14_THT_5_weights+y14_THT_6_weights+y14_THT_7_weights+y14_THT_8_weights+y14_THT_9_weights+y14_THT_10_weights+y14_THT_11_weights+y14_THT_12_weights,\
             label="$bg\_dip\_400\_600$", histtype="step", rwidth=1.0,\
             color=None, edgecolor="#c1bfa8", linewidth=1, linestyle="solid",\
             bottom=None, cumulative=False, normed=False, align="mid", orientation="vertical")

    pad.hist(x=xData, bins=xBinning, weights=y14_THT_0_weights+y14_THT_1_weights+y14_THT_2_weights+y14_THT_3_weights+y14_THT_4_weights+y14_THT_5_weights+y14_THT_6_weights+y14_THT_7_weights+y14_THT_8_weights+y14_THT_9_weights+y14_THT_10_weights+y14_THT_11_weights,\
             label="$bg\_dip\_200\_400$", histtype="step", rwidth=1.0,\
             color=None, edgecolor="#bab5a3", linewidth=1, linestyle="solid",\
             bottom=None, cumulative=False, normed=False, align="mid", orientation="vertical")

    pad.hist(x=xData, bins=xBinning, weights=y14_THT_0_weights+y14_THT_1_weights+y14_THT_2_weights+y14_THT_3_weights+y14_THT_4_weights+y14_THT_5_weights+y14_THT_6_weights+y14_THT_7_weights+y14_THT_8_weights+y14_THT_9_weights+y14_THT_10_weights,\
             label="$bg\_dip\_100\_200$", histtype="step", rwidth=1.0,\
             color=None, edgecolor="#b2a596", linewidth=1, linestyle="solid",\
             bottom=None, cumulative=False, normed=False, align="mid", orientation="vertical")

    pad.hist(x=xData, bins=xBinning, weights=y14_THT_0_weights+y14_THT_1_weights+y14_THT_2_weights+y14_THT_3_weights+y14_THT_4_weights+y14_THT_5_weights+y14_THT_6_weights+y14_THT_7_weights+y14_THT_8_weights+y14_THT_9_weights,\
             label="$bg\_dip\_0\_100$", histtype="step", rwidth=1.0,\
             color=None, edgecolor="#b7a39b", linewidth=1, linestyle="solid",\
             bottom=None, cumulative=False, normed=False, align="mid", orientation="vertical")

    pad.hist(x=xData, bins=xBinning, weights=y14_THT_0_weights+y14_THT_1_weights+y14_THT_2_weights+y14_THT_3_weights+y14_THT_4_weights+y14_THT_5_weights+y14_THT_6_weights+y14_THT_7_weights+y14_THT_8_weights,\
             label="$bg\_vbf\_1600\_inf$", histtype="step", rwidth=1.0,\
             color=None, edgecolor="#ad998c", linewidth=1, linestyle="solid",\
             bottom=None, cumulative=False, normed=False, align="mid", orientation="vertical")

    pad.hist(x=xData, bins=xBinning, weights=y14_THT_0_weights+y14_THT_1_weights+y14_THT_2_weights+y14_THT_3_weights+y14_THT_4_weights+y14_THT_5_weights+y14_THT_6_weights+y14_THT_7_weights,\
             label="$bg\_vbf\_1200\_1600$", histtype="step", rwidth=1.0,\
             color=None, edgecolor="#9b8e82", linewidth=1, linestyle="solid",\
             bottom=None, cumulative=False, normed=False, align="mid", orientation="vertical")

    pad.hist(x=xData, bins=xBinning, weights=y14_THT_0_weights+y14_THT_1_weights+y14_THT_2_weights+y14_THT_3_weights+y14_THT_4_weights+y14_THT_5_weights+y14_THT_6_weights,\
             label="$bg\_vbf\_800\_1200$", histtype="step", rwidth=1.0,\
             color=None, edgecolor="#876656", linewidth=1, linestyle="solid",\
             bottom=None, cumulative=False, normed=False, align="mid", orientation="vertical")

    pad.hist(x=xData, bins=xBinning, weights=y14_THT_0_weights+y14_THT_1_weights+y14_THT_2_weights+y14_THT_3_weights+y14_THT_4_weights+y14_THT_5_weights,\
             label="$bg\_vbf\_600\_800$", histtype="step", rwidth=1.0,\
             color=None, edgecolor="#afcec6", linewidth=1, linestyle="solid",\
             bottom=None, cumulative=False, normed=False, align="mid", orientation="vertical")

    pad.hist(x=xData, bins=xBinning, weights=y14_THT_0_weights+y14_THT_1_weights+y14_THT_2_weights+y14_THT_3_weights+y14_THT_4_weights,\
             label="$bg\_vbf\_400\_600$", histtype="step", rwidth=1.0,\
             color=None, edgecolor="#84c1a3", linewidth=1, linestyle="solid",\
             bottom=None, cumulative=False, normed=False, align="mid", orientation="vertical")

    pad.hist(x=xData, bins=xBinning, weights=y14_THT_0_weights+y14_THT_1_weights+y14_THT_2_weights+y14_THT_3_weights,\
             label="$bg\_vbf\_200\_400$", histtype="step", rwidth=1.0,\
             color=None, edgecolor="#89a8a0", linewidth=1, linestyle="solid",\
             bottom=None, cumulative=False, normed=False, align="mid", orientation="vertical")

    pad.hist(x=xData, bins=xBinning, weights=y14_THT_0_weights+y14_THT_1_weights+y14_THT_2_weights,\
             label="$bg\_vbf\_100\_200$", histtype="step", rwidth=1.0,\
             color=None, edgecolor="#829e8c", linewidth=1, linestyle="solid",\
             bottom=None, cumulative=False, normed=False, align="mid", orientation="vertical")

    pad.hist(x=xData, bins=xBinning, weights=y14_THT_0_weights+y14_THT_1_weights,\
             label="$bg\_vbf\_0\_100$", histtype="step", rwidth=1.0,\
             color=None, edgecolor="#adbcc6", linewidth=1, linestyle="solid",\
             bottom=None, cumulative=False, normed=False, align="mid", orientation="vertical")

    pad.hist(x=xData, bins=xBinning, weights=y14_THT_0_weights,\
             label="$signal$", histtype="step", rwidth=1.0,\
             color=None, edgecolor="#7a8e99", linewidth=1, linestyle="solid",\
             bottom=None, cumulative=False, normed=False, align="mid", orientation="vertical")


    # Axis
    plt.rc('text',usetex=False)
    plt.xlabel(r"THT",\
               fontsize=16,color="black")
    plt.ylabel(r"$\mathrm{Events}$ $(\mathcal{L}_{\mathrm{int}} = 1000.0\ \mathrm{fb}^{-1})$ ",\
               fontsize=16,color="black")

    # Boundary of y-axis
    ymax=(y14_THT_0_weights+y14_THT_1_weights+y14_THT_2_weights+y14_THT_3_weights+y14_THT_4_weights+y14_THT_5_weights+y14_THT_6_weights+y14_THT_7_weights+y14_THT_8_weights+y14_THT_9_weights+y14_THT_10_weights+y14_THT_11_weights+y14_THT_12_weights+y14_THT_13_weights+y14_THT_14_weights+y14_THT_15_weights+y14_THT_16_weights).max()*1.1
    ymin=0 # linear scale
    #ymin=min([x for x in (y14_THT_0_weights+y14_THT_1_weights+y14_THT_2_weights+y14_THT_3_weights+y14_THT_4_weights+y14_THT_5_weights+y14_THT_6_weights+y14_THT_7_weights+y14_THT_8_weights+y14_THT_9_weights+y14_THT_10_weights+y14_THT_11_weights+y14_THT_12_weights+y14_THT_13_weights+y14_THT_14_weights+y14_THT_15_weights+y14_THT_16_weights) if x])/100. # log scale
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
    plt.savefig('../../HTML/MadAnalysis5job_0/selection_13.png')
    plt.savefig('../../PDF/MadAnalysis5job_0/selection_13.png')
    plt.savefig('../../DVI/MadAnalysis5job_0/selection_13.eps')

# Running!
if __name__ == '__main__':
    selection_13()
