void selection_12()
{

  // ROOT version
  Int_t root_version = gROOT->GetVersionInt();

  // Creating a new TCanvas
  TCanvas* canvas = new TCanvas("canvas_plotflow_tempo25","canvas_plotflow_tempo25",0,0,1000,500);
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
  TH1F* S13_THT_0 = new TH1F("S13_THT_0","S13_THT_0",80,0.0,4000.0);
  // Content
  S13_THT_0->SetBinContent(0,0.0); // underflow
  S13_THT_0->SetBinContent(1,2481.65014775);
  S13_THT_0->SetBinContent(2,47204.5499588);
  S13_THT_0->SetBinContent(3,47204.5499588);
  S13_THT_0->SetBinContent(4,36624.2128929);
  S13_THT_0->SetBinContent(5,35810.339271);
  S13_THT_0->SetBinContent(6,32554.8527909);
  S13_THT_0->SetBinContent(7,25636.949025);
  S13_THT_0->SetBinContent(8,29299.3703143);
  S13_THT_0->SetBinContent(9,21160.6541139);
  S13_THT_0->SetBinContent(10,19125.9760647);
  S13_THT_0->SetBinContent(11,17498.2328246);
  S13_THT_0->SetBinContent(12,14242.750348);
  S13_THT_0->SetBinContent(13,13428.8767262);
  S13_THT_0->SetBinContent(14,10987.2638679);
  S13_THT_0->SetBinContent(15,6510.96895673);
  S13_THT_0->SetBinContent(16,7324.84257858);
  S13_THT_0->SetBinContent(17,7324.84257858);
  S13_THT_0->SetBinContent(18,7324.84257858);
  S13_THT_0->SetBinContent(19,3662.42128929);
  S13_THT_0->SetBinContent(20,4476.29090753);
  S13_THT_0->SetBinContent(21,3662.42128929);
  S13_THT_0->SetBinContent(22,2441.6140594);
  S13_THT_0->SetBinContent(23,2848.54966925);
  S13_THT_0->SetBinContent(24,1627.74283972);
  S13_THT_0->SetBinContent(25,1220.80722988);
  S13_THT_0->SetBinContent(26,2034.67844956);
  S13_THT_0->SetBinContent(27,406.935609841);
  S13_THT_0->SetBinContent(28,406.935609841);
  S13_THT_0->SetBinContent(29,0.0);
  S13_THT_0->SetBinContent(30,406.935609841);
  S13_THT_0->SetBinContent(31,0.0);
  S13_THT_0->SetBinContent(32,0.0);
  S13_THT_0->SetBinContent(33,0.0);
  S13_THT_0->SetBinContent(34,0.0);
  S13_THT_0->SetBinContent(35,406.935609841);
  S13_THT_0->SetBinContent(36,0.0);
  S13_THT_0->SetBinContent(37,0.0);
  S13_THT_0->SetBinContent(38,406.935609841);
  S13_THT_0->SetBinContent(39,406.935609841);
  S13_THT_0->SetBinContent(40,406.935609841);
  S13_THT_0->SetBinContent(41,0.0);
  S13_THT_0->SetBinContent(42,0.0);
  S13_THT_0->SetBinContent(43,0.0);
  S13_THT_0->SetBinContent(44,0.0);
  S13_THT_0->SetBinContent(45,0.0);
  S13_THT_0->SetBinContent(46,0.0);
  S13_THT_0->SetBinContent(47,0.0);
  S13_THT_0->SetBinContent(48,0.0);
  S13_THT_0->SetBinContent(49,0.0);
  S13_THT_0->SetBinContent(50,0.0);
  S13_THT_0->SetBinContent(51,0.0);
  S13_THT_0->SetBinContent(52,0.0);
  S13_THT_0->SetBinContent(53,0.0);
  S13_THT_0->SetBinContent(54,0.0);
  S13_THT_0->SetBinContent(55,0.0);
  S13_THT_0->SetBinContent(56,0.0);
  S13_THT_0->SetBinContent(57,0.0);
  S13_THT_0->SetBinContent(58,0.0);
  S13_THT_0->SetBinContent(59,0.0);
  S13_THT_0->SetBinContent(60,0.0);
  S13_THT_0->SetBinContent(61,0.0);
  S13_THT_0->SetBinContent(62,0.0);
  S13_THT_0->SetBinContent(63,0.0);
  S13_THT_0->SetBinContent(64,0.0);
  S13_THT_0->SetBinContent(65,0.0);
  S13_THT_0->SetBinContent(66,0.0);
  S13_THT_0->SetBinContent(67,0.0);
  S13_THT_0->SetBinContent(68,0.0);
  S13_THT_0->SetBinContent(69,0.0);
  S13_THT_0->SetBinContent(70,0.0);
  S13_THT_0->SetBinContent(71,0.0);
  S13_THT_0->SetBinContent(72,0.0);
  S13_THT_0->SetBinContent(73,0.0);
  S13_THT_0->SetBinContent(74,0.0);
  S13_THT_0->SetBinContent(75,0.0);
  S13_THT_0->SetBinContent(76,0.0);
  S13_THT_0->SetBinContent(77,0.0);
  S13_THT_0->SetBinContent(78,0.0);
  S13_THT_0->SetBinContent(79,0.0);
  S13_THT_0->SetBinContent(80,0.0);
  S13_THT_0->SetBinContent(81,0.0); // overflow
  S13_THT_0->SetEntries(1000);
  // Style
  S13_THT_0->SetLineColor(9);
  S13_THT_0->SetLineStyle(1);
  S13_THT_0->SetLineWidth(1);
  S13_THT_0->SetFillColor(9);
  S13_THT_0->SetFillStyle(1001);

  // Creating a new TH1F
  TH1F* S13_THT_1 = new TH1F("S13_THT_1","S13_THT_1",80,0.0,4000.0);
  // Content
  S13_THT_1->SetBinContent(0,0.0); // underflow
  S13_THT_1->SetBinContent(1,670.387849719);
  S13_THT_1->SetBinContent(2,2728.77864902);
  S13_THT_1->SetBinContent(3,1773.7057748);
  S13_THT_1->SetBinContent(4,955.072340275);
  S13_THT_1->SetBinContent(5,682.194528768);
  S13_THT_1->SetBinContent(6,955.072340275);
  S13_THT_1->SetBinContent(7,818.633434522);
  S13_THT_1->SetBinContent(8,409.316770656);
  S13_THT_1->SetBinContent(9,0.0);
  S13_THT_1->SetBinContent(10,0.0);
  S13_THT_1->SetBinContent(11,0.0);
  S13_THT_1->SetBinContent(12,272.877864902);
  S13_THT_1->SetBinContent(13,272.877864902);
  S13_THT_1->SetBinContent(14,136.438905754);
  S13_THT_1->SetBinContent(15,0.0);
  S13_THT_1->SetBinContent(16,0.0);
  S13_THT_1->SetBinContent(17,136.438905754);
  S13_THT_1->SetBinContent(18,0.0);
  S13_THT_1->SetBinContent(19,136.438905754);
  S13_THT_1->SetBinContent(20,0.0);
  S13_THT_1->SetBinContent(21,0.0);
  S13_THT_1->SetBinContent(22,0.0);
  S13_THT_1->SetBinContent(23,0.0);
  S13_THT_1->SetBinContent(24,0.0);
  S13_THT_1->SetBinContent(25,0.0);
  S13_THT_1->SetBinContent(26,0.0);
  S13_THT_1->SetBinContent(27,272.877864902);
  S13_THT_1->SetBinContent(28,0.0);
  S13_THT_1->SetBinContent(29,0.0);
  S13_THT_1->SetBinContent(30,0.0);
  S13_THT_1->SetBinContent(31,0.0);
  S13_THT_1->SetBinContent(32,0.0);
  S13_THT_1->SetBinContent(33,0.0);
  S13_THT_1->SetBinContent(34,0.0);
  S13_THT_1->SetBinContent(35,0.0);
  S13_THT_1->SetBinContent(36,0.0);
  S13_THT_1->SetBinContent(37,0.0);
  S13_THT_1->SetBinContent(38,0.0);
  S13_THT_1->SetBinContent(39,0.0);
  S13_THT_1->SetBinContent(40,0.0);
  S13_THT_1->SetBinContent(41,0.0);
  S13_THT_1->SetBinContent(42,0.0);
  S13_THT_1->SetBinContent(43,0.0);
  S13_THT_1->SetBinContent(44,0.0);
  S13_THT_1->SetBinContent(45,0.0);
  S13_THT_1->SetBinContent(46,0.0);
  S13_THT_1->SetBinContent(47,0.0);
  S13_THT_1->SetBinContent(48,0.0);
  S13_THT_1->SetBinContent(49,0.0);
  S13_THT_1->SetBinContent(50,0.0);
  S13_THT_1->SetBinContent(51,0.0);
  S13_THT_1->SetBinContent(52,0.0);
  S13_THT_1->SetBinContent(53,0.0);
  S13_THT_1->SetBinContent(54,0.0);
  S13_THT_1->SetBinContent(55,0.0);
  S13_THT_1->SetBinContent(56,0.0);
  S13_THT_1->SetBinContent(57,0.0);
  S13_THT_1->SetBinContent(58,0.0);
  S13_THT_1->SetBinContent(59,0.0);
  S13_THT_1->SetBinContent(60,0.0);
  S13_THT_1->SetBinContent(61,0.0);
  S13_THT_1->SetBinContent(62,0.0);
  S13_THT_1->SetBinContent(63,0.0);
  S13_THT_1->SetBinContent(64,0.0);
  S13_THT_1->SetBinContent(65,0.0);
  S13_THT_1->SetBinContent(66,0.0);
  S13_THT_1->SetBinContent(67,0.0);
  S13_THT_1->SetBinContent(68,0.0);
  S13_THT_1->SetBinContent(69,0.0);
  S13_THT_1->SetBinContent(70,0.0);
  S13_THT_1->SetBinContent(71,0.0);
  S13_THT_1->SetBinContent(72,0.0);
  S13_THT_1->SetBinContent(73,0.0);
  S13_THT_1->SetBinContent(74,0.0);
  S13_THT_1->SetBinContent(75,0.0);
  S13_THT_1->SetBinContent(76,0.0);
  S13_THT_1->SetBinContent(77,0.0);
  S13_THT_1->SetBinContent(78,0.0);
  S13_THT_1->SetBinContent(79,0.0);
  S13_THT_1->SetBinContent(80,0.0);
  S13_THT_1->SetBinContent(81,0.0); // overflow
  S13_THT_1->SetEntries(72);
  // Style
  S13_THT_1->SetLineColor(46);
  S13_THT_1->SetLineStyle(1);
  S13_THT_1->SetLineWidth(1);
  S13_THT_1->SetFillColor(46);
  S13_THT_1->SetFillStyle(1001);

  // Creating a new THStack
  THStack* stack = new THStack("mystack_26","mystack");
  stack->Add(S13_THT_0);
  stack->Add(S13_THT_1);
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
  legend->AddEntry(S13_THT_0,"signal1TeV");
  legend->AddEntry(S13_THT_1,"signal4TeV");
  legend->SetFillColor(0);
  legend->SetTextSize(0.05);
  legend->SetTextFont(22);
  legend->SetY1(TMath::Max(0.15,0.97-0.10*legend->GetListOfPrimitives()->GetSize()));
  legend->Draw();

  // Saving the image
  canvas->SaveAs("../../HTML/MadAnalysis5job_0/selection_12.png");
  canvas->SaveAs("../../PDF/MadAnalysis5job_0/selection_12.png");
  canvas->SaveAs("../../DVI/MadAnalysis5job_0/selection_12.eps");

}
