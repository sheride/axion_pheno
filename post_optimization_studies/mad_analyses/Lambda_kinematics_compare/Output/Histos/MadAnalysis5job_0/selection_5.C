void selection_5()
{

  // ROOT version
  Int_t root_version = gROOT->GetVersionInt();

  // Creating a new TCanvas
  TCanvas* canvas = new TCanvas("canvas_plotflow_tempo11","canvas_plotflow_tempo11",0,0,1000,500);
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
  canvas->SetRightMargin(0.3);
  canvas->SetBottomMargin(0.15);
  canvas->SetTopMargin(0.05);

  // Creating a new TH1F
  TH1F* S6_PHI_0 = new TH1F("S6_PHI_0","S6_PHI_0",64,-3.2,3.2);
  // Content
  S6_PHI_0->SetBinContent(0,0.0); // underflow
  S6_PHI_0->SetBinContent(1,2032.8441017);
  S6_PHI_0->SetBinContent(2,6505.09904545);
  S6_PHI_0->SetBinContent(3,7724.80686647);
  S6_PHI_0->SetBinContent(4,4472.25534374);
  S6_PHI_0->SetBinContent(5,6098.53110511);
  S6_PHI_0->SetBinContent(6,6505.09904545);
  S6_PHI_0->SetBinContent(7,6098.53110511);
  S6_PHI_0->SetBinContent(8,6911.67098579);
  S6_PHI_0->SetBinContent(9,5285.39522442);
  S6_PHI_0->SetBinContent(10,7318.23892613);
  S6_PHI_0->SetBinContent(11,5285.39522442);
  S6_PHI_0->SetBinContent(12,5285.39522442);
  S6_PHI_0->SetBinContent(13,6911.67098579);
  S6_PHI_0->SetBinContent(14,7318.23892613);
  S6_PHI_0->SetBinContent(15,6911.67098579);
  S6_PHI_0->SetBinContent(16,5691.96316476);
  S6_PHI_0->SetBinContent(17,8537.94674715);
  S6_PHI_0->SetBinContent(18,7318.23892613);
  S6_PHI_0->SetBinContent(19,5691.96316476);
  S6_PHI_0->SetBinContent(20,4472.25534374);
  S6_PHI_0->SetBinContent(21,4878.82728408);
  S6_PHI_0->SetBinContent(22,4472.25534374);
  S6_PHI_0->SetBinContent(23,6505.09904545);
  S6_PHI_0->SetBinContent(24,9757.65056817);
  S6_PHI_0->SetBinContent(25,6505.09904545);
  S6_PHI_0->SetBinContent(26,6911.67098579);
  S6_PHI_0->SetBinContent(27,6505.09904545);
  S6_PHI_0->SetBinContent(28,5285.39522442);
  S6_PHI_0->SetBinContent(29,8537.94674715);
  S6_PHI_0->SetBinContent(30,7318.23892613);
  S6_PHI_0->SetBinContent(31,8131.37480681);
  S6_PHI_0->SetBinContent(32,5285.39522442);
  S6_PHI_0->SetBinContent(33,5285.39522442);
  S6_PHI_0->SetBinContent(34,5691.96316476);
  S6_PHI_0->SetBinContent(35,8537.94674715);
  S6_PHI_0->SetBinContent(36,6098.53110511);
  S6_PHI_0->SetBinContent(37,7318.23892613);
  S6_PHI_0->SetBinContent(38,5691.96316476);
  S6_PHI_0->SetBinContent(39,4878.82728408);
  S6_PHI_0->SetBinContent(40,6911.67098579);
  S6_PHI_0->SetBinContent(41,6505.09904545);
  S6_PHI_0->SetBinContent(42,9351.08262783);
  S6_PHI_0->SetBinContent(43,7318.23892613);
  S6_PHI_0->SetBinContent(44,6911.67098579);
  S6_PHI_0->SetBinContent(45,4472.25534374);
  S6_PHI_0->SetBinContent(46,3659.11946306);
  S6_PHI_0->SetBinContent(47,4472.25534374);
  S6_PHI_0->SetBinContent(48,6098.53110511);
  S6_PHI_0->SetBinContent(49,10164.2185085);
  S6_PHI_0->SetBinContent(50,4065.6874034);
  S6_PHI_0->SetBinContent(51,5285.39522442);
  S6_PHI_0->SetBinContent(52,9351.08262783);
  S6_PHI_0->SetBinContent(53,9757.65056817);
  S6_PHI_0->SetBinContent(54,8537.94674715);
  S6_PHI_0->SetBinContent(55,4472.25534374);
  S6_PHI_0->SetBinContent(56,8131.37480681);
  S6_PHI_0->SetBinContent(57,5691.96316476);
  S6_PHI_0->SetBinContent(58,3252.55032272);
  S6_PHI_0->SetBinContent(59,5691.96316476);
  S6_PHI_0->SetBinContent(60,4878.82728408);
  S6_PHI_0->SetBinContent(61,7318.23892613);
  S6_PHI_0->SetBinContent(62,6505.09904545);
  S6_PHI_0->SetBinContent(63,9757.65056817);
  S6_PHI_0->SetBinContent(64,1626.27536136);
  S6_PHI_0->SetBinContent(65,0.0); // overflow
  S6_PHI_0->SetEntries(999);
  // Style
  S6_PHI_0->SetLineColor(9);
  S6_PHI_0->SetLineStyle(1);
  S6_PHI_0->SetLineWidth(1);
  S6_PHI_0->SetFillColor(9);
  S6_PHI_0->SetFillStyle(1001);

  // Creating a new TH1F
  TH1F* S6_PHI_1 = new TH1F("S6_PHI_1","S6_PHI_1",64,-3.2,3.2);
  // Content
  S6_PHI_1->SetBinContent(0,0.0); // underflow
  S6_PHI_1->SetBinContent(1,141.959874022);
  S6_PHI_1->SetBinContent(2,283.919803599);
  S6_PHI_1->SetBinContent(3,0.0);
  S6_PHI_1->SetBinContent(4,283.919803599);
  S6_PHI_1->SetBinContent(5,283.919803599);
  S6_PHI_1->SetBinContent(6,283.919803599);
  S6_PHI_1->SetBinContent(7,283.919803599);
  S6_PHI_1->SetBinContent(8,141.959874022);
  S6_PHI_1->SetBinContent(9,141.959874022);
  S6_PHI_1->SetBinContent(10,0.0);
  S6_PHI_1->SetBinContent(11,0.0);
  S6_PHI_1->SetBinContent(12,141.959874022);
  S6_PHI_1->SetBinContent(13,141.959874022);
  S6_PHI_1->SetBinContent(14,425.879677621);
  S6_PHI_1->SetBinContent(15,425.879677621);
  S6_PHI_1->SetBinContent(16,141.959874022);
  S6_PHI_1->SetBinContent(17,0.0);
  S6_PHI_1->SetBinContent(18,0.0);
  S6_PHI_1->SetBinContent(19,141.959874022);
  S6_PHI_1->SetBinContent(20,425.879677621);
  S6_PHI_1->SetBinContent(21,141.959874022);
  S6_PHI_1->SetBinContent(22,283.919803599);
  S6_PHI_1->SetBinContent(23,141.959874022);
  S6_PHI_1->SetBinContent(24,0.0);
  S6_PHI_1->SetBinContent(25,141.959874022);
  S6_PHI_1->SetBinContent(26,0.0);
  S6_PHI_1->SetBinContent(27,283.919803599);
  S6_PHI_1->SetBinContent(28,283.919803599);
  S6_PHI_1->SetBinContent(29,283.919803599);
  S6_PHI_1->SetBinContent(30,141.959874022);
  S6_PHI_1->SetBinContent(31,141.959874022);
  S6_PHI_1->SetBinContent(32,141.959874022);
  S6_PHI_1->SetBinContent(33,283.919803599);
  S6_PHI_1->SetBinContent(34,0.0);
  S6_PHI_1->SetBinContent(35,0.0);
  S6_PHI_1->SetBinContent(36,141.959874022);
  S6_PHI_1->SetBinContent(37,0.0);
  S6_PHI_1->SetBinContent(38,141.959874022);
  S6_PHI_1->SetBinContent(39,0.0);
  S6_PHI_1->SetBinContent(40,141.959874022);
  S6_PHI_1->SetBinContent(41,141.959874022);
  S6_PHI_1->SetBinContent(42,141.959874022);
  S6_PHI_1->SetBinContent(43,425.879677621);
  S6_PHI_1->SetBinContent(44,141.959874022);
  S6_PHI_1->SetBinContent(45,0.0);
  S6_PHI_1->SetBinContent(46,0.0);
  S6_PHI_1->SetBinContent(47,0.0);
  S6_PHI_1->SetBinContent(48,141.959874022);
  S6_PHI_1->SetBinContent(49,283.919803599);
  S6_PHI_1->SetBinContent(50,567.839496088);
  S6_PHI_1->SetBinContent(51,283.919803599);
  S6_PHI_1->SetBinContent(52,0.0);
  S6_PHI_1->SetBinContent(53,141.959874022);
  S6_PHI_1->SetBinContent(54,141.959874022);
  S6_PHI_1->SetBinContent(55,283.919803599);
  S6_PHI_1->SetBinContent(56,283.919803599);
  S6_PHI_1->SetBinContent(57,0.0);
  S6_PHI_1->SetBinContent(58,141.959874022);
  S6_PHI_1->SetBinContent(59,283.919803599);
  S6_PHI_1->SetBinContent(60,141.959874022);
  S6_PHI_1->SetBinContent(61,141.959874022);
  S6_PHI_1->SetBinContent(62,0.0);
  S6_PHI_1->SetBinContent(63,0.0);
  S6_PHI_1->SetBinContent(64,0.0);
  S6_PHI_1->SetBinContent(65,0.0); // overflow
  S6_PHI_1->SetEntries(71);
  // Style
  S6_PHI_1->SetLineColor(46);
  S6_PHI_1->SetLineStyle(1);
  S6_PHI_1->SetLineWidth(1);
  S6_PHI_1->SetFillColor(46);
  S6_PHI_1->SetFillStyle(1001);

  // Creating a new THStack
  THStack* stack = new THStack("mystack_12","mystack");
  stack->Add(S6_PHI_0);
  stack->Add(S6_PHI_1);
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

  // Creating a TLegend
  TLegend* legend = new TLegend(.73,.5,.97,.95);
  legend->AddEntry(S6_PHI_0,"signal1TeV");
  legend->AddEntry(S6_PHI_1,"signal4TeV");
  legend->SetFillColor(0);
  legend->SetTextSize(0.05);
  legend->SetTextFont(22);
  legend->SetY1(TMath::Max(0.15,0.97-0.10*legend->GetListOfPrimitives()->GetSize()));
  legend->Draw();

  // Saving the image
  canvas->SaveAs("../../HTML/MadAnalysis5job_0/selection_5.png");
  canvas->SaveAs("../../PDF/MadAnalysis5job_0/selection_5.png");
  canvas->SaveAs("../../DVI/MadAnalysis5job_0/selection_5.eps");

}
