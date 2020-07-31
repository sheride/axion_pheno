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
    xBinning = numpy.linspace(0.0,8000.0,81,endpoint=True)

    # Creating data sequence: middle of each bin
    xData = numpy.array([50.0,150.0,250.0,350.0,450.0,550.0,650.0,750.0,850.0,950.0,1050.0,1150.0,1250.0,1350.0,1450.0,1550.0,1650.0,1750.0,1850.0,1950.0,2050.0,2150.0,2250.0,2350.0,2450.0,2550.0,2650.0,2750.0,2850.0,2950.0,3050.0,3150.0,3250.0,3350.0,3450.0,3550.0,3650.0,3750.0,3850.0,3950.0,4050.0,4150.0,4250.0,4350.0,4450.0,4550.0,4650.0,4750.0,4850.0,4950.0,5050.0,5150.0,5250.0,5350.0,5450.0,5550.0,5650.0,5750.0,5850.0,5950.0,6050.0,6150.0,6250.0,6350.0,6450.0,6550.0,6650.0,6750.0,6850.0,6950.0,7050.0,7150.0,7250.0,7350.0,7450.0,7550.0,7650.0,7750.0,7850.0,7950.0])

    # Creating weights for histo: y12_TET_0
    y12_TET_0_weights = numpy.array([14689.7202763,61854.231035,43135.1990217,45169.8729331,39879.6927383,30520.172728,29299.3683812,34996.4673438,13835.8106225,19939.848371,13428.8758402,12208.0714934,11801.1327075,7324.8420953,8545.65044572,4476.29061219,2441.61389831,4476.29061219,813.871165985,1220.80714934,1627.74273233,2034.67831532,1220.80714934,0.0,406.935582992,0.0,0.0,0.0,406.935582992,0.0,0.0,0.0,0.0,406.935582992,0.0,0.0,0.0,0.0,0.0,406.935582992,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0])

    # Creating weights for histo: y12_TET_1
    y12_TET_1_weights = numpy.array([3793.39976523,28662.0560109,34462.7090597,32074.2043921,33780.2785827,34462.7090597,26955.9818203,26273.5513433,23885.0466757,14672.2412422,13989.8107652,11260.0928609,10918.8796242,7847.94447968,6824.29676248,5118.22257186,4777.00933515,3753.36442042,3070.93434382,2047.2894291,2729.7195057,1023.64491472,682.429676248,3070.93434382,341.214918195,1023.64491472,341.214918195,1023.64491472,341.214918195,0.0,341.214918195,0.0,682.429676248,0.0,0.0,341.214918195,0.0,0.0,341.214918195,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0])

    # Creating weights for histo: y12_TET_2
    y12_TET_2_weights = numpy.array([2236.08139601,11217.2745793,10378.4661937,8267.23061324,7584.80901138,5885.87131541,5061.27954654,4023.43452723,2914.50082427,2623.05058183,2082.8019471,1713.15791281,1421.70767037,1009.41258597,988.08686091,675.311293433,533.140326388,390.969599352,334.101292537,334.101292537,284.341534074,191.9305255,199.039073852,156.387863742,142.170767037,113.73661363,49.7597584626,42.651250112,35.5426937594,28.4341534074,21.3256170557,35.5426937594,21.3256170557,14.2170767037,14.2170767037,21.3256170557,0.0,7.10854035195,0.0,7.10854035195,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,14.2170767037,0.0,0.0,7.10854035195,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0])

    # Creating weights for histo: y12_TET_3
    y12_TET_3_weights = numpy.array([320.759524674,1477.98114439,1255.60476433,938.843285465,751.503631558,573.459713032,424.017073055,341.787637576,248.117810622,173.753966634,142.292360322,112.975809919,79.369107716,78.6540757523,52.1976931864,37.181917996,30.0315503808,19.3059949599,16.4458471142,16.4458471142,12.8706633066,16.4458471142,6.4353316533,6.4353316533,5.72029569141,3.57518460722,2.86014744589,1.43007392285,2.14511068437,0.715036761518,1.43007392285,0.0,0.0,0.0,1.43007392285,0.715036761518,0.0,0.0,0.0,0.0,0.0,0.715036761518,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0])

    # Creating a new Canvas
    fig   = plt.figure(figsize=(12,6),dpi=80)
    frame = gridspec.GridSpec(1,1,right=0.7)
    pad   = fig.add_subplot(frame[0])

    # Creating a new Stack
    pad.hist(x=xData, bins=xBinning, weights=y12_TET_0_weights+y12_TET_1_weights+y12_TET_2_weights+y12_TET_3_weights,\
             label="$signal100GeV4TeV$", histtype="stepfilled", rwidth=1.0,\
             color="#0000ff", edgecolor="#0000ff", linewidth=1, linestyle="solid",\
             bottom=None, cumulative=False, normed=False, align="mid", orientation="vertical")

    pad.hist(x=xData, bins=xBinning, weights=y12_TET_0_weights+y12_TET_1_weights+y12_TET_2_weights,\
             label="$signal100GeV1p5TeV$", histtype="stepfilled", rwidth=1.0,\
             color="#59d354", edgecolor="#59d354", linewidth=1, linestyle="solid",\
             bottom=None, cumulative=False, normed=False, align="mid", orientation="vertical")

    pad.hist(x=xData, bins=xBinning, weights=y12_TET_0_weights+y12_TET_1_weights,\
             label="$signal100GeV1TeV$", histtype="stepfilled", rwidth=1.0,\
             color="#ce5e60", edgecolor="#ce5e60", linewidth=1, linestyle="solid",\
             bottom=None, cumulative=False, normed=False, align="mid", orientation="vertical")

    pad.hist(x=xData, bins=xBinning, weights=y12_TET_0_weights,\
             label="$signal1MeV$", histtype="stepfilled", rwidth=1.0,\
             color="#5954d8", edgecolor="#5954d8", linewidth=1, linestyle="solid",\
             bottom=None, cumulative=False, normed=False, align="mid", orientation="vertical")


    # Axis
    plt.rc('text',usetex=False)
    plt.xlabel(r"TET",\
               fontsize=16,color="black")
    plt.ylabel(r"$\mathrm{Events}$ $(\mathcal{L}_{\mathrm{int}} = 40.0\ \mathrm{fb}^{-1})$ ",\
               fontsize=16,color="black")

    # Boundary of y-axis
    ymax=(y12_TET_0_weights+y12_TET_1_weights+y12_TET_2_weights+y12_TET_3_weights).max()*1.1
    ymin=0 # linear scale
    #ymin=min([x for x in (y12_TET_0_weights+y12_TET_1_weights+y12_TET_2_weights+y12_TET_3_weights) if x])/100. # log scale
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
