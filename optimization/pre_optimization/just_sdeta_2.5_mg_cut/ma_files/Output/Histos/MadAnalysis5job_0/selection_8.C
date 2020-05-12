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
  S9_sdETA_0->SetBinContent(20,0.74328964206);
  S9_sdETA_0->SetBinContent(21,0.37164486103);
  S9_sdETA_0->SetBinContent(22,1.11493446309);
  S9_sdETA_0->SetBinContent(23,2.60151414721);
  S9_sdETA_0->SetBinContent(24,2.60151414721);
  S9_sdETA_0->SetBinContent(25,8.17618846266);
  S9_sdETA_0->SetBinContent(26,7.80454044163);
  S9_sdETA_0->SetBinContent(27,12.264280694);
  S9_sdETA_0->SetBinContent(28,15.2374408622);
  S9_sdETA_0->SetBinContent(29,18.5822450515);
  S9_sdETA_0->SetBinContent(30,18.5822450515);
  S9_sdETA_0->SetBinContent(31,24.900205409);
  S9_sdETA_0->SetBinContent(32,43.8540824816);
  S9_sdETA_0->SetBinContent(33,43.8540824816);
  S9_sdETA_0->SetBinContent(34,58.7198833228);
  S9_sdETA_0->SetBinContent(35,70.9841640167);
  S9_sdETA_0->SetBinContent(36,93.6545252996);
  S9_sdETA_0->SetBinContent(37,121.527886877);
  S9_sdETA_0->SetBinContent(38,156.462488854);
  S9_sdETA_0->SetBinContent(39,216.29733224);
  S9_sdETA_0->SetBinContent(40,280.591895878);
  S9_sdETA_0->SetBinContent(41,353.805940021);
  S9_sdETA_0->SetBinContent(42,307.350297392);
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
  S9_sdETA_0->SetBinContent(59,301.403977055);
  S9_sdETA_0->SetBinContent(60,370.901580988);
  S9_sdETA_0->SetBinContent(61,266.469375079);
  S9_sdETA_0->SetBinContent(62,213.695812092);
  S9_sdETA_0->SetBinContent(63,152.002768601);
  S9_sdETA_0->SetBinContent(64,126.35924715);
  S9_sdETA_0->SetBinContent(65,90.6813651313);
  S9_sdETA_0->SetBinContent(66,78.4170844374);
  S9_sdETA_0->SetBinContent(67,57.6049632597);
  S9_sdETA_0->SetBinContent(68,43.1108024395);
  S9_sdETA_0->SetBinContent(69,36.421198061);
  S9_sdETA_0->SetBinContent(70,30.8465257455);
  S9_sdETA_0->SetBinContent(71,19.6971771146);
  S9_sdETA_0->SetBinContent(72,15.9807289043);
  S9_sdETA_0->SetBinContent(73,10.4060565888);
  S9_sdETA_0->SetBinContent(74,10.4060565888);
  S9_sdETA_0->SetBinContent(75,8.91947650472);
  S9_sdETA_0->SetBinContent(76,8.17618846266);
  S9_sdETA_0->SetBinContent(77,5.94631633648);
  S9_sdETA_0->SetBinContent(78,3.34480378927);
  S9_sdETA_0->SetBinContent(79,2.22986932618);
  S9_sdETA_0->SetBinContent(80,1.48657968412);
  S9_sdETA_0->SetBinContent(81,1.48657968412);
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
