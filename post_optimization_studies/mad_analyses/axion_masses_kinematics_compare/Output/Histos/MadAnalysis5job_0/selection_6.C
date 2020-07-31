void selection_6()
{

  // ROOT version
  Int_t root_version = gROOT->GetVersionInt();

  // Creating a new TCanvas
  TCanvas* canvas = new TCanvas("canvas_plotflow_tempo13","canvas_plotflow_tempo13",0,0,1000,500);
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
  TH1F* S7_DELTAR_0 = new TH1F("S7_DELTAR_0","S7_DELTAR_0",75,0.0,15.0);
  // Content
  S7_DELTAR_0->SetBinContent(0,0.0); // underflow
  S7_DELTAR_0->SetBinContent(1,0.0);
  S7_DELTAR_0->SetBinContent(2,0.0);
  S7_DELTAR_0->SetBinContent(3,0.0);
  S7_DELTAR_0->SetBinContent(4,0.0);
  S7_DELTAR_0->SetBinContent(5,0.0);
  S7_DELTAR_0->SetBinContent(6,0.0);
  S7_DELTAR_0->SetBinContent(7,0.0);
  S7_DELTAR_0->SetBinContent(8,0.0);
  S7_DELTAR_0->SetBinContent(9,0.0);
  S7_DELTAR_0->SetBinContent(10,0.0);
  S7_DELTAR_0->SetBinContent(11,0.0);
  S7_DELTAR_0->SetBinContent(12,0.0);
  S7_DELTAR_0->SetBinContent(13,6098.53120721);
  S7_DELTAR_0->SetBinContent(14,15043.0460444);
  S7_DELTAR_0->SetBinContent(15,13823.338203);
  S7_DELTAR_0->SetBinContent(16,23580.9929345);
  S7_DELTAR_0->SetBinContent(17,26426.9725646);
  S7_DELTAR_0->SetBinContent(18,32525.5037718);
  S7_DELTAR_0->SetBinContent(19,38624.038979);
  S7_DELTAR_0->SetBinContent(20,35778.0553489);
  S7_DELTAR_0->SetBinContent(21,41063.4346619);
  S7_DELTAR_0->SetBinContent(22,33338.6436661);
  S7_DELTAR_0->SetBinContent(23,28053.2483532);
  S7_DELTAR_0->SetBinContent(24,18702.1655688);
  S7_DELTAR_0->SetBinContent(25,18702.1655688);
  S7_DELTAR_0->SetBinContent(26,12197.0664144);
  S7_DELTAR_0->SetBinContent(27,11383.9265201);
  S7_DELTAR_0->SetBinContent(28,9351.08278438);
  S7_DELTAR_0->SetBinContent(29,6911.6711015);
  S7_DELTAR_0->SetBinContent(30,6505.09915435);
  S7_DELTAR_0->SetBinContent(31,6098.53120721);
  S7_DELTAR_0->SetBinContent(32,5285.39531291);
  S7_DELTAR_0->SetBinContent(33,3659.11952432);
  S7_DELTAR_0->SetBinContent(34,2439.41288288);
  S7_DELTAR_0->SetBinContent(35,1626.27538859);
  S7_DELTAR_0->SetBinContent(36,2439.41288288);
  S7_DELTAR_0->SetBinContent(37,1219.70664144);
  S7_DELTAR_0->SetBinContent(38,1219.70664144);
  S7_DELTAR_0->SetBinContent(39,813.137494294);
  S7_DELTAR_0->SetBinContent(40,2032.84413574);
  S7_DELTAR_0->SetBinContent(41,813.137494294);
  S7_DELTAR_0->SetBinContent(42,0.0);
  S7_DELTAR_0->SetBinContent(43,0.0);
  S7_DELTAR_0->SetBinContent(44,0.0);
  S7_DELTAR_0->SetBinContent(45,406.568747147);
  S7_DELTAR_0->SetBinContent(46,0.0);
  S7_DELTAR_0->SetBinContent(47,0.0);
  S7_DELTAR_0->SetBinContent(48,0.0);
  S7_DELTAR_0->SetBinContent(49,0.0);
  S7_DELTAR_0->SetBinContent(50,0.0);
  S7_DELTAR_0->SetBinContent(51,0.0);
  S7_DELTAR_0->SetBinContent(52,0.0);
  S7_DELTAR_0->SetBinContent(53,0.0);
  S7_DELTAR_0->SetBinContent(54,0.0);
  S7_DELTAR_0->SetBinContent(55,0.0);
  S7_DELTAR_0->SetBinContent(56,0.0);
  S7_DELTAR_0->SetBinContent(57,0.0);
  S7_DELTAR_0->SetBinContent(58,0.0);
  S7_DELTAR_0->SetBinContent(59,0.0);
  S7_DELTAR_0->SetBinContent(60,0.0);
  S7_DELTAR_0->SetBinContent(61,0.0);
  S7_DELTAR_0->SetBinContent(62,0.0);
  S7_DELTAR_0->SetBinContent(63,0.0);
  S7_DELTAR_0->SetBinContent(64,0.0);
  S7_DELTAR_0->SetBinContent(65,0.0);
  S7_DELTAR_0->SetBinContent(66,0.0);
  S7_DELTAR_0->SetBinContent(67,0.0);
  S7_DELTAR_0->SetBinContent(68,0.0);
  S7_DELTAR_0->SetBinContent(69,0.0);
  S7_DELTAR_0->SetBinContent(70,0.0);
  S7_DELTAR_0->SetBinContent(71,0.0);
  S7_DELTAR_0->SetBinContent(72,0.0);
  S7_DELTAR_0->SetBinContent(73,0.0);
  S7_DELTAR_0->SetBinContent(74,0.0);
  S7_DELTAR_0->SetBinContent(75,0.0);
  S7_DELTAR_0->SetBinContent(76,0.0); // overflow
  S7_DELTAR_0->SetEntries(999);
  // Style
  S7_DELTAR_0->SetLineColor(9);
  S7_DELTAR_0->SetLineStyle(1);
  S7_DELTAR_0->SetLineWidth(1);
  S7_DELTAR_0->SetFillColor(9);
  S7_DELTAR_0->SetFillStyle(1001);

  // Creating a new TH1F
  TH1F* S7_DELTAR_1 = new TH1F("S7_DELTAR_1","S7_DELTAR_1",75,0.0,15.0);
  // Content
  S7_DELTAR_1->SetBinContent(0,0.0); // underflow
  S7_DELTAR_1->SetBinContent(1,0.0);
  S7_DELTAR_1->SetBinContent(2,0.0);
  S7_DELTAR_1->SetBinContent(3,0.0);
  S7_DELTAR_1->SetBinContent(4,0.0);
  S7_DELTAR_1->SetBinContent(5,0.0);
  S7_DELTAR_1->SetBinContent(6,0.0);
  S7_DELTAR_1->SetBinContent(7,0.0);
  S7_DELTAR_1->SetBinContent(8,0.0);
  S7_DELTAR_1->SetBinContent(9,0.0);
  S7_DELTAR_1->SetBinContent(10,0.0);
  S7_DELTAR_1->SetBinContent(11,0.0);
  S7_DELTAR_1->SetBinContent(12,0.0);
  S7_DELTAR_1->SetBinContent(13,8522.84548348);
  S7_DELTAR_1->SetBinContent(14,12954.7222549);
  S7_DELTAR_1->SetBinContent(15,16022.9467889);
  S7_DELTAR_1->SetBinContent(16,22159.3958571);
  S7_DELTAR_1->SetBinContent(17,29659.4971625);
  S7_DELTAR_1->SetBinContent(18,29659.4971625);
  S7_DELTAR_1->SetBinContent(19,35114.118112);
  S7_DELTAR_1->SetBinContent(20,35114.118112);
  S7_DELTAR_1->SetBinContent(21,31364.0654592);
  S7_DELTAR_1->SetBinContent(22,23182.1360351);
  S7_DELTAR_1->SetBinContent(23,15000.2066109);
  S7_DELTAR_1->SetBinContent(24,13295.6383142);
  S7_DELTAR_1->SetBinContent(25,13977.4624329);
  S7_DELTAR_1->SetBinContent(26,8181.92942414);
  S7_DELTAR_1->SetBinContent(27,8181.92942414);
  S7_DELTAR_1->SetBinContent(28,5795.53300877);
  S7_DELTAR_1->SetBinContent(29,5795.53300877);
  S7_DELTAR_1->SetBinContent(30,6818.27318679);
  S7_DELTAR_1->SetBinContent(31,3750.05145273);
  S7_DELTAR_1->SetBinContent(32,2386.39641538);
  S7_DELTAR_1->SetBinContent(33,1363.65503736);
  S7_DELTAR_1->SetBinContent(34,3750.05145273);
  S7_DELTAR_1->SetBinContent(35,2386.39641538);
  S7_DELTAR_1->SetBinContent(36,1022.74137802);
  S7_DELTAR_1->SetBinContent(37,1363.65503736);
  S7_DELTAR_1->SetBinContent(38,2386.39641538);
  S7_DELTAR_1->SetBinContent(39,0.0);
  S7_DELTAR_1->SetBinContent(40,340.913739339);
  S7_DELTAR_1->SetBinContent(41,340.913739339);
  S7_DELTAR_1->SetBinContent(42,681.827318679);
  S7_DELTAR_1->SetBinContent(43,0.0);
  S7_DELTAR_1->SetBinContent(44,0.0);
  S7_DELTAR_1->SetBinContent(45,0.0);
  S7_DELTAR_1->SetBinContent(46,0.0);
  S7_DELTAR_1->SetBinContent(47,0.0);
  S7_DELTAR_1->SetBinContent(48,0.0);
  S7_DELTAR_1->SetBinContent(49,0.0);
  S7_DELTAR_1->SetBinContent(50,0.0);
  S7_DELTAR_1->SetBinContent(51,0.0);
  S7_DELTAR_1->SetBinContent(52,0.0);
  S7_DELTAR_1->SetBinContent(53,0.0);
  S7_DELTAR_1->SetBinContent(54,0.0);
  S7_DELTAR_1->SetBinContent(55,0.0);
  S7_DELTAR_1->SetBinContent(56,0.0);
  S7_DELTAR_1->SetBinContent(57,0.0);
  S7_DELTAR_1->SetBinContent(58,0.0);
  S7_DELTAR_1->SetBinContent(59,0.0);
  S7_DELTAR_1->SetBinContent(60,0.0);
  S7_DELTAR_1->SetBinContent(61,0.0);
  S7_DELTAR_1->SetBinContent(62,0.0);
  S7_DELTAR_1->SetBinContent(63,0.0);
  S7_DELTAR_1->SetBinContent(64,0.0);
  S7_DELTAR_1->SetBinContent(65,0.0);
  S7_DELTAR_1->SetBinContent(66,0.0);
  S7_DELTAR_1->SetBinContent(67,0.0);
  S7_DELTAR_1->SetBinContent(68,0.0);
  S7_DELTAR_1->SetBinContent(69,0.0);
  S7_DELTAR_1->SetBinContent(70,0.0);
  S7_DELTAR_1->SetBinContent(71,0.0);
  S7_DELTAR_1->SetBinContent(72,0.0);
  S7_DELTAR_1->SetBinContent(73,0.0);
  S7_DELTAR_1->SetBinContent(74,0.0);
  S7_DELTAR_1->SetBinContent(75,0.0);
  S7_DELTAR_1->SetBinContent(76,0.0); // overflow
  S7_DELTAR_1->SetEntries(999);
  // Style
  S7_DELTAR_1->SetLineColor(46);
  S7_DELTAR_1->SetLineStyle(1);
  S7_DELTAR_1->SetLineWidth(1);
  S7_DELTAR_1->SetFillColor(46);
  S7_DELTAR_1->SetFillStyle(1001);

  // Creating a new TH1F
  TH1F* S7_DELTAR_2 = new TH1F("S7_DELTAR_2","S7_DELTAR_2",75,0.0,15.0);
  // Content
  S7_DELTAR_2->SetBinContent(0,0.0); // underflow
  S7_DELTAR_2->SetBinContent(1,0.0);
  S7_DELTAR_2->SetBinContent(2,0.0);
  S7_DELTAR_2->SetBinContent(3,0.0);
  S7_DELTAR_2->SetBinContent(4,0.0);
  S7_DELTAR_2->SetBinContent(5,0.0);
  S7_DELTAR_2->SetBinContent(6,0.0);
  S7_DELTAR_2->SetBinContent(7,0.0);
  S7_DELTAR_2->SetBinContent(8,0.0);
  S7_DELTAR_2->SetBinContent(9,0.0);
  S7_DELTAR_2->SetBinContent(10,0.0);
  S7_DELTAR_2->SetBinContent(11,0.0);
  S7_DELTAR_2->SetBinContent(12,0.0);
  S7_DELTAR_2->SetBinContent(13,831.662525678);
  S7_DELTAR_2->SetBinContent(14,1663.32545136);
  S7_DELTAR_2->SetBinContent(15,2388.3644122);
  S7_DELTAR_2->SetBinContent(16,3390.62448161);
  S7_DELTAR_2->SetBinContent(17,4023.25867294);
  S7_DELTAR_2->SetBinContent(18,4407.10254633);
  S7_DELTAR_2->SetBinContent(19,5395.14622042);
  S7_DELTAR_2->SetBinContent(20,5999.34602113);
  S7_DELTAR_2->SetBinContent(21,5615.49814774);
  S7_DELTAR_2->SetBinContent(22,4627.45447364);
  S7_DELTAR_2->SetBinContent(23,3888.20071748);
  S7_DELTAR_2->SetBinContent(24,3610.97960893);
  S7_DELTAR_2->SetBinContent(25,3241.35173085);
  S7_DELTAR_2->SetBinContent(26,3113.40377305);
  S7_DELTAR_2->SetBinContent(27,2686.90991373);
  S7_DELTAR_2->SetBinContent(28,2509.20437234);
  S7_DELTAR_2->SetBinContent(29,1933.43776226);
  S7_DELTAR_2->SetBinContent(30,2025.84493178);
  S7_DELTAR_2->SetBinContent(31,1606.45947011);
  S7_DELTAR_2->SetBinContent(32,1442.97032404);
  S7_DELTAR_2->SetBinContent(33,1208.39880141);
  S7_DELTAR_2->SetBinContent(34,1101.77523658);
  S7_DELTAR_2->SetBinContent(35,739.255756158);
  S7_DELTAR_2->SetBinContent(36,710.822965536);
  S7_DELTAR_2->SetBinContent(37,661.065381949);
  S7_DELTAR_2->SetBinContent(38,469.143045254);
  S7_DELTAR_2->SetBinContent(39,447.818252288);
  S7_DELTAR_2->SetBinContent(40,312.762016836);
  S7_DELTAR_2->SetBinContent(41,248.787957938);
  S7_DELTAR_2->SetBinContent(42,270.112670904);
  S7_DELTAR_2->SetBinContent(43,220.355047316);
  S7_DELTAR_2->SetBinContent(44,78.190494209);
  S7_DELTAR_2->SetBinContent(45,49.7575835876);
  S7_DELTAR_2->SetBinContent(46,78.190494209);
  S7_DELTAR_2->SetBinContent(47,35.5411402768);
  S7_DELTAR_2->SetBinContent(48,21.3246849661);
  S7_DELTAR_2->SetBinContent(49,14.2164553107);
  S7_DELTAR_2->SetBinContent(50,7.10822965536);
  S7_DELTAR_2->SetBinContent(51,0.0);
  S7_DELTAR_2->SetBinContent(52,0.0);
  S7_DELTAR_2->SetBinContent(53,0.0);
  S7_DELTAR_2->SetBinContent(54,0.0);
  S7_DELTAR_2->SetBinContent(55,0.0);
  S7_DELTAR_2->SetBinContent(56,0.0);
  S7_DELTAR_2->SetBinContent(57,0.0);
  S7_DELTAR_2->SetBinContent(58,0.0);
  S7_DELTAR_2->SetBinContent(59,0.0);
  S7_DELTAR_2->SetBinContent(60,0.0);
  S7_DELTAR_2->SetBinContent(61,0.0);
  S7_DELTAR_2->SetBinContent(62,0.0);
  S7_DELTAR_2->SetBinContent(63,0.0);
  S7_DELTAR_2->SetBinContent(64,0.0);
  S7_DELTAR_2->SetBinContent(65,0.0);
  S7_DELTAR_2->SetBinContent(66,0.0);
  S7_DELTAR_2->SetBinContent(67,0.0);
  S7_DELTAR_2->SetBinContent(68,0.0);
  S7_DELTAR_2->SetBinContent(69,0.0);
  S7_DELTAR_2->SetBinContent(70,0.0);
  S7_DELTAR_2->SetBinContent(71,0.0);
  S7_DELTAR_2->SetBinContent(72,0.0);
  S7_DELTAR_2->SetBinContent(73,0.0);
  S7_DELTAR_2->SetBinContent(74,0.0);
  S7_DELTAR_2->SetBinContent(75,0.0);
  S7_DELTAR_2->SetBinContent(76,0.0); // overflow
  S7_DELTAR_2->SetEntries(9999);
  // Style
  S7_DELTAR_2->SetLineColor(8);
  S7_DELTAR_2->SetLineStyle(1);
  S7_DELTAR_2->SetLineWidth(1);
  S7_DELTAR_2->SetFillColor(8);
  S7_DELTAR_2->SetFillStyle(1001);

  // Creating a new TH1F
  TH1F* S7_DELTAR_3 = new TH1F("S7_DELTAR_3","S7_DELTAR_3",75,0.0,15.0);
  // Content
  S7_DELTAR_3->SetBinContent(0,0.0); // underflow
  S7_DELTAR_3->SetBinContent(1,0.0);
  S7_DELTAR_3->SetBinContent(2,0.0);
  S7_DELTAR_3->SetBinContent(3,0.0);
  S7_DELTAR_3->SetBinContent(4,0.0);
  S7_DELTAR_3->SetBinContent(5,0.0);
  S7_DELTAR_3->SetBinContent(6,0.0);
  S7_DELTAR_3->SetBinContent(7,0.0);
  S7_DELTAR_3->SetBinContent(8,0.0);
  S7_DELTAR_3->SetBinContent(9,0.0);
  S7_DELTAR_3->SetBinContent(10,0.0);
  S7_DELTAR_3->SetBinContent(11,0.0);
  S7_DELTAR_3->SetBinContent(12,0.0);
  S7_DELTAR_3->SetBinContent(13,33.6221662556);
  S7_DELTAR_3->SetBinContent(14,76.5440724542);
  S7_DELTAR_3->SetBinContent(15,165.249350065);
  S7_DELTAR_3->SetBinContent(16,234.639779486);
  S7_DELTAR_3->SetBinContent(17,331.929460736);
  S7_DELTAR_3->SetBinContent(18,372.705278025);
  S7_DELTAR_3->SetBinContent(19,463.556596545);
  S7_DELTAR_3->SetBinContent(20,442.810987749);
  S7_DELTAR_3->SetBinContent(21,419.20417774);
  S7_DELTAR_3->SetBinContent(22,468.564198668);
  S7_DELTAR_3->SetBinContent(23,439.234186233);
  S7_DELTAR_3->SetBinContent(24,432.795783503);
  S7_DELTAR_3->SetBinContent(25,379.858921058);
  S7_DELTAR_3->SetBinContent(26,343.375305589);
  S7_DELTAR_3->SetBinContent(27,338.367743466);
  S7_DELTAR_3->SetBinContent(28,329.783379826);
  S7_DELTAR_3->SetBinContent(29,262.539031315);
  S7_DELTAR_3->SetBinContent(30,246.801024642);
  S7_DELTAR_3->SetBinContent(31,226.055415846);
  S7_DELTAR_3->SetBinContent(32,203.879086443);
  S7_DELTAR_3->SetBinContent(33,169.541551885);
  S7_DELTAR_3->SetBinContent(34,145.219141572);
  S7_DELTAR_3->SetBinContent(35,125.904293383);
  S7_DELTAR_3->SetBinContent(36,86.5591967006);
  S7_DELTAR_3->SetBinContent(37,109.450886406);
  S7_DELTAR_3->SetBinContent(38,72.9672709377);
  S7_DELTAR_3->SetBinContent(39,56.5138639615);
  S7_DELTAR_3->SetBinContent(40,39.3450886821);
  S7_DELTAR_3->SetBinContent(41,31.4760693457);
  S7_DELTAR_3->SetBinContent(42,34.3375305589);
  S7_DELTAR_3->SetBinContent(43,21.4609570993);
  S7_DELTAR_3->SetBinContent(44,21.4609570993);
  S7_DELTAR_3->SetBinContent(45,7.86901933641);
  S7_DELTAR_3->SetBinContent(46,6.43828672979);
  S7_DELTAR_3->SetBinContent(47,5.00755812317);
  S7_DELTAR_3->SetBinContent(48,2.14609570993);
  S7_DELTAR_3->SetBinContent(49,2.86146081324);
  S7_DELTAR_3->SetBinContent(50,2.86146081324);
  S7_DELTAR_3->SetBinContent(51,0.0);
  S7_DELTAR_3->SetBinContent(52,0.0);
  S7_DELTAR_3->SetBinContent(53,0.0);
  S7_DELTAR_3->SetBinContent(54,0.0);
  S7_DELTAR_3->SetBinContent(55,0.0);
  S7_DELTAR_3->SetBinContent(56,0.0);
  S7_DELTAR_3->SetBinContent(57,0.0);
  S7_DELTAR_3->SetBinContent(58,0.0);
  S7_DELTAR_3->SetBinContent(59,0.0);
  S7_DELTAR_3->SetBinContent(60,0.0);
  S7_DELTAR_3->SetBinContent(61,0.0);
  S7_DELTAR_3->SetBinContent(62,0.0);
  S7_DELTAR_3->SetBinContent(63,0.0);
  S7_DELTAR_3->SetBinContent(64,0.0);
  S7_DELTAR_3->SetBinContent(65,0.0);
  S7_DELTAR_3->SetBinContent(66,0.0);
  S7_DELTAR_3->SetBinContent(67,0.0);
  S7_DELTAR_3->SetBinContent(68,0.0);
  S7_DELTAR_3->SetBinContent(69,0.0);
  S7_DELTAR_3->SetBinContent(70,0.0);
  S7_DELTAR_3->SetBinContent(71,0.0);
  S7_DELTAR_3->SetBinContent(72,0.0);
  S7_DELTAR_3->SetBinContent(73,0.0);
  S7_DELTAR_3->SetBinContent(74,0.0);
  S7_DELTAR_3->SetBinContent(75,0.0);
  S7_DELTAR_3->SetBinContent(76,0.0); // overflow
  S7_DELTAR_3->SetEntries(9999);
  // Style
  S7_DELTAR_3->SetLineColor(4);
  S7_DELTAR_3->SetLineStyle(1);
  S7_DELTAR_3->SetLineWidth(1);
  S7_DELTAR_3->SetFillColor(4);
  S7_DELTAR_3->SetFillStyle(1001);

  // Creating a new THStack
  THStack* stack = new THStack("mystack_14","mystack");
  stack->Add(S7_DELTAR_0);
  stack->Add(S7_DELTAR_1);
  stack->Add(S7_DELTAR_2);
  stack->Add(S7_DELTAR_3);
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
  stack->GetXaxis()->SetTitle("#DeltaR [ j_{1} , j_{2} ] ");

  // Finalizing the TCanvas
  canvas->SetLogx(0);
  canvas->SetLogy(0);

  // Creating a TLegend
  TLegend* legend = new TLegend(.73,.5,.97,.95);
  legend->AddEntry(S7_DELTAR_0,"signal1MeV");
  legend->AddEntry(S7_DELTAR_1,"signal100GeV1TeV");
  legend->AddEntry(S7_DELTAR_2,"signal100GeV1p5TeV");
  legend->AddEntry(S7_DELTAR_3,"signal100GeV4TeV");
  legend->SetFillColor(0);
  legend->SetTextSize(0.05);
  legend->SetTextFont(22);
  legend->SetY1(TMath::Max(0.15,0.97-0.10*legend->GetListOfPrimitives()->GetSize()));
  legend->Draw();

  // Saving the image
  canvas->SaveAs("../../HTML/MadAnalysis5job_0/selection_6.png");
  canvas->SaveAs("../../PDF/MadAnalysis5job_0/selection_6.png");
  canvas->SaveAs("../../DVI/MadAnalysis5job_0/selection_6.eps");

}
