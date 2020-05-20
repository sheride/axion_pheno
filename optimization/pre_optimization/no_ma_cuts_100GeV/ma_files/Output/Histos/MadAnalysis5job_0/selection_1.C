void selection_1()
{

  // ROOT version
  Int_t root_version = gROOT->GetVersionInt();

  // Creating a new TCanvas
  TCanvas* canvas = new TCanvas("canvas_plotflow_tempo3","canvas_plotflow_tempo3",0,0,700,500);
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
  TH1F* S2_ETA_0 = new TH1F("S2_ETA_0","S2_ETA_0",160,-8.0,8.0);
  // Content
  S2_ETA_0->SetBinContent(0,0.0); // underflow
  S2_ETA_0->SetBinContent(1,0.0);
  S2_ETA_0->SetBinContent(2,0.0);
  S2_ETA_0->SetBinContent(3,0.0);
  S2_ETA_0->SetBinContent(4,0.0);
  S2_ETA_0->SetBinContent(5,0.0);
  S2_ETA_0->SetBinContent(6,0.0);
  S2_ETA_0->SetBinContent(7,0.0);
  S2_ETA_0->SetBinContent(8,0.0);
  S2_ETA_0->SetBinContent(9,0.0);
  S2_ETA_0->SetBinContent(10,0.0);
  S2_ETA_0->SetBinContent(11,0.0);
  S2_ETA_0->SetBinContent(12,0.0);
  S2_ETA_0->SetBinContent(13,0.0);
  S2_ETA_0->SetBinContent(14,0.0);
  S2_ETA_0->SetBinContent(15,0.0);
  S2_ETA_0->SetBinContent(16,0.0);
  S2_ETA_0->SetBinContent(17,0.0);
  S2_ETA_0->SetBinContent(18,0.0);
  S2_ETA_0->SetBinContent(19,0.0);
  S2_ETA_0->SetBinContent(20,0.0);
  S2_ETA_0->SetBinContent(21,0.0);
  S2_ETA_0->SetBinContent(22,0.0);
  S2_ETA_0->SetBinContent(23,0.0);
  S2_ETA_0->SetBinContent(24,0.0);
  S2_ETA_0->SetBinContent(25,0.0);
  S2_ETA_0->SetBinContent(26,0.0);
  S2_ETA_0->SetBinContent(27,0.0);
  S2_ETA_0->SetBinContent(28,0.0);
  S2_ETA_0->SetBinContent(29,0.0);
  S2_ETA_0->SetBinContent(30,0.0);
  S2_ETA_0->SetBinContent(31,340.913741021);
  S2_ETA_0->SetBinContent(32,0.0);
  S2_ETA_0->SetBinContent(33,0.0);
  S2_ETA_0->SetBinContent(34,0.0);
  S2_ETA_0->SetBinContent(35,0.0);
  S2_ETA_0->SetBinContent(36,0.0);
  S2_ETA_0->SetBinContent(37,0.0);
  S2_ETA_0->SetBinContent(38,340.913741021);
  S2_ETA_0->SetBinContent(39,0.0);
  S2_ETA_0->SetBinContent(40,681.827322042);
  S2_ETA_0->SetBinContent(41,681.827322042);
  S2_ETA_0->SetBinContent(42,340.913741021);
  S2_ETA_0->SetBinContent(43,0.0);
  S2_ETA_0->SetBinContent(44,0.0);
  S2_ETA_0->SetBinContent(45,340.913741021);
  S2_ETA_0->SetBinContent(46,681.827322042);
  S2_ETA_0->SetBinContent(47,1022.74138306);
  S2_ETA_0->SetBinContent(48,1022.74138306);
  S2_ETA_0->SetBinContent(49,340.913741021);
  S2_ETA_0->SetBinContent(50,340.913741021);
  S2_ETA_0->SetBinContent(51,2727.31008817);
  S2_ETA_0->SetBinContent(52,2045.48236613);
  S2_ETA_0->SetBinContent(53,2045.48236613);
  S2_ETA_0->SetBinContent(54,3409.13741021);
  S2_ETA_0->SetBinContent(55,3068.22374919);
  S2_ETA_0->SetBinContent(56,3068.22374919);
  S2_ETA_0->SetBinContent(57,2386.39642715);
  S2_ETA_0->SetBinContent(58,3409.13741021);
  S2_ETA_0->SetBinContent(59,3068.22374919);
  S2_ETA_0->SetBinContent(60,4431.88079327);
  S2_ETA_0->SetBinContent(61,7159.18928144);
  S2_ETA_0->SetBinContent(62,7500.10134246);
  S2_ETA_0->SetBinContent(63,8181.9294645);
  S2_ETA_0->SetBinContent(64,9545.58570859);
  S2_ETA_0->SetBinContent(65,5795.53303736);
  S2_ETA_0->SetBinContent(66,7500.10134246);
  S2_ETA_0->SetBinContent(67,6136.44909838);
  S2_ETA_0->SetBinContent(68,8863.75758655);
  S2_ETA_0->SetBinContent(69,7159.18928144);
  S2_ETA_0->SetBinContent(70,8522.84552553);
  S2_ETA_0->SetBinContent(71,7500.10134246);
  S2_ETA_0->SetBinContent(72,6477.3611594);
  S2_ETA_0->SetBinContent(73,7159.18928144);
  S2_ETA_0->SetBinContent(74,5454.62097634);
  S2_ETA_0->SetBinContent(75,5795.53303736);
  S2_ETA_0->SetBinContent(76,6136.44909838);
  S2_ETA_0->SetBinContent(77,5454.62097634);
  S2_ETA_0->SetBinContent(78,4431.88079327);
  S2_ETA_0->SetBinContent(79,4090.96473225);
  S2_ETA_0->SetBinContent(80,3409.13741021);
  S2_ETA_0->SetBinContent(81,4431.88079327);
  S2_ETA_0->SetBinContent(82,3068.22374919);
  S2_ETA_0->SetBinContent(83,4772.79285429);
  S2_ETA_0->SetBinContent(84,6136.44909838);
  S2_ETA_0->SetBinContent(85,6136.44909838);
  S2_ETA_0->SetBinContent(86,5113.70491532);
  S2_ETA_0->SetBinContent(87,2386.39642715);
  S2_ETA_0->SetBinContent(88,6136.44909838);
  S2_ETA_0->SetBinContent(89,7500.10134246);
  S2_ETA_0->SetBinContent(90,8522.84552553);
  S2_ETA_0->SetBinContent(91,6818.27322042);
  S2_ETA_0->SetBinContent(92,7500.10134246);
  S2_ETA_0->SetBinContent(93,10227.4138306);
  S2_ETA_0->SetBinContent(94,4090.96473225);
  S2_ETA_0->SetBinContent(95,8181.9294645);
  S2_ETA_0->SetBinContent(96,9886.49776961);
  S2_ETA_0->SetBinContent(97,9886.49776961);
  S2_ETA_0->SetBinContent(98,5795.53303736);
  S2_ETA_0->SetBinContent(99,5113.70491532);
  S2_ETA_0->SetBinContent(100,6136.44909838);
  S2_ETA_0->SetBinContent(101,5113.70491532);
  S2_ETA_0->SetBinContent(102,4772.79285429);
  S2_ETA_0->SetBinContent(103,4772.79285429);
  S2_ETA_0->SetBinContent(104,4090.96473225);
  S2_ETA_0->SetBinContent(105,4090.96473225);
  S2_ETA_0->SetBinContent(106,4431.88079327);
  S2_ETA_0->SetBinContent(107,2386.39642715);
  S2_ETA_0->SetBinContent(108,1022.74138306);
  S2_ETA_0->SetBinContent(109,1704.56870511);
  S2_ETA_0->SetBinContent(110,1022.74138306);
  S2_ETA_0->SetBinContent(111,1363.65504408);
  S2_ETA_0->SetBinContent(112,1363.65504408);
  S2_ETA_0->SetBinContent(113,1363.65504408);
  S2_ETA_0->SetBinContent(114,2045.48236613);
  S2_ETA_0->SetBinContent(115,1022.74138306);
  S2_ETA_0->SetBinContent(116,1022.74138306);
  S2_ETA_0->SetBinContent(117,340.913741021);
  S2_ETA_0->SetBinContent(118,340.913741021);
  S2_ETA_0->SetBinContent(119,340.913741021);
  S2_ETA_0->SetBinContent(120,340.913741021);
  S2_ETA_0->SetBinContent(121,681.827322042);
  S2_ETA_0->SetBinContent(122,681.827322042);
  S2_ETA_0->SetBinContent(123,0.0);
  S2_ETA_0->SetBinContent(124,340.913741021);
  S2_ETA_0->SetBinContent(125,0.0);
  S2_ETA_0->SetBinContent(126,0.0);
  S2_ETA_0->SetBinContent(127,0.0);
  S2_ETA_0->SetBinContent(128,0.0);
  S2_ETA_0->SetBinContent(129,0.0);
  S2_ETA_0->SetBinContent(130,0.0);
  S2_ETA_0->SetBinContent(131,0.0);
  S2_ETA_0->SetBinContent(132,0.0);
  S2_ETA_0->SetBinContent(133,0.0);
  S2_ETA_0->SetBinContent(134,0.0);
  S2_ETA_0->SetBinContent(135,0.0);
  S2_ETA_0->SetBinContent(136,0.0);
  S2_ETA_0->SetBinContent(137,0.0);
  S2_ETA_0->SetBinContent(138,0.0);
  S2_ETA_0->SetBinContent(139,0.0);
  S2_ETA_0->SetBinContent(140,0.0);
  S2_ETA_0->SetBinContent(141,0.0);
  S2_ETA_0->SetBinContent(142,0.0);
  S2_ETA_0->SetBinContent(143,0.0);
  S2_ETA_0->SetBinContent(144,0.0);
  S2_ETA_0->SetBinContent(145,0.0);
  S2_ETA_0->SetBinContent(146,0.0);
  S2_ETA_0->SetBinContent(147,0.0);
  S2_ETA_0->SetBinContent(148,0.0);
  S2_ETA_0->SetBinContent(149,0.0);
  S2_ETA_0->SetBinContent(150,0.0);
  S2_ETA_0->SetBinContent(151,0.0);
  S2_ETA_0->SetBinContent(152,0.0);
  S2_ETA_0->SetBinContent(153,0.0);
  S2_ETA_0->SetBinContent(154,0.0);
  S2_ETA_0->SetBinContent(155,0.0);
  S2_ETA_0->SetBinContent(156,0.0);
  S2_ETA_0->SetBinContent(157,0.0);
  S2_ETA_0->SetBinContent(158,0.0);
  S2_ETA_0->SetBinContent(159,0.0);
  S2_ETA_0->SetBinContent(160,0.0);
  S2_ETA_0->SetBinContent(161,0.0); // overflow
  S2_ETA_0->SetEntries(999);
  // Style
  S2_ETA_0->SetLineColor(9);
  S2_ETA_0->SetLineStyle(1);
  S2_ETA_0->SetLineWidth(1);
  S2_ETA_0->SetFillColor(9);
  S2_ETA_0->SetFillStyle(1001);

  // Creating a new THStack
  THStack* stack = new THStack("mystack_4","mystack");
  stack->Add(S2_ETA_0);
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
  stack->GetXaxis()->SetTitle("#eta [ j_{1} ] ");

  // Finalizing the TCanvas
  canvas->SetLogx(0);
  canvas->SetLogy(0);

  // Saving the image
  canvas->SaveAs("../../HTML/MadAnalysis5job_0/selection_1.png");
  canvas->SaveAs("../../PDF/MadAnalysis5job_0/selection_1.png");
  canvas->SaveAs("../../DVI/MadAnalysis5job_0/selection_1.eps");

}
