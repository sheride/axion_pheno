void selection_5()
{

  // ROOT version
  Int_t root_version = gROOT->GetVersionInt();

  // Creating a new TCanvas
  TCanvas* canvas = new TCanvas("canvas_plotflow_tempo11","canvas_plotflow_tempo11",0,0,700,500);
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
  TH1F* S6_PHI_0 = new TH1F("S6_PHI_0","S6_PHI_0",64,-3.2,3.2);
  // Content
  S6_PHI_0->SetBinContent(0,0.0); // underflow
  S6_PHI_0->SetBinContent(1,26.01514117);
  S6_PHI_0->SetBinContent(2,52.7735623733);
  S6_PHI_0->SetBinContent(3,59.8348426909);
  S6_PHI_0->SetBinContent(4,59.8348426909);
  S6_PHI_0->SetBinContent(5,56.1183625238);
  S6_PHI_0->SetBinContent(6,55.7467225071);
  S6_PHI_0->SetBinContent(7,56.8616825572);
  S6_PHI_0->SetBinContent(8,66.152802975);
  S6_PHI_0->SetBinContent(9,56.8616825572);
  S6_PHI_0->SetBinContent(10,55.0034424736);
  S6_PHI_0->SetBinContent(11,54.6318024569);
  S6_PHI_0->SetBinContent(12,56.8616825572);
  S6_PHI_0->SetBinContent(13,60.5781227243);
  S6_PHI_0->SetBinContent(14,61.3214027578);
  S6_PHI_0->SetBinContent(15,55.0034424736);
  S6_PHI_0->SetBinContent(16,61.3214027578);
  S6_PHI_0->SetBinContent(17,62.0646827912);
  S6_PHI_0->SetBinContent(18,63.9229228748);
  S6_PHI_0->SetBinContent(19,57.6049625906);
  S6_PHI_0->SetBinContent(20,62.8080028246);
  S6_PHI_0->SetBinContent(21,55.7467225071);
  S6_PHI_0->SetBinContent(22,54.6318024569);
  S6_PHI_0->SetBinContent(23,58.348242624);
  S6_PHI_0->SetBinContent(24,61.6930427745);
  S6_PHI_0->SetBinContent(25,53.5168424068);
  S6_PHI_0->SetBinContent(26,57.6049625906);
  S6_PHI_0->SetBinContent(27,62.0646827912);
  S6_PHI_0->SetBinContent(28,51.2870023065);
  S6_PHI_0->SetBinContent(29,60.5781227243);
  S6_PHI_0->SetBinContent(30,62.0646827912);
  S6_PHI_0->SetBinContent(31,61.6930427745);
  S6_PHI_0->SetBinContent(32,65.7811229583);
  S6_PHI_0->SetBinContent(33,55.0034424736);
  S6_PHI_0->SetBinContent(34,63.1796428413);
  S6_PHI_0->SetBinContent(35,60.5781227243);
  S6_PHI_0->SetBinContent(36,56.4900025405);
  S6_PHI_0->SetBinContent(37,55.0034424736);
  S6_PHI_0->SetBinContent(38,62.8080028246);
  S6_PHI_0->SetBinContent(39,52.4019223566);
  S6_PHI_0->SetBinContent(40,56.1183625238);
  S6_PHI_0->SetBinContent(41,46.8272421059);
  S6_PHI_0->SetBinContent(42,60.949762741);
  S6_PHI_0->SetBinContent(43,61.3214027578);
  S6_PHI_0->SetBinContent(44,56.4900025405);
  S6_PHI_0->SetBinContent(45,62.8080028246);
  S6_PHI_0->SetBinContent(46,50.5437222731);
  S6_PHI_0->SetBinContent(47,59.4631626742);
  S6_PHI_0->SetBinContent(48,63.1796428413);
  S6_PHI_0->SetBinContent(49,61.3214027578);
  S6_PHI_0->SetBinContent(50,64.2945628915);
  S6_PHI_0->SetBinContent(51,63.1796428413);
  S6_PHI_0->SetBinContent(52,60.949762741);
  S6_PHI_0->SetBinContent(53,58.348242624);
  S6_PHI_0->SetBinContent(54,61.3214027578);
  S6_PHI_0->SetBinContent(55,61.3214027578);
  S6_PHI_0->SetBinContent(56,55.7467225071);
  S6_PHI_0->SetBinContent(57,61.3214027578);
  S6_PHI_0->SetBinContent(58,62.0646827912);
  S6_PHI_0->SetBinContent(59,63.1796428413);
  S6_PHI_0->SetBinContent(60,62.4363228079);
  S6_PHI_0->SetBinContent(61,60.2064827076);
  S6_PHI_0->SetBinContent(62,59.4631626742);
  S6_PHI_0->SetBinContent(63,69.4976031255);
  S6_PHI_0->SetBinContent(64,21.9270489861);
  S6_PHI_0->SetBinContent(65,0.0); // overflow
  S6_PHI_0->SetEntries(9999);
  // Style
  S6_PHI_0->SetLineColor(9);
  S6_PHI_0->SetLineStyle(1);
  S6_PHI_0->SetLineWidth(1);
  S6_PHI_0->SetFillColor(9);
  S6_PHI_0->SetFillStyle(1001);

  // Creating a new THStack
  THStack* stack = new THStack("mystack_12","mystack");
  stack->Add(S6_PHI_0);
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
  stack->GetXaxis()->SetTitle("#phi [ j_{2} ] ");

  // Finalizing the TCanvas
  canvas->SetLogx(0);
  canvas->SetLogy(0);

  // Saving the image
  canvas->SaveAs("../../HTML/MadAnalysis5job_0/selection_5.png");
  canvas->SaveAs("../../PDF/MadAnalysis5job_0/selection_5.png");
  canvas->SaveAs("../../DVI/MadAnalysis5job_0/selection_5.eps");

}
