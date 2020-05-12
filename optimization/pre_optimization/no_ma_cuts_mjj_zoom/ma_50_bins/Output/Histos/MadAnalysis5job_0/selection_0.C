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
  TH1F* S1_M_0 = new TH1F("S1_M_0","S1_M_0",50,0.0,400.0);
  // Content
  S1_M_0->SetBinContent(0,0.0); // underflow
  S1_M_0->SetBinContent(1,0.0);
  S1_M_0->SetBinContent(2,0.0);
  S1_M_0->SetBinContent(3,0.0);
  S1_M_0->SetBinContent(4,0.0);
  S1_M_0->SetBinContent(5,12.5760774243);
  S1_M_0->SetBinContent(6,25.1521588486);
  S1_M_0->SetBinContent(7,15.7200977804);
  S1_M_0->SetBinContent(8,18.8641181365);
  S1_M_0->SetBinContent(9,22.0081384925);
  S1_M_0->SetBinContent(10,84.888529614);
  S1_M_0->SetBinContent(11,125.760774243);
  S1_M_0->SetBinContent(12,69.1684478337);
  S1_M_0->SetBinContent(13,69.1684478337);
  S1_M_0->SetBinContent(14,69.1684478337);
  S1_M_0->SetBinContent(15,106.896652107);
  S1_M_0->SetBinContent(16,94.3206106823);
  S1_M_0->SetBinContent(17,84.888529614);
  S1_M_0->SetBinContent(18,103.75265175);
  S1_M_0->SetBinContent(19,106.896652107);
  S1_M_0->SetBinContent(20,113.184692819);
  S1_M_0->SetBinContent(21,135.192855311);
  S1_M_0->SetBinContent(22,125.760774243);
  S1_M_0->SetBinContent(23,144.624896379);
  S1_M_0->SetBinContent(24,94.3206106823);
  S1_M_0->SetBinContent(25,144.624896379);
  S1_M_0->SetBinContent(26,147.768936736);
  S1_M_0->SetBinContent(27,138.336855667);
  S1_M_0->SetBinContent(28,119.472733531);
  S1_M_0->SetBinContent(29,160.34501816);
  S1_M_0->SetBinContent(30,207.505303501);
  S1_M_0->SetBinContent(31,150.912937092);
  S1_M_0->SetBinContent(32,141.480896023);
  S1_M_0->SetBinContent(33,188.641181365);
  S1_M_0->SetBinContent(34,157.200977804);
  S1_M_0->SetBinContent(35,132.048814955);
  S1_M_0->SetBinContent(36,172.921099584);
  S1_M_0->SetBinContent(37,176.06509994);
  S1_M_0->SetBinContent(38,194.929222077);
  S1_M_0->SetBinContent(39,147.768936736);
  S1_M_0->SetBinContent(40,242.089507418);
  S1_M_0->SetBinContent(41,157.200977804);
  S1_M_0->SetBinContent(42,135.192855311);
  S1_M_0->SetBinContent(43,166.633058872);
  S1_M_0->SetBinContent(44,191.785221721);
  S1_M_0->SetBinContent(45,135.192855311);
  S1_M_0->SetBinContent(46,176.06509994);
  S1_M_0->SetBinContent(47,223.225385281);
  S1_M_0->SetBinContent(48,154.056977448);
  S1_M_0->SetBinContent(49,172.921099584);
  S1_M_0->SetBinContent(50,157.200977804);
  S1_M_0->SetBinContent(51,25523.1508906); // overflow
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
