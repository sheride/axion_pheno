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
    y3_PHI_0_weights = numpy.array([0.490021165658,1.11802632165,1.11802632165,1.14279271991,1.16225231855,1.07203152487,1.15517591904,1.15340711917,1.11271952202,1.1587143188,1.08264592413,1.2029399157,1.10741232239,1.20824711532,1.13925472016,1.13925472016,1.01896072859,1.03488192747,1.07380072475,1.15340711917,1.18348071706,1.19763271607,1.19409471632,1.14456191979,1.21886111458,1.16932831805,1.04549632673,1.10210512276,1.08972192363,1.1728663178,1.13394792053,1.2029399157,1.15517591904,1.20647791545,1.09149112351,1.19586391619,1.19055671656,1.23832031322,1.13748592028,1.20470871557,1.084414724,1.08618392388,1.10033632289,1.13040952078,1.08264592413,1.10918152227,1.17817351743,1.15340711917,1.06141752561,1.10741232239,1.17463551768,1.15517591904,1.16402111842,1.15163791929,1.10741232239,1.14279271991,1.13040952078,1.1286407209,1.16048311867,1.07556992462,1.20470871557,1.09856712301,1.1728663178,0.516556363799])

    # Creating weights for histo: y3_PHI_1
    y3_PHI_1_weights = numpy.array([0.288494280839,0.77149607677,0.81108487109,0.727689849434,0.72553037345,0.726624699796,0.695599868443,0.68176611261,0.726684651933,0.702031134048,0.723420058218,0.702061909478,0.720232602921,0.734103129398,0.710617878827,0.650797236586,0.690342865367,0.703069505065,0.700975976432,0.661507486067,0.76613675538,0.742665093961,0.704155837792,0.703169025613,0.706362875805,0.661452729782,0.681750125373,0.689306093073,0.72343364737,0.674259705344,0.718056340338,0.73841049062,0.728747405136,0.711657448887,0.665744503448,0.698843279069,0.628292003619,0.721294155431,0.68820417279,0.709556725998,0.671037477806,0.720260180904,0.73089409133,0.695654225047,0.762942905187,0.676374017385,0.705282138611,0.704204998545,0.672124210215,0.729798565942,0.730856921005,0.741580359957,0.741575563786,0.707400447461,0.759755849571,0.718036755973,0.717009576021,0.690316486426,0.724493601156,0.751236251185,0.698878051309,0.726628696605,0.740492828187,0.285305266786])

    # Creating weights for histo: y3_PHI_2
    y3_PHI_2_weights = numpy.array([0.226394724863,0.462512091652,0.461122891377,0.462512091652,0.456956090551,0.447928088762,0.479873695093,0.478484494817,0.493068097707,0.476401294405,0.463900891927,0.46320649179,0.464595292065,0.45140048945,0.485429296194,0.43403888601,0.48056809523,0.450011689175,0.450706089313,0.470150893166,0.479873695093,0.46320649179,0.48056809523,0.459039690964,0.497929698671,0.463900891927,0.469456493028,0.479178894955,0.498624098808,0.497234898533,0.475012094129,0.453484089863,0.452094889588,0.490984897294,0.472928893716,0.465289692203,0.487512496606,0.437511286698,0.489596097019,0.479873695093,0.488901696882,0.460428491239,0.471540093441,0.46320649179,0.427094484634,0.468067692753,0.476401294405,0.493762897845,0.48056809523,0.473623293854,0.454872890138,0.465289692203,0.465289692203,0.500012899083,0.490984897294,0.490984897294,0.469456493028,0.49515169812,0.461817291515,0.452094889588,0.477095694542,0.497929698671,0.498624098808,0.188893757432])

    # Creating weights for histo: y3_PHI_3
    y3_PHI_3_weights = numpy.array([0.142720841239,0.328589814946,0.342340338919,0.331908935905,0.340917858508,0.35798746344,0.339495418097,0.358935783714,0.29776972604,0.326219054261,0.333805536453,0.326693214398,0.325744894124,0.349926821111,0.322425813165,0.303459567685,0.340443738371,0.319106732206,0.332383056042,0.340917858508,0.321003332754,0.333805536453,0.330486455494,0.307726968918,0.350400981248,0.339495418097,0.326693214398,0.322425813165,0.33902125796,0.326693214398,0.327641534672,0.321951653028,0.314365170836,0.316735931521,0.34376281933,0.330012295357,0.301088806999,0.326219054261,0.329063975083,0.32005501248,0.313416850562,0.326219054261,0.31531349111,0.296821405766,0.313416850562,0.336176337138,0.318158411932,0.319580892343,0.311046089877,0.316735931521,0.313891010699,0.338547097823,0.323848293576,0.342340338919,0.339495418097,0.332857216179,0.317210091658,0.329063975083,0.313891010699,0.321477492891,0.323374133439,0.325270733987,0.302037127274,0.132289398225])

    # Creating weights for histo: y3_PHI_4
    y3_PHI_4_weights = numpy.array([0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0])

    # Creating weights for histo: y3_PHI_5
    y3_PHI_5_weights = numpy.array([0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,1.0529581672,1.05462838872,0.0,0.0,0.0,0.0,0.0,0.0,1.0521138287,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0])

    # Creating weights for histo: y3_PHI_6
    y3_PHI_6_weights = numpy.array([0.0,0.461149073386,0.691021577308,0.0,0.69070840998,0.459442983893,0.460150011971,0.230350862212,0.230559781324,0.691836196616,0.461210554089,0.230350862212,0.691508427621,0.691199487091,0.460092373813,0.230010873928,0.691579130428,0.460998061411,0.690321850063,0.0,0.0,0.691930338941,0.461195568167,0.0,0.0,0.230610349202,0.0,0.230742916967,0.229973216998,0.230010873928,1.15113700638,0.690481315635,0.460598821099,1.15171992029,0.920955561933,0.0,0.461149073386,0.230350862212,0.0,0.0,0.461072991017,1.14958961395,1.15140828998,0.229943168304,0.23035543484,0.230176948675,0.691073067396,0.0,0.23041895209,0.921971914795,0.461299701107,0.0,0.460429364913,0.230742916967,0.690877097657,0.0,0.230104824126,0.460354051053,0.69136394797,0.230829220503,0.0,0.0,1.38220953677,0.0])

    # Creating weights for histo: y3_PHI_7
    y3_PHI_7_weights = numpy.array([0.166124113985,0.5815832957,0.470538362578,0.637073832457,0.359991572865,0.415350581913,0.553981326742,0.470599144614,0.470721862776,0.553965169492,0.498513871771,0.526282414283,0.415143999929,0.5816371532,0.332360982493,0.415510615628,0.415460605092,0.5536408704,0.387841709491,0.470509895042,0.33229235265,0.470624149882,0.554107891868,0.415285183519,0.55370665349,0.498395000573,0.360223121648,0.415292108055,0.415558317986,0.63712845935,0.332344594425,0.442969092817,0.470591065989,0.387515871614,0.471018079028,0.442924852727,0.498662364593,0.692356633141,0.415277104894,0.415177083822,0.553747046615,0.387586655757,0.276816049661,0.553855146312,0.470761871205,0.470706090222,0.470646846972,0.359937638426,0.443366099534,0.498403848591,0.24915945381,0.470974993028,0.58118975125,0.664599246825,0.802956472491,0.332367099166,0.332449270324,0.470991150278,0.637122688904,0.387810933777,0.442695958351,0.442578625939,0.387468938649,0.221409607544])

    # Creating weights for histo: y3_PHI_8
    y3_PHI_8_weights = numpy.array([0.0806149621864,0.201576878611,0.251935387355,0.191623214003,0.171407381381,0.161230106417,0.201732647345,0.282402101282,0.20168580143,0.211755609925,0.201596782056,0.211697537981,0.131100840847,0.201553698378,0.191487409395,0.221775477761,0.191555433062,0.161254257549,0.151356541041,0.181452128525,0.191598759465,0.161273190095,0.242050838676,0.141209546014,0.121075754424,0.171357683448,0.181438475246,0.252077624174,0.151176560494,0.171384322511,0.231868405807,0.221751144585,0.211571806459,0.120998628572,0.151219158722,0.161426228173,0.201501148427,0.211811618706,0.161242788795,0.221893927535,0.16139564483,0.161362998325,0.151272315485,0.201556307671,0.221755331591,0.181461776841,0.161342002617,0.181529679145,0.141150988621,0.171314478408,0.151257145176,0.181539024056,0.181474095132,0.221837493985,0.221732333402,0.181531924351,0.181393692494,0.221874630902,0.191489533239,0.19151022554,0.221827056812,0.211811497344,0.21173625261,0.0806095615564])

    # Creating weights for histo: y3_PHI_9
    y3_PHI_9_weights = numpy.array([0.0395865298968,0.101896417406,0.0933459470188,0.10755542289,0.101887760786,0.0990355007525,0.0905088072143,0.107469703118,0.0764095974419,0.0990157251855,0.076367160768,0.0905252740288,0.104680694119,0.0933839591981,0.0877324945915,0.0594129208436,0.115954767933,0.11883422899,0.0990057989282,0.0735334836114,0.101866061526,0.10463741102,0.0962214837413,0.104683117973,0.113136095584,0.110345047471,0.0961728912489,0.116031908034,0.0876683201835,0.10186421478,0.0763696615693,0.104683348816,0.124496889491,0.09903507754,0.101858943861,0.0792129956662,0.0735642242301,0.107568965691,0.101855789004,0.0933922695531,0.127272394163,0.0962306405213,0.141420850484,0.113159680064,0.0933661073244,0.101836167332,0.0820426330669,0.067894292168,0.087728916522,0.107515487018,0.0792351950867,0.127270047257,0.0820197026429,0.11598608566,0.0933831127731,0.11034743285,0.104693428969,0.0905193875274,0.0735282511657,0.118861353065,0.0678698997371,0.0735311751795,0.11319676887,0.0367563115407])

    # Creating weights for histo: y3_PHI_10
    y3_PHI_10_weights = numpy.array([0.00306015899345,0.0182543951546,0.0167479645438,0.00915157423036,0.0167713688717,0.0167601570054,0.0167717351182,0.0152574243021,0.00760106409042,0.0136973681264,0.0121782961068,0.0167592472966,0.0152516352457,0.0198134471063,0.0045782551435,0.0106577969077,0.00911448646353,0.0137284754435,0.015246838599,0.0137367809673,0.0106357583245,0.00763448466726,0.0121541711005,0.00759903910213,0.00913771475684,0.0167294986355,0.0106478527265,0.0198058386322,0.015221425823,0.00912230995971,0.0167406514298,0.0197317977827,0.0182461014453,0.0136948989166,0.0106832982917,0.0137145817083,0.00914706821792,0.00912661512734,0.0121802336685,0.0137045867252,0.0137233361792,0.0213243081173,0.0091622591744,0.0137228163456,0.0106459966842,0.0107082503061,0.0121744446122,0.00913460993233,0.0136791030628,0.0076148987537,0.0060918275595,0.0122106911937,0.0107153956556,0.0137294087812,0.0137341699847,0.00759467368106,0.0289543907388,0.0228722427179,0.0152048384044,0.0137033462131,0.0076473363724,0.0122128414146,0.0152063742765,0.00760014138572])

    # Creating weights for histo: y3_PHI_11
    y3_PHI_11_weights = numpy.array([0.00144489876295,0.00270880642445,0.00216676624261,0.00234565618175,0.00216701271327,0.00306899709378,0.00144438810656,0.00126259135418,0.00144487142011,0.00126348095919,0.00162558832295,0.00180636299235,0.00108307907665,0.00216732080158,0.00234741151492,0.00216687599908,0.00162421578951,0.00198617681131,0.00108246405536,0.00198672713407,0.00108414044089,0.00234824181293,0.00126383911186,0.00252680094224,0.00180588545546,0.00270846252087,0.00198696513229,0.00144512251208,0.00198423007828,0.00180540830368,0.00234771536702,0.00162428125827,0.00252762430826,0.00162606932583,0.00234602550262,0.00252726538537,0.00270806008051,0.00216740899186,0.00361206744592,0.00252833522204,0.00180495117765,0.00198636705585,0.00288848006324,0.00198667783994,0.00271090258032,0.00198777501944,0.00198629272954,0.002167276899,0.00216627214598,0.00198564882497,0.00252838952261,0.00234748622634,0.00306922584936,0.00234714732919,0.00198830300579,0.00270864583342,0.00144451365255,0.0030701204608,0.00198650723603,0.00180293319919,0.00198504728253,0.00216522734149,0.00162565417682,0.000721566708453])

    # Creating weights for histo: y3_PHI_12
    y3_PHI_12_weights = numpy.array([0.0,0.0,0.0121240822392,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.012170493784,0.0,0.0,0.0121753353338,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0121313846429,0.0,0.0,0.0,0.0,0.0])

    # Creating weights for histo: y3_PHI_13
    y3_PHI_13_weights = numpy.array([0.0100532490873,0.0300951759264,0.0100532490873,0.0,0.0,0.0402072404221,0.0100187052616,0.0301548136101,0.020069144564,0.0301576895076,0.0301620033537,0.0100309732782,0.0200612482421,0.0,0.0200599135943,0.0,0.0401530735548,0.0200979572549,0.0300918165807,0.0301138816559,0.0200670124331,0.0100696698006,0.0100602900776,0.0100324442832,0.040238875294,0.0201002505352,0.0100187052616,0.0501717250999,0.0100329194674,0.0300870275503,0.0201006430787,0.0,0.0100457329128,0.0301051423986,0.0,0.0100340929658,0.0200736526159,0.0301062497844,0.0201025934,0.0100187052616,0.0100340929658,0.0200731732996,0.060241456881,0.0200748219822,0.0300982790859,0.0200996265977,0.0401535570031,0.0,0.0100340929658,0.0,0.0,0.010015362444,0.0200870982629,0.0200455754274,0.0200864619292,0.0100299567972,0.0200840157636,0.0100309732782,0.0100340929658,0.0,0.0300997129026,0.0301702674269,0.020078863114,0.0100324442832])

    # Creating weights for histo: y3_PHI_14
    y3_PHI_14_weights = numpy.array([0.065957788021,0.132061100916,0.126500360668,0.110037158518,0.104549627601,0.14305887308,0.104460451973,0.0935357266329,0.104522854599,0.104367173048,0.126481997396,0.110068847351,0.0825098814125,0.110046543287,0.0990558401707,0.0879956653807,0.14852117481,0.121007710786,0.0880366577307,0.0769747359921,0.0989970939487,0.131998170143,0.126459165185,0.115576772876,0.115499338367,0.093531379575,0.126485450666,0.0770109343903,0.0880088284346,0.143059401227,0.087953088589,0.110019323392,0.0935194353224,0.0715355914865,0.0935425519201,0.143085524201,0.0769745734853,0.115469030842,0.137468922228,0.137454255986,0.121054350249,0.0880390547065,0.110003478975,0.120932185733,0.109985034449,0.13750853327,0.0660089776751,0.104471502438,0.11002033906,0.0715331132572,0.109953142482,0.0604229676143,0.0990091194547,0.109886799065,0.104501525577,0.104575181801,0.0825125627753,0.154032797366,0.0439766661747,0.115565641158,0.104511438494,0.0880189038586,0.088041370429,0.0549764290476])

    # Creating weights for histo: y3_PHI_15
    y3_PHI_15_weights = numpy.array([0.0444090014736,0.107563633571,0.0907796179619,0.0957358233388,0.0986967841827,0.101652654504,0.113489082551,0.0818956131099,0.122373007237,0.116447718589,0.10160058687,0.0987052817487,0.10361835797,0.121380675908,0.107558583131,0.128287633845,0.0957365849131,0.097692989156,0.0937506396033,0.102625705978,0.10854558344,0.106585732071,0.117436001549,0.121366486576,0.0907745675217,0.0996619794166,0.116459302535,0.111516324501,0.116464473224,0.115482483272,0.0957265641984,0.0927730186833,0.0976911854274,0.0868341018633,0.106583768011,0.104585437098,0.10857544517,0.114448145107,0.102587426848,0.0986830758451,0.110515856352,0.0927793918578,0.111526665879,0.113463349356,0.106594911046,0.124348490921,0.127328290708,0.110547201147,0.128291401633,0.0917880225173,0.12334730128,0.119389559909,0.119411284819,0.0848804633376,0.116459102121,0.0996645046367,0.100665373615,0.111512396381,0.0957502932507,0.0927692508946,0.0907950498624,0.121374182485,0.101645078843,0.0483564415494])

    # Creating weights for histo: y3_PHI_16
    y3_PHI_16_weights = numpy.array([0.020675832506,0.0436089615331,0.0463768979025,0.045375071381,0.0451286058124,0.0506653987961,0.0456317796746,0.0547041932589,0.0446154692999,0.0504074501726,0.0431111490973,0.0514288018884,0.0486460615806,0.0443713643593,0.0476343924407,0.0544362019637,0.0514184391315,0.0486545838479,0.0541958580236,0.0524247868558,0.0511788954044,0.0491543968159,0.0468867935528,0.047131058536,0.0478951418093,0.0536952848534,0.0496618918276,0.0504127315776,0.0468817522117,0.0468901544469,0.0536929242254,0.0501707472012,0.0436070810328,0.0468843529035,0.0431061077561,0.0496564103693,0.0476363129516,0.0468885540212,0.0463847399887,0.0436094416608,0.0504168126633,0.0531823083834,0.0483986357566,0.0451238845564,0.044370044008,0.0524269474306,0.0463842998717,0.0489051305022,0.0448666161139,0.0506649986896,0.0506784022554,0.0463834996588,0.0504109711093,0.0458844068824,0.0504144120247,0.0491621188702,0.0504202135681,0.0468813921159,0.0468822323394,0.0481430877717,0.0451271254186,0.0473866065208,0.0458778051261,0.0189066898512])

    # Creating weights for histo: y3_PHI_17
    y3_PHI_17_weights = numpy.array([0.0103077483659,0.0249209804149,0.0231858877469,0.0257753146222,0.0237583632502,0.0191842379888,0.0231833183056,0.023471295679,0.0289263193707,0.0266195210319,0.0208933763011,0.0217711354142,0.0231921563836,0.0289218203491,0.0243415064336,0.0254895767618,0.0254810386186,0.026056893387,0.0260530442241,0.0263566481991,0.0269133971225,0.0254839579837,0.0200496997761,0.0323627220535,0.0254700510081,0.0234863324089,0.0266188111863,0.0240588579014,0.0223223055508,0.0257777141004,0.0231976651856,0.0237547940264,0.0226261194801,0.0234619277162,0.0214624525437,0.0231813087427,0.024333848099,0.0255028838679,0.0300458159129,0.0249171612455,0.0271948959047,0.0263236053849,0.0237618324957,0.0266333980141,0.0257692559398,0.0271992449589,0.0254793289904,0.0260414967353,0.0260740296604,0.0234529396709,0.0280575183095,0.0243242301906,0.0240597177144,0.0306281492724,0.0271960956438,0.0292098277159,0.0237595629893,0.0263548385926,0.0272027342001,0.0263345829976,0.0240543588798,0.0223163168531,0.0251888221671,0.0111588332798])

    # Creating weights for histo: y3_PHI_18
    y3_PHI_18_weights = numpy.array([0.00135902406478,0.0042119430902,0.00345569642331,0.00390628157679,0.00362856582063,0.00341103786351,0.00341314807643,0.00325865911567,0.00410343916866,0.00375691035388,0.00399291849546,0.00403915206622,0.00386362929093,0.00321814428481,0.00349631938424,0.00345380330875,0.00380043815807,0.00313245748585,0.0043386187321,0.00358633096716,0.00421055583999,0.00334653659646,0.00379806600213,0.00315214805659,0.00366812717892,0.00373385308195,0.00384479579773,0.00384491566285,0.00401789025649,0.00354234465792,0.00360811666292,0.00416599912364,0.00436186250746,0.00388601976072,0.00395235504798,0.00388730181461,0.00362913077933,0.00317416384309,0.00403649156341,0.00395280014155,0.00377773335666,0.00364896258975,0.00427664091928,0.00408276201574,0.00375708218849,0.00416737128592,0.00386596163154,0.00367167996442,0.00321862877461,0.00379930069672,0.00364943157252,0.00397319481512,0.00382350213573,0.00377999863985,0.00380140210836,0.00356138686731,0.00423379542425,0.00347769963654,0.00364711767271,0.00358305353616,0.00408215807993,0.00362839691978,0.00392851907186,0.00146871364518])

    # Creating weights for histo: y3_PHI_19
    y3_PHI_19_weights = numpy.array([0.00042567839908,0.000795090956149,0.000594508007593,0.000593348285261,0.00059622843072,0.000510786838492,0.00079509957089,0.000594142772294,0.000820635593169,0.000708762045631,0.00084872143016,0.000567634472558,0.000822892209638,0.000623556616121,0.000652571211276,0.000653067895636,0.000512617916477,0.000794789737285,0.000733777618748,0.000877595961514,0.000567844048405,0.000624684701561,0.000907055701115,0.000396361248291,0.000652755834081,0.00102207006428,0.000539561260618,0.000709188326764,0.000397443140897,0.000820415174631,0.000623147564469,0.000624401306298,0.000625460176752,0.000652888174321,0.000594160595896,0.000650847966079,0.00076539757884,0.00113149999607,0.00062606528802,0.000651421143395,0.000651259542742,0.000709832501426,0.000765170327922,0.000709304031644,0.000851823627987,0.000821263578059,0.000822419735671,0.000765308757893,0.000681614027134,0.000962656277202,0.000537315932429,0.000681260674236,0.000623181577841,0.000734269104557,0.000536770678756,0.000567596597405,0.00085098101723,0.000737376203874,0.000990775681976,0.000765655278411,0.000852917551524,0.000737495770533,0.000651718946069,0.000282729551003])

    # Creating a new Canvas
    fig   = plt.figure(figsize=(12,6),dpi=80)
    frame = gridspec.GridSpec(1,1,right=0.7)
    pad   = fig.add_subplot(frame[0])

    # Creating a new Stack
    pad.hist(x=xData, bins=xBinning, weights=y3_PHI_0_weights+y3_PHI_1_weights+y3_PHI_2_weights+y3_PHI_3_weights+y3_PHI_4_weights+y3_PHI_5_weights+y3_PHI_6_weights+y3_PHI_7_weights+y3_PHI_8_weights+y3_PHI_9_weights+y3_PHI_10_weights+y3_PHI_11_weights+y3_PHI_12_weights+y3_PHI_13_weights+y3_PHI_14_weights+y3_PHI_15_weights+y3_PHI_16_weights+y3_PHI_17_weights+y3_PHI_18_weights+y3_PHI_19_weights,\
             label="$bg\_vbf\_1600\_inf$", histtype="step", rwidth=1.0,\
             color=None, edgecolor="#ccc6aa", linewidth=1, linestyle="solid",\
             bottom=None, cumulative=False, normed=False, align="mid", orientation="vertical")

    pad.hist(x=xData, bins=xBinning, weights=y3_PHI_0_weights+y3_PHI_1_weights+y3_PHI_2_weights+y3_PHI_3_weights+y3_PHI_4_weights+y3_PHI_5_weights+y3_PHI_6_weights+y3_PHI_7_weights+y3_PHI_8_weights+y3_PHI_9_weights+y3_PHI_10_weights+y3_PHI_11_weights+y3_PHI_12_weights+y3_PHI_13_weights+y3_PHI_14_weights+y3_PHI_15_weights+y3_PHI_16_weights+y3_PHI_17_weights+y3_PHI_18_weights,\
             label="$bg\_vbf\_1200\_1600$", histtype="step", rwidth=1.0,\
             color=None, edgecolor="#c1bfa8", linewidth=1, linestyle="solid",\
             bottom=None, cumulative=False, normed=False, align="mid", orientation="vertical")

    pad.hist(x=xData, bins=xBinning, weights=y3_PHI_0_weights+y3_PHI_1_weights+y3_PHI_2_weights+y3_PHI_3_weights+y3_PHI_4_weights+y3_PHI_5_weights+y3_PHI_6_weights+y3_PHI_7_weights+y3_PHI_8_weights+y3_PHI_9_weights+y3_PHI_10_weights+y3_PHI_11_weights+y3_PHI_12_weights+y3_PHI_13_weights+y3_PHI_14_weights+y3_PHI_15_weights+y3_PHI_16_weights+y3_PHI_17_weights,\
             label="$bg\_vbf\_800\_1200$", histtype="step", rwidth=1.0,\
             color=None, edgecolor="#bab5a3", linewidth=1, linestyle="solid",\
             bottom=None, cumulative=False, normed=False, align="mid", orientation="vertical")

    pad.hist(x=xData, bins=xBinning, weights=y3_PHI_0_weights+y3_PHI_1_weights+y3_PHI_2_weights+y3_PHI_3_weights+y3_PHI_4_weights+y3_PHI_5_weights+y3_PHI_6_weights+y3_PHI_7_weights+y3_PHI_8_weights+y3_PHI_9_weights+y3_PHI_10_weights+y3_PHI_11_weights+y3_PHI_12_weights+y3_PHI_13_weights+y3_PHI_14_weights+y3_PHI_15_weights+y3_PHI_16_weights,\
             label="$bg\_vbf\_600\_800$", histtype="step", rwidth=1.0,\
             color=None, edgecolor="#b2a596", linewidth=1, linestyle="solid",\
             bottom=None, cumulative=False, normed=False, align="mid", orientation="vertical")

    pad.hist(x=xData, bins=xBinning, weights=y3_PHI_0_weights+y3_PHI_1_weights+y3_PHI_2_weights+y3_PHI_3_weights+y3_PHI_4_weights+y3_PHI_5_weights+y3_PHI_6_weights+y3_PHI_7_weights+y3_PHI_8_weights+y3_PHI_9_weights+y3_PHI_10_weights+y3_PHI_11_weights+y3_PHI_12_weights+y3_PHI_13_weights+y3_PHI_14_weights+y3_PHI_15_weights,\
             label="$bg\_vbf\_400\_600$", histtype="step", rwidth=1.0,\
             color=None, edgecolor="#b7a39b", linewidth=1, linestyle="solid",\
             bottom=None, cumulative=False, normed=False, align="mid", orientation="vertical")

    pad.hist(x=xData, bins=xBinning, weights=y3_PHI_0_weights+y3_PHI_1_weights+y3_PHI_2_weights+y3_PHI_3_weights+y3_PHI_4_weights+y3_PHI_5_weights+y3_PHI_6_weights+y3_PHI_7_weights+y3_PHI_8_weights+y3_PHI_9_weights+y3_PHI_10_weights+y3_PHI_11_weights+y3_PHI_12_weights+y3_PHI_13_weights+y3_PHI_14_weights,\
             label="$bg\_vbf\_200\_400$", histtype="step", rwidth=1.0,\
             color=None, edgecolor="#ad998c", linewidth=1, linestyle="solid",\
             bottom=None, cumulative=False, normed=False, align="mid", orientation="vertical")

    pad.hist(x=xData, bins=xBinning, weights=y3_PHI_0_weights+y3_PHI_1_weights+y3_PHI_2_weights+y3_PHI_3_weights+y3_PHI_4_weights+y3_PHI_5_weights+y3_PHI_6_weights+y3_PHI_7_weights+y3_PHI_8_weights+y3_PHI_9_weights+y3_PHI_10_weights+y3_PHI_11_weights+y3_PHI_12_weights+y3_PHI_13_weights,\
             label="$bg\_vbf\_100\_200$", histtype="step", rwidth=1.0,\
             color=None, edgecolor="#9b8e82", linewidth=1, linestyle="solid",\
             bottom=None, cumulative=False, normed=False, align="mid", orientation="vertical")

    pad.hist(x=xData, bins=xBinning, weights=y3_PHI_0_weights+y3_PHI_1_weights+y3_PHI_2_weights+y3_PHI_3_weights+y3_PHI_4_weights+y3_PHI_5_weights+y3_PHI_6_weights+y3_PHI_7_weights+y3_PHI_8_weights+y3_PHI_9_weights+y3_PHI_10_weights+y3_PHI_11_weights+y3_PHI_12_weights,\
             label="$bg\_vbf\_0\_100$", histtype="step", rwidth=1.0,\
             color=None, edgecolor="#876656", linewidth=1, linestyle="solid",\
             bottom=None, cumulative=False, normed=False, align="mid", orientation="vertical")

    pad.hist(x=xData, bins=xBinning, weights=y3_PHI_0_weights+y3_PHI_1_weights+y3_PHI_2_weights+y3_PHI_3_weights+y3_PHI_4_weights+y3_PHI_5_weights+y3_PHI_6_weights+y3_PHI_7_weights+y3_PHI_8_weights+y3_PHI_9_weights+y3_PHI_10_weights+y3_PHI_11_weights,\
             label="$bg\_dip\_1600\_inf$", histtype="step", rwidth=1.0,\
             color=None, edgecolor="#afcec6", linewidth=1, linestyle="solid",\
             bottom=None, cumulative=False, normed=False, align="mid", orientation="vertical")

    pad.hist(x=xData, bins=xBinning, weights=y3_PHI_0_weights+y3_PHI_1_weights+y3_PHI_2_weights+y3_PHI_3_weights+y3_PHI_4_weights+y3_PHI_5_weights+y3_PHI_6_weights+y3_PHI_7_weights+y3_PHI_8_weights+y3_PHI_9_weights+y3_PHI_10_weights,\
             label="$bg\_dip\_1200\_1600$", histtype="step", rwidth=1.0,\
             color=None, edgecolor="#84c1a3", linewidth=1, linestyle="solid",\
             bottom=None, cumulative=False, normed=False, align="mid", orientation="vertical")

    pad.hist(x=xData, bins=xBinning, weights=y3_PHI_0_weights+y3_PHI_1_weights+y3_PHI_2_weights+y3_PHI_3_weights+y3_PHI_4_weights+y3_PHI_5_weights+y3_PHI_6_weights+y3_PHI_7_weights+y3_PHI_8_weights+y3_PHI_9_weights,\
             label="$bg\_dip\_800\_1200$", histtype="step", rwidth=1.0,\
             color=None, edgecolor="#89a8a0", linewidth=1, linestyle="solid",\
             bottom=None, cumulative=False, normed=False, align="mid", orientation="vertical")

    pad.hist(x=xData, bins=xBinning, weights=y3_PHI_0_weights+y3_PHI_1_weights+y3_PHI_2_weights+y3_PHI_3_weights+y3_PHI_4_weights+y3_PHI_5_weights+y3_PHI_6_weights+y3_PHI_7_weights+y3_PHI_8_weights,\
             label="$bg\_dip\_600\_800$", histtype="step", rwidth=1.0,\
             color=None, edgecolor="#829e8c", linewidth=1, linestyle="solid",\
             bottom=None, cumulative=False, normed=False, align="mid", orientation="vertical")

    pad.hist(x=xData, bins=xBinning, weights=y3_PHI_0_weights+y3_PHI_1_weights+y3_PHI_2_weights+y3_PHI_3_weights+y3_PHI_4_weights+y3_PHI_5_weights+y3_PHI_6_weights+y3_PHI_7_weights,\
             label="$bg\_dip\_400\_600$", histtype="step", rwidth=1.0,\
             color=None, edgecolor="#adbcc6", linewidth=1, linestyle="solid",\
             bottom=None, cumulative=False, normed=False, align="mid", orientation="vertical")

    pad.hist(x=xData, bins=xBinning, weights=y3_PHI_0_weights+y3_PHI_1_weights+y3_PHI_2_weights+y3_PHI_3_weights+y3_PHI_4_weights+y3_PHI_5_weights+y3_PHI_6_weights,\
             label="$bg\_dip\_200\_400$", histtype="step", rwidth=1.0,\
             color=None, edgecolor="#7a8e99", linewidth=1, linestyle="solid",\
             bottom=None, cumulative=False, normed=False, align="mid", orientation="vertical")

    pad.hist(x=xData, bins=xBinning, weights=y3_PHI_0_weights+y3_PHI_1_weights+y3_PHI_2_weights+y3_PHI_3_weights+y3_PHI_4_weights+y3_PHI_5_weights,\
             label="$bg\_dip\_100\_200$", histtype="step", rwidth=1.0,\
             color=None, edgecolor="#758991", linewidth=1, linestyle="solid",\
             bottom=None, cumulative=False, normed=False, align="mid", orientation="vertical")

    pad.hist(x=xData, bins=xBinning, weights=y3_PHI_0_weights+y3_PHI_1_weights+y3_PHI_2_weights+y3_PHI_3_weights+y3_PHI_4_weights,\
             label="$bg\_dip\_0\_100$", histtype="step", rwidth=1.0,\
             color=None, edgecolor="#688296", linewidth=1, linestyle="solid",\
             bottom=None, cumulative=False, normed=False, align="mid", orientation="vertical")

    pad.hist(x=xData, bins=xBinning, weights=y3_PHI_0_weights+y3_PHI_1_weights+y3_PHI_2_weights+y3_PHI_3_weights,\
             label="$signal\_2pt4TeVL$", histtype="step", rwidth=1.0,\
             color=None, edgecolor="#6d7a84", linewidth=1, linestyle="solid",\
             bottom=None, cumulative=False, normed=False, align="mid", orientation="vertical")

    pad.hist(x=xData, bins=xBinning, weights=y3_PHI_0_weights+y3_PHI_1_weights+y3_PHI_2_weights,\
             label="$signal\_2pt2TeVL$", histtype="step", rwidth=1.0,\
             color=None, edgecolor="#7c99d1", linewidth=1, linestyle="solid",\
             bottom=None, cumulative=False, normed=False, align="mid", orientation="vertical")

    pad.hist(x=xData, bins=xBinning, weights=y3_PHI_0_weights+y3_PHI_1_weights,\
             label="$signal\_2TeVL$", histtype="step", rwidth=1.0,\
             color=None, edgecolor="#7f7f9b", linewidth=1, linestyle="solid",\
             bottom=None, cumulative=False, normed=False, align="mid", orientation="vertical")

    pad.hist(x=xData, bins=xBinning, weights=y3_PHI_0_weights,\
             label="$signal\_1pt8TeVL$", histtype="step", rwidth=1.0,\
             color=None, edgecolor="#aaa5bf", linewidth=1, linestyle="solid",\
             bottom=None, cumulative=False, normed=False, align="mid", orientation="vertical")


    # Axis
    plt.rc('text',usetex=False)
    plt.xlabel(r"\phi [ j_{1} ] ",\
               fontsize=16,color="black")
    plt.ylabel(r"$\mathrm{Events}$ $(\mathcal{L}_{\mathrm{int}} = 40.0\ \mathrm{fb}^{-1})$ ",\
               fontsize=16,color="black")

    # Boundary of y-axis
    ymax=(y3_PHI_0_weights+y3_PHI_1_weights+y3_PHI_2_weights+y3_PHI_3_weights+y3_PHI_4_weights+y3_PHI_5_weights+y3_PHI_6_weights+y3_PHI_7_weights+y3_PHI_8_weights+y3_PHI_9_weights+y3_PHI_10_weights+y3_PHI_11_weights+y3_PHI_12_weights+y3_PHI_13_weights+y3_PHI_14_weights+y3_PHI_15_weights+y3_PHI_16_weights+y3_PHI_17_weights+y3_PHI_18_weights+y3_PHI_19_weights).max()*1.1
    ymin=0 # linear scale
    #ymin=min([x for x in (y3_PHI_0_weights+y3_PHI_1_weights+y3_PHI_2_weights+y3_PHI_3_weights+y3_PHI_4_weights+y3_PHI_5_weights+y3_PHI_6_weights+y3_PHI_7_weights+y3_PHI_8_weights+y3_PHI_9_weights+y3_PHI_10_weights+y3_PHI_11_weights+y3_PHI_12_weights+y3_PHI_13_weights+y3_PHI_14_weights+y3_PHI_15_weights+y3_PHI_16_weights+y3_PHI_17_weights+y3_PHI_18_weights+y3_PHI_19_weights) if x])/100. # log scale
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
