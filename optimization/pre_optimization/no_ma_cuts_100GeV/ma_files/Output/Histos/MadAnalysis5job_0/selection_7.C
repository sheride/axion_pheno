void selection_7()
{

  // ROOT version
  Int_t root_version = gROOT->GetVersionInt();

  // Creating a new TCanvas
  TCanvas* canvas = new TCanvas("canvas_plotflow_tempo15","canvas_plotflow_tempo15",0,0,700,500);
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
  TH1F* S8_M_0 = new TH1F("S8_M_0","S8_M_0",160,0.0,8000.0);
  // Content
  S8_M_0->SetBinContent(0,0.0); // underflow
  S8_M_0->SetBinContent(1,0.0);
  S8_M_0->SetBinContent(2,0.0);
  S8_M_0->SetBinContent(3,1704.56872032);
  S8_M_0->SetBinContent(4,4772.7928969);
  S8_M_0->SetBinContent(5,6477.36121722);
  S8_M_0->SetBinContent(6,7841.01747347);
  S8_M_0->SetBinContent(7,6477.36121722);
  S8_M_0->SetBinContent(8,14659.2907548);
  S8_M_0->SetBinContent(9,8863.75766567);
  S8_M_0->SetBinContent(10,10568.325986);
  S8_M_0->SetBinContent(11,9545.58579379);
  S8_M_0->SetBinContent(12,13636.5505626);
  S8_M_0->SetBinContent(13,10568.325986);
  S8_M_0->SetBinContent(14,16363.8590751);
  S8_M_0->SetBinContent(15,11591.0661782);
  S8_M_0->SetBinContent(16,10568.325986);
  S8_M_0->SetBinContent(17,15000.2068188);
  S8_M_0->SetBinContent(18,11931.9822422);
  S8_M_0->SetBinContent(19,11931.9822422);
  S8_M_0->SetBinContent(20,9545.58579379);
  S8_M_0->SetBinContent(21,10909.2420501);
  S8_M_0->SetBinContent(22,9545.58579379);
  S8_M_0->SetBinContent(23,7841.01747347);
  S8_M_0->SetBinContent(24,9886.49785786);
  S8_M_0->SetBinContent(25,8522.8456016);
  S8_M_0->SetBinContent(26,7841.01747347);
  S8_M_0->SetBinContent(27,9886.49785786);
  S8_M_0->SetBinContent(28,5795.53308909);
  S8_M_0->SetBinContent(29,6477.36121722);
  S8_M_0->SetBinContent(30,6136.44915315);
  S8_M_0->SetBinContent(31,6818.27328128);
  S8_M_0->SetBinContent(32,7159.18934535);
  S8_M_0->SetBinContent(33,4090.96476877);
  S8_M_0->SetBinContent(34,6136.44915315);
  S8_M_0->SetBinContent(35,3409.13744064);
  S8_M_0->SetBinContent(36,3750.0515047);
  S8_M_0->SetBinContent(37,2727.31011251);
  S8_M_0->SetBinContent(38,3068.22377658);
  S8_M_0->SetBinContent(39,2727.31011251);
  S8_M_0->SetBinContent(40,3409.13744064);
  S8_M_0->SetBinContent(41,681.827328128);
  S8_M_0->SetBinContent(42,2045.48238438);
  S8_M_0->SetBinContent(43,1022.74139219);
  S8_M_0->SetBinContent(44,1704.56872032);
  S8_M_0->SetBinContent(45,4090.96476877);
  S8_M_0->SetBinContent(46,2045.48238438);
  S8_M_0->SetBinContent(47,1704.56872032);
  S8_M_0->SetBinContent(48,1704.56872032);
  S8_M_0->SetBinContent(49,681.827328128);
  S8_M_0->SetBinContent(50,1704.56872032);
  S8_M_0->SetBinContent(51,1022.74139219);
  S8_M_0->SetBinContent(52,681.827328128);
  S8_M_0->SetBinContent(53,1363.65505626);
  S8_M_0->SetBinContent(54,340.913744064);
  S8_M_0->SetBinContent(55,0.0);
  S8_M_0->SetBinContent(56,681.827328128);
  S8_M_0->SetBinContent(57,681.827328128);
  S8_M_0->SetBinContent(58,681.827328128);
  S8_M_0->SetBinContent(59,1022.74139219);
  S8_M_0->SetBinContent(60,1022.74139219);
  S8_M_0->SetBinContent(61,1022.74139219);
  S8_M_0->SetBinContent(62,1022.74139219);
  S8_M_0->SetBinContent(63,340.913744064);
  S8_M_0->SetBinContent(64,681.827328128);
  S8_M_0->SetBinContent(65,681.827328128);
  S8_M_0->SetBinContent(66,340.913744064);
  S8_M_0->SetBinContent(67,340.913744064);
  S8_M_0->SetBinContent(68,0.0);
  S8_M_0->SetBinContent(69,0.0);
  S8_M_0->SetBinContent(70,0.0);
  S8_M_0->SetBinContent(71,1704.56872032);
  S8_M_0->SetBinContent(72,0.0);
  S8_M_0->SetBinContent(73,0.0);
  S8_M_0->SetBinContent(74,0.0);
  S8_M_0->SetBinContent(75,0.0);
  S8_M_0->SetBinContent(76,0.0);
  S8_M_0->SetBinContent(77,0.0);
  S8_M_0->SetBinContent(78,0.0);
  S8_M_0->SetBinContent(79,0.0);
  S8_M_0->SetBinContent(80,0.0);
  S8_M_0->SetBinContent(81,0.0);
  S8_M_0->SetBinContent(82,0.0);
  S8_M_0->SetBinContent(83,0.0);
  S8_M_0->SetBinContent(84,0.0);
  S8_M_0->SetBinContent(85,340.913744064);
  S8_M_0->SetBinContent(86,0.0);
  S8_M_0->SetBinContent(87,0.0);
  S8_M_0->SetBinContent(88,340.913744064);
  S8_M_0->SetBinContent(89,0.0);
  S8_M_0->SetBinContent(90,0.0);
  S8_M_0->SetBinContent(91,0.0);
  S8_M_0->SetBinContent(92,340.913744064);
  S8_M_0->SetBinContent(93,0.0);
  S8_M_0->SetBinContent(94,0.0);
  S8_M_0->SetBinContent(95,340.913744064);
  S8_M_0->SetBinContent(96,0.0);
  S8_M_0->SetBinContent(97,0.0);
  S8_M_0->SetBinContent(98,0.0);
  S8_M_0->SetBinContent(99,0.0);
  S8_M_0->SetBinContent(100,0.0);
  S8_M_0->SetBinContent(101,0.0);
  S8_M_0->SetBinContent(102,0.0);
  S8_M_0->SetBinContent(103,0.0);
  S8_M_0->SetBinContent(104,0.0);
  S8_M_0->SetBinContent(105,0.0);
  S8_M_0->SetBinContent(106,0.0);
  S8_M_0->SetBinContent(107,0.0);
  S8_M_0->SetBinContent(108,0.0);
  S8_M_0->SetBinContent(109,0.0);
  S8_M_0->SetBinContent(110,0.0);
  S8_M_0->SetBinContent(111,0.0);
  S8_M_0->SetBinContent(112,0.0);
  S8_M_0->SetBinContent(113,0.0);
  S8_M_0->SetBinContent(114,0.0);
  S8_M_0->SetBinContent(115,0.0);
  S8_M_0->SetBinContent(116,0.0);
  S8_M_0->SetBinContent(117,0.0);
  S8_M_0->SetBinContent(118,0.0);
  S8_M_0->SetBinContent(119,0.0);
  S8_M_0->SetBinContent(120,0.0);
  S8_M_0->SetBinContent(121,0.0);
  S8_M_0->SetBinContent(122,0.0);
  S8_M_0->SetBinContent(123,0.0);
  S8_M_0->SetBinContent(124,0.0);
  S8_M_0->SetBinContent(125,0.0);
  S8_M_0->SetBinContent(126,0.0);
  S8_M_0->SetBinContent(127,0.0);
  S8_M_0->SetBinContent(128,0.0);
  S8_M_0->SetBinContent(129,0.0);
  S8_M_0->SetBinContent(130,0.0);
  S8_M_0->SetBinContent(131,0.0);
  S8_M_0->SetBinContent(132,0.0);
  S8_M_0->SetBinContent(133,0.0);
  S8_M_0->SetBinContent(134,0.0);
  S8_M_0->SetBinContent(135,0.0);
  S8_M_0->SetBinContent(136,0.0);
  S8_M_0->SetBinContent(137,0.0);
  S8_M_0->SetBinContent(138,0.0);
  S8_M_0->SetBinContent(139,0.0);
  S8_M_0->SetBinContent(140,0.0);
  S8_M_0->SetBinContent(141,0.0);
  S8_M_0->SetBinContent(142,0.0);
  S8_M_0->SetBinContent(143,0.0);
  S8_M_0->SetBinContent(144,0.0);
  S8_M_0->SetBinContent(145,0.0);
  S8_M_0->SetBinContent(146,0.0);
  S8_M_0->SetBinContent(147,0.0);
  S8_M_0->SetBinContent(148,0.0);
  S8_M_0->SetBinContent(149,0.0);
  S8_M_0->SetBinContent(150,0.0);
  S8_M_0->SetBinContent(151,0.0);
  S8_M_0->SetBinContent(152,0.0);
  S8_M_0->SetBinContent(153,0.0);
  S8_M_0->SetBinContent(154,0.0);
  S8_M_0->SetBinContent(155,0.0);
  S8_M_0->SetBinContent(156,0.0);
  S8_M_0->SetBinContent(157,0.0);
  S8_M_0->SetBinContent(158,0.0);
  S8_M_0->SetBinContent(159,0.0);
  S8_M_0->SetBinContent(160,0.0);
  S8_M_0->SetBinContent(161,0.0); // overflow
  S8_M_0->SetEntries(999);
  // Style
  S8_M_0->SetLineColor(9);
  S8_M_0->SetLineStyle(1);
  S8_M_0->SetLineWidth(1);
  S8_M_0->SetFillColor(9);
  S8_M_0->SetFillStyle(1001);

  // Creating a new THStack
  THStack* stack = new THStack("mystack_16","mystack");
  stack->Add(S8_M_0);
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
  stack->GetXaxis()->SetTitle("M [ j_{1} , j_{2} ]   ( GeV ) ");

  // Finalizing the TCanvas
  canvas->SetLogx(0);
  canvas->SetLogy(0);

  // Saving the image
  canvas->SaveAs("../../HTML/MadAnalysis5job_0/selection_7.png");
  canvas->SaveAs("../../PDF/MadAnalysis5job_0/selection_7.png");
  canvas->SaveAs("../../DVI/MadAnalysis5job_0/selection_7.eps");

}
