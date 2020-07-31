void selection_9()
{

  // ROOT version
  Int_t root_version = gROOT->GetVersionInt();

  // Creating a new TCanvas
  TCanvas* canvas = new TCanvas("canvas_plotflow_tempo19","canvas_plotflow_tempo19",0,0,1000,500);
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
  TH1F* S10_THT_0 = new TH1F("S10_THT_0","S10_THT_0",80,0.0,4000.0);
  // Content
  S10_THT_0->SetBinContent(0,0.0); // underflow
  S10_THT_0->SetBinContent(1,2481.65014775);
  S10_THT_0->SetBinContent(2,47204.5499588);
  S10_THT_0->SetBinContent(3,47204.5499588);
  S10_THT_0->SetBinContent(4,36624.2128929);
  S10_THT_0->SetBinContent(5,35810.339271);
  S10_THT_0->SetBinContent(6,32554.8527909);
  S10_THT_0->SetBinContent(7,25636.949025);
  S10_THT_0->SetBinContent(8,29299.3703143);
  S10_THT_0->SetBinContent(9,21160.6541139);
  S10_THT_0->SetBinContent(10,19125.9760647);
  S10_THT_0->SetBinContent(11,17498.2328246);
  S10_THT_0->SetBinContent(12,14242.750348);
  S10_THT_0->SetBinContent(13,13428.8767262);
  S10_THT_0->SetBinContent(14,10987.2638679);
  S10_THT_0->SetBinContent(15,6510.96895673);
  S10_THT_0->SetBinContent(16,7324.84257858);
  S10_THT_0->SetBinContent(17,7324.84257858);
  S10_THT_0->SetBinContent(18,7324.84257858);
  S10_THT_0->SetBinContent(19,3662.42128929);
  S10_THT_0->SetBinContent(20,4476.29090753);
  S10_THT_0->SetBinContent(21,3662.42128929);
  S10_THT_0->SetBinContent(22,2441.6140594);
  S10_THT_0->SetBinContent(23,2848.54966925);
  S10_THT_0->SetBinContent(24,1627.74283972);
  S10_THT_0->SetBinContent(25,1220.80722988);
  S10_THT_0->SetBinContent(26,2034.67844956);
  S10_THT_0->SetBinContent(27,406.935609841);
  S10_THT_0->SetBinContent(28,406.935609841);
  S10_THT_0->SetBinContent(29,0.0);
  S10_THT_0->SetBinContent(30,406.935609841);
  S10_THT_0->SetBinContent(31,0.0);
  S10_THT_0->SetBinContent(32,0.0);
  S10_THT_0->SetBinContent(33,0.0);
  S10_THT_0->SetBinContent(34,0.0);
  S10_THT_0->SetBinContent(35,406.935609841);
  S10_THT_0->SetBinContent(36,0.0);
  S10_THT_0->SetBinContent(37,0.0);
  S10_THT_0->SetBinContent(38,406.935609841);
  S10_THT_0->SetBinContent(39,406.935609841);
  S10_THT_0->SetBinContent(40,406.935609841);
  S10_THT_0->SetBinContent(41,0.0);
  S10_THT_0->SetBinContent(42,0.0);
  S10_THT_0->SetBinContent(43,0.0);
  S10_THT_0->SetBinContent(44,0.0);
  S10_THT_0->SetBinContent(45,0.0);
  S10_THT_0->SetBinContent(46,0.0);
  S10_THT_0->SetBinContent(47,0.0);
  S10_THT_0->SetBinContent(48,0.0);
  S10_THT_0->SetBinContent(49,0.0);
  S10_THT_0->SetBinContent(50,0.0);
  S10_THT_0->SetBinContent(51,0.0);
  S10_THT_0->SetBinContent(52,0.0);
  S10_THT_0->SetBinContent(53,0.0);
  S10_THT_0->SetBinContent(54,0.0);
  S10_THT_0->SetBinContent(55,0.0);
  S10_THT_0->SetBinContent(56,0.0);
  S10_THT_0->SetBinContent(57,0.0);
  S10_THT_0->SetBinContent(58,0.0);
  S10_THT_0->SetBinContent(59,0.0);
  S10_THT_0->SetBinContent(60,0.0);
  S10_THT_0->SetBinContent(61,0.0);
  S10_THT_0->SetBinContent(62,0.0);
  S10_THT_0->SetBinContent(63,0.0);
  S10_THT_0->SetBinContent(64,0.0);
  S10_THT_0->SetBinContent(65,0.0);
  S10_THT_0->SetBinContent(66,0.0);
  S10_THT_0->SetBinContent(67,0.0);
  S10_THT_0->SetBinContent(68,0.0);
  S10_THT_0->SetBinContent(69,0.0);
  S10_THT_0->SetBinContent(70,0.0);
  S10_THT_0->SetBinContent(71,0.0);
  S10_THT_0->SetBinContent(72,0.0);
  S10_THT_0->SetBinContent(73,0.0);
  S10_THT_0->SetBinContent(74,0.0);
  S10_THT_0->SetBinContent(75,0.0);
  S10_THT_0->SetBinContent(76,0.0);
  S10_THT_0->SetBinContent(77,0.0);
  S10_THT_0->SetBinContent(78,0.0);
  S10_THT_0->SetBinContent(79,0.0);
  S10_THT_0->SetBinContent(80,0.0);
  S10_THT_0->SetBinContent(81,0.0); // overflow
  S10_THT_0->SetEntries(1000);
  // Style
  S10_THT_0->SetLineColor(9);
  S10_THT_0->SetLineStyle(1);
  S10_THT_0->SetLineWidth(1);
  S10_THT_0->SetFillColor(9);
  S10_THT_0->SetFillStyle(1001);

  // Creating a new TH1F
  TH1F* S10_THT_1 = new TH1F("S10_THT_1","S10_THT_1",80,0.0,4000.0);
  // Content
  S10_THT_1->SetBinContent(0,0.0); // underflow
  S10_THT_1->SetBinContent(1,1746.10994152);
  S10_THT_1->SetBinContent(2,22861.3990337);
  S10_THT_1->SetBinContent(3,23543.8295129);
  S10_THT_1->SetBinContent(4,30368.1303014);
  S10_THT_1->SetBinContent(5,29685.6998222);
  S10_THT_1->SetBinContent(6,26273.5514297);
  S10_THT_1->SetBinContent(7,27297.1951467);
  S10_THT_1->SetBinContent(8,19449.2506413);
  S10_THT_1->SetBinContent(9,25591.1209505);
  S10_THT_1->SetBinContent(10,16719.532728);
  S10_THT_1->SetBinContent(11,17401.9632072);
  S10_THT_1->SetBinContent(12,15354.6717696);
  S10_THT_1->SetBinContent(13,12624.9538563);
  S10_THT_1->SetBinContent(14,10236.4491809);
  S10_THT_1->SetBinContent(15,7165.51402628);
  S10_THT_1->SetBinContent(16,8530.37498468);
  S10_THT_1->SetBinContent(17,6824.29678492);
  S10_THT_1->SetBinContent(18,6483.08354708);
  S10_THT_1->SetBinContent(19,4777.00935086);
  S10_THT_1->SetBinContent(20,4094.57887166);
  S10_THT_1->SetBinContent(21,3753.36443276);
  S10_THT_1->SetBinContent(22,3070.93435392);
  S10_THT_1->SetBinContent(23,3753.36443276);
  S10_THT_1->SetBinContent(24,2388.50467543);
  S10_THT_1->SetBinContent(25,2729.71951467);
  S10_THT_1->SetBinContent(26,682.429678492);
  S10_THT_1->SetBinContent(27,341.214919316);
  S10_THT_1->SetBinContent(28,1364.85975734);
  S10_THT_1->SetBinContent(29,682.429678492);
  S10_THT_1->SetBinContent(30,682.429678492);
  S10_THT_1->SetBinContent(31,682.429678492);
  S10_THT_1->SetBinContent(32,1023.64491809);
  S10_THT_1->SetBinContent(33,341.214919316);
  S10_THT_1->SetBinContent(34,682.429678492);
  S10_THT_1->SetBinContent(35,341.214919316);
  S10_THT_1->SetBinContent(36,0.0);
  S10_THT_1->SetBinContent(37,341.214919316);
  S10_THT_1->SetBinContent(38,341.214919316);
  S10_THT_1->SetBinContent(39,0.0);
  S10_THT_1->SetBinContent(40,0.0);
  S10_THT_1->SetBinContent(41,341.214919316);
  S10_THT_1->SetBinContent(42,0.0);
  S10_THT_1->SetBinContent(43,0.0);
  S10_THT_1->SetBinContent(44,0.0);
  S10_THT_1->SetBinContent(45,341.214919316);
  S10_THT_1->SetBinContent(46,0.0);
  S10_THT_1->SetBinContent(47,0.0);
  S10_THT_1->SetBinContent(48,0.0);
  S10_THT_1->SetBinContent(49,0.0);
  S10_THT_1->SetBinContent(50,0.0);
  S10_THT_1->SetBinContent(51,0.0);
  S10_THT_1->SetBinContent(52,0.0);
  S10_THT_1->SetBinContent(53,0.0);
  S10_THT_1->SetBinContent(54,0.0);
  S10_THT_1->SetBinContent(55,0.0);
  S10_THT_1->SetBinContent(56,0.0);
  S10_THT_1->SetBinContent(57,0.0);
  S10_THT_1->SetBinContent(58,0.0);
  S10_THT_1->SetBinContent(59,0.0);
  S10_THT_1->SetBinContent(60,0.0);
  S10_THT_1->SetBinContent(61,0.0);
  S10_THT_1->SetBinContent(62,0.0);
  S10_THT_1->SetBinContent(63,0.0);
  S10_THT_1->SetBinContent(64,0.0);
  S10_THT_1->SetBinContent(65,0.0);
  S10_THT_1->SetBinContent(66,0.0);
  S10_THT_1->SetBinContent(67,0.0);
  S10_THT_1->SetBinContent(68,0.0);
  S10_THT_1->SetBinContent(69,0.0);
  S10_THT_1->SetBinContent(70,0.0);
  S10_THT_1->SetBinContent(71,0.0);
  S10_THT_1->SetBinContent(72,0.0);
  S10_THT_1->SetBinContent(73,0.0);
  S10_THT_1->SetBinContent(74,0.0);
  S10_THT_1->SetBinContent(75,0.0);
  S10_THT_1->SetBinContent(76,0.0);
  S10_THT_1->SetBinContent(77,0.0);
  S10_THT_1->SetBinContent(78,0.0);
  S10_THT_1->SetBinContent(79,0.0);
  S10_THT_1->SetBinContent(80,0.0);
  S10_THT_1->SetBinContent(81,0.0); // overflow
  S10_THT_1->SetEntries(1000);
  // Style
  S10_THT_1->SetLineColor(46);
  S10_THT_1->SetLineStyle(1);
  S10_THT_1->SetLineWidth(1);
  S10_THT_1->SetFillColor(46);
  S10_THT_1->SetFillStyle(1001);

  // Creating a new TH1F
  TH1F* S10_THT_2 = new TH1F("S10_THT_2","S10_THT_2",80,0.0,4000.0);
  // Content
  S10_THT_2->SetBinContent(0,0.0); // underflow
  S10_THT_2->SetBinContent(1,729.07128429);
  S10_THT_2->SetBinContent(2,9269.53483939);
  S10_THT_2->SetBinContent(3,9475.6837983);
  S10_THT_2->SetBinContent(4,7776.74196496);
  S10_THT_2->SetBinContent(5,6952.1501295);
  S10_THT_2->SetBinContent(6,5992.49642446);
  S10_THT_2->SetBinContent(7,5324.2953855);
  S10_THT_2->SetBinContent(8,3980.78179851);
  S10_THT_2->SetBinContent(9,3497.40119155);
  S10_THT_2->SetBinContent(10,2758.11306325);
  S10_THT_2->SetBinContent(11,2523.5312687);
  S10_THT_2->SetBinContent(12,2160.99591348);
  S10_THT_2->SetBinContent(13,1684.72361544);
  S10_THT_2->SetBinContent(14,1606.52981726);
  S10_THT_2->SetBinContent(15,1194.23469956);
  S10_THT_2->SetBinContent(16,980.97823177);
  S10_THT_2->SetBinContent(17,881.458706808);
  S10_THT_2->SetBinContent(18,653.985621186);
  S10_THT_2->SetBinContent(19,490.489315894);
  S10_THT_2->SetBinContent(20,504.706333743);
  S10_THT_2->SetBinContent(21,454.946571262);
  S10_THT_2->SetBinContent(22,326.992810593);
  S10_THT_2->SetBinContent(23,284.341557036);
  S10_THT_2->SetBinContent(24,298.558654889);
  S10_THT_2->SetBinContent(25,199.039089926);
  S10_THT_2->SetBinContent(26,199.039089926);
  S10_THT_2->SetBinContent(27,113.736622815);
  S10_THT_2->SetBinContent(28,106.628073888);
  S10_THT_2->SetBinContent(29,85.3024671109);
  S10_THT_2->SetBinContent(30,78.1939181846);
  S10_THT_2->SetBinContent(31,106.628073888);
  S10_THT_2->SetBinContent(32,35.5426966296);
  S10_THT_2->SetBinContent(33,14.2170778518);
  S10_THT_2->SetBinContent(34,49.759762481);
  S10_THT_2->SetBinContent(35,49.759762481);
  S10_THT_2->SetBinContent(36,63.9768603336);
  S10_THT_2->SetBinContent(37,42.6512535563);
  S10_THT_2->SetBinContent(38,35.5426966296);
  S10_THT_2->SetBinContent(39,28.4341557036);
  S10_THT_2->SetBinContent(40,0.0);
  S10_THT_2->SetBinContent(41,7.108540926);
  S10_THT_2->SetBinContent(42,14.2170778518);
  S10_THT_2->SetBinContent(43,7.108540926);
  S10_THT_2->SetBinContent(44,0.0);
  S10_THT_2->SetBinContent(45,0.0);
  S10_THT_2->SetBinContent(46,0.0);
  S10_THT_2->SetBinContent(47,7.108540926);
  S10_THT_2->SetBinContent(48,0.0);
  S10_THT_2->SetBinContent(49,0.0);
  S10_THT_2->SetBinContent(50,14.2170778518);
  S10_THT_2->SetBinContent(51,0.0);
  S10_THT_2->SetBinContent(52,7.108540926);
  S10_THT_2->SetBinContent(53,7.108540926);
  S10_THT_2->SetBinContent(54,0.0);
  S10_THT_2->SetBinContent(55,0.0);
  S10_THT_2->SetBinContent(56,0.0);
  S10_THT_2->SetBinContent(57,0.0);
  S10_THT_2->SetBinContent(58,0.0);
  S10_THT_2->SetBinContent(59,0.0);
  S10_THT_2->SetBinContent(60,0.0);
  S10_THT_2->SetBinContent(61,7.108540926);
  S10_THT_2->SetBinContent(62,0.0);
  S10_THT_2->SetBinContent(63,0.0);
  S10_THT_2->SetBinContent(64,0.0);
  S10_THT_2->SetBinContent(65,0.0);
  S10_THT_2->SetBinContent(66,0.0);
  S10_THT_2->SetBinContent(67,0.0);
  S10_THT_2->SetBinContent(68,0.0);
  S10_THT_2->SetBinContent(69,0.0);
  S10_THT_2->SetBinContent(70,0.0);
  S10_THT_2->SetBinContent(71,0.0);
  S10_THT_2->SetBinContent(72,0.0);
  S10_THT_2->SetBinContent(73,0.0);
  S10_THT_2->SetBinContent(74,0.0);
  S10_THT_2->SetBinContent(75,0.0);
  S10_THT_2->SetBinContent(76,0.0);
  S10_THT_2->SetBinContent(77,0.0);
  S10_THT_2->SetBinContent(78,0.0);
  S10_THT_2->SetBinContent(79,0.0);
  S10_THT_2->SetBinContent(80,0.0);
  S10_THT_2->SetBinContent(81,0.0); // overflow
  S10_THT_2->SetEntries(10000);
  // Style
  S10_THT_2->SetLineColor(8);
  S10_THT_2->SetLineStyle(1);
  S10_THT_2->SetLineWidth(1);
  S10_THT_2->SetFillColor(8);
  S10_THT_2->SetFillStyle(1001);

  // Creating a new TH1F
  TH1F* S10_THT_3 = new TH1F("S10_THT_3","S10_THT_3",80,0.0,4000.0);
  // Content
  S10_THT_3->SetBinContent(0,0.0); // underflow
  S10_THT_3->SetBinContent(1,105.533423737);
  S10_THT_3->SetBinContent(2,1274.1958288);
  S10_THT_3->SetBinContent(3,1180.52600232);
  S10_THT_3->SetBinContent(4,923.112497605);
  S10_THT_3->SetBinContent(5,763.65925102);
  S10_THT_3->SetBinContent(6,619.221915487);
  S10_THT_3->SetBinContent(7,486.940203239);
  S10_THT_3->SetBinContent(8,373.964273949);
  S10_THT_3->SetBinContent(9,303.890662081);
  S10_THT_3->SetBinContent(10,235.247154115);
  S10_THT_3->SetBinContent(11,178.759229452);
  S10_THT_3->SetBinContent(12,149.44271918);
  S10_THT_3->SetBinContent(13,115.120945206);
  S10_THT_3->SetBinContent(14,93.6698264773);
  S10_THT_3->SetBinContent(15,69.3585799079);
  S10_THT_3->SetBinContent(16,64.3533162057);
  S10_THT_3->SetBinContent(17,40.7571015963);
  S10_THT_3->SetBinContent(18,23.5962186075);
  S10_THT_3->SetBinContent(19,28.6014743134);
  S10_THT_3->SetBinContent(20,24.3112545658);
  S10_THT_3->SetBinContent(21,22.8811786511);
  S10_THT_3->SetBinContent(22,15.015775114);
  S10_THT_3->SetBinContent(23,13.5856991994);
  S10_THT_3->SetBinContent(24,9.29547945173);
  S10_THT_3->SetBinContent(25,9.29547945173);
  S10_THT_3->SetBinContent(26,5.00525970407);
  S10_THT_3->SetBinContent(27,4.29021974766);
  S10_THT_3->SetBinContent(28,3.57518458904);
  S10_THT_3->SetBinContent(29,4.29021974766);
  S10_THT_3->SetBinContent(30,0.0);
  S10_THT_3->SetBinContent(31,2.14511067346);
  S10_THT_3->SetBinContent(32,3.57518458904);
  S10_THT_3->SetBinContent(33,0.715036757882);
  S10_THT_3->SetBinContent(34,1.43007391558);
  S10_THT_3->SetBinContent(35,0.0);
  S10_THT_3->SetBinContent(36,0.715036757882);
  S10_THT_3->SetBinContent(37,0.715036757882);
  S10_THT_3->SetBinContent(38,0.715036757882);
  S10_THT_3->SetBinContent(39,0.0);
  S10_THT_3->SetBinContent(40,0.0);
  S10_THT_3->SetBinContent(41,0.0);
  S10_THT_3->SetBinContent(42,0.715036757882);
  S10_THT_3->SetBinContent(43,0.715036757882);
  S10_THT_3->SetBinContent(44,0.0);
  S10_THT_3->SetBinContent(45,0.0);
  S10_THT_3->SetBinContent(46,0.0);
  S10_THT_3->SetBinContent(47,0.0);
  S10_THT_3->SetBinContent(48,0.715036757882);
  S10_THT_3->SetBinContent(49,0.0);
  S10_THT_3->SetBinContent(50,0.0);
  S10_THT_3->SetBinContent(51,0.0);
  S10_THT_3->SetBinContent(52,0.0);
  S10_THT_3->SetBinContent(53,0.0);
  S10_THT_3->SetBinContent(54,0.0);
  S10_THT_3->SetBinContent(55,0.0);
  S10_THT_3->SetBinContent(56,0.0);
  S10_THT_3->SetBinContent(57,0.0);
  S10_THT_3->SetBinContent(58,0.0);
  S10_THT_3->SetBinContent(59,0.0);
  S10_THT_3->SetBinContent(60,0.0);
  S10_THT_3->SetBinContent(61,0.0);
  S10_THT_3->SetBinContent(62,0.0);
  S10_THT_3->SetBinContent(63,0.0);
  S10_THT_3->SetBinContent(64,0.0);
  S10_THT_3->SetBinContent(65,0.0);
  S10_THT_3->SetBinContent(66,0.0);
  S10_THT_3->SetBinContent(67,0.0);
  S10_THT_3->SetBinContent(68,0.0);
  S10_THT_3->SetBinContent(69,0.0);
  S10_THT_3->SetBinContent(70,0.0);
  S10_THT_3->SetBinContent(71,0.0);
  S10_THT_3->SetBinContent(72,0.0);
  S10_THT_3->SetBinContent(73,0.0);
  S10_THT_3->SetBinContent(74,0.0);
  S10_THT_3->SetBinContent(75,0.0);
  S10_THT_3->SetBinContent(76,0.0);
  S10_THT_3->SetBinContent(77,0.0);
  S10_THT_3->SetBinContent(78,0.0);
  S10_THT_3->SetBinContent(79,0.0);
  S10_THT_3->SetBinContent(80,0.0);
  S10_THT_3->SetBinContent(81,0.0); // overflow
  S10_THT_3->SetEntries(10000);
  // Style
  S10_THT_3->SetLineColor(4);
  S10_THT_3->SetLineStyle(1);
  S10_THT_3->SetLineWidth(1);
  S10_THT_3->SetFillColor(4);
  S10_THT_3->SetFillStyle(1001);

  // Creating a new THStack
  THStack* stack = new THStack("mystack_20","mystack");
  stack->Add(S10_THT_0);
  stack->Add(S10_THT_1);
  stack->Add(S10_THT_2);
  stack->Add(S10_THT_3);
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
  stack->GetXaxis()->SetTitle("THT");

  // Finalizing the TCanvas
  canvas->SetLogx(0);
  canvas->SetLogy(0);

  // Creating a TLegend
  TLegend* legend = new TLegend(.73,.5,.97,.95);
  legend->AddEntry(S10_THT_0,"signal1MeV");
  legend->AddEntry(S10_THT_1,"signal100GeV1TeV");
  legend->AddEntry(S10_THT_2,"signal100GeV1p5TeV");
  legend->AddEntry(S10_THT_3,"signal100GeV4TeV");
  legend->SetFillColor(0);
  legend->SetTextSize(0.05);
  legend->SetTextFont(22);
  legend->SetY1(TMath::Max(0.15,0.97-0.10*legend->GetListOfPrimitives()->GetSize()));
  legend->Draw();

  // Saving the image
  canvas->SaveAs("../../HTML/MadAnalysis5job_0/selection_9.png");
  canvas->SaveAs("../../PDF/MadAnalysis5job_0/selection_9.png");
  canvas->SaveAs("../../DVI/MadAnalysis5job_0/selection_9.eps");

}
