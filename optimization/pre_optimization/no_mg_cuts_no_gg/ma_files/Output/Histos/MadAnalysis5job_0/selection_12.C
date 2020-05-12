void selection_12()
{

  // ROOT version
  Int_t root_version = gROOT->GetVersionInt();

  // Creating a new TCanvas
  TCanvas* canvas = new TCanvas("canvas_plotflow_tempo25","canvas_plotflow_tempo25",0,0,700,500);
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
  TH1F* S13_THT_0 = new TH1F("S13_THT_0","S13_THT_0",80,0.0,4000.0);
  // Content
  S13_THT_0->SetBinContent(0,0.0); // underflow
  S13_THT_0->SetBinContent(1,8.17647734094);
  S13_THT_0->SetBinContent(2,161.263020047);
  S13_THT_0->SetBinContent(3,216.312877984);
  S13_THT_0->SetBinContent(4,222.794864733);
  S13_THT_0->SetBinContent(5,214.334523902);
  S13_THT_0->SetBinContent(6,197.032210297);
  S13_THT_0->SetBinContent(7,177.074462708);
  S13_THT_0->SetBinContent(8,154.949203988);
  S13_THT_0->SetBinContent(9,134.422186421);
  S13_THT_0->SetBinContent(10,113.9044828);
  S13_THT_0->SetBinContent(11,97.8141813947);
  S13_THT_0->SetBinContent(12,84.1555794005);
  S13_THT_0->SetBinContent(13,72.0609608268);
  S13_THT_0->SetBinContent(14,62.7450561065);
  S13_THT_0->SetBinContent(15,54.0407138744);
  S13_THT_0->SetBinContent(16,45.7302356333);
  S13_THT_0->SetBinContent(17,39.6517386182);
  S13_THT_0->SetBinContent(18,35.0029243184);
  S13_THT_0->SetBinContent(19,30.0295529786);
  S13_THT_0->SetBinContent(20,26.4881788496);
  S13_THT_0->SetBinContent(21,22.9506662107);
  S13_THT_0->SetBinContent(22,20.0674682713);
  S13_THT_0->SetBinContent(23,17.0794544616);
  S13_THT_0->SetBinContent(24,15.0466597654);
  S13_THT_0->SetBinContent(25,12.7875761556);
  S13_THT_0->SetBinContent(26,11.2203548396);
  S13_THT_0->SetBinContent(27,9.79195529039);
  S13_THT_0->SetBinContent(28,8.55450362622);
  S13_THT_0->SetBinContent(29,7.31199524888);
  S13_THT_0->SetBinContent(30,6.51090795061);
  S13_THT_0->SetBinContent(31,5.6404657326);
  S13_THT_0->SetBinContent(32,5.01800632732);
  S13_THT_0->SetBinContent(33,4.17268378168);
  S13_THT_0->SetBinContent(34,3.88459863522);
  S13_THT_0->SetBinContent(35,3.25797753501);
  S13_THT_0->SetBinContent(36,2.88644862647);
  S13_THT_0->SetBinContent(37,2.37787959316);
  S13_THT_0->SetBinContent(38,2.07592825963);
  S13_THT_0->SetBinContent(39,1.86236827229);
  S13_THT_0->SetBinContent(40,1.56746835539);
  S13_THT_0->SetBinContent(41,1.38399521178);
  S13_THT_0->SetBinContent(42,1.25632459688);
  S13_THT_0->SetBinContent(43,1.03796572878);
  S13_THT_0->SetBinContent(44,0.949757063857);
  S13_THT_0->SetBinContent(45,0.74076650641);
  S13_THT_0->SetBinContent(46,0.631570683012);
  S13_THT_0->SetBinContent(47,0.557267379693);
  S13_THT_0->SetBinContent(48,0.448243044828);
  S13_THT_0->SetBinContent(49,0.436527060145);
  S13_THT_0->SetBinContent(50,0.371609456181);
  S13_THT_0->SetBinContent(51,0.341342449546);
  S13_THT_0->SetBinContent(52,0.25308745474);
  S13_THT_0->SetBinContent(53,0.25306506929);
  S13_THT_0->SetBinContent(54,0.227563245316);
  S13_THT_0->SetBinContent(55,0.174121542088);
  S13_THT_0->SetBinContent(56,0.176486165098);
  S13_THT_0->SetBinContent(57,0.118429061852);
  S13_THT_0->SetBinContent(58,0.111486534451);
  S13_THT_0->SetBinContent(59,0.0580393547829);
  S13_THT_0->SetBinContent(60,0.0580673765689);
  S13_THT_0->SetBinContent(61,0.0742807179985);
  S13_THT_0->SetBinContent(62,0.0464392947493);
  S13_THT_0->SetBinContent(63,0.0510597314943);
  S13_THT_0->SetBinContent(64,0.0348351493711);
  S13_THT_0->SetBinContent(65,0.0464062762111);
  S13_THT_0->SetBinContent(66,0.0301832250927);
  S13_THT_0->SetBinContent(67,0.0348406537932);
  S13_THT_0->SetBinContent(68,0.0232250598566);
  S13_THT_0->SetBinContent(69,0.0139462510242);
  S13_THT_0->SetBinContent(70,0.0255424495678);
  S13_THT_0->SetBinContent(71,0.016245008846);
  S13_THT_0->SetBinContent(72,0.00697689306321);
  S13_THT_0->SetBinContent(73,0.0115974057589);
  S13_THT_0->SetBinContent(74,0.009284924857);
  S13_THT_0->SetBinContent(75,0.00928627597877);
  S13_THT_0->SetBinContent(76,0.00928863044838);
  S13_THT_0->SetBinContent(77,0.00464149505728);
  S13_THT_0->SetBinContent(78,0.00696555643195);
  S13_THT_0->SetBinContent(79,0.00232833939398);
  S13_THT_0->SetBinContent(80,0.00232582382908);
  S13_THT_0->SetBinContent(81,0.0185866907674); // overflow
  S13_THT_0->SetEntries(1000000);
  // Style
  S13_THT_0->SetLineColor(9);
  S13_THT_0->SetLineStyle(1);
  S13_THT_0->SetLineWidth(1);
  S13_THT_0->SetFillColor(9);
  S13_THT_0->SetFillStyle(1001);

  // Creating a new THStack
  THStack* stack = new THStack("mystack_26","mystack");
  stack->Add(S13_THT_0);
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
  canvas->SaveAs("../../HTML/MadAnalysis5job_0/selection_12.png");
  canvas->SaveAs("../../PDF/MadAnalysis5job_0/selection_12.png");
  canvas->SaveAs("../../DVI/MadAnalysis5job_0/selection_12.eps");

}
