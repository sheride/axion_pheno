void selection_3()
{

  // ROOT version
  Int_t root_version = gROOT->GetVersionInt();

  // Creating a new TCanvas
  TCanvas* canvas = new TCanvas("canvas_plotflow_tempo7","canvas_plotflow_tempo7",0,0,700,500);
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
  TH1F* S4_PT_0 = new TH1F("S4_PT_0","S4_PT_0",100,0.0,1000.0);
  // Content
  S4_PT_0->SetBinContent(0,0.0); // underflow
  S4_PT_0->SetBinContent(1,0.0);
  S4_PT_0->SetBinContent(2,0.0);
  S4_PT_0->SetBinContent(3,36477.7714118);
  S4_PT_0->SetBinContent(4,24886.7050567);
  S4_PT_0->SetBinContent(5,20113.9120869);
  S4_PT_0->SetBinContent(6,19432.0839483);
  S4_PT_0->SetBinContent(7,17386.6035327);
  S4_PT_0->SetBinContent(8,14659.2909786);
  S4_PT_0->SetBinContent(9,17727.515602);
  S4_PT_0->SetBinContent(10,16022.9472557);
  S4_PT_0->SetBinContent(11,12954.7226322);
  S4_PT_0->SetBinContent(12,15682.0351864);
  S4_PT_0->SetBinContent(13,11931.9824244);
  S4_PT_0->SetBinContent(14,11931.9824244);
  S4_PT_0->SetBinContent(15,12613.810563);
  S4_PT_0->SetBinContent(16,9204.66987027);
  S4_PT_0->SetBinContent(17,7500.10152392);
  S4_PT_0->SetBinContent(18,8181.92966246);
  S4_PT_0->SetBinContent(19,7841.01759319);
  S4_PT_0->SetBinContent(20,5113.70503904);
  S4_PT_0->SetBinContent(21,5795.53317758);
  S4_PT_0->SetBinContent(22,5113.70503904);
  S4_PT_0->SetBinContent(23,2727.31015415);
  S4_PT_0->SetBinContent(24,6477.36131612);
  S4_PT_0->SetBinContent(25,1704.56874635);
  S4_PT_0->SetBinContent(26,3750.05156196);
  S4_PT_0->SetBinContent(27,4090.96483123);
  S4_PT_0->SetBinContent(28,2727.31015415);
  S4_PT_0->SetBinContent(29,3750.05156196);
  S4_PT_0->SetBinContent(30,2386.39648488);
  S4_PT_0->SetBinContent(31,2727.31015415);
  S4_PT_0->SetBinContent(32,2045.48241562);
  S4_PT_0->SetBinContent(33,4090.96483123);
  S4_PT_0->SetBinContent(34,2045.48241562);
  S4_PT_0->SetBinContent(35,1704.56874635);
  S4_PT_0->SetBinContent(36,1704.56874635);
  S4_PT_0->SetBinContent(37,681.827338539);
  S4_PT_0->SetBinContent(38,1022.74140781);
  S4_PT_0->SetBinContent(39,1022.74140781);
  S4_PT_0->SetBinContent(40,681.827338539);
  S4_PT_0->SetBinContent(41,1022.74140781);
  S4_PT_0->SetBinContent(42,1022.74140781);
  S4_PT_0->SetBinContent(43,1363.65507708);
  S4_PT_0->SetBinContent(44,340.913749269);
  S4_PT_0->SetBinContent(45,340.913749269);
  S4_PT_0->SetBinContent(46,1022.74140781);
  S4_PT_0->SetBinContent(47,0.0);
  S4_PT_0->SetBinContent(48,1022.74140781);
  S4_PT_0->SetBinContent(49,1022.74140781);
  S4_PT_0->SetBinContent(50,1704.56874635);
  S4_PT_0->SetBinContent(51,0.0);
  S4_PT_0->SetBinContent(52,340.913749269);
  S4_PT_0->SetBinContent(53,681.827338539);
  S4_PT_0->SetBinContent(54,681.827338539);
  S4_PT_0->SetBinContent(55,340.913749269);
  S4_PT_0->SetBinContent(56,340.913749269);
  S4_PT_0->SetBinContent(57,0.0);
  S4_PT_0->SetBinContent(58,0.0);
  S4_PT_0->SetBinContent(59,0.0);
  S4_PT_0->SetBinContent(60,681.827338539);
  S4_PT_0->SetBinContent(61,340.913749269);
  S4_PT_0->SetBinContent(62,0.0);
  S4_PT_0->SetBinContent(63,340.913749269);
  S4_PT_0->SetBinContent(64,0.0);
  S4_PT_0->SetBinContent(65,0.0);
  S4_PT_0->SetBinContent(66,340.913749269);
  S4_PT_0->SetBinContent(67,340.913749269);
  S4_PT_0->SetBinContent(68,340.913749269);
  S4_PT_0->SetBinContent(69,340.913749269);
  S4_PT_0->SetBinContent(70,340.913749269);
  S4_PT_0->SetBinContent(71,0.0);
  S4_PT_0->SetBinContent(72,0.0);
  S4_PT_0->SetBinContent(73,0.0);
  S4_PT_0->SetBinContent(74,0.0);
  S4_PT_0->SetBinContent(75,0.0);
  S4_PT_0->SetBinContent(76,340.913749269);
  S4_PT_0->SetBinContent(77,0.0);
  S4_PT_0->SetBinContent(78,0.0);
  S4_PT_0->SetBinContent(79,0.0);
  S4_PT_0->SetBinContent(80,0.0);
  S4_PT_0->SetBinContent(81,0.0);
  S4_PT_0->SetBinContent(82,0.0);
  S4_PT_0->SetBinContent(83,0.0);
  S4_PT_0->SetBinContent(84,0.0);
  S4_PT_0->SetBinContent(85,0.0);
  S4_PT_0->SetBinContent(86,0.0);
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

  // Creating a new THStack
  THStack* stack = new THStack("mystack_8","mystack");
  stack->Add(S4_PT_0);
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

  // Saving the image
  canvas->SaveAs("../../HTML/MadAnalysis5job_0/selection_3.png");
  canvas->SaveAs("../../PDF/MadAnalysis5job_0/selection_3.png");
  canvas->SaveAs("../../DVI/MadAnalysis5job_0/selection_3.eps");

}
