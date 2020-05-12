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
  TH1F* S1_M_0 = new TH1F("S1_M_0","S1_M_0",20,0.0,400.0);
  // Content
  S1_M_0->SetBinContent(0,0.0); // underflow
  S1_M_0->SetBinContent(1,0.0);
  S1_M_0->SetBinContent(2,12.5760772419);
  S1_M_0->SetBinContent(3,56.5923655885);
  S1_M_0->SetBinContent(4,110.040690866);
  S1_M_0->SetBinContent(5,232.657462975);
  S1_M_0->SetBinContent(6,207.505300491);
  S1_M_0->SetBinContent(7,235.801463285);
  S1_M_0->SetBinContent(8,267.24166639);
  S1_M_0->SetBinContent(9,326.978032289);
  S1_M_0->SetBinContent(10,317.545991358);
  S1_M_0->SetBinContent(11,345.842154152);
  S1_M_0->SetBinContent(12,427.586842224);
  S1_M_0->SetBinContent(13,370.994316636);
  S1_M_0->SetBinContent(14,399.29047943);
  S1_M_0->SetBinContent(15,437.018843155);
  S1_M_0->SetBinContent(16,496.755249054);
  S1_M_0->SetBinContent(17,377.282357257);
  S1_M_0->SetBinContent(18,408.722440361);
  S1_M_0->SetBinContent(19,487.323248123);
  S1_M_0->SetBinContent(20,396.146479119);
  S1_M_0->SetBinContent(21,25523.1505204); // overflow
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
