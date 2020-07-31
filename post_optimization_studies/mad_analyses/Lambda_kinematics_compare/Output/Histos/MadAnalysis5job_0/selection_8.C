void selection_8()
{

  // ROOT version
  Int_t root_version = gROOT->GetVersionInt();

  // Creating a new TCanvas
  TCanvas* canvas = new TCanvas("canvas_plotflow_tempo17","canvas_plotflow_tempo17",0,0,1000,500);
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
  TH1F* S9_sdETA_0 = new TH1F("S9_sdETA_0","S9_sdETA_0",100,-15.0,15.0);
  // Content
  S9_sdETA_0->SetBinContent(0,0.0); // underflow
  S9_sdETA_0->SetBinContent(1,0.0);
  S9_sdETA_0->SetBinContent(2,0.0);
  S9_sdETA_0->SetBinContent(3,0.0);
  S9_sdETA_0->SetBinContent(4,0.0);
  S9_sdETA_0->SetBinContent(5,0.0);
  S9_sdETA_0->SetBinContent(6,0.0);
  S9_sdETA_0->SetBinContent(7,0.0);
  S9_sdETA_0->SetBinContent(8,0.0);
  S9_sdETA_0->SetBinContent(9,0.0);
  S9_sdETA_0->SetBinContent(10,0.0);
  S9_sdETA_0->SetBinContent(11,0.0);
  S9_sdETA_0->SetBinContent(12,0.0);
  S9_sdETA_0->SetBinContent(13,0.0);
  S9_sdETA_0->SetBinContent(14,0.0);
  S9_sdETA_0->SetBinContent(15,0.0);
  S9_sdETA_0->SetBinContent(16,0.0);
  S9_sdETA_0->SetBinContent(17,0.0);
  S9_sdETA_0->SetBinContent(18,0.0);
  S9_sdETA_0->SetBinContent(19,0.0);
  S9_sdETA_0->SetBinContent(20,0.0);
  S9_sdETA_0->SetBinContent(21,0.0);
  S9_sdETA_0->SetBinContent(22,0.0);
  S9_sdETA_0->SetBinContent(23,0.0);
  S9_sdETA_0->SetBinContent(24,0.0);
  S9_sdETA_0->SetBinContent(25,406.568725926);
  S9_sdETA_0->SetBinContent(26,1219.70657778);
  S9_sdETA_0->SetBinContent(27,1219.70657778);
  S9_sdETA_0->SetBinContent(28,813.137451852);
  S9_sdETA_0->SetBinContent(29,2032.84402963);
  S9_sdETA_0->SetBinContent(30,2032.84402963);
  S9_sdETA_0->SetBinContent(31,5691.96296296);
  S9_sdETA_0->SetBinContent(32,1626.2753037);
  S9_sdETA_0->SetBinContent(33,4878.82711111);
  S9_sdETA_0->SetBinContent(34,7318.23866667);
  S9_sdETA_0->SetBinContent(35,9351.0822963);
  S9_sdETA_0->SetBinContent(36,12197.0657778);
  S9_sdETA_0->SetBinContent(37,14229.9094074);
  S9_sdETA_0->SetBinContent(38,10570.7900741);
  S9_sdETA_0->SetBinContent(39,24800.6954815);
  S9_sdETA_0->SetBinContent(40,24800.6954815);
  S9_sdETA_0->SetBinContent(41,33338.6419259);
  S9_sdETA_0->SetBinContent(42,42283.1522963);
  S9_sdETA_0->SetBinContent(43,0.0);
  S9_sdETA_0->SetBinContent(44,0.0);
  S9_sdETA_0->SetBinContent(45,0.0);
  S9_sdETA_0->SetBinContent(46,0.0);
  S9_sdETA_0->SetBinContent(47,0.0);
  S9_sdETA_0->SetBinContent(48,0.0);
  S9_sdETA_0->SetBinContent(49,0.0);
  S9_sdETA_0->SetBinContent(50,0.0);
  S9_sdETA_0->SetBinContent(51,0.0);
  S9_sdETA_0->SetBinContent(52,0.0);
  S9_sdETA_0->SetBinContent(53,0.0);
  S9_sdETA_0->SetBinContent(54,0.0);
  S9_sdETA_0->SetBinContent(55,0.0);
  S9_sdETA_0->SetBinContent(56,0.0);
  S9_sdETA_0->SetBinContent(57,0.0);
  S9_sdETA_0->SetBinContent(58,0.0);
  S9_sdETA_0->SetBinContent(59,38217.465037);
  S9_sdETA_0->SetBinContent(60,34964.9176296);
  S9_sdETA_0->SetBinContent(61,24800.6954815);
  S9_sdETA_0->SetBinContent(62,23174.4197778);
  S9_sdETA_0->SetBinContent(63,20328.4402963);
  S9_sdETA_0->SetBinContent(64,14229.9094074);
  S9_sdETA_0->SetBinContent(65,7724.80659259);
  S9_sdETA_0->SetBinContent(66,9351.0822963);
  S9_sdETA_0->SetBinContent(67,8537.94644444);
  S9_sdETA_0->SetBinContent(68,4065.68725926);
  S9_sdETA_0->SetBinContent(69,4878.82711111);
  S9_sdETA_0->SetBinContent(70,7318.23866667);
  S9_sdETA_0->SetBinContent(71,2439.41275556);
  S9_sdETA_0->SetBinContent(72,1626.2753037);
  S9_sdETA_0->SetBinContent(73,1219.70657778);
  S9_sdETA_0->SetBinContent(74,813.137451852);
  S9_sdETA_0->SetBinContent(75,2032.84402963);
  S9_sdETA_0->SetBinContent(76,406.568725926);
  S9_sdETA_0->SetBinContent(77,813.137451852);
  S9_sdETA_0->SetBinContent(78,0.0);
  S9_sdETA_0->SetBinContent(79,406.568725926);
  S9_sdETA_0->SetBinContent(80,0.0);
  S9_sdETA_0->SetBinContent(81,0.0);
  S9_sdETA_0->SetBinContent(82,0.0);
  S9_sdETA_0->SetBinContent(83,0.0);
  S9_sdETA_0->SetBinContent(84,0.0);
  S9_sdETA_0->SetBinContent(85,0.0);
  S9_sdETA_0->SetBinContent(86,0.0);
  S9_sdETA_0->SetBinContent(87,0.0);
  S9_sdETA_0->SetBinContent(88,0.0);
  S9_sdETA_0->SetBinContent(89,0.0);
  S9_sdETA_0->SetBinContent(90,0.0);
  S9_sdETA_0->SetBinContent(91,0.0);
  S9_sdETA_0->SetBinContent(92,0.0);
  S9_sdETA_0->SetBinContent(93,0.0);
  S9_sdETA_0->SetBinContent(94,0.0);
  S9_sdETA_0->SetBinContent(95,0.0);
  S9_sdETA_0->SetBinContent(96,0.0);
  S9_sdETA_0->SetBinContent(97,0.0);
  S9_sdETA_0->SetBinContent(98,0.0);
  S9_sdETA_0->SetBinContent(99,0.0);
  S9_sdETA_0->SetBinContent(100,0.0);
  S9_sdETA_0->SetBinContent(101,0.0); // overflow
  S9_sdETA_0->SetEntries(999);
  // Style
  S9_sdETA_0->SetLineColor(9);
  S9_sdETA_0->SetLineStyle(1);
  S9_sdETA_0->SetLineWidth(1);
  S9_sdETA_0->SetFillColor(9);
  S9_sdETA_0->SetFillStyle(1001);

  // Creating a new TH1F
  TH1F* S9_sdETA_1 = new TH1F("S9_sdETA_1","S9_sdETA_1",100,-15.0,15.0);
  // Content
  S9_sdETA_1->SetBinContent(0,0.0); // underflow
  S9_sdETA_1->SetBinContent(1,0.0);
  S9_sdETA_1->SetBinContent(2,0.0);
  S9_sdETA_1->SetBinContent(3,0.0);
  S9_sdETA_1->SetBinContent(4,0.0);
  S9_sdETA_1->SetBinContent(5,0.0);
  S9_sdETA_1->SetBinContent(6,0.0);
  S9_sdETA_1->SetBinContent(7,0.0);
  S9_sdETA_1->SetBinContent(8,0.0);
  S9_sdETA_1->SetBinContent(9,0.0);
  S9_sdETA_1->SetBinContent(10,0.0);
  S9_sdETA_1->SetBinContent(11,0.0);
  S9_sdETA_1->SetBinContent(12,0.0);
  S9_sdETA_1->SetBinContent(13,0.0);
  S9_sdETA_1->SetBinContent(14,0.0);
  S9_sdETA_1->SetBinContent(15,0.0);
  S9_sdETA_1->SetBinContent(16,0.0);
  S9_sdETA_1->SetBinContent(17,0.0);
  S9_sdETA_1->SetBinContent(18,0.0);
  S9_sdETA_1->SetBinContent(19,0.0);
  S9_sdETA_1->SetBinContent(20,0.0);
  S9_sdETA_1->SetBinContent(21,0.0);
  S9_sdETA_1->SetBinContent(22,0.0);
  S9_sdETA_1->SetBinContent(23,0.0);
  S9_sdETA_1->SetBinContent(24,0.0);
  S9_sdETA_1->SetBinContent(25,0.0);
  S9_sdETA_1->SetBinContent(26,0.0);
  S9_sdETA_1->SetBinContent(27,141.959876369);
  S9_sdETA_1->SetBinContent(28,141.959876369);
  S9_sdETA_1->SetBinContent(29,0.0);
  S9_sdETA_1->SetBinContent(30,283.919808294);
  S9_sdETA_1->SetBinContent(31,425.879684664);
  S9_sdETA_1->SetBinContent(32,567.839505477);
  S9_sdETA_1->SetBinContent(33,283.919808294);
  S9_sdETA_1->SetBinContent(34,425.879684664);
  S9_sdETA_1->SetBinContent(35,283.919808294);
  S9_sdETA_1->SetBinContent(36,567.839505477);
  S9_sdETA_1->SetBinContent(37,141.959876369);
  S9_sdETA_1->SetBinContent(38,425.879684664);
  S9_sdETA_1->SetBinContent(39,283.919808294);
  S9_sdETA_1->SetBinContent(40,141.959876369);
  S9_sdETA_1->SetBinContent(41,425.879684664);
  S9_sdETA_1->SetBinContent(42,425.879684664);
  S9_sdETA_1->SetBinContent(43,0.0);
  S9_sdETA_1->SetBinContent(44,0.0);
  S9_sdETA_1->SetBinContent(45,0.0);
  S9_sdETA_1->SetBinContent(46,0.0);
  S9_sdETA_1->SetBinContent(47,0.0);
  S9_sdETA_1->SetBinContent(48,0.0);
  S9_sdETA_1->SetBinContent(49,0.0);
  S9_sdETA_1->SetBinContent(50,0.0);
  S9_sdETA_1->SetBinContent(51,0.0);
  S9_sdETA_1->SetBinContent(52,0.0);
  S9_sdETA_1->SetBinContent(53,0.0);
  S9_sdETA_1->SetBinContent(54,0.0);
  S9_sdETA_1->SetBinContent(55,0.0);
  S9_sdETA_1->SetBinContent(56,0.0);
  S9_sdETA_1->SetBinContent(57,0.0);
  S9_sdETA_1->SetBinContent(58,0.0);
  S9_sdETA_1->SetBinContent(59,141.959876369);
  S9_sdETA_1->SetBinContent(60,567.839505477);
  S9_sdETA_1->SetBinContent(61,425.879684664);
  S9_sdETA_1->SetBinContent(62,425.879684664);
  S9_sdETA_1->SetBinContent(63,425.879684664);
  S9_sdETA_1->SetBinContent(64,425.879684664);
  S9_sdETA_1->SetBinContent(65,283.919808294);
  S9_sdETA_1->SetBinContent(66,425.879684664);
  S9_sdETA_1->SetBinContent(67,141.959876369);
  S9_sdETA_1->SetBinContent(68,567.839505477);
  S9_sdETA_1->SetBinContent(69,567.839505477);
  S9_sdETA_1->SetBinContent(70,141.959876369);
  S9_sdETA_1->SetBinContent(71,141.959876369);
  S9_sdETA_1->SetBinContent(72,141.959876369);
  S9_sdETA_1->SetBinContent(73,0.0);
  S9_sdETA_1->SetBinContent(74,0.0);
  S9_sdETA_1->SetBinContent(75,283.919808294);
  S9_sdETA_1->SetBinContent(76,0.0);
  S9_sdETA_1->SetBinContent(77,0.0);
  S9_sdETA_1->SetBinContent(78,0.0);
  S9_sdETA_1->SetBinContent(79,0.0);
  S9_sdETA_1->SetBinContent(80,0.0);
  S9_sdETA_1->SetBinContent(81,0.0);
  S9_sdETA_1->SetBinContent(82,0.0);
  S9_sdETA_1->SetBinContent(83,0.0);
  S9_sdETA_1->SetBinContent(84,0.0);
  S9_sdETA_1->SetBinContent(85,0.0);
  S9_sdETA_1->SetBinContent(86,0.0);
  S9_sdETA_1->SetBinContent(87,0.0);
  S9_sdETA_1->SetBinContent(88,0.0);
  S9_sdETA_1->SetBinContent(89,0.0);
  S9_sdETA_1->SetBinContent(90,0.0);
  S9_sdETA_1->SetBinContent(91,0.0);
  S9_sdETA_1->SetBinContent(92,0.0);
  S9_sdETA_1->SetBinContent(93,0.0);
  S9_sdETA_1->SetBinContent(94,0.0);
  S9_sdETA_1->SetBinContent(95,0.0);
  S9_sdETA_1->SetBinContent(96,0.0);
  S9_sdETA_1->SetBinContent(97,0.0);
  S9_sdETA_1->SetBinContent(98,0.0);
  S9_sdETA_1->SetBinContent(99,0.0);
  S9_sdETA_1->SetBinContent(100,0.0);
  S9_sdETA_1->SetBinContent(101,0.0); // overflow
  S9_sdETA_1->SetEntries(71);
  // Style
  S9_sdETA_1->SetLineColor(46);
  S9_sdETA_1->SetLineStyle(1);
  S9_sdETA_1->SetLineWidth(1);
  S9_sdETA_1->SetFillColor(46);
  S9_sdETA_1->SetFillStyle(1001);

  // Creating a new THStack
  THStack* stack = new THStack("mystack_18","mystack");
  stack->Add(S9_sdETA_0);
  stack->Add(S9_sdETA_1);
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
  stack->GetXaxis()->SetTitle("#Delta#eta ( j_{1} , j_{2} ) ");

  // Finalizing the TCanvas
  canvas->SetLogx(0);
  canvas->SetLogy(0);

  // Creating a TLegend
  TLegend* legend = new TLegend(.73,.5,.97,.95);
  legend->AddEntry(S9_sdETA_0,"signal1TeV");
  legend->AddEntry(S9_sdETA_1,"signal4TeV");
  legend->SetFillColor(0);
  legend->SetTextSize(0.05);
  legend->SetTextFont(22);
  legend->SetY1(TMath::Max(0.15,0.97-0.10*legend->GetListOfPrimitives()->GetSize()));
  legend->Draw();

  // Saving the image
  canvas->SaveAs("../../HTML/MadAnalysis5job_0/selection_8.png");
  canvas->SaveAs("../../PDF/MadAnalysis5job_0/selection_8.png");
  canvas->SaveAs("../../DVI/MadAnalysis5job_0/selection_8.eps");

}
