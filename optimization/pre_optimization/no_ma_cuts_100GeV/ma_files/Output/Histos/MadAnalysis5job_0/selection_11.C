void selection_11()
{

  // ROOT version
  Int_t root_version = gROOT->GetVersionInt();

  // Creating a new TCanvas
  TCanvas* canvas = new TCanvas("canvas_plotflow_tempo23","canvas_plotflow_tempo23",0,0,700,500);
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
  TH1F* S12_TET_0 = new TH1F("S12_TET_0","S12_TET_0",80,0.0,8000.0);
  // Content
  S12_TET_0->SetBinContent(0,0.0); // underflow
  S12_TET_0->SetBinContent(1,3793.39976523);
  S12_TET_0->SetBinContent(2,28662.0560109);
  S12_TET_0->SetBinContent(3,34462.7090597);
  S12_TET_0->SetBinContent(4,32074.2043921);
  S12_TET_0->SetBinContent(5,33780.2785827);
  S12_TET_0->SetBinContent(6,34462.7090597);
  S12_TET_0->SetBinContent(7,26955.9818203);
  S12_TET_0->SetBinContent(8,26273.5513433);
  S12_TET_0->SetBinContent(9,23885.0466757);
  S12_TET_0->SetBinContent(10,14672.2412422);
  S12_TET_0->SetBinContent(11,13989.8107652);
  S12_TET_0->SetBinContent(12,11260.0928609);
  S12_TET_0->SetBinContent(13,10918.8796242);
  S12_TET_0->SetBinContent(14,7847.94447968);
  S12_TET_0->SetBinContent(15,6824.29676248);
  S12_TET_0->SetBinContent(16,5118.22257186);
  S12_TET_0->SetBinContent(17,4777.00933515);
  S12_TET_0->SetBinContent(18,3753.36442042);
  S12_TET_0->SetBinContent(19,3070.93434382);
  S12_TET_0->SetBinContent(20,2047.2894291);
  S12_TET_0->SetBinContent(21,2729.7195057);
  S12_TET_0->SetBinContent(22,1023.64491472);
  S12_TET_0->SetBinContent(23,682.429676248);
  S12_TET_0->SetBinContent(24,3070.93434382);
  S12_TET_0->SetBinContent(25,341.214918195);
  S12_TET_0->SetBinContent(26,1023.64491472);
  S12_TET_0->SetBinContent(27,341.214918195);
  S12_TET_0->SetBinContent(28,1023.64491472);
  S12_TET_0->SetBinContent(29,341.214918195);
  S12_TET_0->SetBinContent(30,0.0);
  S12_TET_0->SetBinContent(31,341.214918195);
  S12_TET_0->SetBinContent(32,0.0);
  S12_TET_0->SetBinContent(33,682.429676248);
  S12_TET_0->SetBinContent(34,0.0);
  S12_TET_0->SetBinContent(35,0.0);
  S12_TET_0->SetBinContent(36,341.214918195);
  S12_TET_0->SetBinContent(37,0.0);
  S12_TET_0->SetBinContent(38,0.0);
  S12_TET_0->SetBinContent(39,341.214918195);
  S12_TET_0->SetBinContent(40,0.0);
  S12_TET_0->SetBinContent(41,0.0);
  S12_TET_0->SetBinContent(42,0.0);
  S12_TET_0->SetBinContent(43,0.0);
  S12_TET_0->SetBinContent(44,0.0);
  S12_TET_0->SetBinContent(45,0.0);
  S12_TET_0->SetBinContent(46,0.0);
  S12_TET_0->SetBinContent(47,0.0);
  S12_TET_0->SetBinContent(48,0.0);
  S12_TET_0->SetBinContent(49,0.0);
  S12_TET_0->SetBinContent(50,0.0);
  S12_TET_0->SetBinContent(51,0.0);
  S12_TET_0->SetBinContent(52,0.0);
  S12_TET_0->SetBinContent(53,0.0);
  S12_TET_0->SetBinContent(54,0.0);
  S12_TET_0->SetBinContent(55,0.0);
  S12_TET_0->SetBinContent(56,0.0);
  S12_TET_0->SetBinContent(57,0.0);
  S12_TET_0->SetBinContent(58,0.0);
  S12_TET_0->SetBinContent(59,0.0);
  S12_TET_0->SetBinContent(60,0.0);
  S12_TET_0->SetBinContent(61,0.0);
  S12_TET_0->SetBinContent(62,0.0);
  S12_TET_0->SetBinContent(63,0.0);
  S12_TET_0->SetBinContent(64,0.0);
  S12_TET_0->SetBinContent(65,0.0);
  S12_TET_0->SetBinContent(66,0.0);
  S12_TET_0->SetBinContent(67,0.0);
  S12_TET_0->SetBinContent(68,0.0);
  S12_TET_0->SetBinContent(69,0.0);
  S12_TET_0->SetBinContent(70,0.0);
  S12_TET_0->SetBinContent(71,0.0);
  S12_TET_0->SetBinContent(72,0.0);
  S12_TET_0->SetBinContent(73,0.0);
  S12_TET_0->SetBinContent(74,0.0);
  S12_TET_0->SetBinContent(75,0.0);
  S12_TET_0->SetBinContent(76,0.0);
  S12_TET_0->SetBinContent(77,0.0);
  S12_TET_0->SetBinContent(78,0.0);
  S12_TET_0->SetBinContent(79,0.0);
  S12_TET_0->SetBinContent(80,0.0);
  S12_TET_0->SetBinContent(81,0.0); // overflow
  S12_TET_0->SetEntries(1000);
  // Style
  S12_TET_0->SetLineColor(9);
  S12_TET_0->SetLineStyle(1);
  S12_TET_0->SetLineWidth(1);
  S12_TET_0->SetFillColor(9);
  S12_TET_0->SetFillStyle(1001);

  // Creating a new THStack
  THStack* stack = new THStack("mystack_24","mystack");
  stack->Add(S12_TET_0);
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
  stack->GetXaxis()->SetTitle("TET");

  // Finalizing the TCanvas
  canvas->SetLogx(0);
  canvas->SetLogy(0);

  // Saving the image
  canvas->SaveAs("../../HTML/MadAnalysis5job_0/selection_11.png");
  canvas->SaveAs("../../PDF/MadAnalysis5job_0/selection_11.png");
  canvas->SaveAs("../../DVI/MadAnalysis5job_0/selection_11.eps");

}
