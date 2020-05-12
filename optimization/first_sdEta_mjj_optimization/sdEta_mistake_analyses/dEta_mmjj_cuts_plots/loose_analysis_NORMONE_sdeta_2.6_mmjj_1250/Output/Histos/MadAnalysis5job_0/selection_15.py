def selection_15():

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

    # Creating weights for histo: y16_TET_0
    y16_TET_0_weights = numpy.array([0.0,0.0,0.0,0.0,0.0,0.0,0.00818816930527,0.0409408465264,0.0491289998316,0.0532230764843,0.106446192969,0.131010692884,0.147387039495,0.184233769369,0.249739115811,0.286585885685,0.356185308779,0.282491809032,0.376655732043,0.458537225095,0.507666384927,0.51176038158,0.560889541411,0.560889541411,0.638677077811,0.638677077811,0.695994230948,0.933451236801,0.888416073622,0.912980853538,0.96210961337,1.04808554307,1.02352116316,1.19956661922,1.166813846,1.17090824265,1.22822539579,1.38380046859,1.34695369872,1.50662276817,1.62944546775,1.64582185436,1.57622231126,1.72360939076,1.97744278322,1.92421962674,1.95697239996,2.00200716314,1.99791316649,2.07160670623,2.15758223594,2.39913323844,2.35819247192,2.59155508112,2.76350694053,2.66115462421,2.84538847358,2.88632924011,2.77169493383,2.92317600998,2.90270562672,3.12788024261,3.07465708613,3.28754971207,3.39809002169,3.52091232127,3.44312478487,3.68467578737,3.67648739407,3.58232347106,3.8034040903,3.93850877984,4.08998865598,4.1227446292,4.20052856561,4.1227446292,4.20871655891,4.25784851874,4.38066841832,4.35201244175])

    # Creating weights for histo: y16_TET_1
    y16_TET_1_weights = numpy.array([0.0,0.0,0.0,0.0,0.0,0.388830979109,2.64770430193,7.08396095784,12.6117102506,17.3989760847,19.0050224752,14.775763776,9.92675527247,6.8518141285,4.33729134787,3.08673693776,1.45784836308,0.93515330878,0.644184520708,0.485982298337,0.243079146992,0.242952777792,0.230640051861,0.0850463114179,0.121512617403,0.0849844285608,0.0607736519231,0.0364426062531,0.0,0.0121474085812,0.0,0.024267728893,0.0,0.0242461560083,0.0121666142964,0.0122009843156,0.0121676116318,0.0,0.0,0.0,0.0,0.0,0.0,0.0242798851695,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0])

    # Creating weights for histo: y16_TET_2
    y16_TET_2_weights = numpy.array([0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.291200564859,6.86772933567,19.0460127348,30.3607216665,37.4900497044,42.371023072,43.5532563196,47.7195634703,48.2334719286,42.6795251665,34.3485802309,28.2426312414,21.9368707425,17.6100648193,12.69000598,11.2155386897,8.30286322876,6.04427336321,4.47787525853,3.20211868779,2.58045638982,2.0079164184,1.41556471188,0.913605441331,0.702780663465,0.662759685882,0.441664589827,0.381508830083,0.200603920836,0.210925972834,0.18071441974,0.15060567313,0.100373218369,0.150643399143,0.130498162785,0.0803902079989,0.0802486424784,0.0702820331562,0.110529821347,0.0602520375209,0.0502429915992,0.0300959040636,0.0200641357603,0.060178527579,0.0201156133801,0.0300832515936,0.010061122695,0.0100408671731,0.0401215444724,0.0301027633387,0.020077172515,0.0100533874161,0.0201246006832,0.0301363242014,0.0,0.0401277095558,0.0,0.0100272973783,0.0,0.0,0.0,0.0,0.0,0.0100300948055,0.0,0.0,0.0,0.0,0.0,0.0,0.0])

    # Creating weights for histo: y16_TET_3
    y16_TET_3_weights = numpy.array([0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.203572487752,4.49378878582,12.7610336518,19.598382895,23.1066242957,27.0175972929,28.8292536901,30.2636749803,31.6638571988,31.0389738275,30.3453441852,29.5584996045,30.0864467526,28.3547614193,26.9692571512,25.7861241596,24.2447971774,22.2483521689,19.5976313254,16.9138982968,14.8562430257,12.3088894034,10.7699877565,9.69163574941,8.07957997765,7.05136375411,6.2429064704,5.03885953226,4.59863477094,4.10902985815,3.58627300886,3.38302584917,2.87089497472,2.40892832162,2.12296991602,1.84810752094,1.49068622513,1.45190929829,1.13861366708,0.791985722691,0.945947388054,0.781094464108,0.742449569753,0.610669362806,0.461998340903,0.423463541333,0.462012559787,0.313417832351,0.241954820265,0.209058823677,0.203518049741,0.165077541682,0.143016984402,0.0769988297255,0.0715443441005,0.0715060749909,0.0825044220806,0.0550105043748,0.0495124683406,0.0495093808116,0.0495233153175,0.043970963148,0.0495077964217])

    # Creating weights for histo: y16_TET_4
    y16_TET_4_weights = numpy.array([0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0384787002008,1.0608193934,2.61525690075,4.11417905482,5.36257204887,6.09984669198,6.95442823748,7.37944830838,7.62726545276,7.75086538586,7.81684600912,7.78748120467,7.84444716164,7.74862875456,7.67765779803,7.33423869477,7.19701054229,6.78074058988,5.94177137216,5.5874256436,4.94998171569,4.29079676958,3.96910104799,3.51222982426,3.22510368443,2.90127835315,2.66847349407,2.42956760185,2.18796532634,2.07541306919,1.86518014886,1.77424946257,1.65392751706,1.50885432019,1.34206174994,1.28093557858,1.11810721685,0.980875456908,0.940422492683,0.858584634526,0.798396004501,0.755924460489,0.639458098569,0.561542361781,0.578276612679,0.469791577351,0.455904822641])

    # Creating weights for histo: y16_TET_5
    y16_TET_5_weights = numpy.array([0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0113406419825,0.295946049467,0.804847424971,1.26291572506,1.6269063146,1.90843687219,2.07057384647,2.22607397627,2.2666920406,2.32946719502,2.30324789841,2.35620582032,2.33601361709,2.23673901885,2.21297393034,2.15050085077,2.16134433757,1.97001813079,1.81547783882,1.60319323897,1.48697684289,1.25884071536,1.20262518628,1.0644957606,0.959156859739,0.870185214358,0.820001179766,0.756465836989,0.702525271604,0.664499049472,0.622127750718])

    # Creating weights for histo: y16_TET_6
    y16_TET_6_weights = numpy.array([0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.00257117243545,0.0813043922308,0.197818183215,0.288272125143,0.382520410395,0.466400429586,0.517349355456,0.559755210764,0.576279338023,0.583517240852,0.600117842783,0.596929498753,0.619829314403,0.598342530761,0.594086940199])

    # Creating weights for histo: y16_TET_7
    y16_TET_7_weights = numpy.array([0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0])

    # Creating weights for histo: y16_TET_8
    y16_TET_8_weights = numpy.array([0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0])

    # Creating weights for histo: y16_TET_9
    y16_TET_9_weights = numpy.array([0.0,0.0,0.0,0.0,0.0,0.0,0.0,15.6602037919,5.21469620307,26.0690233789,10.4224540315,20.829908251,13.0235714419,2.60548081724,13.0410058389,2.60449852185,0.0,2.61096113319,0.0,0.0,2.60521312828,2.60925653916,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0])

    # Creating weights for histo: y16_TET_10
    y16_TET_10_weights = numpy.array([0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,13.6894199245,22.1186114187,29.4916832559,37.9241222299,30.53388954,44.2310972595,40.0358074716,54.7706696168,55.800012957,36.8681218523,16.8591063607,23.1658312883,12.6379829485,15.7961531444,13.690251033,9.47942798008,5.26912436998,4.21217745208,10.5340970449,4.21384736464,2.10638230744,3.1595561464,1.0534543381,2.10774863452,1.05325887368,1.0534543381,0.0,1.05366365433,1.05401456683,0.0,1.05389798077,1.05609503163,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0])

    # Creating weights for histo: y16_TET_11
    y16_TET_11_weights = numpy.array([0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,9.6771037261,16.3542203796,23.4924047301,32.9362042207,35.0152124684,38.9323513128,34.0853691738,45.1406693142,41.6918641887,43.7701539034,44.4445375519,35.2364361262,38.4621540188,38.9262034361,42.6167738123,39.8557239672,31.0959718188,29.0227348903,28.3340881679,23.2562955259,19.1194584657,15.4341253119,14.9699913613,9.67207015206,8.7522594237,8.06627165793,6.91200012478,5.06705306988,4.60554733655,6.21843125856,4.14520585736,5.29646877336,3.2235980278,5.29753696694,2.30081326409,4.37740347505,2.07369033437,3.68656887699,1.38333757615,2.07300599885,0.690753907175,1.61198748475,1.15275454458,0.230411697933,0.230603089019,1.15113265786,0.230111988944,0.230603089019,0.230581686723,0.922126172417,0.460700745726,0.0,0.229965976873,0.230003632618,0.0,0.23044873889,0.0,0.0,0.230628641132,0.0,0.460592389399,0.230411697933])

    # Creating weights for histo: y16_TET_12
    y16_TET_12_weights = numpy.array([0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.193901297864,3.35099693471,9.49795073047,13.374582483,18.3596608857,21.3215381167,22.9015945347,23.5923183547,26.3344736848,25.476749217,24.9767706138,26.5008895667,27.6083321125,27.4406005075,26.998267501,25.916654676,26.5569501403,23.3978260202,19.6605878144,15.8956578705,13.955766589,11.8250685364,9.9134345232,9.1663154281,8.11362927429,6.56342668906,6.09194387702,4.8464042718,4.15367609006,3.82180957437,4.01488654482,3.51624366981,3.29492943625,2.63030040518,2.63044505777,2.13245658185,1.99328193756,2.10522803974,1.66187361665,1.5508912239,1.27320864526,1.6331631549,0.997137250278,1.13512505083,1.49581205658,0.913421871073,0.88578591647])

    # Creating weights for histo: y16_TET_13
    y16_TET_13_weights = numpy.array([0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0704930774857,1.88512290989,4.73946669714,8.07618628305,9.92925963065,11.7965448641,13.2786770693,13.1966522783,13.4695544681,13.1166664257,13.1568565708,13.1667053712,12.9252246779,12.4808392768,11.8569302081,11.6045751769,11.250952874,9.65851774463,8.97339197904,7.21860031483,6.51421386369,5.48436794571,5.14133659255,4.15369791219,3.33639857448,3.49848143044,2.69215655707,2.42928824997,2.32865875334,2.04688232711,1.71392915498])

    # Creating weights for histo: y16_TET_14
    y16_TET_14_weights = numpy.array([0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0198076244188,0.444225683924,1.23343190204,2.03407330978,2.44728178246,2.8660120182,3.19986207543,3.44863381399,3.48549789209,3.34376417609,3.33280760082,3.48553713539,3.49957546387,3.37554239955,3.19670837618])

    # Creating weights for histo: y16_TET_15
    y16_TET_15_weights = numpy.array([0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0])

    # Creating weights for histo: y16_TET_16
    y16_TET_16_weights = numpy.array([0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0])

    # Creating a new Canvas
    fig   = plt.figure(figsize=(12,6),dpi=80)
    frame = gridspec.GridSpec(1,1,right=0.7)
    pad   = fig.add_subplot(frame[0])

    # Creating a new Stack
    pad.hist(x=xData, bins=xBinning, weights=y16_TET_0_weights+y16_TET_1_weights+y16_TET_2_weights+y16_TET_3_weights+y16_TET_4_weights+y16_TET_5_weights+y16_TET_6_weights+y16_TET_7_weights+y16_TET_8_weights+y16_TET_9_weights+y16_TET_10_weights+y16_TET_11_weights+y16_TET_12_weights+y16_TET_13_weights+y16_TET_14_weights+y16_TET_15_weights+y16_TET_16_weights,\
             label="$bg\_dip\_1600\_inf$", histtype="step", rwidth=1.0,\
             color=None, edgecolor="#e5e5e5", linewidth=4, linestyle="dashdot",\
             bottom=None, cumulative=False, normed=False, align="mid", orientation="vertical")

    pad.hist(x=xData, bins=xBinning, weights=y16_TET_0_weights+y16_TET_1_weights+y16_TET_2_weights+y16_TET_3_weights+y16_TET_4_weights+y16_TET_5_weights+y16_TET_6_weights+y16_TET_7_weights+y16_TET_8_weights+y16_TET_9_weights+y16_TET_10_weights+y16_TET_11_weights+y16_TET_12_weights+y16_TET_13_weights+y16_TET_14_weights+y16_TET_15_weights,\
             label="$bg\_dip\_1200\_1600$", histtype="step", rwidth=1.0,\
             color=None, edgecolor="#f2f2f2", linewidth=4, linestyle="dashdot",\
             bottom=None, cumulative=False, normed=False, align="mid", orientation="vertical")

    pad.hist(x=xData, bins=xBinning, weights=y16_TET_0_weights+y16_TET_1_weights+y16_TET_2_weights+y16_TET_3_weights+y16_TET_4_weights+y16_TET_5_weights+y16_TET_6_weights+y16_TET_7_weights+y16_TET_8_weights+y16_TET_9_weights+y16_TET_10_weights+y16_TET_11_weights+y16_TET_12_weights+y16_TET_13_weights+y16_TET_14_weights,\
             label="$bg\_dip\_800\_1200$", histtype="step", rwidth=1.0,\
             color=None, edgecolor="#ccc6aa", linewidth=4, linestyle="dashdot",\
             bottom=None, cumulative=False, normed=False, align="mid", orientation="vertical")

    pad.hist(x=xData, bins=xBinning, weights=y16_TET_0_weights+y16_TET_1_weights+y16_TET_2_weights+y16_TET_3_weights+y16_TET_4_weights+y16_TET_5_weights+y16_TET_6_weights+y16_TET_7_weights+y16_TET_8_weights+y16_TET_9_weights+y16_TET_10_weights+y16_TET_11_weights+y16_TET_12_weights+y16_TET_13_weights,\
             label="$bg\_dip\_600\_800$", histtype="step", rwidth=1.0,\
             color=None, edgecolor="#ccc6aa", linewidth=4, linestyle="dashdot",\
             bottom=None, cumulative=False, normed=False, align="mid", orientation="vertical")

    pad.hist(x=xData, bins=xBinning, weights=y16_TET_0_weights+y16_TET_1_weights+y16_TET_2_weights+y16_TET_3_weights+y16_TET_4_weights+y16_TET_5_weights+y16_TET_6_weights+y16_TET_7_weights+y16_TET_8_weights+y16_TET_9_weights+y16_TET_10_weights+y16_TET_11_weights+y16_TET_12_weights,\
             label="$bg\_dip\_400\_600$", histtype="step", rwidth=1.0,\
             color=None, edgecolor="#c1bfa8", linewidth=4, linestyle="dashdot",\
             bottom=None, cumulative=False, normed=False, align="mid", orientation="vertical")

    pad.hist(x=xData, bins=xBinning, weights=y16_TET_0_weights+y16_TET_1_weights+y16_TET_2_weights+y16_TET_3_weights+y16_TET_4_weights+y16_TET_5_weights+y16_TET_6_weights+y16_TET_7_weights+y16_TET_8_weights+y16_TET_9_weights+y16_TET_10_weights+y16_TET_11_weights,\
             label="$bg\_dip\_200\_400$", histtype="step", rwidth=1.0,\
             color=None, edgecolor="#bab5a3", linewidth=4, linestyle="dashdot",\
             bottom=None, cumulative=False, normed=False, align="mid", orientation="vertical")

    pad.hist(x=xData, bins=xBinning, weights=y16_TET_0_weights+y16_TET_1_weights+y16_TET_2_weights+y16_TET_3_weights+y16_TET_4_weights+y16_TET_5_weights+y16_TET_6_weights+y16_TET_7_weights+y16_TET_8_weights+y16_TET_9_weights+y16_TET_10_weights,\
             label="$bg\_dip\_100\_200$", histtype="step", rwidth=1.0,\
             color=None, edgecolor="#b2a596", linewidth=4, linestyle="dashdot",\
             bottom=None, cumulative=False, normed=False, align="mid", orientation="vertical")

    pad.hist(x=xData, bins=xBinning, weights=y16_TET_0_weights+y16_TET_1_weights+y16_TET_2_weights+y16_TET_3_weights+y16_TET_4_weights+y16_TET_5_weights+y16_TET_6_weights+y16_TET_7_weights+y16_TET_8_weights+y16_TET_9_weights,\
             label="$bg\_dip\_0\_100$", histtype="step", rwidth=1.0,\
             color=None, edgecolor="#b7a39b", linewidth=4, linestyle="dashdot",\
             bottom=None, cumulative=False, normed=False, align="mid", orientation="vertical")

    pad.hist(x=xData, bins=xBinning, weights=y16_TET_0_weights+y16_TET_1_weights+y16_TET_2_weights+y16_TET_3_weights+y16_TET_4_weights+y16_TET_5_weights+y16_TET_6_weights+y16_TET_7_weights+y16_TET_8_weights,\
             label="$bg\_vbf\_1600\_inf$", histtype="step", rwidth=1.0,\
             color=None, edgecolor="#ad998c", linewidth=4, linestyle="dashdot",\
             bottom=None, cumulative=False, normed=False, align="mid", orientation="vertical")

    pad.hist(x=xData, bins=xBinning, weights=y16_TET_0_weights+y16_TET_1_weights+y16_TET_2_weights+y16_TET_3_weights+y16_TET_4_weights+y16_TET_5_weights+y16_TET_6_weights+y16_TET_7_weights,\
             label="$bg\_vbf\_1200\_1600$", histtype="step", rwidth=1.0,\
             color=None, edgecolor="#9b8e82", linewidth=4, linestyle="dashdot",\
             bottom=None, cumulative=False, normed=False, align="mid", orientation="vertical")

    pad.hist(x=xData, bins=xBinning, weights=y16_TET_0_weights+y16_TET_1_weights+y16_TET_2_weights+y16_TET_3_weights+y16_TET_4_weights+y16_TET_5_weights+y16_TET_6_weights,\
             label="$bg\_vbf\_800\_1200$", histtype="step", rwidth=1.0,\
             color=None, edgecolor="#876656", linewidth=4, linestyle="dashdot",\
             bottom=None, cumulative=False, normed=False, align="mid", orientation="vertical")

    pad.hist(x=xData, bins=xBinning, weights=y16_TET_0_weights+y16_TET_1_weights+y16_TET_2_weights+y16_TET_3_weights+y16_TET_4_weights+y16_TET_5_weights,\
             label="$bg\_vbf\_600\_800$", histtype="step", rwidth=1.0,\
             color=None, edgecolor="#afcec6", linewidth=4, linestyle="dashdot",\
             bottom=None, cumulative=False, normed=False, align="mid", orientation="vertical")

    pad.hist(x=xData, bins=xBinning, weights=y16_TET_0_weights+y16_TET_1_weights+y16_TET_2_weights+y16_TET_3_weights+y16_TET_4_weights,\
             label="$bg\_vbf\_400\_600$", histtype="step", rwidth=1.0,\
             color=None, edgecolor="#84c1a3", linewidth=4, linestyle="dashdot",\
             bottom=None, cumulative=False, normed=False, align="mid", orientation="vertical")

    pad.hist(x=xData, bins=xBinning, weights=y16_TET_0_weights+y16_TET_1_weights+y16_TET_2_weights+y16_TET_3_weights,\
             label="$bg\_vbf\_200\_400$", histtype="step", rwidth=1.0,\
             color=None, edgecolor="#89a8a0", linewidth=4, linestyle="dashdot",\
             bottom=None, cumulative=False, normed=False, align="mid", orientation="vertical")

    pad.hist(x=xData, bins=xBinning, weights=y16_TET_0_weights+y16_TET_1_weights+y16_TET_2_weights,\
             label="$bg\_vbf\_100\_200$", histtype="step", rwidth=1.0,\
             color=None, edgecolor="#829e8c", linewidth=4, linestyle="dashdot",\
             bottom=None, cumulative=False, normed=False, align="mid", orientation="vertical")

    pad.hist(x=xData, bins=xBinning, weights=y16_TET_0_weights+y16_TET_1_weights,\
             label="$bg\_vbf\_0\_100$", histtype="step", rwidth=1.0,\
             color=None, edgecolor="#adbcc6", linewidth=4, linestyle="dashdot",\
             bottom=None, cumulative=False, normed=False, align="mid", orientation="vertical")

    pad.hist(x=xData, bins=xBinning, weights=y16_TET_0_weights,\
             label="$signal$", histtype="step", rwidth=1.0,\
             color=None, edgecolor="#7a8e99", linewidth=3, linestyle="dashed",\
             bottom=None, cumulative=False, normed=False, align="mid", orientation="vertical")


    # Axis
    plt.rc('text',usetex=False)
    plt.xlabel(r"$E_{T}$ $(GeV)$ ",\
               fontsize=16,color="black")
    plt.ylabel(r"$\mathrm{Events}$ $(\mathcal{L}_{\mathrm{int}} = 40.0\ \mathrm{fb}^{-1})$ ",\
               fontsize=16,color="black")

    # Boundary of y-axis
    ymax=(y16_TET_0_weights+y16_TET_1_weights+y16_TET_2_weights+y16_TET_3_weights+y16_TET_4_weights+y16_TET_5_weights+y16_TET_6_weights+y16_TET_7_weights+y16_TET_8_weights+y16_TET_9_weights+y16_TET_10_weights+y16_TET_11_weights+y16_TET_12_weights+y16_TET_13_weights+y16_TET_14_weights+y16_TET_15_weights+y16_TET_16_weights).max()*1.1
    ymin=0 # linear scale
    #ymin=min([x for x in (y16_TET_0_weights+y16_TET_1_weights+y16_TET_2_weights+y16_TET_3_weights+y16_TET_4_weights+y16_TET_5_weights+y16_TET_6_weights+y16_TET_7_weights+y16_TET_8_weights+y16_TET_9_weights+y16_TET_10_weights+y16_TET_11_weights+y16_TET_12_weights+y16_TET_13_weights+y16_TET_14_weights+y16_TET_15_weights+y16_TET_16_weights) if x])/100. # log scale
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
    plt.savefig('../../HTML/MadAnalysis5job_0/selection_15.png')
    plt.savefig('../../PDF/MadAnalysis5job_0/selection_15.png')
    plt.savefig('../../DVI/MadAnalysis5job_0/selection_15.eps')

# Running!
if __name__ == '__main__':
    selection_15()
