void selection_3()
{

  // ROOT version
  Int_t root_version = gROOT->GetVersionInt();

  // Creating a new TCanvas
  TCanvas* canvas = new TCanvas("canvas_plotflow_tempo7","canvas_plotflow_tempo7",0,0,1000,500);
  gStyle->SetOptStat(0);
  gStyle->SetOptTitle(0);
  canvas->SetHighLightColor(2);
  canvas->SetFillColor(0);
  canvas->SetBorderMode(0);
  canvas->SetBorderSize(3);
  canvas->SetFrameBorderMode(0);
  canvas->SetFrameBorderSize(0);
  canvas->SetTickx(1);
  canvas->SetTicky(1);
  canvas->SetLeftMargin(0.14);
  canvas->SetRightMargin(0.3);
  canvas->SetBottomMargin(0.15);
  canvas->SetTopMargin(0.05);

  // Creating a new TH1F
  TH1F* S4_PT_0 = new TH1F("S4_PT_0","S4_PT_0",100,0.0,1000.0);
  // Content
  S4_PT_0->SetBinContent(0,0.0); // underflow
  S4_PT_0->SetBinContent(1,0.0);
  S4_PT_0->SetBinContent(2,0.0);
  S4_PT_0->SetBinContent(3,53667.0718078);
  S4_PT_0->SetBinContent(4,42283.1535455);
  S4_PT_0->SetBinContent(5,34964.9186627);
  S4_PT_0->SetBinContent(6,23174.4204625);
  S4_PT_0->SetBinContent(7,22361.2845866);
  S4_PT_0->SetBinContent(8,17482.4573313);
  S4_PT_0->SetBinContent(9,18295.5972072);
  S4_PT_0->SetBinContent(10,17889.0292693);
  S4_PT_0->SetBinContent(11,13010.202014);
  S4_PT_0->SetBinContent(12,14636.4777658);
  S4_PT_0->SetBinContent(13,12197.0661381);
  S4_PT_0->SetBinContent(14,12197.0661381);
  S4_PT_0->SetBinContent(15,9351.08257257);
  S4_PT_0->SetBinContent(16,12603.6340761);
  S4_PT_0->SetBinContent(17,9757.65051051);
  S4_PT_0->SetBinContent(18,6911.67094494);
  S4_PT_0->SetBinContent(19,6911.67094494);
  S4_PT_0->SetBinContent(20,5691.96313113);
  S4_PT_0->SetBinContent(21,5691.96313113);
  S4_PT_0->SetBinContent(22,6911.67094494);
  S4_PT_0->SetBinContent(23,4472.25531732);
  S4_PT_0->SetBinContent(24,6505.09900701);
  S4_PT_0->SetBinContent(25,3252.5503035);
  S4_PT_0->SetBinContent(26,3659.11944144);
  S4_PT_0->SetBinContent(27,3252.5503035);
  S4_PT_0->SetBinContent(28,2032.84408969);
  S4_PT_0->SetBinContent(29,2032.84408969);
  S4_PT_0->SetBinContent(30,1219.70661381);
  S4_PT_0->SetBinContent(31,2439.41282763);
  S4_PT_0->SetBinContent(32,1626.27535175);
  S4_PT_0->SetBinContent(33,2439.41282763);
  S4_PT_0->SetBinContent(34,2439.41282763);
  S4_PT_0->SetBinContent(35,2439.41282763);
  S4_PT_0->SetBinContent(36,2032.84408969);
  S4_PT_0->SetBinContent(37,1626.27535175);
  S4_PT_0->SetBinContent(38,2032.84408969);
  S4_PT_0->SetBinContent(39,1219.70661381);
  S4_PT_0->SetBinContent(40,813.137475876);
  S4_PT_0->SetBinContent(41,1219.70661381);
  S4_PT_0->SetBinContent(42,2439.41282763);
  S4_PT_0->SetBinContent(43,1626.27535175);
  S4_PT_0->SetBinContent(44,1219.70661381);
  S4_PT_0->SetBinContent(45,1219.70661381);
  S4_PT_0->SetBinContent(46,0.0);
  S4_PT_0->SetBinContent(47,406.568737938);
  S4_PT_0->SetBinContent(48,406.568737938);
  S4_PT_0->SetBinContent(49,406.568737938);
  S4_PT_0->SetBinContent(50,406.568737938);
  S4_PT_0->SetBinContent(51,0.0);
  S4_PT_0->SetBinContent(52,813.137475876);
  S4_PT_0->SetBinContent(53,406.568737938);
  S4_PT_0->SetBinContent(54,813.137475876);
  S4_PT_0->SetBinContent(55,406.568737938);
  S4_PT_0->SetBinContent(56,0.0);
  S4_PT_0->SetBinContent(57,0.0);
  S4_PT_0->SetBinContent(58,813.137475876);
  S4_PT_0->SetBinContent(59,0.0);
  S4_PT_0->SetBinContent(60,0.0);
  S4_PT_0->SetBinContent(61,406.568737938);
  S4_PT_0->SetBinContent(62,0.0);
  S4_PT_0->SetBinContent(63,0.0);
  S4_PT_0->SetBinContent(64,406.568737938);
  S4_PT_0->SetBinContent(65,0.0);
  S4_PT_0->SetBinContent(66,0.0);
  S4_PT_0->SetBinContent(67,0.0);
  S4_PT_0->SetBinContent(68,0.0);
  S4_PT_0->SetBinContent(69,0.0);
  S4_PT_0->SetBinContent(70,0.0);
  S4_PT_0->SetBinContent(71,406.568737938);
  S4_PT_0->SetBinContent(72,0.0);
  S4_PT_0->SetBinContent(73,406.568737938);
  S4_PT_0->SetBinContent(74,0.0);
  S4_PT_0->SetBinContent(75,0.0);
  S4_PT_0->SetBinContent(76,0.0);
  S4_PT_0->SetBinContent(77,0.0);
  S4_PT_0->SetBinContent(78,0.0);
  S4_PT_0->SetBinContent(79,0.0);
  S4_PT_0->SetBinContent(80,0.0);
  S4_PT_0->SetBinContent(81,0.0);
  S4_PT_0->SetBinContent(82,0.0);
  S4_PT_0->SetBinContent(83,0.0);
  S4_PT_0->SetBinContent(84,0.0);
  S4_PT_0->SetBinContent(85,0.0);
  S4_PT_0->SetBinContent(86,406.568737938);
  S4_PT_0->SetBinContent(87,0.0);
  S4_PT_0->SetBinContent(88,0.0);
  S4_PT_0->SetBinContent(89,0.0);
  S4_PT_0->SetBinContent(90,0.0);
  S4_PT_0->SetBinContent(91,0.0);
  S4_PT_0->SetBinContent(92,0.0);
  S4_PT_0->SetBinContent(93,0.0);
  S4_PT_0->SetBinContent(94,0.0);
  S4_PT_0->SetBinContent(95,0.0);
  S4_PT_0->SetBinContent(96,0.0);
  S4_PT_0->SetBinContent(97,0.0);
  S4_PT_0->SetBinContent(98,0.0);
  S4_PT_0->SetBinContent(99,0.0);
  S4_PT_0->SetBinContent(100,0.0);
  S4_PT_0->SetBinContent(101,0.0); // overflow
  S4_PT_0->SetEntries(999);
  // Style
  S4_PT_0->SetLineColor(9);
  S4_PT_0->SetLineStyle(1);
  S4_PT_0->SetLineWidth(1);
  S4_PT_0->SetFillColor(9);
  S4_PT_0->SetFillStyle(1001);

  // Creating a new TH1F
  TH1F* S4_PT_1 = new TH1F("S4_PT_1","S4_PT_1",100,0.0,1000.0);
  // Content
  S4_PT_1->SetBinContent(0,0.0); // underflow
  S4_PT_1->SetBinContent(1,0.0);
  S4_PT_1->SetBinContent(2,0.0);
  S4_PT_1->SetBinContent(3,36477.7714118);
  S4_PT_1->SetBinContent(4,24886.7050567);
  S4_PT_1->SetBinContent(5,20113.9120869);
  S4_PT_1->SetBinContent(6,19432.0839483);
  S4_PT_1->SetBinContent(7,17386.6035327);
  S4_PT_1->SetBinContent(8,14659.2909786);
  S4_PT_1->SetBinContent(9,17727.515602);
  S4_PT_1->SetBinContent(10,16022.9472557);
  S4_PT_1->SetBinContent(11,12954.7226322);
  S4_PT_1->SetBinContent(12,15682.0351864);
  S4_PT_1->SetBinContent(13,11931.9824244);
  S4_PT_1->SetBinContent(14,11931.9824244);
  S4_PT_1->SetBinContent(15,12613.810563);
  S4_PT_1->SetBinContent(16,9204.66987027);
  S4_PT_1->SetBinContent(17,7500.10152392);
  S4_PT_1->SetBinContent(18,8181.92966246);
  S4_PT_1->SetBinContent(19,7841.01759319);
  S4_PT_1->SetBinContent(20,5113.70503904);
  S4_PT_1->SetBinContent(21,5795.53317758);
  S4_PT_1->SetBinContent(22,5113.70503904);
  S4_PT_1->SetBinContent(23,2727.31015415);
  S4_PT_1->SetBinContent(24,6477.36131612);
  S4_PT_1->SetBinContent(25,1704.56874635);
  S4_PT_1->SetBinContent(26,3750.05156196);
  S4_PT_1->SetBinContent(27,4090.96483123);
  S4_PT_1->SetBinContent(28,2727.31015415);
  S4_PT_1->SetBinContent(29,3750.05156196);
  S4_PT_1->SetBinContent(30,2386.39648488);
  S4_PT_1->SetBinContent(31,2727.31015415);
  S4_PT_1->SetBinContent(32,2045.48241562);
  S4_PT_1->SetBinContent(33,4090.96483123);
  S4_PT_1->SetBinContent(34,2045.48241562);
  S4_PT_1->SetBinContent(35,1704.56874635);
  S4_PT_1->SetBinContent(36,1704.56874635);
  S4_PT_1->SetBinContent(37,681.827338539);
  S4_PT_1->SetBinContent(38,1022.74140781);
  S4_PT_1->SetBinContent(39,1022.74140781);
  S4_PT_1->SetBinContent(40,681.827338539);
  S4_PT_1->SetBinContent(41,1022.74140781);
  S4_PT_1->SetBinContent(42,1022.74140781);
  S4_PT_1->SetBinContent(43,1363.65507708);
  S4_PT_1->SetBinContent(44,340.913749269);
  S4_PT_1->SetBinContent(45,340.913749269);
  S4_PT_1->SetBinContent(46,1022.74140781);
  S4_PT_1->SetBinContent(47,0.0);
  S4_PT_1->SetBinContent(48,1022.74140781);
  S4_PT_1->SetBinContent(49,1022.74140781);
  S4_PT_1->SetBinContent(50,1704.56874635);
  S4_PT_1->SetBinContent(51,0.0);
  S4_PT_1->SetBinContent(52,340.913749269);
  S4_PT_1->SetBinContent(53,681.827338539);
  S4_PT_1->SetBinContent(54,681.827338539);
  S4_PT_1->SetBinContent(55,340.913749269);
  S4_PT_1->SetBinContent(56,340.913749269);
  S4_PT_1->SetBinContent(57,0.0);
  S4_PT_1->SetBinContent(58,0.0);
  S4_PT_1->SetBinContent(59,0.0);
  S4_PT_1->SetBinContent(60,681.827338539);
  S4_PT_1->SetBinContent(61,340.913749269);
  S4_PT_1->SetBinContent(62,0.0);
  S4_PT_1->SetBinContent(63,340.913749269);
  S4_PT_1->SetBinContent(64,0.0);
  S4_PT_1->SetBinContent(65,0.0);
  S4_PT_1->SetBinContent(66,340.913749269);
  S4_PT_1->SetBinContent(67,340.913749269);
  S4_PT_1->SetBinContent(68,340.913749269);
  S4_PT_1->SetBinContent(69,340.913749269);
  S4_PT_1->SetBinContent(70,340.913749269);
  S4_PT_1->SetBinContent(71,0.0);
  S4_PT_1->SetBinContent(72,0.0);
  S4_PT_1->SetBinContent(73,0.0);
  S4_PT_1->SetBinContent(74,0.0);
  S4_PT_1->SetBinContent(75,0.0);
  S4_PT_1->SetBinContent(76,340.913749269);
  S4_PT_1->SetBinContent(77,0.0);
  S4_PT_1->SetBinContent(78,0.0);
  S4_PT_1->SetBinContent(79,0.0);
  S4_PT_1->SetBinContent(80,0.0);
  S4_PT_1->SetBinContent(81,0.0);
  S4_PT_1->SetBinContent(82,0.0);
  S4_PT_1->SetBinContent(83,0.0);
  S4_PT_1->SetBinContent(84,0.0);
  S4_PT_1->SetBinContent(85,0.0);
  S4_PT_1->SetBinContent(86,0.0);
  S4_PT_1->SetBinContent(87,0.0);
  S4_PT_1->SetBinContent(88,0.0);
  S4_PT_1->SetBinContent(89,0.0);
  S4_PT_1->SetBinContent(90,0.0);
  S4_PT_1->SetBinContent(91,0.0);
  S4_PT_1->SetBinContent(92,0.0);
  S4_PT_1->SetBinContent(93,0.0);
  S4_PT_1->SetBinContent(94,0.0);
  S4_PT_1->SetBinContent(95,0.0);
  S4_PT_1->SetBinContent(96,0.0);
  S4_PT_1->SetBinContent(97,0.0);
  S4_PT_1->SetBinContent(98,0.0);
  S4_PT_1->SetBinContent(99,0.0);
  S4_PT_1->SetBinContent(100,0.0);
  S4_PT_1->SetBinContent(101,0.0); // overflow
  S4_PT_1->SetEntries(999);
  // Style
  S4_PT_1->SetLineColor(46);
  S4_PT_1->SetLineStyle(1);
  S4_PT_1->SetLineWidth(1);
  S4_PT_1->SetFillColor(46);
  S4_PT_1->SetFillStyle(1001);

  // Creating a new TH1F
  TH1F* S4_PT_2 = new TH1F("S4_PT_2","S4_PT_2",100,0.0,1000.0);
  // Content
  S4_PT_2->SetBinContent(0,0.0); // underflow
  S4_PT_2->SetBinContent(1,0.0);
  S4_PT_2->SetBinContent(2,0.0);
  S4_PT_2->SetBinContent(3,11806.7683753);
  S4_PT_2->SetBinContent(4,8323.73344462);
  S4_PT_2->SetBinContent(5,6312.10606219);
  S4_PT_2->SetBinContent(6,4926.00248772);
  S4_PT_2->SetBinContent(7,4336.01866885);
  S4_PT_2->SetBinContent(8,3881.09240851);
  S4_PT_2->SetBinContent(9,3376.40816345);
  S4_PT_2->SetBinContent(10,3248.46020273);
  S4_PT_2->SetBinContent(11,2885.94071402);
  S4_PT_2->SetBinContent(12,2267.52490387);
  S4_PT_2->SetBinContent(13,1961.87099771);
  S4_PT_2->SetBinContent(14,1762.84065881);
  S4_PT_2->SetBinContent(15,1457.18675265);
  S4_PT_2->SetBinContent(16,1478.5115461);
  S4_PT_2->SetBinContent(17,1158.6412443);
  S4_PT_2->SetBinContent(18,1371.88797883);
  S4_PT_2->SetBinContent(19,1030.69288358);
  S4_PT_2->SetBinContent(20,902.744922858);
  S4_PT_2->SetBinContent(21,817.446149045);
  S4_PT_2->SetBinContent(22,632.632205783);
  S4_PT_2->SetBinContent(23,526.009038516);
  S4_PT_2->SetBinContent(24,661.065397054);
  S4_PT_2->SetBinContent(25,561.549827605);
  S4_PT_2->SetBinContent(26,561.549827605);
  S4_PT_2->SetBinContent(27,398.060757796);
  S4_PT_2->SetBinContent(28,312.762023982);
  S4_PT_2->SetBinContent(29,369.627846525);
  S4_PT_2->SetBinContent(30,355.411410889);
  S4_PT_2->SetBinContent(31,241.679765805);
  S4_PT_2->SetBinContent(32,369.627846525);
  S4_PT_2->SetBinContent(33,234.571527987);
  S4_PT_2->SetBinContent(34,170.597467627);
  S4_PT_2->SetBinContent(35,206.138616716);
  S4_PT_2->SetBinContent(36,255.89620144);
  S4_PT_2->SetBinContent(37,106.623407267);
  S4_PT_2->SetBinContent(38,156.381031991);
  S4_PT_2->SetBinContent(39,120.839882902);
  S4_PT_2->SetBinContent(40,92.4069716312);
  S4_PT_2->SetBinContent(41,99.5152094489);
  S4_PT_2->SetBinContent(42,120.839882902);
  S4_PT_2->SetBinContent(43,92.4069716312);
  S4_PT_2->SetBinContent(44,78.1904959956);
  S4_PT_2->SetBinContent(45,63.97406036);
  S4_PT_2->SetBinContent(46,49.7575847245);
  S4_PT_2->SetBinContent(47,42.6493869067);
  S4_PT_2->SetBinContent(48,56.8658225423);
  S4_PT_2->SetBinContent(49,78.1904959956);
  S4_PT_2->SetBinContent(50,63.97406036);
  S4_PT_2->SetBinContent(51,49.7575847245);
  S4_PT_2->SetBinContent(52,35.5411410889);
  S4_PT_2->SetBinContent(53,71.0822981778);
  S4_PT_2->SetBinContent(54,21.3246854533);
  S4_PT_2->SetBinContent(55,21.3246854533);
  S4_PT_2->SetBinContent(56,71.0822981778);
  S4_PT_2->SetBinContent(57,14.2164556356);
  S4_PT_2->SetBinContent(58,42.6493869067);
  S4_PT_2->SetBinContent(59,14.2164556356);
  S4_PT_2->SetBinContent(60,28.4329112711);
  S4_PT_2->SetBinContent(61,7.10822981778);
  S4_PT_2->SetBinContent(62,7.10822981778);
  S4_PT_2->SetBinContent(63,14.2164556356);
  S4_PT_2->SetBinContent(64,14.2164556356);
  S4_PT_2->SetBinContent(65,14.2164556356);
  S4_PT_2->SetBinContent(66,14.2164556356);
  S4_PT_2->SetBinContent(67,21.3246854533);
  S4_PT_2->SetBinContent(68,14.2164556356);
  S4_PT_2->SetBinContent(69,21.3246854533);
  S4_PT_2->SetBinContent(70,21.3246854533);
  S4_PT_2->SetBinContent(71,0.0);
  S4_PT_2->SetBinContent(72,7.10822981778);
  S4_PT_2->SetBinContent(73,21.3246854533);
  S4_PT_2->SetBinContent(74,14.2164556356);
  S4_PT_2->SetBinContent(75,0.0);
  S4_PT_2->SetBinContent(76,0.0);
  S4_PT_2->SetBinContent(77,14.2164556356);
  S4_PT_2->SetBinContent(78,7.10822981778);
  S4_PT_2->SetBinContent(79,7.10822981778);
  S4_PT_2->SetBinContent(80,0.0);
  S4_PT_2->SetBinContent(81,7.10822981778);
  S4_PT_2->SetBinContent(82,14.2164556356);
  S4_PT_2->SetBinContent(83,14.2164556356);
  S4_PT_2->SetBinContent(84,0.0);
  S4_PT_2->SetBinContent(85,0.0);
  S4_PT_2->SetBinContent(86,0.0);
  S4_PT_2->SetBinContent(87,0.0);
  S4_PT_2->SetBinContent(88,7.10822981778);
  S4_PT_2->SetBinContent(89,7.10822981778);
  S4_PT_2->SetBinContent(90,14.2164556356);
  S4_PT_2->SetBinContent(91,7.10822981778);
  S4_PT_2->SetBinContent(92,0.0);
  S4_PT_2->SetBinContent(93,0.0);
  S4_PT_2->SetBinContent(94,0.0);
  S4_PT_2->SetBinContent(95,0.0);
  S4_PT_2->SetBinContent(96,0.0);
  S4_PT_2->SetBinContent(97,0.0);
  S4_PT_2->SetBinContent(98,0.0);
  S4_PT_2->SetBinContent(99,0.0);
  S4_PT_2->SetBinContent(100,0.0);
  S4_PT_2->SetBinContent(101,28.4329112711); // overflow
  S4_PT_2->SetEntries(9999);
  // Style
  S4_PT_2->SetLineColor(8);
  S4_PT_2->SetLineStyle(1);
  S4_PT_2->SetLineWidth(1);
  S4_PT_2->SetFillColor(8);
  S4_PT_2->SetFillStyle(1001);

  // Creating a new TH1F
  TH1F* S4_PT_3 = new TH1F("S4_PT_3","S4_PT_3",100,0.0,1000.0);
  // Content
  S4_PT_3->SetBinContent(0,0.0); // underflow
  S4_PT_3->SetBinContent(1,0.0);
  S4_PT_3->SetBinContent(2,0.0);
  S4_PT_3->SetBinContent(3,1595.26459645);
  S4_PT_3->SetBinContent(4,985.773168569);
  S4_PT_3->SetBinContent(5,733.964674421);
  S4_PT_3->SetBinContent(6,585.168618788);
  S4_PT_3->SetBinContent(7,457.833771179);
  S4_PT_3->SetBinContent(8,384.866463897);
  S4_PT_3->SetBinContent(9,334.790925174);
  S4_PT_3->SetBinContent(10,291.868989126);
  S4_PT_3->SetBinContent(11,221.047842647);
  S4_PT_3->SetBinContent(12,214.60956024);
  S4_PT_3->SetBinContent(13,203.163715961);
  S4_PT_3->SetBinContent(14,153.088137238);
  S4_PT_3->SetBinContent(15,134.488650284);
  S4_PT_3->SetBinContent(16,132.342569481);
  S4_PT_3->SetBinContent(17,110.881601457);
  S4_PT_3->SetBinContent(18,84.4131115611);
  S4_PT_3->SetBinContent(19,65.0982243395);
  S4_PT_3->SetBinContent(20,58.6599419323);
  S4_PT_3->SetBinContent(21,50.0755787227);
  S4_PT_3->SetBinContent(22,41.4911755131);
  S4_PT_3->SetBinContent(23,30.0453392336);
  S4_PT_3->SetBinContent(24,35.7682613733);
  S4_PT_3->SetBinContent(25,27.1838781637);
  S4_PT_3->SetBinContent(26,22.1763202915);
  S4_PT_3->SetBinContent(27,18.5994949541);
  S4_PT_3->SetBinContent(28,22.1763202915);
  S4_PT_3->SetBinContent(29,16.4533981517);
  S4_PT_3->SetBinContent(30,12.8765728144);
  S4_PT_3->SetBinContent(31,15.0226696168);
  S4_PT_3->SetBinContent(32,15.7380338843);
  S4_PT_3->SetBinContent(33,7.15365067467);
  S4_PT_3->SetBinContent(34,11.4458442795);
  S4_PT_3->SetBinContent(35,7.15365067467);
  S4_PT_3->SetBinContent(36,10.730476012);
  S4_PT_3->SetBinContent(37,8.5843832096);
  S4_PT_3->SetBinContent(38,4.2921896048);
  S4_PT_3->SetBinContent(39,3.57682613733);
  S4_PT_3->SetBinContent(40,2.86146066987);
  S4_PT_3->SetBinContent(41,3.57682613733);
  S4_PT_3->SetBinContent(42,5.00755787227);
  S4_PT_3->SetBinContent(43,3.57682613733);
  S4_PT_3->SetBinContent(44,2.1460956024);
  S4_PT_3->SetBinContent(45,3.57682613733);
  S4_PT_3->SetBinContent(46,0.715365067467);
  S4_PT_3->SetBinContent(47,2.1460956024);
  S4_PT_3->SetBinContent(48,1.43073053493);
  S4_PT_3->SetBinContent(49,1.43073053493);
  S4_PT_3->SetBinContent(50,1.43073053493);
  S4_PT_3->SetBinContent(51,1.43073053493);
  S4_PT_3->SetBinContent(52,2.1460956024);
  S4_PT_3->SetBinContent(53,1.43073053493);
  S4_PT_3->SetBinContent(54,2.1460956024);
  S4_PT_3->SetBinContent(55,0.715365067467);
  S4_PT_3->SetBinContent(56,0.715365067467);
  S4_PT_3->SetBinContent(57,0.0);
  S4_PT_3->SetBinContent(58,0.0);
  S4_PT_3->SetBinContent(59,0.0);
  S4_PT_3->SetBinContent(60,0.715365067467);
  S4_PT_3->SetBinContent(61,0.0);
  S4_PT_3->SetBinContent(62,0.0);
  S4_PT_3->SetBinContent(63,0.0);
  S4_PT_3->SetBinContent(64,1.43073053493);
  S4_PT_3->SetBinContent(65,0.715365067467);
  S4_PT_3->SetBinContent(66,0.715365067467);
  S4_PT_3->SetBinContent(67,0.0);
  S4_PT_3->SetBinContent(68,0.715365067467);
  S4_PT_3->SetBinContent(69,0.0);
  S4_PT_3->SetBinContent(70,0.715365067467);
  S4_PT_3->SetBinContent(71,0.0);
  S4_PT_3->SetBinContent(72,0.0);
  S4_PT_3->SetBinContent(73,0.0);
  S4_PT_3->SetBinContent(74,0.0);
  S4_PT_3->SetBinContent(75,0.0);
  S4_PT_3->SetBinContent(76,0.715365067467);
  S4_PT_3->SetBinContent(77,0.715365067467);
  S4_PT_3->SetBinContent(78,0.0);
  S4_PT_3->SetBinContent(79,0.0);
  S4_PT_3->SetBinContent(80,0.0);
  S4_PT_3->SetBinContent(81,0.0);
  S4_PT_3->SetBinContent(82,0.0);
  S4_PT_3->SetBinContent(83,0.715365067467);
  S4_PT_3->SetBinContent(84,0.0);
  S4_PT_3->SetBinContent(85,0.0);
  S4_PT_3->SetBinContent(86,0.0);
  S4_PT_3->SetBinContent(87,0.0);
  S4_PT_3->SetBinContent(88,0.0);
  S4_PT_3->SetBinContent(89,0.0);
  S4_PT_3->SetBinContent(90,0.0);
  S4_PT_3->SetBinContent(91,0.0);
  S4_PT_3->SetBinContent(92,0.0);
  S4_PT_3->SetBinContent(93,0.0);
  S4_PT_3->SetBinContent(94,0.0);
  S4_PT_3->SetBinContent(95,0.0);
  S4_PT_3->SetBinContent(96,0.0);
  S4_PT_3->SetBinContent(97,0.715365067467);
  S4_PT_3->SetBinContent(98,0.0);
  S4_PT_3->SetBinContent(99,0.0);
  S4_PT_3->SetBinContent(100,0.0);
  S4_PT_3->SetBinContent(101,0.715365067467); // overflow
  S4_PT_3->SetEntries(9999);
  // Style
  S4_PT_3->SetLineColor(4);
  S4_PT_3->SetLineStyle(1);
  S4_PT_3->SetLineWidth(1);
  S4_PT_3->SetFillColor(4);
  S4_PT_3->SetFillStyle(1001);

  // Creating a new THStack
  THStack* stack = new THStack("mystack_8","mystack");
  stack->Add(S4_PT_0);
  stack->Add(S4_PT_1);
  stack->Add(S4_PT_2);
  stack->Add(S4_PT_3);
  stack->Draw("");

  // Y axis
  stack->GetYaxis()->SetLabelSize(0.04);
  stack->GetYaxis()->SetLabelOffset(0.005);
  stack->GetYaxis()->SetTitleSize(0.06);
  stack->GetYaxis()->SetTitleFont(22);
  stack->GetYaxis()->SetTitleOffset(1);
  stack->GetYaxis()->SetTitle("Events  ( L_{int} = 40.0 fb^{-1} )");

  // X axis
  stack->GetXaxis()->SetLabelSize(0.04);
  stack->GetXaxis()->SetLabelOffset(0.005);
  stack->GetXaxis()->SetTitleSize(0.06);
  stack->GetXaxis()->SetTitleFont(22);
  stack->GetXaxis()->SetTitleOffset(1);
  stack->GetXaxis()->SetTitle("p_{T} [ j_{2} ]   ( GeV ) ");

  // Finalizing the TCanvas
  canvas->SetLogx(0);
  canvas->SetLogy(0);

  // Creating a TLegend
  TLegend* legend = new TLegend(.73,.5,.97,.95);
  legend->AddEntry(S4_PT_0,"signal1MeV");
  legend->AddEntry(S4_PT_1,"signal100GeV1TeV");
  legend->AddEntry(S4_PT_2,"signal100GeV1p5TeV");
  legend->AddEntry(S4_PT_3,"signal100GeV4TeV");
  legend->SetFillColor(0);
  legend->SetTextSize(0.05);
  legend->SetTextFont(22);
  legend->SetY1(TMath::Max(0.15,0.97-0.10*legend->GetListOfPrimitives()->GetSize()));
  legend->Draw();

  // Saving the image
  canvas->SaveAs("../../HTML/MadAnalysis5job_0/selection_3.png");
  canvas->SaveAs("../../PDF/MadAnalysis5job_0/selection_3.png");
  canvas->SaveAs("../../DVI/MadAnalysis5job_0/selection_3.eps");

}
