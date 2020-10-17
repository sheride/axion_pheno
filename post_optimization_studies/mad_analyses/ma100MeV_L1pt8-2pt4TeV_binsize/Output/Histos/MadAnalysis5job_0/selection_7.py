def selection_7():

    # Library import
    import numpy
    import matplotlib
    import matplotlib.pyplot   as plt
    import matplotlib.gridspec as gridspec

    # Library version
    matplotlib_version = matplotlib.__version__
    numpy_version      = numpy.__version__

    # Histo binning
    xBinning = numpy.linspace(750.0,6000.0,21,endpoint=True)

    # Creating data sequence: middle of each bin
    xData = numpy.array([881.25,1143.75,1406.25,1668.75,1931.25,2193.75,2456.25,2718.75,2981.25,3243.75,3506.25,3768.75,4031.25,4293.75,4556.25,4818.75,5081.25,5343.75,5606.25,5868.75])

    # Creating weights for histo: y8_M_0
    y8_M_0_weights = numpy.array([556.846139685,576.217137587,525.13644312,448.714151398,382.242858598,292.420528327,224.62248567,168.234671778,125.645296391,96.1909695811,65.6752128864,45.2429350995,32.7712764504,20.03425583,12.2063026779,9.95078892218,8.49134008026,3.98031556887,4.37834652576,1.19409467066])

    # Creating weights for histo: y8_M_1
    y8_M_1_weights = numpy.array([345.736664738,368.333895064,336.04207403,314.245207243,240.19380409,195.385796126,148.988961622,112.520292085,83.7509399285,59.3886532041,42.2331755112,30.6136055769,20.9147282774,14.2651671136,8.97627492427,7.29258282285,3.68689712112,2.88425299642,1.92352837982,1.52245691819])

    # Creating weights for histo: y8_M_2
    y8_M_2_weights = numpy.array([232.818536368,242.818768789,236.516547264,206.255329937,166.150120227,128.597071135,103.596415082,76.2519784615,56.5118836822,42.9698504035,29.011168024,20.1567708802,15.2087256822,10.2606834842,7.08351771501,4.73970714754,2.96882681879,1.61462499092,1.35420182787,0.781270089155])

    # Creating weights for histo: y8_M_3
    y8_M_3_weights = numpy.array([169.77140219,175.49684395,165.432890856,137.659212318,114.473015191,91.9269282597,71.0166518316,52.417906114,39.6157021784,29.907366194,20.5190853079,14.0112973073,10.4195702031,7.2901432411,4.69414044305,3.0938649511,1.92033029034,1.74252173568,0.568986774915,0.746795029576])

    # Creating weights for histo: y8_M_4
    y8_M_4_weights = numpy.array([0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0])

    # Creating weights for histo: y8_M_5
    y8_M_5_weights = numpy.array([0.0,157.880409317,79.0971195289,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0])

    # Creating weights for histo: y8_M_6
    y8_M_6_weights = numpy.array([587.379391599,431.646019427,241.972483967,69.1428839324,51.7944212727,34.5899157442,17.3128927115,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0])

    # Creating weights for histo: y8_M_7
    y8_M_7_weights = numpy.array([222.253013534,236.78229385,197.272667187,101.752854311,74.7652519532,49.8410778464,22.8325356777,2.07793955731,8.30798975567,4.14912921356,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0])

    # Creating weights for histo: y8_M_8
    y8_M_8_weights = numpy.array([36.3056646945,44.6289815042,43.8471908417,32.5124870417,38.562293246,30.2483983429,22.6859073156,9.0634417076,5.29110148876,3.0236950954,0.753221803182,0.75534287007,2.26722796885,0.0,0.0,0.0,0.0,0.0,0.0,0.0])

    # Creating weights for histo: y8_M_9
    y8_M_9_weights = numpy.array([6.153787524,15.7051307614,15.4887783389,12.5204330284,9.96863329331,9.33512643731,10.1866910959,9.12420179807,6.15119626968,5.51939479375,4.03053162194,2.54574635727,1.06101361022,1.48555946683,0.212260578002,0.212031289507,0.0,0.212281036791,0.0,0.424877698747])

    # Creating weights for histo: y8_M_10
    y8_M_10_weights = numpy.array([0.0,0.342229130968,0.910578099182,1.02754571386,1.02942758454,0.798495104572,0.800384243903,0.229144835782,0.113137214489,0.0,0.45840375388,0.457575393939,0.115000204415,0.57050970678,0.572815641021,0.113137214489,0.115000204415,0.0,0.114144631366,0.115222164104])

    # Creating weights for histo: y8_M_11
    y8_M_11_weights = numpy.array([0.0,0.0271125965826,0.0677184454599,0.0947422665806,0.0947957120304,0.0948460679809,0.0812186332474,0.027096664006,0.0406829015663,0.0270118644699,0.0135575225415,0.0135469604963,0.0271029209639,0.0,0.0406195812684,0.0,0.0135469604963,0.0270792299906,0.0135002715216,0.0270939181053])

    # Creating weights for histo: y8_M_12
    y8_M_12_weights = numpy.array([2.73194704997,0.913150150035,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0])

    # Creating weights for histo: y8_M_13
    y8_M_13_weights = numpy.array([25.5997769691,19.5787601161,18.0732649535,4.52159578422,7.52873711732,6.02253847545,3.76406330445,0.752556991122,0.0,0.754386037151,0.0,0.753054694938,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0])

    # Creating weights for histo: y8_M_14
    y8_M_14_weights = numpy.array([77.9670856012,92.8067768048,74.6868184437,60.6289093159,32.5934691537,35.4779092418,23.1072453713,16.0895370372,13.1999841955,5.36290986665,9.0681083979,3.7129803982,1.23649386834,2.06385227314,1.23831105919,2.06414569279,1.64965585386,0.0,0.413164727762,0.0])

    # Creating weights for histo: y8_M_15
    y8_M_15_weights = numpy.array([11.9137375642,30.4178365241,50.9931679587,57.28857737,48.7037833278,35.3023380648,26.5686611208,20.2084436814,15.249033223,10.8063704403,7.7723488404,4.95864687921,4.14520962577,3.10857277768,1.48034156501,1.48004605387,0.444294536715,0.740638399577,0.517983531463,0.517808269006])

    # Creating weights for histo: y8_M_16
    y8_M_16_weights = numpy.array([1.02110728423,3.45995273238,6.7875353267,10.6063377388,17.7901072339,19.8130497953,17.8277017815,12.4587274495,9.3399044253,6.73006320218,5.14196964296,3.87650260058,2.45774264999,1.83416739827,1.28541663948,0.850616550958,0.642643801639,0.453637273528,0.132301808903,0.189077948149])

    # Creating weights for histo: y8_M_17
    y8_M_17_weights = numpy.array([0.235964962811,0.579678918552,1.09528228028,1.87012754358,3.19908569912,4.27227412326,5.38970274449,5.453772453,5.47725190816,4.74604551597,4.14229848762,2.96213927034,2.1270571893,1.97546605909,1.05239844067,0.686671230462,0.558409298883,0.385908144934,0.171853341423,0.129089242159])

    # Creating weights for histo: y8_M_18
    y8_M_18_weights = numpy.array([0.00162106522106,0.0307919555687,0.0583229691766,0.0858284347251,0.144211187869,0.204142760673,0.187683341779,0.249376907148,0.289594198077,0.278534384136,0.310977873375,0.374113420494,0.416224027551,0.385504120778,0.362691602372,0.225201521739,0.178216163928,0.115029162365,0.0664230681137,0.0469646440171])

    # Creating weights for histo: y8_M_19
    y8_M_19_weights = numpy.array([0.0,0.0,0.00852161114693,0.00639111008164,0.019034569823,0.0191432720387,0.0190600944084,0.0212584383073,0.0298214801327,0.025571547565,0.0340316558201,0.0127111655974,0.0191208433672,0.025566346875,0.0127869041252,0.0339612404825,0.0404481824643,0.0276668019841,0.03193409617,0.0212907004033])

    # Creating a new Canvas
    fig   = plt.figure(figsize=(12,6),dpi=80)
    frame = gridspec.GridSpec(1,1,right=0.7)
    pad   = fig.add_subplot(frame[0])

    # Creating a new Stack
    pad.hist(x=xData, bins=xBinning, weights=y8_M_0_weights+y8_M_1_weights+y8_M_2_weights+y8_M_3_weights+y8_M_4_weights+y8_M_5_weights+y8_M_6_weights+y8_M_7_weights+y8_M_8_weights+y8_M_9_weights+y8_M_10_weights+y8_M_11_weights+y8_M_12_weights+y8_M_13_weights+y8_M_14_weights+y8_M_15_weights+y8_M_16_weights+y8_M_17_weights+y8_M_18_weights+y8_M_19_weights,\
             label="$bg\_vbf\_1600\_inf$", histtype="step", rwidth=1.0,\
             color=None, edgecolor="#ccc6aa", linewidth=1, linestyle="solid",\
             bottom=None, cumulative=False, normed=False, align="mid", orientation="vertical")

    pad.hist(x=xData, bins=xBinning, weights=y8_M_0_weights+y8_M_1_weights+y8_M_2_weights+y8_M_3_weights+y8_M_4_weights+y8_M_5_weights+y8_M_6_weights+y8_M_7_weights+y8_M_8_weights+y8_M_9_weights+y8_M_10_weights+y8_M_11_weights+y8_M_12_weights+y8_M_13_weights+y8_M_14_weights+y8_M_15_weights+y8_M_16_weights+y8_M_17_weights+y8_M_18_weights,\
             label="$bg\_vbf\_1200\_1600$", histtype="step", rwidth=1.0,\
             color=None, edgecolor="#c1bfa8", linewidth=1, linestyle="solid",\
             bottom=None, cumulative=False, normed=False, align="mid", orientation="vertical")

    pad.hist(x=xData, bins=xBinning, weights=y8_M_0_weights+y8_M_1_weights+y8_M_2_weights+y8_M_3_weights+y8_M_4_weights+y8_M_5_weights+y8_M_6_weights+y8_M_7_weights+y8_M_8_weights+y8_M_9_weights+y8_M_10_weights+y8_M_11_weights+y8_M_12_weights+y8_M_13_weights+y8_M_14_weights+y8_M_15_weights+y8_M_16_weights+y8_M_17_weights,\
             label="$bg\_vbf\_800\_1200$", histtype="step", rwidth=1.0,\
             color=None, edgecolor="#bab5a3", linewidth=1, linestyle="solid",\
             bottom=None, cumulative=False, normed=False, align="mid", orientation="vertical")

    pad.hist(x=xData, bins=xBinning, weights=y8_M_0_weights+y8_M_1_weights+y8_M_2_weights+y8_M_3_weights+y8_M_4_weights+y8_M_5_weights+y8_M_6_weights+y8_M_7_weights+y8_M_8_weights+y8_M_9_weights+y8_M_10_weights+y8_M_11_weights+y8_M_12_weights+y8_M_13_weights+y8_M_14_weights+y8_M_15_weights+y8_M_16_weights,\
             label="$bg\_vbf\_600\_800$", histtype="step", rwidth=1.0,\
             color=None, edgecolor="#b2a596", linewidth=1, linestyle="solid",\
             bottom=None, cumulative=False, normed=False, align="mid", orientation="vertical")

    pad.hist(x=xData, bins=xBinning, weights=y8_M_0_weights+y8_M_1_weights+y8_M_2_weights+y8_M_3_weights+y8_M_4_weights+y8_M_5_weights+y8_M_6_weights+y8_M_7_weights+y8_M_8_weights+y8_M_9_weights+y8_M_10_weights+y8_M_11_weights+y8_M_12_weights+y8_M_13_weights+y8_M_14_weights+y8_M_15_weights,\
             label="$bg\_vbf\_400\_600$", histtype="step", rwidth=1.0,\
             color=None, edgecolor="#b7a39b", linewidth=1, linestyle="solid",\
             bottom=None, cumulative=False, normed=False, align="mid", orientation="vertical")

    pad.hist(x=xData, bins=xBinning, weights=y8_M_0_weights+y8_M_1_weights+y8_M_2_weights+y8_M_3_weights+y8_M_4_weights+y8_M_5_weights+y8_M_6_weights+y8_M_7_weights+y8_M_8_weights+y8_M_9_weights+y8_M_10_weights+y8_M_11_weights+y8_M_12_weights+y8_M_13_weights+y8_M_14_weights,\
             label="$bg\_vbf\_200\_400$", histtype="step", rwidth=1.0,\
             color=None, edgecolor="#ad998c", linewidth=1, linestyle="solid",\
             bottom=None, cumulative=False, normed=False, align="mid", orientation="vertical")

    pad.hist(x=xData, bins=xBinning, weights=y8_M_0_weights+y8_M_1_weights+y8_M_2_weights+y8_M_3_weights+y8_M_4_weights+y8_M_5_weights+y8_M_6_weights+y8_M_7_weights+y8_M_8_weights+y8_M_9_weights+y8_M_10_weights+y8_M_11_weights+y8_M_12_weights+y8_M_13_weights,\
             label="$bg\_vbf\_100\_200$", histtype="step", rwidth=1.0,\
             color=None, edgecolor="#9b8e82", linewidth=1, linestyle="solid",\
             bottom=None, cumulative=False, normed=False, align="mid", orientation="vertical")

    pad.hist(x=xData, bins=xBinning, weights=y8_M_0_weights+y8_M_1_weights+y8_M_2_weights+y8_M_3_weights+y8_M_4_weights+y8_M_5_weights+y8_M_6_weights+y8_M_7_weights+y8_M_8_weights+y8_M_9_weights+y8_M_10_weights+y8_M_11_weights+y8_M_12_weights,\
             label="$bg\_vbf\_0\_100$", histtype="step", rwidth=1.0,\
             color=None, edgecolor="#876656", linewidth=1, linestyle="solid",\
             bottom=None, cumulative=False, normed=False, align="mid", orientation="vertical")

    pad.hist(x=xData, bins=xBinning, weights=y8_M_0_weights+y8_M_1_weights+y8_M_2_weights+y8_M_3_weights+y8_M_4_weights+y8_M_5_weights+y8_M_6_weights+y8_M_7_weights+y8_M_8_weights+y8_M_9_weights+y8_M_10_weights+y8_M_11_weights,\
             label="$bg\_dip\_1600\_inf$", histtype="step", rwidth=1.0,\
             color=None, edgecolor="#afcec6", linewidth=1, linestyle="solid",\
             bottom=None, cumulative=False, normed=False, align="mid", orientation="vertical")

    pad.hist(x=xData, bins=xBinning, weights=y8_M_0_weights+y8_M_1_weights+y8_M_2_weights+y8_M_3_weights+y8_M_4_weights+y8_M_5_weights+y8_M_6_weights+y8_M_7_weights+y8_M_8_weights+y8_M_9_weights+y8_M_10_weights,\
             label="$bg\_dip\_1200\_1600$", histtype="step", rwidth=1.0,\
             color=None, edgecolor="#84c1a3", linewidth=1, linestyle="solid",\
             bottom=None, cumulative=False, normed=False, align="mid", orientation="vertical")

    pad.hist(x=xData, bins=xBinning, weights=y8_M_0_weights+y8_M_1_weights+y8_M_2_weights+y8_M_3_weights+y8_M_4_weights+y8_M_5_weights+y8_M_6_weights+y8_M_7_weights+y8_M_8_weights+y8_M_9_weights,\
             label="$bg\_dip\_800\_1200$", histtype="step", rwidth=1.0,\
             color=None, edgecolor="#89a8a0", linewidth=1, linestyle="solid",\
             bottom=None, cumulative=False, normed=False, align="mid", orientation="vertical")

    pad.hist(x=xData, bins=xBinning, weights=y8_M_0_weights+y8_M_1_weights+y8_M_2_weights+y8_M_3_weights+y8_M_4_weights+y8_M_5_weights+y8_M_6_weights+y8_M_7_weights+y8_M_8_weights,\
             label="$bg\_dip\_600\_800$", histtype="step", rwidth=1.0,\
             color=None, edgecolor="#829e8c", linewidth=1, linestyle="solid",\
             bottom=None, cumulative=False, normed=False, align="mid", orientation="vertical")

    pad.hist(x=xData, bins=xBinning, weights=y8_M_0_weights+y8_M_1_weights+y8_M_2_weights+y8_M_3_weights+y8_M_4_weights+y8_M_5_weights+y8_M_6_weights+y8_M_7_weights,\
             label="$bg\_dip\_400\_600$", histtype="step", rwidth=1.0,\
             color=None, edgecolor="#adbcc6", linewidth=1, linestyle="solid",\
             bottom=None, cumulative=False, normed=False, align="mid", orientation="vertical")

    pad.hist(x=xData, bins=xBinning, weights=y8_M_0_weights+y8_M_1_weights+y8_M_2_weights+y8_M_3_weights+y8_M_4_weights+y8_M_5_weights+y8_M_6_weights,\
             label="$bg\_dip\_200\_400$", histtype="step", rwidth=1.0,\
             color=None, edgecolor="#7a8e99", linewidth=1, linestyle="solid",\
             bottom=None, cumulative=False, normed=False, align="mid", orientation="vertical")

    pad.hist(x=xData, bins=xBinning, weights=y8_M_0_weights+y8_M_1_weights+y8_M_2_weights+y8_M_3_weights+y8_M_4_weights+y8_M_5_weights,\
             label="$bg\_dip\_100\_200$", histtype="step", rwidth=1.0,\
             color=None, edgecolor="#758991", linewidth=1, linestyle="solid",\
             bottom=None, cumulative=False, normed=False, align="mid", orientation="vertical")

    pad.hist(x=xData, bins=xBinning, weights=y8_M_0_weights+y8_M_1_weights+y8_M_2_weights+y8_M_3_weights+y8_M_4_weights,\
             label="$bg\_dip\_0\_100$", histtype="step", rwidth=1.0,\
             color=None, edgecolor="#688296", linewidth=1, linestyle="solid",\
             bottom=None, cumulative=False, normed=False, align="mid", orientation="vertical")

    pad.hist(x=xData, bins=xBinning, weights=y8_M_0_weights+y8_M_1_weights+y8_M_2_weights+y8_M_3_weights,\
             label="$signal\_2pt4TeVL$", histtype="step", rwidth=1.0,\
             color=None, edgecolor="#6d7a84", linewidth=1, linestyle="solid",\
             bottom=None, cumulative=False, normed=False, align="mid", orientation="vertical")

    pad.hist(x=xData, bins=xBinning, weights=y8_M_0_weights+y8_M_1_weights+y8_M_2_weights,\
             label="$signal\_2pt2TeVL$", histtype="step", rwidth=1.0,\
             color=None, edgecolor="#7c99d1", linewidth=1, linestyle="solid",\
             bottom=None, cumulative=False, normed=False, align="mid", orientation="vertical")

    pad.hist(x=xData, bins=xBinning, weights=y8_M_0_weights+y8_M_1_weights,\
             label="$signal\_2TeVL$", histtype="step", rwidth=1.0,\
             color=None, edgecolor="#7f7f9b", linewidth=1, linestyle="solid",\
             bottom=None, cumulative=False, normed=False, align="mid", orientation="vertical")

    pad.hist(x=xData, bins=xBinning, weights=y8_M_0_weights,\
             label="$signal\_1pt8TeVL$", histtype="step", rwidth=1.0,\
             color=None, edgecolor="#aaa5bf", linewidth=1, linestyle="solid",\
             bottom=None, cumulative=False, normed=False, align="mid", orientation="vertical")


    # Axis
    plt.rc('text',usetex=False)
    plt.xlabel(r"M [ j_{1} , j_{2} ]   ( GeV ) ",\
               fontsize=16,color="black")
    plt.ylabel(r"$\mathrm{Events}$ $(\mathcal{L}_{\mathrm{int}} = 3000.0\ \mathrm{fb}^{-1})$ ",\
               fontsize=16,color="black")

    # Boundary of y-axis
    ymax=(y8_M_0_weights+y8_M_1_weights+y8_M_2_weights+y8_M_3_weights+y8_M_4_weights+y8_M_5_weights+y8_M_6_weights+y8_M_7_weights+y8_M_8_weights+y8_M_9_weights+y8_M_10_weights+y8_M_11_weights+y8_M_12_weights+y8_M_13_weights+y8_M_14_weights+y8_M_15_weights+y8_M_16_weights+y8_M_17_weights+y8_M_18_weights+y8_M_19_weights).max()*1.1
    ymin=0 # linear scale
    #ymin=min([x for x in (y8_M_0_weights+y8_M_1_weights+y8_M_2_weights+y8_M_3_weights+y8_M_4_weights+y8_M_5_weights+y8_M_6_weights+y8_M_7_weights+y8_M_8_weights+y8_M_9_weights+y8_M_10_weights+y8_M_11_weights+y8_M_12_weights+y8_M_13_weights+y8_M_14_weights+y8_M_15_weights+y8_M_16_weights+y8_M_17_weights+y8_M_18_weights+y8_M_19_weights) if x])/100. # log scale
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
    plt.savefig('../../HTML/MadAnalysis5job_0/selection_7.png')
    plt.savefig('../../PDF/MadAnalysis5job_0/selection_7.png')
    plt.savefig('../../DVI/MadAnalysis5job_0/selection_7.eps')

# Running!
if __name__ == '__main__':
    selection_7()
