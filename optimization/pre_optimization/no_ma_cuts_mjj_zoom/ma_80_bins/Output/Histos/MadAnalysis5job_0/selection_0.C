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
  TH1F* S1_M_0 = new TH1F("S1_M_0","S1_M_0",80,0.0,400.0);
  // Content
  S1_M_0->SetBinContent(0,0.0); // underflow
  S1_M_0->SetBinContent(1,0.0);
  S1_M_0->SetBinContent(2,0.0);
  S1_M_0->SetBinContent(3,0.0);
  S1_M_0->SetBinContent(4,0.0);
  S1_M_0->SetBinContent(5,0.0);
  S1_M_0->SetBinContent(6,0.0);
  S1_M_0->SetBinContent(7,3.14401955096);
  S1_M_0->SetBinContent(8,9.43206105287);
  S1_M_0->SetBinContent(9,15.7200977548);
  S1_M_0->SetBinContent(10,12.5760774038);
  S1_M_0->SetBinContent(11,12.5760774038);
  S1_M_0->SetBinContent(12,15.7200977548);
  S1_M_0->SetBinContent(13,9.43206105287);
  S1_M_0->SetBinContent(14,12.5760774038);
  S1_M_0->SetBinContent(15,6.28804070191);
  S1_M_0->SetBinContent(16,81.7445291248);
  S1_M_0->SetBinContent(17,100.608611231);
  S1_M_0->SetBinContent(18,44.0162849134);
  S1_M_0->SetBinContent(19,44.0162849134);
  S1_M_0->SetBinContent(20,44.0162849134);
  S1_M_0->SetBinContent(21,31.4401955096);
  S1_M_0->SetBinContent(22,40.8722445624);
  S1_M_0->SetBinContent(23,84.8885294758);
  S1_M_0->SetBinContent(24,50.3043256153);
  S1_M_0->SetBinContent(25,47.1602852643);
  S1_M_0->SetBinContent(26,72.312448072);
  S1_M_0->SetBinContent(27,53.4483259662);
  S1_M_0->SetBinContent(28,62.8804070191);
  S1_M_0->SetBinContent(29,56.5923663172);
  S1_M_0->SetBinContent(30,81.7445291248);
  S1_M_0->SetBinContent(31,78.6004887739);
  S1_M_0->SetBinContent(32,50.3043256153);
  S1_M_0->SetBinContent(33,66.0244073701);
  S1_M_0->SetBinContent(34,97.4646108796);
  S1_M_0->SetBinContent(35,69.168447721);
  S1_M_0->SetBinContent(36,94.3206105287);
  S1_M_0->SetBinContent(37,94.3206105287);
  S1_M_0->SetBinContent(38,56.5923663172);
  S1_M_0->SetBinContent(39,78.6004887739);
  S1_M_0->SetBinContent(40,88.0325698267);
  S1_M_0->SetBinContent(41,81.7445291248);
  S1_M_0->SetBinContent(42,88.0325698267);
  S1_M_0->SetBinContent(43,91.1765701777);
  S1_M_0->SetBinContent(44,84.8885294758);
  S1_M_0->SetBinContent(45,88.0325698267);
  S1_M_0->SetBinContent(46,81.7445291248);
  S1_M_0->SetBinContent(47,144.624896144);
  S1_M_0->SetBinContent(48,113.184692634);
  S1_M_0->SetBinContent(49,106.896651932);
  S1_M_0->SetBinContent(50,75.4564884229);
  S1_M_0->SetBinContent(51,97.4646108796);
  S1_M_0->SetBinContent(52,91.1765701777);
  S1_M_0->SetBinContent(53,122.616773687);
  S1_M_0->SetBinContent(54,113.184692634);
  S1_M_0->SetBinContent(55,62.8804070191);
  S1_M_0->SetBinContent(56,100.608611231);
  S1_M_0->SetBinContent(57,116.328732985);
  S1_M_0->SetBinContent(58,100.608611231);
  S1_M_0->SetBinContent(59,122.616773687);
  S1_M_0->SetBinContent(60,97.4646108796);
  S1_M_0->SetBinContent(61,116.328732985);
  S1_M_0->SetBinContent(62,113.184692634);
  S1_M_0->SetBinContent(63,116.328732985);
  S1_M_0->SetBinContent(64,150.912936846);
  S1_M_0->SetBinContent(65,106.896651932);
  S1_M_0->SetBinContent(66,78.6004887739);
  S1_M_0->SetBinContent(67,81.7445291248);
  S1_M_0->SetBinContent(68,110.040692283);
  S1_M_0->SetBinContent(69,100.608611231);
  S1_M_0->SetBinContent(70,141.480895793);
  S1_M_0->SetBinContent(71,81.7445291248);
  S1_M_0->SetBinContent(72,84.8885294758);
  S1_M_0->SetBinContent(73,106.896651932);
  S1_M_0->SetBinContent(74,128.904814389);
  S1_M_0->SetBinContent(75,138.336855442);
  S1_M_0->SetBinContent(76,113.184692634);
  S1_M_0->SetBinContent(77,84.8885294758);
  S1_M_0->SetBinContent(78,116.328732985);
  S1_M_0->SetBinContent(79,97.4646108796);
  S1_M_0->SetBinContent(80,97.4646108796);
  S1_M_0->SetBinContent(81,25523.1508491); // overflow
  S1_M_0->SetEntries(9999);
  // Style
  S1_M_0->SetLineColor(9);
  S1_M_0->SetLineStyle(1);
  S1_M_0->SetLineWidth(1);
  S1_M_0->SetFillColor(9);
  S1_M_0->SetFillStyle(1001);

  // Creating a new THStack
  THStack* stack = new THStack("mystack_2","mystack");
  stack->Add(S1_M_0);
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
  stack->GetXaxis()->SetTitle("M [ j_{1} , j_{2} ]   ( GeV ) ");

  // Finalizing the TCanvas
  canvas->SetLogx(0);
  canvas->SetLogy(0);

  // Saving the image
  canvas->SaveAs("../../HTML/MadAnalysis5job_0/selection_0.png");
  canvas->SaveAs("../../PDF/MadAnalysis5job_0/selection_0.png");
  canvas->SaveAs("../../DVI/MadAnalysis5job_0/selection_0.eps");

}
