def selection_5():

    # Library import
    import numpy
    import matplotlib
    import matplotlib.pyplot   as plt
    import matplotlib.gridspec as gridspec

    # Library version
    matplotlib_version = matplotlib.__version__
    numpy_version      = numpy.__version__

    # Histo binning
    xBinning = numpy.linspace(-3.2,3.2,65,endpoint=True)

    # Creating data sequence: middle of each bin
    xData = numpy.array([-3.15,-3.05,-2.95,-2.85,-2.75,-2.65,-2.55,-2.45,-2.35,-2.25,-2.15,-2.05,-1.95,-1.85,-1.75,-1.65,-1.55,-1.45,-1.35,-1.25,-1.15,-1.05,-0.95,-0.85,-0.75,-0.65,-0.55,-0.45,-0.35,-0.25,-0.15,-0.05,0.05,0.15,0.25,0.35,0.45,0.55,0.65,0.75,0.85,0.95,1.05,1.15,1.25,1.35,1.45,1.55,1.65,1.75,1.85,1.95,2.05,2.15,2.25,2.35,2.45,2.55,2.65,2.75,2.85,2.95,3.05,3.15])

    # Creating weights for histo: y6_PHI_0
    y6_PHI_0_weights = numpy.array([2032.8441017,6505.09904545,7724.80686647,4472.25534374,6098.53110511,6505.09904545,6098.53110511,6911.67098579,5285.39522442,7318.23892613,5285.39522442,5285.39522442,6911.67098579,7318.23892613,6911.67098579,5691.96316476,8537.94674715,7318.23892613,5691.96316476,4472.25534374,4878.82728408,4472.25534374,6505.09904545,9757.65056817,6505.09904545,6911.67098579,6505.09904545,5285.39522442,8537.94674715,7318.23892613,8131.37480681,5285.39522442,5285.39522442,5691.96316476,8537.94674715,6098.53110511,7318.23892613,5691.96316476,4878.82728408,6911.67098579,6505.09904545,9351.08262783,7318.23892613,6911.67098579,4472.25534374,3659.11946306,4472.25534374,6098.53110511,10164.2185085,4065.6874034,5285.39522442,9351.08262783,9757.65056817,8537.94674715,4472.25534374,8131.37480681,5691.96316476,3252.55032272,5691.96316476,4878.82728408,7318.23892613,6505.09904545,9757.65056817,1626.27536136])

    # Creating weights for histo: y6_PHI_1
    y6_PHI_1_weights = numpy.array([3409.13752713,4772.79301798,5795.53323612,8181.92974511,5454.6211634,5113.70509069,5113.70509069,6818.27345425,4772.79301798,3750.05159984,4090.96487255,5795.53323612,3750.05159984,5454.6211634,5795.53323612,6477.36138154,3068.22385441,5454.6211634,3750.05159984,4772.79301798,4431.88094527,4090.96487255,4772.79301798,6136.44930883,7159.18952697,5454.6211634,4090.96487255,5113.70509069,6136.44930883,6477.36138154,9545.58603596,5795.53323612,1704.56876356,5113.70509069,5454.6211634,6477.36138154,5795.53323612,4431.88094527,6136.44930883,6818.27345425,4090.96487255,6136.44930883,3068.22385441,5113.70509069,6818.27345425,4772.79301798,7500.10159968,7841.01767239,8181.92974511,5113.70509069,6136.44930883,3750.05159984,7159.18952697,5454.6211634,5113.70509069,5113.70509069,6136.44930883,6818.27345425,3068.22385441,5113.70509069,1704.56876356,5113.70509069,5454.6211634,3068.22385441])

    # Creating weights for histo: y6_PHI_2
    y6_PHI_2_weights = numpy.array([497.575847189,1208.39882889,1151.53284635,1059.12607473,1265.26441142,1115.99165727,1130.2080529,1023.58488565,1059.12607473,1073.34247036,1187.07403544,1243.94001797,1094.66726382,1123.10005508,1222.61522452,1251.04801579,1030.69288346,1108.88365945,1009.36849001,1172.8576398,1400.32076995,1144.42484853,1030.69288346,1201.29043107,1137.31645072,1094.66726382,1300.80560051,945.394509659,1144.42484853,1087.558866,1052.01767691,1094.66726382,1009.36849001,1101.77526163,1158.64124417,1251.04801579,959.610905292,1158.64124417,1044.9096791,1187.07403544,1222.61522452,1087.558866,1066.23407255,1300.80560051,1194.18243325,1208.39882889,1059.12607473,1201.29043107,1151.53284635,1059.12607473,1151.53284635,1208.39882889,1052.01767691,1201.29043107,1030.69288346,1208.39882889,966.71890311,1094.66726382,980.935298744,1172.8576398,1044.9096791,1187.07403544,1137.31645072,554.441829725])

    # Creating weights for histo: y6_PHI_3
    y6_PHI_3_weights = numpy.array([50.7909381409,118.750602414,136.634768802,125.188924713,130.911846758,101.581876282,104.443317304,108.735518837,111.596959859,108.020158581,108.735518837,125.188924713,132.342567269,116.604521647,102.297236537,90.8513924492,118.750602414,125.904284969,100.866476026,116.604521647,135.204008291,88.7052716827,90.8513924492,110.881599603,104.443317304,110.166239348,115.889161392,121.612083436,118.035242158,111.596959859,113.743080625,125.188924713,111.596959859,100.866476026,108.735518837,113.02768037,99.4357555153,106.58939807,132.342567269,119.466002669,115.889161392,101.581876282,113.02768037,126.619645224,118.750602414,97.2896747488,121.612083436,108.020158581,110.881599603,102.297236537,110.881599603,118.035242158,123.758164202,110.166239348,125.188924713,109.450879092,120.181362925,113.743080625,115.889161392,118.750602414,108.735518837,120.89672318,125.188924713,42.9218953303])

    # Creating a new Canvas
    fig   = plt.figure(figsize=(12,6),dpi=80)
    frame = gridspec.GridSpec(1,1,right=0.7)
    pad   = fig.add_subplot(frame[0])

    # Creating a new Stack
    pad.hist(x=xData, bins=xBinning, weights=y6_PHI_0_weights+y6_PHI_1_weights+y6_PHI_2_weights+y6_PHI_3_weights,\
             label="$signal100GeV4TeV$", histtype="stepfilled", rwidth=1.0,\
             color="#0000ff", edgecolor="#0000ff", linewidth=1, linestyle="solid",\
             bottom=None, cumulative=False, normed=False, align="mid", orientation="vertical")

    pad.hist(x=xData, bins=xBinning, weights=y6_PHI_0_weights+y6_PHI_1_weights+y6_PHI_2_weights,\
             label="$signal100GeV1p5TeV$", histtype="stepfilled", rwidth=1.0,\
             color="#59d354", edgecolor="#59d354", linewidth=1, linestyle="solid",\
             bottom=None, cumulative=False, normed=False, align="mid", orientation="vertical")

    pad.hist(x=xData, bins=xBinning, weights=y6_PHI_0_weights+y6_PHI_1_weights,\
             label="$signal100GeV1TeV$", histtype="stepfilled", rwidth=1.0,\
             color="#ce5e60", edgecolor="#ce5e60", linewidth=1, linestyle="solid",\
             bottom=None, cumulative=False, normed=False, align="mid", orientation="vertical")

    pad.hist(x=xData, bins=xBinning, weights=y6_PHI_0_weights,\
             label="$signal1MeV$", histtype="stepfilled", rwidth=1.0,\
             color="#5954d8", edgecolor="#5954d8", linewidth=1, linestyle="solid",\
             bottom=None, cumulative=False, normed=False, align="mid", orientation="vertical")


    # Axis
    plt.rc('text',usetex=False)
    plt.xlabel(r"\phi [ j_{2} ] ",\
               fontsize=16,color="black")
    plt.ylabel(r"$\mathrm{Events}$ $(\mathcal{L}_{\mathrm{int}} = 40.0\ \mathrm{fb}^{-1})$ ",\
               fontsize=16,color="black")

    # Boundary of y-axis
    ymax=(y6_PHI_0_weights+y6_PHI_1_weights+y6_PHI_2_weights+y6_PHI_3_weights).max()*1.1
    ymin=0 # linear scale
    #ymin=min([x for x in (y6_PHI_0_weights+y6_PHI_1_weights+y6_PHI_2_weights+y6_PHI_3_weights) if x])/100. # log scale
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
    plt.savefig('../../HTML/MadAnalysis5job_0/selection_5.png')
    plt.savefig('../../PDF/MadAnalysis5job_0/selection_5.png')
    plt.savefig('../../DVI/MadAnalysis5job_0/selection_5.eps')

# Running!
if __name__ == '__main__':
    selection_5()
