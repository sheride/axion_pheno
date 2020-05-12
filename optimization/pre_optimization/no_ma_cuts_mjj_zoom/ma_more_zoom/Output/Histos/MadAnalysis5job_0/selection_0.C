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
  TH1F* S1_M_0 = new TH1F("S1_M_0","S1_M_0",30,50.0,110.0);
  // Content
  S1_M_0->SetBinContent(0,40.8722412923); // underflow
  S1_M_0->SetBinContent(1,0.0);
  S1_M_0->SetBinContent(2,9.43206029823);
  S1_M_0->SetBinContent(3,3.14401929941);
  S1_M_0->SetBinContent(4,6.28804019882);
  S1_M_0->SetBinContent(5,9.43206029823);
  S1_M_0->SetBinContent(6,0.0);
  S1_M_0->SetBinContent(7,3.14401929941);
  S1_M_0->SetBinContent(8,9.43206029823);
  S1_M_0->SetBinContent(9,3.14401929941);
  S1_M_0->SetBinContent(10,6.28804019882);
  S1_M_0->SetBinContent(11,3.14401929941);
  S1_M_0->SetBinContent(12,3.14401929941);
  S1_M_0->SetBinContent(13,3.14401929941);
  S1_M_0->SetBinContent(14,22.0081366959);
  S1_M_0->SetBinContent(15,56.5923617894);
  S1_M_0->SetBinContent(16,66.0244020876);
  S1_M_0->SetBinContent(17,18.8641165965);
  S1_M_0->SetBinContent(18,15.720096497);
  S1_M_0->SetBinContent(19,25.1521567953);
  S1_M_0->SetBinContent(20,18.8641165965);
  S1_M_0->SetBinContent(21,28.2961768947);
  S1_M_0->SetBinContent(22,9.43206029823);
  S1_M_0->SetBinContent(23,12.5760763976);
  S1_M_0->SetBinContent(24,15.720096497);
  S1_M_0->SetBinContent(25,22.0081366959);
  S1_M_0->SetBinContent(26,6.28804019882);
  S1_M_0->SetBinContent(27,25.1521567953);
  S1_M_0->SetBinContent(28,3.14401929941);
  S1_M_0->SetBinContent(29,15.720096497);
  S1_M_0->SetBinContent(30,22.0081366959);
  S1_M_0->SetBinContent(31,30952.8729787); // overflow
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
