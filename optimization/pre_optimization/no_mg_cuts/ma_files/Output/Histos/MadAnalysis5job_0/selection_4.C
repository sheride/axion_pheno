void selection_4()
{

  // ROOT version
  Int_t root_version = gROOT->GetVersionInt();

  // Creating a new TCanvas
  TCanvas* canvas = new TCanvas("canvas_plotflow_tempo9","canvas_plotflow_tempo9",0,0,700,500);
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
  canvas->SetRightMargin(0.05);
  canvas->SetBottomMargin(0.15);
  canvas->SetTopMargin(0.05);

  // Creating a new TH1F
  TH1F* S5_ETA_0 = new TH1F("S5_ETA_0","S5_ETA_0",160,-8.0,8.0);
  // Content
  S5_ETA_0->SetBinContent(0,0.0); // underflow
  S5_ETA_0->SetBinContent(1,0.0);
  S5_ETA_0->SetBinContent(2,0.0);
  S5_ETA_0->SetBinContent(3,0.0);
  S5_ETA_0->SetBinContent(4,0.0);
  S5_ETA_0->SetBinContent(5,0.0);
  S5_ETA_0->SetBinContent(6,0.0);
  S5_ETA_0->SetBinContent(7,0.0);
  S5_ETA_0->SetBinContent(8,0.0);
  S5_ETA_0->SetBinContent(9,0.0);
  S5_ETA_0->SetBinContent(10,0.0);
  S5_ETA_0->SetBinContent(11,0.0);
  S5_ETA_0->SetBinContent(12,0.0);
  S5_ETA_0->SetBinContent(13,0.0);
  S5_ETA_0->SetBinContent(14,0.0);
  S5_ETA_0->SetBinContent(15,0.0);
  S5_ETA_0->SetBinContent(16,0.0);
  S5_ETA_0->SetBinContent(17,0.0);
  S5_ETA_0->SetBinContent(18,0.0);
  S5_ETA_0->SetBinContent(19,0.0);
  S5_ETA_0->SetBinContent(20,0.0);
  S5_ETA_0->SetBinContent(21,0.0);
  S5_ETA_0->SetBinContent(22,0.0);
  S5_ETA_0->SetBinContent(23,0.0);
  S5_ETA_0->SetBinContent(24,0.0);
  S5_ETA_0->SetBinContent(25,0.0);
  S5_ETA_0->SetBinContent(26,0.0);
  S5_ETA_0->SetBinContent(27,0.0);
  S5_ETA_0->SetBinContent(28,0.0);
  S5_ETA_0->SetBinContent(29,0.0);
  S5_ETA_0->SetBinContent(30,0.0);
  S5_ETA_0->SetBinContent(31,0.0);
  S5_ETA_0->SetBinContent(32,0.0);
  S5_ETA_0->SetBinContent(33,3.14401948471);
  S5_ETA_0->SetBinContent(34,12.5760771388);
  S5_ETA_0->SetBinContent(35,3.14401948471);
  S5_ETA_0->SetBinContent(36,6.28804056942);
  S5_ETA_0->SetBinContent(37,22.008137993);
  S5_ETA_0->SetBinContent(38,6.28804056942);
  S5_ETA_0->SetBinContent(39,22.008137993);
  S5_ETA_0->SetBinContent(40,15.7200974235);
  S5_ETA_0->SetBinContent(41,22.008137993);
  S5_ETA_0->SetBinContent(42,31.4401948471);
  S5_ETA_0->SetBinContent(43,22.008137993);
  S5_ETA_0->SetBinContent(44,28.2961785624);
  S5_ETA_0->SetBinContent(45,53.44832484);
  S5_ETA_0->SetBinContent(46,47.1602842706);
  S5_ETA_0->SetBinContent(47,44.0162839859);
  S5_ETA_0->SetBinContent(48,66.0244059789);
  S5_ETA_0->SetBinContent(49,66.0244059789);
  S5_ETA_0->SetBinContent(50,53.44832484);
  S5_ETA_0->SetBinContent(51,69.1684462636);
  S5_ETA_0->SetBinContent(52,103.752649395);
  S5_ETA_0->SetBinContent(53,110.040689965);
  S5_ETA_0->SetBinContent(54,125.760771388);
  S5_ETA_0->SetBinContent(55,176.065095944);
  S5_ETA_0->SetBinContent(56,166.63305509);
  S5_ETA_0->SetBinContent(57,128.904811673);
  S5_ETA_0->SetBinContent(58,257.809623346);
  S5_ETA_0->SetBinContent(59,232.657461068);
  S5_ETA_0->SetBinContent(60,282.961785624);
  S5_ETA_0->SetBinContent(61,298.681867047);
  S5_ETA_0->SetBinContent(62,311.257948186);
  S5_ETA_0->SetBinContent(63,352.130191887);
  S5_ETA_0->SetBinContent(64,330.122069894);
  S5_ETA_0->SetBinContent(65,415.010437582);
  S5_ETA_0->SetBinContent(66,443.306840144);
  S5_ETA_0->SetBinContent(67,559.635650678);
  S5_ETA_0->SetBinContent(68,562.779650963);
  S5_ETA_0->SetBinContent(69,688.540462351);
  S5_ETA_0->SetBinContent(70,694.828462921);
  S5_ETA_0->SetBinContent(71,773.428870038);
  S5_ETA_0->SetBinContent(72,723.124465483);
  S5_ETA_0->SetBinContent(73,751.420868045);
  S5_ETA_0->SetBinContent(74,927.485683989);
  S5_ETA_0->SetBinContent(75,804.868872885);
  S5_ETA_0->SetBinContent(76,952.638086267);
  S5_ETA_0->SetBinContent(77,990.366089683);
  S5_ETA_0->SetBinContent(78,996.654090253);
  S5_ETA_0->SetBinContent(79,1053.24649538);
  S5_ETA_0->SetBinContent(80,1065.82249652);
  S5_ETA_0->SetBinContent(81,1059.53449595);
  S5_ETA_0->SetBinContent(82,905.477681996);
  S5_ETA_0->SetBinContent(83,987.222089398);
  S5_ETA_0->SetBinContent(84,921.19768342);
  S5_ETA_0->SetBinContent(85,848.885276871);
  S5_ETA_0->SetBinContent(86,974.64608826);
  S5_ETA_0->SetBinContent(87,789.148871462);
  S5_ETA_0->SetBinContent(88,817.445274024);
  S5_ETA_0->SetBinContent(89,757.708868615);
  S5_ETA_0->SetBinContent(90,726.268465768);
  S5_ETA_0->SetBinContent(91,738.844466906);
  S5_ETA_0->SetBinContent(92,666.532060358);
  S5_ETA_0->SetBinContent(93,597.363654095);
  S5_ETA_0->SetBinContent(94,534.4832484);
  S5_ETA_0->SetBinContent(95,506.187245838);
  S5_ETA_0->SetBinContent(96,449.594840713);
  S5_ETA_0->SetBinContent(97,314.401948471);
  S5_ETA_0->SetBinContent(98,411.866437297);
  S5_ETA_0->SetBinContent(99,377.282354165);
  S5_ETA_0->SetBinContent(100,245.233542207);
  S5_ETA_0->SetBinContent(101,264.097663916);
  S5_ETA_0->SetBinContent(102,226.369420499);
  S5_ETA_0->SetBinContent(103,157.200974235);
  S5_ETA_0->SetBinContent(104,160.34501452);
  S5_ETA_0->SetBinContent(105,125.760771388);
  S5_ETA_0->SetBinContent(106,103.752649395);
  S5_ETA_0->SetBinContent(107,88.0325679718);
  S5_ETA_0->SetBinContent(108,116.328730534);
  S5_ETA_0->SetBinContent(109,47.1602842706);
  S5_ETA_0->SetBinContent(110,75.456486833);
  S5_ETA_0->SetBinContent(111,88.0325679718);
  S5_ETA_0->SetBinContent(112,62.8804056942);
  S5_ETA_0->SetBinContent(113,72.3124465483);
  S5_ETA_0->SetBinContent(114,50.3043245553);
  S5_ETA_0->SetBinContent(115,47.1602842706);
  S5_ETA_0->SetBinContent(116,28.2961785624);
  S5_ETA_0->SetBinContent(117,37.7282354165);
  S5_ETA_0->SetBinContent(118,37.7282354165);
  S5_ETA_0->SetBinContent(119,18.8641177083);
  S5_ETA_0->SetBinContent(120,31.4401948471);
  S5_ETA_0->SetBinContent(121,18.8641177083);
  S5_ETA_0->SetBinContent(122,12.5760771388);
  S5_ETA_0->SetBinContent(123,3.14401948471);
  S5_ETA_0->SetBinContent(124,15.7200974235);
  S5_ETA_0->SetBinContent(125,9.43206085413);
  S5_ETA_0->SetBinContent(126,9.43206085413);
  S5_ETA_0->SetBinContent(127,12.5760771388);
  S5_ETA_0->SetBinContent(128,6.28804056942);
  S5_ETA_0->SetBinContent(129,6.28804056942);
  S5_ETA_0->SetBinContent(130,0.0);
  S5_ETA_0->SetBinContent(131,0.0);
  S5_ETA_0->SetBinContent(132,0.0);
  S5_ETA_0->SetBinContent(133,0.0);
  S5_ETA_0->SetBinContent(134,0.0);
  S5_ETA_0->SetBinContent(135,0.0);
  S5_ETA_0->SetBinContent(136,0.0);
  S5_ETA_0->SetBinContent(137,0.0);
  S5_ETA_0->SetBinContent(138,0.0);
  S5_ETA_0->SetBinContent(139,0.0);
  S5_ETA_0->SetBinContent(140,0.0);
  S5_ETA_0->SetBinContent(141,0.0);
  S5_ETA_0->SetBinContent(142,0.0);
  S5_ETA_0->SetBinContent(143,0.0);
  S5_ETA_0->SetBinContent(144,0.0);
  S5_ETA_0->SetBinContent(145,0.0);
  S5_ETA_0->SetBinContent(146,0.0);
  S5_ETA_0->SetBinContent(147,0.0);
  S5_ETA_0->SetBinContent(148,0.0);
  S5_ETA_0->SetBinContent(149,0.0);
  S5_ETA_0->SetBinContent(150,0.0);
  S5_ETA_0->SetBinContent(151,0.0);
  S5_ETA_0->SetBinContent(152,0.0);
  S5_ETA_0->SetBinContent(153,0.0);
  S5_ETA_0->SetBinContent(154,0.0);
  S5_ETA_0->SetBinContent(155,0.0);
  S5_ETA_0->SetBinContent(156,0.0);
  S5_ETA_0->SetBinContent(157,0.0);
  S5_ETA_0->SetBinContent(158,0.0);
  S5_ETA_0->SetBinContent(159,0.0);
  S5_ETA_0->SetBinContent(160,0.0);
  S5_ETA_0->SetBinContent(161,0.0); // overflow
  S5_ETA_0->SetEntries(9999);
  // Style
  S5_ETA_0->SetLineColor(9);
  S5_ETA_0->SetLineStyle(1);
  S5_ETA_0->SetLineWidth(1);
  S5_ETA_0->SetFillColor(9);
  S5_ETA_0->SetFillStyle(1001);

  // Creating a new THStack
  THStack* stack = new THStack("mystack_10","mystack");
  stack->Add(S5_ETA_0);
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
  stack->GetXaxis()->SetTitle("#eta [ j_{2} ] ");

  // Finalizing the TCanvas
  canvas->SetLogx(0);
  canvas->SetLogy(0);

  // Saving the image
  canvas->SaveAs("../../HTML/MadAnalysis5job_0/selection_4.png");
  canvas->SaveAs("../../PDF/MadAnalysis5job_0/selection_4.png");
  canvas->SaveAs("../../DVI/MadAnalysis5job_0/selection_4.eps");

}
