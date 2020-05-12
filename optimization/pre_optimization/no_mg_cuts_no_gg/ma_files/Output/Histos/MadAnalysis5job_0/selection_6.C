void selection_6()
{

  // ROOT version
  Int_t root_version = gROOT->GetVersionInt();

  // Creating a new TCanvas
  TCanvas* canvas = new TCanvas("canvas_plotflow_tempo13","canvas_plotflow_tempo13",0,0,700,500);
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
  TH1F* S7_DELTAR_0 = new TH1F("S7_DELTAR_0","S7_DELTAR_0",75,0.0,15.0);
  // Content
  S7_DELTAR_0->SetBinContent(0,0.0); // underflow
  S7_DELTAR_0->SetBinContent(1,0.0);
  S7_DELTAR_0->SetBinContent(2,0.0);
  S7_DELTAR_0->SetBinContent(3,50.5635130925);
  S7_DELTAR_0->SetBinContent(4,47.501413836);
  S7_DELTAR_0->SetBinContent(5,45.6316388903);
  S7_DELTAR_0->SetBinContent(6,45.2730261773);
  S7_DELTAR_0->SetBinContent(7,47.3076566384);
  S7_DELTAR_0->SetBinContent(8,50.7170557779);
  S7_DELTAR_0->SetBinContent(9,57.1029684177);
  S7_DELTAR_0->SetBinContent(10,64.0639565774);
  S7_DELTAR_0->SetBinContent(11,71.0777912433);
  S7_DELTAR_0->SetBinContent(12,80.8186575298);
  S7_DELTAR_0->SetBinContent(13,91.6252083907);
  S7_DELTAR_0->SetBinContent(14,99.9279861307);
  S7_DELTAR_0->SetBinContent(15,110.37756324);
  S7_DELTAR_0->SetBinContent(16,117.081474334);
  S7_DELTAR_0->SetBinContent(17,110.291217965);
  S7_DELTAR_0->SetBinContent(18,107.641737193);
  S7_DELTAR_0->SetBinContent(19,104.447441722);
  S7_DELTAR_0->SetBinContent(20,100.282081707);
  S7_DELTAR_0->SetBinContent(21,95.1397808718);
  S7_DELTAR_0->SetBinContent(22,91.3486236887);
  S7_DELTAR_0->SetBinContent(23,85.2704360144);
  S7_DELTAR_0->SetBinContent(24,78.502045787);
  S7_DELTAR_0->SetBinContent(25,72.8467101111);
  S7_DELTAR_0->SetBinContent(26,66.742299057);
  S7_DELTAR_0->SetBinContent(27,59.9928967952);
  S7_DELTAR_0->SetBinContent(28,53.6051053462);
  S7_DELTAR_0->SetBinContent(29,47.4591206413);
  S7_DELTAR_0->SetBinContent(30,42.3465609566);
  S7_DELTAR_0->SetBinContent(31,37.538971983);
  S7_DELTAR_0->SetBinContent(32,32.1986566488);
  S7_DELTAR_0->SetBinContent(33,27.4120903511);
  S7_DELTAR_0->SetBinContent(34,23.8194913228);
  S7_DELTAR_0->SetBinContent(35,20.28160162);
  S7_DELTAR_0->SetBinContent(36,16.9720671868);
  S7_DELTAR_0->SetBinContent(37,14.4507012162);
  S7_DELTAR_0->SetBinContent(38,12.0006020771);
  S7_DELTAR_0->SetBinContent(39,9.91745036842);
  S7_DELTAR_0->SetBinContent(40,8.04351006263);
  S7_DELTAR_0->SetBinContent(41,6.45057565667);
  S7_DELTAR_0->SetBinContent(42,5.11586958686);
  S7_DELTAR_0->SetBinContent(43,3.96393727593);
  S7_DELTAR_0->SetBinContent(44,2.95375872216);
  S7_DELTAR_0->SetBinContent(45,2.2013651855);
  S7_DELTAR_0->SetBinContent(46,1.53492197395);
  S7_DELTAR_0->SetBinContent(47,1.08692950939);
  S7_DELTAR_0->SetBinContent(48,0.640957364355);
  S7_DELTAR_0->SetBinContent(49,0.346029008505);
  S7_DELTAR_0->SetBinContent(50,0.153223087956);
  S7_DELTAR_0->SetBinContent(51,0.041799547651);
  S7_DELTAR_0->SetBinContent(52,0.0);
  S7_DELTAR_0->SetBinContent(53,0.0);
  S7_DELTAR_0->SetBinContent(54,0.0);
  S7_DELTAR_0->SetBinContent(55,0.0);
  S7_DELTAR_0->SetBinContent(56,0.0);
  S7_DELTAR_0->SetBinContent(57,0.0);
  S7_DELTAR_0->SetBinContent(58,0.0);
  S7_DELTAR_0->SetBinContent(59,0.0);
  S7_DELTAR_0->SetBinContent(60,0.0);
  S7_DELTAR_0->SetBinContent(61,0.0);
  S7_DELTAR_0->SetBinContent(62,0.0);
  S7_DELTAR_0->SetBinContent(63,0.0);
  S7_DELTAR_0->SetBinContent(64,0.0);
  S7_DELTAR_0->SetBinContent(65,0.0);
  S7_DELTAR_0->SetBinContent(66,0.0);
  S7_DELTAR_0->SetBinContent(67,0.0);
  S7_DELTAR_0->SetBinContent(68,0.0);
  S7_DELTAR_0->SetBinContent(69,0.0);
  S7_DELTAR_0->SetBinContent(70,0.0);
  S7_DELTAR_0->SetBinContent(71,0.0);
  S7_DELTAR_0->SetBinContent(72,0.0);
  S7_DELTAR_0->SetBinContent(73,0.0);
  S7_DELTAR_0->SetBinContent(74,0.0);
  S7_DELTAR_0->SetBinContent(75,0.0);
  S7_DELTAR_0->SetBinContent(76,0.0); // overflow
  S7_DELTAR_0->SetEntries(999999);
  // Style
  S7_DELTAR_0->SetLineColor(9);
  S7_DELTAR_0->SetLineStyle(1);
  S7_DELTAR_0->SetLineWidth(1);
  S7_DELTAR_0->SetFillColor(9);
  S7_DELTAR_0->SetFillStyle(1001);

  // Creating a new THStack
  THStack* stack = new THStack("mystack_14","mystack");
  stack->Add(S7_DELTAR_0);
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
  stack->GetXaxis()->SetTitle("#DeltaR [ j_{1} , j_{2} ] ");

  // Finalizing the TCanvas
  canvas->SetLogx(0);
  canvas->SetLogy(0);

  // Saving the image
  canvas->SaveAs("../../HTML/MadAnalysis5job_0/selection_6.png");
  canvas->SaveAs("../../PDF/MadAnalysis5job_0/selection_6.png");
  canvas->SaveAs("../../DVI/MadAnalysis5job_0/selection_6.eps");

}
