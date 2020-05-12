def selection_13():

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

    # Creating weights for histo: y14_THT_0
    y14_THT_0_weights = numpy.array([0.0,0.0,0.0,0.642771036877,2.5055794049,3.38580743374,3.82796824637,4.17596434149,4.28241224824,4.50758805096,4.84739575326,5.07257155599,5.0766635524,5.41237925829,5.45741521883,5.66621103591,6.07971467364,5.82588289602,6.29260648713,6.13293862701,6.28032649789,6.37858241181,6.65288617149,6.91900193835,7.58633735371,7.02954184151,7.13598974825,7.34888156174,7.41438550436,7.61908932502,7.9548050309,8.37649666146,8.16769684439,8.32736470451,8.53207252516,8.29870872961,8.71221236735,8.6958323817,8.92510418083,9.10933601943,8.87597222388,9.12162000867,9.75210745631,9.89539933077,9.88311934153,10.5463587605,10.4849508143,10.8820744664,10.9393904161,11.3569900503,11.6476697956,11.3569900503,12.3313811966,12.3968851393,12.2208412935,12.3682291644,12.0366054549,12.0407014513,12.2945332289,11.8032456593,11.6435737992,11.7459257096,11.0294623372,11.3856460252,11.1891301974,10.7305945991,10.6036787103,10.5463587605,10.1164831371,10.0632591837,9.4696157038,9.6866035137,9.30175985085,8.6958323817,8.60166846419,8.8227522705,8.04078095558,8.07353292688,7.96299302373,7.84426512774])

    # Creating weights for histo: y14_THT_1
    y14_THT_1_weights = numpy.array([0.0,0.0,0.0,1.89440891827,10.825703072,22.3069398707,31.069039882,36.7685512411,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0])

    # Creating weights for histo: y14_THT_2
    y14_THT_2_weights = numpy.array([0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,60.4829361707,62.829799842,64.0589736153,63.8533193352,60.5210753912,57.6903849235,56.3238190503,52.0473091612,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0])

    # Creating weights for histo: y14_THT_3
    y14_THT_3_weights = numpy.array([0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,58.4035809794,55.2883046148,52.1948440818,47.1996280466,43.8209366885,41.7480670665,38.4197430603,35.4605981737,32.7814434376,30.9667400094,27.0722606438,25.9678514394,23.3214976387,21.6210774799,20.6762407234,18.7504674939,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0])

    # Creating weights for histo: y14_THT_4
    y14_THT_4_weights = numpy.array([0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,17.784308742,16.4410553598,15.5172424842,14.1720811514,13.4065199566,12.2041743424,11.2925266564,10.5828251264,9.8171516992,9.08892781622,8.71280901294,8.05962450882,7.52382707,7.09827791471,6.56945090908,6.21900927375,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0])

    # Creating weights for histo: y14_THT_5
    y14_THT_5_weights = numpy.array([0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,5.79698835106,5.46025691729,5.13581252796,4.78689807554,4.35060997409,4.05897771479,3.72238311493,3.40483403409,3.06955496018,2.85984860011,2.6395204082,2.39321938087,2.30047800184,2.05163154381,1.90339521449,1.73806584995,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0])

    # Creating weights for histo: y14_THT_6
    y14_THT_6_weights = numpy.array([0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,1.60707061909,1.4888657773,1.37919110968,1.28177538099,1.19206809869,1.0937926548,1.02086881258,0.939995103947,0.833644235237,0.817428207188,0.744061511676,0.705464197967,0.634769017451,0.593764001351,0.543028808608,0.507370421309])

    # Creating weights for histo: y14_THT_7
    y14_THT_7_weights = numpy.array([0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0])

    # Creating weights for histo: y14_THT_8
    y14_THT_8_weights = numpy.array([0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0])

    # Creating weights for histo: y14_THT_9
    y14_THT_9_weights = numpy.array([0.0,0.0,0.0,0.0,2.59864517509,31.2893900254,41.7145995778,41.6936382986,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0])

    # Creating weights for histo: y14_THT_10
    y14_THT_10_weights = numpy.array([0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,62.1460220858,55.8298668845,69.5043719458,53.7213523348,60.0186152088,70.5756169243,58.9814995466,65.295615454,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0])

    # Creating weights for histo: y14_THT_11
    y14_THT_11_weights = numpy.array([0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,61.0448790667,64.0286740996,64.0345914308,55.9664640706,57.5865832373,54.1326677698,55.7431424551,47.2146544144,50.2122053211,47.9031013148,43.5320763638,43.3109833535,44.4436527585,43.0784399232,42.8505074002,39.1530975974,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0])

    # Creating weights for histo: y14_THT_12
    y14_THT_12_weights = numpy.array([0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,40.6526136917,41.5366103733,39.4034076579,36.2478649731,36.2720827427,34.1701880828,35.1124612973,33.7278819705,32.5914010945,30.7647349427,29.9358986076,30.3218055931,27.0275695304,27.8840591345,27.4409951349,28.3845263653,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0])

    # Creating weights for histo: y14_THT_13
    y14_THT_13_weights = numpy.array([0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,25.3258303924,25.3773196564,24.3882828043,23.7628869828,21.423739126,18.2890715213,17.9777268345,16.5748886389,14.8607664393,14.2549468541,12.6420979988,12.0475107799,10.6861613406,9.51871737473,8.52961983998,8.16562684985,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0])

    # Creating weights for histo: y14_THT_14
    y14_THT_14_weights = numpy.array([0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,7.57333526862,7.18605402624,6.49006660841,5.90721143577,5.6642800899,5.20545294609,5.06967116758,4.52958348473,4.11646322999,3.98360161384,3.53079754535,3.39505962699,3.04135640433,2.90562848916,2.56045337174,2.44166816931])

    # Creating weights for histo: y14_THT_15
    y14_THT_15_weights = numpy.array([0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0])

    # Creating weights for histo: y14_THT_16
    y14_THT_16_weights = numpy.array([0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0])

    # Creating a new Canvas
    fig   = plt.figure(figsize=(12,6),dpi=80)
    frame = gridspec.GridSpec(1,1,right=0.7)
    pad   = fig.add_subplot(frame[0])

    # Creating a new Stack
    pad.hist(x=xData, bins=xBinning, weights=y14_THT_0_weights+y14_THT_1_weights+y14_THT_2_weights+y14_THT_3_weights+y14_THT_4_weights+y14_THT_5_weights+y14_THT_6_weights+y14_THT_7_weights+y14_THT_8_weights+y14_THT_9_weights+y14_THT_10_weights+y14_THT_11_weights+y14_THT_12_weights+y14_THT_13_weights+y14_THT_14_weights+y14_THT_15_weights+y14_THT_16_weights,\
             label="$bg\_dip\_1600\_inf$", histtype="step", rwidth=1.0,\
             color=None, edgecolor="#e5e5e5", linewidth=4, linestyle="dashdot",\
             bottom=None, cumulative=False, normed=False, align="mid", orientation="vertical")

    pad.hist(x=xData, bins=xBinning, weights=y14_THT_0_weights+y14_THT_1_weights+y14_THT_2_weights+y14_THT_3_weights+y14_THT_4_weights+y14_THT_5_weights+y14_THT_6_weights+y14_THT_7_weights+y14_THT_8_weights+y14_THT_9_weights+y14_THT_10_weights+y14_THT_11_weights+y14_THT_12_weights+y14_THT_13_weights+y14_THT_14_weights+y14_THT_15_weights,\
             label="$bg\_dip\_1200\_1600$", histtype="step", rwidth=1.0,\
             color=None, edgecolor="#f2f2f2", linewidth=4, linestyle="dashdot",\
             bottom=None, cumulative=False, normed=False, align="mid", orientation="vertical")

    pad.hist(x=xData, bins=xBinning, weights=y14_THT_0_weights+y14_THT_1_weights+y14_THT_2_weights+y14_THT_3_weights+y14_THT_4_weights+y14_THT_5_weights+y14_THT_6_weights+y14_THT_7_weights+y14_THT_8_weights+y14_THT_9_weights+y14_THT_10_weights+y14_THT_11_weights+y14_THT_12_weights+y14_THT_13_weights+y14_THT_14_weights,\
             label="$bg\_dip\_800\_1200$", histtype="step", rwidth=1.0,\
             color=None, edgecolor="#ccc6aa", linewidth=4, linestyle="dashdot",\
             bottom=None, cumulative=False, normed=False, align="mid", orientation="vertical")

    pad.hist(x=xData, bins=xBinning, weights=y14_THT_0_weights+y14_THT_1_weights+y14_THT_2_weights+y14_THT_3_weights+y14_THT_4_weights+y14_THT_5_weights+y14_THT_6_weights+y14_THT_7_weights+y14_THT_8_weights+y14_THT_9_weights+y14_THT_10_weights+y14_THT_11_weights+y14_THT_12_weights+y14_THT_13_weights,\
             label="$bg\_dip\_600\_800$", histtype="step", rwidth=1.0,\
             color=None, edgecolor="#ccc6aa", linewidth=4, linestyle="dashdot",\
             bottom=None, cumulative=False, normed=False, align="mid", orientation="vertical")

    pad.hist(x=xData, bins=xBinning, weights=y14_THT_0_weights+y14_THT_1_weights+y14_THT_2_weights+y14_THT_3_weights+y14_THT_4_weights+y14_THT_5_weights+y14_THT_6_weights+y14_THT_7_weights+y14_THT_8_weights+y14_THT_9_weights+y14_THT_10_weights+y14_THT_11_weights+y14_THT_12_weights,\
             label="$bg\_dip\_400\_600$", histtype="step", rwidth=1.0,\
             color=None, edgecolor="#c1bfa8", linewidth=4, linestyle="dashdot",\
             bottom=None, cumulative=False, normed=False, align="mid", orientation="vertical")

    pad.hist(x=xData, bins=xBinning, weights=y14_THT_0_weights+y14_THT_1_weights+y14_THT_2_weights+y14_THT_3_weights+y14_THT_4_weights+y14_THT_5_weights+y14_THT_6_weights+y14_THT_7_weights+y14_THT_8_weights+y14_THT_9_weights+y14_THT_10_weights+y14_THT_11_weights,\
             label="$bg\_dip\_200\_400$", histtype="step", rwidth=1.0,\
             color=None, edgecolor="#bab5a3", linewidth=4, linestyle="dashdot",\
             bottom=None, cumulative=False, normed=False, align="mid", orientation="vertical")

    pad.hist(x=xData, bins=xBinning, weights=y14_THT_0_weights+y14_THT_1_weights+y14_THT_2_weights+y14_THT_3_weights+y14_THT_4_weights+y14_THT_5_weights+y14_THT_6_weights+y14_THT_7_weights+y14_THT_8_weights+y14_THT_9_weights+y14_THT_10_weights,\
             label="$bg\_dip\_100\_200$", histtype="step", rwidth=1.0,\
             color=None, edgecolor="#b2a596", linewidth=4, linestyle="dashdot",\
             bottom=None, cumulative=False, normed=False, align="mid", orientation="vertical")

    pad.hist(x=xData, bins=xBinning, weights=y14_THT_0_weights+y14_THT_1_weights+y14_THT_2_weights+y14_THT_3_weights+y14_THT_4_weights+y14_THT_5_weights+y14_THT_6_weights+y14_THT_7_weights+y14_THT_8_weights+y14_THT_9_weights,\
             label="$bg\_dip\_0\_100$", histtype="step", rwidth=1.0,\
             color=None, edgecolor="#b7a39b", linewidth=4, linestyle="dashdot",\
             bottom=None, cumulative=False, normed=False, align="mid", orientation="vertical")

    pad.hist(x=xData, bins=xBinning, weights=y14_THT_0_weights+y14_THT_1_weights+y14_THT_2_weights+y14_THT_3_weights+y14_THT_4_weights+y14_THT_5_weights+y14_THT_6_weights+y14_THT_7_weights+y14_THT_8_weights,\
             label="$bg\_vbf\_1600\_inf$", histtype="step", rwidth=1.0,\
             color=None, edgecolor="#ad998c", linewidth=4, linestyle="dashdot",\
             bottom=None, cumulative=False, normed=False, align="mid", orientation="vertical")

    pad.hist(x=xData, bins=xBinning, weights=y14_THT_0_weights+y14_THT_1_weights+y14_THT_2_weights+y14_THT_3_weights+y14_THT_4_weights+y14_THT_5_weights+y14_THT_6_weights+y14_THT_7_weights,\
             label="$bg\_vbf\_1200\_1600$", histtype="step", rwidth=1.0,\
             color=None, edgecolor="#9b8e82", linewidth=4, linestyle="dashdot",\
             bottom=None, cumulative=False, normed=False, align="mid", orientation="vertical")

    pad.hist(x=xData, bins=xBinning, weights=y14_THT_0_weights+y14_THT_1_weights+y14_THT_2_weights+y14_THT_3_weights+y14_THT_4_weights+y14_THT_5_weights+y14_THT_6_weights,\
             label="$bg\_vbf\_800\_1200$", histtype="step", rwidth=1.0,\
             color=None, edgecolor="#876656", linewidth=4, linestyle="dashdot",\
             bottom=None, cumulative=False, normed=False, align="mid", orientation="vertical")

    pad.hist(x=xData, bins=xBinning, weights=y14_THT_0_weights+y14_THT_1_weights+y14_THT_2_weights+y14_THT_3_weights+y14_THT_4_weights+y14_THT_5_weights,\
             label="$bg\_vbf\_600\_800$", histtype="step", rwidth=1.0,\
             color=None, edgecolor="#afcec6", linewidth=4, linestyle="dashdot",\
             bottom=None, cumulative=False, normed=False, align="mid", orientation="vertical")

    pad.hist(x=xData, bins=xBinning, weights=y14_THT_0_weights+y14_THT_1_weights+y14_THT_2_weights+y14_THT_3_weights+y14_THT_4_weights,\
             label="$bg\_vbf\_400\_600$", histtype="step", rwidth=1.0,\
             color=None, edgecolor="#84c1a3", linewidth=4, linestyle="dashdot",\
             bottom=None, cumulative=False, normed=False, align="mid", orientation="vertical")

    pad.hist(x=xData, bins=xBinning, weights=y14_THT_0_weights+y14_THT_1_weights+y14_THT_2_weights+y14_THT_3_weights,\
             label="$bg\_vbf\_200\_400$", histtype="step", rwidth=1.0,\
             color=None, edgecolor="#89a8a0", linewidth=4, linestyle="dashdot",\
             bottom=None, cumulative=False, normed=False, align="mid", orientation="vertical")

    pad.hist(x=xData, bins=xBinning, weights=y14_THT_0_weights+y14_THT_1_weights+y14_THT_2_weights,\
             label="$bg\_vbf\_100\_200$", histtype="step", rwidth=1.0,\
             color=None, edgecolor="#829e8c", linewidth=4, linestyle="dashdot",\
             bottom=None, cumulative=False, normed=False, align="mid", orientation="vertical")

    pad.hist(x=xData, bins=xBinning, weights=y14_THT_0_weights+y14_THT_1_weights,\
             label="$bg\_vbf\_0\_100$", histtype="step", rwidth=1.0,\
             color=None, edgecolor="#adbcc6", linewidth=4, linestyle="dashdot",\
             bottom=None, cumulative=False, normed=False, align="mid", orientation="vertical")

    pad.hist(x=xData, bins=xBinning, weights=y14_THT_0_weights,\
             label="$signal$", histtype="step", rwidth=1.0,\
             color=None, edgecolor="#7a8e99", linewidth=3, linestyle="dashed",\
             bottom=None, cumulative=False, normed=False, align="mid", orientation="vertical")


    # Axis
    plt.rc('text',usetex=False)
    plt.xlabel(r"THT",\
               fontsize=16,color="black")
    plt.ylabel(r"$\mathrm{Events}$ $(\mathcal{L}_{\mathrm{int}} = 40.0\ \mathrm{fb}^{-1})$ ",\
               fontsize=16,color="black")

    # Boundary of y-axis
    ymax=(y14_THT_0_weights+y14_THT_1_weights+y14_THT_2_weights+y14_THT_3_weights+y14_THT_4_weights+y14_THT_5_weights+y14_THT_6_weights+y14_THT_7_weights+y14_THT_8_weights+y14_THT_9_weights+y14_THT_10_weights+y14_THT_11_weights+y14_THT_12_weights+y14_THT_13_weights+y14_THT_14_weights+y14_THT_15_weights+y14_THT_16_weights).max()*1.1
    ymin=0 # linear scale
    #ymin=min([x for x in (y14_THT_0_weights+y14_THT_1_weights+y14_THT_2_weights+y14_THT_3_weights+y14_THT_4_weights+y14_THT_5_weights+y14_THT_6_weights+y14_THT_7_weights+y14_THT_8_weights+y14_THT_9_weights+y14_THT_10_weights+y14_THT_11_weights+y14_THT_12_weights+y14_THT_13_weights+y14_THT_14_weights+y14_THT_15_weights+y14_THT_16_weights) if x])/100. # log scale
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
    plt.savefig('../../HTML/MadAnalysis5job_0/selection_13.png')
    plt.savefig('../../PDF/MadAnalysis5job_0/selection_13.png')
    plt.savefig('../../DVI/MadAnalysis5job_0/selection_13.eps')

# Running!
if __name__ == '__main__':
    selection_13()
