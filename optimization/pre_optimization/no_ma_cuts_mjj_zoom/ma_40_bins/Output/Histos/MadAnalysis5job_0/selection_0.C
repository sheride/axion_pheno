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
  TH1F* S1_M_0 = new TH1F("S1_M_0","S1_M_0",40,0.0,400.0);
  // Content
  S1_M_0->SetBinContent(0,0.0); // underflow
  S1_M_0->SetBinContent(1,0.0);
  S1_M_0->SetBinContent(2,0.0);
  S1_M_0->SetBinContent(3,0.0);
  S1_M_0->SetBinContent(4,12.5760774307);
  S1_M_0->SetBinContent(5,28.2961792191);
  S1_M_0->SetBinContent(6,28.2961792191);
  S1_M_0->SetBinContent(7,22.0081385037);
  S1_M_0->SetBinContent(8,88.0325700149);
  S1_M_0->SetBinContent(9,144.624896453);
  S1_M_0->SetBinContent(10,88.0325700149);
  S1_M_0->SetBinContent(11,72.3124482265);
  S1_M_0->SetBinContent(12,135.19285538);
  S1_M_0->SetBinContent(13,119.472733592);
  S1_M_0->SetBinContent(14,116.328733234);
  S1_M_0->SetBinContent(15,138.336855738);
  S1_M_0->SetBinContent(16,128.904814665);
  S1_M_0->SetBinContent(17,163.489018599);
  S1_M_0->SetBinContent(18,163.489018599);
  S1_M_0->SetBinContent(19,150.912937168);
  S1_M_0->SetBinContent(20,166.633058957);
  S1_M_0->SetBinContent(21,169.777059314);
  S1_M_0->SetBinContent(22,176.06510003);
  S1_M_0->SetBinContent(23,169.777059314);
  S1_M_0->SetBinContent(24,257.809629329);
  S1_M_0->SetBinContent(25,182.353140745);
  S1_M_0->SetBinContent(26,188.641181461);
  S1_M_0->SetBinContent(27,235.801466826);
  S1_M_0->SetBinContent(28,163.489018599);
  S1_M_0->SetBinContent(29,216.93734468);
  S1_M_0->SetBinContent(30,220.081385037);
  S1_M_0->SetBinContent(31,229.51342611);
  S1_M_0->SetBinContent(32,267.241670402);
  S1_M_0->SetBinContent(33,185.497181103);
  S1_M_0->SetBinContent(34,191.785221818);
  S1_M_0->SetBinContent(35,242.089507541);
  S1_M_0->SetBinContent(36,166.633058957);
  S1_M_0->SetBinContent(37,235.801466826);
  S1_M_0->SetBinContent(38,251.521588614);
  S1_M_0->SetBinContent(39,201.217262891);
  S1_M_0->SetBinContent(40,194.929222176);
  S1_M_0->SetBinContent(41,25523.1509036); // overflow
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
