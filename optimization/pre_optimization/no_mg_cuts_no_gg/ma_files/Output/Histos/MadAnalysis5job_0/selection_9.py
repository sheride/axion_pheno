def selection_9():

    # Library import
    import numpy
    import matplotlib
    import matplotlib.pyplot   as plt
    import matplotlib.gridspec as gridspec

    # Library version
    matplotlib_version = matplotlib.__version__
    numpy_version      = numpy.__version__

    # Histo binning
    xBinning = numpy.linspace(0.0,4000.0,401,endpoint=True)

    # Creating data sequence: middle of each bin
    xData = numpy.array([5.0,15.0,25.0,35.0,45.0,55.0,65.0,75.0,85.0,95.0,105.0,115.0,125.0,135.0,145.0,155.0,165.0,175.0,185.0,195.0,205.0,215.0,225.0,235.0,245.0,255.0,265.0,275.0,285.0,295.0,305.0,315.0,325.0,335.0,345.0,355.0,365.0,375.0,385.0,395.0,405.0,415.0,425.0,435.0,445.0,455.0,465.0,475.0,485.0,495.0,505.0,515.0,525.0,535.0,545.0,555.0,565.0,575.0,585.0,595.0,605.0,615.0,625.0,635.0,645.0,655.0,665.0,675.0,685.0,695.0,705.0,715.0,725.0,735.0,745.0,755.0,765.0,775.0,785.0,795.0,805.0,815.0,825.0,835.0,845.0,855.0,865.0,875.0,885.0,895.0,905.0,915.0,925.0,935.0,945.0,955.0,965.0,975.0,985.0,995.0,1005.0,1015.0,1025.0,1035.0,1045.0,1055.0,1065.0,1075.0,1085.0,1095.0,1105.0,1115.0,1125.0,1135.0,1145.0,1155.0,1165.0,1175.0,1185.0,1195.0,1205.0,1215.0,1225.0,1235.0,1245.0,1255.0,1265.0,1275.0,1285.0,1295.0,1305.0,1315.0,1325.0,1335.0,1345.0,1355.0,1365.0,1375.0,1385.0,1395.0,1405.0,1415.0,1425.0,1435.0,1445.0,1455.0,1465.0,1475.0,1485.0,1495.0,1505.0,1515.0,1525.0,1535.0,1545.0,1555.0,1565.0,1575.0,1585.0,1595.0,1605.0,1615.0,1625.0,1635.0,1645.0,1655.0,1665.0,1675.0,1685.0,1695.0,1705.0,1715.0,1725.0,1735.0,1745.0,1755.0,1765.0,1775.0,1785.0,1795.0,1805.0,1815.0,1825.0,1835.0,1845.0,1855.0,1865.0,1875.0,1885.0,1895.0,1905.0,1915.0,1925.0,1935.0,1945.0,1955.0,1965.0,1975.0,1985.0,1995.0,2005.0,2015.0,2025.0,2035.0,2045.0,2055.0,2065.0,2075.0,2085.0,2095.0,2105.0,2115.0,2125.0,2135.0,2145.0,2155.0,2165.0,2175.0,2185.0,2195.0,2205.0,2215.0,2225.0,2235.0,2245.0,2255.0,2265.0,2275.0,2285.0,2295.0,2305.0,2315.0,2325.0,2335.0,2345.0,2355.0,2365.0,2375.0,2385.0,2395.0,2405.0,2415.0,2425.0,2435.0,2445.0,2455.0,2465.0,2475.0,2485.0,2495.0,2505.0,2515.0,2525.0,2535.0,2545.0,2555.0,2565.0,2575.0,2585.0,2595.0,2605.0,2615.0,2625.0,2635.0,2645.0,2655.0,2665.0,2675.0,2685.0,2695.0,2705.0,2715.0,2725.0,2735.0,2745.0,2755.0,2765.0,2775.0,2785.0,2795.0,2805.0,2815.0,2825.0,2835.0,2845.0,2855.0,2865.0,2875.0,2885.0,2895.0,2905.0,2915.0,2925.0,2935.0,2945.0,2955.0,2965.0,2975.0,2985.0,2995.0,3005.0,3015.0,3025.0,3035.0,3045.0,3055.0,3065.0,3075.0,3085.0,3095.0,3105.0,3115.0,3125.0,3135.0,3145.0,3155.0,3165.0,3175.0,3185.0,3195.0,3205.0,3215.0,3225.0,3235.0,3245.0,3255.0,3265.0,3275.0,3285.0,3295.0,3305.0,3315.0,3325.0,3335.0,3345.0,3355.0,3365.0,3375.0,3385.0,3395.0,3405.0,3415.0,3425.0,3435.0,3445.0,3455.0,3465.0,3475.0,3485.0,3495.0,3505.0,3515.0,3525.0,3535.0,3545.0,3555.0,3565.0,3575.0,3585.0,3595.0,3605.0,3615.0,3625.0,3635.0,3645.0,3655.0,3665.0,3675.0,3685.0,3695.0,3705.0,3715.0,3725.0,3735.0,3745.0,3755.0,3765.0,3775.0,3785.0,3795.0,3805.0,3815.0,3825.0,3835.0,3845.0,3855.0,3865.0,3875.0,3885.0,3895.0,3905.0,3915.0,3925.0,3935.0,3945.0,3955.0,3965.0,3975.0,3985.0,3995.0])

    # Creating weights for histo: y10_M_0
    y10_M_0_weights = numpy.array([1.66959108742,4.48636474154,6.97784175421,8.76824707494,10.5330766045,11.8681225117,12.9736778599,13.8860836177,14.5435989138,14.9708641321,16.2201963609,16.3659879647,16.909583458,17.2622479549,17.4603064343,17.6949297405,16.7955597212,17.3090502937,17.4088350545,17.2580945871,16.6893350417,17.2439555478,16.8001288255,17.401539678,17.1973290976,17.3576115177,17.64803546,17.4852906004,17.0861715443,16.8701084755,17.1717493089,17.2856930964,17.337068537,17.4574762279,16.9841881768,17.1511663535,16.9928786692,16.8813413566,16.909403572,16.3432303874,16.5237439859,16.6428525002,16.4732719728,15.8489676291,16.3990310234,16.3479673853,15.782893504,15.6468956934,15.678875426,15.5580200188,15.9090535494,15.3955070123,15.5045698931,15.620864191,15.2516661722,15.205047717,15.0751940125,14.4045350463,14.7572355204,14.6017020906,14.8318762165,14.3292947302,14.2253206244,14.0975136228,14.1231453785,13.6398676585,13.591654214,13.8468045111,13.3592015322,13.6007364581,13.1712566433,13.3294803681,12.8458708583,12.8642392173,12.7602171418,12.1796770623,12.7737685536,12.3766442333,12.4487825153,11.8682904053,12.0657732495,11.875689716,11.8011969262,11.7937696333,11.7424421624,11.4806081011,11.4362961841,11.2505419069,11.3111275104,11.2204489784,11.1718197974,10.8121477416,10.8330345045,10.6934989359,10.5727674502,10.4540426926,10.4774238747,10.3191761651,10.1405533682,10.0130461766,9.93852540458,9.9086523368,9.68301133803,9.63892327908,9.76906080371,9.39072057892,9.3465085985,9.32098477437,9.26083089722,8.92822568761,9.40435193997,9.21190190624,8.84744088543,8.68464405882,8.93089199782,8.46876487344,8.60579802792,8.51974856225,8.30589609243,8.07419493432,8.18112716543,8.1137338763,8.03936101052,7.85325495626,7.71617782964,7.63754366448,7.63264277045,7.48882191771,7.43278543114,7.44922301373,7.27747985691,7.23114522174,7.07087079654,7.08496586372,7.1687527633,6.9384387261,6.85272904508,6.9686315912,6.76199055111,6.63198894035,6.57864674626,6.50898289611,6.47178247208,6.33259868058,6.33460141134,6.03977226094,6.15616649545,5.87740716072,6.00498630673,5.88439473231,5.66364663264,5.83992691403,6.06519215094,5.77981700902,5.67061021942,5.5034601517,5.58466069041,5.47293549687,5.51014391583,5.48723843231,5.48952898066,5.31049444479,5.56616841,5.10827460273,4.94405068055,5.16895614547,4.81599583601,4.82296741774,4.96249898883,4.91832698308,4.61611451191,4.72802358891,4.55588868036,4.71390853441,4.64635934408,4.53243954138,4.38633613523,4.45388132809,4.38409355647,4.39806470218,4.27038961697,4.10998327538,4.21711138235,4.18443209303,4.09838262735,4.13797753386,4.13579091964,3.91024625982,3.88955417354,3.72928694378,3.74998702499,3.80127292227,3.7525521993,3.87769169145,3.62018888528,3.55974799003,3.56915322941,3.52694318026,3.34394915374,3.46482814601,3.36237067899,3.33242085986,3.44783251708,3.28120092078,3.34376007357,3.36681346335,3.0605667489,3.05366512285,3.14669616391,2.97223433006,3.13950272279,2.87687236623,2.82569919751,2.85389292958,2.88630638737,2.82833512698,2.90717875939,2.87482766208,2.96557734896,2.64028070751,2.78883536017,2.68440834137,2.57984820694,2.71214436352,2.48447025324,2.53348758823,2.52183737162,2.48240196403,2.46376737381,2.52658156497,2.56613010086,2.45001608876,2.43816919679,2.28276848285,2.36161251501,2.44525350707,2.30581507695,2.23153095492,2.26853550308,2.11765352537,2.01104668804,2.25470147048,2.05502401717,2.0781197801,2.09452498321,1.98084143079,2.0990717017,1.93907470069,2.0969606396,1.96218565399,1.91119876722,1.9111224156,1.93432291216,1.79501120173,1.83898533288,1.69751978745,1.79721820303,1.69279198372,1.88783637326,1.74633565013,1.78106883778,1.75767086637,1.6859223374,1.60680687726,1.66017145716,1.65569989104,1.63014368743,1.63720281367,1.54191480297,1.5511037794,1.49530754058,1.51621309157,1.4304978141,1.50001695596,1.43051820118,1.41398747762,1.55113535939,1.33531053956,1.4234099061,1.32363353993,1.31426707597,1.29576680063,1.31199571546,1.2562274589,1.27490762025,1.28652225941,1.15633756468,1.26077057968,1.22850582764,1.1424523645,1.13079255397,1.20276454132,1.08673167779,1.16799377749,1.17727469565,1.09624364953,1.1774549814,1.01474889728,1.16339868965,1.16111493699,1.12153442136,0.942668978324,0.991575583492,1.07512743205,0.982377412884,0.97984541755,1.01715377317,1.04264761631,0.970522126237,1.0171565714,0.993840947805,0.926524410033,0.884719703997,0.905584880576,0.856872152536,0.833631681313,0.794171089681,0.849841008563,0.905573687669,0.852205909793,0.754646938331,0.898608501894,0.833692442805,0.685067834473,0.787160332787,0.812832462933,0.747704937862,0.750013474814,0.768724816398,0.752388369711,0.752393566418,0.791811385157,0.764026194176,0.731537584012,0.766365911367,0.701268367295,0.643240742623,0.691968661036,0.666387673128,0.715269094257,0.673404426222,0.610773718779,0.58286980304,0.552675338949,0.652591216709,0.594470451065,0.606002742412,0.596747408031,0.640806685221,0.617728511141,0.587441705572,0.538709389946,0.543445588354,0.575888227652,0.552632166309,0.545766117706,0.568857483425,0.564225219148,0.434210017001,0.541050306377,0.452861396586,0.506176008157,0.473702188619,0.452784245481,0.501585317532,0.422719299307,0.471343683335,0.499290771713,0.41567536344,0.404111891854,0.438842281278,0.429551369445,0.401657847119,0.397124080419,0.482959121986,0.448148383484,0.424919504915,0.390130472656,0.415628193335,0.424940691488,0.369243310011,0.320491686622,0.339016386491,0.366863738078,0.32740146751,0.315836037165,0.33202433774,0.366912627094,0.373954724126,0.31816216297,0.383149736736,0.378468823291,0.318077896375,0.292544198497,0.239176340672,0.348304380174,0.376101123834,0.318087570244,0.294925449366,0.255460300622])

    # Creating a new Canvas
    fig   = plt.figure(figsize=(8,6),dpi=80)
    frame = gridspec.GridSpec(1,1)
    pad   = fig.add_subplot(frame[0])

    # Creating a new Stack
    pad.hist(x=xData, bins=xBinning, weights=y10_M_0_weights,\
             label="$signal$", histtype="stepfilled", rwidth=1.0,\
             color="#5954d8", edgecolor="#5954d8", linewidth=1, linestyle="solid",\
             bottom=None, cumulative=False, normed=False, align="mid", orientation="vertical")


    # Axis
    plt.rc('text',usetex=False)
    plt.xlabel(r"M [ a_{1} , a_{2} ]   ( GeV ) ",\
               fontsize=16,color="black")
    plt.ylabel(r"$\mathrm{Events}$ $(\mathcal{L}_{\mathrm{int}} = 40.0\ \mathrm{fb}^{-1})$ ",\
               fontsize=16,color="black")

    # Boundary of y-axis
    ymax=(y10_M_0_weights).max()*1.1
    ymin=0 # linear scale
    #ymin=min([x for x in (y10_M_0_weights) if x])/100. # log scale
    plt.gca().set_ylim(ymin,ymax)

    # Log/Linear scale for X-axis
    plt.gca().set_xscale("linear")
    #plt.gca().set_xscale("log",nonposx="clip")

    # Log/Linear scale for Y-axis
    plt.gca().set_yscale("linear")
    #plt.gca().set_yscale("log",nonposy="clip")

    # Saving the image
    plt.savefig('../../HTML/MadAnalysis5job_0/selection_9.png')
    plt.savefig('../../PDF/MadAnalysis5job_0/selection_9.png')
    plt.savefig('../../DVI/MadAnalysis5job_0/selection_9.eps')

# Running!
if __name__ == '__main__':
    selection_9()