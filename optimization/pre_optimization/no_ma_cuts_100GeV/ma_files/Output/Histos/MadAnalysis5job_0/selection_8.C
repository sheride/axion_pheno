void selection_8()
{

  // ROOT version
  Int_t root_version = gROOT->GetVersionInt();

  // Creating a new TCanvas
  TCanvas* canvas = new TCanvas("canvas_plotflow_tempo17","canvas_plotflow_tempo17",0,0,700,500);
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
  S9_sdETA_0->SetBinContent(25,0.0);
  S9_sdETA_0->SetBinContent(26,1704.5688044);
  S9_sdETA_0->SetBinContent(27,340.913760881);
  S9_sdETA_0->SetBinContent(28,2045.48248529);
  S9_sdETA_0->SetBinContent(29,681.827361762);
  S9_sdETA_0->SetBinContent(30,1363.65512352);
  S9_sdETA_0->SetBinContent(31,2386.39656617);
  S9_sdETA_0->SetBinContent(32,4431.88105145);
  S9_sdETA_0->SetBinContent(33,3068.22392793);
  S9_sdETA_0->SetBinContent(34,4772.79313233);
  S9_sdETA_0->SetBinContent(35,7500.10177938);
  S9_sdETA_0->SetBinContent(36,11931.9828308);
  S9_sdETA_0->SetBinContent(37,8863.7581029);
  S9_sdETA_0->SetBinContent(38,12954.7230735);
  S9_sdETA_0->SetBinContent(39,17045.688044);
  S9_sdETA_0->SetBinContent(40,15341.1196396);
  S9_sdETA_0->SetBinContent(41,30341.3271984);
  S9_sdETA_0->SetBinContent(42,43296.0502719);
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
  S9_sdETA_0->SetBinContent(59,40227.8095439);
  S9_sdETA_0->SetBinContent(60,35114.1203307);
  S9_sdETA_0->SetBinContent(61,20795.7409337);
  S9_sdETA_0->SetBinContent(62,19432.0846102);
  S9_sdETA_0->SetBinContent(63,10568.3265073);
  S9_sdETA_0->SetBinContent(64,8863.7581029);
  S9_sdETA_0->SetBinContent(65,6818.27361762);
  S9_sdETA_0->SetBinContent(66,7500.10177938);
  S9_sdETA_0->SetBinContent(67,2727.31024705);
  S9_sdETA_0->SetBinContent(68,5454.62129409);
  S9_sdETA_0->SetBinContent(69,3750.05168969);
  S9_sdETA_0->SetBinContent(70,2386.39656617);
  S9_sdETA_0->SetBinContent(71,2045.48248529);
  S9_sdETA_0->SetBinContent(72,1363.65512352);
  S9_sdETA_0->SetBinContent(73,2386.39656617);
  S9_sdETA_0->SetBinContent(74,681.827361762);
  S9_sdETA_0->SetBinContent(75,1022.74144264);
  S9_sdETA_0->SetBinContent(76,681.827361762);
  S9_sdETA_0->SetBinContent(77,340.913760881);
  S9_sdETA_0->SetBinContent(78,340.913760881);
  S9_sdETA_0->SetBinContent(79,0.0);
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

  // Creating a new THStack
  THStack* stack = new THStack("mystack_18","mystack");
  stack->Add(S9_sdETA_0);
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

  // Saving the image
  canvas->SaveAs("../../HTML/MadAnalysis5job_0/selection_8.png");
  canvas->SaveAs("../../PDF/MadAnalysis5job_0/selection_8.png");
  canvas->SaveAs("../../DVI/MadAnalysis5job_0/selection_8.eps");

}
