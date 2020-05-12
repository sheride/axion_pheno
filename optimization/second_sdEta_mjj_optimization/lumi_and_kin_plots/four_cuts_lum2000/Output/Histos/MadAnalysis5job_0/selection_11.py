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
    y12_PT_0_weights = numpy.array([0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,1287.58950936,1390.1462225,1489.01833875,1572.537668,1570.69526956,1551.65788569,1558.82247962,1537.73789748,1483.90074308,1484.51494256,1395.05921833,1342.85946255,1295.77750243,1233.54755514,1172.54560681,1123.41664842,1019.63153633,994.043558009,935.088807945,871.835261524,808.172115449,769.48314822,723.424587233,679.208624685,639.08645867,603.672688667,566.825919878,508.485169294,483.715990275,454.034015417,421.895442639,402.039059458,349.225304193,334.077317024,318.724530029,297.844547715,274.712967308,254.447384474,230.292204934,222.718211349,189.556099439,176.045610883,180.139687415,160.078684407,155.575188222,146.158796198,122.208416485,115.043762554,109.107347582,99.4862357315,97.4391974654,95.5968590259,82.2910902964,80.0393522037,65.5053445146,62.8441867687,59.9783291962,53.6324945713,51.176056652,45.0349218538,46.46786064,37.6655680959,36.4373491362,35.4138300032,34.7997105234,32.1385527775,28.4538758985,22.9268605801])

    # Creating weights for histo: y12_PT_1
    y12_PT_1_weights = numpy.array([0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,1.21472880116,0.60876676669,0.0,0.0,0.0,0.0,0.606569232146,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0])

    # Creating weights for histo: y12_PT_2
    y12_PT_2_weights = numpy.array([0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,17.0714413011,17.0611215395,4.51826639568,4.01343275017,4.51746478057,3.0130914659,1.50881938612,2.00649572433,0.501704660748,1.50712752371,0.0,1.00557554172,1.00446505686,0.0,0.0,0.503483502532,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0])

    # Creating weights for histo: y12_PT_3
    y12_PT_3_weights = numpy.array([0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,69.0220461706,54.4496026869,41.8060504629,33.0062242415,24.7536474587,22.8275187514,17.335381807,10.1733753891,7.69448635762,4.67559349386,3.30173557026,2.47442425929,2.19945279578,2.47595178825,1.37436290192,0.82540555609,1.10182268763,0.5495978111,0.27518535819,0.0,0.0,0.273960491216,0.275207296106,0.274721411893,0.0,0.274237152711,0.274799007114,0.0,0.274403108983,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.275710852528,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0])

    # Creating weights for histo: y12_PT_4
    y12_PT_4_weights = numpy.array([0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,27.4353190622,24.4714695165,25.2607818957,22.8470500499,21.416371259,19.0474240324,16.9738777253,13.4710094333,12.0396953285,8.73265202275,7.74626407099,5.32873236673,4.73756777754,2.91052927396,2.12134516002,1.43158546602,1.52988495948,1.03611258742,0.542820608862,0.543226247765,0.296097359801,0.542721403695,0.197418020776,0.0986040833883,0.148024570039,0.0986992802652,0.148166904401,0.0,0.0493829690603,0.0,0.0492109733555,0.147875742248,0.0988017521877,0.0491954412334,0.0,0.0,0.0,0.0492714384034,0.0,0.0,0.0,0.0987516084854,0.0,0.0491954412334,0.0,0.0,0.0,0.0,0.0,0.0,0.049339719616,0.0,0.0,0.0,0.0493145275161,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0])

    # Creating weights for histo: y12_PT_5
    y12_PT_5_weights = numpy.array([0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,5.68387049621,5.40739493652,5.09204247069,5.18032123553,5.30621055127,5.09164635957,4.89031187921,4.91509483157,4.72614382514,4.44933217117,4.60027851615,4.07176225148,3.65505935381,3.26430373514,2.89853912719,2.94911931645,2.23095384949,1.92866264774,1.46218218597,1.08406011139,0.642773117145,0.655301031601,0.415965690857,0.290000153744,0.189114552306,0.151295662973,0.264721462313,0.0378029248546,0.0882372732026,0.0756254752148,0.0504713587304,0.0630576895739,0.0252171341627,0.0126065405129,0.0251928473496,0.0126179217056,0.0125885474653,0.0,0.0125807332732,0.0,0.0125807332732,0.0126041178332,0.0,0.0,0.0126043098871,0.0126008929285,0.0126093292952,0.0,0.0,0.0,0.0,0.0,0.0,0.0125979080912,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0])

    # Creating weights for histo: y12_PT_6
    y12_PT_6_weights = numpy.array([0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,1.27486504818,1.1315210326,0.987373249629,1.04520751213,1.10222900984,1.18764828911,1.0589710289,1.34494926548,1.24555703005,0.972331602751,1.33138819012,1.01693019571,1.14568843248,1.10209204948,1.01692619687,1.31692687529,1.04513303368,1.17428665603,0.959440833399,1.10217652503,1.03110459358,0.930706649204,0.987978574445,0.601345967704,0.786741813292,0.801418065916,0.601765346334,0.429468909717,0.514863995986,0.429546037396,0.386464705332,0.24313693505,0.20022355438,0.271824082857,0.114410189164,0.0428954758515,0.0427474186999,0.0429187191248,0.014227022634,0.0143091888548,0.0,0.0431162669535,0.0,0.0,0.0,0.0428925566963,0.0,0.0,0.0143091888548,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0])

    # Creating weights for histo: y12_PT_7
    y12_PT_7_weights = numpy.array([0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0831560627448,0.0842338924582,0.0669606005132,0.0766646721541,0.0518231028699,0.0669535177999,0.0604112280651,0.0614648131059,0.0431962532539,0.0583169661239,0.0550974119081,0.0593976456864,0.0529232703715,0.0421253386157,0.0539910627484,0.0507557505432,0.0431900506411,0.0399771600431,0.0518544093011,0.0421127867066,0.0431910983797,0.0637258750416,0.0421489546451,0.053922834007,0.0518286139753,0.0486096255383,0.0496732269607,0.0539805224975,0.0486149899603,0.049694537965,0.0637027619268,0.0733682977398,0.0659065544674,0.0723690274712,0.0658737183379,0.0850585675567,0.073449392712,0.0712710183113,0.0842321951215,0.0570949675711,0.0626401663336,0.0604939365549,0.0432049494848,0.046365243602,0.0399593694407,0.0259109751787,0.0226805454356,0.0172875474771,0.01504074736,0.0118873180265,0.0129509802176,0.00432465028,0.00432181719467,0.00647910271172,0.00107913771027,0.0,0.0,0.00216102175311,0.00107966975196,0.0,0.0,0.0,0.00108375928549,0.00108110410618,0.0,0.0,0.0,0.0])

    # Creating weights for histo: y12_PT_8
    y12_PT_8_weights = numpy.array([0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.00568683606153,0.00425671907843,0.00283993902531,0.0,0.00426173861659,0.00424375187629,0.0014128667288,0.0,0.00284231552904,0.00568107409796,0.00568127232554,0.00565601798294,0.00425116053942,0.0,0.00426272084541,0.00709717260455,0.00568160864425,0.00284133404265,0.00141749352393,0.00141749352393,0.00284087002677,0.00283412360711,0.0,0.00141749352393,0.0,0.00283591730689,0.00142040457394,0.0,0.00284285007533,0.0,0.00283591730689,0.00283228387696,0.00566182152234,0.00142146327257,0.00284133404265,0.00426074005442,0.00141842452539,0.00565984073135,0.00425725362472,0.00568524281661,0.00425975782561,0.00141842452539,0.00568622504542,0.00983012812891,0.00284133404265,0.00141987002765,0.00702829705724,0.00567031115685,0.00284186858894,0.00568622504542,0.014187697532,0.00851117969877,0.00710167764191,0.00426067991797,0.0028389567965,0.005664447481,0.0070818118229,0.00852498138706,0.00852664441997,0.00708978398691,0.00142244550138,0.00702330870094,0.00709924916841,0.0,0.00283988779796,0.00278398464977,0.00567375601073,0.00423362370891])

    # Creating weights for histo: y12_PT_9
    y12_PT_9_weights = numpy.array([0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0])

    # Creating weights for histo: y12_PT_10
    y12_PT_10_weights = numpy.array([0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,52.6056850335,105.379334197,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0])

    # Creating weights for histo: y12_PT_11
    y12_PT_11_weights = numpy.array([0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,161.275851417,92.1790222383,218.853074363,149.680659284,138.19630982,69.1021705308,23.0069337894,23.0224198685,34.4838092034,0.0,11.5064276947,11.5180095911,11.5336589849,0.0,0.0,0.0,0.0,0.0,0.0,0.0,11.5336589849,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0])

    # Creating weights for histo: y12_PT_12
    y12_PT_12_weights = numpy.array([0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,56.7569291628,41.5345113402,49.8440409419,53.9910545313,45.7118758274,37.3805351241,44.3107722105,44.3095989502,42.9154771939,34.6214115477,36.0010118035,40.1590848137,24.9065853661,15.233784984,9.68465800467,4.14950051651,4.15142197069,11.0813743973,5.53202238274,2.77502606199,1.38190753944,1.38293423838,0.0,0.0,1.38348086228,1.38631976756,0.0,1.38653537818,1.38464700609,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0])

    # Creating weights for histo: y12_PT_13
    y12_PT_13_weights = numpy.array([0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,4.03315576214,9.57820442714,6.04355402532,5.54554327718,5.04075057668,6.05257842189,6.55315022945,5.04108436405,7.55576857782,8.57254861375,9.58493782862,9.57910868746,11.0880066073,11.0822502925,16.6383533881,9.07255298278,10.079504498,10.5879445841,7.05858016037,5.04149401218,3.52748914563,2.01794853337,2.52160999815,2.01586448644,1.51352572995,0.502147890802,3.0267413411,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.504028327437,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.5048758439,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0])

    # Creating weights for histo: y12_PT_14
    y12_PT_14_weights = numpy.array([0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,2.82823379118,1.83999309197,1.84008543065,1.41475961129,1.55545856165,1.41511338387,0.848398959621,0.989347032049,0.707352969716,1.27268846965,1.69731001418,1.55669205254,1.69627255062,1.55597238794,1.98158618856,1.55568171346,1.13229365982,2.26162247847,2.68766738531,3.39542799183,2.68840032359,2.82883976378,3.95975199845,5.23764625366,4.38581037135,3.39523561958,2.54581016161,1.69716919769,2.12217567911,2.26187833356,1.97996064302,0.848431470532,0.424173894301,1.41411035494,0.849270598303,0.566199058977,0.706907050832,0.848985502623,0.141506067387,0.0,0.141548908688,0.282681023651,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0])

    # Creating weights for histo: y12_PT_15
    y12_PT_15_weights = numpy.array([0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.305043755349,0.153481575561,0.0,0.153366931848,0.0,0.0,0.0,0.0758637042809,0.0762248319771,0.0756327031086,0.0,0.0754248079629,0.0,0.152762629472,0.0,0.152431285503,0.0768147743418,0.0,0.0760814682411,0.0,0.0756327031086,0.0,0.0,0.0,0.153007695182,0.0763222200385,0.0754248079629,0.0772705126486,0.0,0.0761303395559,0.07604748879,0.0,0.0,0.152129016126,0.0760814682411,0.152022409292,0.228897814793,0.304658576111,0.0756327031086,0.22703012688,0.457189022517,0.152188938149,0.227245586147,0.07604748879,0.228170004499,0.0754248079629,0.0,0.0766668012194,0.0766668012194,0.152913202761,0.0754248079629,0.0769107441305,0.0765765636164,0.0,0.0755578301269,0.0769107441305,0.0,0.0,0.0,0.0,0.0,0.151857535086,0.0,0.0,0.0,0.0,0.0,0.0])

    # Creating weights for histo: y12_PT_16
    y12_PT_16_weights = numpy.array([0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.00902765150004,0.00902516835112,0.0,0.0,0.00900018094332,0.00903130692623,0.0,0.0,0.00903130692623,0.0,0.0,0.0,0.00903130692623,0.0,0.0,0.0,0.00903671595604,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.00904851187585,0.0,0.00899993455335,0.00902010195737,0.0,0.0180712047777,0.00900772856107,0.00902735698703,0.00902669096414,0.0180961729363,0.0270545234075,0.063234542082,0.00903285648815,0.0180202829007,0.036098498243,0.0,0.0180555339907,0.0,0.0180657033517,0.0,0.00901015011249,0.00904851187585,0.036057574409,0.0,0.0,0.0])

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
    plt.ylabel(r"$\mathrm{Events}$ $(\mathcal{L}_{\mathrm{int}} = 2000.0\ \mathrm{fb}^{-1})$ ",\
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
