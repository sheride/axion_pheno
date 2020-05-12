def selection_3():

    # Library import
    import numpy
    import matplotlib
    import matplotlib.pyplot   as plt
    import matplotlib.gridspec as gridspec

    # Library version
    matplotlib_version = matplotlib.__version__
    numpy_version      = numpy.__version__

    # Histo binning
    xBinning = numpy.linspace(0.0,500.0,101,endpoint=True)

    # Creating data sequence: middle of each bin
    xData = numpy.array([2.5,7.5,12.5,17.5,22.5,27.5,32.5,37.5,42.5,47.5,52.5,57.5,62.5,67.5,72.5,77.5,82.5,87.5,92.5,97.5,102.5,107.5,112.5,117.5,122.5,127.5,132.5,137.5,142.5,147.5,152.5,157.5,162.5,167.5,172.5,177.5,182.5,187.5,192.5,197.5,202.5,207.5,212.5,217.5,222.5,227.5,232.5,237.5,242.5,247.5,252.5,257.5,262.5,267.5,272.5,277.5,282.5,287.5,292.5,297.5,302.5,307.5,312.5,317.5,322.5,327.5,332.5,337.5,342.5,347.5,352.5,357.5,362.5,367.5,372.5,377.5,382.5,387.5,392.5,397.5,402.5,407.5,412.5,417.5,422.5,427.5,432.5,437.5,442.5,447.5,452.5,457.5,462.5,467.5,472.5,477.5,482.5,487.5,492.5,497.5])

    # Creating weights for histo: y4_PT_0
    y4_PT_0_weights = numpy.array([0.0,0.0,0.0,0.0,15.4142267198,15.5002026457,14.6199754041,14.4193635769,14.1737197885,13.7929681166,13.6824282118,13.9485439825,13.4572524058,14.0345199085,13.7725001342,14.1204958344,13.7725001342,13.7929681166,13.9403559896,13.6783362153,13.7315561695,13.7520281518,13.960827972,13.1788566457,13.3958444587,13.6824282118,12.9168368714,13.0396567656,12.6056851395,13.3016805398,12.4869572418,12.7039410548,12.3190973864,12.1307695487,12.2617814358,12.2576854393,11.6967979225,11.2300703247,11.4143061659,11.2587303,11.1440983987,11.1154384234,10.6773708008,10.1697032382,10.3907870477,10.0305073582,10.0878233088,9.89130747808,9.47371183786,8.99470425055,9.1830320883,9.06430019059,8.90872832463,8.54026064208,8.47066070205,7.84016924525,8.13903698776,8.04078107241,8.00802910063,7.47170156271,7.32431768969,7.10323388016,6.82893011649,6.70201422584,6.41543047274,6.01011482195,6.22300663853,5.74399905122,5.46969528755,5.21586350624,4.94155974257,4.95383973199,4.60175203533,4.41751619406,4.13912043391,4.22100036337,3.93032061381,3.96307338559,3.72561639017,3.62735847483,3.4513126265,3.18929125225,3.25889079228,3.01733980039,2.9108934921,2.71847165788,2.68981328257,2.63249613196,2.38685114359,2.57108458487,2.23946407057,2.14120575523,2.04294783988,1.99381908221,1.90784315629,1.74407969738,1.78092646563,1.76045608327,1.7399857009,1.60897501378])

    # Creating weights for histo: y4_PT_1
    y4_PT_1_weights = numpy.array([0.0,0.0,0.0,0.0,21.0552752178,22.8793695245,22.8896352695,18.5043116952,12.8449783305,4.69107294659,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0])

    # Creating weights for histo: y4_PT_2
    y4_PT_2_weights = numpy.array([0.0,0.0,0.0,0.0,6.7468202307,11.3851199394,18.0427902536,26.5360480521,37.2782183802,48.5149920321,53.32355052,51.4867523323,47.7998092949,43.3928076501,38.0413664584,31.9372851022,26.4056350502,20.3303874422,12.7208811339,3.86515361722,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0])

    # Creating weights for histo: y4_PT_3
    y4_PT_3_weights = numpy.array([0.0,0.0,0.0,0.0,0.836003734826,1.17173067247,1.67766292907,2.49730113504,3.17929770319,4.36747231151,5.37362489602,6.68222532404,8.51487692901,10.2859038921,13.7675113125,16.8754911577,20.500359925,25.6374435346,31.1813984695,38.7225174936,40.1915109921,37.335355702,33.5367606139,32.0898429479,29.0863718978,27.6045042158,25.4398457394,22.0557351731,21.4571526704,18.6073999405,17.2485865404,15.6810318028,13.4543708685,12.1331887597,10.721078921,8.71269003879,7.45861293587,5.28547187973,3.20107575169,1.12187276622,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0])

    # Creating weights for histo: y4_PT_4
    y4_PT_4_weights = numpy.array([0.0,0.0,0.0,0.0,0.0483487925558,0.0700695282055,0.117408710229,0.141122532829,0.192428769162,0.252623891106,0.264502567474,0.341470018739,0.393734960198,0.478665941003,0.531907384438,0.5467076303,0.603968195858,0.703584865319,0.803280498284,0.880267109222,0.936506760843,1.02829121266,1.13877839095,1.23843955254,1.38358489512,1.48220429962,1.58490695903,1.8167381962,1.98155667461,2.313172529,2.52243784045,2.78396416522,3.2891714636,3.70664189122,4.33338083692,5.01417451007,5.82066445393,7.01727018402,8.21773991503,9.60676407286,9.91800854562,9.40667375946,8.81849986779,8.03106137247,7.56708464742,7.00083214689,6.42035018238,6.07104289554,5.56175234223,5.0990502565,4.70527890094,4.34801914747,3.97593710249,3.49643863764,3.0720603063,2.51650796185,2.15129453926,1.48125152677,0.916771496374,0.345416189807,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0])

    # Creating weights for histo: y4_PT_5
    y4_PT_5_weights = numpy.array([0.0,0.0,0.0,0.0,0.00806299400788,0.01184819598,0.0201700781403,0.0287279987909,0.0307591301047,0.0405862172544,0.0410833404414,0.0509194978387,0.0569767588265,0.0665492908975,0.0746331340718,0.0743601864355,0.0831760510045,0.0905013062009,0.10663130321,0.10209033796,0.100824544297,0.120231353299,0.126543877541,0.132089211673,0.137132421379,0.142922656198,0.154506406649,0.171142849155,0.17291272773,0.176963411489,0.201396025884,0.217791008557,0.225105581106,0.221050576277,0.242990813062,0.247036055472,0.259632976986,0.284366906048,0.310813339467,0.321638822019,0.356180501439,0.385174166061,0.406119836393,0.441910705361,0.472892382613,0.482947274213,0.565658169952,0.611282275594,0.656668322245,0.751173340565,0.803125014176,0.935455805713,1.03000443484,1.16356793184,1.3385408901,1.56336780215,1.85155001363,2.13681710274,2.51373570307,2.94477851537,3.06551403361,2.84285005753,2.68358699218,2.45090653402,2.22025977981,2.04940264146,1.91252912424,1.76229829707,1.6342393641,1.47772057879,1.32822993504,1.18533772639,1.05670865214,0.948286985276,0.846985882888,0.672520650448,0.539720142515,0.417439041289,0.240468187956,0.0723524889285,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0])

    # Creating weights for histo: y4_PT_6
    y4_PT_6_weights = numpy.array([0.0,0.0,0.0,0.0,0.00458240903485,0.00486145559811,0.0060120144649,0.0114668115132,0.0100133329913,0.00944485130611,0.0134564224363,0.0131676780855,0.0168692818952,0.0223226054316,0.0168916844741,0.0220606122192,0.0263485218097,0.0269023183595,0.0280369325082,0.0306323227613,0.024336628268,0.0231870590734,0.0377876424958,0.0326459257368,0.035485345153,0.0297689687552,0.0334997928854,0.0349339178183,0.0335086299581,0.035523952364,0.0349300990833,0.0423735333772,0.039774264409,0.0466441786867,0.0394972661672,0.0417901866162,0.04723772207,0.0429294992084,0.0460780462233,0.048401336612,0.0452564783752,0.0518360388353,0.043495691652,0.0589868600599,0.0526842578549,0.0566958889652,0.0567026167365,0.0581079112198,0.0552604444694,0.0627348285109,0.0630084278786,0.0695838796997,0.0652843339638,0.0767436379639,0.0755838321602,0.0790429962803,0.0898963909934,0.0978784168739,0.0941639673195,0.101923936758,0.108215352669,0.117389713577,0.122508218026,0.136263761375,0.144850916801,0.152321841988,0.166643197908,0.189826018385,0.195536126859,0.215312775662,0.235643740843,0.274568046809,0.291193839362,0.329627807756,0.363327444441,0.414585064883,0.498732690208,0.583198810029,0.686218583781,0.797955369943,0.809074786534,0.748150768175,0.710026797091,0.666768526791,0.601580820819,0.586923976033,0.542585063706,0.499298502777,0.485590143797,0.44545503892,0.412820749329,0.406532532359,0.392300546835,0.386869845804,0.338411997912,0.315790791395,0.277391111642,0.296619941915,0.256562711242,0.246511440817])

    # Creating weights for histo: y4_PT_7
    y4_PT_7_weights = numpy.array([0.0,0.0,0.0,0.0,0.000432150234573,0.00071280594608,0.000755552342501,0.000820813958841,0.00114314570954,0.00133914387564,0.00159792557575,0.00168453440669,0.001660941705,0.00142543964595,0.00207168018503,0.00215789842359,0.00181439002814,0.00174960701319,0.00226838451869,0.00233084116208,0.00198591414516,0.00215863267021,0.00187921746669,0.00198670706446,0.00191922091556,0.00192062403067,0.00237543449049,0.00239751217989,0.00235314893218,0.00226791136547,0.00207114626369,0.00217965425146,0.00220306087695,0.00174977381123,0.00172780592355,0.00205177506097,0.0018345478638,0.00211713390631,0.00205201561894,0.00196375179948,0.00235516391947,0.0020087608657,0.0024191330606,0.00192051087622,0.00183574101456,0.00213570255066,0.00181397009943,0.00203012903482,0.0022246272759,0.00209532946394,0.00209529258398,0.00187946682556,0.00241759541743,0.00244062402325,0.00192245713267,0.00237615323075,0.00239769574154,0.00205064854561,0.00235233463927,0.00245987704245,0.00235397747417,0.00228963492337,0.00248398815912,0.00289436705948,0.00272117077122,0.00265674649777,0.00272033426651,0.00295752106952,0.00313211251016,0.00276463297428,0.00317569122039,0.0030225593106,0.0030026026384,0.0032400949584,0.0035417349521,0.00373483049716,0.00386656490148,0.00433881497575,0.00397084761848,0.00424911702847,0.00358377937188,0.00434070088316,0.00479582063179,0.00462209503219,0.00455627686361,0.00520581690248,0.00559246983036,0.00524571013054,0.00528965596407,0.00635019809092,0.00671517146541,0.00662988654147,0.00770533152776,0.0078384514454,0.00753497541606,0.00788310135103,0.00967536297982,0.00939063287013,0.00980279164798,0.0115069520644])

    # Creating weights for histo: y4_PT_8
    y4_PT_8_weights = numpy.array([0.0,0.0,0.0,0.0,2.84546946001e-05,8.5161984217e-05,0.000198747593639,0.000255687606689,0.000141975254333,0.000368538718977,0.000170251671199,0.000283578923453,0.000254656019603,0.000170130185706,0.000227144307877,0.000170150235268,0.000312331777315,8.50537611377e-05,0.000283840904394,0.000198730068837,0.000198606207099,0.000227338714369,0.000226632672762,0.000282207384907,0.000227056683866,0.000198633682425,0.000283990162243,0.000340128192819,0.000397841079349,0.000142050922864,0.000255619735209,0.000197089569133,0.000255117605071,0.000169911571224,0.00017005058152,0.000227310199436,0.000227226288307,0.000198301305244,0.000198748781761,0.000448450628891,0.000255272357986,0.000141578867069,0.000282269315776,0.000198923287207,0.000113417742609,0.000255292259032,0.000112684775183,0.000113645995732,0.000141716317954,0.00011350731217,0.000198653583471,0.000141607337447,0.000170352958615,0.00011352831223,0.000170448602451,0.00019679684553,0.000197080361186,0.000168352903435,0.000195843823024,0.000141960595875,0.000256845431756,8.50760087255e-05,0.000227077773034,0.000170424840007,0.000255160971531,0.000170311077308,0.000228897530673,0.000198547543566,0.000141921194773,0.000198626999237,0.000141984536537,5.68093047578e-05,0.000283803775576,0.000198971851701,0.000284063380273,0.000170230879061,0.00011363926799,8.38753370019e-05,0.000170393057739,0.000142016407915,0.000141270415699,0.000113597030247,0.000170496127338,0.0001962121409,0.000113524124099,0.000170516028385,0.000227317179654,0.000227117723643,0.000226758613713,0.000255180278516,0.000170258205871,0.00016870622127,0.00019877521748,0.000340477649256,0.000169801966953,0.00022694470335,0.000255565824165,0.000340166509759,0.000226882326935,0.000255730824633])

    # Creating weights for histo: y4_PT_9
    y4_PT_9_weights = numpy.array([0.0,0.0,0.0,0.0,20.8422280792,23.4609530557,36.4960863614,18.2517719803,13.0355756078,5.20965799256,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0])

    # Creating weights for histo: y4_PT_10
    y4_PT_10_weights = numpy.array([0.0,0.0,0.0,0.0,11.5841529842,21.0620382692,12.6463905509,27.3811876619,38.9561753654,52.6740841954,46.3546962438,53.7307464088,53.6986948603,38.9689498121,42.1254309376,28.4434983354,18.9557397883,31.5932613332,15.7928406576,2.10507298057,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0])

    # Creating weights for histo: y4_PT_11
    y4_PT_11_weights = numpy.array([0.0,0.0,0.0,0.0,4.14755360048,8.293908365,7.60015121626,5.75851631985,5.52770581558,10.3679675833,7.13953692253,9.90588548403,8.98010746779,12.6700746038,9.44537493571,16.5837975556,21.8826640299,29.0291864773,38.2387864983,40.3075931245,44.913774486,43.0626103807,44.224866475,46.0633890089,40.7752928461,38.4669188338,37.3099153316,31.0970478674,33.8578594974,33.3988167547,34.0873558931,27.1835900428,24.8747895216,21.6472848847,24.6495390033,20.9581770677,13.1311346186,11.2873825472,6.90620194638,0.460963569978,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0])

    # Creating weights for histo: y4_PT_12
    y4_PT_12_weights = numpy.array([0.0,0.0,0.0,0.0,0.913463049855,1.21802908663,1.27382997893,0.886476877349,1.13502427351,1.38451152681,0.858567005699,1.05251920432,0.83090335123,1.13523163454,0.94179995443,1.3011343102,1.30153018126,1.1076545408,1.02416460288,1.16272716884,1.02433541605,1.52295329246,1.80016460038,1.6339556921,2.46496483978,2.38193271194,2.6576674862,2.8523379465,3.71088302348,4.12505340797,4.45768897285,5.75897370635,6.58996438774,7.69873806257,9.49746229244,12.5992640247,15.2027952775,18.0282874723,20.7402735464,26.3608347254,30.5995442926,26.4168837584,26.4419517452,24.7539213741,23.5941845899,25.0048782362,23.4553911953,22.5410059852,22.0411004698,19.9661359511,19.9364552393,18.1114742553,16.5597097055,15.6711849937,12.8784435312,11.6859560147,9.80307552166,7.67118866826,4.4867387531,1.2187792796,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0])

    # Creating weights for histo: y4_PT_13
    y4_PT_13_weights = numpy.array([0.0,0.0,0.0,0.0,0.201626733467,0.322553984664,0.191495697671,0.342840450699,0.221737644479,0.231907517197,0.191657599088,0.221840198225,0.161363040387,0.0806628299249,0.121055109625,0.110899618705,0.221905310752,0.1916375738,0.292442020178,0.171514586933,0.151262710031,0.232020326318,0.292300568827,0.25196994274,0.241825920848,0.302463463036,0.272349799435,0.352876639451,0.332633743588,0.372879413909,0.312673264965,0.524319984905,0.514165889687,0.554539600484,0.715988992339,0.635174212958,0.524210391967,0.776290595155,0.897310084041,0.91752288129,1.01854014186,1.26054210319,1.07875860939,1.36088093129,1.53272824141,2.03637272356,1.86517471822,2.23813053164,2.29874707761,2.73210340663,3.28627957848,4.34591949953,4.32560718267,4.86968636172,6.26071202615,7.44080830072,8.21786228411,10.4854833895,12.6834164935,14.4361389051,16.3717346715,15.5064237836,13.5806222034,12.7937679655,11.4832706582,11.3022299205,10.4148183969,9.44666248576,9.08369504314,7.54041286826,7.61171502914,6.20002326777,5.73576549247,5.38463481537,4.65788071381,3.59947386503,3.03473890509,2.16779868697,1.20991574849,0.47379806511,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0])

    # Creating weights for histo: y4_PT_14
    y4_PT_14_weights = numpy.array([0.0,0.0,0.0,0.0,0.107444861959,0.0764043032494,0.0990259062878,0.130164073066,0.0962005431923,0.10466555202,0.113183847082,0.0962129317608,0.0735640123136,0.0961943489081,0.0678941646363,0.121650240967,0.0792386307439,0.0678999741824,0.0792145461355,0.0735916365129,0.0820666870065,0.096186038564,0.110332668056,0.0961517583946,0.0877014465642,0.0820314449917,0.0820402554954,0.0876880576765,0.0990356401631,0.0763721776137,0.104656741516,0.0876859416167,0.0962179333568,0.115998475983,0.0905388134901,0.0792165467739,0.0848605015735,0.0594017239783,0.121623155401,0.10463681208,0.0990431810309,0.107484220672,0.130150568757,0.144278884714,0.152800257681,0.138687869884,0.127294772874,0.138652089236,0.127289848226,0.158387694446,0.169774404803,0.164103941544,0.246101298736,0.189519282202,0.186626012823,0.248893074191,0.27442218192,0.243259122583,0.308329309181,0.316877613819,0.373428351141,0.472519239702,0.43285196672,0.458423203277,0.568766105368,0.526224068911,0.662050102523,0.698734500611,0.775130416568,0.840221186657,1.05530443387,1.12596274976,1.42591615547,1.3975363304,1.73421068432,1.98035807469,2.45573168674,3.08378671086,3.35533066666,3.84764314535,4.02579614679,4.09385632594,3.63540195887,3.33842450277,3.42330889659,3.05567851093,3.01584118368,2.80662981015,2.54624095234,2.59460638547,2.25192396056,2.11347939909,1.96071565306,1.83902105178,1.76266976545,1.59852315644,1.51358412981,1.45710341483,1.3353507181,1.19402716103])

    # Creating weights for histo: y4_PT_15
    y4_PT_15_weights = numpy.array([0.0,0.0,0.0,0.0,0.0122002763198,0.00761033393201,0.00457192023381,0.00914230918122,0.00762393945899,0.00760926699402,0.00908277451442,0.010682836476,0.00760293862212,0.00455338174329,0.0182884276737,0.0152101757164,0.00912374115199,0.00916230924681,0.00459324717798,0.00911996965029,0.0090955553208,0.00916242149389,0.0106725522808,0.00915275052225,0.00457830059384,0.00609873566224,0.0,0.00303684932844,0.00456379000097,0.00609376488916,0.00456998840258,0.00460059640749,0.00606293357165,0.00608480166487,0.00151071447174,0.00453214223369,0.00455688030737,0.00456032215714,0.00608597730528,0.0,0.00305407157432,0.00455570939315,0.00152280643555,0.00607696800062,0.00151683016499,0.0,0.00611526552091,0.0076197780464,0.0,0.00152148310161,0.00152764133059,0.00303985755004,0.00153108318036,0.00304711107415,0.00152148310161,0.00304556679071,0.00151221149325,0.00305997577044,0.00612021502612,0.00305925857071,0.00302953790847,0.00915644640488,0.00458040256801,0.00150805480685,0.00306048619924,0.00761354065369,0.00761375569546,0.00304924140547,0.00606942854185,0.0121877400939,0.00153288740439,0.0045702637033,0.0106376056311,0.00610285453911,0.00456939644696,0.0106652869412,0.00911137743212,0.0121906939643,0.00304791334535,0.00762249560715,0.0152817539035,0.0122069284359,0.0152054849702,0.0137201726022,0.0167614539178,0.0136604453431,0.00912304876478,0.0167446050411,0.0197624917033,0.02130776764,0.0136984084853,0.021329579019,0.0273764470804,0.022878813142,0.030504371322,0.019796910201,0.0244054560644,0.0351177733484,0.0365740668937,0.0411584264665])

    # Creating weights for histo: y4_PT_16
    y4_PT_16_weights = numpy.array([0.0,0.0,0.0,0.0,0.00180590286179,0.00144602488374,0.00144544333404,0.000722281268285,0.00144399523676,0.000903195219611,0.00090261444017,0.00144405993898,0.000541753604611,0.00126266457233,0.000724035545708,0.000542679847685,0.000722716852866,0.000542217303847,0.000903027301948,0.000540944826875,0.00036084030801,0.000541326107807,0.000903263002888,0.00054105844089,0.000360980380611,0.000180377192502,0.000360876548955,0.000180413009801,0.000361513942838,0.000902817404868,0.000361397209251,0.0,0.0,0.0,0.000180616513685,0.0,0.0,0.000541147406441,0.000360557967553,0.000722013601367,0.0,0.000361251898851,0.000180072783967,0.0,0.000181039774034,0.000360896575832,0.0,0.000180072783967,0.000180186397982,0.0,0.000180413009801,0.000541639220331,0.0,0.000361436685307,0.000180272243962,0.000361313365959,0.000180572724148,0.000361168479205,0.000180803764988,0.0,0.000180803764988,0.000361263568358,0.000180824485103,0.000179954779444,0.000180682178735,0.000722503104464,0.000180223794324,0.0,0.0,0.000180622406209,0.000541095413586,0.000360969365828,0.000361166900162,0.000361475506639,0.000180803764988,0.000361458830412,0.000180726545971,0.000181039774034,0.000722533529912,0.000361451012227,0.00036103541601,0.0,0.000361010883086,0.000541556031764,0.000360636958179,0.00036079016379,0.000360782923304,0.000360950340295,0.000361249434005,0.0010833123323,0.000180755469403,0.0,0.000180223794324,0.0010837875855,0.000541571051922,0.000180411122653,0.000542773819956,0.0,0.000361254902883,0.00108337549399])

    # Creating a new Canvas
    fig   = plt.figure(figsize=(12,6),dpi=80)
    frame = gridspec.GridSpec(1,1,right=0.7)
    pad   = fig.add_subplot(frame[0])

    # Creating a new Stack
    pad.hist(x=xData, bins=xBinning, weights=y4_PT_0_weights+y4_PT_1_weights+y4_PT_2_weights+y4_PT_3_weights+y4_PT_4_weights+y4_PT_5_weights+y4_PT_6_weights+y4_PT_7_weights+y4_PT_8_weights+y4_PT_9_weights+y4_PT_10_weights+y4_PT_11_weights+y4_PT_12_weights+y4_PT_13_weights+y4_PT_14_weights+y4_PT_15_weights+y4_PT_16_weights,\
             label="$bg\_dip\_1600\_inf$", histtype="step", rwidth=1.0,\
             color=None, edgecolor="#e5e5e5", linewidth=4, linestyle="dashdot",\
             bottom=None, cumulative=False, normed=False, align="mid", orientation="vertical")

    pad.hist(x=xData, bins=xBinning, weights=y4_PT_0_weights+y4_PT_1_weights+y4_PT_2_weights+y4_PT_3_weights+y4_PT_4_weights+y4_PT_5_weights+y4_PT_6_weights+y4_PT_7_weights+y4_PT_8_weights+y4_PT_9_weights+y4_PT_10_weights+y4_PT_11_weights+y4_PT_12_weights+y4_PT_13_weights+y4_PT_14_weights+y4_PT_15_weights,\
             label="$bg\_dip\_1200\_1600$", histtype="step", rwidth=1.0,\
             color=None, edgecolor="#f2f2f2", linewidth=4, linestyle="dashdot",\
             bottom=None, cumulative=False, normed=False, align="mid", orientation="vertical")

    pad.hist(x=xData, bins=xBinning, weights=y4_PT_0_weights+y4_PT_1_weights+y4_PT_2_weights+y4_PT_3_weights+y4_PT_4_weights+y4_PT_5_weights+y4_PT_6_weights+y4_PT_7_weights+y4_PT_8_weights+y4_PT_9_weights+y4_PT_10_weights+y4_PT_11_weights+y4_PT_12_weights+y4_PT_13_weights+y4_PT_14_weights,\
             label="$bg\_dip\_800\_1200$", histtype="step", rwidth=1.0,\
             color=None, edgecolor="#ccc6aa", linewidth=4, linestyle="dashdot",\
             bottom=None, cumulative=False, normed=False, align="mid", orientation="vertical")

    pad.hist(x=xData, bins=xBinning, weights=y4_PT_0_weights+y4_PT_1_weights+y4_PT_2_weights+y4_PT_3_weights+y4_PT_4_weights+y4_PT_5_weights+y4_PT_6_weights+y4_PT_7_weights+y4_PT_8_weights+y4_PT_9_weights+y4_PT_10_weights+y4_PT_11_weights+y4_PT_12_weights+y4_PT_13_weights,\
             label="$bg\_dip\_600\_800$", histtype="step", rwidth=1.0,\
             color=None, edgecolor="#ccc6aa", linewidth=4, linestyle="dashdot",\
             bottom=None, cumulative=False, normed=False, align="mid", orientation="vertical")

    pad.hist(x=xData, bins=xBinning, weights=y4_PT_0_weights+y4_PT_1_weights+y4_PT_2_weights+y4_PT_3_weights+y4_PT_4_weights+y4_PT_5_weights+y4_PT_6_weights+y4_PT_7_weights+y4_PT_8_weights+y4_PT_9_weights+y4_PT_10_weights+y4_PT_11_weights+y4_PT_12_weights,\
             label="$bg\_dip\_400\_600$", histtype="step", rwidth=1.0,\
             color=None, edgecolor="#c1bfa8", linewidth=4, linestyle="dashdot",\
             bottom=None, cumulative=False, normed=False, align="mid", orientation="vertical")

    pad.hist(x=xData, bins=xBinning, weights=y4_PT_0_weights+y4_PT_1_weights+y4_PT_2_weights+y4_PT_3_weights+y4_PT_4_weights+y4_PT_5_weights+y4_PT_6_weights+y4_PT_7_weights+y4_PT_8_weights+y4_PT_9_weights+y4_PT_10_weights+y4_PT_11_weights,\
             label="$bg\_dip\_200\_400$", histtype="step", rwidth=1.0,\
             color=None, edgecolor="#bab5a3", linewidth=4, linestyle="dashdot",\
             bottom=None, cumulative=False, normed=False, align="mid", orientation="vertical")

    pad.hist(x=xData, bins=xBinning, weights=y4_PT_0_weights+y4_PT_1_weights+y4_PT_2_weights+y4_PT_3_weights+y4_PT_4_weights+y4_PT_5_weights+y4_PT_6_weights+y4_PT_7_weights+y4_PT_8_weights+y4_PT_9_weights+y4_PT_10_weights,\
             label="$bg\_dip\_100\_200$", histtype="step", rwidth=1.0,\
             color=None, edgecolor="#b2a596", linewidth=4, linestyle="dashdot",\
             bottom=None, cumulative=False, normed=False, align="mid", orientation="vertical")

    pad.hist(x=xData, bins=xBinning, weights=y4_PT_0_weights+y4_PT_1_weights+y4_PT_2_weights+y4_PT_3_weights+y4_PT_4_weights+y4_PT_5_weights+y4_PT_6_weights+y4_PT_7_weights+y4_PT_8_weights+y4_PT_9_weights,\
             label="$bg\_dip\_0\_100$", histtype="step", rwidth=1.0,\
             color=None, edgecolor="#b7a39b", linewidth=4, linestyle="dashdot",\
             bottom=None, cumulative=False, normed=False, align="mid", orientation="vertical")

    pad.hist(x=xData, bins=xBinning, weights=y4_PT_0_weights+y4_PT_1_weights+y4_PT_2_weights+y4_PT_3_weights+y4_PT_4_weights+y4_PT_5_weights+y4_PT_6_weights+y4_PT_7_weights+y4_PT_8_weights,\
             label="$bg\_vbf\_1600\_inf$", histtype="step", rwidth=1.0,\
             color=None, edgecolor="#ad998c", linewidth=4, linestyle="dashdot",\
             bottom=None, cumulative=False, normed=False, align="mid", orientation="vertical")

    pad.hist(x=xData, bins=xBinning, weights=y4_PT_0_weights+y4_PT_1_weights+y4_PT_2_weights+y4_PT_3_weights+y4_PT_4_weights+y4_PT_5_weights+y4_PT_6_weights+y4_PT_7_weights,\
             label="$bg\_vbf\_1200\_1600$", histtype="step", rwidth=1.0,\
             color=None, edgecolor="#9b8e82", linewidth=4, linestyle="dashdot",\
             bottom=None, cumulative=False, normed=False, align="mid", orientation="vertical")

    pad.hist(x=xData, bins=xBinning, weights=y4_PT_0_weights+y4_PT_1_weights+y4_PT_2_weights+y4_PT_3_weights+y4_PT_4_weights+y4_PT_5_weights+y4_PT_6_weights,\
             label="$bg\_vbf\_800\_1200$", histtype="step", rwidth=1.0,\
             color=None, edgecolor="#876656", linewidth=4, linestyle="dashdot",\
             bottom=None, cumulative=False, normed=False, align="mid", orientation="vertical")

    pad.hist(x=xData, bins=xBinning, weights=y4_PT_0_weights+y4_PT_1_weights+y4_PT_2_weights+y4_PT_3_weights+y4_PT_4_weights+y4_PT_5_weights,\
             label="$bg\_vbf\_600\_800$", histtype="step", rwidth=1.0,\
             color=None, edgecolor="#afcec6", linewidth=4, linestyle="dashdot",\
             bottom=None, cumulative=False, normed=False, align="mid", orientation="vertical")

    pad.hist(x=xData, bins=xBinning, weights=y4_PT_0_weights+y4_PT_1_weights+y4_PT_2_weights+y4_PT_3_weights+y4_PT_4_weights,\
             label="$bg\_vbf\_400\_600$", histtype="step", rwidth=1.0,\
             color=None, edgecolor="#84c1a3", linewidth=4, linestyle="dashdot",\
             bottom=None, cumulative=False, normed=False, align="mid", orientation="vertical")

    pad.hist(x=xData, bins=xBinning, weights=y4_PT_0_weights+y4_PT_1_weights+y4_PT_2_weights+y4_PT_3_weights,\
             label="$bg\_vbf\_200\_400$", histtype="step", rwidth=1.0,\
             color=None, edgecolor="#89a8a0", linewidth=4, linestyle="dashdot",\
             bottom=None, cumulative=False, normed=False, align="mid", orientation="vertical")

    pad.hist(x=xData, bins=xBinning, weights=y4_PT_0_weights+y4_PT_1_weights+y4_PT_2_weights,\
             label="$bg\_vbf\_100\_200$", histtype="step", rwidth=1.0,\
             color=None, edgecolor="#829e8c", linewidth=4, linestyle="dashdot",\
             bottom=None, cumulative=False, normed=False, align="mid", orientation="vertical")

    pad.hist(x=xData, bins=xBinning, weights=y4_PT_0_weights+y4_PT_1_weights,\
             label="$bg\_vbf\_0\_100$", histtype="step", rwidth=1.0,\
             color=None, edgecolor="#adbcc6", linewidth=4, linestyle="dashdot",\
             bottom=None, cumulative=False, normed=False, align="mid", orientation="vertical")

    pad.hist(x=xData, bins=xBinning, weights=y4_PT_0_weights,\
             label="$signal$", histtype="step", rwidth=1.0,\
             color=None, edgecolor="#7a8e99", linewidth=3, linestyle="dashed",\
             bottom=None, cumulative=False, normed=False, align="mid", orientation="vertical")


    # Axis
    plt.rc('text',usetex=False)
    plt.xlabel(r"p_{T} [ j_{2} ]   ( GeV ) ",\
               fontsize=16,color="black")
    plt.ylabel(r"$\mathrm{Events}$ $(\mathcal{L}_{\mathrm{int}} = 40.0\ \mathrm{fb}^{-1})$ ",\
               fontsize=16,color="black")

    # Boundary of y-axis
    ymax=(y4_PT_0_weights+y4_PT_1_weights+y4_PT_2_weights+y4_PT_3_weights+y4_PT_4_weights+y4_PT_5_weights+y4_PT_6_weights+y4_PT_7_weights+y4_PT_8_weights+y4_PT_9_weights+y4_PT_10_weights+y4_PT_11_weights+y4_PT_12_weights+y4_PT_13_weights+y4_PT_14_weights+y4_PT_15_weights+y4_PT_16_weights).max()*1.1
    #ymin=0 # linear scale
    ymin=min([x for x in (y4_PT_0_weights+y4_PT_1_weights+y4_PT_2_weights+y4_PT_3_weights+y4_PT_4_weights+y4_PT_5_weights+y4_PT_6_weights+y4_PT_7_weights+y4_PT_8_weights+y4_PT_9_weights+y4_PT_10_weights+y4_PT_11_weights+y4_PT_12_weights+y4_PT_13_weights+y4_PT_14_weights+y4_PT_15_weights+y4_PT_16_weights) if x])/100. # log scale
    plt.gca().set_ylim(ymin,ymax)

    # Log/Linear scale for X-axis
    plt.gca().set_xscale("linear")
    #plt.gca().set_xscale("log",nonposx="clip")

    # Log/Linear scale for Y-axis
    #plt.gca().set_yscale("linear")
    plt.gca().set_yscale("log",nonposy="clip")

    # Legend
    plt.legend(bbox_to_anchor=(1.05,1), loc=2, borderaxespad=0.)

    # Saving the image
    plt.savefig('../../HTML/MadAnalysis5job_0/selection_3.png')
    plt.savefig('../../PDF/MadAnalysis5job_0/selection_3.png')
    plt.savefig('../../DVI/MadAnalysis5job_0/selection_3.eps')

# Running!
if __name__ == '__main__':
    selection_3()
