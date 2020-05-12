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
    xBinning = numpy.linspace(0.0,2000.0,81,endpoint=True)

    # Creating data sequence: middle of each bin
    xData = numpy.array([12.5,37.5,62.5,87.5,112.5,137.5,162.5,187.5,212.5,237.5,262.5,287.5,312.5,337.5,362.5,387.5,412.5,437.5,462.5,487.5,512.5,537.5,562.5,587.5,612.5,637.5,662.5,687.5,712.5,737.5,762.5,787.5,812.5,837.5,862.5,887.5,912.5,937.5,962.5,987.5,1012.5,1037.5,1062.5,1087.5,1112.5,1137.5,1162.5,1187.5,1212.5,1237.5,1262.5,1287.5,1312.5,1337.5,1362.5,1387.5,1412.5,1437.5,1462.5,1487.5,1512.5,1537.5,1562.5,1587.5,1612.5,1637.5,1662.5,1687.5,1712.5,1737.5,1762.5,1787.5,1812.5,1837.5,1862.5,1887.5,1912.5,1937.5,1962.5,1987.5])

    # Creating weights for histo: y12_PT_0
    y12_PT_0_weights = numpy.array([0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,25.7517901873,27.8029244499,29.7803667749,31.4507533601,31.4139053913,31.0331577138,31.1764495924,30.7547579496,29.6780148616,29.6902988512,27.9011843667,26.857189251,25.9155500486,24.6709511028,23.4509121362,22.4683329685,20.3926307267,19.8808711602,18.7017761589,17.4367052305,16.163442309,15.3896629644,14.4684917447,13.5841724937,12.7817291734,12.0734537733,11.3365183976,10.1697033859,9.6743198055,9.08068030833,8.43790885278,8.04078118916,6.98450608387,6.68154634048,6.37449060057,5.95689095429,5.49425934616,5.08894768947,4.60584409868,4.45436422699,3.79112198878,3.52091221766,3.6027937483,3.20157368815,3.11150376444,2.92317592396,2.4441683297,2.30087525107,2.18214695164,1.98972471463,1.94878394931,1.91193718052,1.64582180593,1.60078704407,1.31010689029,1.25688373537,1.19956658392,1.07264989143,1.02352113304,0.900698437075,0.9293572128,0.753311361918,0.728746982725,0.708276600064,0.695994210467,0.642771055549,0.56907751797,0.458537211602])

    # Creating weights for histo: y12_PT_1
    y12_PT_1_weights = numpy.array([0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0242945760233,0.0121753353338,0.0,0.0,0.0,0.0,0.0121313846429,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0])

    # Creating weights for histo: y12_PT_2
    y12_PT_2_weights = numpy.array([0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.341428826021,0.34122243079,0.0903653279136,0.0802686550033,0.0903492956113,0.0602618293179,0.0301763877224,0.0401299144865,0.010034093215,0.0301425504742,0.0,0.0201115108343,0.0200893011373,0.0,0.0,0.0100696700506,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0])

    # Creating weights for histo: y12_PT_3
    y12_PT_3_weights = numpy.array([0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,1.38044092341,1.08899205374,0.836121009257,0.660124484831,0.495072949174,0.456550375028,0.34670763614,0.203467507781,0.153889727152,0.0935118698771,0.0660347114052,0.0494884851857,0.0439890559155,0.049519035765,0.0274872580384,0.0165081111218,0.0220364537527,0.010991956222,0.00550370716379,0.0,0.0,0.00547920982432,0.00550414592211,0.00549442823786,0.0,0.00548474305423,0.00549598014229,0.0,0.00548806217966,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.00551421705056,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0])

    # Creating weights for histo: y12_PT_4
    y12_PT_4_weights = numpy.array([0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.548706381244,0.489429390329,0.505215637913,0.456941000998,0.428327425179,0.380948480648,0.339477554506,0.269420188667,0.24079390657,0.174653040455,0.15492528142,0.106574647335,0.0947513555508,0.0582105854792,0.0424269032005,0.0286317093204,0.0305976991897,0.0207222517484,0.0108564121772,0.0108645249553,0.00592194719602,0.0108544280739,0.00394836041553,0.00197208166777,0.00296049140078,0.0019739856053,0.00296333808802,0.0,0.000987659381206,0.0,0.000984219467109,0.00295751484495,0.00197603504375,0.000983908824669,0.0,0.0,0.0,0.000985428768068,0.0,0.0,0.0,0.00197503216971,0.0,0.000983908824669,0.0,0.0,0.0,0.0,0.0,0.0,0.000986794392319,0.0,0.0,0.0,0.000986290550322,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0])

    # Creating weights for histo: y12_PT_5
    y12_PT_5_weights = numpy.array([0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.113677409924,0.10814789873,0.101840849414,0.103606424711,0.106124211025,0.101832927191,0.0978062375842,0.0983018966314,0.0945228765029,0.0889866434234,0.092005570323,0.0814352450296,0.0731011870763,0.0652860747028,0.0579707825438,0.0589823863291,0.0446190769898,0.0385732529548,0.0292436437195,0.0216812022277,0.0128554623429,0.013106020632,0.00831931381714,0.00580000307488,0.00378229104612,0.00302591325946,0.00529442924626,0.000756058497093,0.00176474546405,0.0015125095043,0.00100942717461,0.00126115379148,0.000504342683255,0.000252130810257,0.000503856946991,0.000252358434112,0.000251770949305,0.0,0.000251614665463,0.0,0.000251614665463,0.000252082356664,0.0,0.0,0.000252086197742,0.000252017858571,0.000252186585904,0.0,0.0,0.0,0.0,0.0,0.0,0.000251958161824,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0])

    # Creating weights for histo: y12_PT_6
    y12_PT_6_weights = numpy.array([0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0254973009635,0.0226304206519,0.0197474649926,0.0209041502425,0.0220445801968,0.0237529657822,0.021179420578,0.0268989853096,0.024911140601,0.019446632055,0.0266277638024,0.0203386039142,0.0229137686497,0.0220418409896,0.0203385239374,0.0263385375058,0.0209026606736,0.0234857331205,0.019188816668,0.0220435305006,0.0206220918715,0.0186141329841,0.0197595714889,0.0120269193541,0.0157348362658,0.0160283613183,0.0120353069267,0.00858937819435,0.0102972799197,0.00859092074792,0.00772929410665,0.004862738701,0.0040044710876,0.00543648165714,0.00228820378327,0.00085790951703,0.000854948373998,0.000858374382496,0.000284540452681,0.000286183777095,0.0,0.000862325339071,0.0,0.0,0.0,0.000857851133926,0.0,0.0,0.000286183777095,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0])

    # Creating weights for histo: y12_PT_7
    y12_PT_7_weights = numpy.array([0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0016631212549,0.00168467784916,0.00133921201026,0.00153329344308,0.0010364620574,0.001339070356,0.0012082245613,0.00122929626212,0.000863925065078,0.00116633932248,0.00110194823816,0.00118795291373,0.00105846540743,0.000842506772315,0.00107982125497,0.00101511501086,0.000863801012821,0.000799543200862,0.00103708818602,0.000842255734132,0.000863821967594,0.00127451750083,0.000842979092902,0.00107845668014,0.00103657227951,0.000972192510767,0.000993464539214,0.00107961044995,0.000972299799206,0.0009938907593,0.00127405523854,0.0014673659548,0.00131813108935,0.00144738054942,0.00131747436676,0.00170117135113,0.00146898785424,0.00142542036623,0.00168464390243,0.00114189935142,0.00125280332667,0.0012098787311,0.000864098989696,0.000927304872041,0.000799187388814,0.000518219503574,0.000453610908712,0.000345750949543,0.000300814947201,0.000237746360529,0.000259019604353,8.64930056e-05,8.64363438933e-05,0.000129582054234,2.15827542054e-05,0.0,0.0,4.32204350622e-05,2.15933950392e-05,0.0,0.0,0.0,2.16751857099e-05,2.16220821237e-05,0.0,0.0,0.0,0.0])

    # Creating weights for histo: y12_PT_8
    y12_PT_8_weights = numpy.array([0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.000113736721231,8.51343815685e-05,5.67987805063e-05,0.0,8.52347723319e-05,8.48750375258e-05,2.8257334576e-05,0.0,5.68463105807e-05,0.000113621481959,0.000113625446511,0.000113120359659,8.50232107883e-05,0.0,8.52544169081e-05,0.000141943452091,0.000113632172885,5.6826680853e-05,2.83498704786e-05,2.83498704786e-05,5.68174005354e-05,5.66824721422e-05,0.0,2.83498704786e-05,0.0,5.67183461378e-05,2.84080914789e-05,0.0,5.68570015066e-05,0.0,5.67183461378e-05,5.66456775391e-05,0.000113236430447,2.84292654515e-05,5.6826680853e-05,8.52148010885e-05,2.83684905078e-05,0.000113196814627,8.51450724944e-05,0.000113704856332,8.51951565123e-05,2.83684905078e-05,0.000113724500908,0.000196602562578,5.6826680853e-05,2.8397400553e-05,0.000140565941145,0.000113406223137,5.68373717789e-05,0.000113724500908,0.00028375395064,0.000170223593975,0.000142033552838,8.52135983593e-05,5.677913593e-05,0.00011328894962,0.000141636236458,0.000170499627741,0.000170532888399,0.000141795679738,2.84489100277e-05,0.000140466174019,0.000141984983368,0.0,5.67977559592e-05,5.56796929953e-05,0.000113475120215,8.46724741782e-05])

    # Creating weights for histo: y12_PT_9
    y12_PT_9_weights = numpy.array([0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0])

    # Creating weights for histo: y12_PT_10
    y12_PT_10_weights = numpy.array([0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,1.05211370067,2.10758668394,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0])

    # Creating weights for histo: y12_PT_11
    y12_PT_11_weights = numpy.array([0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,3.22551702834,1.84358044477,4.37706148725,2.99361318568,2.76392619639,1.38204341062,0.460138675788,0.460448397371,0.689676184067,0.0,0.230128553894,0.230360191822,0.230673179699,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.230673179699,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0])

    # Creating weights for histo: y12_PT_12
    y12_PT_12_weights = numpy.array([0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,1.13513858326,0.830690226803,0.996880818839,1.07982109063,0.914237516547,0.747610702481,0.886215444211,0.886191979004,0.858309543879,0.692428230955,0.720020236069,0.803181696275,0.498131707321,0.304675699681,0.193693160093,0.0829900103302,0.0830284394138,0.221627487946,0.110640447655,0.0555005212398,0.0276381507887,0.0276586847675,0.0,0.0,0.0276696172456,0.0277263953511,0.0,0.0277307075636,0.0276929401219,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0])

    # Creating weights for histo: y12_PT_13
    y12_PT_13_weights = numpy.array([0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0806631152429,0.191564088543,0.120871080506,0.110910865544,0.100815011534,0.121051568438,0.131063004589,0.100821687281,0.151115371556,0.171450972275,0.191698756572,0.191582173749,0.221760132146,0.22164500585,0.332767067763,0.181451059656,0.201590089961,0.211758891682,0.141171603207,0.100829880244,0.0705497829126,0.0403589706674,0.0504321999629,0.0403172897288,0.0302705145991,0.010042957816,0.0605348268221,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0100805665487,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.010097516878,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0])

    # Creating weights for histo: y12_PT_14
    y12_PT_14_weights = numpy.array([0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0565646758237,0.0367998618393,0.036801708613,0.0282951922258,0.031109171233,0.0283022676773,0.0169679791924,0.019786940641,0.0141470593943,0.0254537693929,0.0339462002836,0.0311338410508,0.0339254510123,0.0311194477588,0.0396317237712,0.0311136342693,0.0226458731964,0.0452324495693,0.0537533477062,0.0679085598366,0.0537680064719,0.0565767952757,0.079195039969,0.104752925073,0.087716207427,0.0679047123915,0.0509162032322,0.0339433839538,0.0424435135822,0.0452375666713,0.0395992128603,0.0169686294106,0.00848347788602,0.0282822070987,0.0169854119661,0.0113239811795,0.0141381410166,0.0169797100525,0.00283012134774,0.0,0.00283097817376,0.00565362047301,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0])

    # Creating weights for histo: y12_PT_15
    y12_PT_15_weights = numpy.array([0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.00610087510698,0.00306963151122,0.0,0.00306733863696,0.0,0.0,0.0,0.00151727408562,0.00152449663954,0.00151265406217,0.0,0.00150849615926,0.0,0.00305525258944,0.0,0.00304862571007,0.00153629548684,0.0,0.00152162936482,0.0,0.00151265406217,0.0,0.0,0.0,0.00306015390365,0.00152644440077,0.00150849615926,0.00154541025297,0.0,0.00152260679112,0.0015209497758,0.0,0.0,0.00304258032252,0.00152162936482,0.00304044818583,0.00457795629586,0.00609317152222,0.00151265406217,0.0045406025376,0.00914378045033,0.00304377876298,0.00454491172294,0.0015209497758,0.00456340008998,0.00150849615926,0.0,0.00153333602439,0.00153333602439,0.00305826405522,0.00150849615926,0.00153821488261,0.00153153127233,0.0,0.00151115660254,0.00153821488261,0.0,0.0,0.0,0.0,0.0,0.00303715070171,0.0,0.0,0.0,0.0,0.0,0.0])

    # Creating weights for histo: y12_PT_16
    y12_PT_16_weights = numpy.array([0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.000180553030001,0.000180503367022,0.0,0.0,0.000180003618866,0.000180626138525,0.0,0.0,0.000180626138525,0.0,0.0,0.0,0.000180626138525,0.0,0.0,0.0,0.000180734319121,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.000180970237517,0.0,0.000179998691067,0.000180402039147,0.0,0.000361424095555,0.000180154571221,0.000180547139741,0.000180533819283,0.000361923458727,0.00054109046815,0.00126469084164,0.000180657129763,0.000360405658014,0.000721969964861,0.0,0.000361110679814,0.0,0.000361314067034,0.0,0.00018020300225,0.000180970237517,0.00072115148818,0.0,0.0,0.0])

    # Creating a new Canvas
    fig   = plt.figure(figsize=(12,6),dpi=80)
    frame = gridspec.GridSpec(1,1,right=0.7)
    pad   = fig.add_subplot(frame[0])

    # Creating a new Stack
    pad.hist(x=xData, bins=xBinning, weights=y12_PT_0_weights+y12_PT_1_weights+y12_PT_2_weights+y12_PT_3_weights+y12_PT_4_weights+y12_PT_5_weights+y12_PT_6_weights+y12_PT_7_weights+y12_PT_8_weights+y12_PT_9_weights+y12_PT_10_weights+y12_PT_11_weights+y12_PT_12_weights+y12_PT_13_weights+y12_PT_14_weights+y12_PT_15_weights+y12_PT_16_weights,\
             label="$bg\_dip\_1600\_inf$", histtype="step", rwidth=1.0,\
             color=None, edgecolor="#e5e5e5", linewidth=1, linestyle="solid",\
             bottom=None, cumulative=False, normed=False, align="mid", orientation="vertical")

    pad.hist(x=xData, bins=xBinning, weights=y12_PT_0_weights+y12_PT_1_weights+y12_PT_2_weights+y12_PT_3_weights+y12_PT_4_weights+y12_PT_5_weights+y12_PT_6_weights+y12_PT_7_weights+y12_PT_8_weights+y12_PT_9_weights+y12_PT_10_weights+y12_PT_11_weights+y12_PT_12_weights+y12_PT_13_weights+y12_PT_14_weights+y12_PT_15_weights,\
             label="$bg\_dip\_1200\_1600$", histtype="step", rwidth=1.0,\
             color=None, edgecolor="#f2f2f2", linewidth=1, linestyle="solid",\
             bottom=None, cumulative=False, normed=False, align="mid", orientation="vertical")

    pad.hist(x=xData, bins=xBinning, weights=y12_PT_0_weights+y12_PT_1_weights+y12_PT_2_weights+y12_PT_3_weights+y12_PT_4_weights+y12_PT_5_weights+y12_PT_6_weights+y12_PT_7_weights+y12_PT_8_weights+y12_PT_9_weights+y12_PT_10_weights+y12_PT_11_weights+y12_PT_12_weights+y12_PT_13_weights+y12_PT_14_weights,\
             label="$bg\_dip\_800\_1200$", histtype="step", rwidth=1.0,\
             color=None, edgecolor="#ccc6aa", linewidth=1, linestyle="solid",\
             bottom=None, cumulative=False, normed=False, align="mid", orientation="vertical")

    pad.hist(x=xData, bins=xBinning, weights=y12_PT_0_weights+y12_PT_1_weights+y12_PT_2_weights+y12_PT_3_weights+y12_PT_4_weights+y12_PT_5_weights+y12_PT_6_weights+y12_PT_7_weights+y12_PT_8_weights+y12_PT_9_weights+y12_PT_10_weights+y12_PT_11_weights+y12_PT_12_weights+y12_PT_13_weights,\
             label="$bg\_dip\_600\_800$", histtype="step", rwidth=1.0,\
             color=None, edgecolor="#ccc6aa", linewidth=1, linestyle="solid",\
             bottom=None, cumulative=False, normed=False, align="mid", orientation="vertical")

    pad.hist(x=xData, bins=xBinning, weights=y12_PT_0_weights+y12_PT_1_weights+y12_PT_2_weights+y12_PT_3_weights+y12_PT_4_weights+y12_PT_5_weights+y12_PT_6_weights+y12_PT_7_weights+y12_PT_8_weights+y12_PT_9_weights+y12_PT_10_weights+y12_PT_11_weights+y12_PT_12_weights,\
             label="$bg\_dip\_400\_600$", histtype="step", rwidth=1.0,\
             color=None, edgecolor="#c1bfa8", linewidth=1, linestyle="solid",\
             bottom=None, cumulative=False, normed=False, align="mid", orientation="vertical")

    pad.hist(x=xData, bins=xBinning, weights=y12_PT_0_weights+y12_PT_1_weights+y12_PT_2_weights+y12_PT_3_weights+y12_PT_4_weights+y12_PT_5_weights+y12_PT_6_weights+y12_PT_7_weights+y12_PT_8_weights+y12_PT_9_weights+y12_PT_10_weights+y12_PT_11_weights,\
             label="$bg\_dip\_200\_400$", histtype="step", rwidth=1.0,\
             color=None, edgecolor="#bab5a3", linewidth=1, linestyle="solid",\
             bottom=None, cumulative=False, normed=False, align="mid", orientation="vertical")

    pad.hist(x=xData, bins=xBinning, weights=y12_PT_0_weights+y12_PT_1_weights+y12_PT_2_weights+y12_PT_3_weights+y12_PT_4_weights+y12_PT_5_weights+y12_PT_6_weights+y12_PT_7_weights+y12_PT_8_weights+y12_PT_9_weights+y12_PT_10_weights,\
             label="$bg\_dip\_100\_200$", histtype="step", rwidth=1.0,\
             color=None, edgecolor="#b2a596", linewidth=1, linestyle="solid",\
             bottom=None, cumulative=False, normed=False, align="mid", orientation="vertical")

    pad.hist(x=xData, bins=xBinning, weights=y12_PT_0_weights+y12_PT_1_weights+y12_PT_2_weights+y12_PT_3_weights+y12_PT_4_weights+y12_PT_5_weights+y12_PT_6_weights+y12_PT_7_weights+y12_PT_8_weights+y12_PT_9_weights,\
             label="$bg\_dip\_0\_100$", histtype="step", rwidth=1.0,\
             color=None, edgecolor="#b7a39b", linewidth=1, linestyle="solid",\
             bottom=None, cumulative=False, normed=False, align="mid", orientation="vertical")

    pad.hist(x=xData, bins=xBinning, weights=y12_PT_0_weights+y12_PT_1_weights+y12_PT_2_weights+y12_PT_3_weights+y12_PT_4_weights+y12_PT_5_weights+y12_PT_6_weights+y12_PT_7_weights+y12_PT_8_weights,\
             label="$bg\_vbf\_1600\_inf$", histtype="step", rwidth=1.0,\
             color=None, edgecolor="#ad998c", linewidth=1, linestyle="solid",\
             bottom=None, cumulative=False, normed=False, align="mid", orientation="vertical")

    pad.hist(x=xData, bins=xBinning, weights=y12_PT_0_weights+y12_PT_1_weights+y12_PT_2_weights+y12_PT_3_weights+y12_PT_4_weights+y12_PT_5_weights+y12_PT_6_weights+y12_PT_7_weights,\
             label="$bg\_vbf\_1200\_1600$", histtype="step", rwidth=1.0,\
             color=None, edgecolor="#9b8e82", linewidth=1, linestyle="solid",\
             bottom=None, cumulative=False, normed=False, align="mid", orientation="vertical")

    pad.hist(x=xData, bins=xBinning, weights=y12_PT_0_weights+y12_PT_1_weights+y12_PT_2_weights+y12_PT_3_weights+y12_PT_4_weights+y12_PT_5_weights+y12_PT_6_weights,\
             label="$bg\_vbf\_800\_1200$", histtype="step", rwidth=1.0,\
             color=None, edgecolor="#876656", linewidth=1, linestyle="solid",\
             bottom=None, cumulative=False, normed=False, align="mid", orientation="vertical")

    pad.hist(x=xData, bins=xBinning, weights=y12_PT_0_weights+y12_PT_1_weights+y12_PT_2_weights+y12_PT_3_weights+y12_PT_4_weights+y12_PT_5_weights,\
             label="$bg\_vbf\_600\_800$", histtype="step", rwidth=1.0,\
             color=None, edgecolor="#afcec6", linewidth=1, linestyle="solid",\
             bottom=None, cumulative=False, normed=False, align="mid", orientation="vertical")

    pad.hist(x=xData, bins=xBinning, weights=y12_PT_0_weights+y12_PT_1_weights+y12_PT_2_weights+y12_PT_3_weights+y12_PT_4_weights,\
             label="$bg\_vbf\_400\_600$", histtype="step", rwidth=1.0,\
             color=None, edgecolor="#84c1a3", linewidth=1, linestyle="solid",\
             bottom=None, cumulative=False, normed=False, align="mid", orientation="vertical")

    pad.hist(x=xData, bins=xBinning, weights=y12_PT_0_weights+y12_PT_1_weights+y12_PT_2_weights+y12_PT_3_weights,\
             label="$bg\_vbf\_200\_400$", histtype="step", rwidth=1.0,\
             color=None, edgecolor="#89a8a0", linewidth=1, linestyle="solid",\
             bottom=None, cumulative=False, normed=False, align="mid", orientation="vertical")

    pad.hist(x=xData, bins=xBinning, weights=y12_PT_0_weights+y12_PT_1_weights+y12_PT_2_weights,\
             label="$bg\_vbf\_100\_200$", histtype="step", rwidth=1.0,\
             color=None, edgecolor="#829e8c", linewidth=1, linestyle="solid",\
             bottom=None, cumulative=False, normed=False, align="mid", orientation="vertical")

    pad.hist(x=xData, bins=xBinning, weights=y12_PT_0_weights+y12_PT_1_weights,\
             label="$bg\_vbf\_0\_100$", histtype="step", rwidth=1.0,\
             color=None, edgecolor="#adbcc6", linewidth=1, linestyle="solid",\
             bottom=None, cumulative=False, normed=False, align="mid", orientation="vertical")

    pad.hist(x=xData, bins=xBinning, weights=y12_PT_0_weights,\
             label="$signal$", histtype="step", rwidth=1.0,\
             color=None, edgecolor="#7a8e99", linewidth=1, linestyle="solid",\
             bottom=None, cumulative=False, normed=False, align="mid", orientation="vertical")


    # Axis
    plt.rc('text',usetex=False)
    plt.xlabel(r"p_{T} [ a_{1} ] ",\
               fontsize=16,color="black")
    plt.ylabel(r"$\mathrm{Events}$ $(\mathcal{L}_{\mathrm{int}} = 40.0\ \mathrm{fb}^{-1})$ ",\
               fontsize=16,color="black")

    # Boundary of y-axis
    ymax=(y12_PT_0_weights+y12_PT_1_weights+y12_PT_2_weights+y12_PT_3_weights+y12_PT_4_weights+y12_PT_5_weights+y12_PT_6_weights+y12_PT_7_weights+y12_PT_8_weights+y12_PT_9_weights+y12_PT_10_weights+y12_PT_11_weights+y12_PT_12_weights+y12_PT_13_weights+y12_PT_14_weights+y12_PT_15_weights+y12_PT_16_weights).max()*1.1
    ymin=0 # linear scale
    #ymin=min([x for x in (y12_PT_0_weights+y12_PT_1_weights+y12_PT_2_weights+y12_PT_3_weights+y12_PT_4_weights+y12_PT_5_weights+y12_PT_6_weights+y12_PT_7_weights+y12_PT_8_weights+y12_PT_9_weights+y12_PT_10_weights+y12_PT_11_weights+y12_PT_12_weights+y12_PT_13_weights+y12_PT_14_weights+y12_PT_15_weights+y12_PT_16_weights) if x])/100. # log scale
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
