def selection_4():

    # Library import
    import numpy
    import matplotlib
    import matplotlib.pyplot   as plt
    import matplotlib.gridspec as gridspec

    # Library version
    matplotlib_version = matplotlib.__version__
    numpy_version      = numpy.__version__

    # Histo binning
    xBinning = numpy.linspace(-8.0,8.0,161,endpoint=True)

    # Creating data sequence: middle of each bin
    xData = numpy.array([-7.95,-7.85,-7.75,-7.65,-7.55,-7.45,-7.35,-7.25,-7.15,-7.05,-6.95,-6.85,-6.75,-6.65,-6.55,-6.45,-6.35,-6.25,-6.15,-6.05,-5.95,-5.85,-5.75,-5.65,-5.55,-5.45,-5.35,-5.25,-5.15,-5.05,-4.95,-4.85,-4.75,-4.65,-4.55,-4.45,-4.35,-4.25,-4.15,-4.05,-3.95,-3.85,-3.75,-3.65,-3.55,-3.45,-3.35,-3.25,-3.15,-3.05,-2.95,-2.85,-2.75,-2.65,-2.55,-2.45,-2.35,-2.25,-2.15,-2.05,-1.95,-1.85,-1.75,-1.65,-1.55,-1.45,-1.35,-1.25,-1.15,-1.05,-0.95,-0.85,-0.75,-0.65,-0.55,-0.45,-0.35,-0.25,-0.15,-0.05,0.05,0.15,0.25,0.35,0.45,0.55,0.65,0.75,0.85,0.95,1.05,1.15,1.25,1.35,1.45,1.55,1.65,1.75,1.85,1.95,2.05,2.15,2.25,2.35,2.45,2.55,2.65,2.75,2.85,2.95,3.05,3.15,3.25,3.35,3.45,3.55,3.65,3.75,3.85,3.95,4.05,4.15,4.25,4.35,4.45,4.55,4.65,4.75,4.85,4.95,5.05,5.15,5.25,5.35,5.45,5.55,5.65,5.75,5.85,5.95,6.05,6.15,6.25,6.35,6.45,6.55,6.65,6.75,6.85,6.95,7.05,7.15,7.25,7.35,7.45,7.55,7.65,7.75,7.85,7.95])

    # Creating weights for histo: y5_ETA_0
    y5_ETA_0_weights = numpy.array([0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,406.56873994,406.56873994,406.56873994,1219.70661982,813.13747988,813.13747988,1219.70661982,1219.70661982,2845.98157958,1219.70661982,813.13747988,2032.8440997,3252.55031952,2845.98157958,1219.70661982,3252.55031952,3252.55031952,4472.25533934,813.13747988,2439.41283964,2845.98157958,4065.6873994,4878.82727928,6911.67097898,5285.39521922,6505.09903904,8944.51467868,10977.3583784,10164.2184985,11383.9263183,7724.80685886,9757.65055856,6911.67097898,6911.67097898,5691.96315916,7724.80685886,4472.25533934,6911.67097898,7318.23891892,5285.39521922,4472.25533934,6098.5310991,4878.82727928,2845.98157958,3659.11945946,1219.70661982,1626.27535976,3659.11945946,1626.27535976,1626.27535976,1219.70661982,1219.70661982,406.56873994,2845.98157958,3659.11945946,813.13747988,4472.25533934,5691.96315916,4878.82727928,6098.5310991,3659.11945946,6505.09903904,4472.25533934,6505.09903904,6098.5310991,7318.23891892,7318.23891892,7724.80685886,10570.7904384,10164.2184985,6911.67097898,7318.23891892,8944.51467868,6911.67097898,6911.67097898,10164.2184985,5691.96315916,4472.25533934,6098.5310991,3252.55031952,2439.41283964,3659.11945946,4472.25533934,2032.8440997,2439.41283964,813.13747988,2032.8440997,813.13747988,2032.8440997,1626.27535976,2032.8440997,1219.70661982,1626.27535976,1219.70661982,0.0,0.0,0.0,813.13747988,406.56873994,813.13747988,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0])

    # Creating weights for histo: y5_ETA_1
    y5_ETA_1_weights = numpy.array([0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,681.827329249,340.913744625,1704.56872312,340.913744625,681.827329249,0.0,1363.6550585,0.0,1022.74139387,2386.39645237,2386.39645237,2727.310117,681.827329249,2727.310117,1363.6550585,1363.6550585,2386.39645237,4431.88084012,3750.05151087,3750.05151087,4431.88084012,4772.79290474,3409.13744625,4090.9647755,6818.27329249,5795.53309862,7500.10142174,5454.62103399,4090.9647755,7841.01748637,9204.66974486,6818.27329249,8522.84561562,6136.44916324,8181.92955099,5113.70496937,4772.79290474,6818.27329249,4431.88084012,3409.13744625,2727.310117,4431.88084012,4090.9647755,3068.22378162,1363.6550585,2727.310117,681.827329249,1022.74139387,681.827329249,681.827329249,1704.56872312,340.913744625,2045.48238775,1704.56872312,1022.74139387,3409.13744625,2386.39645237,3750.05151087,3409.13744625,4431.88084012,5113.70496937,5454.62103399,5113.70496937,4772.79290474,6477.36122787,6136.44916324,5113.70496937,9545.58580949,7841.01748637,9545.58580949,4090.9647755,6477.36122787,8863.75768024,5113.70496937,5454.62103399,5454.62103399,5113.70496937,4772.79290474,3750.05151087,4090.9647755,2727.310117,3409.13744625,3409.13744625,2386.39645237,1704.56872312,1022.74139387,1704.56872312,340.913744625,1022.74139387,681.827329249,1363.6550585,340.913744625,1022.74139387,1022.74139387,681.827329249,340.913744625,681.827329249,1022.74139387,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0])

    # Creating weights for histo: y5_ETA_2
    y5_ETA_2_weights = numpy.array([0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,234.571527696,234.571527696,184.813943033,184.813943033,220.355052078,312.762023595,334.086697022,355.411410449,341.194934831,447.818261966,348.30317264,490.46784882,554.4418291,689.498187471,710.822980898,845.878939269,774.796961179,746.363769943,774.796961179,717.930978707,952.502506403,980.935297639,1009.36848888,938.286110785,1009.36848888,1201.29042972,1208.39882753,1251.04801438,1322.13039247,1130.20805163,1343.4551859,1243.94001657,1179.96563629,1073.34246916,1123.10005382,988.043695448,867.203732696,789.013356797,881.420128314,767.68856337,675.281791853,597.091015954,575.766622527,398.060757303,270.112676741,369.627846067,298.545587977,383.844321685,298.545587977,312.762023595,270.112676741,248.787963314,298.545587977,298.545587977,326.978499213,405.169075112,454.926659775,518.900640056,611.307411572,739.255772134,632.632204999,767.68856337,1009.36848888,810.338150224,924.069715167,916.961317359,1208.39882753,1279.48120562,1279.48120562,1222.61522314,1165.74924067,1329.23879028,1208.39882753,1165.74924067,1265.26441,1272.37280781,1023.58488449,1229.72362095,1123.10005382,1087.55886477,874.312130505,924.069715167,838.77094146,746.363769943,689.498187471,604.199413763,653.956998426,582.874620336,419.38547073,533.117035674,483.359451011,462.034657584,284.329112359,447.818261966,326.978499213,341.194934831,213.246854269,248.787963314,227.463289887,135.056318371,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0])

    # Creating weights for histo: y5_ETA_3
    y5_ETA_3_weights = numpy.array([0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,22.8916845218,36.4836255816,25.753145587,33.6221645164,39.3450866469,40.7758151795,43.6372962447,55.7985007719,56.5138610382,60.0906623698,72.9672671633,77.2594287611,75.8287082285,64.3828639676,84.4131114242,80.1209098263,90.8513938209,98.7203967503,85.1284716905,105.158679147,110.166241011,129.481088201,110.881601278,120.18136474,125.90428687,110.166241011,110.881601278,113.027682076,116.604523408,105.158679147,115.173802875,94.4281951525,86.5591922231,92.2821143536,82.2669906253,70.8211463644,70.105786098,62.952143435,70.105786098,44.352656511,53.652379973,45.0680167773,52.2216594404,40.0604549132,38.6297223806,35.052893049,37.1989898479,25.753145587,15.0226695924,17.8841306577,22.8916845218,27.1838781197,22.1763202555,32.9068002501,42.9218959784,45.7833770436,37.9143541143,48.6448181088,42.9218959784,58.6599418371,50.7909389078,59.3753021034,70.8211463644,68.6750655654,77.9747890274,95.8589556851,83.6977111579,104.443318881,99.4357570166,111.596961544,102.297238082,113.743082343,127.335007403,106.58939968,125.188926604,118.750604207,98.005036484,125.188926604,102.297238082,105.874039413,100.866477549,104.443318881,76.5440684948,90.1360335546,95.1435554188,82.9823508916,72.9672671633,70.8211463644,68.6750655654,82.9823508916,67.2443450328,58.6599418371,52.2216594404,50.7909389078,39.3450866469,44.352656511,33.6221645164,27.1838781197,30.0453391849,22.1763202555,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0])

    # Creating a new Canvas
    fig   = plt.figure(figsize=(12,6),dpi=80)
    frame = gridspec.GridSpec(1,1,right=0.7)
    pad   = fig.add_subplot(frame[0])

    # Creating a new Stack
    pad.hist(x=xData, bins=xBinning, weights=y5_ETA_0_weights+y5_ETA_1_weights+y5_ETA_2_weights+y5_ETA_3_weights,\
             label="$signal100GeV4TeV$", histtype="stepfilled", rwidth=1.0,\
             color="#0000ff", edgecolor="#0000ff", linewidth=1, linestyle="solid",\
             bottom=None, cumulative=False, normed=False, align="mid", orientation="vertical")

    pad.hist(x=xData, bins=xBinning, weights=y5_ETA_0_weights+y5_ETA_1_weights+y5_ETA_2_weights,\
             label="$signal100GeV1p5TeV$", histtype="stepfilled", rwidth=1.0,\
             color="#59d354", edgecolor="#59d354", linewidth=1, linestyle="solid",\
             bottom=None, cumulative=False, normed=False, align="mid", orientation="vertical")

    pad.hist(x=xData, bins=xBinning, weights=y5_ETA_0_weights+y5_ETA_1_weights,\
             label="$signal100GeV1TeV$", histtype="stepfilled", rwidth=1.0,\
             color="#ce5e60", edgecolor="#ce5e60", linewidth=1, linestyle="solid",\
             bottom=None, cumulative=False, normed=False, align="mid", orientation="vertical")

    pad.hist(x=xData, bins=xBinning, weights=y5_ETA_0_weights,\
             label="$signal1MeV$", histtype="stepfilled", rwidth=1.0,\
             color="#5954d8", edgecolor="#5954d8", linewidth=1, linestyle="solid",\
             bottom=None, cumulative=False, normed=False, align="mid", orientation="vertical")


    # Axis
    plt.rc('text',usetex=False)
    plt.xlabel(r"\eta [ j_{2} ] ",\
               fontsize=16,color="black")
    plt.ylabel(r"$\mathrm{Events}$ $(\mathcal{L}_{\mathrm{int}} = 40.0\ \mathrm{fb}^{-1})$ ",\
               fontsize=16,color="black")

    # Boundary of y-axis
    ymax=(y5_ETA_0_weights+y5_ETA_1_weights+y5_ETA_2_weights+y5_ETA_3_weights).max()*1.1
    ymin=0 # linear scale
    #ymin=min([x for x in (y5_ETA_0_weights+y5_ETA_1_weights+y5_ETA_2_weights+y5_ETA_3_weights) if x])/100. # log scale
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
    plt.savefig('../../HTML/MadAnalysis5job_0/selection_4.png')
    plt.savefig('../../PDF/MadAnalysis5job_0/selection_4.png')
    plt.savefig('../../DVI/MadAnalysis5job_0/selection_4.eps')

# Running!
if __name__ == '__main__':
    selection_4()
