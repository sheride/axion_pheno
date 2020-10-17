def selection_9():

    # Library import
    import numpy
    import matplotlib
    import matplotlib.pyplot   as plt
    import matplotlib.gridspec as gridspec

    # Library version
    matplotlib_version = matplotlib.__version__
    numpy_version      = numpy.__version__

    # Histo binning
    xBinning = numpy.linspace(500.0,4000.0,41,endpoint=True)

    # Creating data sequence: middle of each bin
    xData = numpy.array([543.75,631.25,718.75,806.25,893.75,981.25,1068.75,1156.25,1243.75,1331.25,1418.75,1506.25,1593.75,1681.25,1768.75,1856.25,1943.75,2031.25,2118.75,2206.25,2293.75,2381.25,2468.75,2556.25,2643.75,2731.25,2818.75,2906.25,2993.75,3081.25,3168.75,3256.25,3343.75,3431.25,3518.75,3606.25,3693.75,3781.25,3868.75,3956.25])

    # Creating weights for histo: y10_M_0
    y10_M_0_weights = numpy.array([176.46067525,232.052410604,227.276021003,232.052410604,222.234281424,205.915002788,201.271303177,186.27877443,178.848855051,169.030725871,147.27166769,131.350429021,121.797649819,113.571680507,103.355541361,89.2917525365,93.2720622038,77.7488335013,65.1445145548,60.3681249541,61.4295248654,51.7441156749,50.0192958191,40.0685066508,35.8228470057,35.9555069946,30.6484174382,29.9850454937,27.7295316822,21.3610272145,19.238191392,19.105516403,16.8500025916,13.9311048356,14.9925227468,10.8795290906,9.42008021261,7.69527835678,9.2874022237,8.49134029024])

    # Creating weights for histo: y10_M_1
    y10_M_1_weights = numpy.array([115.567907729,144.897843886,152.751928136,149.067048438,143.531290601,136.480357665,130.473794223,119.981148218,113.957198602,98.5779585291,90.4830457908,90.8901820267,83.7485412245,73.3281377701,70.5274949061,61.1474141631,59.8678217245,52.4949148305,44.2419078124,42.1538582777,36.0664791023,32.3783320021,31.2561443916,25.4042639422,25.9668775389,21.9576048052,21.8785936367,19.2353256245,15.8695871375,15.5470556221,14.1043658823,13.7852486517,11.7020462624,9.6181694094,8.73569817092,7.93241196268,6.8117201627,5.60960411316,5.6095561513,4.40845329605])

    # Creating weights for histo: y10_M_2
    y10_M_2_weights = numpy.array([79.6374791156,95.6795629663,103.336014804,102.867234692,98.6483936789,95.6795629663,88.700211291,84.0125901658,76.5124083655,72.3456173653,64.6891655275,57.8660838898,51.667992402,46.2511911018,46.3553511268,42.2406701392,35.7300985764,33.8550381263,32.5008378013,29.1674200011,26.042340251,22.1880743259,22.5005814009,18.8546535257,17.6046222257,15.1566426381,13.8545253255,11.6669698005,11.3023767129,10.6252735504,8.75022510034,8.28146298783,6.66683860026,6.66683860026,5.46889031272,4.84387616269,4.53136608768,4.37511405017,3.59384186264,3.69801088765])

    # Creating weights for histo: y10_M_3
    y10_M_3_weights = numpy.array([56.3296971344,66.0024500767,71.3367216993,68.669570888,68.6340208771,66.2513901524,60.0636482702,58.4278377726,53.0224361284,50.568705382,46.5857841705,42.5673129482,39.6157020503,34.032520352,31.6498896273,29.9784871189,27.0624322319,25.2487846802,23.5062641502,19.3811098954,18.5987546574,15.8249448136,14.5091624134,12.8022008942,11.6997905589,11.4508564831,9.92170501799,8.25030850958,7.71688134733,7.00565013098,5.61874370911,6.57890900118,5.76099175238,4.80082646032,3.48504406008,3.59173009254,3.16498896273,2.77381014374,2.16926195985,1.99145340576])

    # Creating weights for histo: y10_M_4
    y10_M_4_weights = numpy.array([0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0])

    # Creating weights for histo: y10_M_5
    y10_M_5_weights = numpy.array([0.0,78.9085275503,158.069001296,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0])

    # Creating weights for histo: y10_M_6
    y10_M_6_weights = numpy.array([431.886384623,345.468298229,259.23296102,69.0686148513,69.102565102,17.3004886513,34.5703759645,17.2486900217,51.8012233715,34.5060779939,17.3004886513,0.0,17.2964768729,17.2596417155,34.5442071804,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,17.2515144059,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0])

    # Creating weights for histo: y10_M_7
    y10_M_7_weights = numpy.array([303.232533396,180.660599217,139.153907595,66.4489221758,51.9282705759,37.3800954483,49.8790083346,16.6057550138,12.4565024189,4.15832324172,14.5418193277,10.3750543834,6.22338410345,8.3041368381,2.07715246103,2.0802989138,2.07522090947,0.0,4.1490939162,2.07028600441,0.0,2.07793921848,0.0,2.0794792666,0.0,0.0,0.0,2.07697012487,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0])

    # Creating weights for histo: y10_M_8
    y10_M_8_weights = numpy.array([77.1216332539,62.0060265446,34.0337768278,22.6840791223,15.1173864029,7.56154935934,9.07259569428,7.56377511423,10.5877658205,5.29293161623,2.27210475911,1.51369994456,3.77981837884,3.02303577093,0.0,0.754445792862,1.51069904435,1.51297987416,0.751764418205,1.51367035886,0.756398448995,0.0,0.0,0.0,0.757503588643,0.0,0.0,0.0,0.757313785005,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0])

    # Creating weights for histo: y10_M_9
    y10_M_9_weights = numpy.array([30.9752704771,18.890676357,15.9121277006,11.2458155059,8.06650235642,5.51680339371,4.6678069272,3.39409869423,2.54627088916,2.33445201308,1.69784057419,1.48398418739,0.424144172122,0.42396642016,0.211939522341,0.0,0.212060774573,1.06150326577,0.211939522341,0.211760962415,0.0,0.424843637636,0.212260572395,0.0,0.0,0.0,0.0,0.211607074231,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0])

    # Creating weights for histo: y10_M_10
    y10_M_10_weights = numpy.array([1.71197029584,1.48402463275,0.800874885228,0.229337431742,0.802187585187,0.685610539175,0.0,0.685668776994,0.114337238966,0.114483321046,0.457163605358,0.0,0.113449045733,0.0,0.226898091465,0.0,0.0,0.227673975235,0.114071224206,0.0,0.115000192777,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0])

    # Creating weights for histo: y10_M_11
    y10_M_11_weights = numpy.array([0.0947974410912,0.189590810973,0.0677245643041,0.0948292022973,0.0542057822538,0.0406224672073,0.0134999014569,0.0541923559257,0.0,0.0,0.027015495837,0.0135876316831,0.0135550735594,0.0,0.0135002710418,0.0,0.0135115924682,0.0135566269711,0.0,0.0,0.0135575220597,0.0135257781778,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0])

    # Creating weights for histo: y10_M_12
    y10_M_12_weights = numpy.array([0.0,0.912787033803,0.0,0.909306167943,0.913150150035,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.909853848219,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0])

    # Creating weights for histo: y10_M_13
    y10_M_13_weights = numpy.array([14.3002261044,15.815033764,12.8022151729,12.8052739128,5.2694745129,6.02194933975,4.51375190541,1.50452787608,3.76368812183,6.03187862333,2.26192271872,0.751971234906,1.5068211563,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0])

    # Creating weights for histo: y10_M_14
    y10_M_14_weights = numpy.array([116.750461706,80.8489064136,70.1332998558,42.4900910105,40.0147321172,25.1574599103,22.2769472802,11.1408395836,8.25449817055,10.3113638539,5.77703689351,5.36263266782,1.23823276966,3.30095587715,2.06156314007,1.23641679755,1.65109981761,0.412044376027,1.23757767905,0.0,0.0,0.0,0.82497662835,0.410615973805,0.0,0.41322963299,0.824565901772,0.412044376027,0.0,0.413566319094,0.41219855084,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0])

    # Creating weights for histo: y10_M_15
    y10_M_15_weights = numpy.array([105.173460652,69.0559589939,46.0369352292,29.3067519022,22.9470880002,16.650686927,10.5847995603,8.21429230764,7.32695928663,4.44075055386,2.81293009119,2.29547057539,1.70226882325,1.77636876329,0.888337097464,0.888376478905,0.51800875163,0.221967753398,0.148049990104,0.222051747099,0.147781595058,0.295865525351,0.0741429590035,0.22238964588,0.0739651412732,0.148190380434,0.0,0.147762415394,0.0,0.0740800388835,0.0,0.148067606535,0.147993743785,0.0,0.0,0.073932583944,0.0,0.0,0.0,0.0])

    # Creating weights for histo: y10_M_16
    y10_M_16_weights = numpy.array([36.071649539,23.7445032819,17.4691217867,12.3831779762,8.6965177207,6.29554415168,4.44296843017,3.53588295645,2.64753203852,1.81479152153,1.19137832922,1.07795040816,0.945233675814,0.661670925132,0.567417483276,0.283617876147,0.321355353017,0.245698908361,0.151245520412,0.11348814796,0.0756458816923,0.0567285746318,0.075619114183,0.0,0.0566696080894,0.0,0.0,0.0,0.0188733537298,0.0,0.0189064650189,0.0,0.0,0.0188968623249,0.0,0.0,0.0,0.0,0.0,0.0])

    # Creating weights for histo: y10_M_17
    y10_M_17_weights = numpy.array([12.239368935,9.08260974103,6.61203027319,4.89685575338,3.41533988202,2.34079576656,2.01902785968,1.67520583345,0.944491242049,0.94514280354,0.493499871795,0.536815064947,0.429522906458,0.257739356465,0.171821638974,0.150352125482,0.0857590633925,0.128961264235,0.0643875915357,0.0426650487499,0.107311427914,0.0426027342786,0.0,0.0,0.0,0.0427797880538,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0])

    # Creating weights for histo: y10_M_18
    y10_M_18_weights = numpy.array([1.04779044477,0.779111479224,0.521424025918,0.401587027723,0.270571401637,0.236365132845,0.197527555215,0.150412569549,0.105289942815,0.0940056714331,0.0583188221486,0.0680496218575,0.0372721931684,0.0437476583011,0.0194314025412,0.0226730138362,0.0113404500826,0.0129620792527,0.00810970174238,0.00324519141805,0.00323792744573,0.00486698717858,0.00162106527712,0.00485074932442,0.00162219023415,0.00324236881003,0.0,0.00161444629275,0.0,0.00323712906885,0.00161870660779,0.0,0.0,0.0,0.0,0.0,0.0,0.00161842371835,0.0,0.0])

    # Creating weights for histo: y10_M_19
    y10_M_19_weights = numpy.array([0.0829551828044,0.0553342510094,0.0614457300278,0.0638546406694,0.0255513801011,0.0403435792613,0.0105847050275,0.0255709355867,0.00425990862504,0.0170424052318,0.00851587719838,0.0127698657231,0.00213366829569,0.00426130512726,0.00213366829569,0.0,0.00635995618555,0.0,0.0063660644907,0.0,0.0,0.00213219495244,0.0,0.0,0.00212624032935,0.0,0.0,0.0,0.00212763683157,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0])

    # Creating a new Canvas
    fig   = plt.figure(figsize=(12,6),dpi=80)
    frame = gridspec.GridSpec(1,1,right=0.7)
    pad   = fig.add_subplot(frame[0])

    # Creating a new Stack
    pad.hist(x=xData, bins=xBinning, weights=y10_M_0_weights+y10_M_1_weights+y10_M_2_weights+y10_M_3_weights+y10_M_4_weights+y10_M_5_weights+y10_M_6_weights+y10_M_7_weights+y10_M_8_weights+y10_M_9_weights+y10_M_10_weights+y10_M_11_weights+y10_M_12_weights+y10_M_13_weights+y10_M_14_weights+y10_M_15_weights+y10_M_16_weights+y10_M_17_weights+y10_M_18_weights+y10_M_19_weights,\
             label="$bg\_vbf\_1600\_inf$", histtype="step", rwidth=1.0,\
             color=None, edgecolor="#ccc6aa", linewidth=1, linestyle="solid",\
             bottom=None, cumulative=False, normed=False, align="mid", orientation="vertical")

    pad.hist(x=xData, bins=xBinning, weights=y10_M_0_weights+y10_M_1_weights+y10_M_2_weights+y10_M_3_weights+y10_M_4_weights+y10_M_5_weights+y10_M_6_weights+y10_M_7_weights+y10_M_8_weights+y10_M_9_weights+y10_M_10_weights+y10_M_11_weights+y10_M_12_weights+y10_M_13_weights+y10_M_14_weights+y10_M_15_weights+y10_M_16_weights+y10_M_17_weights+y10_M_18_weights,\
             label="$bg\_vbf\_1200\_1600$", histtype="step", rwidth=1.0,\
             color=None, edgecolor="#c1bfa8", linewidth=1, linestyle="solid",\
             bottom=None, cumulative=False, normed=False, align="mid", orientation="vertical")

    pad.hist(x=xData, bins=xBinning, weights=y10_M_0_weights+y10_M_1_weights+y10_M_2_weights+y10_M_3_weights+y10_M_4_weights+y10_M_5_weights+y10_M_6_weights+y10_M_7_weights+y10_M_8_weights+y10_M_9_weights+y10_M_10_weights+y10_M_11_weights+y10_M_12_weights+y10_M_13_weights+y10_M_14_weights+y10_M_15_weights+y10_M_16_weights+y10_M_17_weights,\
             label="$bg\_vbf\_800\_1200$", histtype="step", rwidth=1.0,\
             color=None, edgecolor="#bab5a3", linewidth=1, linestyle="solid",\
             bottom=None, cumulative=False, normed=False, align="mid", orientation="vertical")

    pad.hist(x=xData, bins=xBinning, weights=y10_M_0_weights+y10_M_1_weights+y10_M_2_weights+y10_M_3_weights+y10_M_4_weights+y10_M_5_weights+y10_M_6_weights+y10_M_7_weights+y10_M_8_weights+y10_M_9_weights+y10_M_10_weights+y10_M_11_weights+y10_M_12_weights+y10_M_13_weights+y10_M_14_weights+y10_M_15_weights+y10_M_16_weights,\
             label="$bg\_vbf\_600\_800$", histtype="step", rwidth=1.0,\
             color=None, edgecolor="#b2a596", linewidth=1, linestyle="solid",\
             bottom=None, cumulative=False, normed=False, align="mid", orientation="vertical")

    pad.hist(x=xData, bins=xBinning, weights=y10_M_0_weights+y10_M_1_weights+y10_M_2_weights+y10_M_3_weights+y10_M_4_weights+y10_M_5_weights+y10_M_6_weights+y10_M_7_weights+y10_M_8_weights+y10_M_9_weights+y10_M_10_weights+y10_M_11_weights+y10_M_12_weights+y10_M_13_weights+y10_M_14_weights+y10_M_15_weights,\
             label="$bg\_vbf\_400\_600$", histtype="step", rwidth=1.0,\
             color=None, edgecolor="#b7a39b", linewidth=1, linestyle="solid",\
             bottom=None, cumulative=False, normed=False, align="mid", orientation="vertical")

    pad.hist(x=xData, bins=xBinning, weights=y10_M_0_weights+y10_M_1_weights+y10_M_2_weights+y10_M_3_weights+y10_M_4_weights+y10_M_5_weights+y10_M_6_weights+y10_M_7_weights+y10_M_8_weights+y10_M_9_weights+y10_M_10_weights+y10_M_11_weights+y10_M_12_weights+y10_M_13_weights+y10_M_14_weights,\
             label="$bg\_vbf\_200\_400$", histtype="step", rwidth=1.0,\
             color=None, edgecolor="#ad998c", linewidth=1, linestyle="solid",\
             bottom=None, cumulative=False, normed=False, align="mid", orientation="vertical")

    pad.hist(x=xData, bins=xBinning, weights=y10_M_0_weights+y10_M_1_weights+y10_M_2_weights+y10_M_3_weights+y10_M_4_weights+y10_M_5_weights+y10_M_6_weights+y10_M_7_weights+y10_M_8_weights+y10_M_9_weights+y10_M_10_weights+y10_M_11_weights+y10_M_12_weights+y10_M_13_weights,\
             label="$bg\_vbf\_100\_200$", histtype="step", rwidth=1.0,\
             color=None, edgecolor="#9b8e82", linewidth=1, linestyle="solid",\
             bottom=None, cumulative=False, normed=False, align="mid", orientation="vertical")

    pad.hist(x=xData, bins=xBinning, weights=y10_M_0_weights+y10_M_1_weights+y10_M_2_weights+y10_M_3_weights+y10_M_4_weights+y10_M_5_weights+y10_M_6_weights+y10_M_7_weights+y10_M_8_weights+y10_M_9_weights+y10_M_10_weights+y10_M_11_weights+y10_M_12_weights,\
             label="$bg\_vbf\_0\_100$", histtype="step", rwidth=1.0,\
             color=None, edgecolor="#876656", linewidth=1, linestyle="solid",\
             bottom=None, cumulative=False, normed=False, align="mid", orientation="vertical")

    pad.hist(x=xData, bins=xBinning, weights=y10_M_0_weights+y10_M_1_weights+y10_M_2_weights+y10_M_3_weights+y10_M_4_weights+y10_M_5_weights+y10_M_6_weights+y10_M_7_weights+y10_M_8_weights+y10_M_9_weights+y10_M_10_weights+y10_M_11_weights,\
             label="$bg\_dip\_1600\_inf$", histtype="step", rwidth=1.0,\
             color=None, edgecolor="#afcec6", linewidth=1, linestyle="solid",\
             bottom=None, cumulative=False, normed=False, align="mid", orientation="vertical")

    pad.hist(x=xData, bins=xBinning, weights=y10_M_0_weights+y10_M_1_weights+y10_M_2_weights+y10_M_3_weights+y10_M_4_weights+y10_M_5_weights+y10_M_6_weights+y10_M_7_weights+y10_M_8_weights+y10_M_9_weights+y10_M_10_weights,\
             label="$bg\_dip\_1200\_1600$", histtype="step", rwidth=1.0,\
             color=None, edgecolor="#84c1a3", linewidth=1, linestyle="solid",\
             bottom=None, cumulative=False, normed=False, align="mid", orientation="vertical")

    pad.hist(x=xData, bins=xBinning, weights=y10_M_0_weights+y10_M_1_weights+y10_M_2_weights+y10_M_3_weights+y10_M_4_weights+y10_M_5_weights+y10_M_6_weights+y10_M_7_weights+y10_M_8_weights+y10_M_9_weights,\
             label="$bg\_dip\_800\_1200$", histtype="step", rwidth=1.0,\
             color=None, edgecolor="#89a8a0", linewidth=1, linestyle="solid",\
             bottom=None, cumulative=False, normed=False, align="mid", orientation="vertical")

    pad.hist(x=xData, bins=xBinning, weights=y10_M_0_weights+y10_M_1_weights+y10_M_2_weights+y10_M_3_weights+y10_M_4_weights+y10_M_5_weights+y10_M_6_weights+y10_M_7_weights+y10_M_8_weights,\
             label="$bg\_dip\_600\_800$", histtype="step", rwidth=1.0,\
             color=None, edgecolor="#829e8c", linewidth=1, linestyle="solid",\
             bottom=None, cumulative=False, normed=False, align="mid", orientation="vertical")

    pad.hist(x=xData, bins=xBinning, weights=y10_M_0_weights+y10_M_1_weights+y10_M_2_weights+y10_M_3_weights+y10_M_4_weights+y10_M_5_weights+y10_M_6_weights+y10_M_7_weights,\
             label="$bg\_dip\_400\_600$", histtype="step", rwidth=1.0,\
             color=None, edgecolor="#adbcc6", linewidth=1, linestyle="solid",\
             bottom=None, cumulative=False, normed=False, align="mid", orientation="vertical")

    pad.hist(x=xData, bins=xBinning, weights=y10_M_0_weights+y10_M_1_weights+y10_M_2_weights+y10_M_3_weights+y10_M_4_weights+y10_M_5_weights+y10_M_6_weights,\
             label="$bg\_dip\_200\_400$", histtype="step", rwidth=1.0,\
             color=None, edgecolor="#7a8e99", linewidth=1, linestyle="solid",\
             bottom=None, cumulative=False, normed=False, align="mid", orientation="vertical")

    pad.hist(x=xData, bins=xBinning, weights=y10_M_0_weights+y10_M_1_weights+y10_M_2_weights+y10_M_3_weights+y10_M_4_weights+y10_M_5_weights,\
             label="$bg\_dip\_100\_200$", histtype="step", rwidth=1.0,\
             color=None, edgecolor="#758991", linewidth=1, linestyle="solid",\
             bottom=None, cumulative=False, normed=False, align="mid", orientation="vertical")

    pad.hist(x=xData, bins=xBinning, weights=y10_M_0_weights+y10_M_1_weights+y10_M_2_weights+y10_M_3_weights+y10_M_4_weights,\
             label="$bg\_dip\_0\_100$", histtype="step", rwidth=1.0,\
             color=None, edgecolor="#688296", linewidth=1, linestyle="solid",\
             bottom=None, cumulative=False, normed=False, align="mid", orientation="vertical")

    pad.hist(x=xData, bins=xBinning, weights=y10_M_0_weights+y10_M_1_weights+y10_M_2_weights+y10_M_3_weights,\
             label="$signal\_2pt4TeVL$", histtype="step", rwidth=1.0,\
             color=None, edgecolor="#6d7a84", linewidth=1, linestyle="solid",\
             bottom=None, cumulative=False, normed=False, align="mid", orientation="vertical")

    pad.hist(x=xData, bins=xBinning, weights=y10_M_0_weights+y10_M_1_weights+y10_M_2_weights,\
             label="$signal\_2pt2TeVL$", histtype="step", rwidth=1.0,\
             color=None, edgecolor="#7c99d1", linewidth=1, linestyle="solid",\
             bottom=None, cumulative=False, normed=False, align="mid", orientation="vertical")

    pad.hist(x=xData, bins=xBinning, weights=y10_M_0_weights+y10_M_1_weights,\
             label="$signal\_2TeVL$", histtype="step", rwidth=1.0,\
             color=None, edgecolor="#7f7f9b", linewidth=1, linestyle="solid",\
             bottom=None, cumulative=False, normed=False, align="mid", orientation="vertical")

    pad.hist(x=xData, bins=xBinning, weights=y10_M_0_weights,\
             label="$signal\_1pt8TeVL$", histtype="step", rwidth=1.0,\
             color=None, edgecolor="#aaa5bf", linewidth=1, linestyle="solid",\
             bottom=None, cumulative=False, normed=False, align="mid", orientation="vertical")


    # Axis
    plt.rc('text',usetex=False)
    plt.xlabel(r"M [ a_{1} , a_{2} ]   ( GeV ) ",\
               fontsize=16,color="black")
    plt.ylabel(r"$\mathrm{Events}$ $(\mathcal{L}_{\mathrm{int}} = 3000.0\ \mathrm{fb}^{-1})$ ",\
               fontsize=16,color="black")

    # Boundary of y-axis
    ymax=(y10_M_0_weights+y10_M_1_weights+y10_M_2_weights+y10_M_3_weights+y10_M_4_weights+y10_M_5_weights+y10_M_6_weights+y10_M_7_weights+y10_M_8_weights+y10_M_9_weights+y10_M_10_weights+y10_M_11_weights+y10_M_12_weights+y10_M_13_weights+y10_M_14_weights+y10_M_15_weights+y10_M_16_weights+y10_M_17_weights+y10_M_18_weights+y10_M_19_weights).max()*1.1
    ymin=0 # linear scale
    #ymin=min([x for x in (y10_M_0_weights+y10_M_1_weights+y10_M_2_weights+y10_M_3_weights+y10_M_4_weights+y10_M_5_weights+y10_M_6_weights+y10_M_7_weights+y10_M_8_weights+y10_M_9_weights+y10_M_10_weights+y10_M_11_weights+y10_M_12_weights+y10_M_13_weights+y10_M_14_weights+y10_M_15_weights+y10_M_16_weights+y10_M_17_weights+y10_M_18_weights+y10_M_19_weights) if x])/100. # log scale
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
    plt.savefig('../../HTML/MadAnalysis5job_0/selection_9.png')
    plt.savefig('../../PDF/MadAnalysis5job_0/selection_9.png')
    plt.savefig('../../DVI/MadAnalysis5job_0/selection_9.eps')

# Running!
if __name__ == '__main__':
    selection_9()
