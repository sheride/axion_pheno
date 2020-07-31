void selection_0()
{

  // ROOT version
  Int_t root_version = gROOT->GetVersionInt();

  // Creating a new TCanvas
  TCanvas* canvas = new TCanvas("canvas_plotflow_tempo1","canvas_plotflow_tempo1",0,0,700,500);
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
  TH1F* S1_ETA_0 = new TH1F("S1_ETA_0","S1_ETA_0",100,-8.0,8.0);
  // Content
  S1_ETA_0->SetBinContent(0,0.0); // underflow
  S1_ETA_0->SetBinContent(1,0.0);
  S1_ETA_0->SetBinContent(2,0.0);
  S1_ETA_0->SetBinContent(3,0.0);
  S1_ETA_0->SetBinContent(4,0.0);
  S1_ETA_0->SetBinContent(5,0.0);
  S1_ETA_0->SetBinContent(6,0.0);
  S1_ETA_0->SetBinContent(7,0.0);
  S1_ETA_0->SetBinContent(8,0.0);
  S1_ETA_0->SetBinContent(9,0.0);
  S1_ETA_0->SetBinContent(10,0.0);
  S1_ETA_0->SetBinContent(11,0.0);
  S1_ETA_0->SetBinContent(12,0.0);
  S1_ETA_0->SetBinContent(13,0.0);
  S1_ETA_0->SetBinContent(14,0.0);
  S1_ETA_0->SetBinContent(15,0.0);
  S1_ETA_0->SetBinContent(16,0.0);
  S1_ETA_0->SetBinContent(17,0.0);
  S1_ETA_0->SetBinContent(18,0.0);
  S1_ETA_0->SetBinContent(19,0.0);
  S1_ETA_0->SetBinContent(20,0.0);
  S1_ETA_0->SetBinContent(21,0.0);
  S1_ETA_0->SetBinContent(22,0.0);
  S1_ETA_0->SetBinContent(23,0.0);
  S1_ETA_0->SetBinContent(24,813.137467067);
  S1_ETA_0->SetBinContent(25,406.568733534);
  S1_ETA_0->SetBinContent(26,813.137467067);
  S1_ETA_0->SetBinContent(27,0.0);
  S1_ETA_0->SetBinContent(28,406.568733534);
  S1_ETA_0->SetBinContent(29,0.0);
  S1_ETA_0->SetBinContent(30,813.137467067);
  S1_ETA_0->SetBinContent(31,406.568733534);
  S1_ETA_0->SetBinContent(32,1626.27533413);
  S1_ETA_0->SetBinContent(33,813.137467067);
  S1_ETA_0->SetBinContent(34,4065.68733534);
  S1_ETA_0->SetBinContent(35,2032.84406767);
  S1_ETA_0->SetBinContent(36,4472.25526887);
  S1_ETA_0->SetBinContent(37,4878.8272024);
  S1_ETA_0->SetBinContent(38,6098.531003);
  S1_ETA_0->SetBinContent(39,6911.67087007);
  S1_ETA_0->SetBinContent(40,6911.67087007);
  S1_ETA_0->SetBinContent(41,12197.066006);
  S1_ETA_0->SetBinContent(42,15043.0455407);
  S1_ETA_0->SetBinContent(43,13823.3377401);
  S1_ETA_0->SetBinContent(44,12603.6339395);
  S1_ETA_0->SetBinContent(45,13010.2018731);
  S1_ETA_0->SetBinContent(46,19515.3008096);
  S1_ETA_0->SetBinContent(47,18702.1649425);
  S1_ETA_0->SetBinContent(48,16669.3212749);
  S1_ETA_0->SetBinContent(49,15856.1814078);
  S1_ETA_0->SetBinContent(50,21548.1484773);
  S1_ETA_0->SetBinContent(51,21141.5765437);
  S1_ETA_0->SetBinContent(52,22361.2843443);
  S1_ETA_0->SetBinContent(53,21954.7164108);
  S1_ETA_0->SetBinContent(54,14636.4776072);
  S1_ETA_0->SetBinContent(55,13010.2018731);
  S1_ETA_0->SetBinContent(56,15043.0455407);
  S1_ETA_0->SetBinContent(57,13823.3377401);
  S1_ETA_0->SetBinContent(58,11790.4940725);
  S1_ETA_0->SetBinContent(59,9757.6504048);
  S1_ETA_0->SetBinContent(60,9351.08247127);
  S1_ETA_0->SetBinContent(61,9351.08247127);
  S1_ETA_0->SetBinContent(62,5691.96306947);
  S1_ETA_0->SetBinContent(63,6098.531003);
  S1_ETA_0->SetBinContent(64,6098.531003);
  S1_ETA_0->SetBinContent(65,5285.39513594);
  S1_ETA_0->SetBinContent(66,4878.8272024);
  S1_ETA_0->SetBinContent(67,2845.98153473);
  S1_ETA_0->SetBinContent(68,2439.4128012);
  S1_ETA_0->SetBinContent(69,2439.4128012);
  S1_ETA_0->SetBinContent(70,2032.84406767);
  S1_ETA_0->SetBinContent(71,1626.27533413);
  S1_ETA_0->SetBinContent(72,1219.7066006);
  S1_ETA_0->SetBinContent(73,813.137467067);
  S1_ETA_0->SetBinContent(74,813.137467067);
  S1_ETA_0->SetBinContent(75,406.568733534);
  S1_ETA_0->SetBinContent(76,0.0);
  S1_ETA_0->SetBinContent(77,406.568733534);
  S1_ETA_0->SetBinContent(78,406.568733534);
  S1_ETA_0->SetBinContent(79,0.0);
  S1_ETA_0->SetBinContent(80,0.0);
  S1_ETA_0->SetBinContent(81,0.0);
  S1_ETA_0->SetBinContent(82,0.0);
  S1_ETA_0->SetBinContent(83,0.0);
  S1_ETA_0->SetBinContent(84,0.0);
  S1_ETA_0->SetBinContent(85,0.0);
  S1_ETA_0->SetBinContent(86,0.0);
  S1_ETA_0->SetBinContent(87,0.0);
  S1_ETA_0->SetBinContent(88,0.0);
  S1_ETA_0->SetBinContent(89,0.0);
  S1_ETA_0->SetBinContent(90,0.0);
  S1_ETA_0->SetBinContent(91,0.0);
  S1_ETA_0->SetBinContent(92,0.0);
  S1_ETA_0->SetBinContent(93,0.0);
  S1_ETA_0->SetBinContent(94,0.0);
  S1_ETA_0->SetBinContent(95,0.0);
  S1_ETA_0->SetBinContent(96,0.0);
  S1_ETA_0->SetBinContent(97,0.0);
  S1_ETA_0->SetBinContent(98,0.0);
  S1_ETA_0->SetBinContent(99,0.0);
  S1_ETA_0->SetBinContent(100,0.0);
  S1_ETA_0->SetBinContent(101,0.0); // overflow
  S1_ETA_0->SetEntries(999);
  // Style
  S1_ETA_0->SetLineColor(9);
  S1_ETA_0->SetLineStyle(1);
  S1_ETA_0->SetLineWidth(1);
  S1_ETA_0->SetFillColor(9);
  S1_ETA_0->SetFillStyle(1001);

  // Creating a new THStack
  THStack* stack = new THStack("mystack_2","mystack");
  stack->Add(S1_ETA_0);
  stack->Draw("");

  // Y axis
  stack->GetYaxis()->SetLabelSize(0.04);
  stack->GetYaxis()->SetLabelOffset(0.005);
  stack->GetYaxis()->SetTitleSize(0.06);
  stack->GetYaxis()->SetTitleFont(22);
  stack->GetYaxis()->SetTitleOffset(1);
  stack->GetYaxis()->SetTitle("N. of ax ( L_{int} = 40.0 fb^{-1} )");

  // X axis
  stack->GetXaxis()->SetLabelSize(0.04);
  stack->GetXaxis()->SetLabelOffset(0.005);
  stack->GetXaxis()->SetTitleSize(0.06);
  stack->GetXaxis()->SetTitleFont(22);
  stack->GetXaxis()->SetTitleOffset(1);
  stack->GetXaxis()->SetTitle("#eta [ ax ] ");

  // Finalizing the TCanvas
  canvas->SetLogx(0);
  canvas->SetLogy(0);

  // Saving the image
  canvas->SaveAs("../../HTML/MadAnalysis5job_0/selection_0.png");
  canvas->SaveAs("../../PDF/MadAnalysis5job_0/selection_0.png");
  canvas->SaveAs("../../DVI/MadAnalysis5job_0/selection_0.eps");

}
