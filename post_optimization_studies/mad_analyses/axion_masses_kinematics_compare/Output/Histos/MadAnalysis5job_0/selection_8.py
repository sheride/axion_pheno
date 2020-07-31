def selection_8():

    # Library import
    import numpy
    import matplotlib
    import matplotlib.pyplot   as plt
    import matplotlib.gridspec as gridspec

    # Library version
    matplotlib_version = matplotlib.__version__
    numpy_version      = numpy.__version__

    # Histo binning
    xBinning = numpy.linspace(-15.0,15.0,101,endpoint=True)

    # Creating data sequence: middle of each bin
    xData = numpy.array([-14.85,-14.55,-14.25,-13.95,-13.65,-13.35,-13.05,-12.75,-12.45,-12.15,-11.85,-11.55,-11.25,-10.95,-10.65,-10.35,-10.05,-9.75,-9.45,-9.15,-8.85,-8.55,-8.25,-7.95,-7.65,-7.35,-7.05,-6.75,-6.45,-6.15,-5.85,-5.55,-5.25,-4.95,-4.65,-4.35,-4.05,-3.75,-3.45,-3.15,-2.85,-2.55,-2.25,-1.95,-1.65,-1.35,-1.05,-0.75,-0.45,-0.15,0.15,0.45,0.75,1.05,1.35,1.65,1.95,2.25,2.55,2.85,3.15,3.45,3.75,4.05,4.35,4.65,4.95,5.25,5.55,5.85,6.15,6.45,6.75,7.05,7.35,7.65,7.95,8.25,8.55,8.85,9.15,9.45,9.75,10.05,10.35,10.65,10.95,11.25,11.55,11.85,12.15,12.45,12.75,13.05,13.35,13.65,13.95,14.25,14.55,14.85])

    # Creating weights for histo: y9_sdETA_0
    y9_sdETA_0_weights = numpy.array([0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,406.568725926,1219.70657778,1219.70657778,813.137451852,2032.84402963,2032.84402963,5691.96296296,1626.2753037,4878.82711111,7318.23866667,9351.0822963,12197.0657778,14229.9094074,10570.7900741,24800.6954815,24800.6954815,33338.6419259,42283.1522963,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,38217.465037,34964.9176296,24800.6954815,23174.4197778,20328.4402963,14229.9094074,7724.80659259,9351.0822963,8537.94644444,4065.68725926,4878.82711111,7318.23866667,2439.41275556,1626.2753037,1219.70657778,813.137451852,2032.84402963,406.568725926,813.137451852,0.0,406.568725926,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0])

    # Creating weights for histo: y9_sdETA_1
    y9_sdETA_1_weights = numpy.array([0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,1704.5688044,340.913760881,2045.48248529,681.827361762,1363.65512352,2386.39656617,4431.88105145,3068.22392793,4772.79313233,7500.10177938,11931.9828308,8863.7581029,12954.7230735,17045.688044,15341.1196396,30341.3271984,43296.0502719,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,40227.8095439,35114.1203307,20795.7409337,19432.0846102,10568.3265073,8863.7581029,6818.27361762,7500.10177938,2727.31024705,5454.62129409,3750.05168969,2386.39656617,2045.48248529,1363.65512352,2386.39656617,681.827361762,1022.74144264,681.827361762,340.913760881,340.913760881,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0])

    # Creating weights for histo: y9_sdETA_2
    y9_sdETA_2_weights = numpy.array([0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,7.10822967737,14.2164553547,42.6493860642,49.7575837416,71.0822967737,156.381028902,326.978493159,263.004434063,326.978493159,483.359442061,589.983007221,860.095718961,867.203716639,1315.02197031,1286.5891796,1833.92260076,1791.2734147,2075.60252179,2196.44248231,2757.99229882,2772.20869417,3077.8625943,3888.20072952,4144.0986459,4933.11038809,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,4698.53846474,3824.22675042,3653.62920617,3376.40809675,2971.23902914,2452.33839869,2359.93162889,2111.14371018,1791.2734147,1585.13468205,1378.99634941,1243.93999354,817.446132897,682.389777027,540.22542348,476.251444384,334.086690836,234.571523353,170.597464257,99.5152074831,71.0822967737,28.4329107095,21.3246850321,14.2164553547,7.10822967737,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0])

    # Creating weights for histo: y9_sdETA_3
    y9_sdETA_3_weights = numpy.array([0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.715365066547,2.86146066619,2.86146066619,6.43828639892,8.58438319856,18.5994949302,24.3224170626,28.6146066619,51.5062991914,64.3828639892,97.2896762503,116.604523447,140.211572243,167.395462372,170.256903438,214.609559964,236.07052796,252.523934091,287.576827152,262.539017823,334.075564477,294.015109551,286.146066619,281.853905019,251.093173558,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,221.047842363,266.831219422,295.445830084,321.914319946,287.576827152,289.722907951,302.599472749,263.254378089,228.916845295,193.148591968,200.302274633,165.249341572,118.03524398,86.5591922521,90.8513938514,57.9445815903,56.5138610572,30.7607034615,25.7531455957,21.4609559964,14.3073053309,5.00755786583,4.29218959928,2.86146066619,1.43073053309,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0])

    # Creating a new Canvas
    fig   = plt.figure(figsize=(12,6),dpi=80)
    frame = gridspec.GridSpec(1,1,right=0.7)
    pad   = fig.add_subplot(frame[0])

    # Creating a new Stack
    pad.hist(x=xData, bins=xBinning, weights=y9_sdETA_0_weights+y9_sdETA_1_weights+y9_sdETA_2_weights+y9_sdETA_3_weights,\
             label="$signal100GeV4TeV$", histtype="stepfilled", rwidth=1.0,\
             color="#0000ff", edgecolor="#0000ff", linewidth=1, linestyle="solid",\
             bottom=None, cumulative=False, normed=False, align="mid", orientation="vertical")

    pad.hist(x=xData, bins=xBinning, weights=y9_sdETA_0_weights+y9_sdETA_1_weights+y9_sdETA_2_weights,\
             label="$signal100GeV1p5TeV$", histtype="stepfilled", rwidth=1.0,\
             color="#59d354", edgecolor="#59d354", linewidth=1, linestyle="solid",\
             bottom=None, cumulative=False, normed=False, align="mid", orientation="vertical")

    pad.hist(x=xData, bins=xBinning, weights=y9_sdETA_0_weights+y9_sdETA_1_weights,\
             label="$signal100GeV1TeV$", histtype="stepfilled", rwidth=1.0,\
             color="#ce5e60", edgecolor="#ce5e60", linewidth=1, linestyle="solid",\
             bottom=None, cumulative=False, normed=False, align="mid", orientation="vertical")

    pad.hist(x=xData, bins=xBinning, weights=y9_sdETA_0_weights,\
             label="$signal1MeV$", histtype="stepfilled", rwidth=1.0,\
             color="#5954d8", edgecolor="#5954d8", linewidth=1, linestyle="solid",\
             bottom=None, cumulative=False, normed=False, align="mid", orientation="vertical")


    # Axis
    plt.rc('text',usetex=False)
    plt.xlabel(r"\Delta\eta ( j_{1} , j_{2} ) ",\
               fontsize=16,color="black")
    plt.ylabel(r"$\mathrm{Events}$ $(\mathcal{L}_{\mathrm{int}} = 40.0\ \mathrm{fb}^{-1})$ ",\
               fontsize=16,color="black")

    # Boundary of y-axis
    ymax=(y9_sdETA_0_weights+y9_sdETA_1_weights+y9_sdETA_2_weights+y9_sdETA_3_weights).max()*1.1
    ymin=0 # linear scale
    #ymin=min([x for x in (y9_sdETA_0_weights+y9_sdETA_1_weights+y9_sdETA_2_weights+y9_sdETA_3_weights) if x])/100. # log scale
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
    plt.savefig('../../HTML/MadAnalysis5job_0/selection_8.png')
    plt.savefig('../../PDF/MadAnalysis5job_0/selection_8.png')
    plt.savefig('../../DVI/MadAnalysis5job_0/selection_8.eps')

# Running!
if __name__ == '__main__':
    selection_8()
