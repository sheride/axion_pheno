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
    xBinning = numpy.linspace(0.0,1000.0,81,endpoint=True)

    # Creating data sequence: middle of each bin
    xData = numpy.array([6.25,18.75,31.25,43.75,56.25,68.75,81.25,93.75,106.25,118.75,131.25,143.75,156.25,168.75,181.25,193.75,206.25,218.75,231.25,243.75,256.25,268.75,281.25,293.75,306.25,318.75,331.25,343.75,356.25,368.75,381.25,393.75,406.25,418.75,431.25,443.75,456.25,468.75,481.25,493.75,506.25,518.75,531.25,543.75,556.25,568.75,581.25,593.75,606.25,618.75,631.25,643.75,656.25,668.75,681.25,693.75,706.25,718.75,731.25,743.75,756.25,768.75,781.25,793.75,806.25,818.75,831.25,843.75,856.25,868.75,881.25,893.75,906.25,918.75,931.25,943.75,956.25,968.75,981.25,993.75])

    # Creating weights for histo: y11_PT_0
    y11_PT_0_weights = numpy.array([0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,12.4787691437,13.2730204527,13.7847800075,14.0181438044,14.7223271918,15.0580388998,15.7908822622,15.6598703762,15.938270134,15.4756385365,15.5452384759,15.4879185258,15.6516823833,15.5247664937,15.2218027573,15.5329544866,15.0826068784,14.5954073022,15.2914026967,14.3988914732,14.0345197902,13.8666639362,13.3999363423,13.4572522924,12.9373047448,12.9782447091,12.4050732078,12.2658773289,11.9670055889,11.4839060092,11.2751061908,11.1932262621,10.239303092,10.1533271668,10.0182232843,9.86264741966,9.71935554432,8.98242018544,8.86369228873,8.57301254162,8.06944097972,8.09400495835,7.91795711151,7.47170149974,7.47988949262,6.98860192003,6.82893005894,6.75523812305,6.62013424059,6.16159463951,6.15750264307,5.91595085322,5.76037498857,5.57614314885,5.27727540886,4.89243174367])

    # Creating weights for histo: y11_PT_1
    y11_PT_1_weights = numpy.array([0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0242945760233,0.0,0.0,0.0121753353338,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0121313846429,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0])

    # Creating weights for histo: y11_PT_2
    y11_PT_2_weights = numpy.array([0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.150669137655,0.190759727264,0.190674235426,0.150548151622,0.070288133145,0.0200771817313,0.0300825613524,0.0501861054774,0.0401057913719,0.0502434994663,0.0401994398502,0.0200624014362,0.0100696699792,0.0201067175291,0.0,0.0401299142018,0.0100340931438,0.0,0.0100532492656,0.0200893009947,0.0,0.0,0.0,0.0201115106916,0.0100324444611,0.0100568565336,0.0,0.0,0.0,0.0,0.0100696699792,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0])

    # Creating weights for histo: y11_PT_3
    y11_PT_3_weights = numpy.array([0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.670932601278,0.709508397282,0.560955791361,0.528036321659,0.445512783756,0.390608433521,0.374044412312,0.286079905325,0.258512515517,0.23656033873,0.280502677402,0.176047559977,0.181583715245,0.165123939769,0.109949387521,0.0935181313366,0.0824680430984,0.0714216924313,0.0770245145918,0.0164873725636,0.044032121629,0.0220026055587,0.0219941472728,0.0274943365443,0.0220187624284,0.0219702796315,0.0219904625153,0.0275285718828,0.0219874643333,0.00549979520151,0.0,0.0165081120205,0.0110251602642,0.0110112906255,0.0,0.0109919568204,0.0055037074634,0.0,0.0,0.0,0.0,0.0,0.0,0.00547921012259,0.00550414622174,0.0,0.0,0.00549442853697,0.0,0.0,0.00548474335281,0.0,0.00549598044147,0.0,0.0,0.0])

    # Creating weights for histo: y11_PT_4
    y11_PT_4_weights = numpy.array([0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.272384704513,0.276321526047,0.254583250259,0.234846313336,0.249655499437,0.25556007037,0.219057501322,0.237883674744,0.226998042739,0.201329318598,0.21709676643,0.163851693088,0.172712898481,0.166764637194,0.134204260789,0.135215953016,0.11249797115,0.128295922064,0.0819150842869,0.0927379464803,0.0858457731383,0.069079499688,0.0562512502586,0.0503233911643,0.048368428208,0.046382922087,0.0276286493598,0.0305819489236,0.0177656041135,0.0246612927253,0.0118453527524,0.0167863509715,0.0148014501022,0.0157962473902,0.00888295437176,0.0118392922189,0.0049332622207,0.00592314935434,0.00394932539259,0.00691519695592,0.0039504172506,0.00197153122025,0.00493744286648,0.00591698460534,0.00296199394423,0.000986366653111,0.0,0.00197208155838,0.00197658246647,0.000983908770092,0.0,0.00197398549581,0.000987659326421,0.00197567859722,0.0,0.0])

    # Creating weights for histo: y11_PT_5
    y11_PT_5_weights = numpy.array([0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0526768168777,0.0610005918594,0.0549544958112,0.0531934017898,0.0499110010122,0.0519298473381,0.050419303601,0.0531871200277,0.0562119685569,0.0499122413601,0.0521777568816,0.0496551692464,0.0494102205335,0.0483960160293,0.0526847791112,0.0456171164936,0.0468840718994,0.0476388036164,0.0423485595994,0.0466380828946,0.0476396838633,0.0443658854988,0.0380733443179,0.0433619238679,0.0350367284878,0.0380644578251,0.0332725776089,0.0320134804075,0.028478480771,0.0294922851629,0.0307514343789,0.0282309593364,0.0249574290471,0.0196616634812,0.0209217129498,0.0176515396022,0.0158810389421,0.013362604472,0.0126057641635,0.00907543783786,0.0068060212221,0.00604944498766,0.00680508095834,0.00630093953681,0.00428469794159,0.00403461578866,0.00302769852867,0.00277230488576,0.00302710476211,0.000755186644628,0.00176520837548,0.00126070485237,0.00277280902718,0.00252161896345,0.000251644711264,0.000504413497854])

    # Creating weights for histo: y11_PT_6
    y11_PT_6_weights = numpy.array([0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0131746770756,0.0123226236711,0.00916571632146,0.0134647031383,0.0103099461663,0.00943751066061,0.0114566043084,0.00944753875835,0.0126023427167,0.00944223629295,0.0134462084909,0.0103067670864,0.0123040490468,0.00887537335052,0.0134401602413,0.0134588348366,0.0108768121079,0.0140343182842,0.0097220213195,0.00972461356926,0.012021410846,0.0146063527299,0.00860684306671,0.0117317546763,0.0111648987318,0.011748869723,0.0117340040253,0.0103078367768,0.0114533452516,0.0088851705151,0.0126030125228,0.0137355347561,0.0105854064445,0.0103172540513,0.0126091307522,0.0108766021687,0.0103077468029,0.00888107570019,0.0103133051942,0.011730225119,0.0100285576039,0.0105935440894,0.0100183105695,0.00859583025396,0.00829939404649,0.0114601732755,0.00572755836947,0.00629936188204,0.00915262810936,0.00658220902236,0.006868092284,0.00916026389946,0.00601625081809,0.00601905200739,0.00572046542226,0.00286891269903])

    # Creating weights for histo: y11_PT_7
    y11_PT_7_weights = numpy.array([0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.000734358806736,0.000928762534,0.000885583545251,0.000799094390865,0.000842334986651,0.000496877092735,0.000820632965138,0.000712660557083,0.00053985784932,0.000496604261574,0.000712567517886,0.000626502907226,0.000495176822351,0.000713047801312,0.000539783250324,0.000689512656147,0.000453748814539,0.000410176169401,0.000431973870412,0.000734365512264,0.000583300868225,0.000518647007716,0.000626453453959,0.000561499521083,0.00051851666902,0.000539948373945,0.000432150728707,0.000410355793726,0.000496839374141,0.000582981936561,0.000367260833621,0.000647854145818,0.000474996955641,0.000388804143673,0.000345829673521,0.000453713610519,0.000561600523095,0.000475487716455,0.000388716762265,0.000453539266797,0.000410392925586,0.000453429044684,0.000539995731735,0.00073452183488,0.000453899269819,0.000389079824683,0.000626388075063,0.000452069079835,0.000691111924518,0.000345460576127,0.00051852505093,0.000453667510015,0.000496810037457,0.000496654553032,0.000518267307207,0.000561342779371])

    # Creating weights for histo: y11_PT_8
    y11_PT_8_weights = numpy.array([0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,5.68585252373e-05,5.68781698116e-05,5.67658854044e-05,2.8368487681e-05,2.83498676537e-05,2.84489071929e-05,0.0,0.0,2.83973977234e-05,5.68373661153e-05,2.8368487681e-05,5.65065413875e-05,2.82573317603e-05,0.0,0.0,0.0,5.68463049163e-05,0.0,8.5224072914e-05,2.83973977234e-05,5.68781698116e-05,5.67472653771e-05,2.84292626186e-05,8.46910857684e-05,0.0,8.50232023162e-05,0.0,0.0,5.68569958411e-05,2.83973977234e-05,2.83973977234e-05,0.000113546040224,5.67948102953e-05,5.68373661153e-05,0.0,5.68266751906e-05,2.83498676537e-05,0.0,0.0,2.83498676537e-05,0.0,5.68173948739e-05,0.0,5.66824664941e-05,0.0,0.0,2.83498676537e-05,0.0,0.0,0.0,0.0,5.67183404862e-05,0.0,2.84080886482e-05,0.0,0.0])

    # Creating weights for histo: y11_PT_9
    y11_PT_9_weights = numpy.array([0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0])

    # Creating weights for histo: y11_PT_10
    y11_PT_10_weights = numpy.array([0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,1.05211370067,2.10758668394,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0])

    # Creating weights for histo: y11_PT_11
    y11_PT_11_weights = numpy.array([0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,1.84401800963,1.38149881123,0.691361931884,1.15221877857,1.15121775541,3.22584421885,1.38172015071,1.61189284242,1.84200981499,0.921916587899,0.230360177005,1.15168310629,0.230186256435,0.229952466611,0.460448367754,0.0,0.459655618892,0.230020174972,0.0,0.0,0.0,0.230128539092,0.0,0.230360177005,0.230673164862,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.230673164862,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0])

    # Creating weights for histo: y11_PT_12
    y11_PT_12_weights = numpy.array([0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.553686910493,0.581451249288,0.470909359278,0.359780800664,0.553838087964,0.4430426968,0.553487648585,0.526333789807,0.526393414509,0.387844070789,0.38780214116,0.359808304963,0.443033464588,0.443181949331,0.526179534932,0.360012567652,0.443086165132,0.415223349409,0.332341551134,0.360086656153,0.387772521146,0.33224788265,0.387776367901,0.415405685596,0.415059477647,0.0830721741801,0.221540274435,0.083135414832,0.0552810235032,0.13841212997,0.0,0.0829900074935,0.0830284365759,0.0,0.110822433851,0.110805046519,0.0830170117135,0.0276234283127,0.0555005193427,0.0,0.027638149844,0.0,0.0,0.0276586838221,0.0,0.0,0.0,0.0,0.0276696162998,0.0,0.0,0.0277263944034,0.0,0.0,0.0277307066158,0.0])

    # Creating weights for histo: y11_PT_13
    y11_PT_13_weights = numpy.array([0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0604982741732,0.0201648290679,0.0806575927152,0.110906435462,0.0302369113657,0.09063419362,0.0504804596321,0.0604303757543,0.0402771200046,0.0605378977679,0.0605255597731,0.0605260088688,0.0604937043207,0.070569264076,0.0302280386907,0.070593660898,0.100726891839,0.0503884981786,0.0908014514343,0.0806495818184,0.0908597731903,0.100838983705,0.0705777604817,0.121004413591,0.120929705909,0.100830426611,0.100753048631,0.120891957593,0.161378787096,0.171388281228,0.100863744659,0.080587254614,0.100814101374,0.100775988926,0.141116498186,0.0706424545419,0.0805940517386,0.0605775517069,0.0504246989356,0.0504051936157,0.0705497830316,0.0,0.0201634332299,0.0201955435744,0.050432200048,0.0,0.0201648290679,0.0201524607288,0.0100921884349,0.0201783201464,0.0,0.010042957833,0.020153067615,0.0403817593092,0.0,0.0])

    # Creating weights for histo: y11_PT_14
    y11_PT_14_weights = numpy.array([0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0282811922533,0.0282834891781,0.019829151578,0.0169707075591,0.0226401912246,0.0141615185337,0.0113143398343,0.0169808532721,0.0198036430164,0.0113055291848,0.0113252281042,0.0169770404539,0.0113190721919,0.00564890368115,0.0056493846118,0.014137556645,0.0,0.0141470598346,0.00848432458798,0.0169694455971,0.0113117581986,0.0226344392941,0.0169754360693,0.0141584059505,0.0113136857686,0.022611770147,0.00849108070174,0.0226283680255,0.0169938653318,0.0226378481305,0.0141402767887,0.0169733622963,0.014153596644,0.0084922772572,0.0311022929692,0.0141301580079,0.0311200797083,0.0226332619758,0.0424427838885,0.0254657511294,0.0226473782523,0.0311206145032,0.0197792963832,0.0367975045007,0.031124138763,0.0480709036707,0.0594579948462,0.045294933487,0.045274503553,0.0424417066038,0.0311224920564,0.0367822301433,0.0226548461434,0.0282613625208,0.0197920314268,0.0141513574309])

    # Creating weights for histo: y11_PT_15
    y11_PT_15_weights = numpy.array([0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.00456753990495,0.00153333590369,0.0030696312696,0.0,0.0,0.0,0.0,0.00306733839552,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.00151727396619,0.00152449651954,0.0,0.0,0.0015126539431,0.0,0.0,0.00150849604052,0.0,0.0,0.0,0.00152305579093,0.00153219773991,0.0,0.0,0.00152094965608,0.00152767581401,0.0,0.00153629536591,0.0,0.0,0.0,0.00152162924505,0.0,0.0,0.0015126539431,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.00306015366276,0.00152644428062,0.0,0.0,0.00150849604052,0.0,0.00154541013132])

    # Creating weights for histo: y11_PT_16
    y11_PT_16_weights = numpy.array([0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.000180552998633,0.0,0.000180503335663,0.0,0.0,0.0,0.0,0.0,0.000180003587594,0.0,0.0,0.000180626107144,0.0,0.0,0.0,0.0,0.0,0.000180626107144,0.0,0.0,0.0,0.0,0.0,0.0,0.000180626107144,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.000180734287722,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0])

    # Creating a new Canvas
    fig   = plt.figure(figsize=(12,6),dpi=80)
    frame = gridspec.GridSpec(1,1,right=0.7)
    pad   = fig.add_subplot(frame[0])

    # Creating a new Stack
    pad.hist(x=xData, bins=xBinning, weights=y11_PT_0_weights+y11_PT_1_weights+y11_PT_2_weights+y11_PT_3_weights+y11_PT_4_weights+y11_PT_5_weights+y11_PT_6_weights+y11_PT_7_weights+y11_PT_8_weights+y11_PT_9_weights+y11_PT_10_weights+y11_PT_11_weights+y11_PT_12_weights+y11_PT_13_weights+y11_PT_14_weights+y11_PT_15_weights+y11_PT_16_weights,\
             label="$bg\_dip\_1600\_inf$", histtype="step", rwidth=1.0,\
             color=None, edgecolor="#e5e5e5", linewidth=1, linestyle="solid",\
             bottom=None, cumulative=False, normed=False, align="mid", orientation="vertical")

    pad.hist(x=xData, bins=xBinning, weights=y11_PT_0_weights+y11_PT_1_weights+y11_PT_2_weights+y11_PT_3_weights+y11_PT_4_weights+y11_PT_5_weights+y11_PT_6_weights+y11_PT_7_weights+y11_PT_8_weights+y11_PT_9_weights+y11_PT_10_weights+y11_PT_11_weights+y11_PT_12_weights+y11_PT_13_weights+y11_PT_14_weights+y11_PT_15_weights,\
             label="$bg\_dip\_1200\_1600$", histtype="step", rwidth=1.0,\
             color=None, edgecolor="#f2f2f2", linewidth=1, linestyle="solid",\
             bottom=None, cumulative=False, normed=False, align="mid", orientation="vertical")

    pad.hist(x=xData, bins=xBinning, weights=y11_PT_0_weights+y11_PT_1_weights+y11_PT_2_weights+y11_PT_3_weights+y11_PT_4_weights+y11_PT_5_weights+y11_PT_6_weights+y11_PT_7_weights+y11_PT_8_weights+y11_PT_9_weights+y11_PT_10_weights+y11_PT_11_weights+y11_PT_12_weights+y11_PT_13_weights+y11_PT_14_weights,\
             label="$bg\_dip\_800\_1200$", histtype="step", rwidth=1.0,\
             color=None, edgecolor="#ccc6aa", linewidth=1, linestyle="solid",\
             bottom=None, cumulative=False, normed=False, align="mid", orientation="vertical")

    pad.hist(x=xData, bins=xBinning, weights=y11_PT_0_weights+y11_PT_1_weights+y11_PT_2_weights+y11_PT_3_weights+y11_PT_4_weights+y11_PT_5_weights+y11_PT_6_weights+y11_PT_7_weights+y11_PT_8_weights+y11_PT_9_weights+y11_PT_10_weights+y11_PT_11_weights+y11_PT_12_weights+y11_PT_13_weights,\
             label="$bg\_dip\_600\_800$", histtype="step", rwidth=1.0,\
             color=None, edgecolor="#ccc6aa", linewidth=1, linestyle="solid",\
             bottom=None, cumulative=False, normed=False, align="mid", orientation="vertical")

    pad.hist(x=xData, bins=xBinning, weights=y11_PT_0_weights+y11_PT_1_weights+y11_PT_2_weights+y11_PT_3_weights+y11_PT_4_weights+y11_PT_5_weights+y11_PT_6_weights+y11_PT_7_weights+y11_PT_8_weights+y11_PT_9_weights+y11_PT_10_weights+y11_PT_11_weights+y11_PT_12_weights,\
             label="$bg\_dip\_400\_600$", histtype="step", rwidth=1.0,\
             color=None, edgecolor="#c1bfa8", linewidth=1, linestyle="solid",\
             bottom=None, cumulative=False, normed=False, align="mid", orientation="vertical")

    pad.hist(x=xData, bins=xBinning, weights=y11_PT_0_weights+y11_PT_1_weights+y11_PT_2_weights+y11_PT_3_weights+y11_PT_4_weights+y11_PT_5_weights+y11_PT_6_weights+y11_PT_7_weights+y11_PT_8_weights+y11_PT_9_weights+y11_PT_10_weights+y11_PT_11_weights,\
             label="$bg\_dip\_200\_400$", histtype="step", rwidth=1.0,\
             color=None, edgecolor="#bab5a3", linewidth=1, linestyle="solid",\
             bottom=None, cumulative=False, normed=False, align="mid", orientation="vertical")

    pad.hist(x=xData, bins=xBinning, weights=y11_PT_0_weights+y11_PT_1_weights+y11_PT_2_weights+y11_PT_3_weights+y11_PT_4_weights+y11_PT_5_weights+y11_PT_6_weights+y11_PT_7_weights+y11_PT_8_weights+y11_PT_9_weights+y11_PT_10_weights,\
             label="$bg\_dip\_100\_200$", histtype="step", rwidth=1.0,\
             color=None, edgecolor="#b2a596", linewidth=1, linestyle="solid",\
             bottom=None, cumulative=False, normed=False, align="mid", orientation="vertical")

    pad.hist(x=xData, bins=xBinning, weights=y11_PT_0_weights+y11_PT_1_weights+y11_PT_2_weights+y11_PT_3_weights+y11_PT_4_weights+y11_PT_5_weights+y11_PT_6_weights+y11_PT_7_weights+y11_PT_8_weights+y11_PT_9_weights,\
             label="$bg\_dip\_0\_100$", histtype="step", rwidth=1.0,\
             color=None, edgecolor="#b7a39b", linewidth=1, linestyle="solid",\
             bottom=None, cumulative=False, normed=False, align="mid", orientation="vertical")

    pad.hist(x=xData, bins=xBinning, weights=y11_PT_0_weights+y11_PT_1_weights+y11_PT_2_weights+y11_PT_3_weights+y11_PT_4_weights+y11_PT_5_weights+y11_PT_6_weights+y11_PT_7_weights+y11_PT_8_weights,\
             label="$bg\_vbf\_1600\_inf$", histtype="step", rwidth=1.0,\
             color=None, edgecolor="#ad998c", linewidth=1, linestyle="solid",\
             bottom=None, cumulative=False, normed=False, align="mid", orientation="vertical")

    pad.hist(x=xData, bins=xBinning, weights=y11_PT_0_weights+y11_PT_1_weights+y11_PT_2_weights+y11_PT_3_weights+y11_PT_4_weights+y11_PT_5_weights+y11_PT_6_weights+y11_PT_7_weights,\
             label="$bg\_vbf\_1200\_1600$", histtype="step", rwidth=1.0,\
             color=None, edgecolor="#9b8e82", linewidth=1, linestyle="solid",\
             bottom=None, cumulative=False, normed=False, align="mid", orientation="vertical")

    pad.hist(x=xData, bins=xBinning, weights=y11_PT_0_weights+y11_PT_1_weights+y11_PT_2_weights+y11_PT_3_weights+y11_PT_4_weights+y11_PT_5_weights+y11_PT_6_weights,\
             label="$bg\_vbf\_800\_1200$", histtype="step", rwidth=1.0,\
             color=None, edgecolor="#876656", linewidth=1, linestyle="solid",\
             bottom=None, cumulative=False, normed=False, align="mid", orientation="vertical")

    pad.hist(x=xData, bins=xBinning, weights=y11_PT_0_weights+y11_PT_1_weights+y11_PT_2_weights+y11_PT_3_weights+y11_PT_4_weights+y11_PT_5_weights,\
             label="$bg\_vbf\_600\_800$", histtype="step", rwidth=1.0,\
             color=None, edgecolor="#afcec6", linewidth=1, linestyle="solid",\
             bottom=None, cumulative=False, normed=False, align="mid", orientation="vertical")

    pad.hist(x=xData, bins=xBinning, weights=y11_PT_0_weights+y11_PT_1_weights+y11_PT_2_weights+y11_PT_3_weights+y11_PT_4_weights,\
             label="$bg\_vbf\_400\_600$", histtype="step", rwidth=1.0,\
             color=None, edgecolor="#84c1a3", linewidth=1, linestyle="solid",\
             bottom=None, cumulative=False, normed=False, align="mid", orientation="vertical")

    pad.hist(x=xData, bins=xBinning, weights=y11_PT_0_weights+y11_PT_1_weights+y11_PT_2_weights+y11_PT_3_weights,\
             label="$bg\_vbf\_200\_400$", histtype="step", rwidth=1.0,\
             color=None, edgecolor="#89a8a0", linewidth=1, linestyle="solid",\
             bottom=None, cumulative=False, normed=False, align="mid", orientation="vertical")

    pad.hist(x=xData, bins=xBinning, weights=y11_PT_0_weights+y11_PT_1_weights+y11_PT_2_weights,\
             label="$bg\_vbf\_100\_200$", histtype="step", rwidth=1.0,\
             color=None, edgecolor="#829e8c", linewidth=1, linestyle="solid",\
             bottom=None, cumulative=False, normed=False, align="mid", orientation="vertical")

    pad.hist(x=xData, bins=xBinning, weights=y11_PT_0_weights+y11_PT_1_weights,\
             label="$bg\_vbf\_0\_100$", histtype="step", rwidth=1.0,\
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
