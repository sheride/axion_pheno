def selection_2():

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

    # Creating weights for histo: y3_PHI_0
    y3_PHI_0_weights = numpy.array([11.4429661752,27.0659887615,26.7712170146,27.6391602694,27.4180804592,27.2297526209,27.5654683326,27.3034445576,27.0741767545,27.2543165998,26.4764412677,27.1683406736,27.0004848177,27.1765286666,27.4426444381,26.791684997,26.9841088318,27.4344564451,27.2952565646,26.8326249619,27.0127648072,27.2256566244,27.2788805787,27.7742641534,27.4057964697,27.9134640339,27.7128562061,26.9308848775,26.6934290814,26.513289236,27.4549284276,27.2829765752,27.1274007088,26.7712170146,27.7005722166,27.864336076,27.0291407931,27.610500294,27.6841962307,27.3362005295,26.9595448529,26.9472608634,27.4426444381,27.1519646877,27.5859363151,27.8274881077,27.0332367896,26.8367209583,26.7875930005,26.8203449724,27.6268802799,27.6268802799,27.4876803994,27.5327163608,27.5245283678,26.9800128353,27.4180804592,26.7179930603,26.8285329654,27.2829765752,27.8520520866,27.1274007088,27.2584125963,11.4798101436])

    # Creating weights for histo: y3_PHI_1
    y3_PHI_1_weights = numpy.array([1.15414565601,3.35357580488,2.89148601339,3.29232663113,3.17050077049,3.2924383785,3.36532289663,2.75821025293,3.08589719759,3.47501755898,3.2440269348,3.16009104242,2.96464969968,3.27958582891,3.51138111425,3.49917501718,3.2436548441,3.49914137281,3.14661967675,3.14712674546,3.23207557367,3.32847510276,3.14746038546,3.02544667708,3.03790350481,3.11011793925,3.24437819804,3.21917496069,3.12230160674,3.34193845787,3.74245905357,3.31741571794,2.86795458078,3.01273551395,3.54816522414,3.49912975749,3.02539981528,3.55978254474,3.34106690849,3.42701064877,3.25673249055,3.34144821134,3.46271453408,3.31704803305,3.51207242593,3.48772391578,3.3423834447,2.8070742935,3.25650018419,3.46255632544,3.17092132511,3.24476791198,3.36558724525,3.26837784813,3.28147231676,2.92910482406,3.6930639126,2.9280786708,3.11045999034,3.14726012135,3.34102204933,3.49802910598,3.0864042663,1.19062576499])

    # Creating weights for histo: y3_PHI_2
    y3_PHI_2_weights = numpy.array([6.23516406848,15.2112042187,15.2104067257,16.1042311196,15.8036464959,15.331249645,14.6376083958,15.1310417077,15.4523859425,15.5122640326,14.7982185319,14.4878863121,15.5110450666,15.0105624122,15.1399174332,14.7992432897,14.8194822577,14.7176593404,15.0105458838,14.6683428678,15.5817946807,14.6986930556,15.452687585,15.1807920496,15.1404050196,16.2349290693,14.8598899482,15.9433565299,15.9033827087,14.7278573341,14.8489564428,14.6887884402,15.6226321083,15.3621122117,14.8396675086,15.2805902437,15.5735015797,15.0297766223,15.2092580052,15.0708123902,14.7594140916,15.3410633545,14.7080728958,14.3168178608,14.909590705,15.090435677,15.5318336023,14.8896120586,14.9491926383,14.5593053245,14.979819676,15.3619675886,14.8283827757,15.3312661733,15.3713970139,14.3375196226,15.2206501723,15.1703337344,15.3510754041,15.2006260729,15.0692008758,15.0700603501,15.0103392794,6.6964290738])

    # Creating weights for histo: y3_PHI_3
    y3_PHI_3_weights = numpy.array([7.92073918815,18.277204508,18.239699173,18.5691830535,18.4971624102,18.4144572965,18.0140780952,18.5354599398,18.0081061668,18.1563968664,18.3379394255,17.7216607957,17.9196322515,18.3816441909,18.3282746517,18.1628766118,18.3658693625,17.9918153963,18.5358580684,18.2288481386,17.8664211512,18.3107448076,18.0304419913,17.9979579512,18.2946449763,18.3716584767,18.2112045435,17.6834323292,18.2564855729,18.3871489276,18.6287317105,18.1842577403,18.2894368048,18.0176043767,18.9206818182,18.2397113606,18.5968408006,18.0901937751,18.1235065726,18.2398372992,17.7547826541,18.1575506267,18.1895877879,19.1298008737,18.3044844392,18.4203520366,18.7514974945,18.3429647829,17.6015072224,18.3983452776,18.6355405213,18.0035805014,18.0633729105,18.1008335576,18.5632680007,18.1123670981,18.4552532859,18.5578404522,18.4268399071,18.3480998288,18.2830261225,18.0422924097,18.1399679697,7.73959069507])

    # Creating weights for histo: y3_PHI_4
    y3_PHI_4_weights = numpy.array([2.29250078658,5.44439661154,5.68425759565,5.55282928048,5.56774418367,5.66258469009,5.67063336669,5.57672679535,5.65365819469,5.63091907999,5.53830719119,5.59641558989,5.50356320278,5.61214818731,5.60333793275,5.55490558251,5.52632235901,5.54714149558,5.45143118695,5.47991019452,5.41980565989,5.55320606116,5.64672783521,5.52342034613,5.52443444731,5.56483415418,5.61319435494,5.48981872467,5.64187778607,5.57066623807,5.61121425223,5.60729012156,5.52231806223,5.65658425739,5.62095443357,5.58366116313,5.47106386522,5.58452294872,5.54902940727,5.66565505178,5.60639226122,5.60433600072,5.68120326718,5.63490333523,5.45529920135,5.38316173488,5.45821323914,5.50179153194,5.58649904313,5.38634833742,5.54998739218,5.51845405614,5.52746071765,5.63686740472,5.58755723567,5.51233337429,5.60340206563,5.61726278459,5.61621260866,5.55185526235,5.56481812096,5.42277581395,5.51871058766,2.26962418701])

    # Creating weights for histo: y3_PHI_5
    y3_PHI_5_weights = numpy.array([0.731780619511,1.75999199447,1.75163075359,1.77711097302,1.77588707428,1.75468189834,1.77437150435,1.74032679442,1.7738157687,1.77612793308,1.80188622039,1.76301113141,1.78067904395,1.73627980659,1.75599221817,1.79226547207,1.77486442467,1.7852001475,1.79977530514,1.78040657745,1.75346040018,1.76231296099,1.79078190995,1.7758846737,1.75795429709,1.82077483089,1.78921472742,1.76628673095,1.76576260301,1.76383733308,1.75143470573,1.75370846073,1.78247548244,1.77107630003,1.75874649046,1.78169489191,1.76662881445,1.77823324696,1.76702211045,1.73991189314,1.78343731722,1.74264335986,1.82175066908,1.74182516015,1.76477996316,1.76148835972,1.77788996317,1.72067959875,1.78237745852,1.7587556927,1.7698163925,1.79704383842,1.77991125654,1.75271621854,1.78628321187,1.77765270526,1.79855500728,1.76656439872,1.79298484766,1.76654119306,1.77438430748,1.75622467491,1.71843665128,0.750694436163])

    # Creating weights for histo: y3_PHI_6
    y3_PHI_6_weights = numpy.array([0.252234145541,0.666519367981,0.651030760104,0.658206754552,0.650574013216,0.62047840193,0.639304990841,0.605570399422,0.650421664287,0.667996272889,0.642609683035,0.639281898582,0.654114526358,0.648458322442,0.647344295888,0.651009567208,0.647256325378,0.64018539571,0.639929381532,0.655999494475,0.65191096504,0.639056574116,0.64797008611,0.634145020577,0.642088857627,0.659048072524,0.623637842815,0.626730506086,0.62931883842,0.639568302573,0.639602890978,0.647337098301,0.639349675862,0.617536388158,0.640673532076,0.638517154941,0.638713189226,0.640746907479,0.612336931131,0.633892305293,0.649403205696,0.6321435915,0.636178039064,0.651915163633,0.663703012085,0.661131674055,0.649021533641,0.631026166086,0.631865684661,0.65528353448,0.656803524946,0.62767738867,0.641041808621,0.670806530829,0.654738617149,0.644461862144,0.627821140481,0.633705367958,0.633887606868,0.667317600395,0.645312776898,0.616736456313,0.631233496584,0.263131892376])

    # Creating weights for histo: y3_PHI_7
    y3_PHI_7_weights = numpy.array([0.028180736618,0.0704422444063,0.0700721887924,0.0715392937612,0.0706827176919,0.0703092674569,0.0724095740418,0.0700666987261,0.0725361389289,0.0711653825283,0.0726533162218,0.0705064488457,0.0710365545603,0.0717284705495,0.0715120110653,0.0691425235962,0.0704213318637,0.071258420293,0.0707037140523,0.0734401977854,0.0715332169703,0.0714975105849,0.0717565495146,0.0711500857786,0.0714989773965,0.0699539637769,0.0728195269313,0.0729735002411,0.0719367577976,0.0753007854448,0.070978762183,0.0708242021486,0.0727018886405,0.0723955764681,0.0738055596021,0.0715660735502,0.0730410154839,0.0713477281654,0.0713621867369,0.0706019173269,0.072441885806,0.0714805374791,0.0723258819624,0.0729867015455,0.0717688288232,0.0735016781461,0.0723857278759,0.0716734022509,0.0718563765216,0.07240429352,0.0717130899821,0.0710006805393,0.0706966733566,0.0717803956804,0.0723596605382,0.0710502168627,0.071676377783,0.0737431991543,0.0710225150778,0.0714583257605,0.0721520857415,0.0702423389388,0.0713587921158,0.0302085785186])

    # Creating weights for histo: y3_PHI_8
    y3_PHI_8_weights = numpy.array([0.00589943415204,0.0134300731229,0.0129326875375,0.0129559473555,0.012360225443,0.0123297024078,0.0122799305849,0.012417523331,0.0123884585823,0.0132426966736,0.0145181271086,0.0126991627063,0.0122449005237,0.0123370309657,0.0129781676618,0.0123600145706,0.0120852567631,0.0129829464459,0.0128103949194,0.0122457440132,0.0127575624768,0.0126436616886,0.0126998175987,0.0126633648915,0.0123281906607,0.0130075264439,0.0127116977331,0.0122752913924,0.0115953348721,0.0126155859611,0.0123358355271,0.0134620158341,0.0115685615043,0.0122750151793,0.0121573855139,0.0129991687694,0.0138376864729,0.0127352218842,0.0128448918595,0.0121209550819,0.0131253031259,0.0127230328663,0.0134354473986,0.0125604220422,0.0139973153833,0.0127613136293,0.0131004528549,0.0125866756541,0.0127283878369,0.01317915726,0.0123396787506,0.0135507589528,0.0116400932784,0.0131525873395,0.012429283179,0.0125062471445,0.0136489839037,0.0132660411377,0.0125445561227,0.0113464668475,0.0129307050401,0.0126421143011,0.0134732559263,0.00458971616426])

    # Creating weights for histo: y3_PHI_9
    y3_PHI_9_weights = numpy.array([0.0,2.61802246854,2.60133245831,2.59814004154,5.23020691354,0.0,15.6477911358,2.60604494535,0.0,5.20757697778,10.4064480635,7.80670489196,5.21066480079,2.60351585296,2.60470714507,2.60135629953,2.61218252233,2.60470714507,2.60604494535,0.0,0.0,0.0,0.0,0.0,2.60701166852,7.81100784831,0.0,0.0,0.0,7.80410927485,2.60667135428,0.0,7.83303790812,2.61802246854,0.0,2.60604494535,10.4287049995,5.21164536725,7.82236319246,2.60667135428,13.0464098414,5.21241828434,0.0,5.21075324404,0.0,2.60874977064,2.60197540228,2.60399267743,7.82587785028,2.60133245831,2.59814004154,5.21457553055,2.60604494535,5.23106058317,2.60470714507,7.81999060616,7.82485113952,2.61044172846,2.6044372009,0.0,2.60351585296,7.82636236547,0.0,2.60300480479])

    # Creating weights for histo: y3_PHI_10
    y3_PHI_10_weights = numpy.array([10.5335910004,17.9040012762,23.176394945,12.6306880456,10.5294472014,11.5842268127,14.7584076502,12.6425538545,9.46950804093,13.6926740966,16.8492524452,11.5795751386,13.6923816837,13.6917276021,20.0110557511,17.9075564018,9.4749830883,16.8557932607,17.903435688,20.0082701332,14.73768096,14.7470304787,15.8020794176,11.5881551496,24.2072159337,22.1212536651,17.9044129628,17.9085259815,16.8582133625,12.6364324207,27.378738122,17.8999459705,12.649729514,22.1170790857,10.5394508017,18.9539599216,8.42599402255,20.0158459366,15.8019139735,15.7911331704,7.36884047998,14.7435907792,8.42418183189,17.9076025723,20.0077507155,14.7542946315,13.6905579504,12.6351358002,13.6940091925,11.5847192976,20.0214518003,13.6950595705,20.0204129649,21.0675590597,13.6900385327,22.1152476574,13.6914390367,12.6411110276,11.5789787701,13.6935474879,17.9041590252,26.3328040019,13.6906272061,2.10601948709])

    # Creating weights for histo: y3_PHI_11
    y3_PHI_11_weights = numpy.array([9.44674383257,29.9397340228,27.8731066755,28.1017085847,25.1099610684,26.9472564559,30.172408846,19.8076148085,25.106960176,26.0386085347,26.0258134366,25.341648402,24.6461906367,19.5785479724,27.4109692519,28.3264873339,27.6419572739,26.2546266762,22.575889982,29.2525719382,27.1843000558,23.9561967241,24.6429323055,28.5656711349,29.9387081096,29.7149629584,26.2613085607,21.4256260385,23.9587595861,28.0987845397,22.5725240643,28.1006557748,24.1812982325,26.9446244312,29.4851622292,23.7272221049,27.8719923877,27.8691067665,24.1858207041,27.4122910278,27.1809418229,24.8809672373,29.2567332268,24.8762449624,27.8613528603,26.4826675991,25.7946601927,26.0238230881,27.412344821,23.489909539,23.5014942899,27.4046062842,26.4849538103,27.8715005641,20.2693180441,24.4161824195,28.3299416261,27.1823058648,24.6431705325,27.8706129762,26.9499883822,25.3354122326,25.5614090137,11.0536006573])

    # Creating weights for histo: y3_PHI_12
    y3_PHI_12_weights = numpy.array([6.72726796428,17.4172678201,17.8886425817,16.7520971927,17.944810836,17.0301377455,17.1967112436,16.6431307795,17.1132244433,17.0310225879,16.366082789,17.0582949683,16.1445374974,16.8642105671,16.948012833,16.8629102335,16.9474434561,16.8086578553,16.1155569864,16.3103377202,17.9710714184,17.5575691944,16.7536398961,17.0851056919,17.3907340907,16.8077768601,17.305981581,17.5552301328,15.8948580658,17.2498056325,16.7804198426,18.0274820425,17.3061470081,17.2502595951,17.6123217008,17.1932911356,17.0015188658,17.527265267,16.0616970166,17.3628692506,17.278447595,16.9481051643,17.6663740277,17.0027999637,16.5592708065,16.6700761529,17.3076743229,17.308005177,17.1133667875,16.0051209655,16.8637412159,16.0596387963,17.9986823472,17.5282155108,16.7804429254,15.7844451276,18.0833463727,15.9778870564,17.5287541105,16.3085487998,16.2824267144,16.0612622897,16.449969692,7.11603307364])

    # Creating weights for histo: y3_PHI_13
    y3_PHI_13_weights = numpy.array([3.24574342161,8.94402484566,8.92249445894,8.57094475109,8.20642705101,8.59976318585,8.54957214059,9.0228947544,8.51954611086,7.7626753432,8.2272110348,8.60861685953,8.66034318884,8.26543536004,8.72174848287,9.10476847977,7.96491412511,9.16508147684,8.22753265558,8.30830801567,8.44772151751,8.78124225723,8.63001981161,8.52921293895,8.14717600931,8.51899389407,7.95474969508,8.26720730844,8.33709610885,8.68013803706,7.74251032768,8.31762288141,8.38875568669,8.43887391214,8.07621311689,8.6711083822,8.39851960783,7.99571689935,8.33746627616,8.56952476504,8.32710766,8.16581787741,8.14627789848,8.78159421958,8.61006111884,8.36829939198,8.74201059146,8.30747665632,8.66095002049,8.8520048952,8.62048041817,8.85185318729,8.41823556794,8.40863549133,8.70073390305,7.92425640498,8.62015879739,8.05551408952,8.53915890959,8.51847808717,8.01503841889,8.5283087598,8.62980742053,3.6698058699])

    # Creating weights for histo: y3_PHI_14
    y3_PHI_14_weights = numpy.array([1.20799430389,3.0725955575,2.91396359553,3.18006088322,3.10366758328,3.18840936687,3.10628920491,2.98475584358,2.98176602532,2.92835596735,2.86290968824,3.04702378159,3.2337475696,3.16864717219,2.99616609195,2.93102760523,3.18291142543,3.12329127139,2.98471236791,3.08111294221,3.18871138814,3.08651700697,2.96496094596,3.10636730722,3.19415354221,3.14293381178,3.16306612681,3.2366608245,3.04717036771,2.87450961367,2.90265915079,3.05251364348,2.96227045579,3.20555032467,3.20001775659,3.05240014504,3.14895692398,3.11494201827,2.93100836821,2.96208462614,3.13168515441,3.04143234822,3.06116722632,3.13215723098,2.79252795828,3.08382613207,3.21404500969,3.13751743533,3.14298575175,3.04707918422,3.18574273061,3.13764324546,3.10075125046,2.99617840365,2.95369651423,3.11775716435,3.17979271911,3.0556000316,3.15146312345,3.21107827586,3.10926863517,3.12893272103,3.05563889039,1.28151012979])

    # Creating weights for histo: y3_PHI_15
    y3_PHI_15_weights = numpy.array([0.153706755039,0.34279721466,0.355039102995,0.34277937227,0.367005556819,0.371466745144,0.399137928915,0.348665943055,0.362713812118,0.409741035079,0.353363099944,0.35486576004,0.316852488911,0.329050539321,0.310638847028,0.323042734812,0.34421716169,0.325806532851,0.333462808776,0.35667351319,0.380806468297,0.348776305918,0.358039696727,0.318318991581,0.359705537887,0.333650449275,0.336883348563,0.370093235593,0.354993847132,0.33059136559,0.347058355526,0.363850998622,0.384016916895,0.370417825299,0.315174831598,0.33498390207,0.350500637033,0.312385038025,0.318190313682,0.370069012481,0.338160083826,0.345785401432,0.357796047665,0.336712959646,0.349009674928,0.356814834373,0.36266512957,0.32742345514,0.343970322267,0.344343830843,0.341096279527,0.359537748524,0.348809863791,0.351774890904,0.359389928458,0.341038734865,0.330334836922,0.345925068353,0.338115064285,0.354786119173,0.325921031367,0.332092962232,0.312332810631,0.138718320248])

    # Creating weights for histo: y3_PHI_16
    y3_PHI_16_weights = numpy.array([0.0287080149553,0.0673545845564,0.0621131551273,0.0700586209649,0.0678915637002,0.066088680199,0.0705934434112,0.0626550253527,0.0635643429001,0.0680726877706,0.0673473827276,0.0534436551576,0.0606632767779,0.0630090318283,0.0608344646351,0.0653583300245,0.0646398031734,0.0644604121634,0.0588689815538,0.0628307191671,0.0716868890004,0.0691551573104,0.0653700763229,0.0626493255095,0.0677137517009,0.0686067784803,0.0653703073976,0.063737109768,0.0655417263297,0.0550786628726,0.0693325456728,0.0601222923389,0.0608450170475,0.0659000462001,0.0673442632188,0.0682489207593,0.0631939686316,0.0657346737233,0.0706028019375,0.0590490657879,0.0613778753587,0.058857119718,0.0659063622425,0.0585058091142,0.0734883090284,0.0655444607139,0.0641081772607,0.0615720166385,0.0707841185702,0.068979463496,0.0644614519997,0.0651866415053,0.0688019595963,0.0660875248254,0.0586813873912,0.0669897560813,0.0675264656379,0.0662739251019,0.0624796781504,0.0612147366043,0.0651733932212,0.0684232666378,0.0603113884872,0.0265366250396])

    # Creating a new Canvas
    fig   = plt.figure(figsize=(12,6),dpi=80)
    frame = gridspec.GridSpec(1,1,right=0.7)
    pad   = fig.add_subplot(frame[0])

    # Creating a new Stack
    pad.hist(x=xData, bins=xBinning, weights=y3_PHI_0_weights+y3_PHI_1_weights+y3_PHI_2_weights+y3_PHI_3_weights+y3_PHI_4_weights+y3_PHI_5_weights+y3_PHI_6_weights+y3_PHI_7_weights+y3_PHI_8_weights+y3_PHI_9_weights+y3_PHI_10_weights+y3_PHI_11_weights+y3_PHI_12_weights+y3_PHI_13_weights+y3_PHI_14_weights+y3_PHI_15_weights+y3_PHI_16_weights,\
             label="$bg\_dip\_1600\_inf$", histtype="step", rwidth=1.0,\
             color=None, edgecolor="#e5e5e5", linewidth=1, linestyle="solid",\
             bottom=None, cumulative=False, normed=False, align="mid", orientation="vertical")

    pad.hist(x=xData, bins=xBinning, weights=y3_PHI_0_weights+y3_PHI_1_weights+y3_PHI_2_weights+y3_PHI_3_weights+y3_PHI_4_weights+y3_PHI_5_weights+y3_PHI_6_weights+y3_PHI_7_weights+y3_PHI_8_weights+y3_PHI_9_weights+y3_PHI_10_weights+y3_PHI_11_weights+y3_PHI_12_weights+y3_PHI_13_weights+y3_PHI_14_weights+y3_PHI_15_weights,\
             label="$bg\_dip\_1200\_1600$", histtype="step", rwidth=1.0,\
             color=None, edgecolor="#f2f2f2", linewidth=1, linestyle="solid",\
             bottom=None, cumulative=False, normed=False, align="mid", orientation="vertical")

    pad.hist(x=xData, bins=xBinning, weights=y3_PHI_0_weights+y3_PHI_1_weights+y3_PHI_2_weights+y3_PHI_3_weights+y3_PHI_4_weights+y3_PHI_5_weights+y3_PHI_6_weights+y3_PHI_7_weights+y3_PHI_8_weights+y3_PHI_9_weights+y3_PHI_10_weights+y3_PHI_11_weights+y3_PHI_12_weights+y3_PHI_13_weights+y3_PHI_14_weights,\
             label="$bg\_dip\_800\_1200$", histtype="step", rwidth=1.0,\
             color=None, edgecolor="#ccc6aa", linewidth=1, linestyle="solid",\
             bottom=None, cumulative=False, normed=False, align="mid", orientation="vertical")

    pad.hist(x=xData, bins=xBinning, weights=y3_PHI_0_weights+y3_PHI_1_weights+y3_PHI_2_weights+y3_PHI_3_weights+y3_PHI_4_weights+y3_PHI_5_weights+y3_PHI_6_weights+y3_PHI_7_weights+y3_PHI_8_weights+y3_PHI_9_weights+y3_PHI_10_weights+y3_PHI_11_weights+y3_PHI_12_weights+y3_PHI_13_weights,\
             label="$bg\_dip\_600\_800$", histtype="step", rwidth=1.0,\
             color=None, edgecolor="#ccc6aa", linewidth=1, linestyle="solid",\
             bottom=None, cumulative=False, normed=False, align="mid", orientation="vertical")

    pad.hist(x=xData, bins=xBinning, weights=y3_PHI_0_weights+y3_PHI_1_weights+y3_PHI_2_weights+y3_PHI_3_weights+y3_PHI_4_weights+y3_PHI_5_weights+y3_PHI_6_weights+y3_PHI_7_weights+y3_PHI_8_weights+y3_PHI_9_weights+y3_PHI_10_weights+y3_PHI_11_weights+y3_PHI_12_weights,\
             label="$bg\_dip\_400\_600$", histtype="step", rwidth=1.0,\
             color=None, edgecolor="#c1bfa8", linewidth=1, linestyle="solid",\
             bottom=None, cumulative=False, normed=False, align="mid", orientation="vertical")

    pad.hist(x=xData, bins=xBinning, weights=y3_PHI_0_weights+y3_PHI_1_weights+y3_PHI_2_weights+y3_PHI_3_weights+y3_PHI_4_weights+y3_PHI_5_weights+y3_PHI_6_weights+y3_PHI_7_weights+y3_PHI_8_weights+y3_PHI_9_weights+y3_PHI_10_weights+y3_PHI_11_weights,\
             label="$bg\_dip\_200\_400$", histtype="step", rwidth=1.0,\
             color=None, edgecolor="#bab5a3", linewidth=1, linestyle="solid",\
             bottom=None, cumulative=False, normed=False, align="mid", orientation="vertical")

    pad.hist(x=xData, bins=xBinning, weights=y3_PHI_0_weights+y3_PHI_1_weights+y3_PHI_2_weights+y3_PHI_3_weights+y3_PHI_4_weights+y3_PHI_5_weights+y3_PHI_6_weights+y3_PHI_7_weights+y3_PHI_8_weights+y3_PHI_9_weights+y3_PHI_10_weights,\
             label="$bg\_dip\_100\_200$", histtype="step", rwidth=1.0,\
             color=None, edgecolor="#b2a596", linewidth=1, linestyle="solid",\
             bottom=None, cumulative=False, normed=False, align="mid", orientation="vertical")

    pad.hist(x=xData, bins=xBinning, weights=y3_PHI_0_weights+y3_PHI_1_weights+y3_PHI_2_weights+y3_PHI_3_weights+y3_PHI_4_weights+y3_PHI_5_weights+y3_PHI_6_weights+y3_PHI_7_weights+y3_PHI_8_weights+y3_PHI_9_weights,\
             label="$bg\_dip\_0\_100$", histtype="step", rwidth=1.0,\
             color=None, edgecolor="#b7a39b", linewidth=1, linestyle="solid",\
             bottom=None, cumulative=False, normed=False, align="mid", orientation="vertical")

    pad.hist(x=xData, bins=xBinning, weights=y3_PHI_0_weights+y3_PHI_1_weights+y3_PHI_2_weights+y3_PHI_3_weights+y3_PHI_4_weights+y3_PHI_5_weights+y3_PHI_6_weights+y3_PHI_7_weights+y3_PHI_8_weights,\
             label="$bg\_vbf\_1600\_inf$", histtype="step", rwidth=1.0,\
             color=None, edgecolor="#ad998c", linewidth=1, linestyle="solid",\
             bottom=None, cumulative=False, normed=False, align="mid", orientation="vertical")

    pad.hist(x=xData, bins=xBinning, weights=y3_PHI_0_weights+y3_PHI_1_weights+y3_PHI_2_weights+y3_PHI_3_weights+y3_PHI_4_weights+y3_PHI_5_weights+y3_PHI_6_weights+y3_PHI_7_weights,\
             label="$bg\_vbf\_1200\_1600$", histtype="step", rwidth=1.0,\
             color=None, edgecolor="#9b8e82", linewidth=1, linestyle="solid",\
             bottom=None, cumulative=False, normed=False, align="mid", orientation="vertical")

    pad.hist(x=xData, bins=xBinning, weights=y3_PHI_0_weights+y3_PHI_1_weights+y3_PHI_2_weights+y3_PHI_3_weights+y3_PHI_4_weights+y3_PHI_5_weights+y3_PHI_6_weights,\
             label="$bg\_vbf\_800\_1200$", histtype="step", rwidth=1.0,\
             color=None, edgecolor="#876656", linewidth=1, linestyle="solid",\
             bottom=None, cumulative=False, normed=False, align="mid", orientation="vertical")

    pad.hist(x=xData, bins=xBinning, weights=y3_PHI_0_weights+y3_PHI_1_weights+y3_PHI_2_weights+y3_PHI_3_weights+y3_PHI_4_weights+y3_PHI_5_weights,\
             label="$bg\_vbf\_600\_800$", histtype="step", rwidth=1.0,\
             color=None, edgecolor="#afcec6", linewidth=1, linestyle="solid",\
             bottom=None, cumulative=False, normed=False, align="mid", orientation="vertical")

    pad.hist(x=xData, bins=xBinning, weights=y3_PHI_0_weights+y3_PHI_1_weights+y3_PHI_2_weights+y3_PHI_3_weights+y3_PHI_4_weights,\
             label="$bg\_vbf\_400\_600$", histtype="step", rwidth=1.0,\
             color=None, edgecolor="#84c1a3", linewidth=1, linestyle="solid",\
             bottom=None, cumulative=False, normed=False, align="mid", orientation="vertical")

    pad.hist(x=xData, bins=xBinning, weights=y3_PHI_0_weights+y3_PHI_1_weights+y3_PHI_2_weights+y3_PHI_3_weights,\
             label="$bg\_vbf\_200\_400$", histtype="step", rwidth=1.0,\
             color=None, edgecolor="#89a8a0", linewidth=1, linestyle="solid",\
             bottom=None, cumulative=False, normed=False, align="mid", orientation="vertical")

    pad.hist(x=xData, bins=xBinning, weights=y3_PHI_0_weights+y3_PHI_1_weights+y3_PHI_2_weights,\
             label="$bg\_vbf\_100\_200$", histtype="step", rwidth=1.0,\
             color=None, edgecolor="#829e8c", linewidth=1, linestyle="solid",\
             bottom=None, cumulative=False, normed=False, align="mid", orientation="vertical")

    pad.hist(x=xData, bins=xBinning, weights=y3_PHI_0_weights+y3_PHI_1_weights,\
             label="$bg\_vbf\_0\_100$", histtype="step", rwidth=1.0,\
             color=None, edgecolor="#adbcc6", linewidth=1, linestyle="solid",\
             bottom=None, cumulative=False, normed=False, align="mid", orientation="vertical")

    pad.hist(x=xData, bins=xBinning, weights=y3_PHI_0_weights,\
             label="$signal$", histtype="step", rwidth=1.0,\
             color=None, edgecolor="#7a8e99", linewidth=1, linestyle="solid",\
             bottom=None, cumulative=False, normed=False, align="mid", orientation="vertical")


    # Axis
    plt.rc('text',usetex=False)
    plt.xlabel(r"\phi [ j_{1} ] ",\
               fontsize=16,color="black")
    plt.ylabel(r"$\mathrm{Events}$ $(\mathcal{L}_{\mathrm{int}} = 40.0\ \mathrm{fb}^{-1})$ ",\
               fontsize=16,color="black")

    # Boundary of y-axis
    ymax=(y3_PHI_0_weights+y3_PHI_1_weights+y3_PHI_2_weights+y3_PHI_3_weights+y3_PHI_4_weights+y3_PHI_5_weights+y3_PHI_6_weights+y3_PHI_7_weights+y3_PHI_8_weights+y3_PHI_9_weights+y3_PHI_10_weights+y3_PHI_11_weights+y3_PHI_12_weights+y3_PHI_13_weights+y3_PHI_14_weights+y3_PHI_15_weights+y3_PHI_16_weights).max()*1.1
    ymin=0 # linear scale
    #ymin=min([x for x in (y3_PHI_0_weights+y3_PHI_1_weights+y3_PHI_2_weights+y3_PHI_3_weights+y3_PHI_4_weights+y3_PHI_5_weights+y3_PHI_6_weights+y3_PHI_7_weights+y3_PHI_8_weights+y3_PHI_9_weights+y3_PHI_10_weights+y3_PHI_11_weights+y3_PHI_12_weights+y3_PHI_13_weights+y3_PHI_14_weights+y3_PHI_15_weights+y3_PHI_16_weights) if x])/100. # log scale
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
    plt.savefig('../../HTML/MadAnalysis5job_0/selection_2.png')
    plt.savefig('../../PDF/MadAnalysis5job_0/selection_2.png')
    plt.savefig('../../DVI/MadAnalysis5job_0/selection_2.eps')

# Running!
if __name__ == '__main__':
    selection_2()
