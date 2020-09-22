def selection_15():

    # Library import
    import numpy
    import matplotlib
    import matplotlib.pyplot   as plt
    import matplotlib.gridspec as gridspec

    # Library version
    matplotlib_version = matplotlib.__version__
    numpy_version      = numpy.__version__

    # Histo binning
    xBinning = numpy.linspace(0.0,6.28,101,endpoint=True)

    # Creating data sequence: middle of each bin
    xData = numpy.array([0.0314,0.0942,0.157,0.2198,0.2826,0.3454,0.4082,0.471,0.5338,0.5966,0.6594,0.7222,0.785,0.8478,0.9106,0.9734,1.0362,1.099,1.1618,1.2246,1.2874,1.3502,1.413,1.4758,1.5386,1.6014,1.6642,1.727,1.7898,1.8526,1.9154,1.9782,2.041,2.1038,2.1666,2.2294,2.2922,2.355,2.4178,2.4806,2.5434,2.6062,2.669,2.7318,2.7946,2.8574,2.9202,2.983,3.0458,3.1086,3.1714,3.2342,3.297,3.3598,3.4226,3.4854,3.5482,3.611,3.6738,3.7366,3.7994,3.8622,3.925,3.9878,4.0506,4.1134,4.1762,4.239,4.3018,4.3646,4.4274,4.4902,4.553,4.6158,4.6786,4.7414,4.8042,4.867,4.9298,4.9926,5.0554,5.1182,5.181,5.2438,5.3066,5.3694,5.4322,5.495,5.5578,5.6206,5.6834,5.7462,5.809,5.8718,5.9346,5.9974,6.0602,6.123,6.1858,6.2486])

    # Creating weights for histo: y16_DELTAR_0
    y16_DELTAR_0_weights = numpy.array([0.0,0.0,0.0,0.0,0.0,0.0,0.0040940844023,0.0,0.0204704180115,0.0491289968276,0.0655053424368,0.135104761276,0.15966925969,0.237456871333,0.327526712184,0.552701514311,0.67552380638,0.880228026495,1.13815539984,1.33876562355,1.73589167458,1.85052597384,2.38685110254,2.57517893705,3.04190412691,3.64782879445,4.03676845267,4.31926020443,4.83511175112,5.6948709956,6.39086638399,6.98041386592,8.10219288015,8.84322022897,9.52283963175,10.7756305309,11.9342535127,13.1624804334,14.6076911634,16.6096974041,18.3865318427,20.953521587,23.6228632413,26.5419446761,30.7424769849,34.2388219125,40.3308045591,47.0533186516,56.846350046,66.0703419403,49.1822367808,33.9890861319,26.9922962804,21.5144090941,17.9607442169,14.583127185,12.5934009335,10.8984504229,9.26900785481,7.8278891212,7.03363781915,6.17387857467,5.09303952446,4.51168003534,3.93032054621,3.27936111824,2.71437761473,2.51376739101,2.16167610042,1.82186719902,1.49024669044,1.34695361636,1.15862578185,1.03170909338,0.724652963207,0.822910876863,0.712370574001,0.67552380638,0.466725589862,0.429878822242,0.364373479805,0.323432635782,0.241550947736,0.233362794931,0.241550947736,0.171951528897,0.184233758104,0.114634339264,0.0900698408506,0.094163917253,0.102352110058,0.0777876116437,0.0777876116437,0.0614112660345,0.0245645024138,0.040940844023,0.0204704180115,0.0245645024138,0.0204704180115,0.0245645024138])

    # Creating weights for histo: y16_DELTAR_1
    y16_DELTAR_1_weights = numpy.array([0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.012170493784,0.0,0.0,0.0,0.0,0.0121753353338,0.0121240822392,0.0,0.0,0.0,0.0,0.0121313846429,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0])

    # Creating weights for histo: y16_DELTAR_2
    y16_DELTAR_2_weights = numpy.array([0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0100367002096,0.0,0.0,0.0,0.0301281658925,0.0401223350501,0.0602051771728,0.0601582372378,0.0904552794635,0.15059413745,0.130545454873,0.0802712969437,0.0903795392338,0.0301340375165,0.0703456493479,0.0200337783209,0.03011702179,0.0702237129498,0.0201312737229,0.0502198216492,0.0301083403813,0.020089779812,0.0100584801742,0.0,0.0200925689367,0.0,0.0200840156211,0.0200887054825,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0100262833455,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0])

    # Creating weights for histo: y16_DELTAR_3
    y16_DELTAR_3_weights = numpy.array([0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.016515267118,0.0220069009008,0.0495286288392,0.022002062371,0.0329763191398,0.0660276497099,0.0549803234228,0.126420220089,0.165065366391,0.13745779619,0.198055364229,0.241926163303,0.231024317916,0.219927793815,0.280445938464,0.341151327309,0.473038395395,0.319115785237,0.275073829773,0.280639967164,0.26959463154,0.198032532543,0.198127474979,0.214507787336,0.175987727795,0.164950111068,0.132121072549,0.10996665946,0.0770186280475,0.099013138087,0.0990174850449,0.0714561063505,0.0934856764335,0.0769928306806,0.0659375823674,0.0550237930018,0.0549600105355,0.0384994907114,0.0604921847788,0.022002216749,0.0439525381334,0.0384809694207,0.0494565587149,0.0220230415211,0.0165031281366,0.00547487971328,0.0,0.00549392507646,0.0,0.0,0.0109910311511,0.0,0.0109708604539,0.00547487971328,0.0,0.00550972850282,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0])

    # Creating weights for histo: y16_DELTAR_4
    y16_DELTAR_4_weights = numpy.array([0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.00197547377757,0.00098613778175,0.0108551089026,0.00592052794488,0.00987107787771,0.0286162117425,0.0335586208893,0.0404403927341,0.0365189149239,0.0651251620591,0.074996977462,0.0759750000612,0.0898085284828,0.127282065613,0.106587107415,0.122387102587,0.129256589025,0.139155700878,0.138150742575,0.139173136937,0.16579968195,0.174696040059,0.180568664938,0.176657255951,0.175664923758,0.199363373325,0.145071895862,0.157882228264,0.130265234955,0.131239008767,0.0986763074887,0.104593785125,0.114457022789,0.113501967688,0.0838746970256,0.0967308842572,0.0976869414308,0.0720312842617,0.0878155268567,0.0759831769714,0.0671101471064,0.0523019229658,0.0572451057125,0.0394784714333,0.0335684331816,0.0335553220672,0.0355120326415,0.0276385378645,0.0227029147516,0.0157889322936,0.0177681253628,0.0207311410259,0.0108588285951,0.0118294839584,0.00789309130355,0.00888986067195,0.00691297637737,0.00296119469722,0.0,0.00295842577095,0.000984736884626,0.0,0.000985635543096,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0])

    # Creating weights for histo: y16_DELTAR_5
    y16_DELTAR_5_weights = numpy.array([0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.00100895389316,0.000503663318289,0.00327564988468,0.00201654820484,0.00629897937308,0.00831978237173,0.0121005671876,0.013362333215,0.0178976217302,0.0189036039896,0.0184031675767,0.0242021786682,0.0267203812277,0.0305080359711,0.0337823066688,0.0363002651598,0.0385712223469,0.0431014134318,0.0425997126642,0.046130063213,0.0486419680054,0.0529411342692,0.0524370728392,0.0589914718782,0.0557094310003,0.0579764670873,0.0544504377509,0.0609955941966,0.0592313391804,0.0695645984952,0.0567159134,0.0506680964983,0.0524304709869,0.0484001801644,0.0433619665381,0.0373021262628,0.0350388392278,0.0350369506979,0.0292437092252,0.0289900580556,0.0262079814581,0.0239488715951,0.0214224307241,0.0239484154671,0.0199143355815,0.0143703440436,0.0128540786085,0.0128531623514,0.0153800193391,0.0078141404983,0.00932810528785,0.00831969434703,0.00630625341404,0.00504227876694,0.00479004399469,0.00327893440625,0.00226967562755,0.00201639416162,0.00226669399096,0.00201684108702,0.00126127068842,0.000251958174643,0.000251938729186,0.000504775630383,0.000252082369489,0.0,0.000252082369489,0.000504066631451,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0])

    # Creating weights for histo: y16_DELTAR_6
    y16_DELTAR_6_weights = numpy.array([0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.000860356234349,0.00113989714218,0.002868712866,0.00343424121619,0.00314988950048,0.00315307757793,0.00458060448723,0.00572795347303,0.00744232137768,0.00773851166759,0.00858811181449,0.00859023320061,0.00945720831962,0.00886380403603,0.0160270721648,0.0105975433351,0.0131797361129,0.0177365074968,0.0146001650761,0.01317853646,0.0174633465428,0.0200413405355,0.0174799317434,0.0208967130121,0.0174813813239,0.0203316565253,0.019170842436,0.0194710655589,0.0183224579373,0.0208920243689,0.0231903792822,0.0254821161107,0.0249103915535,0.0217499561048,0.0203270078705,0.0160308110828,0.0171788788606,0.0103172244524,0.0117485402653,0.00973025030807,0.00857420183969,0.0102948609238,0.0103070873858,0.00801811675685,0.008024143013,0.0065942437902,0.00629764461861,0.00457444127071,0.00487302986661,0.00457707050987,0.00343223379708,0.00229065514149,0.00143045606167,0.00200561062627,0.00114371003882,0.00114534356612,0.0017131112683,0.00114313320574,0.00114237742445,0.000859759207114,0.0,0.0,0.000283957629739,0.0,0.000287128712107,0.000858030207443,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0])

    # Creating weights for histo: y16_DELTAR_7
    y16_DELTAR_7_weights = numpy.array([0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,4.31740420382e-05,0.000194363236407,0.000107916329618,0.00015120486854,0.000324227428246,0.000345608296202,0.000410561640262,0.000194461681933,0.000367106510891,0.000387281515447,0.000539934526479,0.000431913925908,0.00120947977586,0.000907123766817,0.000950557145133,0.00116626348899,0.00110154886172,0.000971834622236,0.00105852368239,0.000864074279953,0.0015116962261,0.00149067565452,0.00142279811372,0.00136041365726,0.00133744890179,0.00129595845008,0.00146855453824,0.00176943491212,0.00200875351396,0.00144715426616,0.00192210007692,0.00166371598388,0.0017935098515,0.00187900909961,0.00155400056122,0.00194127118018,0.00200860054411,0.00179254760829,0.00153337016752,0.00140252814213,0.00114349067925,0.0015337335233,0.00110163477629,0.000712818114127,0.000820521459427,0.000626489895176,0.000689761576746,0.000604666336673,0.000432083659574,0.000367494551388,0.000453684678382,0.000216031100943,0.000388550787992,0.000151218908238,0.000172752243127,0.000129585954355,0.000129622415661,0.000129437594558,0.000151094772159,0.000108024875346,4.31976790228e-05,4.32193043492e-05,0.000172817412473,6.47146272791e-05,6.48567425536e-05,4.3231541937e-05,0.0,0.0,2.16086170088e-05,2.1577402778e-05,2.15827546272e-05,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0])

    # Creating weights for histo: y16_DELTAR_8
    y16_DELTAR_8_weights = numpy.array([0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,2.8429264144e-05,0.0,2.70012831845e-05,5.67021141107e-05,0.00014169446579,2.8429264144e-05,0.0,2.83973992471e-05,0.0,5.67658884502e-05,2.83973992471e-05,5.67369635577e-05,5.68978174387e-05,8.49743701372e-05,8.5036897202e-05,0.000113644061313,5.68266782396e-05,0.000113683677131,0.000142022038713,0.000227358118491,0.000141727162204,0.00019891817827,0.000141962065591,0.000141851295726,0.000113009629137,0.000113494922905,0.000198809041741,0.000224879902601,0.000170340889356,0.000168088519264,0.000226931372387,0.000197976782899,0.000227109702962,0.000226864554104,0.000283661728359,0.000226508041441,0.000255597158406,0.000170255807408,0.000283920389359,0.000170371625766,5.66287921811e-05,5.67183435294e-05,2.83684892031e-05,0.0,5.66506046385e-05,0.000142105190354,8.53270815827e-05,2.84080901724e-05,8.52083974628e-05,2.84489087193e-05,0.0,0.0,0.0,0.0,0.0,2.84489087193e-05,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0])

    # Creating weights for histo: y16_DELTAR_9
    y16_DELTAR_9_weights = numpy.array([0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0])

    # Creating weights for histo: y16_DELTAR_10
    y16_DELTAR_10_weights = numpy.array([0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,1.0529581672,0.0,0.0,1.0521138287,0.0,0.0,0.0,1.05462838872,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0])

    # Creating weights for histo: y16_DELTAR_11
    y16_DELTAR_11_weights = numpy.array([0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.230587748609,0.230673171817,0.229982523453,0.461303766524,0.0,0.92149968281,0.460417640042,1.84216012007,0.92124375903,0.922132575402,0.460254709587,1.61217340808,1.61219031595,0.69058034767,0.690232583374,0.230465320206,0.461409440757,0.460783465025,0.920509419174,0.460614386251,0.0,0.460485655821,0.230569111517,0.461361022745,0.230551281392,0.690851642248,0.23075225457,0.230645235392,0.0,0.0,0.0,0.0,0.691171354838,0.0,0.230645235392,0.0,0.230428276584,0.0,0.230020181907,0.23012854603,0.0,0.230587748609,0.230020181907,0.0,0.460704689687,0.0,0.0,0.0,0.229703312915,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0])

    # Creating weights for histo: y16_DELTAR_12
    y16_DELTAR_12_weights = numpy.array([0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0276586855048,0.0,0.0554137399213,0.083144921375,0.0277307083028,0.0554134706485,0.0553649630651,0.0832016610145,0.138521155433,0.221295211137,0.138542427989,0.138483303362,0.30465231953,0.138496882407,0.193843534918,0.19385088222,0.304460481847,0.387725229647,0.387423259362,0.609119840939,0.498475620515,0.719689049636,0.554181252223,0.526223804627,0.553937367942,0.415183753091,0.3324435873,0.442640737832,0.360268206438,0.22142811653,0.249136794466,0.0276381515254,0.249178147084,0.277015575917,0.193850305207,0.193673854545,0.165981217579,0.138383210791,0.194018600748,0.0276586855048,0.249315130038,0.110749044504,0.276857935888,0.083210123876,0.110742428085,0.276959721031,0.110817862955,0.166015376765,0.166304998966,0.083146806285,0.0831491143382,0.0553478834719,0.138523655824,0.027724465019,0.0277219338541,0.0554090084124,0.138455337451,0.0553252260837,0.0552443288214,0.0553701946522,0.0276953720093,0.0,0.0276953720093,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0])

    # Creating weights for histo: y16_DELTAR_13
    y16_DELTAR_13_weights = numpy.array([0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.010103348764,0.0,0.0,0.0100671480081,0.020171285724,0.0403406476191,0.0403093869161,0.040336375141,0.0302593834403,0.0302543280791,0.0504277257668,0.0403500300782,0.0805403398726,0.0806532206873,0.0504254135307,0.040365542087,0.131000734318,0.080619963329,0.131133278242,0.0503906146818,0.0907485282104,0.0605384117837,0.100782358172,0.151215503431,0.0705459575079,0.0806766464907,0.181389455515,0.0806733086172,0.121055691793,0.0907479213243,0.0806901800508,0.100846081212,0.131157675064,0.100852817648,0.0403556437747,0.0504010713293,0.0705054782051,0.0907945301768,0.0605096393137,0.0806726410425,0.0604162152674,0.0302994379229,0.0403528642363,0.0302838348813,0.0403240068023,0.0604610520125,0.0604724432646,0.0302850547224,0.020171285724,0.0504560005902,0.0302076888823,0.0605081949248,0.0201717105443,0.0200470561393,0.0504013140837,0.0100712384204,0.0201586806997,0.0504419754524,0.0403392275057,0.0402537415296,0.0100126435675,0.0,0.0,0.0100712384204,0.0,0.0100533231428,0.0,0.0100975165886,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0])

    # Creating weights for histo: y16_DELTAR_14
    y16_DELTAR_14_weights = numpy.array([0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.00565207393312,0.00282800531951,0.0,0.00565745650891,0.00282930960342,0.0113041016969,0.0084786918639,0.00848989177679,0.00847484826618,0.0141461594251,0.0113199570184,0.0282785757761,0.0282922803758,0.0113337501094,0.0254484181958,0.0283005600778,0.0141323317072,0.0226357549486,0.0169844774367,0.0282932884065,0.0226524220811,0.0395968283764,0.0452695784798,0.0113192644783,0.0311277128035,0.0424384359535,0.0622494697619,0.0565854533589,0.0452837755525,0.0565967263733,0.0452371829915,0.0453040131141,0.0565841452276,0.0565798745634,0.0481057996337,0.0395814385957,0.0254501341564,0.0396248377772,0.0452702325455,0.0395965590552,0.0254703909552,0.00848003077482,0.0141555241067,0.0198122649908,0.019791835057,0.022620295914,0.0113115503507,0.00282586036883,0.0141468404229,0.0254556783248,0.0197924044788,0.0198021923793,0.0141426120807,0.0113334807882,0.0169683027772,0.00848133505873,0.00848406289736,0.00565715256074,0.00849247341249,0.00849797141164,0.00283301931005,0.0,0.0141554625476,0.00565105436015,0.00565845684466,0.00849440867741,0.00848850669653,0.00283201512686,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0])

    # Creating weights for histo: y16_DELTAR_15
    y16_DELTAR_15_weights = numpy.array([0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.00302944691256,0.0,0.0,0.0,0.00152305580806,0.0,0.00152260668839,0.0015454101487,0.00152260668839,0.00152162926216,0.0,0.00304612698073,0.0,0.00456482632799,0.0,0.00153333592093,0.00459311613965,0.00150849605748,0.00152808831215,0.00303898361419,0.00152325200244,0.00305724623826,0.00305314743032,0.00305086755704,0.00304479144066,0.00303609270178,0.00303565303726,0.0,0.00303428322227,0.00608547461823,0.00605987125134,0.00303278576274,0.0030389032454,0.0030483111206,0.00456574229574,0.00152192828131,0.00304590951226,0.00151881871853,0.00308362492753,0.00152094967318,0.00151265396011,0.00153565716049,0.0,0.00153153116899,0.00152162926216,0.00153565716049,0.0,0.0,0.00152192828131,0.0,0.0,0.0,0.0,0.0,0.00305829576001,0.0,0.00153333592093,0.0,0.0,0.0,0.0,0.00151727398325,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0])

    # Creating weights for histo: y16_DELTAR_16
    y16_DELTAR_16_weights = numpy.array([0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.000180766958654,0.0,0.0,0.000180970230372,0.000361088066976,0.0,0.0,0.00017999868396,0.0,0.00018065712263,0.0,0.0,0.000180766958654,0.0,0.000180755024141,0.00036167181869,0.00054162826987,0.000180202995135,0.00036127031855,0.000180402032024,0.000541942802054,0.00018065712263,0.000181168420296,0.000360616345698,0.000180003611759,0.00018065712263,0.000180533812155,0.000722262524432,0.000180003611759,0.000540904884347,0.000903152408578,0.000361266853691,0.000722659828243,0.000541896603936,0.0,0.000180343706901,0.000180766958654,0.000180640760797,0.0,0.0,0.000180640760797,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.000180003611759,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0])

    # Creating a new Canvas
    fig   = plt.figure(figsize=(12,6),dpi=80)
    frame = gridspec.GridSpec(1,1,right=0.7)
    pad   = fig.add_subplot(frame[0])

    # Creating a new Stack
    pad.hist(x=xData, bins=xBinning, weights=y16_DELTAR_0_weights+y16_DELTAR_1_weights+y16_DELTAR_2_weights+y16_DELTAR_3_weights+y16_DELTAR_4_weights+y16_DELTAR_5_weights+y16_DELTAR_6_weights+y16_DELTAR_7_weights+y16_DELTAR_8_weights+y16_DELTAR_9_weights+y16_DELTAR_10_weights+y16_DELTAR_11_weights+y16_DELTAR_12_weights+y16_DELTAR_13_weights+y16_DELTAR_14_weights+y16_DELTAR_15_weights+y16_DELTAR_16_weights,\
             label="$bg\_dip\_1600\_inf$", histtype="step", rwidth=1.0,\
             color=None, edgecolor="#e5e5e5", linewidth=1, linestyle="solid",\
             bottom=None, cumulative=False, normed=False, align="mid", orientation="vertical")

    pad.hist(x=xData, bins=xBinning, weights=y16_DELTAR_0_weights+y16_DELTAR_1_weights+y16_DELTAR_2_weights+y16_DELTAR_3_weights+y16_DELTAR_4_weights+y16_DELTAR_5_weights+y16_DELTAR_6_weights+y16_DELTAR_7_weights+y16_DELTAR_8_weights+y16_DELTAR_9_weights+y16_DELTAR_10_weights+y16_DELTAR_11_weights+y16_DELTAR_12_weights+y16_DELTAR_13_weights+y16_DELTAR_14_weights+y16_DELTAR_15_weights,\
             label="$bg\_dip\_1200\_1600$", histtype="step", rwidth=1.0,\
             color=None, edgecolor="#f2f2f2", linewidth=1, linestyle="solid",\
             bottom=None, cumulative=False, normed=False, align="mid", orientation="vertical")

    pad.hist(x=xData, bins=xBinning, weights=y16_DELTAR_0_weights+y16_DELTAR_1_weights+y16_DELTAR_2_weights+y16_DELTAR_3_weights+y16_DELTAR_4_weights+y16_DELTAR_5_weights+y16_DELTAR_6_weights+y16_DELTAR_7_weights+y16_DELTAR_8_weights+y16_DELTAR_9_weights+y16_DELTAR_10_weights+y16_DELTAR_11_weights+y16_DELTAR_12_weights+y16_DELTAR_13_weights+y16_DELTAR_14_weights,\
             label="$bg\_dip\_800\_1200$", histtype="step", rwidth=1.0,\
             color=None, edgecolor="#ccc6aa", linewidth=1, linestyle="solid",\
             bottom=None, cumulative=False, normed=False, align="mid", orientation="vertical")

    pad.hist(x=xData, bins=xBinning, weights=y16_DELTAR_0_weights+y16_DELTAR_1_weights+y16_DELTAR_2_weights+y16_DELTAR_3_weights+y16_DELTAR_4_weights+y16_DELTAR_5_weights+y16_DELTAR_6_weights+y16_DELTAR_7_weights+y16_DELTAR_8_weights+y16_DELTAR_9_weights+y16_DELTAR_10_weights+y16_DELTAR_11_weights+y16_DELTAR_12_weights+y16_DELTAR_13_weights,\
             label="$bg\_dip\_600\_800$", histtype="step", rwidth=1.0,\
             color=None, edgecolor="#ccc6aa", linewidth=1, linestyle="solid",\
             bottom=None, cumulative=False, normed=False, align="mid", orientation="vertical")

    pad.hist(x=xData, bins=xBinning, weights=y16_DELTAR_0_weights+y16_DELTAR_1_weights+y16_DELTAR_2_weights+y16_DELTAR_3_weights+y16_DELTAR_4_weights+y16_DELTAR_5_weights+y16_DELTAR_6_weights+y16_DELTAR_7_weights+y16_DELTAR_8_weights+y16_DELTAR_9_weights+y16_DELTAR_10_weights+y16_DELTAR_11_weights+y16_DELTAR_12_weights,\
             label="$bg\_dip\_400\_600$", histtype="step", rwidth=1.0,\
             color=None, edgecolor="#c1bfa8", linewidth=1, linestyle="solid",\
             bottom=None, cumulative=False, normed=False, align="mid", orientation="vertical")

    pad.hist(x=xData, bins=xBinning, weights=y16_DELTAR_0_weights+y16_DELTAR_1_weights+y16_DELTAR_2_weights+y16_DELTAR_3_weights+y16_DELTAR_4_weights+y16_DELTAR_5_weights+y16_DELTAR_6_weights+y16_DELTAR_7_weights+y16_DELTAR_8_weights+y16_DELTAR_9_weights+y16_DELTAR_10_weights+y16_DELTAR_11_weights,\
             label="$bg\_dip\_200\_400$", histtype="step", rwidth=1.0,\
             color=None, edgecolor="#bab5a3", linewidth=1, linestyle="solid",\
             bottom=None, cumulative=False, normed=False, align="mid", orientation="vertical")

    pad.hist(x=xData, bins=xBinning, weights=y16_DELTAR_0_weights+y16_DELTAR_1_weights+y16_DELTAR_2_weights+y16_DELTAR_3_weights+y16_DELTAR_4_weights+y16_DELTAR_5_weights+y16_DELTAR_6_weights+y16_DELTAR_7_weights+y16_DELTAR_8_weights+y16_DELTAR_9_weights+y16_DELTAR_10_weights,\
             label="$bg\_dip\_100\_200$", histtype="step", rwidth=1.0,\
             color=None, edgecolor="#b2a596", linewidth=1, linestyle="solid",\
             bottom=None, cumulative=False, normed=False, align="mid", orientation="vertical")

    pad.hist(x=xData, bins=xBinning, weights=y16_DELTAR_0_weights+y16_DELTAR_1_weights+y16_DELTAR_2_weights+y16_DELTAR_3_weights+y16_DELTAR_4_weights+y16_DELTAR_5_weights+y16_DELTAR_6_weights+y16_DELTAR_7_weights+y16_DELTAR_8_weights+y16_DELTAR_9_weights,\
             label="$bg\_dip\_0\_100$", histtype="step", rwidth=1.0,\
             color=None, edgecolor="#b7a39b", linewidth=1, linestyle="solid",\
             bottom=None, cumulative=False, normed=False, align="mid", orientation="vertical")

    pad.hist(x=xData, bins=xBinning, weights=y16_DELTAR_0_weights+y16_DELTAR_1_weights+y16_DELTAR_2_weights+y16_DELTAR_3_weights+y16_DELTAR_4_weights+y16_DELTAR_5_weights+y16_DELTAR_6_weights+y16_DELTAR_7_weights+y16_DELTAR_8_weights,\
             label="$bg\_vbf\_1600\_inf$", histtype="step", rwidth=1.0,\
             color=None, edgecolor="#ad998c", linewidth=1, linestyle="solid",\
             bottom=None, cumulative=False, normed=False, align="mid", orientation="vertical")

    pad.hist(x=xData, bins=xBinning, weights=y16_DELTAR_0_weights+y16_DELTAR_1_weights+y16_DELTAR_2_weights+y16_DELTAR_3_weights+y16_DELTAR_4_weights+y16_DELTAR_5_weights+y16_DELTAR_6_weights+y16_DELTAR_7_weights,\
             label="$bg\_vbf\_1200\_1600$", histtype="step", rwidth=1.0,\
             color=None, edgecolor="#9b8e82", linewidth=1, linestyle="solid",\
             bottom=None, cumulative=False, normed=False, align="mid", orientation="vertical")

    pad.hist(x=xData, bins=xBinning, weights=y16_DELTAR_0_weights+y16_DELTAR_1_weights+y16_DELTAR_2_weights+y16_DELTAR_3_weights+y16_DELTAR_4_weights+y16_DELTAR_5_weights+y16_DELTAR_6_weights,\
             label="$bg\_vbf\_800\_1200$", histtype="step", rwidth=1.0,\
             color=None, edgecolor="#876656", linewidth=1, linestyle="solid",\
             bottom=None, cumulative=False, normed=False, align="mid", orientation="vertical")

    pad.hist(x=xData, bins=xBinning, weights=y16_DELTAR_0_weights+y16_DELTAR_1_weights+y16_DELTAR_2_weights+y16_DELTAR_3_weights+y16_DELTAR_4_weights+y16_DELTAR_5_weights,\
             label="$bg\_vbf\_600\_800$", histtype="step", rwidth=1.0,\
             color=None, edgecolor="#afcec6", linewidth=1, linestyle="solid",\
             bottom=None, cumulative=False, normed=False, align="mid", orientation="vertical")

    pad.hist(x=xData, bins=xBinning, weights=y16_DELTAR_0_weights+y16_DELTAR_1_weights+y16_DELTAR_2_weights+y16_DELTAR_3_weights+y16_DELTAR_4_weights,\
             label="$bg\_vbf\_400\_600$", histtype="step", rwidth=1.0,\
             color=None, edgecolor="#84c1a3", linewidth=1, linestyle="solid",\
             bottom=None, cumulative=False, normed=False, align="mid", orientation="vertical")

    pad.hist(x=xData, bins=xBinning, weights=y16_DELTAR_0_weights+y16_DELTAR_1_weights+y16_DELTAR_2_weights+y16_DELTAR_3_weights,\
             label="$bg\_vbf\_200\_400$", histtype="step", rwidth=1.0,\
             color=None, edgecolor="#89a8a0", linewidth=1, linestyle="solid",\
             bottom=None, cumulative=False, normed=False, align="mid", orientation="vertical")

    pad.hist(x=xData, bins=xBinning, weights=y16_DELTAR_0_weights+y16_DELTAR_1_weights+y16_DELTAR_2_weights,\
             label="$bg\_vbf\_100\_200$", histtype="step", rwidth=1.0,\
             color=None, edgecolor="#829e8c", linewidth=1, linestyle="solid",\
             bottom=None, cumulative=False, normed=False, align="mid", orientation="vertical")

    pad.hist(x=xData, bins=xBinning, weights=y16_DELTAR_0_weights+y16_DELTAR_1_weights,\
             label="$bg\_vbf\_0\_100$", histtype="step", rwidth=1.0,\
             color=None, edgecolor="#adbcc6", linewidth=1, linestyle="solid",\
             bottom=None, cumulative=False, normed=False, align="mid", orientation="vertical")

    pad.hist(x=xData, bins=xBinning, weights=y16_DELTAR_0_weights,\
             label="$signal$", histtype="step", rwidth=1.0,\
             color=None, edgecolor="#7a8e99", linewidth=1, linestyle="solid",\
             bottom=None, cumulative=False, normed=False, align="mid", orientation="vertical")


    # Axis
    plt.rc('text',usetex=False)
    plt.xlabel(r"$\Delta R$ $[ a_{1}, a_{2} ]$ ",\
               fontsize=16,color="black")
    plt.ylabel(r"$\mathrm{Events}$ $(\mathcal{L}_{\mathrm{int}} = 40.0\ \mathrm{fb}^{-1})$ ",\
               fontsize=16,color="black")

    # Boundary of y-axis
    ymax=(y16_DELTAR_0_weights+y16_DELTAR_1_weights+y16_DELTAR_2_weights+y16_DELTAR_3_weights+y16_DELTAR_4_weights+y16_DELTAR_5_weights+y16_DELTAR_6_weights+y16_DELTAR_7_weights+y16_DELTAR_8_weights+y16_DELTAR_9_weights+y16_DELTAR_10_weights+y16_DELTAR_11_weights+y16_DELTAR_12_weights+y16_DELTAR_13_weights+y16_DELTAR_14_weights+y16_DELTAR_15_weights+y16_DELTAR_16_weights).max()*1.1
    ymin=0 # linear scale
    #ymin=min([x for x in (y16_DELTAR_0_weights+y16_DELTAR_1_weights+y16_DELTAR_2_weights+y16_DELTAR_3_weights+y16_DELTAR_4_weights+y16_DELTAR_5_weights+y16_DELTAR_6_weights+y16_DELTAR_7_weights+y16_DELTAR_8_weights+y16_DELTAR_9_weights+y16_DELTAR_10_weights+y16_DELTAR_11_weights+y16_DELTAR_12_weights+y16_DELTAR_13_weights+y16_DELTAR_14_weights+y16_DELTAR_15_weights+y16_DELTAR_16_weights) if x])/100. # log scale
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
    plt.savefig('../../HTML/MadAnalysis5job_0/selection_15.png')
    plt.savefig('../../PDF/MadAnalysis5job_0/selection_15.png')
    plt.savefig('../../DVI/MadAnalysis5job_0/selection_15.eps')

# Running!
if __name__ == '__main__':
    selection_15()