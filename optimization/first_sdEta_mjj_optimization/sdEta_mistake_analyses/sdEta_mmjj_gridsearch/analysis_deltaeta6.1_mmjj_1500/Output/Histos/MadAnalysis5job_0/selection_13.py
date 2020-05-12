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
    xBinning = numpy.linspace(0.0,1000.0,81,endpoint=True)

    # Creating data sequence: middle of each bin
    xData = numpy.array([6.25,18.75,31.25,43.75,56.25,68.75,81.25,93.75,106.25,118.75,131.25,143.75,156.25,168.75,181.25,193.75,206.25,218.75,231.25,243.75,256.25,268.75,281.25,293.75,306.25,318.75,331.25,343.75,356.25,368.75,381.25,393.75,406.25,418.75,431.25,443.75,456.25,468.75,481.25,493.75,506.25,518.75,531.25,543.75,556.25,568.75,581.25,593.75,606.25,618.75,631.25,643.75,656.25,668.75,681.25,693.75,706.25,718.75,731.25,743.75,756.25,768.75,781.25,793.75,806.25,818.75,831.25,843.75,856.25,868.75,881.25,893.75,906.25,918.75,931.25,943.75,956.25,968.75,981.25,993.75])

    # Creating weights for histo: y14_THT_0
    y14_THT_0_weights = numpy.array([0.0,0.0,0.0,6.5095949214,21.1050035345,28.9820213891,33.1129541662,37.2397909466,39.8067809439,42.3246469795,44.6214051877,47.3972030221,48.875161869,50.9263202687,52.8136787963,54.6396373717,55.7081965381,56.637555813,57.5914750688,58.6641142319,58.9015940467,59.6098734941,60.8749525071,59.6507934622,61.656911897,61.7387918332,60.2321530086,60.5310327754,60.5719927435,60.2690329798,60.07659313,60.0479531523,59.5238735612,58.5822342958,58.6149942703,58.1155146599,57.2762353147,55.8719564103,55.6549965796,55.2251169149,54.717437311,52.9323987037,52.9774386685,52.5311990167,51.7410396331,51.491279828,49.8372811184,50.0952009172,48.4002822395,47.4954829454,46.5702036673,45.1127248043,45.6940843508,44.7156051142,43.0861263854,42.4433668869,41.0964079378,40.6992882476,40.2448486021,39.1230694773,37.5755066847,36.830383266,35.5489322657,35.6963201508,34.2470132815,33.4159179299,32.4374306932,32.3187027859,31.4835074375,31.049535776,29.530628961,29.0270573539,28.286029932,27.2338467529,26.2717395035,26.2635515099,24.5153768738,24.0568412315,23.4468217075,23.287149832])

    # Creating weights for histo: y14_THT_1
    y14_THT_1_weights = numpy.array([0.0,0.0,0.0,128.355203897,540.10916779,898.481420235,1125.05262026,1242.73821133,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0])

    # Creating weights for histo: y14_THT_2
    y14_THT_2_weights = numpy.array([0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,1329.56129523,1331.80337594,1277.32775677,1183.88472538,1067.52420782,956.796990331,853.683178111,756.400180637,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0])

    # Creating weights for histo: y14_THT_3
    y14_THT_3_weights = numpy.array([0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,697.418571648,620.484145563,553.23040658,492.187923844,433.74263917,388.327301768,343.912899231,304.830898166,273.707218974,246.771110323,216.749727002,194.334238005,172.836563785,155.247118108,140.128890341,124.889760628,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0])

    # Creating weights for histo: y14_THT_4
    y14_THT_4_weights = numpy.array([0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,114.771801681,103.945360762,94.0644031228,85.1520167049,76.9888259791,70.1053726061,63.6438353345,58.2347234062,52.7310551333,48.2796518706,44.3866881982,40.7696574958,36.9100430726,33.9221748153,31.2683562064,28.647979038,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0])

    # Creating weights for histo: y14_THT_5
    y14_THT_5_weights = numpy.array([0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,26.2191123089,24.3547872383,22.526195005,20.909979295,19.2333926545,17.8391478406,16.4913505138,15.3220213243,14.086715818,13.1766987596,12.2434439542,11.4241013207,10.6311612169,9.79571460067,9.10226710257,8.53441466568,0.000251448706357,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0])

    # Creating weights for histo: y14_THT_6
    y14_THT_6_weights = numpy.array([0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,8.02431558262,7.51030804877,6.95208235154,6.61078486788,6.21951215253,5.74100470726,5.48699893441,5.10793312325,4.79790514766,4.51395242298,4.23149219752,3.93685705714,3.75133430602,3.49375773129,3.27720739094,3.08477395858])

    # Creating weights for histo: y14_THT_7
    y14_THT_7_weights = numpy.array([0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0])

    # Creating weights for histo: y14_THT_8
    y14_THT_8_weights = numpy.array([0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0])

    # Creating weights for histo: y14_THT_9
    y14_THT_9_weights = numpy.array([0.0,0.0,0.0,45503.4508982,138097.118561,178482.936154,181502.27482,171105.624592,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0])

    # Creating weights for histo: y14_THT_10
    y14_THT_10_weights = numpy.array([0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,160424.802241,157100.582391,146319.155163,117179.124838,93107.5900059,74054.4547792,59162.2792087,48131.4114061,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0])

    # Creating weights for histo: y14_THT_11
    y14_THT_11_weights = numpy.array([0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,38962.5545651,32355.4487352,26998.4370463,22670.6752968,19174.8034575,16215.8131434,13782.4002913,11839.5153891,10294.1439018,8822.55620979,7548.61672003,6661.14017414,5800.7249869,5069.22299628,4461.124336,3970.54643612,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0])

    # Creating weights for histo: y14_THT_12
    y14_THT_12_weights = numpy.array([0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,3511.0949143,3146.79112757,2820.84302489,2519.97871399,2263.17156094,2043.11621581,1834.28800363,1661.79187548,1505.52917439,1359.61453285,1231.31713763,1124.97734144,1025.34812608,928.286497499,856.582962369,783.520229737,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0])

    # Creating weights for histo: y14_THT_13
    y14_THT_13_weights = numpy.array([0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,699.460949776,650.756719831,602.350018966,555.76332466,510.87490668,470.624981011,433.548961819,405.021973172,373.599309911,346.072378215,316.916955721,296.3685161,276.853327069,257.440753105,239.772513915,223.559394,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0])

    # Creating weights for histo: y14_THT_14
    y14_THT_14_weights = numpy.array([0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,203.115551013,192.915824447,181.154470828,168.440151122,158.522055294,149.341201024,139.273825515,130.652231411,122.84767424,116.084073524,108.238656811,101.433504019,95.1085470256,89.8081949754,85.2192298579,80.4755217311])

    # Creating weights for histo: y14_THT_15
    y14_THT_15_weights = numpy.array([0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0])

    # Creating weights for histo: y14_THT_16
    y14_THT_16_weights = numpy.array([0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0])

    # Creating a new Canvas
    fig   = plt.figure(figsize=(12,6),dpi=80)
    frame = gridspec.GridSpec(1,1,right=0.7)
    pad   = fig.add_subplot(frame[0])

    # Creating a new Stack
    pad.hist(x=xData, bins=xBinning, weights=y14_THT_0_weights+y14_THT_1_weights+y14_THT_2_weights+y14_THT_3_weights+y14_THT_4_weights+y14_THT_5_weights+y14_THT_6_weights+y14_THT_7_weights+y14_THT_8_weights+y14_THT_9_weights+y14_THT_10_weights+y14_THT_11_weights+y14_THT_12_weights+y14_THT_13_weights+y14_THT_14_weights+y14_THT_15_weights+y14_THT_16_weights,\
             label="$bg\_dip\_1600\_inf$", histtype="step", rwidth=1.0,\
             color=None, edgecolor="#e5e5e5", linewidth=4, linestyle="dashdot",\
             bottom=None, cumulative=False, normed=False, align="mid", orientation="vertical")

    pad.hist(x=xData, bins=xBinning, weights=y14_THT_0_weights+y14_THT_1_weights+y14_THT_2_weights+y14_THT_3_weights+y14_THT_4_weights+y14_THT_5_weights+y14_THT_6_weights+y14_THT_7_weights+y14_THT_8_weights+y14_THT_9_weights+y14_THT_10_weights+y14_THT_11_weights+y14_THT_12_weights+y14_THT_13_weights+y14_THT_14_weights+y14_THT_15_weights,\
             label="$bg\_dip\_1200\_1600$", histtype="step", rwidth=1.0,\
             color=None, edgecolor="#f2f2f2", linewidth=4, linestyle="dashdot",\
             bottom=None, cumulative=False, normed=False, align="mid", orientation="vertical")

    pad.hist(x=xData, bins=xBinning, weights=y14_THT_0_weights+y14_THT_1_weights+y14_THT_2_weights+y14_THT_3_weights+y14_THT_4_weights+y14_THT_5_weights+y14_THT_6_weights+y14_THT_7_weights+y14_THT_8_weights+y14_THT_9_weights+y14_THT_10_weights+y14_THT_11_weights+y14_THT_12_weights+y14_THT_13_weights+y14_THT_14_weights,\
             label="$bg\_dip\_800\_1200$", histtype="step", rwidth=1.0,\
             color=None, edgecolor="#ccc6aa", linewidth=4, linestyle="dashdot",\
             bottom=None, cumulative=False, normed=False, align="mid", orientation="vertical")

    pad.hist(x=xData, bins=xBinning, weights=y14_THT_0_weights+y14_THT_1_weights+y14_THT_2_weights+y14_THT_3_weights+y14_THT_4_weights+y14_THT_5_weights+y14_THT_6_weights+y14_THT_7_weights+y14_THT_8_weights+y14_THT_9_weights+y14_THT_10_weights+y14_THT_11_weights+y14_THT_12_weights+y14_THT_13_weights,\
             label="$bg\_dip\_600\_800$", histtype="step", rwidth=1.0,\
             color=None, edgecolor="#ccc6aa", linewidth=4, linestyle="dashdot",\
             bottom=None, cumulative=False, normed=False, align="mid", orientation="vertical")

    pad.hist(x=xData, bins=xBinning, weights=y14_THT_0_weights+y14_THT_1_weights+y14_THT_2_weights+y14_THT_3_weights+y14_THT_4_weights+y14_THT_5_weights+y14_THT_6_weights+y14_THT_7_weights+y14_THT_8_weights+y14_THT_9_weights+y14_THT_10_weights+y14_THT_11_weights+y14_THT_12_weights,\
             label="$bg\_dip\_400\_600$", histtype="step", rwidth=1.0,\
             color=None, edgecolor="#c1bfa8", linewidth=4, linestyle="dashdot",\
             bottom=None, cumulative=False, normed=False, align="mid", orientation="vertical")

    pad.hist(x=xData, bins=xBinning, weights=y14_THT_0_weights+y14_THT_1_weights+y14_THT_2_weights+y14_THT_3_weights+y14_THT_4_weights+y14_THT_5_weights+y14_THT_6_weights+y14_THT_7_weights+y14_THT_8_weights+y14_THT_9_weights+y14_THT_10_weights+y14_THT_11_weights,\
             label="$bg\_dip\_200\_400$", histtype="step", rwidth=1.0,\
             color=None, edgecolor="#bab5a3", linewidth=4, linestyle="dashdot",\
             bottom=None, cumulative=False, normed=False, align="mid", orientation="vertical")

    pad.hist(x=xData, bins=xBinning, weights=y14_THT_0_weights+y14_THT_1_weights+y14_THT_2_weights+y14_THT_3_weights+y14_THT_4_weights+y14_THT_5_weights+y14_THT_6_weights+y14_THT_7_weights+y14_THT_8_weights+y14_THT_9_weights+y14_THT_10_weights,\
             label="$bg\_dip\_100\_200$", histtype="step", rwidth=1.0,\
             color=None, edgecolor="#b2a596", linewidth=4, linestyle="dashdot",\
             bottom=None, cumulative=False, normed=False, align="mid", orientation="vertical")

    pad.hist(x=xData, bins=xBinning, weights=y14_THT_0_weights+y14_THT_1_weights+y14_THT_2_weights+y14_THT_3_weights+y14_THT_4_weights+y14_THT_5_weights+y14_THT_6_weights+y14_THT_7_weights+y14_THT_8_weights+y14_THT_9_weights,\
             label="$bg\_dip\_0\_100$", histtype="step", rwidth=1.0,\
             color=None, edgecolor="#b7a39b", linewidth=4, linestyle="dashdot",\
             bottom=None, cumulative=False, normed=False, align="mid", orientation="vertical")

    pad.hist(x=xData, bins=xBinning, weights=y14_THT_0_weights+y14_THT_1_weights+y14_THT_2_weights+y14_THT_3_weights+y14_THT_4_weights+y14_THT_5_weights+y14_THT_6_weights+y14_THT_7_weights+y14_THT_8_weights,\
             label="$bg\_vbf\_1600\_inf$", histtype="step", rwidth=1.0,\
             color=None, edgecolor="#ad998c", linewidth=4, linestyle="dashdot",\
             bottom=None, cumulative=False, normed=False, align="mid", orientation="vertical")

    pad.hist(x=xData, bins=xBinning, weights=y14_THT_0_weights+y14_THT_1_weights+y14_THT_2_weights+y14_THT_3_weights+y14_THT_4_weights+y14_THT_5_weights+y14_THT_6_weights+y14_THT_7_weights,\
             label="$bg\_vbf\_1200\_1600$", histtype="step", rwidth=1.0,\
             color=None, edgecolor="#9b8e82", linewidth=4, linestyle="dashdot",\
             bottom=None, cumulative=False, normed=False, align="mid", orientation="vertical")

    pad.hist(x=xData, bins=xBinning, weights=y14_THT_0_weights+y14_THT_1_weights+y14_THT_2_weights+y14_THT_3_weights+y14_THT_4_weights+y14_THT_5_weights+y14_THT_6_weights,\
             label="$bg\_vbf\_800\_1200$", histtype="step", rwidth=1.0,\
             color=None, edgecolor="#876656", linewidth=4, linestyle="dashdot",\
             bottom=None, cumulative=False, normed=False, align="mid", orientation="vertical")

    pad.hist(x=xData, bins=xBinning, weights=y14_THT_0_weights+y14_THT_1_weights+y14_THT_2_weights+y14_THT_3_weights+y14_THT_4_weights+y14_THT_5_weights,\
             label="$bg\_vbf\_600\_800$", histtype="step", rwidth=1.0,\
             color=None, edgecolor="#afcec6", linewidth=4, linestyle="dashdot",\
             bottom=None, cumulative=False, normed=False, align="mid", orientation="vertical")

    pad.hist(x=xData, bins=xBinning, weights=y14_THT_0_weights+y14_THT_1_weights+y14_THT_2_weights+y14_THT_3_weights+y14_THT_4_weights,\
             label="$bg\_vbf\_400\_600$", histtype="step", rwidth=1.0,\
             color=None, edgecolor="#84c1a3", linewidth=4, linestyle="dashdot",\
             bottom=None, cumulative=False, normed=False, align="mid", orientation="vertical")

    pad.hist(x=xData, bins=xBinning, weights=y14_THT_0_weights+y14_THT_1_weights+y14_THT_2_weights+y14_THT_3_weights,\
             label="$bg\_vbf\_200\_400$", histtype="step", rwidth=1.0,\
             color=None, edgecolor="#89a8a0", linewidth=4, linestyle="dashdot",\
             bottom=None, cumulative=False, normed=False, align="mid", orientation="vertical")

    pad.hist(x=xData, bins=xBinning, weights=y14_THT_0_weights+y14_THT_1_weights+y14_THT_2_weights,\
             label="$bg\_vbf\_100\_200$", histtype="step", rwidth=1.0,\
             color=None, edgecolor="#829e8c", linewidth=4, linestyle="dashdot",\
             bottom=None, cumulative=False, normed=False, align="mid", orientation="vertical")

    pad.hist(x=xData, bins=xBinning, weights=y14_THT_0_weights+y14_THT_1_weights,\
             label="$bg\_vbf\_0\_100$", histtype="step", rwidth=1.0,\
             color=None, edgecolor="#adbcc6", linewidth=4, linestyle="dashdot",\
             bottom=None, cumulative=False, normed=False, align="mid", orientation="vertical")

    pad.hist(x=xData, bins=xBinning, weights=y14_THT_0_weights,\
             label="$signal$", histtype="step", rwidth=1.0,\
             color=None, edgecolor="#7a8e99", linewidth=3, linestyle="dashed",\
             bottom=None, cumulative=False, normed=False, align="mid", orientation="vertical")


    # Axis
    plt.rc('text',usetex=False)
    plt.xlabel(r"THT",\
               fontsize=16,color="black")
    plt.ylabel(r"$\mathrm{Events}$ $(\mathcal{L}_{\mathrm{int}} = 40.0\ \mathrm{fb}^{-1})$ ",\
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
