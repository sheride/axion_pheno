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
    y11_PT_0_weights = numpy.array([1.1177222623,1.24383208253,1.42765590643,1.48855734772,1.5205440336,1.58900180035,1.6808227854,1.54408790666,1.55475892822,1.61248772001,1.55575612657,1.52918548673,1.47785435187,1.49163966984,1.47254062357,1.38920681568,1.38381195261,1.30578867558,1.25770493014,1.23740884617,1.23316545744,1.15407703667,1.12205158196,1.02367067044,1.00977464147,0.900828223568,0.92116187733,0.851671740499,0.873039363053,0.833477167129,0.731995947952,0.741588636383,0.693490502506,0.682804293157,0.613347729336,0.586663980421,0.567412256895,0.550341180345,0.504375332322,0.500065197242,0.398587535205,0.468000574015,0.414627480682,0.395352695695,0.402836559411,0.360127453291,0.347268990219,0.271427918908,0.305639975812,0.26177232105,0.253274952091,0.244725345126,0.229745507428,0.223303126462,0.189149422648,0.186997432635,0.192361440505,0.163486892774,0.166695873072,0.161352888302,0.146396631647,0.130357405592,0.128224280412,0.12608915684,0.1175415083,0.101512114341,0.113274018938,0.0769310350877,0.0876321124842,0.0961667314981,0.083338803878,0.0694604407037,0.0822778567741,0.0598476884019,0.0630381236089,0.0523500757379,0.0459381902571,0.0395457891128,0.0363265290782,0.0384679875582])

    # Creating weights for histo: y11_PT_1
    y11_PT_1_weights = numpy.array([0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0])

    # Creating weights for histo: y11_PT_2
    y11_PT_2_weights = numpy.array([1.05211370067,2.10758668394,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0])

    # Creating weights for histo: y11_PT_3
    y11_PT_3_weights = numpy.array([4.14658920504,2.30377423799,2.07275318806,4.60760611414,3.45472954005,1.84264282107,2.30353215771,1.15069093503,0.69037298469,1.15184523526,0.690701137953,0.0,0.230119243263,0.0,0.461014603577,0.229943177894,0.23058895585,0.0,0.0,0.0,0.0,0.0,0.0,0.230663847033,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0])

    # Creating weights for histo: y11_PT_4
    y11_PT_4_weights = numpy.array([3.87624962967,3.18473058273,3.10139209666,3.10051690656,2.38106833168,2.40950720103,2.21517229838,2.07713847071,2.16014111461,1.63424650352,1.57847515899,1.24641880421,1.08018577464,1.16324073759,0.885839331023,0.664484328729,0.304698989566,0.332245203486,0.332162108514,0.2767219513,0.221697538232,0.221289641943,0.138475077356,0.0553246321222,0.0277261530037,0.0276603694845,0.0,0.0,0.0276713026284,0.0,0.0277280841924,0.0277323966675,0.0,0.0,0.0276946269253,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0])

    # Creating weights for histo: y11_PT_5
    y11_PT_5_weights = numpy.array([1.17965986164,1.06883508715,0.988204412474,1.08872013142,0.967719806929,1.00813557685,0.837123467875,0.947858429546,0.655418778333,0.776211562386,0.685757913724,0.695685264776,0.715744473104,0.846678217084,0.856692953585,0.685658998251,0.766007490747,0.755932069907,0.54438773777,0.503979978184,0.383287141238,0.443623213031,0.302565986214,0.292331086931,0.16133999625,0.121056578876,0.0908371130018,0.1209735627,0.0705536760405,0.0604795417084,0.0603866886009,0.0605661564657,0.0100705296824,0.0,0.0,0.0100705296824,0.0100726597027,0.0201668562773,0.0100941965746,0.0,0.0,0.0,0.0100798568653,0.0,0.0,0.0,0.0,0.0,0.0,0.0100700260023,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0100968060012,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0])

    # Creating weights for histo: y11_PT_6
    y11_PT_6_weights = numpy.array([0.5969439391,0.523420122127,0.512106220413,0.469607718219,0.444115465419,0.41308399467,0.387600975823,0.398922187751,0.325378671676,0.345202469653,0.319714833829,0.350789473311,0.311180890812,0.322509220579,0.265968645064,0.25177678932,0.274404169525,0.220698417782,0.263141208455,0.243343419448,0.263072300076,0.302754023183,0.265894773435,0.291492408732,0.246182475449,0.280012872974,0.285712607816,0.268799929153,0.265983380915,0.232045061557,0.175420495539,0.181025813205,0.166891400347,0.121627059711,0.141409458795,0.158422133481,0.0905142532206,0.0508895497778,0.0650870613184,0.07640142473,0.065078173638,0.0396142382953,0.0311307626826,0.0396121606557,0.0396001180412,0.0113231510574,0.00565683927999,0.00849025872114,0.00564710900133,0.00848701529492,0.00282516197809,0.0,0.0,0.00283357680311,0.00283625426492,0.0,0.0,0.00282750317009,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0])

    # Creating weights for histo: y11_PT_7
    y11_PT_7_weights = numpy.array([0.103716400235,0.0792233660025,0.0883604666083,0.0943283021961,0.0823084886271,0.0685385818084,0.0486893663868,0.041181823073,0.0730948551914,0.059392323731,0.050274010712,0.0563691646945,0.0441418841765,0.0410964045417,0.0320134334548,0.0319931688564,0.0213284365709,0.0259649884852,0.0334253265101,0.0289872376825,0.021316667743,0.0167527493483,0.0182673124298,0.0319804665572,0.0182639802918,0.0228729061822,0.0152494470027,0.0212952097193,0.0228909966195,0.0198190371217,0.0152186542661,0.0182409507279,0.0214135124357,0.0182375831415,0.018268872154,0.0213070967082,0.0121814458958,0.00912279840768,0.018243916567,0.021287493811,0.0198268948231,0.0335343772262,0.0350341465601,0.0395942010927,0.0274603976811,0.0304143498648,0.0334948169491,0.0273727931726,0.0259052817707,0.0228257599738,0.0151954356447,0.0259390167142,0.0182202607502,0.0091605201008,0.0137473617146,0.00919928988132,0.0045667826155,0.00764116323059,0.00761210982279,0.00607776542108,0.00610909697148,0.00456613982008,0.0015107925665,0.0,0.0015107925665,0.00153784432826,0.00152607668191,0.0,0.0,0.0,0.00152268900825,0.0015241293899,0.00151228966539,0.0,0.0,0.0,0.0,0.0,0.0,0.0])

    # Creating weights for histo: y11_PT_8
    y11_PT_8_weights = numpy.array([0.0310626664269,0.0296056845074,0.0240158385327,0.0245510958366,0.0205867710895,0.0214809937811,0.018963656906,0.0173379046021,0.0158939746391,0.0137240570422,0.0128229636837,0.0139007494905,0.0106497070352,0.0104741853732,0.00993035514079,0.00884684249451,0.0108360469165,0.00722249205315,0.0101120619435,0.00631703135367,0.00686254844265,0.00686172041945,0.00794383890574,0.00487431839214,0.00613913345769,0.00523414646452,0.0043333958691,0.00451377013214,0.00433416612324,0.005055543786,0.00325035692912,0.00252656336426,0.00234619295249,0.00325053755371,0.00288864288948,0.00270967549563,0.00198608373735,0.00216624348461,0.0036103201811,0.00252623523599,0.001444869288,0.00180619242366,0.00144500254196,0.00270692761399,0.00144445566152,0.00144329026701,0.00126374056103,0.00162580968783,0.0018050747849,0.0021664980536,0.00198500268567,0.0023475717074,0.00252505982818,0.00216759874677,0.00108376182349,0.00216674877133,0.00216478269763,0.00234702367158,0.00289093439555,0.00198672458879,0.00415266343789,0.00307009512319,0.00451533759931,0.00361209869791,0.002527493061,0.00162418406647,0.00396990908957,0.00306972386069,0.00234881297194,0.00198569090774,0.000541380824247,0.0018073112178,0.00126587840139,0.000903551239462,0.00126409526306,0.00162442207499,0.00180485834349,0.000721760479063,0.00144583172054,0.000722306974375])

    # Creating weights for histo: y11_PT_9
    y11_PT_9_weights = numpy.array([0.0,0.0242945760233,0.0,0.0121753353338,0.0,0.0,0.0,0.0,0.0121313846429,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0])

    # Creating weights for histo: y11_PT_10
    y11_PT_10_weights = numpy.array([0.301291549458,0.280990398441,0.170657455913,0.0501597443294,0.0702198736437,0.0803857996688,0.040161591392,0.0301453607939,0.010060984688,0.0501640003273,0.0100532495153,0.0200893014936,0.0,0.0201115111911,0.0200893014936,0.0,0.0,0.0,0.0100696702293,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0])

    # Creating weights for histo: y11_PT_11
    y11_PT_11_weights = numpy.array([1.30353037791,1.10529233995,0.847173373342,0.704093815091,0.555651937211,0.48956040321,0.401552667898,0.324602914011,0.247648650559,0.142947521439,0.153932496664,0.0549893507147,0.0550222989776,0.0549914226769,0.0440200980272,0.0329541700174,0.0440073412398,0.0110097737694,0.0275339085725,0.011011545094,0.010992210842,0.010978844654,0.00549610745236,0.005484870104,0.0,0.00547933674592,0.00550427342134,0.00549455551198,0.0,0.005484870104,0.00549610745236,0.0,0.00548818930632,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.00551434478308,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0])

    # Creating weights for histo: y11_PT_12
    y11_PT_12_weights = numpy.array([0.763834378165,0.686836191003,0.689736178948,0.624621328702,0.587248961605,0.56942175168,0.500385604674,0.457912705913,0.398679239648,0.336492876192,0.302968574646,0.236832776329,0.200343432514,0.161849028616,0.140138640639,0.0897974152243,0.0838806381628,0.0513034121546,0.0463871409545,0.0355292614209,0.0217114982695,0.0167717465865,0.013819438611,0.0138243327164,0.00986624398774,0.0138108328416,0.0059239679093,0.00197207517423,0.00296048165267,0.000988169589309,0.00394619577188,0.00395176366857,0.000984216226338,0.000987656129108,0.000987941518385,0.000984216226338,0.00197328888031,0.00196894992115,0.00295993412212,0.0,0.000988169589309,0.0,0.0,0.000985425523315,0.000987941518385,0.0,0.0,0.0,0.0,0.00197502566646,0.000983905584921,0.0,0.0,0.0,0.000988891479881,0.0,0.0,0.0,0.0,0.00098679114307,0.0,0.0,0.0,0.0,0.000986287302732,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0])

    # Creating weights for histo: y11_PT_13
    y11_PT_13_weights = numpy.array([0.227359329155,0.231416832239,0.223086569673,0.208718285119,0.217036984655,0.210233842202,0.195603649026,0.177964387461,0.192584538005,0.17669921598,0.160065257809,0.154769150206,0.158567505392,0.151753160003,0.136376211174,0.124274880571,0.108395039982,0.106621415285,0.0990640752282,0.0784025818251,0.0695779097217,0.0536913873822,0.0471401909396,0.0327724225204,0.0254661322399,0.021427101996,0.0148752733878,0.0100817974758,0.00832282061601,0.00554542492599,0.00705820528117,0.00705732505055,0.00176338281414,0.00428473862057,0.00201618745008,0.00125919711524,0.00151505014988,0.00176499603681,0.000252013188576,0.000756765876025,0.000756271746561,0.000251766283886,0.00100761920071,0.0,0.000503623151505,0.0,0.000252013188576,0.00050473624314,0.000505203965686,0.0,0.0,0.0,0.000504094875099,0.0,0.0,0.000252181912783,0.0,0.0,0.0,0.0,0.0,0.0,0.000251953492936,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0])

    # Creating weights for histo: y11_PT_14
    y11_PT_14_weights = numpy.array([0.0922301146966,0.0916611890255,0.0835950817344,0.0827270714231,0.0818771271638,0.0778485575383,0.0832983665764,0.0844559736013,0.0787072698815,0.071871583703,0.0721334564752,0.0707133368179,0.0678462133784,0.074434883538,0.0612781687114,0.0590076348975,0.063857555031,0.0558328586902,0.0638187935016,0.0546944474703,0.057563460497,0.0578564764634,0.0532681291676,0.0489505127084,0.0460737313794,0.0449779808368,0.0458173674033,0.0403833349176,0.0429457149535,0.0334843425735,0.03321616118,0.0297901298801,0.0206052670737,0.0205898104515,0.0151686751473,0.019753503212,0.0102980095473,0.0157508379256,0.00828811077611,0.00714750303629,0.00686501376946,0.00515031348768,0.00286023694447,0.0020027123417,0.00171699378058,0.00171610897394,0.00143394163675,0.0,0.000860610728345,0.00143568925484,0.000860467759588,0.000860586933545,0.0,0.00114506076669,0.000573732620615,0.0,0.0,0.000286204055032,0.000286335526301,0.000286785028071,0.0,0.000286335526301,0.0,0.0,0.0,0.000286459699166,0.000286335526301,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0])

    # Creating weights for histo: y11_PT_15
    y11_PT_15_weights = numpy.array([0.0140786721352,0.0126508468167,0.0131291397575,0.0118576272928,0.0120705777288,0.0110094046884,0.0115329481823,0.011378915249,0.0106465662478,0.00982336828481,0.00870349986623,0.00993725533976,0.00943896280282,0.00865876061872,0.00813865796056,0.00876584144062,0.00792551473712,0.00837729102975,0.00766659708171,0.0072976984115,0.00673553876517,0.00671828848482,0.00709829338509,0.00587569862501,0.00699641363169,0.0064987665134,0.00589757161168,0.005461742189,0.00576570922815,0.00522673016991,0.00561502492794,0.00524711114983,0.00518375534613,0.00494642568734,0.00494417091308,0.00537443883867,0.00540033521435,0.00535491282892,0.00518431694418,0.00576611575808,0.00589196820429,0.00539652556789,0.00548119276021,0.00563742598442,0.00464392131773,0.00490127152784,0.00414438320661,0.00431654737486,0.00384418264631,0.00311096232999,0.00300315394525,0.00280600662681,0.00243768338505,0.00183555220719,0.00177111972783,0.00120912814181,0.00133936356741,0.000776226153731,0.000842834196875,0.000647641155825,0.000713069423965,0.000324001211315,0.000302282286914,0.000259192042157,0.000194350392516,0.000108102427417,0.000129744320683,0.000129547384173,2.15937844299e-05,4.32073840507e-05,2.16090062516e-05,0.0,2.15831434042e-05,4.32901568973e-05,4.32291774078e-05,4.32002592993e-05,0.0,2.16407197773e-05,0.0,2.15598454673e-05])

    # Creating weights for histo: y11_PT_16
    y11_PT_16_weights = numpy.array([0.00328983764772,0.00299961992615,0.00278016107878,0.00337320699966,0.00300798582193,0.00331817149463,0.00289307022603,0.00277981355178,0.00243555538113,0.00231888432832,0.00241398791469,0.00257869492223,0.0018741165957,0.00227071916483,0.00178449472801,0.00195357849658,0.00198367077072,0.0017865100876,0.00170296251669,0.00141737507264,0.00161532333512,0.00170277390161,0.00110585958934,0.00147188290098,0.00144601293142,0.00122078929423,0.00113502497629,0.001671428154,0.00127404944122,0.000905470172434,0.000764132870733,0.00124656391664,0.00101871407433,0.000822706765018,0.000936986119164,0.00105023432802,0.000678375384516,0.000823143698541,0.000936367550801,0.000823489294839,0.000677625379657,0.000989755569908,0.000681126788477,0.000766872244914,0.000739292264275,0.000936721166953,0.000878382224685,0.000512626092994,0.000765669860888,0.000792734788685,0.000794627325697,0.000850552885995,0.000653238191978,0.000624481520548,0.000679714848638,0.000568226255144,0.000625441229735,0.00059426033468,0.000792351469371,0.000936456214741,0.000848043265778,0.000823300085693,0.00076791571702,0.000594896576425,0.000709176227603,0.000738059880054,0.000565723466654,0.000652775119671,0.000594360879886,0.00053887373827,0.000395302907249,0.000397929706443,0.000505827930145,0.000425889590534,0.000142035043845,0.000424347847873,0.000253168818208,0.000141662625591,0.000340824633555,0.000198296829092])

    # Creating a new Canvas
    fig   = plt.figure(figsize=(12,6),dpi=80)
    frame = gridspec.GridSpec(1,1,right=0.7)
    pad   = fig.add_subplot(frame[0])

    # Creating a new Stack
    pad.hist(x=xData, bins=xBinning, weights=y11_PT_0_weights+y11_PT_1_weights+y11_PT_2_weights+y11_PT_3_weights+y11_PT_4_weights+y11_PT_5_weights+y11_PT_6_weights+y11_PT_7_weights+y11_PT_8_weights+y11_PT_9_weights+y11_PT_10_weights+y11_PT_11_weights+y11_PT_12_weights+y11_PT_13_weights+y11_PT_14_weights+y11_PT_15_weights+y11_PT_16_weights,\
             label="$bg\_vbf\_1600\_inf$", histtype="step", rwidth=1.0,\
             color=None, edgecolor="#e5e5e5", linewidth=1, linestyle="solid",\
             bottom=None, cumulative=False, normed=False, align="mid", orientation="vertical")

    pad.hist(x=xData, bins=xBinning, weights=y11_PT_0_weights+y11_PT_1_weights+y11_PT_2_weights+y11_PT_3_weights+y11_PT_4_weights+y11_PT_5_weights+y11_PT_6_weights+y11_PT_7_weights+y11_PT_8_weights+y11_PT_9_weights+y11_PT_10_weights+y11_PT_11_weights+y11_PT_12_weights+y11_PT_13_weights+y11_PT_14_weights+y11_PT_15_weights,\
             label="$bg\_vbf\_1200\_1600$", histtype="step", rwidth=1.0,\
             color=None, edgecolor="#f2f2f2", linewidth=1, linestyle="solid",\
             bottom=None, cumulative=False, normed=False, align="mid", orientation="vertical")

    pad.hist(x=xData, bins=xBinning, weights=y11_PT_0_weights+y11_PT_1_weights+y11_PT_2_weights+y11_PT_3_weights+y11_PT_4_weights+y11_PT_5_weights+y11_PT_6_weights+y11_PT_7_weights+y11_PT_8_weights+y11_PT_9_weights+y11_PT_10_weights+y11_PT_11_weights+y11_PT_12_weights+y11_PT_13_weights+y11_PT_14_weights,\
             label="$bg\_vbf\_800\_1200$", histtype="step", rwidth=1.0,\
             color=None, edgecolor="#ccc6aa", linewidth=1, linestyle="solid",\
             bottom=None, cumulative=False, normed=False, align="mid", orientation="vertical")

    pad.hist(x=xData, bins=xBinning, weights=y11_PT_0_weights+y11_PT_1_weights+y11_PT_2_weights+y11_PT_3_weights+y11_PT_4_weights+y11_PT_5_weights+y11_PT_6_weights+y11_PT_7_weights+y11_PT_8_weights+y11_PT_9_weights+y11_PT_10_weights+y11_PT_11_weights+y11_PT_12_weights+y11_PT_13_weights,\
             label="$bg\_vbf\_600\_800$", histtype="step", rwidth=1.0,\
             color=None, edgecolor="#ccc6aa", linewidth=1, linestyle="solid",\
             bottom=None, cumulative=False, normed=False, align="mid", orientation="vertical")

    pad.hist(x=xData, bins=xBinning, weights=y11_PT_0_weights+y11_PT_1_weights+y11_PT_2_weights+y11_PT_3_weights+y11_PT_4_weights+y11_PT_5_weights+y11_PT_6_weights+y11_PT_7_weights+y11_PT_8_weights+y11_PT_9_weights+y11_PT_10_weights+y11_PT_11_weights+y11_PT_12_weights,\
             label="$bg\_vbf\_400\_600$", histtype="step", rwidth=1.0,\
             color=None, edgecolor="#c1bfa8", linewidth=1, linestyle="solid",\
             bottom=None, cumulative=False, normed=False, align="mid", orientation="vertical")

    pad.hist(x=xData, bins=xBinning, weights=y11_PT_0_weights+y11_PT_1_weights+y11_PT_2_weights+y11_PT_3_weights+y11_PT_4_weights+y11_PT_5_weights+y11_PT_6_weights+y11_PT_7_weights+y11_PT_8_weights+y11_PT_9_weights+y11_PT_10_weights+y11_PT_11_weights,\
             label="$bg\_vbf\_200\_400$", histtype="step", rwidth=1.0,\
             color=None, edgecolor="#bab5a3", linewidth=1, linestyle="solid",\
             bottom=None, cumulative=False, normed=False, align="mid", orientation="vertical")

    pad.hist(x=xData, bins=xBinning, weights=y11_PT_0_weights+y11_PT_1_weights+y11_PT_2_weights+y11_PT_3_weights+y11_PT_4_weights+y11_PT_5_weights+y11_PT_6_weights+y11_PT_7_weights+y11_PT_8_weights+y11_PT_9_weights+y11_PT_10_weights,\
             label="$bg\_vbf\_100\_200$", histtype="step", rwidth=1.0,\
             color=None, edgecolor="#b2a596", linewidth=1, linestyle="solid",\
             bottom=None, cumulative=False, normed=False, align="mid", orientation="vertical")

    pad.hist(x=xData, bins=xBinning, weights=y11_PT_0_weights+y11_PT_1_weights+y11_PT_2_weights+y11_PT_3_weights+y11_PT_4_weights+y11_PT_5_weights+y11_PT_6_weights+y11_PT_7_weights+y11_PT_8_weights+y11_PT_9_weights,\
             label="$bg\_vbf\_0\_100$", histtype="step", rwidth=1.0,\
             color=None, edgecolor="#b7a39b", linewidth=1, linestyle="solid",\
             bottom=None, cumulative=False, normed=False, align="mid", orientation="vertical")

    pad.hist(x=xData, bins=xBinning, weights=y11_PT_0_weights+y11_PT_1_weights+y11_PT_2_weights+y11_PT_3_weights+y11_PT_4_weights+y11_PT_5_weights+y11_PT_6_weights+y11_PT_7_weights+y11_PT_8_weights,\
             label="$bg\_dip\_1600\_inf$", histtype="step", rwidth=1.0,\
             color=None, edgecolor="#ad998c", linewidth=1, linestyle="solid",\
             bottom=None, cumulative=False, normed=False, align="mid", orientation="vertical")

    pad.hist(x=xData, bins=xBinning, weights=y11_PT_0_weights+y11_PT_1_weights+y11_PT_2_weights+y11_PT_3_weights+y11_PT_4_weights+y11_PT_5_weights+y11_PT_6_weights+y11_PT_7_weights,\
             label="$bg\_dip\_1200\_1600$", histtype="step", rwidth=1.0,\
             color=None, edgecolor="#9b8e82", linewidth=1, linestyle="solid",\
             bottom=None, cumulative=False, normed=False, align="mid", orientation="vertical")

    pad.hist(x=xData, bins=xBinning, weights=y11_PT_0_weights+y11_PT_1_weights+y11_PT_2_weights+y11_PT_3_weights+y11_PT_4_weights+y11_PT_5_weights+y11_PT_6_weights,\
             label="$bg\_dip\_800\_1200$", histtype="step", rwidth=1.0,\
             color=None, edgecolor="#876656", linewidth=1, linestyle="solid",\
             bottom=None, cumulative=False, normed=False, align="mid", orientation="vertical")

    pad.hist(x=xData, bins=xBinning, weights=y11_PT_0_weights+y11_PT_1_weights+y11_PT_2_weights+y11_PT_3_weights+y11_PT_4_weights+y11_PT_5_weights,\
             label="$bg\_dip\_600\_800$", histtype="step", rwidth=1.0,\
             color=None, edgecolor="#afcec6", linewidth=1, linestyle="solid",\
             bottom=None, cumulative=False, normed=False, align="mid", orientation="vertical")

    pad.hist(x=xData, bins=xBinning, weights=y11_PT_0_weights+y11_PT_1_weights+y11_PT_2_weights+y11_PT_3_weights+y11_PT_4_weights,\
             label="$bg\_dip\_400\_600$", histtype="step", rwidth=1.0,\
             color=None, edgecolor="#84c1a3", linewidth=1, linestyle="solid",\
             bottom=None, cumulative=False, normed=False, align="mid", orientation="vertical")

    pad.hist(x=xData, bins=xBinning, weights=y11_PT_0_weights+y11_PT_1_weights+y11_PT_2_weights+y11_PT_3_weights,\
             label="$bg\_dip\_200\_400$", histtype="step", rwidth=1.0,\
             color=None, edgecolor="#89a8a0", linewidth=1, linestyle="solid",\
             bottom=None, cumulative=False, normed=False, align="mid", orientation="vertical")

    pad.hist(x=xData, bins=xBinning, weights=y11_PT_0_weights+y11_PT_1_weights+y11_PT_2_weights,\
             label="$bg\_dip\_100\_200$", histtype="step", rwidth=1.0,\
             color=None, edgecolor="#829e8c", linewidth=1, linestyle="solid",\
             bottom=None, cumulative=False, normed=False, align="mid", orientation="vertical")

    pad.hist(x=xData, bins=xBinning, weights=y11_PT_0_weights+y11_PT_1_weights,\
             label="$bg\_dip\_0\_100$", histtype="step", rwidth=1.0,\
             color=None, edgecolor="#adbcc6", linewidth=1, linestyle="solid",\
             bottom=None, cumulative=False, normed=False, align="mid", orientation="vertical")

    pad.hist(x=xData, bins=xBinning, weights=y11_PT_0_weights,\
             label="$signal$", histtype="step", rwidth=1.0,\
             color=None, edgecolor="#7a8e99", linewidth=1, linestyle="solid",\
             bottom=None, cumulative=False, normed=False, align="mid", orientation="vertical")


    # Axis
    plt.rc('text',usetex=False)
    plt.xlabel(r"p_{T} [ a_{1} ] ",\
               fontsize=16,color="black")
    plt.ylabel(r"$\mathrm{Events}$ $(\mathcal{L}_{\mathrm{int}} = 40.0\ \mathrm{fb}^{-1})$ ",\
               fontsize=16,color="black")

    # Boundary of y-axis
    ymax=(y11_PT_0_weights+y11_PT_1_weights+y11_PT_2_weights+y11_PT_3_weights+y11_PT_4_weights+y11_PT_5_weights+y11_PT_6_weights+y11_PT_7_weights+y11_PT_8_weights+y11_PT_9_weights+y11_PT_10_weights+y11_PT_11_weights+y11_PT_12_weights+y11_PT_13_weights+y11_PT_14_weights+y11_PT_15_weights+y11_PT_16_weights).max()*1.1
    ymin=0 # linear scale
    #ymin=min([x for x in (y11_PT_0_weights+y11_PT_1_weights+y11_PT_2_weights+y11_PT_3_weights+y11_PT_4_weights+y11_PT_5_weights+y11_PT_6_weights+y11_PT_7_weights+y11_PT_8_weights+y11_PT_9_weights+y11_PT_10_weights+y11_PT_11_weights+y11_PT_12_weights+y11_PT_13_weights+y11_PT_14_weights+y11_PT_15_weights+y11_PT_16_weights) if x])/100. # log scale
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
