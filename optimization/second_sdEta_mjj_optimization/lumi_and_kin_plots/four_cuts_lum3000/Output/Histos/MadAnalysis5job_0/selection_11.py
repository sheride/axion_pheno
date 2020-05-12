def selection_11():

    # Library import
    import numpy
    import matplotlib
    import matplotlib.pyplot   as plt
    import matplotlib.gridspec as gridspec

    # Library version
    matplotlib_version = matplotlib.__version__
    numpy_version      = numpy.__version__

    # Histo binning
    xBinning = numpy.linspace(0.0,2000.0,81,endpoint=True)

    # Creating data sequence: middle of each bin
    xData = numpy.array([12.5,37.5,62.5,87.5,112.5,137.5,162.5,187.5,212.5,237.5,262.5,287.5,312.5,337.5,362.5,387.5,412.5,437.5,462.5,487.5,512.5,537.5,562.5,587.5,612.5,637.5,662.5,687.5,712.5,737.5,762.5,787.5,812.5,837.5,862.5,887.5,912.5,937.5,962.5,987.5,1012.5,1037.5,1062.5,1087.5,1112.5,1137.5,1162.5,1187.5,1212.5,1237.5,1262.5,1287.5,1312.5,1337.5,1362.5,1387.5,1412.5,1437.5,1462.5,1487.5,1512.5,1537.5,1562.5,1587.5,1612.5,1637.5,1662.5,1687.5,1712.5,1737.5,1762.5,1787.5,1812.5,1837.5,1862.5,1887.5,1912.5,1937.5,1962.5,1987.5])

    # Creating weights for histo: y12_PT_0
    y12_PT_0_weights = numpy.array([0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,1931.38426405,2085.21933374,2233.52750812,2358.806502,2356.04290435,2327.48682853,2338.23371943,2306.60684622,2225.85111462,2226.77241384,2092.5888275,2014.28919382,1943.66625364,1850.32133271,1758.81841022,1685.12497264,1529.4473045,1491.06533701,1402.63321192,1307.75289229,1212.25817317,1154.22472233,1085.13688085,1018.81293703,958.629688005,905.509033001,850.238879816,762.727753942,725.573985412,681.051023125,632.843163959,603.058589187,523.83795629,501.115975536,478.086795043,446.766821572,412.069450962,381.671076711,345.438307401,334.077317024,284.334149159,264.068416324,270.209531123,240.118026611,233.362782333,219.238194297,183.312624727,172.565643831,163.661021373,149.229353597,146.158796198,143.395288539,123.436635445,120.059028306,98.2580167718,94.266280153,89.9674937942,80.448741857,76.764084978,67.5523827806,69.70179096,56.4983521438,54.6560237043,53.1207450048,52.199565785,48.2078291662,42.6808138478,34.3902908702])

    # Creating weights for histo: y12_PT_1
    y12_PT_1_weights = numpy.array([0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,1.82209320175,0.913150150035,0.0,0.0,0.0,0.0,0.909853848219,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0])

    # Creating weights for histo: y12_PT_2
    y12_PT_2_weights = numpy.array([0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,25.6071619516,25.5916823092,6.77739959352,6.02014912525,6.77619717085,4.51963719884,2.26322907918,3.00974358649,0.752556991122,2.26069128556,0.0,1.50836331258,1.50669758529,0.0,0.0,0.755225253798,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0])

    # Creating weights for histo: y12_PT_3
    y12_PT_3_weights = numpy.array([0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,103.533069256,81.6744040304,62.7090756943,49.5093363623,37.130471188,34.2412781271,26.0030727105,15.2600630836,11.5417295364,7.01339024078,4.95260335539,3.71163638893,3.29917919367,3.71392768237,2.06154435288,1.23810833414,1.65273403145,0.82439671665,0.412778037284,0.0,0.0,0.410940736824,0.412810944158,0.41208211784,0.0,0.411355729067,0.412198510672,0.0,0.411604663475,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.413566278792,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0])

    # Creating weights for histo: y12_PT_4
    y12_PT_4_weights = numpy.array([0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,41.1529785933,36.7072042747,37.8911728435,34.2705750748,32.1245568884,28.5711360486,25.460816588,20.20651415,18.0595429928,13.0989780341,11.6193961065,7.99309855009,7.10635166631,4.36579391094,3.18201774004,2.14737819903,2.29482743922,1.55416888113,0.814230913292,0.814839371647,0.444146039701,0.814082105543,0.296127031164,0.147906125082,0.222036855058,0.148048920398,0.222250356601,0.0,0.0740744535904,0.0,0.0738164600332,0.221813613371,0.148202628282,0.0737931618502,0.0,0.0,0.0,0.0739071576051,0.0,0.0,0.0,0.148127412728,0.0,0.0737931618502,0.0,0.0,0.0,0.0,0.0,0.0,0.074009579424,0.0,0.0,0.0,0.0739717912742,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0])

    # Creating weights for histo: y12_PT_5
    y12_PT_5_weights = numpy.array([0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,8.52580574432,8.11109240478,7.63806370604,7.7704818533,7.9593158269,7.63746953936,7.33546781881,7.37264224736,7.08921573772,6.67399825676,6.90041777422,6.10764337722,5.48258903072,4.89645560271,4.34780869079,4.42367897468,3.34643077424,2.89299397161,2.19327327896,1.62609016708,0.964159675717,0.982951547401,0.623948536285,0.435000230616,0.283671828459,0.226943494459,0.397082193469,0.056704387282,0.132355909804,0.113438212822,0.0757070380957,0.0945865343608,0.0378257012441,0.0189098107693,0.0377892710243,0.0189268825584,0.0188828211979,0.0,0.0188710999097,0.0,0.0188710999097,0.0189061767498,0.0,0.0,0.0189064648306,0.0189013393928,0.0189139939428,0.0,0.0,0.0,0.0,0.0,0.0,0.0188968621368,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0])

    # Creating weights for histo: y12_PT_6
    y12_PT_6_weights = numpy.array([0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,1.91229757227,1.69728154889,1.48105987444,1.56781126819,1.65334351476,1.78147243366,1.58845654335,2.01742389822,1.86833554508,1.45849740413,1.99708228518,1.52539529357,1.71853264873,1.65313807422,1.5253892953,1.97539031294,1.56769955052,1.76142998404,1.4391612501,1.65326478755,1.54665689036,1.39605997381,1.48196786167,0.902018951556,1.18011271994,1.20212709887,0.902648019501,0.644203364576,0.772295993978,0.644319056094,0.579697057998,0.364705402575,0.30033533157,0.407736124286,0.171615283746,0.0643432137773,0.0641211280499,0.0643780786872,0.0213405339511,0.0214637832822,0.0,0.0646744004303,0.0,0.0,0.0,0.0643388350445,0.0,0.0,0.0214637832822,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0])

    # Creating weights for histo: y12_PT_7
    y12_PT_7_weights = numpy.array([0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.124734094117,0.126350838687,0.10044090077,0.114997008231,0.0777346543049,0.1004302767,0.0906168420977,0.0921972196588,0.0647943798809,0.0874754491858,0.0826461178621,0.0890964685295,0.0793849055572,0.0631880079236,0.0809865941227,0.0761336258148,0.0647850759616,0.0599657400647,0.0777816139516,0.0631691800599,0.0647866475696,0.0955888125624,0.0632234319677,0.0808842510104,0.0777429209629,0.0729144383075,0.074509840441,0.0809707837463,0.0729224849404,0.0745418069475,0.0955541428902,0.11005244661,0.0988598317012,0.108553541207,0.0988105775068,0.127587851335,0.110174089068,0.106906527467,0.126348292682,0.0856424513566,0.0939602495004,0.0907409048323,0.0648074242272,0.0695478654031,0.059939054161,0.0388664627681,0.0340208181534,0.0259313212157,0.02256112104,0.0178309770397,0.0194264703265,0.00648697542,0.006482725792,0.00971865406758,0.0016187065654,0.0,0.0,0.00324153262966,0.00161950462794,0.0,0.0,0.0,0.00162563892824,0.00162165615927,0.0,0.0,0.0,0.0])

    # Creating weights for histo: y12_PT_8
    y12_PT_8_weights = numpy.array([0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.00853025409229,0.00638507861764,0.00425990853797,0.0,0.00639260792489,0.00636562781444,0.0021193000932,0.0,0.00426347329356,0.00852161114693,0.00852190848831,0.00848402697441,0.00637674080912,0.0,0.00639408126811,0.0106457589068,0.00852241296637,0.00426200106398,0.00212624028589,0.00212624028589,0.00426130504016,0.00425118541067,0.0,0.00212624028589,0.0,0.00425387596034,0.00213060686092,0.0,0.00426427511299,0.0,0.00425387596034,0.00424842581543,0.0084927322835,0.00213219490886,0.00426200106398,0.00639111008164,0.00212763678808,0.00848976109703,0.00638588043708,0.00852786422491,0.00638963673842,0.00212763678808,0.00852933756813,0.0147451921934,0.00426200106398,0.00212980504148,0.0105424455859,0.00850546673527,0.00426280288341,0.00852933756813,0.021281546298,0.0127667695482,0.0106525164629,0.00639101987695,0.00425843519475,0.00849667122149,0.0106227177344,0.0127874720806,0.01278996663,0.0106346759804,0.00213366825208,0.0105349630514,0.0106488737526,0.0,0.00425983169694,0.00417597697465,0.0085106340161,0.00635043556336])

    # Creating weights for histo: y12_PT_9
    y12_PT_9_weights = numpy.array([0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0])

    # Creating weights for histo: y12_PT_10
    y12_PT_10_weights = numpy.array([0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,78.9085275503,158.069001296,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0])

    # Creating weights for histo: y12_PT_11
    y12_PT_11_weights = numpy.array([0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,241.913777125,138.268533357,328.279611544,224.520988926,207.29446473,103.653255796,34.5104006841,34.5336298028,51.725713805,0.0,17.259641542,17.2770143866,17.3004884774,0.0,0.0,0.0,0.0,0.0,0.0,0.0,17.3004884774,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0])

    # Creating weights for histo: y12_PT_12
    y12_PT_12_weights = numpy.array([0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,85.1353937442,62.3017670102,74.7660614129,80.9865817969,68.567813741,56.0708026861,66.4661583158,66.4643984253,64.3732157909,51.9321173216,54.0015177052,60.2386272206,37.3598780491,22.8506774761,14.526987007,6.22425077476,6.22713295604,16.6220615959,8.2980335741,4.16253909298,2.07286130915,2.07440135757,0.0,0.0,2.07522129342,2.07947965133,0.0,2.07980306727,2.07697050914,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0])

    # Creating weights for histo: y12_PT_13
    y12_PT_13_weights = numpy.array([0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,6.04973364322,14.3673066407,9.06533103798,8.31831491578,7.56112586502,9.07886763284,9.82972534417,7.56162654607,11.3336528667,12.8588229206,14.3774067429,14.3686630312,16.632009911,16.6233754387,24.9575300822,13.6088294742,15.1192567471,15.8819168762,10.5878702406,7.56224101826,5.29123371845,3.02692280005,3.78241499722,3.02379672966,2.27028859493,0.753221836202,4.54011201166,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.756042491156,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.757313765851,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0])

    # Creating weights for histo: y12_PT_14
    y12_PT_14_weights = numpy.array([0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,4.24235068678,2.75998963795,2.76012814597,2.12213941694,2.33318784248,2.1226700758,1.27259843943,1.48402054807,1.06102945457,1.90903270447,2.54596502127,2.33503807881,2.54440882593,2.33395858191,2.97237928284,2.3335225702,1.69844048973,3.3924337177,4.03150107796,5.09314198775,4.03260048539,4.24325964567,5.93962799767,7.85646938049,6.57871555702,5.09285342936,3.81871524241,2.54575379654,3.18326351866,3.39281750035,2.96994096452,1.2726472058,0.636260841451,2.1211655324,1.27390589745,0.849298588466,1.06036057625,1.27347825393,0.21225910108,0.0,0.212323363032,0.424021535476,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0])

    # Creating weights for histo: y12_PT_15
    y12_PT_15_weights = numpy.array([0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.457565633023,0.230222363342,0.0,0.230050397772,0.0,0.0,0.0,0.113795556421,0.114337247966,0.113449054663,0.0,0.113137211944,0.0,0.229143944208,0.0,0.228646928255,0.115222161513,0.0,0.114122202362,0.0,0.113449054663,0.0,0.0,0.0,0.229511542773,0.114483330058,0.113137211944,0.115905768973,0.0,0.114195509334,0.114071233185,0.0,0.0,0.228193524189,0.114122202362,0.228033613937,0.343346722189,0.456987864166,0.113449054663,0.34054519032,0.685783533775,0.228283407224,0.34086837922,0.114071233185,0.342255006749,0.113137211944,0.0,0.115000201829,0.115000201829,0.229369804142,0.113137211944,0.115366116196,0.114864845425,0.0,0.11333674519,0.115366116196,0.0,0.0,0.0,0.0,0.0,0.227786302629,0.0,0.0,0.0,0.0,0.0,0.0])

    # Creating weights for histo: y12_PT_16
    y12_PT_16_weights = numpy.array([0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0135414772501,0.0135377525267,0.0,0.0,0.013500271415,0.0135469603894,0.0,0.0,0.0135469603894,0.0,0.0,0.0,0.0135469603894,0.0,0.0,0.0,0.0135550739341,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0135727678138,0.0,0.01349990183,0.0135301529361,0.0,0.0271068071666,0.0135115928416,0.0135410354805,0.0135400364462,0.0271442594045,0.0405817851112,0.094851813123,0.0135492847322,0.027030424351,0.0541477473646,0.0,0.027083300986,0.0,0.0270985550275,0.0,0.0135152251687,0.0135727678138,0.0540863616135,0.0,0.0,0.0])

    # Creating a new Canvas
    fig   = plt.figure(figsize=(12,6),dpi=80)
    frame = gridspec.GridSpec(1,1,right=0.7)
    pad   = fig.add_subplot(frame[0])

    # Creating a new Stack
    pad.hist(x=xData, bins=xBinning, weights=y12_PT_0_weights+y12_PT_1_weights+y12_PT_2_weights+y12_PT_3_weights+y12_PT_4_weights+y12_PT_5_weights+y12_PT_6_weights+y12_PT_7_weights+y12_PT_8_weights+y12_PT_9_weights+y12_PT_10_weights+y12_PT_11_weights+y12_PT_12_weights+y12_PT_13_weights+y12_PT_14_weights+y12_PT_15_weights+y12_PT_16_weights,\
             label="$bg\_dip\_1600\_inf$", histtype="step", rwidth=1.0,\
             color=None, edgecolor="#e5e5e5", linewidth=1, linestyle="solid",\
             bottom=None, cumulative=False, normed=False, align="mid", orientation="vertical")

    pad.hist(x=xData, bins=xBinning, weights=y12_PT_0_weights+y12_PT_1_weights+y12_PT_2_weights+y12_PT_3_weights+y12_PT_4_weights+y12_PT_5_weights+y12_PT_6_weights+y12_PT_7_weights+y12_PT_8_weights+y12_PT_9_weights+y12_PT_10_weights+y12_PT_11_weights+y12_PT_12_weights+y12_PT_13_weights+y12_PT_14_weights+y12_PT_15_weights,\
             label="$bg\_dip\_1200\_1600$", histtype="step", rwidth=1.0,\
             color=None, edgecolor="#f2f2f2", linewidth=1, linestyle="solid",\
             bottom=None, cumulative=False, normed=False, align="mid", orientation="vertical")

    pad.hist(x=xData, bins=xBinning, weights=y12_PT_0_weights+y12_PT_1_weights+y12_PT_2_weights+y12_PT_3_weights+y12_PT_4_weights+y12_PT_5_weights+y12_PT_6_weights+y12_PT_7_weights+y12_PT_8_weights+y12_PT_9_weights+y12_PT_10_weights+y12_PT_11_weights+y12_PT_12_weights+y12_PT_13_weights+y12_PT_14_weights,\
             label="$bg\_dip\_800\_1200$", histtype="step", rwidth=1.0,\
             color=None, edgecolor="#ccc6aa", linewidth=1, linestyle="solid",\
             bottom=None, cumulative=False, normed=False, align="mid", orientation="vertical")

    pad.hist(x=xData, bins=xBinning, weights=y12_PT_0_weights+y12_PT_1_weights+y12_PT_2_weights+y12_PT_3_weights+y12_PT_4_weights+y12_PT_5_weights+y12_PT_6_weights+y12_PT_7_weights+y12_PT_8_weights+y12_PT_9_weights+y12_PT_10_weights+y12_PT_11_weights+y12_PT_12_weights+y12_PT_13_weights,\
             label="$bg\_dip\_600\_800$", histtype="step", rwidth=1.0,\
             color=None, edgecolor="#ccc6aa", linewidth=1, linestyle="solid",\
             bottom=None, cumulative=False, normed=False, align="mid", orientation="vertical")

    pad.hist(x=xData, bins=xBinning, weights=y12_PT_0_weights+y12_PT_1_weights+y12_PT_2_weights+y12_PT_3_weights+y12_PT_4_weights+y12_PT_5_weights+y12_PT_6_weights+y12_PT_7_weights+y12_PT_8_weights+y12_PT_9_weights+y12_PT_10_weights+y12_PT_11_weights+y12_PT_12_weights,\
             label="$bg\_dip\_400\_600$", histtype="step", rwidth=1.0,\
             color=None, edgecolor="#c1bfa8", linewidth=1, linestyle="solid",\
             bottom=None, cumulative=False, normed=False, align="mid", orientation="vertical")

    pad.hist(x=xData, bins=xBinning, weights=y12_PT_0_weights+y12_PT_1_weights+y12_PT_2_weights+y12_PT_3_weights+y12_PT_4_weights+y12_PT_5_weights+y12_PT_6_weights+y12_PT_7_weights+y12_PT_8_weights+y12_PT_9_weights+y12_PT_10_weights+y12_PT_11_weights,\
             label="$bg\_dip\_200\_400$", histtype="step", rwidth=1.0,\
             color=None, edgecolor="#bab5a3", linewidth=1, linestyle="solid",\
             bottom=None, cumulative=False, normed=False, align="mid", orientation="vertical")

    pad.hist(x=xData, bins=xBinning, weights=y12_PT_0_weights+y12_PT_1_weights+y12_PT_2_weights+y12_PT_3_weights+y12_PT_4_weights+y12_PT_5_weights+y12_PT_6_weights+y12_PT_7_weights+y12_PT_8_weights+y12_PT_9_weights+y12_PT_10_weights,\
             label="$bg\_dip\_100\_200$", histtype="step", rwidth=1.0,\
             color=None, edgecolor="#b2a596", linewidth=1, linestyle="solid",\
             bottom=None, cumulative=False, normed=False, align="mid", orientation="vertical")

    pad.hist(x=xData, bins=xBinning, weights=y12_PT_0_weights+y12_PT_1_weights+y12_PT_2_weights+y12_PT_3_weights+y12_PT_4_weights+y12_PT_5_weights+y12_PT_6_weights+y12_PT_7_weights+y12_PT_8_weights+y12_PT_9_weights,\
             label="$bg\_dip\_0\_100$", histtype="step", rwidth=1.0,\
             color=None, edgecolor="#b7a39b", linewidth=1, linestyle="solid",\
             bottom=None, cumulative=False, normed=False, align="mid", orientation="vertical")

    pad.hist(x=xData, bins=xBinning, weights=y12_PT_0_weights+y12_PT_1_weights+y12_PT_2_weights+y12_PT_3_weights+y12_PT_4_weights+y12_PT_5_weights+y12_PT_6_weights+y12_PT_7_weights+y12_PT_8_weights,\
             label="$bg\_vbf\_1600\_inf$", histtype="step", rwidth=1.0,\
             color=None, edgecolor="#ad998c", linewidth=1, linestyle="solid",\
             bottom=None, cumulative=False, normed=False, align="mid", orientation="vertical")

    pad.hist(x=xData, bins=xBinning, weights=y12_PT_0_weights+y12_PT_1_weights+y12_PT_2_weights+y12_PT_3_weights+y12_PT_4_weights+y12_PT_5_weights+y12_PT_6_weights+y12_PT_7_weights,\
             label="$bg\_vbf\_1200\_1600$", histtype="step", rwidth=1.0,\
             color=None, edgecolor="#9b8e82", linewidth=1, linestyle="solid",\
             bottom=None, cumulative=False, normed=False, align="mid", orientation="vertical")

    pad.hist(x=xData, bins=xBinning, weights=y12_PT_0_weights+y12_PT_1_weights+y12_PT_2_weights+y12_PT_3_weights+y12_PT_4_weights+y12_PT_5_weights+y12_PT_6_weights,\
             label="$bg\_vbf\_800\_1200$", histtype="step", rwidth=1.0,\
             color=None, edgecolor="#876656", linewidth=1, linestyle="solid",\
             bottom=None, cumulative=False, normed=False, align="mid", orientation="vertical")

    pad.hist(x=xData, bins=xBinning, weights=y12_PT_0_weights+y12_PT_1_weights+y12_PT_2_weights+y12_PT_3_weights+y12_PT_4_weights+y12_PT_5_weights,\
             label="$bg\_vbf\_600\_800$", histtype="step", rwidth=1.0,\
             color=None, edgecolor="#afcec6", linewidth=1, linestyle="solid",\
             bottom=None, cumulative=False, normed=False, align="mid", orientation="vertical")

    pad.hist(x=xData, bins=xBinning, weights=y12_PT_0_weights+y12_PT_1_weights+y12_PT_2_weights+y12_PT_3_weights+y12_PT_4_weights,\
             label="$bg\_vbf\_400\_600$", histtype="step", rwidth=1.0,\
             color=None, edgecolor="#84c1a3", linewidth=1, linestyle="solid",\
             bottom=None, cumulative=False, normed=False, align="mid", orientation="vertical")

    pad.hist(x=xData, bins=xBinning, weights=y12_PT_0_weights+y12_PT_1_weights+y12_PT_2_weights+y12_PT_3_weights,\
             label="$bg\_vbf\_200\_400$", histtype="step", rwidth=1.0,\
             color=None, edgecolor="#89a8a0", linewidth=1, linestyle="solid",\
             bottom=None, cumulative=False, normed=False, align="mid", orientation="vertical")

    pad.hist(x=xData, bins=xBinning, weights=y12_PT_0_weights+y12_PT_1_weights+y12_PT_2_weights,\
             label="$bg\_vbf\_100\_200$", histtype="step", rwidth=1.0,\
             color=None, edgecolor="#829e8c", linewidth=1, linestyle="solid",\
             bottom=None, cumulative=False, normed=False, align="mid", orientation="vertical")

    pad.hist(x=xData, bins=xBinning, weights=y12_PT_0_weights+y12_PT_1_weights,\
             label="$bg\_vbf\_0\_100$", histtype="step", rwidth=1.0,\
             color=None, edgecolor="#adbcc6", linewidth=1, linestyle="solid",\
             bottom=None, cumulative=False, normed=False, align="mid", orientation="vertical")

    pad.hist(x=xData, bins=xBinning, weights=y12_PT_0_weights,\
             label="$signal$", histtype="step", rwidth=1.0,\
             color=None, edgecolor="#7a8e99", linewidth=1, linestyle="solid",\
             bottom=None, cumulative=False, normed=False, align="mid", orientation="vertical")


    # Axis
    plt.rc('text',usetex=False)
    plt.xlabel(r"p_{T} [ a_{1} ] ",\
               fontsize=16,color="black")
    plt.ylabel(r"$\mathrm{Events}$ $(\mathcal{L}_{\mathrm{int}} = 3000.0\ \mathrm{fb}^{-1})$ ",\
               fontsize=16,color="black")

    # Boundary of y-axis
    ymax=(y12_PT_0_weights+y12_PT_1_weights+y12_PT_2_weights+y12_PT_3_weights+y12_PT_4_weights+y12_PT_5_weights+y12_PT_6_weights+y12_PT_7_weights+y12_PT_8_weights+y12_PT_9_weights+y12_PT_10_weights+y12_PT_11_weights+y12_PT_12_weights+y12_PT_13_weights+y12_PT_14_weights+y12_PT_15_weights+y12_PT_16_weights).max()*1.1
    ymin=0 # linear scale
    #ymin=min([x for x in (y12_PT_0_weights+y12_PT_1_weights+y12_PT_2_weights+y12_PT_3_weights+y12_PT_4_weights+y12_PT_5_weights+y12_PT_6_weights+y12_PT_7_weights+y12_PT_8_weights+y12_PT_9_weights+y12_PT_10_weights+y12_PT_11_weights+y12_PT_12_weights+y12_PT_13_weights+y12_PT_14_weights+y12_PT_15_weights+y12_PT_16_weights) if x])/100. # log scale
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
    plt.savefig('../../HTML/MadAnalysis5job_0/selection_11.png')
    plt.savefig('../../PDF/MadAnalysis5job_0/selection_11.png')
    plt.savefig('../../DVI/MadAnalysis5job_0/selection_11.eps')

# Running!
if __name__ == '__main__':
    selection_11()
