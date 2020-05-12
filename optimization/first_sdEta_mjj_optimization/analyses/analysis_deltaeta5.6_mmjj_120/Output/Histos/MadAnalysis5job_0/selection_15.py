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
    y16_TET_0_weights = numpy.array([0.0,0.0,0.0,0.0,0.0122822529552,0.0450349195025,0.237456866468,0.429878813433,0.921168771642,1.33876559612,1.75226802428,2.12482968925,2.53833211741,2.96821093085,3.6027935602,3.90575608776,4.52396393184,4.93746356,4.97840752318,5.83816275005,6.21072641502,6.83302585542,7.45532529582,7.70097307493,8.30689653005,8.97013593363,9.26081567224,10.5217945383,10.4931385641,11.3569897873,11.5739735921,12.1799010473,12.8554244398,13.2402680937,13.91169549,14.2351311991,14.5094349524,15.4469781094,15.827729767,15.9914896197,17.1091766146,17.1583045705,17.5185842465,18.2555195838,19.107090818,19.0702428511,19.3977705566,20.2043018313,19.8644941369,20.3639736878,21.305612841,21.3711167821,22.0302641894,22.0343601857,23.1766071585,22.9227753868,22.9759993389,23.8930745142,23.6105827683,23.7415906505,24.7159857742,24.4826219841,24.8715576343,24.9943815239,25.0189455018,25.7681648281,26.2758283715,25.5962129827,26.0711245556,25.7231288686,26.2103244305,26.8981318119,26.6770520107,27.0455156794,26.6115440697,26.7343679592,26.5746961028,27.1069276242,27.065987661,27.3075394438])

    # Creating weights for histo: y16_TET_1
    y16_TET_1_weights = numpy.array([0.0,0.0,0.0,0.0,0.073039490393,33.1228575975,178.478488593,392.540765441,596.424400407,760.211657667,690.684228928,483.717415769,312.631328673,193.26930004,117.518394544,70.0088260894,38.4672013695,23.0493436352,13.059295113,8.60243607866,5.75885901662,3.72952043082,2.78272864513,2.27190709241,1.66458896396,1.38496511855,1.00850061325,0.704948699787,0.473755398689,0.425211094307,0.291627615347,0.33991375648,0.182355063136,0.206433422651,0.230804994731,0.206645120521,0.121643919373,0.145743588872,0.121474601134,0.0850049664453,0.0485631709281,0.0607065773377,0.109273593676,0.060764578949,0.0243530460128,0.0850212693844,0.0242829313578,0.0729059424841,0.048646287878,0.0121684416355,0.0364150659073,0.0,0.0,0.0,0.0,0.0243142434155,0.0121172175605,0.0,0.0121172175605,0.0,0.0,0.0242897529561,0.0,0.0,0.0121674442321,0.0243006242526,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0])

    # Creating weights for histo: y16_TET_2
    y16_TET_2_weights = numpy.array([0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,8.78502211798,206.776108969,497.228681738,723.616012544,846.88664425,898.84002311,897.668157918,873.856898509,825.280276471,699.95226931,552.605510216,422.823506262,319.966510009,244.907676723,184.297412345,141.10356051,104.929784463,78.0931211831,57.0663638783,41.6656338423,31.5656310496,23.3539633977,15.5927531225,12.6403139757,8.28233905664,6.98757264326,5.42171116765,4.01619894831,3.21288949134,2.76107802358,2.1787825071,2.06806025415,1.64648464383,1.34545536788,1.21473620235,0.95369455342,0.984181642886,0.763006137068,0.542376895631,0.532273897062,0.432015788723,0.45186146624,0.240867138432,0.301196502262,0.331381369513,0.231026032726,0.241069983504,0.220743659445,0.160648916581,0.150588106811,0.120542243597,0.180765412309,0.140687168213,0.0702801356227,0.0902789903,0.140543040365,0.070286044534,0.100460746805,0.0703023663517,0.0301483518327,0.0402405656061,0.0803323092914,0.0200725549155,0.0702946393139,0.0601966405925,0.0703368281137,0.0100301247523,0.0502418606566,0.030141017345,0.0301493187455,0.0300647799939])

    # Creating weights for histo: y16_TET_3
    y16_TET_3_weights = numpy.array([0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,3.03095109511,69.541812553,168.498953274,243.622892883,291.256550832,318.268302939,327.477569436,328.938671002,322.584859691,311.089790897,299.670488944,283.68535124,267.22639656,250.251821107,234.623010995,214.818493266,199.55035769,176.122356828,150.847960719,125.006064881,108.901244007,91.4721893879,77.7384034281,68.7470935531,56.1691073861,49.0683934674,42.5951021147,36.4461212774,32.0249128468,27.3804298966,23.8332376755,21.0779450341,18.5134182658,16.4289323238,14.2788359542,12.2277361729,10.3075525543,9.11978443616,8.00299339418,6.5239881036,6.08838767764,5.07683738657,4.23468387567,3.94370101986,3.11326029062,2.60141039138,2.5028159971,1.78207468405,1.50152449561,1.20441732279,1.18259403517,0.995677848928,0.792211584664,0.68745712281,0.522752199154,0.544542173737,0.577535078051,0.280575295095,0.330014966394,0.368575494406,0.286129512328,0.24188118994,0.318968567299])

    # Creating weights for histo: y16_TET_4
    y16_TET_4_weights = numpy.array([0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.297996585717,7.67096064184,19.8447794052,29.8227384969,36.989107361,41.4794114142,45.0242522263,46.8392209833,48.008007953,47.7601332447,46.9456018818,45.9389916698,45.0297837123,43.6613822459,42.1962198568,40.1561436673,38.5065823765,35.3332329611,31.4376037418,27.7105966641,24.4988314789,21.8685737858,19.4862990258,17.5580871209,15.6335789066,14.2834954774,12.9356847674,11.8016700017,10.7162802051,10.0323640628,9.02265541702,8.48081429155,7.90247337477,7.12683878045,6.51608656206,6.23764438079,5.53116137878,4.95211499711,4.5334496444,4.21378185874,3.81115500975,3.5260016929,3.13720075322,2.905272758,2.68425341445,2.37730684421,2.16318141577])

    # Creating weights for histo: y16_TET_5
    y16_TET_5_weights = numpy.array([0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0564662897096,1.46937832288,3.99815514,6.03042792247,7.75885953491,8.98324644713,9.77861522066,10.4223304752,10.789885408,10.8344644368,10.8675246159,10.9646206373,10.9394063994,10.659933258,10.4152207163,10.1646187176,9.97949691861,9.17284935472,8.27065415244,7.30722780162,6.55344131552,5.74312084296,5.21449406117,4.67906159565,4.18503537401,3.78899419377,3.55677794368,3.19659883569,2.95159502197,2.74139581887,2.54921787422])

    # Creating weights for histo: y16_TET_6
    y16_TET_6_weights = numpy.array([0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0168928224138,0.426860887054,1.11135313811,1.70409027325,2.24869055842,2.587502886,2.89869947873,3.13633575113,3.24877502746,3.33211506666,3.43290825028,3.45565161982,3.52234724327,3.42212986646,3.42314752503])

    # Creating weights for histo: y16_TET_7
    y16_TET_7_weights = numpy.array([0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0])

    # Creating weights for histo: y16_TET_8
    y16_TET_8_weights = numpy.array([0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0])

    # Creating weights for histo: y16_TET_9
    y16_TET_9_weights = numpy.array([0.0,0.0,0.0,0.0,31.2882195568,15934.2926776,62758.2715803,106606.820255,129265.972614,136368.043917,103658.387273,63471.1742054,37073.4512761,22377.2482051,13580.7450208,8536.15529839,5153.1554868,3286.86677675,1918.50094465,1243.53673625,844.442003449,570.713542855,453.552572221,362.386553758,234.545848064,187.703108364,156.393301777,101.624884445,91.190589378,67.7585490597,49.5226229559,49.5527309794,44.3052447094,31.3136671812,26.0553873963,10.4336836783,31.2684436226,10.4419239713,7.81433177742,26.0531033394,2.61035563887,2.60594671681,5.20611177026,10.4419816495,5.22749115858,0.0,5.21481733413,0.0,7.82569438398,7.82529063654,2.59804211095,2.61035563887,2.60865144014,2.60827114851,0.0,0.0,0.0,2.61074131381,0.0,0.0,0.0,5.2087841938,0.0,0.0,0.0,0.0,0.0,0.0,2.61034333418,0.0,0.0,2.60956621649,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0])

    # Creating weights for histo: y16_TET_10
    y16_TET_10_weights = numpy.array([0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,1757.90276114,35535.9598169,75843.4028001,98871.1584101,103096.681057,97820.6453542,87362.3017366,77640.198361,67865.0749147,52841.4261795,38773.5623332,28537.4028234,21130.2565432,15734.1061401,12169.1527822,9287.55426181,7329.38992249,5558.90816881,4389.78867598,3466.29947409,2516.25829789,1931.55965274,1386.1000923,1044.81820786,781.488139742,561.429836752,451.827577626,285.435128287,233.806699748,213.793931615,151.674685628,140.070177361,77.9490845205,101.109967449,61.0831999461,66.3426909245,61.0848159424,44.2345526661,46.3580488224,36.8629967817,27.397567493,22.120762268,29.4912254311,27.3784448695,23.1753230101,17.8973019402,12.6395116056,10.5324947644,6.3210620665,7.36990910717,10.5347917877,8.44036047999,5.26673218108,5.26351173121,7.37569206554,5.2671861991,5.2684097392,3.16003161343,3.16110779004,1.05396166911,4.21641535326,4.21012835794,8.42392733615,2.10948623755,2.10712534384,0.0,1.05085087614,0.0,1.05409941356,2.10773326627,2.11004683438])

    # Creating weights for histo: y16_TET_11
    y16_TET_11_weights = numpy.array([0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,205.022013768,5089.96771147,11604.7123353,15328.4060814,16695.1027004,16674.5540494,16253.9176303,15381.0725659,14527.88858,13376.4917199,12300.995767,11298.3921961,10343.2411008,9517.92535827,8811.39449717,7998.22812532,7268.27456853,6311.60576251,5256.03984947,4357.07863311,3617.16735681,3076.85387286,2589.17728771,2196.95587212,1860.37680687,1605.22811105,1415.40937099,1217.33658978,1056.84040585,919.300077474,809.179595431,705.294791347,642.423142789,568.712734015,474.266553941,424.027253911,379.796858956,339.506095329,305.441903397,261.228491433,227.338778604,205.694378847,181.286746505,148.344546267,135.214004379,116.312549832,85.2286807576,75.7942832835,53.4456273104,44.4532486867,34.323336242,29.2584818407,28.3302768355,22.5746488689,17.9669904257,16.1226337283,15.4355487765,14.0505320438,15.1995505166,9.67493733937,8.0607731779,8.05865222514,6.22081207826])

    # Creating weights for histo: y16_TET_12
    y16_TET_12_weights = numpy.array([0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,11.7129659984,314.214217271,792.018565046,1162.90981666,1388.47965983,1494.8179151,1557.69839905,1569.91309473,1544.89932155,1508.76690521,1458.3257904,1393.3109086,1338.55367817,1251.76893858,1194.32678339,1125.37896194,1062.62504917,947.142891946,797.780054261,677.304683332,577.032226707,492.442669912,430.929077731,372.60873401,334.430134936,298.04365293,266.445216218,235.793101032,219.947659189,206.406697618,196.887698711,183.954817392,177.804997033,162.850824025,152.662075079,141.031530385,130.919916762,123.421247756,111.953360489,103.926824273,98.7159773867,86.1752358886,81.8535034338,73.6574618655,70.3332949512,64.5205617218,59.1765265634])

    # Creating weights for histo: y16_TET_13
    y16_TET_13_weights = numpy.array([0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,1.89511634083,49.4627480368,133.838198876,206.803576856,257.843738688,292.559245802,314.475116759,323.625394756,326.020373281,329.108959238,324.259108004,320.01074731,310.459475618,302.627901305,291.902715723,277.850641787,268.697086904,246.320510118,208.809152153,180.054360459,154.764025627,133.434656494,116.726302756,102.948455591,89.6782222647,79.9106154471,69.5048655184,63.0822912901,56.6620594282,52.0843535356,46.5290556032])

    # Creating weights for histo: y16_TET_14
    y16_TET_14_weights = numpy.array([0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.432891839708,13.4046382671,35.2628502464,55.5827889701,70.4195349378,81.7679456229,90.1586564301,95.4020667738,97.2098898875,100.288475528,99.4345418856,99.241709472,97.8560631487,97.615061106,93.8049665509])

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
    plt.xlabel(r"TET",\
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
