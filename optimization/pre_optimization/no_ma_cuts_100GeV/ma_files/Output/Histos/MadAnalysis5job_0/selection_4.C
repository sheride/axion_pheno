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
  S5_ETA_0->SetBinContent(32,681.827329249);
  S5_ETA_0->SetBinContent(33,340.913744625);
  S5_ETA_0->SetBinContent(34,1704.56872312);
  S5_ETA_0->SetBinContent(35,340.913744625);
  S5_ETA_0->SetBinContent(36,681.827329249);
  S5_ETA_0->SetBinContent(37,0.0);
  S5_ETA_0->SetBinContent(38,1363.6550585);
  S5_ETA_0->SetBinContent(39,0.0);
  S5_ETA_0->SetBinContent(40,1022.74139387);
  S5_ETA_0->SetBinContent(41,2386.39645237);
  S5_ETA_0->SetBinContent(42,2386.39645237);
  S5_ETA_0->SetBinContent(43,2727.310117);
  S5_ETA_0->SetBinContent(44,681.827329249);
  S5_ETA_0->SetBinContent(45,2727.310117);
  S5_ETA_0->SetBinContent(46,1363.6550585);
  S5_ETA_0->SetBinContent(47,1363.6550585);
  S5_ETA_0->SetBinContent(48,2386.39645237);
  S5_ETA_0->SetBinContent(49,4431.88084012);
  S5_ETA_0->SetBinContent(50,3750.05151087);
  S5_ETA_0->SetBinContent(51,3750.05151087);
  S5_ETA_0->SetBinContent(52,4431.88084012);
  S5_ETA_0->SetBinContent(53,4772.79290474);
  S5_ETA_0->SetBinContent(54,3409.13744625);
  S5_ETA_0->SetBinContent(55,4090.9647755);
  S5_ETA_0->SetBinContent(56,6818.27329249);
  S5_ETA_0->SetBinContent(57,5795.53309862);
  S5_ETA_0->SetBinContent(58,7500.10142174);
  S5_ETA_0->SetBinContent(59,5454.62103399);
  S5_ETA_0->SetBinContent(60,4090.9647755);
  S5_ETA_0->SetBinContent(61,7841.01748637);
  S5_ETA_0->SetBinContent(62,9204.66974486);
  S5_ETA_0->SetBinContent(63,6818.27329249);
  S5_ETA_0->SetBinContent(64,8522.84561562);
  S5_ETA_0->SetBinContent(65,6136.44916324);
  S5_ETA_0->SetBinContent(66,8181.92955099);
  S5_ETA_0->SetBinContent(67,5113.70496937);
  S5_ETA_0->SetBinContent(68,4772.79290474);
  S5_ETA_0->SetBinContent(69,6818.27329249);
  S5_ETA_0->SetBinContent(70,4431.88084012);
  S5_ETA_0->SetBinContent(71,3409.13744625);
  S5_ETA_0->SetBinContent(72,2727.310117);
  S5_ETA_0->SetBinContent(73,4431.88084012);
  S5_ETA_0->SetBinContent(74,4090.9647755);
  S5_ETA_0->SetBinContent(75,3068.22378162);
  S5_ETA_0->SetBinContent(76,1363.6550585);
  S5_ETA_0->SetBinContent(77,2727.310117);
  S5_ETA_0->SetBinContent(78,681.827329249);
  S5_ETA_0->SetBinContent(79,1022.74139387);
  S5_ETA_0->SetBinContent(80,681.827329249);
  S5_ETA_0->SetBinContent(81,681.827329249);
  S5_ETA_0->SetBinContent(82,1704.56872312);
  S5_ETA_0->SetBinContent(83,340.913744625);
  S5_ETA_0->SetBinContent(84,2045.48238775);
  S5_ETA_0->SetBinContent(85,1704.56872312);
  S5_ETA_0->SetBinContent(86,1022.74139387);
  S5_ETA_0->SetBinContent(87,3409.13744625);
  S5_ETA_0->SetBinContent(88,2386.39645237);
  S5_ETA_0->SetBinContent(89,3750.05151087);
  S5_ETA_0->SetBinContent(90,3409.13744625);
  S5_ETA_0->SetBinContent(91,4431.88084012);
  S5_ETA_0->SetBinContent(92,5113.70496937);
  S5_ETA_0->SetBinContent(93,5454.62103399);
  S5_ETA_0->SetBinContent(94,5113.70496937);
  S5_ETA_0->SetBinContent(95,4772.79290474);
  S5_ETA_0->SetBinContent(96,6477.36122787);
  S5_ETA_0->SetBinContent(97,6136.44916324);
  S5_ETA_0->SetBinContent(98,5113.70496937);
  S5_ETA_0->SetBinContent(99,9545.58580949);
  S5_ETA_0->SetBinContent(100,7841.01748637);
  S5_ETA_0->SetBinContent(101,9545.58580949);
  S5_ETA_0->SetBinContent(102,4090.9647755);
  S5_ETA_0->SetBinContent(103,6477.36122787);
  S5_ETA_0->SetBinContent(104,8863.75768024);
  S5_ETA_0->SetBinContent(105,5113.70496937);
  S5_ETA_0->SetBinContent(106,5454.62103399);
  S5_ETA_0->SetBinContent(107,5454.62103399);
  S5_ETA_0->SetBinContent(108,5113.70496937);
  S5_ETA_0->SetBinContent(109,4772.79290474);
  S5_ETA_0->SetBinContent(110,3750.05151087);
  S5_ETA_0->SetBinContent(111,4090.9647755);
  S5_ETA_0->SetBinContent(112,2727.310117);
  S5_ETA_0->SetBinContent(113,3409.13744625);
  S5_ETA_0->SetBinContent(114,3409.13744625);
  S5_ETA_0->SetBinContent(115,2386.39645237);
  S5_ETA_0->SetBinContent(116,1704.56872312);
  S5_ETA_0->SetBinContent(117,1022.74139387);
  S5_ETA_0->SetBinContent(118,1704.56872312);
  S5_ETA_0->SetBinContent(119,340.913744625);
  S5_ETA_0->SetBinContent(120,1022.74139387);
  S5_ETA_0->SetBinContent(121,681.827329249);
  S5_ETA_0->SetBinContent(122,1363.6550585);
  S5_ETA_0->SetBinContent(123,340.913744625);
  S5_ETA_0->SetBinContent(124,1022.74139387);
  S5_ETA_0->SetBinContent(125,1022.74139387);
  S5_ETA_0->SetBinContent(126,681.827329249);
  S5_ETA_0->SetBinContent(127,340.913744625);
  S5_ETA_0->SetBinContent(128,681.827329249);
  S5_ETA_0->SetBinContent(129,1022.74139387);
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
  S5_ETA_0->SetEntries(999);
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
