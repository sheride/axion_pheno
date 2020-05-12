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
    y14_THT_0_weights = numpy.array([0.0,0.0,0.0,0.642771029248,2.50557937516,3.38580739355,3.82796820093,4.17596429193,4.28241219741,4.50758799746,4.84739569573,5.07257149578,5.07666349215,5.41237919405,5.45741515406,5.66621096866,6.07971460148,5.82588282688,6.29260641245,6.13293855422,6.28032642335,6.3785823361,6.65288609253,6.91900185623,7.58633726367,7.02954175808,7.13598966356,7.34888147452,7.41438541636,7.61908923459,7.95480493649,8.37649656204,8.16360475108,8.24548467838,8.29870863112,7.87701700556,7.98346491104,7.59862125276,7.56586528185,7.3161295036,6.73886201619,6.42361829611,6.4481822743,6.35401835791,6.27213843062,6.31717039063,5.96098670691,5.69077494684,5.36734323404,5.13397944125,5.21586336855,4.75323177934,4.839207703,4.42161207381,4.56080795021,4.38476410652,3.8893797464,3.79521583002,3.6232643827,3.61098199361,3.29573747353,3.32439624808,2.83310588433,2.91498781162,2.96002257163,2.5588025279,2.4769206006,2.64477805155,2.37047469512,2.23127561873,2.07979455323,2.14530009507,1.9569722623,1.92421949138,1.82596157863,1.78911481135,1.54346942947,1.49843466946,1.49024667673,1.63763334585])

    # Creating weights for histo: y14_THT_1
    y14_THT_1_weights = numpy.array([0.0,0.0,0.0,1.89440891827,10.825703072,22.3069398707,31.069039882,36.7685512411,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0])

    # Creating weights for histo: y14_THT_2
    y14_THT_2_weights = numpy.array([0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,60.4829361707,62.829799842,64.0589736153,63.8533193352,60.5210753912,57.6903849235,56.3238190503,52.0473091612,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0])

    # Creating weights for histo: y14_THT_3
    y14_THT_3_weights = numpy.array([0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,58.4035809794,55.2883046148,52.1948440818,47.1996280466,43.8209366885,41.7480670665,38.4197430603,35.4605981737,32.7814434376,30.9667400094,27.0722606438,25.9678514394,23.3214976387,21.6210774799,20.6762407234,18.7504674939,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0])

    # Creating weights for histo: y14_THT_4
    y14_THT_4_weights = numpy.array([0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,17.6471464906,15.7393332201,14.3004707015,12.4607624118,11.2777815813,9.8486311673,8.78003912744,7.83948813907,6.97013653705,6.11347921283,5.64367469358,4.94805071658,4.45769565667,3.99771106518,3.51415608178,3.2269555621,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0])

    # Creating weights for histo: y14_THT_5
    y14_THT_5_weights = numpy.array([0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,2.90011176759,2.61276908722,2.33549048241,2.11113729617,1.90922603016,1.73235372323,1.58101489701,1.38239804136,1.2598871062,1.15476884928,1.02168251279,0.882264218773,0.867135297371,0.760233401713,0.714120458881,0.617861581186,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0])

    # Creating weights for histo: y14_THT_6
    y14_THT_6_weights = numpy.array([0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.564963666954,0.519137554179,0.460719396965,0.42891494548,0.407603247903,0.345850717562,0.320647235238,0.290017186857,0.264223503995,0.237646985698,0.234448566623,0.194674308586,0.179806633211,0.16173054214,0.145120755522,0.134881515938])

    # Creating weights for histo: y14_THT_7
    y14_THT_7_weights = numpy.array([0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0])

    # Creating weights for histo: y14_THT_8
    y14_THT_8_weights = numpy.array([0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0])

    # Creating weights for histo: y14_THT_9
    y14_THT_9_weights = numpy.array([0.0,0.0,0.0,0.0,2.59864517509,31.2893900254,41.7145995778,41.6936382986,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0])

    # Creating weights for histo: y14_THT_10
    y14_THT_10_weights = numpy.array([0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,62.1460220858,55.8298668845,69.5043719458,53.7213523348,60.0186152088,70.5756169243,58.9814995466,65.295615454,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0])

    # Creating weights for histo: y14_THT_11
    y14_THT_11_weights = numpy.array([0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,61.0448790667,64.0286740996,64.0345914308,55.9664640706,57.5865832373,54.1326677698,55.7431424551,47.2146544144,50.2122053211,47.9031013148,43.5320763638,43.3109833535,44.4436527585,43.0784399232,42.8505074002,39.1530975974,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0])

    # Creating weights for histo: y14_THT_12
    y14_THT_12_weights = numpy.array([0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,40.0714057895,37.4384389827,32.1769257774,26.360895618,24.0333178591,19.910565712,19.05110983,16.3935903285,14.6481253367,12.4884923183,10.9108297213,10.412443105,8.25222531544,7.198610017,7.25524048797,6.39666176264,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0])

    # Creating weights for histo: y14_THT_13
    y14_THT_13_weights = numpy.array([0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,5.25255677098,5.41447288943,4.57705778766,3.93228889895,3.78079373154,3.26609316597,2.78250557728,2.60143988424,2.48998655678,1.93573868225,1.79446058563,1.83486771104,1.42159636025,1.17974401101,1.14956245139,1.14917653519,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0])

    # Creating weights for histo: y14_THT_14
    y14_THT_14_weights = numpy.array([0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.888297015428,1.02706896958,0.826056275454,0.775103948244,0.679056833932,0.670460388863,0.676162882097,0.517788463179,0.520626628918,0.45838704314,0.356372932552,0.410194011671,0.339526839566,0.2829665477,0.268746017717,0.240505556859])

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
