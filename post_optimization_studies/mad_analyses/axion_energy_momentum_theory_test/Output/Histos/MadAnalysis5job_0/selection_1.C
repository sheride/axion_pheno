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
  TH1F* S2_P_0 = new TH1F("S2_P_0","S2_P_0",100,0.0,1000.0);
  // Content
  S2_P_0->SetBinContent(0,0.0); // underflow
  S2_P_0->SetBinContent(1,0.0);
  S2_P_0->SetBinContent(2,0.0);
  S2_P_0->SetBinContent(3,0.0);
  S2_P_0->SetBinContent(4,0.0);
  S2_P_0->SetBinContent(5,0.0);
  S2_P_0->SetBinContent(6,0.0);
  S2_P_0->SetBinContent(7,0.0);
  S2_P_0->SetBinContent(8,0.0);
  S2_P_0->SetBinContent(9,3.83713442454);
  S2_P_0->SetBinContent(10,3.83713442454);
  S2_P_0->SetBinContent(11,0.0);
  S2_P_0->SetBinContent(12,3.83713442454);
  S2_P_0->SetBinContent(13,0.0);
  S2_P_0->SetBinContent(14,3.83713442454);
  S2_P_0->SetBinContent(15,0.0);
  S2_P_0->SetBinContent(16,11.5114040736);
  S2_P_0->SetBinContent(17,0.0);
  S2_P_0->SetBinContent(18,0.0);
  S2_P_0->SetBinContent(19,7.67426804909);
  S2_P_0->SetBinContent(20,0.0);
  S2_P_0->SetBinContent(21,7.67426804909);
  S2_P_0->SetBinContent(22,7.67426804909);
  S2_P_0->SetBinContent(23,3.83713442454);
  S2_P_0->SetBinContent(24,3.83713442454);
  S2_P_0->SetBinContent(25,3.83713442454);
  S2_P_0->SetBinContent(26,7.67426804909);
  S2_P_0->SetBinContent(27,19.1856721227);
  S2_P_0->SetBinContent(28,26.8599401718);
  S2_P_0->SetBinContent(29,7.67426804909);
  S2_P_0->SetBinContent(30,7.67426804909);
  S2_P_0->SetBinContent(31,11.5114040736);
  S2_P_0->SetBinContent(32,19.1856721227);
  S2_P_0->SetBinContent(33,15.3485360982);
  S2_P_0->SetBinContent(34,23.0228041473);
  S2_P_0->SetBinContent(35,11.5114040736);
  S2_P_0->SetBinContent(36,19.1856721227);
  S2_P_0->SetBinContent(37,19.1856721227);
  S2_P_0->SetBinContent(38,19.1856721227);
  S2_P_0->SetBinContent(39,15.3485360982);
  S2_P_0->SetBinContent(40,23.0228041473);
  S2_P_0->SetBinContent(41,7.67426804909);
  S2_P_0->SetBinContent(42,7.67426804909);
  S2_P_0->SetBinContent(43,23.0228041473);
  S2_P_0->SetBinContent(44,11.5114040736);
  S2_P_0->SetBinContent(45,7.67426804909);
  S2_P_0->SetBinContent(46,11.5114040736);
  S2_P_0->SetBinContent(47,38.3713442454);
  S2_P_0->SetBinContent(48,19.1856721227);
  S2_P_0->SetBinContent(49,23.0228041473);
  S2_P_0->SetBinContent(50,19.1856721227);
  S2_P_0->SetBinContent(51,19.1856721227);
  S2_P_0->SetBinContent(52,19.1856721227);
  S2_P_0->SetBinContent(53,7.67426804909);
  S2_P_0->SetBinContent(54,15.3485360982);
  S2_P_0->SetBinContent(55,34.5342082209);
  S2_P_0->SetBinContent(56,15.3485360982);
  S2_P_0->SetBinContent(57,15.3485360982);
  S2_P_0->SetBinContent(58,15.3485360982);
  S2_P_0->SetBinContent(59,19.1856721227);
  S2_P_0->SetBinContent(60,7.67426804909);
  S2_P_0->SetBinContent(61,11.5114040736);
  S2_P_0->SetBinContent(62,26.8599401718);
  S2_P_0->SetBinContent(63,19.1856721227);
  S2_P_0->SetBinContent(64,11.5114040736);
  S2_P_0->SetBinContent(65,19.1856721227);
  S2_P_0->SetBinContent(66,23.0228041473);
  S2_P_0->SetBinContent(67,30.6970721964);
  S2_P_0->SetBinContent(68,19.1856721227);
  S2_P_0->SetBinContent(69,23.0228041473);
  S2_P_0->SetBinContent(70,15.3485360982);
  S2_P_0->SetBinContent(71,23.0228041473);
  S2_P_0->SetBinContent(72,11.5114040736);
  S2_P_0->SetBinContent(73,15.3485360982);
  S2_P_0->SetBinContent(74,11.5114040736);
  S2_P_0->SetBinContent(75,19.1856721227);
  S2_P_0->SetBinContent(76,3.83713442454);
  S2_P_0->SetBinContent(77,23.0228041473);
  S2_P_0->SetBinContent(78,23.0228041473);
  S2_P_0->SetBinContent(79,11.5114040736);
  S2_P_0->SetBinContent(80,19.1856721227);
  S2_P_0->SetBinContent(81,46.0456002945);
  S2_P_0->SetBinContent(82,15.3485360982);
  S2_P_0->SetBinContent(83,11.5114040736);
  S2_P_0->SetBinContent(84,19.1856721227);
  S2_P_0->SetBinContent(85,26.8599401718);
  S2_P_0->SetBinContent(86,19.1856721227);
  S2_P_0->SetBinContent(87,15.3485360982);
  S2_P_0->SetBinContent(88,26.8599401718);
  S2_P_0->SetBinContent(89,15.3485360982);
  S2_P_0->SetBinContent(90,23.0228041473);
  S2_P_0->SetBinContent(91,11.5114040736);
  S2_P_0->SetBinContent(92,11.5114040736);
  S2_P_0->SetBinContent(93,11.5114040736);
  S2_P_0->SetBinContent(94,26.8599401718);
  S2_P_0->SetBinContent(95,30.6970721964);
  S2_P_0->SetBinContent(96,15.3485360982);
  S2_P_0->SetBinContent(97,11.5114040736);
  S2_P_0->SetBinContent(98,19.1856721227);
  S2_P_0->SetBinContent(99,7.67426804909);
  S2_P_0->SetBinContent(100,19.1856721227);
  S2_P_0->SetBinContent(101,924.749205915); // overflow
  S2_P_0->SetEntries(603);
  // Style
  S2_P_0->SetLineColor(9);
  S2_P_0->SetLineStyle(1);
  S2_P_0->SetLineWidth(1);
  S2_P_0->SetFillColor(9);
  S2_P_0->SetFillStyle(1001);

  // Creating a new THStack
  THStack* stack = new THStack("mystack_4","mystack");
  stack->Add(S2_P_0);
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
  stack->GetXaxis()->SetTitle("p [ a_{1} a_{2} ] (GeV/c) ");

  // Finalizing the TCanvas
  canvas->SetLogx(0);
  canvas->SetLogy(0);

  // Saving the image
  canvas->SaveAs("../../HTML/MadAnalysis5job_0/selection_1.png");
  canvas->SaveAs("../../PDF/MadAnalysis5job_0/selection_1.png");
  canvas->SaveAs("../../DVI/MadAnalysis5job_0/selection_1.eps");

}
