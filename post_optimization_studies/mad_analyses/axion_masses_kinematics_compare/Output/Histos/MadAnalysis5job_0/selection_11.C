void selection_11()
{

  // ROOT version
  Int_t root_version = gROOT->GetVersionInt();

  // Creating a new TCanvas
  TCanvas* canvas = new TCanvas("canvas_plotflow_tempo23","canvas_plotflow_tempo23",0,0,1000,500);
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
  TH1F* S12_TET_0 = new TH1F("S12_TET_0","S12_TET_0",80,0.0,8000.0);
  // Content
  S12_TET_0->SetBinContent(0,0.0); // underflow
  S12_TET_0->SetBinContent(1,14689.7202763);
  S12_TET_0->SetBinContent(2,61854.231035);
  S12_TET_0->SetBinContent(3,43135.1990217);
  S12_TET_0->SetBinContent(4,45169.8729331);
  S12_TET_0->SetBinContent(5,39879.6927383);
  S12_TET_0->SetBinContent(6,30520.172728);
  S12_TET_0->SetBinContent(7,29299.3683812);
  S12_TET_0->SetBinContent(8,34996.4673438);
  S12_TET_0->SetBinContent(9,13835.8106225);
  S12_TET_0->SetBinContent(10,19939.848371);
  S12_TET_0->SetBinContent(11,13428.8758402);
  S12_TET_0->SetBinContent(12,12208.0714934);
  S12_TET_0->SetBinContent(13,11801.1327075);
  S12_TET_0->SetBinContent(14,7324.8420953);
  S12_TET_0->SetBinContent(15,8545.65044572);
  S12_TET_0->SetBinContent(16,4476.29061219);
  S12_TET_0->SetBinContent(17,2441.61389831);
  S12_TET_0->SetBinContent(18,4476.29061219);
  S12_TET_0->SetBinContent(19,813.871165985);
  S12_TET_0->SetBinContent(20,1220.80714934);
  S12_TET_0->SetBinContent(21,1627.74273233);
  S12_TET_0->SetBinContent(22,2034.67831532);
  S12_TET_0->SetBinContent(23,1220.80714934);
  S12_TET_0->SetBinContent(24,0.0);
  S12_TET_0->SetBinContent(25,406.935582992);
  S12_TET_0->SetBinContent(26,0.0);
  S12_TET_0->SetBinContent(27,0.0);
  S12_TET_0->SetBinContent(28,0.0);
  S12_TET_0->SetBinContent(29,406.935582992);
  S12_TET_0->SetBinContent(30,0.0);
  S12_TET_0->SetBinContent(31,0.0);
  S12_TET_0->SetBinContent(32,0.0);
  S12_TET_0->SetBinContent(33,0.0);
  S12_TET_0->SetBinContent(34,406.935582992);
  S12_TET_0->SetBinContent(35,0.0);
  S12_TET_0->SetBinContent(36,0.0);
  S12_TET_0->SetBinContent(37,0.0);
  S12_TET_0->SetBinContent(38,0.0);
  S12_TET_0->SetBinContent(39,0.0);
  S12_TET_0->SetBinContent(40,406.935582992);
  S12_TET_0->SetBinContent(41,0.0);
  S12_TET_0->SetBinContent(42,0.0);
  S12_TET_0->SetBinContent(43,0.0);
  S12_TET_0->SetBinContent(44,0.0);
  S12_TET_0->SetBinContent(45,0.0);
  S12_TET_0->SetBinContent(46,0.0);
  S12_TET_0->SetBinContent(47,0.0);
  S12_TET_0->SetBinContent(48,0.0);
  S12_TET_0->SetBinContent(49,0.0);
  S12_TET_0->SetBinContent(50,0.0);
  S12_TET_0->SetBinContent(51,0.0);
  S12_TET_0->SetBinContent(52,0.0);
  S12_TET_0->SetBinContent(53,0.0);
  S12_TET_0->SetBinContent(54,0.0);
  S12_TET_0->SetBinContent(55,0.0);
  S12_TET_0->SetBinContent(56,0.0);
  S12_TET_0->SetBinContent(57,0.0);
  S12_TET_0->SetBinContent(58,0.0);
  S12_TET_0->SetBinContent(59,0.0);
  S12_TET_0->SetBinContent(60,0.0);
  S12_TET_0->SetBinContent(61,0.0);
  S12_TET_0->SetBinContent(62,0.0);
  S12_TET_0->SetBinContent(63,0.0);
  S12_TET_0->SetBinContent(64,0.0);
  S12_TET_0->SetBinContent(65,0.0);
  S12_TET_0->SetBinContent(66,0.0);
  S12_TET_0->SetBinContent(67,0.0);
  S12_TET_0->SetBinContent(68,0.0);
  S12_TET_0->SetBinContent(69,0.0);
  S12_TET_0->SetBinContent(70,0.0);
  S12_TET_0->SetBinContent(71,0.0);
  S12_TET_0->SetBinContent(72,0.0);
  S12_TET_0->SetBinContent(73,0.0);
  S12_TET_0->SetBinContent(74,0.0);
  S12_TET_0->SetBinContent(75,0.0);
  S12_TET_0->SetBinContent(76,0.0);
  S12_TET_0->SetBinContent(77,0.0);
  S12_TET_0->SetBinContent(78,0.0);
  S12_TET_0->SetBinContent(79,0.0);
  S12_TET_0->SetBinContent(80,0.0);
  S12_TET_0->SetBinContent(81,0.0); // overflow
  S12_TET_0->SetEntries(1000);
  // Style
  S12_TET_0->SetLineColor(9);
  S12_TET_0->SetLineStyle(1);
  S12_TET_0->SetLineWidth(1);
  S12_TET_0->SetFillColor(9);
  S12_TET_0->SetFillStyle(1001);

  // Creating a new TH1F
  TH1F* S12_TET_1 = new TH1F("S12_TET_1","S12_TET_1",80,0.0,8000.0);
  // Content
  S12_TET_1->SetBinContent(0,0.0); // underflow
  S12_TET_1->SetBinContent(1,3793.39976523);
  S12_TET_1->SetBinContent(2,28662.0560109);
  S12_TET_1->SetBinContent(3,34462.7090597);
  S12_TET_1->SetBinContent(4,32074.2043921);
  S12_TET_1->SetBinContent(5,33780.2785827);
  S12_TET_1->SetBinContent(6,34462.7090597);
  S12_TET_1->SetBinContent(7,26955.9818203);
  S12_TET_1->SetBinContent(8,26273.5513433);
  S12_TET_1->SetBinContent(9,23885.0466757);
  S12_TET_1->SetBinContent(10,14672.2412422);
  S12_TET_1->SetBinContent(11,13989.8107652);
  S12_TET_1->SetBinContent(12,11260.0928609);
  S12_TET_1->SetBinContent(13,10918.8796242);
  S12_TET_1->SetBinContent(14,7847.94447968);
  S12_TET_1->SetBinContent(15,6824.29676248);
  S12_TET_1->SetBinContent(16,5118.22257186);
  S12_TET_1->SetBinContent(17,4777.00933515);
  S12_TET_1->SetBinContent(18,3753.36442042);
  S12_TET_1->SetBinContent(19,3070.93434382);
  S12_TET_1->SetBinContent(20,2047.2894291);
  S12_TET_1->SetBinContent(21,2729.7195057);
  S12_TET_1->SetBinContent(22,1023.64491472);
  S12_TET_1->SetBinContent(23,682.429676248);
  S12_TET_1->SetBinContent(24,3070.93434382);
  S12_TET_1->SetBinContent(25,341.214918195);
  S12_TET_1->SetBinContent(26,1023.64491472);
  S12_TET_1->SetBinContent(27,341.214918195);
  S12_TET_1->SetBinContent(28,1023.64491472);
  S12_TET_1->SetBinContent(29,341.214918195);
  S12_TET_1->SetBinContent(30,0.0);
  S12_TET_1->SetBinContent(31,341.214918195);
  S12_TET_1->SetBinContent(32,0.0);
  S12_TET_1->SetBinContent(33,682.429676248);
  S12_TET_1->SetBinContent(34,0.0);
  S12_TET_1->SetBinContent(35,0.0);
  S12_TET_1->SetBinContent(36,341.214918195);
  S12_TET_1->SetBinContent(37,0.0);
  S12_TET_1->SetBinContent(38,0.0);
  S12_TET_1->SetBinContent(39,341.214918195);
  S12_TET_1->SetBinContent(40,0.0);
  S12_TET_1->SetBinContent(41,0.0);
  S12_TET_1->SetBinContent(42,0.0);
  S12_TET_1->SetBinContent(43,0.0);
  S12_TET_1->SetBinContent(44,0.0);
  S12_TET_1->SetBinContent(45,0.0);
  S12_TET_1->SetBinContent(46,0.0);
  S12_TET_1->SetBinContent(47,0.0);
  S12_TET_1->SetBinContent(48,0.0);
  S12_TET_1->SetBinContent(49,0.0);
  S12_TET_1->SetBinContent(50,0.0);
  S12_TET_1->SetBinContent(51,0.0);
  S12_TET_1->SetBinContent(52,0.0);
  S12_TET_1->SetBinContent(53,0.0);
  S12_TET_1->SetBinContent(54,0.0);
  S12_TET_1->SetBinContent(55,0.0);
  S12_TET_1->SetBinContent(56,0.0);
  S12_TET_1->SetBinContent(57,0.0);
  S12_TET_1->SetBinContent(58,0.0);
  S12_TET_1->SetBinContent(59,0.0);
  S12_TET_1->SetBinContent(60,0.0);
  S12_TET_1->SetBinContent(61,0.0);
  S12_TET_1->SetBinContent(62,0.0);
  S12_TET_1->SetBinContent(63,0.0);
  S12_TET_1->SetBinContent(64,0.0);
  S12_TET_1->SetBinContent(65,0.0);
  S12_TET_1->SetBinContent(66,0.0);
  S12_TET_1->SetBinContent(67,0.0);
  S12_TET_1->SetBinContent(68,0.0);
  S12_TET_1->SetBinContent(69,0.0);
  S12_TET_1->SetBinContent(70,0.0);
  S12_TET_1->SetBinContent(71,0.0);
  S12_TET_1->SetBinContent(72,0.0);
  S12_TET_1->SetBinContent(73,0.0);
  S12_TET_1->SetBinContent(74,0.0);
  S12_TET_1->SetBinContent(75,0.0);
  S12_TET_1->SetBinContent(76,0.0);
  S12_TET_1->SetBinContent(77,0.0);
  S12_TET_1->SetBinContent(78,0.0);
  S12_TET_1->SetBinContent(79,0.0);
  S12_TET_1->SetBinContent(80,0.0);
  S12_TET_1->SetBinContent(81,0.0); // overflow
  S12_TET_1->SetEntries(1000);
  // Style
  S12_TET_1->SetLineColor(46);
  S12_TET_1->SetLineStyle(1);
  S12_TET_1->SetLineWidth(1);
  S12_TET_1->SetFillColor(46);
  S12_TET_1->SetFillStyle(1001);

  // Creating a new TH1F
  TH1F* S12_TET_2 = new TH1F("S12_TET_2","S12_TET_2",80,0.0,8000.0);
  // Content
  S12_TET_2->SetBinContent(0,0.0); // underflow
  S12_TET_2->SetBinContent(1,2236.08139601);
  S12_TET_2->SetBinContent(2,11217.2745793);
  S12_TET_2->SetBinContent(3,10378.4661937);
  S12_TET_2->SetBinContent(4,8267.23061324);
  S12_TET_2->SetBinContent(5,7584.80901138);
  S12_TET_2->SetBinContent(6,5885.87131541);
  S12_TET_2->SetBinContent(7,5061.27954654);
  S12_TET_2->SetBinContent(8,4023.43452723);
  S12_TET_2->SetBinContent(9,2914.50082427);
  S12_TET_2->SetBinContent(10,2623.05058183);
  S12_TET_2->SetBinContent(11,2082.8019471);
  S12_TET_2->SetBinContent(12,1713.15791281);
  S12_TET_2->SetBinContent(13,1421.70767037);
  S12_TET_2->SetBinContent(14,1009.41258597);
  S12_TET_2->SetBinContent(15,988.08686091);
  S12_TET_2->SetBinContent(16,675.311293433);
  S12_TET_2->SetBinContent(17,533.140326388);
  S12_TET_2->SetBinContent(18,390.969599352);
  S12_TET_2->SetBinContent(19,334.101292537);
  S12_TET_2->SetBinContent(20,334.101292537);
  S12_TET_2->SetBinContent(21,284.341534074);
  S12_TET_2->SetBinContent(22,191.9305255);
  S12_TET_2->SetBinContent(23,199.039073852);
  S12_TET_2->SetBinContent(24,156.387863742);
  S12_TET_2->SetBinContent(25,142.170767037);
  S12_TET_2->SetBinContent(26,113.73661363);
  S12_TET_2->SetBinContent(27,49.7597584626);
  S12_TET_2->SetBinContent(28,42.651250112);
  S12_TET_2->SetBinContent(29,35.5426937594);
  S12_TET_2->SetBinContent(30,28.4341534074);
  S12_TET_2->SetBinContent(31,21.3256170557);
  S12_TET_2->SetBinContent(32,35.5426937594);
  S12_TET_2->SetBinContent(33,21.3256170557);
  S12_TET_2->SetBinContent(34,14.2170767037);
  S12_TET_2->SetBinContent(35,14.2170767037);
  S12_TET_2->SetBinContent(36,21.3256170557);
  S12_TET_2->SetBinContent(37,0.0);
  S12_TET_2->SetBinContent(38,7.10854035195);
  S12_TET_2->SetBinContent(39,0.0);
  S12_TET_2->SetBinContent(40,7.10854035195);
  S12_TET_2->SetBinContent(41,0.0);
  S12_TET_2->SetBinContent(42,0.0);
  S12_TET_2->SetBinContent(43,0.0);
  S12_TET_2->SetBinContent(44,0.0);
  S12_TET_2->SetBinContent(45,0.0);
  S12_TET_2->SetBinContent(46,0.0);
  S12_TET_2->SetBinContent(47,0.0);
  S12_TET_2->SetBinContent(48,0.0);
  S12_TET_2->SetBinContent(49,14.2170767037);
  S12_TET_2->SetBinContent(50,0.0);
  S12_TET_2->SetBinContent(51,0.0);
  S12_TET_2->SetBinContent(52,7.10854035195);
  S12_TET_2->SetBinContent(53,0.0);
  S12_TET_2->SetBinContent(54,0.0);
  S12_TET_2->SetBinContent(55,0.0);
  S12_TET_2->SetBinContent(56,0.0);
  S12_TET_2->SetBinContent(57,0.0);
  S12_TET_2->SetBinContent(58,0.0);
  S12_TET_2->SetBinContent(59,0.0);
  S12_TET_2->SetBinContent(60,0.0);
  S12_TET_2->SetBinContent(61,0.0);
  S12_TET_2->SetBinContent(62,0.0);
  S12_TET_2->SetBinContent(63,0.0);
  S12_TET_2->SetBinContent(64,0.0);
  S12_TET_2->SetBinContent(65,0.0);
  S12_TET_2->SetBinContent(66,0.0);
  S12_TET_2->SetBinContent(67,0.0);
  S12_TET_2->SetBinContent(68,0.0);
  S12_TET_2->SetBinContent(69,0.0);
  S12_TET_2->SetBinContent(70,0.0);
  S12_TET_2->SetBinContent(71,0.0);
  S12_TET_2->SetBinContent(72,0.0);
  S12_TET_2->SetBinContent(73,0.0);
  S12_TET_2->SetBinContent(74,0.0);
  S12_TET_2->SetBinContent(75,0.0);
  S12_TET_2->SetBinContent(76,0.0);
  S12_TET_2->SetBinContent(77,0.0);
  S12_TET_2->SetBinContent(78,0.0);
  S12_TET_2->SetBinContent(79,0.0);
  S12_TET_2->SetBinContent(80,0.0);
  S12_TET_2->SetBinContent(81,0.0); // overflow
  S12_TET_2->SetEntries(10000);
  // Style
  S12_TET_2->SetLineColor(8);
  S12_TET_2->SetLineStyle(1);
  S12_TET_2->SetLineWidth(1);
  S12_TET_2->SetFillColor(8);
  S12_TET_2->SetFillStyle(1001);

  // Creating a new TH1F
  TH1F* S12_TET_3 = new TH1F("S12_TET_3","S12_TET_3",80,0.0,8000.0);
  // Content
  S12_TET_3->SetBinContent(0,0.0); // underflow
  S12_TET_3->SetBinContent(1,320.759524674);
  S12_TET_3->SetBinContent(2,1477.98114439);
  S12_TET_3->SetBinContent(3,1255.60476433);
  S12_TET_3->SetBinContent(4,938.843285465);
  S12_TET_3->SetBinContent(5,751.503631558);
  S12_TET_3->SetBinContent(6,573.459713032);
  S12_TET_3->SetBinContent(7,424.017073055);
  S12_TET_3->SetBinContent(8,341.787637576);
  S12_TET_3->SetBinContent(9,248.117810622);
  S12_TET_3->SetBinContent(10,173.753966634);
  S12_TET_3->SetBinContent(11,142.292360322);
  S12_TET_3->SetBinContent(12,112.975809919);
  S12_TET_3->SetBinContent(13,79.369107716);
  S12_TET_3->SetBinContent(14,78.6540757523);
  S12_TET_3->SetBinContent(15,52.1976931864);
  S12_TET_3->SetBinContent(16,37.181917996);
  S12_TET_3->SetBinContent(17,30.0315503808);
  S12_TET_3->SetBinContent(18,19.3059949599);
  S12_TET_3->SetBinContent(19,16.4458471142);
  S12_TET_3->SetBinContent(20,16.4458471142);
  S12_TET_3->SetBinContent(21,12.8706633066);
  S12_TET_3->SetBinContent(22,16.4458471142);
  S12_TET_3->SetBinContent(23,6.4353316533);
  S12_TET_3->SetBinContent(24,6.4353316533);
  S12_TET_3->SetBinContent(25,5.72029569141);
  S12_TET_3->SetBinContent(26,3.57518460722);
  S12_TET_3->SetBinContent(27,2.86014744589);
  S12_TET_3->SetBinContent(28,1.43007392285);
  S12_TET_3->SetBinContent(29,2.14511068437);
  S12_TET_3->SetBinContent(30,0.715036761518);
  S12_TET_3->SetBinContent(31,1.43007392285);
  S12_TET_3->SetBinContent(32,0.0);
  S12_TET_3->SetBinContent(33,0.0);
  S12_TET_3->SetBinContent(34,0.0);
  S12_TET_3->SetBinContent(35,1.43007392285);
  S12_TET_3->SetBinContent(36,0.715036761518);
  S12_TET_3->SetBinContent(37,0.0);
  S12_TET_3->SetBinContent(38,0.0);
  S12_TET_3->SetBinContent(39,0.0);
  S12_TET_3->SetBinContent(40,0.0);
  S12_TET_3->SetBinContent(41,0.0);
  S12_TET_3->SetBinContent(42,0.715036761518);
  S12_TET_3->SetBinContent(43,0.0);
  S12_TET_3->SetBinContent(44,0.0);
  S12_TET_3->SetBinContent(45,0.0);
  S12_TET_3->SetBinContent(46,0.0);
  S12_TET_3->SetBinContent(47,0.0);
  S12_TET_3->SetBinContent(48,0.0);
  S12_TET_3->SetBinContent(49,0.0);
  S12_TET_3->SetBinContent(50,0.0);
  S12_TET_3->SetBinContent(51,0.0);
  S12_TET_3->SetBinContent(52,0.0);
  S12_TET_3->SetBinContent(53,0.0);
  S12_TET_3->SetBinContent(54,0.0);
  S12_TET_3->SetBinContent(55,0.0);
  S12_TET_3->SetBinContent(56,0.0);
  S12_TET_3->SetBinContent(57,0.0);
  S12_TET_3->SetBinContent(58,0.0);
  S12_TET_3->SetBinContent(59,0.0);
  S12_TET_3->SetBinContent(60,0.0);
  S12_TET_3->SetBinContent(61,0.0);
  S12_TET_3->SetBinContent(62,0.0);
  S12_TET_3->SetBinContent(63,0.0);
  S12_TET_3->SetBinContent(64,0.0);
  S12_TET_3->SetBinContent(65,0.0);
  S12_TET_3->SetBinContent(66,0.0);
  S12_TET_3->SetBinContent(67,0.0);
  S12_TET_3->SetBinContent(68,0.0);
  S12_TET_3->SetBinContent(69,0.0);
  S12_TET_3->SetBinContent(70,0.0);
  S12_TET_3->SetBinContent(71,0.0);
  S12_TET_3->SetBinContent(72,0.0);
  S12_TET_3->SetBinContent(73,0.0);
  S12_TET_3->SetBinContent(74,0.0);
  S12_TET_3->SetBinContent(75,0.0);
  S12_TET_3->SetBinContent(76,0.0);
  S12_TET_3->SetBinContent(77,0.0);
  S12_TET_3->SetBinContent(78,0.0);
  S12_TET_3->SetBinContent(79,0.0);
  S12_TET_3->SetBinContent(80,0.0);
  S12_TET_3->SetBinContent(81,0.0); // overflow
  S12_TET_3->SetEntries(10000);
  // Style
  S12_TET_3->SetLineColor(4);
  S12_TET_3->SetLineStyle(1);
  S12_TET_3->SetLineWidth(1);
  S12_TET_3->SetFillColor(4);
  S12_TET_3->SetFillStyle(1001);

  // Creating a new THStack
  THStack* stack = new THStack("mystack_24","mystack");
  stack->Add(S12_TET_0);
  stack->Add(S12_TET_1);
  stack->Add(S12_TET_2);
  stack->Add(S12_TET_3);
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
  stack->GetXaxis()->SetTitle("TET");

  // Finalizing the TCanvas
  canvas->SetLogx(0);
  canvas->SetLogy(0);

  // Creating a TLegend
  TLegend* legend = new TLegend(.73,.5,.97,.95);
  legend->AddEntry(S12_TET_0,"signal1MeV");
  legend->AddEntry(S12_TET_1,"signal100GeV1TeV");
  legend->AddEntry(S12_TET_2,"signal100GeV1p5TeV");
  legend->AddEntry(S12_TET_3,"signal100GeV4TeV");
  legend->SetFillColor(0);
  legend->SetTextSize(0.05);
  legend->SetTextFont(22);
  legend->SetY1(TMath::Max(0.15,0.97-0.10*legend->GetListOfPrimitives()->GetSize()));
  legend->Draw();

  // Saving the image
  canvas->SaveAs("../../HTML/MadAnalysis5job_0/selection_11.png");
  canvas->SaveAs("../../PDF/MadAnalysis5job_0/selection_11.png");
  canvas->SaveAs("../../DVI/MadAnalysis5job_0/selection_11.eps");

}
