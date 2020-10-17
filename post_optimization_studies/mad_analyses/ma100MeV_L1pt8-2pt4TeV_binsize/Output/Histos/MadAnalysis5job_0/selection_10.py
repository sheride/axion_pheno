def selection_10():

    # Library import
    import numpy
    import matplotlib
    import matplotlib.pyplot   as plt
    import matplotlib.gridspec as gridspec

    # Library version
    matplotlib_version = matplotlib.__version__
    numpy_version      = numpy.__version__

    # Histo binning
    xBinning = numpy.linspace(300.0,2000.0,61,endpoint=True)

    # Creating data sequence: middle of each bin
    xData = numpy.array([314.166666667,342.5,370.833333333,399.166666667,427.5,455.833333333,484.166666667,512.5,540.833333333,569.166666667,597.5,625.833333333,654.166666667,682.5,710.833333333,739.166666667,767.5,795.833333333,824.166666667,852.5,880.833333333,909.166666667,937.5,965.833333333,994.166666667,1022.5,1050.83333333,1079.16666667,1107.5,1135.83333333,1164.16666667,1192.5,1220.83333333,1249.16666667,1277.5,1305.83333333,1334.16666667,1362.5,1390.83333333,1419.16666667,1447.5,1475.83333333,1504.16666667,1532.5,1560.83333333,1589.16666667,1617.5,1645.83333333,1674.16666667,1702.5,1730.83333333,1759.16666667,1787.5,1815.83333333,1844.16666667,1872.5,1900.83333333,1929.16666667,1957.5,1985.83333333])

    # Creating weights for histo: y11_PT_0
    y11_PT_0_weights = numpy.array([134.932698193,153.772876545,168.367365268,172.214984931,160.008675999,172.480334908,163.856325663,153.37483658,149.925226882,132.279168426,140.903177671,130.156308611,116.755939784,111.183470272,106.009070724,102.161421061,94.8641916994,88.7610522335,83.4539626978,75.2279634176,67.0019941374,70.0535638704,64.7464743347,61.6949046017,55.5917351358,45.9062959832,45.3755960297,41.6606363547,41.3952863779,36.2208868307,34.2307170048,32.7712771325,30.3830673415,28.9236274692,25.3413427827,23.08583198,25.3413427827,18.5748073747,19.1055163283,18.5748073747,14.0637827694,15.7885846185,14.3291357462,13.7984267926,9.81811114092,11.9409469552,11.6755939784,11.2775600132,8.35866226862,7.96063130345,6.23582645437,6.23582645437,6.63386041954,5.8377954892,4.90905557046,4.3783466169,3.98031565173,4.77637758207,2.65354386782,3.98031565173])

    # Creating weights for histo: y11_PT_1
    y11_PT_1_weights = numpy.array([87.9181645764,101.305578463,109.237300896,105.464860865,112.59936727,105.626012712,103.46140408,94.8052777169,96.3348713336,90.3178762465,91.123965218,83.1101081014,80.94705823,71.8885918212,66.4395550749,64.5968904226,62.5158553304,56.1792244282,51.5314504913,48.8089555091,47.4471984232,45.8421548068,39.6715618658,38.0675674151,34.6205485981,32.5378648169,30.853144562,27.7301890393,28.7728978428,27.4081761146,21.077624378,22.4392735497,19.713643061,18.9928182846,18.5945430062,14.3458117374,15.8703603661,11.9401797753,13.0642858491,11.701710414,11.2192410895,9.3762766756,9.53758140076,8.89476359068,8.09506253933,8.17536567962,6.41165823794,7.85348465003,6.01135057579,5.20935335043,4.32708296094,4.56832511722,4.00664977997,3.92724292692,3.6861416586,3.52665648647,2.80389375123,2.24387129955,2.40411277025,2.24392885378])

    # Creating weights for histo: y11_PT_2
    y11_PT_2_weights = numpy.array([66.616305625,68.9080361625,71.5122767734,74.1164873842,75.8353077873,72.9706371154,67.4496458205,67.5017558327,66.0433654906,62.9703747698,57.8660835726,56.6160432794,53.3347025098,49.8971217035,45.4178506529,43.9594603108,42.4490199565,38.0739089303,36.1988484905,32.4487576109,29.2715888657,29.6882679634,27.2923714015,25.1048158884,23.5943605341,22.6568363142,21.0942949477,19.8442636545,18.1775532636,15.4170666161,16.354590836,14.3232873596,14.1670323229,12.9170010297,12.2399008709,10.0002593456,11.0419525899,8.64605602795,9.1148181379,7.5522797714,6.56266953929,7.2397696981,6.51058352707,5.05221418501,5.10429719722,4.89595914836,5.31263824609,3.95843492846,4.11468996511,4.16677297733,2.44797987418,2.08338708866,2.23964122531,2.81257265969,2.1875564131,1.8750484398,1.82296392758,1.97921776423,1.45837114206,1.61462497871])

    # Creating weights for histo: y11_PT_3
    y11_PT_3_weights = numpy.array([45.7678649948,49.4662962065,52.2045471036,50.8887466725,51.4221768473,53.2713774531,49.7863363113,48.0793657521,44.4876445753,45.1277547851,40.9314734103,37.5886923151,35.7750417209,34.2458812199,33.1434708587,30.9386501363,28.022598181,27.1691159013,26.2445125984,22.9017165032,21.5859340721,19.9500965362,19.9856585478,18.8832481867,16.5361764177,15.3982040449,13.8690525439,13.6201214623,11.6997908332,12.2687770196,10.7751875302,9.24603302925,8.81929488944,8.39255374963,7.82356756321,7.04121230689,6.89896426029,6.82784023698,6.54334714378,5.68986786415,4.83638858453,4.90750960783,3.8406612583,4.16071636316,3.73397522335,3.91178528161,2.77381020877,3.34279609519,2.95161876703,2.09813858741,2.63156366217,2.34707026896,2.20482372236,1.70696035925,1.60027522429,1.45802837769,0.817918467972,1.13797357283,1.63583693594,0.74679504467])

    # Creating weights for histo: y11_PT_4
    y11_PT_4_weights = numpy.array([0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0])

    # Creating weights for histo: y11_PT_5
    y11_PT_5_weights = numpy.array([78.9085275503,158.069001296,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0])

    # Creating weights for histo: y11_PT_6
    y11_PT_6_weights = numpy.array([259.212170159,155.463724634,362.877152254,310.877071479,120.926695222,51.8377939724,51.7800670206,51.7257120376,0.0,17.2596409523,34.5774930364,0.0,0.0,0.0,0.0,0.0,0.0,17.3004878862,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0])

    # Creating weights for histo: y11_PT_7
    y11_PT_7_weights = numpy.array([93.4475525126,74.7610655594,87.2122898306,89.327504935,66.4673081737,66.4484975424,76.8702220248,74.7578919866,62.3108510613,60.2379021761,68.5199461932,26.9957948454,12.4575079453,8.30206637617,10.3769828765,20.7721041638,8.31052827521,2.07286117915,0.0,2.07440122747,0.0,2.07522116327,2.07947952092,2.07980293683,0.0,2.07697037888,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0])

    # Creating weights for histo: y11_PT_8
    y11_PT_8_weights = numpy.array([9.82746761182,12.0998585852,9.06969595934,10.580796858,11.351181121,10.5854349851,7.56067971449,12.090568676,18.1592370945,12.1008189824,18.9021976914,17.3861582571,26.4629502323,18.9014330149,16.6330930064,17.3903457712,10.5926994118,10.5838237024,2.26865543761,5.29708252089,3.02379669397,2.27028856814,0.753221827312,4.54011195807,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.756042482232,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.757313756912,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0])

    # Creating weights for histo: y11_PT_9
    y11_PT_9_weights = numpy.array([4.24235080438,3.82181446537,2.33477844099,2.9709365733,2.33327736026,1.6982991432,1.27071014861,1.48594700502,2.33283240322,2.75909200931,2.54663772145,3.18198817883,2.75832704103,3.18316549705,1.9106997592,3.60495129389,6.36546820453,4.24521041801,4.02996894468,5.94238966611,8.91432176585,7.85318291823,5.30511423573,4.03091253061,3.3944825763,2.97181956197,4.87661657077,1.48518405664,1.06038253608,2.1211655912,1.27390593277,1.06105978262,1.48531044521,0.849026501449,0.0,0.212323368918,0.42402154723,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0])

    # Creating weights for histo: y11_PT_10
    y11_PT_10_weights = numpy.array([0.457565627878,0.230222360753,0.0,0.230050395185,0.0,0.0,0.113795555142,0.11433724668,0.113449053387,0.113137210672,0.0,0.114229192027,0.114914838246,0.228646925684,0.115222160217,0.0,0.114122201078,0.113449053387,0.0,0.0,0.0,0.229511540193,0.11448332877,0.113137210672,0.11590576767,0.0,0.228266739952,0.0,0.0,0.228193521623,0.114122201078,0.342370946695,0.457146882857,0.22885044782,0.453994239877,0.456538000648,0.457528930071,0.340868375387,0.342530768303,0.113795555142,0.113137210672,0.115000200536,0.0,0.344369913456,0.113137210672,0.115366114898,0.114864844133,0.0,0.228702770172,0.0,0.0,0.0,0.0,0.11433724668,0.113449053387,0.0,0.0,0.0,0.0,0.0])

    # Creating weights for histo: y11_PT_11
    y11_PT_11_weights = numpy.array([0.0270792311667,0.0,0.0,0.0135002721079,0.0,0.0135469610847,0.0,0.0135469610847,0.0,0.0,0.0135469610847,0.0,0.0,0.0,0.0135550746298,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0135727685105,0.0,0.013499902523,0.0135301536306,0.027106808558,0.0135115935351,0.0135410361756,0.0135400371412,0.0406857329682,0.0541197425327,0.0813216585864,0.0135301536306,0.0541364316041,0.0135115935351,0.0135575231303,0.0135257792459,0.0270985564185,0.0135152258625,0.0,0.0405732982894,0.0270858115117,0.0,0.0])

    # Creating weights for histo: y11_PT_12
    y11_PT_12_weights = numpy.array([0.0,1.82209320175,0.913150150035,0.0,0.0,0.0,0.909853848219,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0])

    # Creating weights for histo: y11_PT_13
    y11_PT_13_weights = numpy.array([27.8644436016,24.8418381641,7.52615242158,6.77189252555,7.53565403975,2.26090198735,3.76431737128,1.50655067001,1.50669756391,0.0,2.26079662042,0.754264234666,0.0,0.75522524308,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0])

    # Creating weights for histo: y11_PT_14
    y11_PT_14_weights = numpy.array([113.019671335,88.6861943191,69.3115397716,47.8585722459,42.4970671163,27.6439483583,19.8071697294,14.4293238983,6.18843054969,5.36345516673,4.12616576746,3.29705569646,3.71370245145,0.825017125945,2.47830976795,0.824396770393,0.412778064194,0.0,0.410940763613,0.41281097107,0.412082144704,0.0,0.411355755884,0.412198537543,0.411604690307,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.413566305753,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0])

    # Creating weights for histo: y11_PT_15
    y11_PT_15_weights = numpy.array([46.037057,41.2227507673,41.7387979795,39.2320038003,34.6402778751,28.3487647024,23.9068145212,20.2800872628,14.8008930075,12.286033148,7.9938977915,6.36492499202,4.21784572174,2.59119011434,2.59100072266,1.70225835777,0.740221115312,0.962944819379,0.666358663966,0.591833642391,0.221883616724,0.222036843605,0.148048912761,0.222250345137,0.0,0.0740744497693,0.0738164562254,0.147997145704,0.0738164562254,0.22199577868,0.0,0.0,0.0739071537927,0.0,0.0,0.0,0.0739603337716,0.0741671013776,0.0737931580436,0.0,0.0,0.0,0.0,0.0,0.0740095756062,0.0,0.0,0.0,0.0739717874584,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0])

    # Creating weights for histo: y11_PT_16
    y11_PT_16_weights = numpy.array([9.60336299983,9.15125317095,8.65895606846,9.07462367433,8.69640657433,8.26156959094,8.50733253401,7.69408339591,7.84585697245,7.46816501977,6.67438834421,5.91751302046,5.12273706458,5.08545760669,3.85687095532,3.27115764709,2.43920306161,1.45574527543,1.05867868765,0.850573908701,0.54846445893,0.378266613889,0.245847146691,0.397051883659,0.132343185799,0.132355069132,0.0377979733411,0.113568959127,0.0756791900342,0.018909810707,0.0377892708999,0.0378097066326,0.0,0.0188710998476,0.0,0.0188710998476,0.0189061766876,0.0,0.0,0.0378078161023,0.0,0.0189139938805,0.0,0.0,0.0,0.0,0.0,0.0188968620746,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0])

    # Creating weights for histo: y11_PT_17
    y11_PT_17_weights = numpy.array([2.17024470288,1.91175025858,1.73906548183,1.8901475102,1.97432340054,1.69578500677,2.23217528079,1.99673141589,1.69496474415,2.19121013569,1.80345534805,2.04051274601,1.76113159612,1.97611838109,1.91099072839,1.976104885,1.54699356553,1.97547581704,1.67485631332,1.50342292443,1.26740772487,1.33065192263,1.37362273731,0.988426959118,0.708854014734,0.79388975624,0.837635096776,0.429083277588,0.34327353507,0.429041664631,0.171615286252,0.0858269875277,0.0641109994176,0.042904436385,0.0428043178583,0.0,0.0646744013747,0.0,0.0,0.0213682162518,0.0429706122343,0.0,0.0214637835956,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0])

    # Creating weights for histo: y11_PT_18
    y11_PT_18_weights = numpy.array([0.13930789865,0.155530319287,0.111761916665,0.103652105078,0.106894552402,0.0987100580025,0.101923776332,0.080987411804,0.0972059662849,0.0923760062914,0.0988088807134,0.0810128089893,0.082616760679,0.0874641655213,0.0777397467421,0.0680688883636,0.0842572051065,0.0777468818424,0.082615566257,0.0923671424223,0.082521238345,0.0907130250052,0.0793881749382,0.0874578476571,0.0874585391646,0.0810404064257,0.103654116737,0.114921760272,0.124774516561,0.115036581953,0.119867799233,0.135695211915,0.134465522954,0.123106631858,0.111780210183,0.108312614298,0.10370393671,0.0712908419186,0.0825016875415,0.0647965490561,0.0372539617444,0.0259273954815,0.0355221125958,0.0162079524133,0.0226701404676,0.00648697545566,0.00810260419286,0.00971748170144,0.0,0.0,0.00324153264748,0.00161950463684,0.0,0.0,0.0,0.00162563893718,0.00162165616819,0.0,0.0,0.0])

    # Creating weights for histo: y11_PT_19
    y11_PT_19_weights = numpy.array([0.00853025378717,0.00851131748545,0.00213366817576,0.00426200091153,0.00425824349668,0.00635729089216,0.0,0.00639566908728,0.00852161084212,0.00852190818348,0.00635183183835,0.00637674058103,0.00426427496046,0.00638585014043,0.0149121260124,0.00426200091153,0.00212624020984,0.00212624020984,0.00851249014633,0.0,0.00212624020984,0.0,0.00425387580818,0.00213060678471,0.00213366817576,0.00213060678471,0.00425387580818,0.00213219483259,0.00636180223998,0.00637935540321,0.00426200091153,0.008518746565,0.00422776099547,0.00638963650986,0.0106539114703,0.00639419574412,0.00425527231031,0.00852933726304,0.0147451916659,0.00639180587682,0.00639110985303,0.00841480961042,0.00850479490728,0.00852933726304,0.0212815455368,0.0149004439491,0.0127792641106,0.00426280273093,0.00636606413286,0.01275332748,0.0149137185149,0.0127899661725,0.0106346756,0.00213366817576,0.0126671541663,0.00851667853911,0.00425983154457,0.00417597682528,0.00851063371167,0.00635043533621])

    # Creating a new Canvas
    fig   = plt.figure(figsize=(12,6),dpi=80)
    frame = gridspec.GridSpec(1,1,right=0.7)
    pad   = fig.add_subplot(frame[0])

    # Creating a new Stack
    pad.hist(x=xData, bins=xBinning, weights=y11_PT_0_weights+y11_PT_1_weights+y11_PT_2_weights+y11_PT_3_weights+y11_PT_4_weights+y11_PT_5_weights+y11_PT_6_weights+y11_PT_7_weights+y11_PT_8_weights+y11_PT_9_weights+y11_PT_10_weights+y11_PT_11_weights+y11_PT_12_weights+y11_PT_13_weights+y11_PT_14_weights+y11_PT_15_weights+y11_PT_16_weights+y11_PT_17_weights+y11_PT_18_weights+y11_PT_19_weights,\
             label="$bg\_vbf\_1600\_inf$", histtype="step", rwidth=1.0,\
             color=None, edgecolor="#ccc6aa", linewidth=1, linestyle="solid",\
             bottom=None, cumulative=False, normed=False, align="mid", orientation="vertical")

    pad.hist(x=xData, bins=xBinning, weights=y11_PT_0_weights+y11_PT_1_weights+y11_PT_2_weights+y11_PT_3_weights+y11_PT_4_weights+y11_PT_5_weights+y11_PT_6_weights+y11_PT_7_weights+y11_PT_8_weights+y11_PT_9_weights+y11_PT_10_weights+y11_PT_11_weights+y11_PT_12_weights+y11_PT_13_weights+y11_PT_14_weights+y11_PT_15_weights+y11_PT_16_weights+y11_PT_17_weights+y11_PT_18_weights,\
             label="$bg\_vbf\_1200\_1600$", histtype="step", rwidth=1.0,\
             color=None, edgecolor="#c1bfa8", linewidth=1, linestyle="solid",\
             bottom=None, cumulative=False, normed=False, align="mid", orientation="vertical")

    pad.hist(x=xData, bins=xBinning, weights=y11_PT_0_weights+y11_PT_1_weights+y11_PT_2_weights+y11_PT_3_weights+y11_PT_4_weights+y11_PT_5_weights+y11_PT_6_weights+y11_PT_7_weights+y11_PT_8_weights+y11_PT_9_weights+y11_PT_10_weights+y11_PT_11_weights+y11_PT_12_weights+y11_PT_13_weights+y11_PT_14_weights+y11_PT_15_weights+y11_PT_16_weights+y11_PT_17_weights,\
             label="$bg\_vbf\_800\_1200$", histtype="step", rwidth=1.0,\
             color=None, edgecolor="#bab5a3", linewidth=1, linestyle="solid",\
             bottom=None, cumulative=False, normed=False, align="mid", orientation="vertical")

    pad.hist(x=xData, bins=xBinning, weights=y11_PT_0_weights+y11_PT_1_weights+y11_PT_2_weights+y11_PT_3_weights+y11_PT_4_weights+y11_PT_5_weights+y11_PT_6_weights+y11_PT_7_weights+y11_PT_8_weights+y11_PT_9_weights+y11_PT_10_weights+y11_PT_11_weights+y11_PT_12_weights+y11_PT_13_weights+y11_PT_14_weights+y11_PT_15_weights+y11_PT_16_weights,\
             label="$bg\_vbf\_600\_800$", histtype="step", rwidth=1.0,\
             color=None, edgecolor="#b2a596", linewidth=1, linestyle="solid",\
             bottom=None, cumulative=False, normed=False, align="mid", orientation="vertical")

    pad.hist(x=xData, bins=xBinning, weights=y11_PT_0_weights+y11_PT_1_weights+y11_PT_2_weights+y11_PT_3_weights+y11_PT_4_weights+y11_PT_5_weights+y11_PT_6_weights+y11_PT_7_weights+y11_PT_8_weights+y11_PT_9_weights+y11_PT_10_weights+y11_PT_11_weights+y11_PT_12_weights+y11_PT_13_weights+y11_PT_14_weights+y11_PT_15_weights,\
             label="$bg\_vbf\_400\_600$", histtype="step", rwidth=1.0,\
             color=None, edgecolor="#b7a39b", linewidth=1, linestyle="solid",\
             bottom=None, cumulative=False, normed=False, align="mid", orientation="vertical")

    pad.hist(x=xData, bins=xBinning, weights=y11_PT_0_weights+y11_PT_1_weights+y11_PT_2_weights+y11_PT_3_weights+y11_PT_4_weights+y11_PT_5_weights+y11_PT_6_weights+y11_PT_7_weights+y11_PT_8_weights+y11_PT_9_weights+y11_PT_10_weights+y11_PT_11_weights+y11_PT_12_weights+y11_PT_13_weights+y11_PT_14_weights,\
             label="$bg\_vbf\_200\_400$", histtype="step", rwidth=1.0,\
             color=None, edgecolor="#ad998c", linewidth=1, linestyle="solid",\
             bottom=None, cumulative=False, normed=False, align="mid", orientation="vertical")

    pad.hist(x=xData, bins=xBinning, weights=y11_PT_0_weights+y11_PT_1_weights+y11_PT_2_weights+y11_PT_3_weights+y11_PT_4_weights+y11_PT_5_weights+y11_PT_6_weights+y11_PT_7_weights+y11_PT_8_weights+y11_PT_9_weights+y11_PT_10_weights+y11_PT_11_weights+y11_PT_12_weights+y11_PT_13_weights,\
             label="$bg\_vbf\_100\_200$", histtype="step", rwidth=1.0,\
             color=None, edgecolor="#9b8e82", linewidth=1, linestyle="solid",\
             bottom=None, cumulative=False, normed=False, align="mid", orientation="vertical")

    pad.hist(x=xData, bins=xBinning, weights=y11_PT_0_weights+y11_PT_1_weights+y11_PT_2_weights+y11_PT_3_weights+y11_PT_4_weights+y11_PT_5_weights+y11_PT_6_weights+y11_PT_7_weights+y11_PT_8_weights+y11_PT_9_weights+y11_PT_10_weights+y11_PT_11_weights+y11_PT_12_weights,\
             label="$bg\_vbf\_0\_100$", histtype="step", rwidth=1.0,\
             color=None, edgecolor="#876656", linewidth=1, linestyle="solid",\
             bottom=None, cumulative=False, normed=False, align="mid", orientation="vertical")

    pad.hist(x=xData, bins=xBinning, weights=y11_PT_0_weights+y11_PT_1_weights+y11_PT_2_weights+y11_PT_3_weights+y11_PT_4_weights+y11_PT_5_weights+y11_PT_6_weights+y11_PT_7_weights+y11_PT_8_weights+y11_PT_9_weights+y11_PT_10_weights+y11_PT_11_weights,\
             label="$bg\_dip\_1600\_inf$", histtype="step", rwidth=1.0,\
             color=None, edgecolor="#afcec6", linewidth=1, linestyle="solid",\
             bottom=None, cumulative=False, normed=False, align="mid", orientation="vertical")

    pad.hist(x=xData, bins=xBinning, weights=y11_PT_0_weights+y11_PT_1_weights+y11_PT_2_weights+y11_PT_3_weights+y11_PT_4_weights+y11_PT_5_weights+y11_PT_6_weights+y11_PT_7_weights+y11_PT_8_weights+y11_PT_9_weights+y11_PT_10_weights,\
             label="$bg\_dip\_1200\_1600$", histtype="step", rwidth=1.0,\
             color=None, edgecolor="#84c1a3", linewidth=1, linestyle="solid",\
             bottom=None, cumulative=False, normed=False, align="mid", orientation="vertical")

    pad.hist(x=xData, bins=xBinning, weights=y11_PT_0_weights+y11_PT_1_weights+y11_PT_2_weights+y11_PT_3_weights+y11_PT_4_weights+y11_PT_5_weights+y11_PT_6_weights+y11_PT_7_weights+y11_PT_8_weights+y11_PT_9_weights,\
             label="$bg\_dip\_800\_1200$", histtype="step", rwidth=1.0,\
             color=None, edgecolor="#89a8a0", linewidth=1, linestyle="solid",\
             bottom=None, cumulative=False, normed=False, align="mid", orientation="vertical")

    pad.hist(x=xData, bins=xBinning, weights=y11_PT_0_weights+y11_PT_1_weights+y11_PT_2_weights+y11_PT_3_weights+y11_PT_4_weights+y11_PT_5_weights+y11_PT_6_weights+y11_PT_7_weights+y11_PT_8_weights,\
             label="$bg\_dip\_600\_800$", histtype="step", rwidth=1.0,\
             color=None, edgecolor="#829e8c", linewidth=1, linestyle="solid",\
             bottom=None, cumulative=False, normed=False, align="mid", orientation="vertical")

    pad.hist(x=xData, bins=xBinning, weights=y11_PT_0_weights+y11_PT_1_weights+y11_PT_2_weights+y11_PT_3_weights+y11_PT_4_weights+y11_PT_5_weights+y11_PT_6_weights+y11_PT_7_weights,\
             label="$bg\_dip\_400\_600$", histtype="step", rwidth=1.0,\
             color=None, edgecolor="#adbcc6", linewidth=1, linestyle="solid",\
             bottom=None, cumulative=False, normed=False, align="mid", orientation="vertical")

    pad.hist(x=xData, bins=xBinning, weights=y11_PT_0_weights+y11_PT_1_weights+y11_PT_2_weights+y11_PT_3_weights+y11_PT_4_weights+y11_PT_5_weights+y11_PT_6_weights,\
             label="$bg\_dip\_200\_400$", histtype="step", rwidth=1.0,\
             color=None, edgecolor="#7a8e99", linewidth=1, linestyle="solid",\
             bottom=None, cumulative=False, normed=False, align="mid", orientation="vertical")

    pad.hist(x=xData, bins=xBinning, weights=y11_PT_0_weights+y11_PT_1_weights+y11_PT_2_weights+y11_PT_3_weights+y11_PT_4_weights+y11_PT_5_weights,\
             label="$bg\_dip\_100\_200$", histtype="step", rwidth=1.0,\
             color=None, edgecolor="#758991", linewidth=1, linestyle="solid",\
             bottom=None, cumulative=False, normed=False, align="mid", orientation="vertical")

    pad.hist(x=xData, bins=xBinning, weights=y11_PT_0_weights+y11_PT_1_weights+y11_PT_2_weights+y11_PT_3_weights+y11_PT_4_weights,\
             label="$bg\_dip\_0\_100$", histtype="step", rwidth=1.0,\
             color=None, edgecolor="#688296", linewidth=1, linestyle="solid",\
             bottom=None, cumulative=False, normed=False, align="mid", orientation="vertical")

    pad.hist(x=xData, bins=xBinning, weights=y11_PT_0_weights+y11_PT_1_weights+y11_PT_2_weights+y11_PT_3_weights,\
             label="$signal\_2pt4TeVL$", histtype="step", rwidth=1.0,\
             color=None, edgecolor="#6d7a84", linewidth=1, linestyle="solid",\
             bottom=None, cumulative=False, normed=False, align="mid", orientation="vertical")

    pad.hist(x=xData, bins=xBinning, weights=y11_PT_0_weights+y11_PT_1_weights+y11_PT_2_weights,\
             label="$signal\_2pt2TeVL$", histtype="step", rwidth=1.0,\
             color=None, edgecolor="#7c99d1", linewidth=1, linestyle="solid",\
             bottom=None, cumulative=False, normed=False, align="mid", orientation="vertical")

    pad.hist(x=xData, bins=xBinning, weights=y11_PT_0_weights+y11_PT_1_weights,\
             label="$signal\_2TeVL$", histtype="step", rwidth=1.0,\
             color=None, edgecolor="#7f7f9b", linewidth=1, linestyle="solid",\
             bottom=None, cumulative=False, normed=False, align="mid", orientation="vertical")

    pad.hist(x=xData, bins=xBinning, weights=y11_PT_0_weights,\
             label="$signal\_1pt8TeVL$", histtype="step", rwidth=1.0,\
             color=None, edgecolor="#aaa5bf", linewidth=1, linestyle="solid",\
             bottom=None, cumulative=False, normed=False, align="mid", orientation="vertical")


    # Axis
    plt.rc('text',usetex=False)
    plt.xlabel(r"p_{T} [ a_{1} ] ",\
               fontsize=16,color="black")
    plt.ylabel(r"$\mathrm{Events}$ $(\mathcal{L}_{\mathrm{int}} = 3000.0\ \mathrm{fb}^{-1})$ ",\
               fontsize=16,color="black")

    # Boundary of y-axis
    ymax=(y11_PT_0_weights+y11_PT_1_weights+y11_PT_2_weights+y11_PT_3_weights+y11_PT_4_weights+y11_PT_5_weights+y11_PT_6_weights+y11_PT_7_weights+y11_PT_8_weights+y11_PT_9_weights+y11_PT_10_weights+y11_PT_11_weights+y11_PT_12_weights+y11_PT_13_weights+y11_PT_14_weights+y11_PT_15_weights+y11_PT_16_weights+y11_PT_17_weights+y11_PT_18_weights+y11_PT_19_weights).max()*1.1
    ymin=0 # linear scale
    #ymin=min([x for x in (y11_PT_0_weights+y11_PT_1_weights+y11_PT_2_weights+y11_PT_3_weights+y11_PT_4_weights+y11_PT_5_weights+y11_PT_6_weights+y11_PT_7_weights+y11_PT_8_weights+y11_PT_9_weights+y11_PT_10_weights+y11_PT_11_weights+y11_PT_12_weights+y11_PT_13_weights+y11_PT_14_weights+y11_PT_15_weights+y11_PT_16_weights+y11_PT_17_weights+y11_PT_18_weights+y11_PT_19_weights) if x])/100. # log scale
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
    plt.savefig('../../HTML/MadAnalysis5job_0/selection_10.png')
    plt.savefig('../../PDF/MadAnalysis5job_0/selection_10.png')
    plt.savefig('../../DVI/MadAnalysis5job_0/selection_10.eps')

# Running!
if __name__ == '__main__':
    selection_10()
