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
    xBinning = numpy.linspace(300.0,2000.0,81,endpoint=True)

    # Creating data sequence: middle of each bin
    xData = numpy.array([310.625,331.875,353.125,374.375,395.625,416.875,438.125,459.375,480.625,501.875,523.125,544.375,565.625,586.875,608.125,629.375,650.625,671.875,693.125,714.375,735.625,756.875,778.125,799.375,820.625,841.875,863.125,884.375,905.625,926.875,948.125,969.375,990.625,1011.875,1033.125,1054.375,1075.625,1096.875,1118.125,1139.375,1160.625,1181.875,1203.125,1224.375,1245.625,1266.875,1288.125,1309.375,1330.625,1351.875,1373.125,1394.375,1415.625,1436.875,1458.125,1479.375,1500.625,1521.875,1543.125,1564.375,1585.625,1606.875,1628.125,1649.375,1670.625,1691.875,1713.125,1734.375,1755.625,1776.875,1798.125,1819.375,1840.625,1861.875,1883.125,1904.375,1925.625,1946.875,1968.125,1989.375])

    # Creating weights for histo: y11_PT_0
    y11_PT_0_weights = numpy.array([1.32677186546,1.48067744985,1.6045094373,1.6823466294,1.70534422707,1.66819463084,1.67173263048,1.68411582922,1.64165903353,1.59389543837,1.50721304716,1.48598464932,1.36745946133,1.33207906492,1.34800026331,1.3303098651,1.16932828143,1.15340708304,1.07910789057,1.05080349344,1.02426789614,0.965889902055,0.928740305822,0.891590709589,0.840288714791,0.764220722505,0.72176392681,0.682845130757,0.718225927169,0.656309933448,0.661616732909,0.583779540802,0.550167944211,0.486483150669,0.447564354615,0.474099951924,0.440488355333,0.399800599459,0.376803201791,0.373265162149,0.34496068502,0.329039406634,0.336115525917,0.28835177076,0.290120770581,0.28835177076,0.219359617756,0.233511856321,0.237049895962,0.238818935783,0.178671941882,0.185748061164,0.1715958226,0.182210021523,0.132677186546,0.159212623855,0.132677186546,0.130908146725,0.14329134547,0.0990656299544,0.120293987802,0.122063027622,0.118524947981,0.104372709416,0.0884514710307,0.0796063119276,0.0742992324658,0.0583779540802,0.0654540733627,0.0601469939009,0.0725301926452,0.0513018347978,0.045994755336,0.0424567156947,0.054839914439,0.0336115525917,0.0495328349772,0.0212283498474,0.045994755336,0.0353805844123])

    # Creating weights for histo: y11_PT_1
    y11_PT_1_weights = numpy.array([0.873037762675,0.95106331696,1.06114617936,1.09423346843,1.06744756851,1.08459753091,1.14761781734,1.01620711478,1.00014588663,1.03222557694,0.963811979257,0.931837405354,0.889052228014,0.943496933728,0.888019449277,0.806790442369,0.823897239089,0.737333674208,0.683890572021,0.678548020404,0.666816149557,0.619809529098,0.612314688975,0.544952255404,0.526791896474,0.477674954137,0.495847303532,0.470187308293,0.455226804846,0.453069720154,0.3729332045,0.366520383958,0.351529025047,0.336625995896,0.322687519736,0.295978398758,0.276766955647,0.302419276989,0.276764757395,0.262865889738,0.19662512422,0.236137424143,0.211571359014,0.198740002474,0.190185445036,0.18381351198,0.16669820203,0.151745212607,0.168857445005,0.127150410329,0.123955990523,0.125033813441,0.116484891522,0.122870733517,0.0951009359866,0.0961731633542,0.105796111211,0.0811993504907,0.0833514791237,0.0833518788059,0.0758703480994,0.0726626588454,0.0801479465644,0.0705257980714,0.0651864039436,0.0491530336373,0.0512910135214,0.041673381437,0.0438158377614,0.0448753552359,0.0341884294511,0.0438165971575,0.0416688650285,0.0374032250541,0.0267076501471,0.0277761444832,0.0235070992167,0.0192369588211,0.0277775753454,0.021370546198])

    # Creating weights for histo: y11_PT_2
    y11_PT_2_weights = numpy.array([0.67154494152,0.658350538739,0.71529615074,0.71529615074,0.750019358057,0.740991356155,0.752797358643,0.728490953521,0.697240146935,0.638905334641,0.682656543862,0.661128139325,0.629877332739,0.609738128495,0.574320521031,0.552097716348,0.56112571825,0.497929704933,0.464595297908,0.458345296591,0.441678093078,0.436122491907,0.409732886346,0.372231838443,0.377787519614,0.309035745126,0.343064432297,0.275701578101,0.286118500296,0.30625790454,0.250006452686,0.252089853125,0.234728289466,0.242367371076,0.213199964929,0.207644243758,0.201394082441,0.187504839514,0.170837756002,0.152781712197,0.161115273953,0.144448190441,0.147226031026,0.145142630587,0.13125338766,0.124308786197,0.121530905611,0.0916690193181,0.11041950327,0.0951413400499,0.0902800990254,0.0881967385864,0.073613015513,0.0666683740495,0.0687517744886,0.0756964159521,0.0611126928788,0.0618071330251,0.0493068103908,0.0500012905372,0.0465289698054,0.0527791311226,0.0527791311226,0.0368065077565,0.0430566490737,0.04375112922,0.0333341950248,0.0229172568295,0.0208338723905,0.0201394082441,0.0270840337076,0.0270840337076,0.0201394082441,0.0263895695613,0.013889246927,0.0180560238051,0.0194449480978,0.0145837110733,0.0194449480978,0.013889246927])

    # Creating weights for histo: y11_PT_3
    y11_PT_3_weights = numpy.array([0.453292942281,0.480793750913,0.522993764159,0.508768959694,0.49407015508,0.523941764456,0.514932961628,0.541485769963,0.48980255374,0.497863356271,0.468939747192,0.44143893856,0.454240942578,0.434326536328,0.3845402007,0.375531237873,0.353245910878,0.357039192068,0.324796581948,0.340443746859,0.313416858376,0.291131531381,0.281648448405,0.262208042303,0.26742376394,0.239448595159,0.23091379248,0.205309384443,0.199145342508,0.201516143252,0.191084699978,0.192507180425,0.165480291941,0.163109531197,0.147462406286,0.134660202267,0.1417725245,0.122806318547,0.111426554975,0.125177079291,0.110478274677,0.0929345091705,0.0919861888729,0.0891412679799,0.0872446273846,0.0763390639615,0.0772873842592,0.0692267017291,0.0725458227709,0.0649593003896,0.074916583515,0.0578469781572,0.0564244977107,0.0545278971154,0.0440964538411,0.0507346559247,0.0355616711622,0.0493121754782,0.0327167382692,0.038880760204,0.0412515329481,0.0308201136739,0.0289234930786,0.0327167382692,0.0284493369298,0.0270268684833,0.0213370026973,0.0256044040368,0.0232336232926,0.0246560917391,0.0189662259532,0.016595445209,0.016595445209,0.0170696013579,0.0113797355719,0.00663817808361,0.0113797355719,0.0128022000184,0.0156471369114,0.00711233423244])

    # Creating weights for histo: y11_PT_4
    y11_PT_4_weights = numpy.array([0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0])

    # Creating weights for histo: y11_PT_5
    y11_PT_5_weights = numpy.array([1.05211370067,2.10758668394,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0])

    # Creating weights for histo: y11_PT_6
    y11_PT_6_weights = numpy.array([2.76494538114,1.61312974571,1.84223992232,4.14706012429,2.99360673049,1.84271718555,1.38204326894,0.230186247644,0.690400846426,0.459655601338,0.230020166188,0.0,0.230128530303,0.0,0.461033208979,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.230673156052,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0])

    # Creating weights for histo: y11_PT_7
    y11_PT_7_weights = numpy.array([0.968948010971,0.747849601217,0.830593690179,0.858221086004,0.886272778927,0.747995777915,0.636779545687,0.692195516379,0.831061070936,0.719954855907,0.747564941333,0.55393890317,0.637028815424,0.609308712799,0.553485755408,0.276891901,0.0830829880949,0.166052650782,0.138335356288,0.0276831160736,0.193957859266,0.138310083106,0.055500522371,0.0276381513521,0.0,0.0276586853313,0.0,0.0,0.0276696178096,0.0,0.0277263959163,0.0277307081288,0.0,0.0,0.0276929406863,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0])

    # Creating weights for histo: y11_PT_8
    y11_PT_8_weights = numpy.array([0.0806631119786,0.121028623245,0.110839491251,0.100762451118,0.120909612882,0.0807183993017,0.110954071345,0.12098347092,0.0504072488348,0.161220868532,0.121043067134,0.171468625722,0.121026559832,0.161314875187,0.201597364436,0.16125018113,0.262124056535,0.262186929934,0.161244294335,0.141077712216,0.191605895243,0.141129236845,0.0807201592714,0.100769612374,0.0302487383011,0.0302908926091,0.0403368419672,0.0403172880973,0.0100921880095,0.0201783192958,0.0301960241751,0.0403817576069,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0100805661408,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0100975164694,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0])

    # Creating weights for histo: y11_PT_9
    y11_PT_9_weights = numpy.array([0.0452490317736,0.0368056173862,0.033950093685,0.022647850641,0.0311240721924,0.0226241234474,0.0254720984614,0.0141465514428,0.00847081204366,0.0141375561163,0.0198094788499,0.0254420114411,0.0311275541302,0.0283018250435,0.0226139046333,0.031126307558,0.0282985547152,0.0226378472839,0.0367781543234,0.0169813566524,0.0367509067175,0.0537560405803,0.0537536551644,0.0452811194653,0.039604522086,0.0509199734087,0.0763679753218,0.0849299641183,0.0735807322279,0.0650809566179,0.0509417499477,0.0395859774008,0.0311140765302,0.0339577347108,0.0311110716756,0.0537226832317,0.0198024534152,0.00848509375969,0.00848264678464,0.0254528958631,0.0141639842163,0.0084793726089,0.0141473940333,0.0141462667319,0.0113203529678,0.0,0.0,0.00283097815599,0.00282347948558,0.00283014095194,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0])

    # Creating weights for histo: y11_PT_10
    y11_PT_10_weights = numpy.array([0.00610087496977,0.00306963144219,0.0,0.0,0.00306733856798,0.0,0.0,0.0,0.0015172740515,0.00152449660526,0.0,0.00151265402815,0.0,0.00150849612533,0.0,0.00152305587656,0.00153219782606,0.00152094974159,0.00152767589991,0.00153629545228,0.0,0.0,0.0015216293306,0.00151265402815,0.0,0.0,0.0,0.0,0.0,0.00458659820126,0.0,0.00150849612533,0.00154541021822,0.0,0.00152260675687,0.00152094974159,0.0,0.0,0.0015216293306,0.00152094974159,0.0015216293306,0.0015216293306,0.003043316574,0.00609529170288,0.00305133926995,0.00302115015348,0.00303210631015,0.00608717327353,0.00610038566569,0.00303042447509,0.00151448714563,0.00456707685934,0.0015172740515,0.00150849612533,0.0,0.0015333359899,0.0,0.00306899321947,0.00152260675687,0.00150849612533,0.00153821484801,0.00153153123788,0.0,0.0,0.00151115656855,0.00153821484801,0.0,0.0,0.0,0.0,0.0,0.00152449660526,0.00151265402815,0.0,0.0,0.0,0.0,0.0,0.0,0.0])

    # Creating weights for histo: y11_PT_11
    y11_PT_11_weights = numpy.array([0.000180553039269,0.000180503376288,0.0,0.0,0.0,0.000180003628106,0.000180626147796,0.0,0.0,0.0,0.000180626147796,0.0,0.0,0.0,0.000180626147796,0.0,0.0,0.0,0.0,0.000180734328398,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.000180970246806,0.0,0.0,0.000179998700306,0.000180402048407,0.0,0.000361424114107,0.000180154580469,0.0,0.000180547149008,0.00018053382855,0.000361923477304,0.000360556667374,0.000903175974642,0.000722705707008,0.0,0.000360405676513,0.000721970001919,0.0,0.000180766975071,0.000180343723279,0.0,0.00036131408558,0.0,0.0001802030115,0.0,0.000540977310526,0.000361144153489,0.0,0.0,0.0])

    # Creating weights for histo: y11_PT_12
    y11_PT_12_weights = numpy.array([0.0,0.0242945760233,0.0,0.0121753353338,0.0,0.0,0.0,0.0,0.0121313846429,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0])

    # Creating weights for histo: y11_PT_13
    y11_PT_13_weights = numpy.array([0.301291549458,0.280990398441,0.170657455913,0.0501597443294,0.0702198736437,0.0803857996688,0.040161591392,0.0301453607939,0.010060984688,0.0501640003273,0.0100532495153,0.0200893014936,0.0,0.0201115111911,0.0200893014936,0.0,0.0,0.0,0.0100696702293,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0])

    # Creating weights for histo: y11_PT_14
    y11_PT_14_weights = numpy.array([1.22648283204,0.989819405521,0.753684926609,0.643578104822,0.467596587331,0.445592042045,0.374051553748,0.286087811144,0.225603424644,0.137448253383,0.137444109553,0.0385031766595,0.0550210321501,0.0439835369592,0.0440190845132,0.0274653442747,0.0440063280195,0.0110095202815,0.0275332746347,0.0110112915653,0.0109919577586,0.00550370793316,0.0,0.0,0.0,0.00547921059026,0.00550414669154,0.00549442900593,0.0,0.00548474382094,0.00549598091057,0.0,0.00548806294684,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.00551421782139,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0])

    # Creating weights for histo: y11_PT_15
    y11_PT_15_weights = numpy.array([0.473698016813,0.428271674243,0.426269533778,0.391742250677,0.386907091473,0.368104727815,0.320760138273,0.287175244051,0.242761595753,0.205273790235,0.187507609423,0.150960950213,0.126315102115,0.0927609113887,0.081914079928,0.0542746811077,0.0414431051564,0.029599420183,0.0286274020303,0.0256638693865,0.0157917336156,0.0118387427528,0.00789750820225,0.0098776712183,0.00690874742552,0.00789289065307,0.00296062663409,0.00197208150333,0.00296049115392,0.0,0.00197398544071,0.00296333784092,0.0,0.00098765929885,0.0,0.000984219385041,0.0019732952133,0.000984219385041,0.00295994362161,0.0,0.0,0.0,0.0,0.000985428685899,0.0,0.0,0.0,0.0,0.0,0.00197503200502,0.000983908742626,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.000986794310036,0.0,0.0,0.0,0.0,0.000986290468081,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0])

    # Creating weights for histo: y11_PT_16
    y11_PT_16_weights = numpy.array([0.0945173574931,0.0962982571368,0.0867184894672,0.0879802034497,0.0899898072579,0.0867147684232,0.088727853208,0.0816688727626,0.0867170890743,0.0788891728987,0.076625817899,0.0783982351628,0.0783989553648,0.0688265497608,0.062515819242,0.0577262354914,0.0509132040487,0.0519240476478,0.048396217891,0.0363007404218,0.0342863992846,0.0259660729599,0.0206746364111,0.0146209700135,0.00932674468221,0.0113401455556,0.00705923651724,0.00504343497028,0.00479178436798,0.00201697907732,0.00327795045149,0.00352882723669,0.000504413516673,0.00176474551146,0.00126015114405,0.000503972993081,0.000757812209415,0.0015134782167,0.000252017865341,0.000252130817031,0.000252086204514,0.000251770956069,0.000504129436972,0.0,0.000251614672223,0.0,0.0,0.000251614672223,0.000252082363437,0.0,0.0,0.0,0.0005041042299,0.0,0.0,0.000252186592679,0.0,0.0,0.0,0.0,0.0,0.0,0.000251958168593,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0])

    # Creating weights for histo: y11_PT_17
    y11_PT_17_weights = numpy.array([0.0206214725109,0.0197704487821,0.0191921461326,0.0180300824133,0.0168990297199,0.0188871543918,0.0197446662431,0.0186058957831,0.0208834367031,0.0208977825516,0.0211869188807,0.0160168150172,0.0240541391579,0.0168983299224,0.0197606916056,0.0197558829971,0.0174670853347,0.0186205415449,0.0234697482703,0.0157525015049,0.0194774635668,0.0174699245131,0.01718629659,0.0191806294653,0.0151745387571,0.017469634597,0.0160362793846,0.0105953738863,0.0151693202672,0.0105842671004,0.0146025242879,0.00887990831171,0.0065892751804,0.00972326325972,0.00572885916956,0.00916365320096,0.00371448209463,0.00487273491676,0.00342530777656,0.00400611969987,0.00228820383431,0.000857909536166,0.000570990765379,0.000570272873125,0.000572059156206,0.000284540459028,0.000286183783479,0.0,0.000287276367304,0.000575049090972,0.0,0.0,0.0,0.000857851153061,0.0,0.0,0.0,0.000286183783479,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0])

    # Creating weights for histo: y11_PT_18
    y11_PT_18_weights = numpy.array([0.00144703232661,0.00136101381819,0.00138208803424,0.00123120108973,0.00101491639154,0.000971718544365,0.00118786703652,0.000948921426809,0.000993445711168,0.000948902148417,0.00066922758298,0.00112332004666,0.000993883246846,0.000885535750516,0.000928899140405,0.000820984150606,0.000820783822969,0.000907008526365,0.000907032414807,0.000669450960869,0.000691527234205,0.000820856326486,0.000799445576767,0.000755810613009,0.000712685688447,0.00108016452813,0.000778060391873,0.000862475021905,0.00107988205778,0.000712852069351,0.000777814382828,0.000863572213863,0.000928533270053,0.000777813544637,0.000864475364616,0.00105788583168,0.000950542488113,0.00155403452646,0.000950571824796,0.00127462273389,0.0011231498939,0.00129421502833,0.00140066318396,0.00138235206439,0.00103665780759,0.00146859520799,0.000990798704137,0.00107994115024,0.00108010753115,0.000821083476234,0.000583160040387,0.000948934837864,0.000583212008227,0.000496693518901,0.000431951649645,0.000194514364551,0.000410334202037,0.0001712664679,0.000237744188712,0.000172657906793,8.64930083208e-05,6.48105590045e-05,8.63748653059e-05,8.64157271149e-05,0.0,0.0,0.0,4.32204364217e-05,2.15933957184e-05,0.0,0.0,0.0,0.0,2.16751863917e-05,0.0,2.16220828038e-05,0.0,0.0,0.0,0.0])

    # Creating weights for histo: y11_PT_19
    y11_PT_19_weights = numpy.array([0.000113736722393,5.67658916409e-05,5.67183467175e-05,2.84489103184e-05,0.0,8.5234773203e-05,8.48750383933e-05,2.82573348648e-05,0.0,5.68463111617e-05,8.5224082277e-05,5.68266814338e-05,8.519618193e-05,8.47704900466e-05,5.67183467175e-05,5.66547357081e-05,5.68570020877e-05,5.6794816535e-05,0.000113546052698,0.000113632174046,2.83974008433e-05,5.67791365103e-05,0.0,2.83498707683e-05,5.68174011161e-05,5.66824727215e-05,0.0,2.83498707683e-05,0.0,0.0,5.67183467175e-05,2.84080917692e-05,2.84489103184e-05,2.84080917692e-05,0.0,5.67183467175e-05,2.8429265742e-05,5.64159419982e-05,8.50369019819e-05,2.8429265742e-05,5.68266814338e-05,2.83974008433e-05,8.51858770653e-05,5.63701491987e-05,8.51951573829e-05,5.67765825669e-05,0.000113704857494,5.68266814338e-05,5.67369667468e-05,2.8429265742e-05,0.000198018221365,8.38794607626e-05,5.68266814338e-05,2.83974008433e-05,0.000140565942581,5.68463111617e-05,8.49680049035e-05,2.8429265742e-05,0.00014209297802,0.000255385433045,0.000141774744791,0.000113655783174,0.000142040265815,2.8429265742e-05,5.67183467175e-05,8.492045998e-05,0.000113286367137,0.000198849589343,0.000142124842919,8.52135992302e-05,0.000113439084045,0.0,0.000140466175454,0.000141984984819,0.0,5.67977565397e-05,5.56796935644e-05,5.68463111617e-05,5.66287953641e-05,8.46724750435e-05])

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
    plt.ylabel(r"$\mathrm{Events}$ $(\mathcal{L}_{\mathrm{int}} = 40.0\ \mathrm{fb}^{-1})$ ",\
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
