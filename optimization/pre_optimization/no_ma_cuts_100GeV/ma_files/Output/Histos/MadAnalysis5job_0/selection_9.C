void selection_9()
{

  // ROOT version
  Int_t root_version = gROOT->GetVersionInt();

  // Creating a new TCanvas
  TCanvas* canvas = new TCanvas("canvas_plotflow_tempo19","canvas_plotflow_tempo19",0,0,700,500);
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
  TH1F* S10_THT_0 = new TH1F("S10_THT_0","S10_THT_0",80,0.0,4000.0);
  // Content
  S10_THT_0->SetBinContent(0,0.0); // underflow
  S10_THT_0->SetBinContent(1,1746.10994152);
  S10_THT_0->SetBinContent(2,22861.3990337);
  S10_THT_0->SetBinContent(3,23543.8295129);
  S10_THT_0->SetBinContent(4,30368.1303014);
  S10_THT_0->SetBinContent(5,29685.6998222);
  S10_THT_0->SetBinContent(6,26273.5514297);
  S10_THT_0->SetBinContent(7,27297.1951467);
  S10_THT_0->SetBinContent(8,19449.2506413);
  S10_THT_0->SetBinContent(9,25591.1209505);
  S10_THT_0->SetBinContent(10,16719.532728);
  S10_THT_0->SetBinContent(11,17401.9632072);
  S10_THT_0->SetBinContent(12,15354.6717696);
  S10_THT_0->SetBinContent(13,12624.9538563);
  S10_THT_0->SetBinContent(14,10236.4491809);
  S10_THT_0->SetBinContent(15,7165.51402628);
  S10_THT_0->SetBinContent(16,8530.37498468);
  S10_THT_0->SetBinContent(17,6824.29678492);
  S10_THT_0->SetBinContent(18,6483.08354708);
  S10_THT_0->SetBinContent(19,4777.00935086);
  S10_THT_0->SetBinContent(20,4094.57887166);
  S10_THT_0->SetBinContent(21,3753.36443276);
  S10_THT_0->SetBinContent(22,3070.93435392);
  S10_THT_0->SetBinContent(23,3753.36443276);
  S10_THT_0->SetBinContent(24,2388.50467543);
  S10_THT_0->SetBinContent(25,2729.71951467);
  S10_THT_0->SetBinContent(26,682.429678492);
  S10_THT_0->SetBinContent(27,341.214919316);
  S10_THT_0->SetBinContent(28,1364.85975734);
  S10_THT_0->SetBinContent(29,682.429678492);
  S10_THT_0->SetBinContent(30,682.429678492);
  S10_THT_0->SetBinContent(31,682.429678492);
  S10_THT_0->SetBinContent(32,1023.64491809);
  S10_THT_0->SetBinContent(33,341.214919316);
  S10_THT_0->SetBinContent(34,682.429678492);
  S10_THT_0->SetBinContent(35,341.214919316);
  S10_THT_0->SetBinContent(36,0.0);
  S10_THT_0->SetBinContent(37,341.214919316);
  S10_THT_0->SetBinContent(38,341.214919316);
  S10_THT_0->SetBinContent(39,0.0);
  S10_THT_0->SetBinContent(40,0.0);
  S10_THT_0->SetBinContent(41,341.214919316);
  S10_THT_0->SetBinContent(42,0.0);
  S10_THT_0->SetBinContent(43,0.0);
  S10_THT_0->SetBinContent(44,0.0);
  S10_THT_0->SetBinContent(45,341.214919316);
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

  // Creating a new THStack
  THStack* stack = new THStack("mystack_20","mystack");
  stack->Add(S10_THT_0);
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

  // Saving the image
  canvas->SaveAs("../../HTML/MadAnalysis5job_0/selection_9.png");
  canvas->SaveAs("../../PDF/MadAnalysis5job_0/selection_9.png");
  canvas->SaveAs("../../DVI/MadAnalysis5job_0/selection_9.eps");

}
