def selection_1():

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

    # Creating weights for histo: y2_ETA_0
    y2_ETA_0_weights = numpy.array([0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,1.45944923233,1.59212632618,1.32677183848,2.78622107081,3.84763782159,4.51102479083,5.30708675392,4.77637777853,8.75669359397,11.0122074894,10.2161425263,13.4003963786,13.2677183848,20.1669350649,17.6460681818,23.6165419049,26.9334707511,31.7098485297,34.4960684005,39.5378081667,38.4763782159,46.7023778345,50.2846476684,53.9996074961,62.2256071147,64.8791369917,70.1862267456,70.5842667271,74.8299265303,76.4220564564,76.5547464503,76.1567064687,79.3409663211,78.6775763519,70.716956721,77.3507964134,63.9503970347,63.4196970593,56.7858273669,44.1815079514,46.5696878406,36.3535483144,33.7000184374,25.7393748065,25.2086658311,21.6263839972,17.1153592064,12.7370094094,9.81811154475,6.50118269855,9.55275855706,9.02204958166,12.8696874033,17.3807121941,16.7173252248,22.2897679665,26.9334707511,32.5058984928,37.0169382836,51.6114276069,52.0094675884,53.3362175269,59.4393872439,69.5228367763,70.716956721,68.7267868133,82.3925361796,75.2279665118,73.3704865979,73.1051366102,81.3311062288,74.9626165241,72.441746641,67.1346568871,66.8693068994,57.8472573177,59.8374272254,49.753947693,43.2527679944,40.4665481236,39.6704681606,32.5058984928,29.719690622,26.8007927573,20.4322880526,18.4421301449,17.5133901879,14.3291363356,12.6043344156,11.2775604771,11.0122074894,8.09330962473,5.17441176007,5.30708675392,3.98031581544,4.51102479083,2.25551239542,1.59212632618,1.99015790772,0.796063163088,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0])

    # Creating weights for histo: y2_ETA_1
    y2_ETA_1_weights = numpy.array([0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,1.04195493284,1.20261547487,1.52315597965,2.00346823323,2.0036903566,3.12465526036,3.44682407031,4.88866850925,4.3275507126,6.17145343303,8.09349201947,8.97531279171,8.33512986799,12.1809276726,13.4632869349,17.7892818846,15.4683684852,19.553268155,22.8411526148,22.8401484133,25.8892067887,31.6554874169,31.4963139923,36.3067087452,39.6721924977,41.3573324669,45.7652372816,47.6064931069,49.8490698,50.4890309001,48.4862635096,50.7322275091,53.2154228612,47.8424954368,49.3703504797,43.1985283399,43.7577636335,38.1485341175,35.1028660462,30.9335714876,29.1745702531,23.6433836771,23.0009975054,18.194622556,13.7835222823,11.2199578401,9.69718075912,8.89610677668,6.25094122399,4.88780219815,4.64821471917,6.33202974204,8.65648332631,10.8995426357,12.9831377516,14.0256937065,20.2748393584,20.8354235793,26.3693200005,27.808097878,30.294989291,36.6243661426,39.1886769913,43.4362692872,45.6795054559,50.2497311923,50.8106751272,47.2845491181,49.9288963216,51.293171444,52.8169497288,49.6891469713,48.9698689444,42.5590168822,37.1069224117,39.1076214471,34.1404213864,34.7009156789,33.257203725,25.0044183763,25.4846724761,23.8019575784,20.4335691358,17.7896296081,16.2707883974,11.4592845264,11.3801084876,8.73451727337,7.77353545035,7.13391308088,5.52874351879,5.37013064844,3.28537545496,4.08726179141,2.08390956593,1.76325455221,1.76300005459,1.84288982589,1.12177965587,0.80129700509,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0])

    # Creating weights for histo: y2_ETA_2
    y2_ETA_2_weights = numpy.array([0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.781270083839,1.14586286963,1.25003219414,1.61462497993,1.71879430445,2.23964122701,2.91674198633,3.48967282115,4.06260395596,4.63553509078,5.10429720108,5.26055223785,5.78140036041,8.90648009577,9.06273513254,10.8336145492,12.812832015,13.5420181865,13.6461872111,16.8233529587,18.3858913263,22.8651743804,23.0735124294,27.7611335324,26.7194402873,28.4382366917,30.1049470839,30.521617182,33.3862878561,33.3862878561,33.8029579541,34.5842181379,34.1675480399,33.3862878561,32.969587758,31.0945573168,27.8132195447,25.6256640299,23.8547846132,21.6151430862,18.3338083141,15.4170666278,13.4899321743,13.2815941253,8.90648009577,9.2189871693,6.9793456423,5.6772313359,3.33342078438,3.43758980889,2.55214920054,4.58345207852,4.63553509078,6.19807645846,8.43771798546,10.6773595125,11.6148837331,14.1670323336,17.3441980812,17.7608771793,22.0839051965,25.7298330544,25.7819160667,25.834002079,30.8341272555,30.4174571575,31.1466373291,34.7404881747,34.6362981502,35.0529982483,35.2613182973,33.8550379664,31.1987173413,32.3445976109,28.9069988021,29.0111678266,24.4797987603,22.3443292578,20.3130257798,20.0005157063,17.2400290567,14.0628633091,11.5627977208,12.1878148679,10.9377835737,9.53149724284,7.29185571583,6.56266954425,5.72931434815,4.47928305401,3.85426590694,3.38550379664,2.44797987603,2.70840333731,1.66670979219,1.19794768189,1.04169354512,0.989609032863,0.781270083839,0.416677298048,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0])

    # Creating weights for histo: y2_ETA_3
    y2_ETA_3_weights = numpy.array([0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.391178513022,0.960164977418,0.960164977418,1.06685010824,0.711233305495,1.38690520071,1.81364512401,2.24038534731,3.5206060172,2.59600185006,3.8050990994,4.19627821242,5.04975745901,5.47649858231,5.79655367478,7.07677104467,8.10806034264,9.708335805,11.2019252365,13.0866937811,13.335624853,13.6201209352,14.6514072332,17.4963410552,17.9230821785,20.9102610415,21.7637432881,22.6883465553,22.4038534731,25.106539254,23.7551948635,24.6442361204,22.4394124834,23.3640157505,22.3327294525,21.1591921135,19.9500957641,17.2829719935,14.9359003154,14.9359003154,13.0866937811,11.9842834626,10.3128839797,8.49923945566,7.61019819879,6.29441581863,4.94307142819,3.55616802747,3.34279596582,1.92033025484,2.09813850621,2.88049523225,3.84066110967,5.36981255148,6.54334689055,6.57890890083,9.06822562006,9.708335805,12.0198454729,13.2645038325,15.149272377,17.3185340038,17.2474099832,20.0212197847,20.8035780107,21.7637432881,22.3682914628,22.6172225347,25.2487842951,24.7153601409,24.5375530896,22.8305915964,21.621495247,21.4792472059,20.8746990313,19.41667161,18.0297652093,15.7182585414,14.6869692435,14.6514072332,11.5931043496,10.099514918,9.4238427228,7.75244323989,7.85912927072,6.6144709111,6.08104675698,5.61874362341,3.91178513022,3.27167494528,2.59600185006,2.27594675758,2.06257679593,1.56471345209,1.45802832126,1.17353523907,0.817918436319,0.462301633572,0.568986764396,0.106685010824,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0])

    # Creating weights for histo: y2_ETA_4
    y2_ETA_4_weights = numpy.array([0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0])

    # Creating weights for histo: y2_ETA_5
    y2_ETA_5_weights = numpy.array([0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,79.0971291539,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,78.9085371523,0.0,0.0,0.0,0.0,78.97186254,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0])

    # Creating weights for histo: y2_ETA_6
    y2_ETA_6_weights = numpy.array([0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,17.2515124641,0.0,17.2947860598,0.0,17.2486880802,0.0,17.2821195627,34.5406295819,0.0,17.2515124641,0.0,51.874622701,34.5832835424,17.2940799638,34.5409754248,51.8767842193,34.5442032921,69.1565664602,17.30641791,69.053707011,17.2596397728,0.0,0.0,17.2639685733,17.2940799638,17.2109249151,51.8136102454,17.2770126156,17.2277472912,0.0,0.0,0.0,17.2486880802,17.30641791,17.3004867039,0.0,34.5413789083,69.1357870646,0.0,17.2464343372,34.5757614588,34.4951224174,51.8131491215,34.5531663879,34.6112968191,51.8655443243,34.5912667498,34.5182074324,51.8340726183,17.292682182,17.2821195627,0.0,34.5543768381,34.5072557399,0.0,17.2277472912,17.2515124641,34.5813814063,17.2515124641,0.0,0.0,34.55933392,17.2464343372,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0])

    # Creating weights for histo: y2_ETA_7
    y2_ETA_7_weights = numpy.array([0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,2.08223946531,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,4.14932829355,6.23077667368,0.0,6.23785662634,6.23592363193,8.31175478801,8.30954194218,22.8580916521,22.8401234593,31.1529457219,20.7628382298,14.541544769,24.9169441931,18.6802646739,18.6696332046,16.6040757695,33.2329054078,22.8487815432,10.3871820348,26.9963614866,26.9875447241,16.6251482937,16.6190867694,10.3824736066,16.6179962144,16.6071656755,12.4587029019,18.6906797631,6.23248463292,12.4683880694,8.31708062037,20.7747073925,14.5310171622,24.9078648896,16.6093439006,33.2609194014,12.4604772176,22.8514156088,14.5405176854,14.5512328216,27.0011968577,24.917850104,33.2199514602,29.0717743081,24.9210381022,16.6092717739,29.0705625803,16.6102238458,14.532751087,6.23569282663,10.3851596034,6.22824358549,2.07303841192,4.15633323448,0.0,2.07522125307,4.15309907518,4.15325775382,2.07672610364,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0])

    # Creating weights for histo: y2_ETA_8
    y2_ETA_8_weights = numpy.array([0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.756356590431,0.0,0.0,1.51430307084,1.5130946088,0.0,4.53674036657,3.77716439686,6.80353659064,6.80741914476,6.04828195373,4.53183869889,8.32150146077,4.53361156505,9.07391587051,7.56083491665,7.56481760698,6.04232840063,3.78336510434,6.05150451917,5.2948525269,8.32638537703,6.80299494475,9.07609155735,6.04037574446,3.78463410327,6.80367769167,2.26775844205,4.53082049566,3.78704602054,4.54267662341,6.80251247027,7.56563690328,5.2916527197,9.07921398657,6.05351634674,7.55460826479,8.31643547866,8.31943046179,6.79792896265,6.05372572246,4.52855332074,5.29470687423,6.80354114229,4.53606217131,5.29259491044,2.27098464881,3.7748680914,2.27073157728,1.51265446463,2.26680805835,3.02760887603,3.02796754574,1.5130946088,0.757151763004,0.755036157898,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0])

    # Creating weights for histo: y2_ETA_9
    y2_ETA_9_weights = numpy.array([0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.211760959591,0.212060771744,0.212259097916,0.849832408802,0.212437802119,0.849003380587,0.636924227674,1.06034901811,3.18186684867,3.18453312807,2.54561207643,1.27318621387,3.39328202876,2.96794698187,2.75736342702,2.54471523699,2.54784898096,4.87972702219,1.69744811216,3.60599860712,2.54771999537,2.12263484004,2.33358399835,3.60538686336,3.39183346571,2.1247418933,3.18435999304,2.97231575569,2.54649737353,1.27357461345,4.03105952355,2.33583446512,1.48522641141,2.75801239481,2.12264320823,3.39527885272,2.5474833775,2.97099704391,2.96954559528,4.03243017584,1.90967875822,1.48557412425,2.12157352233,1.48544629289,1.90931200052,1.06052994421,1.69787662135,1.69753525679,1.48504721665,0.849078694323,0.424543819816,0.212260569564,0.212259097916,0.0,0.211642910359,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0])

    # Creating weights for histo: y2_ETA_10
    y2_ETA_10_weights = numpy.array([0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.230905955223,0.0,0.0,0.229059452883,0.454503994725,0.0,0.113795548744,0.344319102205,0.455315069393,0.115366108412,0.0,0.34353293595,0.454789067526,0.0,0.115222153739,0.0,0.114144621098,0.34185760139,0.341338779529,0.114071225489,0.457247554511,0.0,0.341835263596,0.115174287037,0.34235461731,0.228408554382,0.686838593709,0.0,0.341020288679,0.0,0.113137204311,0.114229185604,0.228317696291,0.229043054106,0.114575687339,0.0,0.0,0.0,0.229559482632,0.0,0.22959414167,0.229122388732,0.114071225489,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0])

    # Creating weights for histo: y2_ETA_11
    y2_ETA_11_weights = numpy.array([0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0135414779986,0.0,0.0135469611382,0.0,0.0,0.0406421047775,0.0135469611382,0.0,0.0134999025763,0.013530153684,0.0,0.0135575231838,0.0270858116186,0.0,0.0541255463854,0.0541074136226,0.0270961109124,0.0407030574245,0.0,0.0541750361235,0.0406357236619,0.0135566280952,0.040594665081,0.013537753275,0.0271177893811,0.0271302917479,0.0677010666251,0.0,0.0406509112944,0.0135115935885,0.0135492854812,0.0135400371947,0.0,0.0135414779986,0.0,0.0135002721612,0.0,0.0135469611382,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0])

    # Creating weights for histo: y2_ETA_12
    y2_ETA_12_weights = numpy.array([0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.912787033803,0.0,0.0,0.0,0.0,0.0,0.909853848219,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.909306167943,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.913150150035,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0])

    # Creating weights for histo: y2_ETA_13
    y2_ETA_13_weights = numpy.array([0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.752772971972,0.752556969762,0.753054673564,0.754386015739,0.0,0.0,2.25993133988,1.50619828921,2.25718932043,2.25954768029,1.50630117692,0.754099045801,3.01024771282,2.26392722582,1.50480372688,2.25843574925,1.50539626092,0.753054673564,2.25801552113,0.752246757118,2.26201295659,0.0,1.5042180107,1.50468007569,1.50620293776,0.0,2.25914356711,0.752556969762,1.50676665084,0.0,0.752667295138,0.0,0.0,0.0,0.0,0.0,0.751402891954,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.755225232362,0.753429965783,0.752468957383,0.751152180637,0.752468957383,0.753054673564,0.754386015739,0.753054673564,0.752752518391,1.50732633519,2.26169468648,3.00771704704,1.5068190244,2.26129553174,4.51350409532,3.01190817171,0.752772971972,2.25808060071,3.76763637622,0.0,0.752752518391,2.25830961883,3.00965920752,0.752433318568,1.50724080204,1.50566711592,1.50862079894,3.0109127641,0.0,0.0,0.0,0.754573816801,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0])

    # Creating weights for histo: y2_ETA_14
    y2_ETA_14_weights = numpy.array([0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.412673551619,0.412082141934,2.06086714023,0.82472674769,2.06405240393,3.30476136773,4.12649785542,5.36525586806,7.84363417534,5.77365152582,9.48685120837,9.90265700706,11.1414972869,12.3759652179,9.90224567111,16.0840155838,12.374009087,10.307637053,9.90029258709,11.9613355353,6.59945262206,10.7246860003,8.66282952096,8.254988405,7.4251135594,6.59653670723,4.95479438976,5.35648984196,4.53319941846,2.88485256913,3.3021044422,2.47511321394,1.65146081481,2.0653351627,3.29888383407,0.411927967127,0.826322731169,1.236996276,0.824474461642,0.412346311021,0.412426445357,0.826028092753,0.412682387725,1.23575251797,0.413102864472,2.88919658143,1.65110188611,2.8860125365,2.89043515968,4.12505665614,5.36482015664,7.01174530706,6.18982295646,8.25172513981,6.59519910367,5.77320057974,9.89316885785,12.7858325443,13.6115026224,12.3752248132,15.6753548429,16.9196917897,10.3147668761,8.25064347861,11.5557552436,7.83817102457,8.66147972966,9.48346911279,7.01470387896,5.36716324808,7.01539857967,2.88680748131,4.54044502502,1.23874034042,0.0,1.65103637705,0.413852105284,0.412282934815,0.0,0.0,0.0,0.410940760852,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0])

    # Creating weights for histo: y2_ETA_15
    y2_ETA_15_weights = numpy.array([0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.148078101576,0.517898435166,0.666564282224,1.40676314377,1.48016383942,2.07218115546,2.51750770901,3.18364691215,4.81119775392,6.14337875878,7.17915278186,9.4743242905,9.99126734991,9.47337733216,10.4346813482,9.3270376958,8.9550814751,9.84404689198,11.0996775877,8.50942183272,10.2152214963,5.92201597147,6.58661238406,5.9209938577,4.07032760412,4.66208638551,3.18209871041,2.8872471453,2.29465804678,1.85162523679,1.40621661353,1.40627222854,0.44408648904,1.11084978283,0.813844563876,0.740564417534,0.740256580915,0.592443898236,0.961944640899,1.03636354223,1.84958852479,2.36749207053,2.29403215241,3.03412369201,4.44000511234,4.4398728388,4.51652535935,6.66190308832,7.62257579881,7.62475831234,8.80698620803,7.8449787372,9.91903096211,8.80649920088,10.8065714321,8.36373755166,8.06865931779,10.0651812068,8.73652048202,7.32612372379,6.51268650231,5.69789648319,4.36734484794,2.51576350192,1.99893828621,1.85067948093,1.33255407638,0.591968915953,0.0737931572703,0.147715822368,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0])

    # Creating weights for histo: y2_ETA_16
    y2_ETA_16_weights = numpy.array([0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0189268819331,0.0377617220488,0.245746521156,0.226967733763,0.774988081812,0.794114246644,1.3236616831,1.9099154255,2.15526694586,3.28941167002,3.83839765893,3.32721327326,3.78155571494,4.42386788156,4.06438804855,4.44321130733,3.59230162974,3.51627230374,3.55422995075,2.98737604994,2.74160051065,2.09918301448,1.75813075036,1.79615531613,1.28583547296,0.907473143471,0.643105289088,0.680628414211,0.378070947757,0.340288549909,0.245732927343,0.34037857516,0.151217125946,0.189027221564,0.283371494847,0.529310670041,0.643055175031,0.812769279324,1.00179980181,1.17202044819,1.51202331797,1.66379418924,2.1363592423,2.74121250181,2.68441947154,3.34621460307,3.66812989934,4.13991323314,4.17797891044,3.98822968636,4.23498289989,4.08332936153,3.72486981471,3.2520781981,3.17581780729,2.60895340354,1.98475941901,1.17230972933,1.07779041695,0.604909675334,0.321240707046,0.245692506005,0.0756395166556,0.0378256999944,0.018882820574,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0])

    # Creating weights for histo: y2_ETA_17
    y2_ETA_17_weights = numpy.array([0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0215457283154,0.0,0.0,0.042831431868,0.128702285423,0.172116073788,0.558715312587,0.622558214856,0.708380932339,0.751269122784,1.41748360585,1.33178340291,1.69627693792,1.97604498797,1.78149952905,1.48153457291,1.86833790266,1.45959592079,1.52628537442,1.37450079278,1.03010219337,1.03025964781,0.665925366716,0.729297630162,0.687591547678,0.257901302118,0.449990846649,0.23656892457,0.107409646377,0.128886507119,0.107376281031,0.128800731938,0.171845627041,0.0861165574612,0.257027579927,0.365475600854,0.257589692281,0.42971633801,0.579605842982,0.687435067955,0.859103671217,1.07316298387,1.07397274957,1.56791932777,1.67448374371,1.37319317113,1.37538253765,1.82480849775,1.45925401972,1.73864267954,1.20272624517,1.11737993984,0.923918667214,0.666026962319,0.557901348105,0.45078891573,0.300558484405,0.0430193649902,0.0854155852852,0.0,0.0430420159362,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0])

    # Creating weights for histo: y2_ETA_18
    y2_ETA_18_weights = numpy.array([0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.00162193247978,0.00161987744514,0.00324628523592,0.0194429474461,0.0356414924427,0.0502051753404,0.0760123620339,0.12960032934,0.135966504808,0.153913482586,0.170088000839,0.170129114105,0.136086512796,0.173335194464,0.158718202622,0.147215289207,0.103694194205,0.0745182028577,0.0922194440053,0.0712847450865,0.0583049287508,0.0534689022821,0.0550666304268,0.0242991690778,0.0372717214413,0.0194433560642,0.0177078764766,0.0275397242309,0.0178243357741,0.0129612525018,0.0290469214672,0.0534906533371,0.0403820280081,0.0696555847814,0.0550619784671,0.0728842648643,0.0939835740071,0.1036907681,0.10678642728,0.127825260946,0.174824638816,0.136075385812,0.139330406045,0.147411614481,0.131226000675,0.105291670893,0.0939586483039,0.0794115930191,0.0583362037504,0.0388747930532,0.0194263638383,0.00648453326843,0.00323900240436,0.00161987744514,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0])

    # Creating weights for histo: y2_ETA_19
    y2_ETA_19_weights = numpy.array([0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0021298050306,0.0,0.0042574418078,0.00639202657314,0.00852030480589,0.00636206191271,0.0042471595872,0.010622733271,0.0106549062758,0.0170332284184,0.0254326099446,0.0191748324447,0.0127762910887,0.00848699700388,0.00638614767759,0.00850279618764,0.0127916370218,0.00852171689901,0.0170414804768,0.00211496468924,0.00213060685003,0.0021298050306,0.00425983167517,0.00212763677721,0.00636615119182,0.0021298050306,0.0147763517121,0.0106340957206,0.0106548294348,0.012742046717,0.012760867201,0.00850870403778,0.0149182737519,0.00851944173636,0.014913073062,0.0211878224065,0.017036313196,0.0275742028345,0.00638941620542,0.0148833389247,0.0127718031271,0.0021298050306,0.00425983167517,0.00425604530562,0.00422776112509,0.00213219489796,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0])

    # Creating a new Canvas
    fig   = plt.figure(figsize=(12,6),dpi=80)
    frame = gridspec.GridSpec(1,1,right=0.7)
    pad   = fig.add_subplot(frame[0])

    # Creating a new Stack
    pad.hist(x=xData, bins=xBinning, weights=y2_ETA_0_weights+y2_ETA_1_weights+y2_ETA_2_weights+y2_ETA_3_weights+y2_ETA_4_weights+y2_ETA_5_weights+y2_ETA_6_weights+y2_ETA_7_weights+y2_ETA_8_weights+y2_ETA_9_weights+y2_ETA_10_weights+y2_ETA_11_weights+y2_ETA_12_weights+y2_ETA_13_weights+y2_ETA_14_weights+y2_ETA_15_weights+y2_ETA_16_weights+y2_ETA_17_weights+y2_ETA_18_weights+y2_ETA_19_weights,\
             label="$bg\_vbf\_1600\_inf$", histtype="step", rwidth=1.0,\
             color=None, edgecolor="#ccc6aa", linewidth=1, linestyle="solid",\
             bottom=None, cumulative=False, normed=False, align="mid", orientation="vertical")

    pad.hist(x=xData, bins=xBinning, weights=y2_ETA_0_weights+y2_ETA_1_weights+y2_ETA_2_weights+y2_ETA_3_weights+y2_ETA_4_weights+y2_ETA_5_weights+y2_ETA_6_weights+y2_ETA_7_weights+y2_ETA_8_weights+y2_ETA_9_weights+y2_ETA_10_weights+y2_ETA_11_weights+y2_ETA_12_weights+y2_ETA_13_weights+y2_ETA_14_weights+y2_ETA_15_weights+y2_ETA_16_weights+y2_ETA_17_weights+y2_ETA_18_weights,\
             label="$bg\_vbf\_1200\_1600$", histtype="step", rwidth=1.0,\
             color=None, edgecolor="#c1bfa8", linewidth=1, linestyle="solid",\
             bottom=None, cumulative=False, normed=False, align="mid", orientation="vertical")

    pad.hist(x=xData, bins=xBinning, weights=y2_ETA_0_weights+y2_ETA_1_weights+y2_ETA_2_weights+y2_ETA_3_weights+y2_ETA_4_weights+y2_ETA_5_weights+y2_ETA_6_weights+y2_ETA_7_weights+y2_ETA_8_weights+y2_ETA_9_weights+y2_ETA_10_weights+y2_ETA_11_weights+y2_ETA_12_weights+y2_ETA_13_weights+y2_ETA_14_weights+y2_ETA_15_weights+y2_ETA_16_weights+y2_ETA_17_weights,\
             label="$bg\_vbf\_800\_1200$", histtype="step", rwidth=1.0,\
             color=None, edgecolor="#bab5a3", linewidth=1, linestyle="solid",\
             bottom=None, cumulative=False, normed=False, align="mid", orientation="vertical")

    pad.hist(x=xData, bins=xBinning, weights=y2_ETA_0_weights+y2_ETA_1_weights+y2_ETA_2_weights+y2_ETA_3_weights+y2_ETA_4_weights+y2_ETA_5_weights+y2_ETA_6_weights+y2_ETA_7_weights+y2_ETA_8_weights+y2_ETA_9_weights+y2_ETA_10_weights+y2_ETA_11_weights+y2_ETA_12_weights+y2_ETA_13_weights+y2_ETA_14_weights+y2_ETA_15_weights+y2_ETA_16_weights,\
             label="$bg\_vbf\_600\_800$", histtype="step", rwidth=1.0,\
             color=None, edgecolor="#b2a596", linewidth=1, linestyle="solid",\
             bottom=None, cumulative=False, normed=False, align="mid", orientation="vertical")

    pad.hist(x=xData, bins=xBinning, weights=y2_ETA_0_weights+y2_ETA_1_weights+y2_ETA_2_weights+y2_ETA_3_weights+y2_ETA_4_weights+y2_ETA_5_weights+y2_ETA_6_weights+y2_ETA_7_weights+y2_ETA_8_weights+y2_ETA_9_weights+y2_ETA_10_weights+y2_ETA_11_weights+y2_ETA_12_weights+y2_ETA_13_weights+y2_ETA_14_weights+y2_ETA_15_weights,\
             label="$bg\_vbf\_400\_600$", histtype="step", rwidth=1.0,\
             color=None, edgecolor="#b7a39b", linewidth=1, linestyle="solid",\
             bottom=None, cumulative=False, normed=False, align="mid", orientation="vertical")

    pad.hist(x=xData, bins=xBinning, weights=y2_ETA_0_weights+y2_ETA_1_weights+y2_ETA_2_weights+y2_ETA_3_weights+y2_ETA_4_weights+y2_ETA_5_weights+y2_ETA_6_weights+y2_ETA_7_weights+y2_ETA_8_weights+y2_ETA_9_weights+y2_ETA_10_weights+y2_ETA_11_weights+y2_ETA_12_weights+y2_ETA_13_weights+y2_ETA_14_weights,\
             label="$bg\_vbf\_200\_400$", histtype="step", rwidth=1.0,\
             color=None, edgecolor="#ad998c", linewidth=1, linestyle="solid",\
             bottom=None, cumulative=False, normed=False, align="mid", orientation="vertical")

    pad.hist(x=xData, bins=xBinning, weights=y2_ETA_0_weights+y2_ETA_1_weights+y2_ETA_2_weights+y2_ETA_3_weights+y2_ETA_4_weights+y2_ETA_5_weights+y2_ETA_6_weights+y2_ETA_7_weights+y2_ETA_8_weights+y2_ETA_9_weights+y2_ETA_10_weights+y2_ETA_11_weights+y2_ETA_12_weights+y2_ETA_13_weights,\
             label="$bg\_vbf\_100\_200$", histtype="step", rwidth=1.0,\
             color=None, edgecolor="#9b8e82", linewidth=1, linestyle="solid",\
             bottom=None, cumulative=False, normed=False, align="mid", orientation="vertical")

    pad.hist(x=xData, bins=xBinning, weights=y2_ETA_0_weights+y2_ETA_1_weights+y2_ETA_2_weights+y2_ETA_3_weights+y2_ETA_4_weights+y2_ETA_5_weights+y2_ETA_6_weights+y2_ETA_7_weights+y2_ETA_8_weights+y2_ETA_9_weights+y2_ETA_10_weights+y2_ETA_11_weights+y2_ETA_12_weights,\
             label="$bg\_vbf\_0\_100$", histtype="step", rwidth=1.0,\
             color=None, edgecolor="#876656", linewidth=1, linestyle="solid",\
             bottom=None, cumulative=False, normed=False, align="mid", orientation="vertical")

    pad.hist(x=xData, bins=xBinning, weights=y2_ETA_0_weights+y2_ETA_1_weights+y2_ETA_2_weights+y2_ETA_3_weights+y2_ETA_4_weights+y2_ETA_5_weights+y2_ETA_6_weights+y2_ETA_7_weights+y2_ETA_8_weights+y2_ETA_9_weights+y2_ETA_10_weights+y2_ETA_11_weights,\
             label="$bg\_dip\_1600\_inf$", histtype="step", rwidth=1.0,\
             color=None, edgecolor="#afcec6", linewidth=1, linestyle="solid",\
             bottom=None, cumulative=False, normed=False, align="mid", orientation="vertical")

    pad.hist(x=xData, bins=xBinning, weights=y2_ETA_0_weights+y2_ETA_1_weights+y2_ETA_2_weights+y2_ETA_3_weights+y2_ETA_4_weights+y2_ETA_5_weights+y2_ETA_6_weights+y2_ETA_7_weights+y2_ETA_8_weights+y2_ETA_9_weights+y2_ETA_10_weights,\
             label="$bg\_dip\_1200\_1600$", histtype="step", rwidth=1.0,\
             color=None, edgecolor="#84c1a3", linewidth=1, linestyle="solid",\
             bottom=None, cumulative=False, normed=False, align="mid", orientation="vertical")

    pad.hist(x=xData, bins=xBinning, weights=y2_ETA_0_weights+y2_ETA_1_weights+y2_ETA_2_weights+y2_ETA_3_weights+y2_ETA_4_weights+y2_ETA_5_weights+y2_ETA_6_weights+y2_ETA_7_weights+y2_ETA_8_weights+y2_ETA_9_weights,\
             label="$bg\_dip\_800\_1200$", histtype="step", rwidth=1.0,\
             color=None, edgecolor="#89a8a0", linewidth=1, linestyle="solid",\
             bottom=None, cumulative=False, normed=False, align="mid", orientation="vertical")

    pad.hist(x=xData, bins=xBinning, weights=y2_ETA_0_weights+y2_ETA_1_weights+y2_ETA_2_weights+y2_ETA_3_weights+y2_ETA_4_weights+y2_ETA_5_weights+y2_ETA_6_weights+y2_ETA_7_weights+y2_ETA_8_weights,\
             label="$bg\_dip\_600\_800$", histtype="step", rwidth=1.0,\
             color=None, edgecolor="#829e8c", linewidth=1, linestyle="solid",\
             bottom=None, cumulative=False, normed=False, align="mid", orientation="vertical")

    pad.hist(x=xData, bins=xBinning, weights=y2_ETA_0_weights+y2_ETA_1_weights+y2_ETA_2_weights+y2_ETA_3_weights+y2_ETA_4_weights+y2_ETA_5_weights+y2_ETA_6_weights+y2_ETA_7_weights,\
             label="$bg\_dip\_400\_600$", histtype="step", rwidth=1.0,\
             color=None, edgecolor="#adbcc6", linewidth=1, linestyle="solid",\
             bottom=None, cumulative=False, normed=False, align="mid", orientation="vertical")

    pad.hist(x=xData, bins=xBinning, weights=y2_ETA_0_weights+y2_ETA_1_weights+y2_ETA_2_weights+y2_ETA_3_weights+y2_ETA_4_weights+y2_ETA_5_weights+y2_ETA_6_weights,\
             label="$bg\_dip\_200\_400$", histtype="step", rwidth=1.0,\
             color=None, edgecolor="#7a8e99", linewidth=1, linestyle="solid",\
             bottom=None, cumulative=False, normed=False, align="mid", orientation="vertical")

    pad.hist(x=xData, bins=xBinning, weights=y2_ETA_0_weights+y2_ETA_1_weights+y2_ETA_2_weights+y2_ETA_3_weights+y2_ETA_4_weights+y2_ETA_5_weights,\
             label="$bg\_dip\_100\_200$", histtype="step", rwidth=1.0,\
             color=None, edgecolor="#758991", linewidth=1, linestyle="solid",\
             bottom=None, cumulative=False, normed=False, align="mid", orientation="vertical")

    pad.hist(x=xData, bins=xBinning, weights=y2_ETA_0_weights+y2_ETA_1_weights+y2_ETA_2_weights+y2_ETA_3_weights+y2_ETA_4_weights,\
             label="$bg\_dip\_0\_100$", histtype="step", rwidth=1.0,\
             color=None, edgecolor="#688296", linewidth=1, linestyle="solid",\
             bottom=None, cumulative=False, normed=False, align="mid", orientation="vertical")

    pad.hist(x=xData, bins=xBinning, weights=y2_ETA_0_weights+y2_ETA_1_weights+y2_ETA_2_weights+y2_ETA_3_weights,\
             label="$signal\_2pt4TeVL$", histtype="step", rwidth=1.0,\
             color=None, edgecolor="#6d7a84", linewidth=1, linestyle="solid",\
             bottom=None, cumulative=False, normed=False, align="mid", orientation="vertical")

    pad.hist(x=xData, bins=xBinning, weights=y2_ETA_0_weights+y2_ETA_1_weights+y2_ETA_2_weights,\
             label="$signal\_2pt2TeVL$", histtype="step", rwidth=1.0,\
             color=None, edgecolor="#7c99d1", linewidth=1, linestyle="solid",\
             bottom=None, cumulative=False, normed=False, align="mid", orientation="vertical")

    pad.hist(x=xData, bins=xBinning, weights=y2_ETA_0_weights+y2_ETA_1_weights,\
             label="$signal\_2TeVL$", histtype="step", rwidth=1.0,\
             color=None, edgecolor="#7f7f9b", linewidth=1, linestyle="solid",\
             bottom=None, cumulative=False, normed=False, align="mid", orientation="vertical")

    pad.hist(x=xData, bins=xBinning, weights=y2_ETA_0_weights,\
             label="$signal\_1pt8TeVL$", histtype="step", rwidth=1.0,\
             color=None, edgecolor="#aaa5bf", linewidth=1, linestyle="solid",\
             bottom=None, cumulative=False, normed=False, align="mid", orientation="vertical")


    # Axis
    plt.rc('text',usetex=False)
    plt.xlabel(r"\eta [ j_{1} ] ",\
               fontsize=16,color="black")
    plt.ylabel(r"$\mathrm{Events}$ $(\mathcal{L}_{\mathrm{int}} = 3000.0\ \mathrm{fb}^{-1})$ ",\
               fontsize=16,color="black")

    # Boundary of y-axis
    ymax=(y2_ETA_0_weights+y2_ETA_1_weights+y2_ETA_2_weights+y2_ETA_3_weights+y2_ETA_4_weights+y2_ETA_5_weights+y2_ETA_6_weights+y2_ETA_7_weights+y2_ETA_8_weights+y2_ETA_9_weights+y2_ETA_10_weights+y2_ETA_11_weights+y2_ETA_12_weights+y2_ETA_13_weights+y2_ETA_14_weights+y2_ETA_15_weights+y2_ETA_16_weights+y2_ETA_17_weights+y2_ETA_18_weights+y2_ETA_19_weights).max()*1.1
    ymin=0 # linear scale
    #ymin=min([x for x in (y2_ETA_0_weights+y2_ETA_1_weights+y2_ETA_2_weights+y2_ETA_3_weights+y2_ETA_4_weights+y2_ETA_5_weights+y2_ETA_6_weights+y2_ETA_7_weights+y2_ETA_8_weights+y2_ETA_9_weights+y2_ETA_10_weights+y2_ETA_11_weights+y2_ETA_12_weights+y2_ETA_13_weights+y2_ETA_14_weights+y2_ETA_15_weights+y2_ETA_16_weights+y2_ETA_17_weights+y2_ETA_18_weights+y2_ETA_19_weights) if x])/100. # log scale
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
    plt.savefig('../../HTML/MadAnalysis5job_0/selection_1.png')
    plt.savefig('../../PDF/MadAnalysis5job_0/selection_1.png')
    plt.savefig('../../DVI/MadAnalysis5job_0/selection_1.eps')

# Running!
if __name__ == '__main__':
    selection_1()
