def selection_4():

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

    # Creating weights for histo: y5_ETA_0
    y5_ETA_0_weights = numpy.array([0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,1.93650155414,2.16577055928,2.86585876426,3.2752672163,3.82387435003,4.39295226636,5.03572372006,5.70305915288,6.52597045348,7.36934973668,8.43790882849,9.65385179504,10.7346868764,11.6640460865,13.5022885242,14.5462796369,14.8819953516,16.2903621546,16.7284257823,17.4162331977,17.174681403,17.7683248984,17.7069129506,17.3384452638,17.0764254865,15.6557786939,15.2299910558,13.7847802841,12.7407891714,11.2996703962,9.60881583332,8.6794566232,7.11142195589,5.67030718072,4.68772801583,3.77883958831,2.8331059921,2.13711178364,1.64991579771,1.08902627442,0.888416044921,0.65505344326,0.405314455517,0.302962222508,0.159669264295,0.131010688652,0.0614112678056,0.0163763340815,0.0286585876426,0.00409408452037,0.00409408452037,0.0122822535611,0.065505344326,0.0736934973668,0.10644618953,0.180139686896,0.282491799906,0.454443213762,0.749217363229,0.822910900595,1.07674428486,1.54346948818,2.12892379059,2.70618969997,3.63964050661,4.68772801583,5.76856309721,7.32431777495,8.39696486329,9.67022778112,11.5371301944,12.6097772828,13.8789442041,14.9556872889,16.2330422033,16.6301698658,17.5267731037,17.891148794,17.9320887592,17.8543008254,17.6250330202,16.585133904,15.979210419,15.3159669827,14.2105639222,12.8513290775,12.1389576829,10.7060309008,9.67431977765,8.58938869975,7.6559374931,6.73476627602,5.75628310765,4.98659576181,4.66725603323,3.78702758135,3.32849037106,2.87814115382,2.10845340799,2.04294786367,0.00409408452037,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0])

    # Creating weights for histo: y5_ETA_1
    y5_ETA_1_weights = numpy.array([0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0121240822392,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0121753353338,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0121313846429,0.012170493784,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0])

    # Creating weights for histo: y5_ETA_2
    y5_ETA_2_weights = numpy.array([0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0200482816269,0.010032919325,0.0200940397991,0.0100262832744,0.010040728874,0.0100696696577,0.0100271592661,0.0301165257319,0.0401877986198,0.0,0.0502017229729,0.010040728874,0.0,0.0301145712787,0.0402058597513,0.0,0.0100568562125,0.0401512714171,0.0,0.0301337191358,0.0100702894631,0.0,0.050140155629,0.0300994521571,0.0100355638284,0.0100184158769,0.0401671012489,0.0100262832744,0.0301196784758,0.0,0.0,0.0100367001384,0.0100153623019,0.0,0.0,0.0,0.0100369728528,0.0100609841169,0.0,0.0,0.0100568562125,0.0100602899348,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0100340928234,0.0100568562125,0.0,0.0,0.0100532489446,0.0200646444914,0.0301498340782,0.0200868128673,0.0301214387233,0.0301310828965,0.010045943504,0.0200609297906,0.0200572522781,0.0,0.0301088194839,0.010045943504,0.0,0.0301025759767,0.0200638924608,0.0201178403294,0.0300965762597,0.0100299566548,0.0200777058588,0.0100187051194,0.0301077410223,0.0301692711779,0.0100355638284,0.0100324441408,0.0200798255935,0.0,0.0100369728528,0.0200832055994,0.0,0.0,0.0100696696577,0.0,0.0100187051194,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0])

    # Creating weights for histo: y5_ETA_3
    y5_ETA_3_weights = numpy.array([0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0275282721771,0.0274997813219,0.00549710596009,0.0164555265735,0.0110053636951,0.0770293110214,0.0440010037659,0.0550185105048,0.0330098306536,0.0549834910877,0.0880414145324,0.121011383177,0.0934765336867,0.0880213454001,0.0990525836506,0.148391326591,0.170522298147,0.115509109618,0.0880932530198,0.142979039121,0.143099738296,0.137527304026,0.142956573069,0.132021455399,0.131943372662,0.0934995278747,0.0934989997397,0.0935291846896,0.104510168858,0.0825596976154,0.071452814174,0.0495039679626,0.0549952725621,0.0274769699499,0.0275034010784,0.0110008136084,0.0220214688448,0.0275283574913,0.0,0.0110360564673,0.021979583672,0.0219691225352,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0110095197118,0.0,0.00550243199904,0.00551802823363,0.00547487959922,0.0220146884032,0.0275094786942,0.0385276029448,0.0384989861497,0.0220041419523,0.0495313903599,0.0165169689939,0.0550053883798,0.0825226875355,0.104575210722,0.126506425347,0.066013876197,0.104442608196,0.126527185118,0.0990133797788,0.170543342297,0.0825431629255,0.181466759744,0.1538988815,0.20895098952,0.132032830616,0.115526172443,0.0824931525979,0.126454668112,0.104502043703,0.08245756442,0.0825350783965,0.0990397052803,0.0770264265915,0.0385428294849,0.0935220345535,0.0329914596786,0.043969193785,0.0494868645118,0.0274664559996,0.0164761360286,0.0165097701068,0.0110073624832,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0])

    # Creating weights for histo: y5_ETA_4
    y5_ETA_4_weights = numpy.array([0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.00295952755959,0.00197733276196,0.00197153597409,0.00295929588047,0.00592188256639,0.00888223262692,0.00986622754723,0.0207193880908,0.0266393306452,0.0276408337728,0.028623718397,0.0355146850478,0.0365133262569,0.0562514891552,0.0592211905545,0.0720236262363,0.0769833630669,0.0878251039945,0.100658684083,0.116441122468,0.105610244004,0.12136374254,0.104612220072,0.122368861145,0.107579035503,0.124337372063,0.114461228008,0.0977014885466,0.0799371916409,0.0838926916906,0.0818885871641,0.0473736095304,0.0503348935223,0.0305824370646,0.0296045868517,0.0236809646878,0.025663292179,0.01382357141,0.0108591409111,0.00690936069003,0.0049344204759,0.00296236222172,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.00197140370055,0.00197179531041,0.000988009622793,0.00394563925743,0.00493570713674,0.00987045228407,0.00888712273977,0.020722578689,0.0157902465318,0.0246790126701,0.033550310684,0.0444057519442,0.0463809967883,0.0631546850964,0.0799404383551,0.08090190669,0.08585110172,0.103606500224,0.0976781202204,0.0977050960069,0.115473882196,0.132224963753,0.1322358663,0.117436981924,0.104620837893,0.107570056935,0.0986854033011,0.0976784008007,0.0799142241437,0.075986220958,0.0641623289231,0.0661257893969,0.0592049169003,0.0414675156152,0.0375125005685,0.0266518204744,0.0197401189434,0.0167707462239,0.0128311630906,0.0118483786737,0.00395132701983,0.00987041220117,0.00296029153951,0.00395140718562,0.000988172359335,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0])

    # Creating weights for histo: y5_ETA_5
    y5_ETA_5_weights = numpy.array([0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.000504690405707,0.000503681322579,0.00176459470884,0.000504669999982,0.000755187890129,0.00201616849525,0.00327598677425,0.00529427346382,0.0068047412699,0.00630216825829,0.00806693941664,0.010840665667,0.01310830592,0.0178963013326,0.0183999386429,0.0226806437203,0.025963360783,0.0310093045706,0.035792138535,0.0400765646566,0.0519272497141,0.0415845077543,0.0476444880596,0.0441119769099,0.050664615445,0.0526808211507,0.0473877760315,0.0398268505919,0.0317628720061,0.0352897295695,0.0277249790567,0.0264671781437,0.01915871554,0.0146224307521,0.00958156839025,0.0110892754217,0.00579553410721,0.00529300110682,0.0035290593812,0.00201740124113,0.00075590049007,0.000252358446569,0.0,0.000252130822703,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.000251770961733,0.000252017871011,0.0,0.0012607777482,0.00100783957898,0.00226974524365,0.0032772871391,0.00453781321669,0.011097473722,0.0110881991197,0.0126025360114,0.0186502288691,0.0219320576825,0.0284887093436,0.0340287397618,0.0400856872162,0.0451133778823,0.0463772524995,0.0509192869005,0.0516829011549,0.0499042020887,0.0499201265568,0.0456294026682,0.0410958106359,0.0451322231699,0.039827538785,0.0239494277149,0.0272195212356,0.0229396403894,0.0196642173734,0.0146193658922,0.012354134315,0.00907918743253,0.00730944287875,0.00453884950745,0.00478865559789,0.00403269148997,0.00352844480876,0.00252244454586,0.00252372690566,0.00100823288933,0.00126131029763,0.000251614677883,0.000756485454199,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0])

    # Creating weights for histo: y5_ETA_6
    y5_ETA_6_weights = numpy.array([0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.000283957625274,0.000287128707592,0.000572547709956,0.000861351732727,0.000858235034671,0.00142977823532,0.000286450303915,0.00143123581351,0.000859256738999,0.00314945657622,0.00143529663835,0.00429543394091,0.00544119536808,0.00543670366794,0.00687030779608,0.00572291084221,0.00886473662672,0.0131701286858,0.00973534068191,0.0134554561147,0.0177613000431,0.0174690846075,0.0151850655816,0.0186052458129,0.0208887349921,0.0174626364735,0.0197556129072,0.0174692045728,0.0154570468727,0.0123066885575,0.010887799171,0.00944630632579,0.00601141435195,0.00457853701348,0.00315233774244,0.00228783792074,0.0017190425249,0.000574099460894,0.00085594249811,0.000286764712928,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.00085828172116,0.00257774402458,0.00229116695735,0.00515367657338,0.00314700028705,0.00745015599335,0.0103183139748,0.0122993706752,0.0143236348717,0.0151823563656,0.0186132135071,0.0191729715183,0.0237481674986,0.0226402381232,0.0217478463732,0.0211806505145,0.0189065386215,0.0180207549592,0.0117413421635,0.0131746173868,0.0146080025783,0.00887664717991,0.00715153841053,0.00629180320999,0.00514740738762,0.00373118123045,0.0042993318129,0.00286459701196,0.00228898858775,0.00114435383452,0.00257892468291,0.00114002408751,0.00200925553992,0.0,0.000568809991618,0.00057289490948,0.000571732745799,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0])

    # Creating weights for histo: y5_ETA_7
    y5_ETA_7_weights = numpy.array([0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,2.1617996646e-05,8.63041639912e-05,0.000129543836942,0.000129532437545,0.0,0.00021618093038,8.64047469058e-05,0.000237509621227,0.000129647940258,0.000322270298485,0.000410490734636,0.000430353219956,0.000626435839991,0.000475241698333,0.000691605605799,0.000819277594701,0.000970180465002,0.00112314528505,0.00105669727804,0.00114471529107,0.00118825302473,0.0014903026789,0.0017929520587,0.00114463650112,0.00161964099142,0.00144665053218,0.00170707143259,0.00164166529694,0.00123133310612,0.00123126898451,0.000928988408734,0.000496921088276,0.000366997383194,0.000345373062397,0.000172778396927,2.15827549073e-05,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,2.15983662139e-05,0.0,0.0,6.48950068125e-05,0.000107900405391,0.000280954818599,0.0004105766073,0.000496826372698,0.00094881791124,0.00116613190815,0.00172641059339,0.00185748940943,0.00190084693203,0.00185734859335,0.00172633389892,0.002138216743,0.00196600957321,0.00140282697541,0.00108005933632,0.000926656561499,0.00125301165787,0.000777599387679,0.00108001868406,0.00099358569012,0.000907322010752,0.000712771184686,0.000691494964593,0.000496688909381,0.00010813861926,0.000280705372971,0.000302205809145,0.000365607872139,0.000194619348176,0.000172678819842,0.000151298580251,0.000108110372225,0.000108019428507,8.64090216796e-05,4.32315844076e-05,4.32170417946e-05,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0])

    # Creating weights for histo: y5_ETA_8
    y5_ETA_8_weights = numpy.array([0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,2.84292642893e-05,0.0,2.83973993922e-05,2.83973993922e-05,5.66030748554e-05,2.84292642893e-05,0.000141723376559,0.000113644061894,0.000112773137535,0.000198503757442,0.000141120452911,8.50868331672e-05,0.000142062857986,0.000225435534901,0.000111915784712,0.000255442735234,0.000113583286953,5.67183438192e-05,0.000198632048547,0.000170429981271,0.000198798351831,0.000198741185077,0.000142022856106,0.000113357649033,0.000113596531822,0.0,2.83973993922e-05,2.83973993922e-05,2.83498693196e-05,5.64019963668e-05,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,5.67658887402e-05,2.83684893481e-05,0.000142025796111,5.68978177294e-05,8.45111565312e-05,0.000141783943621,0.000113497477428,0.000198740145682,0.000141909131387,0.000198819139742,0.000142041461286,0.000113259010398,0.000113446992503,2.84292642893e-05,5.51480250594e-05,5.65914781711e-05,0.000113545022349,0.000113683677712,8.51264489853e-05,0.000170163302076,2.84080903176e-05,2.83973993922e-05,0.000113642859165,8.52862783201e-05,5.6878173154e-05,2.84489088647e-05,0.0,8.51961775765e-05,0.0,0.0,2.83684893481e-05,2.84489088647e-05,0.0,2.83684893481e-05,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0])

    # Creating weights for histo: y5_ETA_9
    y5_ETA_9_weights = numpy.array([0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0])

    # Creating weights for histo: y5_ETA_10
    y5_ETA_10_weights = numpy.array([0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,1.0521138287,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,1.0529581672,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,1.05462838872,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0])

    # Creating weights for histo: y5_ETA_11
    y5_ETA_11_weights = numpy.array([0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.230673161153,0.0,0.0,0.0,0.0,0.691026068854,0.230619670779,0.690578010125,0.460783443723,0.229982512821,0.230364746113,0.0,0.229982512821,0.921962685466,0.461195765349,0.691490266921,0.0,0.460080998305,0.461188848491,0.690561870788,0.230752243903,0.461033219172,0.230597152562,0.230428265931,0.229982512821,0.459723627277,0.230360173301,0.230020171273,0.0,0.0,0.0,0.0,0.0,0.0,0.229952462913,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.230020171273,0.0,0.0,0.0,0.690728643934,0.0,0.229982512821,0.230465309552,0.0,0.0,0.0,0.0,0.921987663011,0.691353466828,0.690780136104,0.0,0.691670105244,0.0,0.0,1.15198896663,0.461138893401,0.230020171273,0.0,0.460124420806,0.0,0.230551270733,0.230752243903,0.229932019753,0.230752243903,0.230587737949,0.460570173916,0.0,0.459889631883,0.0,0.690224097526,0.0,0.230619670779,0.230360173301,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0])

    # Creating weights for histo: y5_ETA_12
    y5_ETA_12_weights = numpy.array([0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0554467039881,0.0831726910094,0.0276908199867,0.0277244637063,0.0277261678187,0.138459100715,0.110763733864,0.110696415651,0.138481027219,0.0553453804604,0.110839668808,0.0276896813472,0.249341468504,0.304489895107,0.193882570303,0.165968553895,0.415543020352,0.221455956552,0.110817588434,0.41551493904,0.24918529025,0.138688482718,0.415323370639,0.332468383129,0.304440925915,0.30428051623,0.193931154819,0.193743817848,0.138552153719,0.33202835282,0.110822973891,0.110800931985,0.221591477732,0.0553593057136,0.0830496717832,0.027763192836,0.0276953706979,0.0,0.0830522875767,0.0276873271331,0.0,0.0,0.0,0.0,0.0276896813472,0.0276896813472,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.027763192836,0.0,0.0554193535598,0.027603817928,0.0554837482391,0.0277263947773,0.0276586841951,0.0831603813932,0.0553866946095,0.110896946991,0.138389897592,0.0830404011036,0.276814223641,0.221656410957,0.276896121056,0.193704811752,0.193765744352,0.193745241148,0.304459505742,0.304710891184,0.221625021436,0.193771283679,0.166210553255,0.193715351861,0.221506118237,0.332359866169,0.193744356394,0.249216833641,0.19377143755,0.221591593134,0.1384076696,0.110700454743,0.166063030199,0.166173124328,0.0831490719334,0.166071069917,0.0554810939782,0.0830438247156,0.0276586841951,0.0276929395487,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0])

    # Creating weights for histo: y5_ETA_13
    y5_ETA_13_weights = numpy.array([0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0100450209578,0.0,0.0200719202967,0.0302570227044,0.0201730639343,0.0807196141628,0.040348427967,0.0302623268889,0.0604818076191,0.0504090944485,0.0403768120299,0.0504226704906,0.0504235808197,0.0403129979564,0.0706525268263,0.0706297079089,0.120951914474,0.0705543933437,0.0604464807792,0.0605190340126,0.0907542330928,0.0302540671691,0.13107884078,0.0302726621592,0.0604138485135,0.0604985091246,0.050332353701,0.0604686624662,0.0301965950553,0.0,0.0302875915573,0.0302954446635,0.0605230030477,0.0100953560911,0.040347511569,0.0,0.0100921881456,0.0100996953267,0.0201665945285,0.0100953560911,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0201987048721,0.0201875442367,0.0201245615971,0.0201424829437,0.0101000473206,0.0504036264047,0.0302668906724,0.050308903622,0.0503705389745,0.0706056145306,0.0504038145394,0.110960869966,0.100781812144,0.0806490333092,0.0806486084889,0.0806237261587,0.0706145357563,0.0402893536739,0.0605118484812,0.0806438140887,0.0806781031534,0.100820045968,0.050385189205,0.0403465891021,0.0605020047886,0.0705439549028,0.0201625041162,0.0705455328066,0.0201750545207,0.0403691045764,0.0201483758077,0.050360561767,0.0100592767124,0.0604937875508,0.0403312045394,0.0100853121261,0.0100921881456,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0])

    # Creating weights for histo: y5_ETA_14
    y5_ETA_14_weights = numpy.array([0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.00566304279343,0.0113243080673,0.00565465151583,0.0113270474481,0.0226121500506,0.0141291878309,0.00565787567476,0.0141412072492,0.00849151124252,0.0198041884835,0.0282808755203,0.0339622436944,0.0254604059094,0.0226399170613,0.0113074601055,0.0396079460531,0.0396194499137,0.0396201424538,0.0339383202812,0.0481071444908,0.00849126115859,0.0254815707045,0.0339557068853,0.0113223958871,0.0169703182216,0.0283032714978,0.0141288069338,0.0226442338946,0.0197992483641,0.0282745349309,0.0141461896905,0.0113219688207,0.0141390603748,0.0056663977655,0.0113208722989,0.00566218481319,0.00282800521671,0.00283012131147,0.00282190547736,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.00282347946712,0.00565759865872,0.0,0.00283355053922,0.00849388896355,0.00566924872226,0.0113134197978,0.0141524456361,0.0113166093298,0.0113165477706,0.0254648920303,0.0169795905641,0.0198015222041,0.0282696871502,0.0226120269323,0.0339307869839,0.0395990199806,0.0282947532545,0.0226330955413,0.0254486750495,0.039614178914,0.0226347076208,0.0424486301401,0.0395931718642,0.0339560146809,0.0395998279441,0.0198092017043,0.016970391323,0.028310854812,0.0198078820307,0.0339708581238,0.0198045462959,0.0169803023414,0.0113155205028,0.00282142762469,0.0113133543913,0.00849043780536,0.0,0.00282930950057,0.00283041371729,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0])

    # Creating weights for histo: y5_ETA_15
    y5_ETA_15_weights = numpy.array([0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.00152260673975,0.00153821483072,0.00151881876977,0.0,0.00304355646424,0.0,0.00456097823541,0.0015356572123,0.00456914512233,0.00152449658811,0.00305783256077,0.00303609280421,0.00304190063088,0.0,0.00304325980887,0.00151265401114,0.00152644434928,0.0,0.00150849610837,0.00154541020084,0.00152162931349,0.00152305585944,0.0030361719911,0.00152449658811,0.00153629543501,0.0,0.0,0.00152495989053,0.00153629543501,0.00153333597266,0.00152162931349,0.00152094972449,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.00154541020084,0.00153219780883,0.00151265401114,0.00305061000709,0.00150849610837,0.00152162931349,0.00151727403443,0.0,0.0,0.0,0.00306015380041,0.00306014316337,0.00305496528615,0.00607878412211,0.00301699221674,0.00306438379871,0.00152192833265,0.00151115655156,0.00305428569715,0.00150849610837,0.00304681258196,0.0,0.00303898371671,0.0,0.0,0.0,0.00151265401114,0.0,0.00152094972449,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0])

    # Creating weights for histo: y5_ETA_16
    y5_ETA_16_weights = numpy.array([0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.000180755028423,0.0,0.0,0.0,0.0,0.000180686039232,0.0,0.000542211148965,0.000541323760103,0.0,0.0,0.0,0.0,0.000361533925874,0.000180154568376,0.000722930104357,0.000360550714414,0.000360973850682,0.000180970234659,0.000180626135672,0.000541377657908,0.00018065712691,0.0,0.000180533816432,0.0,0.0,0.0,0.000180553027149,0.000180626135672,0.000180003616023,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.000180553027149,0.0,0.0,0.000180626135672,0.00018065712691,0.000361237718936,0.000180626135672,0.0,0.0,0.0,0.000179998688224,0.0,0.000180766962937,0.0,0.000360616354241,0.000902862921764,0.0,0.0,0.0,0.00018065712691,0.000542553400027,0.0,0.000361314061327,0.0,0.000180402036298,0.0,0.0,0.000360206615427,0.0,0.000180755028423,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0])

    # Creating a new Canvas
    fig   = plt.figure(figsize=(12,6),dpi=80)
    frame = gridspec.GridSpec(1,1,right=0.7)
    pad   = fig.add_subplot(frame[0])

    # Creating a new Stack
    pad.hist(x=xData, bins=xBinning, weights=y5_ETA_0_weights+y5_ETA_1_weights+y5_ETA_2_weights+y5_ETA_3_weights+y5_ETA_4_weights+y5_ETA_5_weights+y5_ETA_6_weights+y5_ETA_7_weights+y5_ETA_8_weights+y5_ETA_9_weights+y5_ETA_10_weights+y5_ETA_11_weights+y5_ETA_12_weights+y5_ETA_13_weights+y5_ETA_14_weights+y5_ETA_15_weights+y5_ETA_16_weights,\
             label="$bg\_dip\_1600\_inf$", histtype="step", rwidth=1.0,\
             color=None, edgecolor="#e5e5e5", linewidth=1, linestyle="solid",\
             bottom=None, cumulative=False, normed=False, align="mid", orientation="vertical")

    pad.hist(x=xData, bins=xBinning, weights=y5_ETA_0_weights+y5_ETA_1_weights+y5_ETA_2_weights+y5_ETA_3_weights+y5_ETA_4_weights+y5_ETA_5_weights+y5_ETA_6_weights+y5_ETA_7_weights+y5_ETA_8_weights+y5_ETA_9_weights+y5_ETA_10_weights+y5_ETA_11_weights+y5_ETA_12_weights+y5_ETA_13_weights+y5_ETA_14_weights+y5_ETA_15_weights,\
             label="$bg\_dip\_1200\_1600$", histtype="step", rwidth=1.0,\
             color=None, edgecolor="#f2f2f2", linewidth=1, linestyle="solid",\
             bottom=None, cumulative=False, normed=False, align="mid", orientation="vertical")

    pad.hist(x=xData, bins=xBinning, weights=y5_ETA_0_weights+y5_ETA_1_weights+y5_ETA_2_weights+y5_ETA_3_weights+y5_ETA_4_weights+y5_ETA_5_weights+y5_ETA_6_weights+y5_ETA_7_weights+y5_ETA_8_weights+y5_ETA_9_weights+y5_ETA_10_weights+y5_ETA_11_weights+y5_ETA_12_weights+y5_ETA_13_weights+y5_ETA_14_weights,\
             label="$bg\_dip\_800\_1200$", histtype="step", rwidth=1.0,\
             color=None, edgecolor="#ccc6aa", linewidth=1, linestyle="solid",\
             bottom=None, cumulative=False, normed=False, align="mid", orientation="vertical")

    pad.hist(x=xData, bins=xBinning, weights=y5_ETA_0_weights+y5_ETA_1_weights+y5_ETA_2_weights+y5_ETA_3_weights+y5_ETA_4_weights+y5_ETA_5_weights+y5_ETA_6_weights+y5_ETA_7_weights+y5_ETA_8_weights+y5_ETA_9_weights+y5_ETA_10_weights+y5_ETA_11_weights+y5_ETA_12_weights+y5_ETA_13_weights,\
             label="$bg\_dip\_600\_800$", histtype="step", rwidth=1.0,\
             color=None, edgecolor="#ccc6aa", linewidth=1, linestyle="solid",\
             bottom=None, cumulative=False, normed=False, align="mid", orientation="vertical")

    pad.hist(x=xData, bins=xBinning, weights=y5_ETA_0_weights+y5_ETA_1_weights+y5_ETA_2_weights+y5_ETA_3_weights+y5_ETA_4_weights+y5_ETA_5_weights+y5_ETA_6_weights+y5_ETA_7_weights+y5_ETA_8_weights+y5_ETA_9_weights+y5_ETA_10_weights+y5_ETA_11_weights+y5_ETA_12_weights,\
             label="$bg\_dip\_400\_600$", histtype="step", rwidth=1.0,\
             color=None, edgecolor="#c1bfa8", linewidth=1, linestyle="solid",\
             bottom=None, cumulative=False, normed=False, align="mid", orientation="vertical")

    pad.hist(x=xData, bins=xBinning, weights=y5_ETA_0_weights+y5_ETA_1_weights+y5_ETA_2_weights+y5_ETA_3_weights+y5_ETA_4_weights+y5_ETA_5_weights+y5_ETA_6_weights+y5_ETA_7_weights+y5_ETA_8_weights+y5_ETA_9_weights+y5_ETA_10_weights+y5_ETA_11_weights,\
             label="$bg\_dip\_200\_400$", histtype="step", rwidth=1.0,\
             color=None, edgecolor="#bab5a3", linewidth=1, linestyle="solid",\
             bottom=None, cumulative=False, normed=False, align="mid", orientation="vertical")

    pad.hist(x=xData, bins=xBinning, weights=y5_ETA_0_weights+y5_ETA_1_weights+y5_ETA_2_weights+y5_ETA_3_weights+y5_ETA_4_weights+y5_ETA_5_weights+y5_ETA_6_weights+y5_ETA_7_weights+y5_ETA_8_weights+y5_ETA_9_weights+y5_ETA_10_weights,\
             label="$bg\_dip\_100\_200$", histtype="step", rwidth=1.0,\
             color=None, edgecolor="#b2a596", linewidth=1, linestyle="solid",\
             bottom=None, cumulative=False, normed=False, align="mid", orientation="vertical")

    pad.hist(x=xData, bins=xBinning, weights=y5_ETA_0_weights+y5_ETA_1_weights+y5_ETA_2_weights+y5_ETA_3_weights+y5_ETA_4_weights+y5_ETA_5_weights+y5_ETA_6_weights+y5_ETA_7_weights+y5_ETA_8_weights+y5_ETA_9_weights,\
             label="$bg\_dip\_0\_100$", histtype="step", rwidth=1.0,\
             color=None, edgecolor="#b7a39b", linewidth=1, linestyle="solid",\
             bottom=None, cumulative=False, normed=False, align="mid", orientation="vertical")

    pad.hist(x=xData, bins=xBinning, weights=y5_ETA_0_weights+y5_ETA_1_weights+y5_ETA_2_weights+y5_ETA_3_weights+y5_ETA_4_weights+y5_ETA_5_weights+y5_ETA_6_weights+y5_ETA_7_weights+y5_ETA_8_weights,\
             label="$bg\_vbf\_1600\_inf$", histtype="step", rwidth=1.0,\
             color=None, edgecolor="#ad998c", linewidth=1, linestyle="solid",\
             bottom=None, cumulative=False, normed=False, align="mid", orientation="vertical")

    pad.hist(x=xData, bins=xBinning, weights=y5_ETA_0_weights+y5_ETA_1_weights+y5_ETA_2_weights+y5_ETA_3_weights+y5_ETA_4_weights+y5_ETA_5_weights+y5_ETA_6_weights+y5_ETA_7_weights,\
             label="$bg\_vbf\_1200\_1600$", histtype="step", rwidth=1.0,\
             color=None, edgecolor="#9b8e82", linewidth=1, linestyle="solid",\
             bottom=None, cumulative=False, normed=False, align="mid", orientation="vertical")

    pad.hist(x=xData, bins=xBinning, weights=y5_ETA_0_weights+y5_ETA_1_weights+y5_ETA_2_weights+y5_ETA_3_weights+y5_ETA_4_weights+y5_ETA_5_weights+y5_ETA_6_weights,\
             label="$bg\_vbf\_800\_1200$", histtype="step", rwidth=1.0,\
             color=None, edgecolor="#876656", linewidth=1, linestyle="solid",\
             bottom=None, cumulative=False, normed=False, align="mid", orientation="vertical")

    pad.hist(x=xData, bins=xBinning, weights=y5_ETA_0_weights+y5_ETA_1_weights+y5_ETA_2_weights+y5_ETA_3_weights+y5_ETA_4_weights+y5_ETA_5_weights,\
             label="$bg\_vbf\_600\_800$", histtype="step", rwidth=1.0,\
             color=None, edgecolor="#afcec6", linewidth=1, linestyle="solid",\
             bottom=None, cumulative=False, normed=False, align="mid", orientation="vertical")

    pad.hist(x=xData, bins=xBinning, weights=y5_ETA_0_weights+y5_ETA_1_weights+y5_ETA_2_weights+y5_ETA_3_weights+y5_ETA_4_weights,\
             label="$bg\_vbf\_400\_600$", histtype="step", rwidth=1.0,\
             color=None, edgecolor="#84c1a3", linewidth=1, linestyle="solid",\
             bottom=None, cumulative=False, normed=False, align="mid", orientation="vertical")

    pad.hist(x=xData, bins=xBinning, weights=y5_ETA_0_weights+y5_ETA_1_weights+y5_ETA_2_weights+y5_ETA_3_weights,\
             label="$bg\_vbf\_200\_400$", histtype="step", rwidth=1.0,\
             color=None, edgecolor="#89a8a0", linewidth=1, linestyle="solid",\
             bottom=None, cumulative=False, normed=False, align="mid", orientation="vertical")

    pad.hist(x=xData, bins=xBinning, weights=y5_ETA_0_weights+y5_ETA_1_weights+y5_ETA_2_weights,\
             label="$bg\_vbf\_100\_200$", histtype="step", rwidth=1.0,\
             color=None, edgecolor="#829e8c", linewidth=1, linestyle="solid",\
             bottom=None, cumulative=False, normed=False, align="mid", orientation="vertical")

    pad.hist(x=xData, bins=xBinning, weights=y5_ETA_0_weights+y5_ETA_1_weights,\
             label="$bg\_vbf\_0\_100$", histtype="step", rwidth=1.0,\
             color=None, edgecolor="#adbcc6", linewidth=1, linestyle="solid",\
             bottom=None, cumulative=False, normed=False, align="mid", orientation="vertical")

    pad.hist(x=xData, bins=xBinning, weights=y5_ETA_0_weights,\
             label="$signal$", histtype="step", rwidth=1.0,\
             color=None, edgecolor="#7a8e99", linewidth=1, linestyle="solid",\
             bottom=None, cumulative=False, normed=False, align="mid", orientation="vertical")


    # Axis
    plt.rc('text',usetex=False)
    plt.xlabel(r"\eta [ j_{2} ] ",\
               fontsize=16,color="black")
    plt.ylabel(r"$\mathrm{Events}$ $(\mathcal{L}_{\mathrm{int}} = 40.0\ \mathrm{fb}^{-1})$ ",\
               fontsize=16,color="black")

    # Boundary of y-axis
    ymax=(y5_ETA_0_weights+y5_ETA_1_weights+y5_ETA_2_weights+y5_ETA_3_weights+y5_ETA_4_weights+y5_ETA_5_weights+y5_ETA_6_weights+y5_ETA_7_weights+y5_ETA_8_weights+y5_ETA_9_weights+y5_ETA_10_weights+y5_ETA_11_weights+y5_ETA_12_weights+y5_ETA_13_weights+y5_ETA_14_weights+y5_ETA_15_weights+y5_ETA_16_weights).max()*1.1
    ymin=0 # linear scale
    #ymin=min([x for x in (y5_ETA_0_weights+y5_ETA_1_weights+y5_ETA_2_weights+y5_ETA_3_weights+y5_ETA_4_weights+y5_ETA_5_weights+y5_ETA_6_weights+y5_ETA_7_weights+y5_ETA_8_weights+y5_ETA_9_weights+y5_ETA_10_weights+y5_ETA_11_weights+y5_ETA_12_weights+y5_ETA_13_weights+y5_ETA_14_weights+y5_ETA_15_weights+y5_ETA_16_weights) if x])/100. # log scale
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
    plt.savefig('../../HTML/MadAnalysis5job_0/selection_4.png')
    plt.savefig('../../PDF/MadAnalysis5job_0/selection_4.png')
    plt.savefig('../../DVI/MadAnalysis5job_0/selection_4.eps')

# Running!
if __name__ == '__main__':
    selection_4()
