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
  S9_sdETA_0->SetBinContent(24,3.14401933085);
  S9_sdETA_0->SetBinContent(25,0.0);
  S9_sdETA_0->SetBinContent(26,3.14401933085);
  S9_sdETA_0->SetBinContent(27,3.14401933085);
  S9_sdETA_0->SetBinContent(28,40.8722417011);
  S9_sdETA_0->SetBinContent(29,25.1521570468);
  S9_sdETA_0->SetBinContent(30,18.8641167851);
  S9_sdETA_0->SetBinContent(31,25.1521570468);
  S9_sdETA_0->SetBinContent(32,28.2961771777);
  S9_sdETA_0->SetBinContent(33,56.5923623554);
  S9_sdETA_0->SetBinContent(34,66.0244027479);
  S9_sdETA_0->SetBinContent(35,106.896644449);
  S9_sdETA_0->SetBinContent(36,110.04068458);
  S9_sdETA_0->SetBinContent(37,66.0244027479);
  S9_sdETA_0->SetBinContent(38,144.624886019);
  S9_sdETA_0->SetBinContent(39,201.217248375);
  S9_sdETA_0->SetBinContent(40,279.817731646);
  S9_sdETA_0->SetBinContent(41,386.714416095);
  S9_sdETA_0->SetBinContent(42,525.051221852);
  S9_sdETA_0->SetBinContent(43,631.948026301);
  S9_sdETA_0->SetBinContent(44,974.646040564);
  S9_sdETA_0->SetBinContent(45,1270.18405286);
  S9_sdETA_0->SetBinContent(46,1619.17006739);
  S9_sdETA_0->SetBinContent(47,1801.52327498);
  S9_sdETA_0->SetBinContent(48,2251.11809369);
  S9_sdETA_0->SetBinContent(49,2455.4793022);
  S9_sdETA_0->SetBinContent(50,2512.07170455);
  S9_sdETA_0->SetBinContent(51,2508.92770442);
  S9_sdETA_0->SetBinContent(52,2392.59889958);
  S9_sdETA_0->SetBinContent(53,2241.6860933);
  S9_sdETA_0->SetBinContent(54,1902.13167917);
  S9_sdETA_0->SetBinContent(55,1550.00166451);
  S9_sdETA_0->SetBinContent(56,1188.43924946);
  S9_sdETA_0->SetBinContent(57,1009.230442);
  S9_sdETA_0->SetBinContent(58,741.988430881);
  S9_sdETA_0->SetBinContent(59,565.923623554);
  S9_sdETA_0->SetBinContent(60,399.290456618);
  S9_sdETA_0->SetBinContent(61,298.681852431);
  S9_sdETA_0->SetBinContent(62,232.657449683);
  S9_sdETA_0->SetBinContent(63,160.345006674);
  S9_sdETA_0->SetBinContent(64,144.624886019);
  S9_sdETA_0->SetBinContent(65,106.896644449);
  S9_sdETA_0->SetBinContent(66,88.0325636639);
  S9_sdETA_0->SetBinContent(67,62.8804026171);
  S9_sdETA_0->SetBinContent(68,44.0162818319);
  S9_sdETA_0->SetBinContent(69,53.4483222245);
  S9_sdETA_0->SetBinContent(70,28.2961771777);
  S9_sdETA_0->SetBinContent(71,31.4401933085);
  S9_sdETA_0->SetBinContent(72,15.7200966543);
  S9_sdETA_0->SetBinContent(73,25.1521570468);
  S9_sdETA_0->SetBinContent(74,6.28804026171);
  S9_sdETA_0->SetBinContent(75,12.5760765234);
  S9_sdETA_0->SetBinContent(76,3.14401933085);
  S9_sdETA_0->SetBinContent(77,12.5760765234);
  S9_sdETA_0->SetBinContent(78,0.0);
  S9_sdETA_0->SetBinContent(79,0.0);
  S9_sdETA_0->SetBinContent(80,0.0);
  S9_sdETA_0->SetBinContent(81,3.14401933085);
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
  S9_sdETA_0->SetEntries(9999);
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
