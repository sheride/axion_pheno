void selection_6()
{

  // ROOT version
  Int_t root_version = gROOT->GetVersionInt();

  // Creating a new TCanvas
  TCanvas* canvas = new TCanvas("canvas_plotflow_tempo13","canvas_plotflow_tempo13",0,0,1000,500);
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
  TH1F* S7_DELTAR_0 = new TH1F("S7_DELTAR_0","S7_DELTAR_0",75,0.0,15.0);
  // Content
  S7_DELTAR_0->SetBinContent(0,0.0); // underflow
  S7_DELTAR_0->SetBinContent(1,0.0);
  S7_DELTAR_0->SetBinContent(2,0.0);
  S7_DELTAR_0->SetBinContent(3,0.0);
  S7_DELTAR_0->SetBinContent(4,0.0);
  S7_DELTAR_0->SetBinContent(5,0.0);
  S7_DELTAR_0->SetBinContent(6,0.0);
  S7_DELTAR_0->SetBinContent(7,0.0);
  S7_DELTAR_0->SetBinContent(8,0.0);
  S7_DELTAR_0->SetBinContent(9,0.0);
  S7_DELTAR_0->SetBinContent(10,0.0);
  S7_DELTAR_0->SetBinContent(11,0.0);
  S7_DELTAR_0->SetBinContent(12,0.0);
  S7_DELTAR_0->SetBinContent(13,6098.53120721);
  S7_DELTAR_0->SetBinContent(14,15043.0460444);
  S7_DELTAR_0->SetBinContent(15,13823.338203);
  S7_DELTAR_0->SetBinContent(16,23580.9929345);
  S7_DELTAR_0->SetBinContent(17,26426.9725646);
  S7_DELTAR_0->SetBinContent(18,32525.5037718);
  S7_DELTAR_0->SetBinContent(19,38624.038979);
  S7_DELTAR_0->SetBinContent(20,35778.0553489);
  S7_DELTAR_0->SetBinContent(21,41063.4346619);
  S7_DELTAR_0->SetBinContent(22,33338.6436661);
  S7_DELTAR_0->SetBinContent(23,28053.2483532);
  S7_DELTAR_0->SetBinContent(24,18702.1655688);
  S7_DELTAR_0->SetBinContent(25,18702.1655688);
  S7_DELTAR_0->SetBinContent(26,12197.0664144);
  S7_DELTAR_0->SetBinContent(27,11383.9265201);
  S7_DELTAR_0->SetBinContent(28,9351.08278438);
  S7_DELTAR_0->SetBinContent(29,6911.6711015);
  S7_DELTAR_0->SetBinContent(30,6505.09915435);
  S7_DELTAR_0->SetBinContent(31,6098.53120721);
  S7_DELTAR_0->SetBinContent(32,5285.39531291);
  S7_DELTAR_0->SetBinContent(33,3659.11952432);
  S7_DELTAR_0->SetBinContent(34,2439.41288288);
  S7_DELTAR_0->SetBinContent(35,1626.27538859);
  S7_DELTAR_0->SetBinContent(36,2439.41288288);
  S7_DELTAR_0->SetBinContent(37,1219.70664144);
  S7_DELTAR_0->SetBinContent(38,1219.70664144);
  S7_DELTAR_0->SetBinContent(39,813.137494294);
  S7_DELTAR_0->SetBinContent(40,2032.84413574);
  S7_DELTAR_0->SetBinContent(41,813.137494294);
  S7_DELTAR_0->SetBinContent(42,0.0);
  S7_DELTAR_0->SetBinContent(43,0.0);
  S7_DELTAR_0->SetBinContent(44,0.0);
  S7_DELTAR_0->SetBinContent(45,406.568747147);
  S7_DELTAR_0->SetBinContent(46,0.0);
  S7_DELTAR_0->SetBinContent(47,0.0);
  S7_DELTAR_0->SetBinContent(48,0.0);
  S7_DELTAR_0->SetBinContent(49,0.0);
  S7_DELTAR_0->SetBinContent(50,0.0);
  S7_DELTAR_0->SetBinContent(51,0.0);
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
  S7_DELTAR_0->SetEntries(999);
  // Style
  S7_DELTAR_0->SetLineColor(9);
  S7_DELTAR_0->SetLineStyle(1);
  S7_DELTAR_0->SetLineWidth(1);
  S7_DELTAR_0->SetFillColor(9);
  S7_DELTAR_0->SetFillStyle(1001);

  // Creating a new TH1F
  TH1F* S7_DELTAR_1 = new TH1F("S7_DELTAR_1","S7_DELTAR_1",75,0.0,15.0);
  // Content
  S7_DELTAR_1->SetBinContent(0,0.0); // underflow
  S7_DELTAR_1->SetBinContent(1,0.0);
  S7_DELTAR_1->SetBinContent(2,0.0);
  S7_DELTAR_1->SetBinContent(3,0.0);
  S7_DELTAR_1->SetBinContent(4,0.0);
  S7_DELTAR_1->SetBinContent(5,0.0);
  S7_DELTAR_1->SetBinContent(6,0.0);
  S7_DELTAR_1->SetBinContent(7,0.0);
  S7_DELTAR_1->SetBinContent(8,0.0);
  S7_DELTAR_1->SetBinContent(9,0.0);
  S7_DELTAR_1->SetBinContent(10,0.0);
  S7_DELTAR_1->SetBinContent(11,0.0);
  S7_DELTAR_1->SetBinContent(12,0.0);
  S7_DELTAR_1->SetBinContent(13,0.0);
  S7_DELTAR_1->SetBinContent(14,141.959881847);
  S7_DELTAR_1->SetBinContent(15,0.0);
  S7_DELTAR_1->SetBinContent(16,567.839527387);
  S7_DELTAR_1->SetBinContent(17,0.0);
  S7_DELTAR_1->SetBinContent(18,709.799409233);
  S7_DELTAR_1->SetBinContent(19,709.799409233);
  S7_DELTAR_1->SetBinContent(20,851.75929108);
  S7_DELTAR_1->SetBinContent(21,425.879701095);
  S7_DELTAR_1->SetBinContent(22,709.799409233);
  S7_DELTAR_1->SetBinContent(23,283.919819249);
  S7_DELTAR_1->SetBinContent(24,425.879701095);
  S7_DELTAR_1->SetBinContent(25,709.799409233);
  S7_DELTAR_1->SetBinContent(26,425.879701095);
  S7_DELTAR_1->SetBinContent(27,709.799409233);
  S7_DELTAR_1->SetBinContent(28,425.879701095);
  S7_DELTAR_1->SetBinContent(29,567.839527387);
  S7_DELTAR_1->SetBinContent(30,567.839527387);
  S7_DELTAR_1->SetBinContent(31,425.879701095);
  S7_DELTAR_1->SetBinContent(32,425.879701095);
  S7_DELTAR_1->SetBinContent(33,425.879701095);
  S7_DELTAR_1->SetBinContent(34,0.0);
  S7_DELTAR_1->SetBinContent(35,0.0);
  S7_DELTAR_1->SetBinContent(36,141.959881847);
  S7_DELTAR_1->SetBinContent(37,0.0);
  S7_DELTAR_1->SetBinContent(38,425.879701095);
  S7_DELTAR_1->SetBinContent(39,0.0);
  S7_DELTAR_1->SetBinContent(40,0.0);
  S7_DELTAR_1->SetBinContent(41,0.0);
  S7_DELTAR_1->SetBinContent(42,0.0);
  S7_DELTAR_1->SetBinContent(43,0.0);
  S7_DELTAR_1->SetBinContent(44,0.0);
  S7_DELTAR_1->SetBinContent(45,0.0);
  S7_DELTAR_1->SetBinContent(46,0.0);
  S7_DELTAR_1->SetBinContent(47,0.0);
  S7_DELTAR_1->SetBinContent(48,0.0);
  S7_DELTAR_1->SetBinContent(49,0.0);
  S7_DELTAR_1->SetBinContent(50,0.0);
  S7_DELTAR_1->SetBinContent(51,0.0);
  S7_DELTAR_1->SetBinContent(52,0.0);
  S7_DELTAR_1->SetBinContent(53,0.0);
  S7_DELTAR_1->SetBinContent(54,0.0);
  S7_DELTAR_1->SetBinContent(55,0.0);
  S7_DELTAR_1->SetBinContent(56,0.0);
  S7_DELTAR_1->SetBinContent(57,0.0);
  S7_DELTAR_1->SetBinContent(58,0.0);
  S7_DELTAR_1->SetBinContent(59,0.0);
  S7_DELTAR_1->SetBinContent(60,0.0);
  S7_DELTAR_1->SetBinContent(61,0.0);
  S7_DELTAR_1->SetBinContent(62,0.0);
  S7_DELTAR_1->SetBinContent(63,0.0);
  S7_DELTAR_1->SetBinContent(64,0.0);
  S7_DELTAR_1->SetBinContent(65,0.0);
  S7_DELTAR_1->SetBinContent(66,0.0);
  S7_DELTAR_1->SetBinContent(67,0.0);
  S7_DELTAR_1->SetBinContent(68,0.0);
  S7_DELTAR_1->SetBinContent(69,0.0);
  S7_DELTAR_1->SetBinContent(70,0.0);
  S7_DELTAR_1->SetBinContent(71,0.0);
  S7_DELTAR_1->SetBinContent(72,0.0);
  S7_DELTAR_1->SetBinContent(73,0.0);
  S7_DELTAR_1->SetBinContent(74,0.0);
  S7_DELTAR_1->SetBinContent(75,0.0);
  S7_DELTAR_1->SetBinContent(76,0.0); // overflow
  S7_DELTAR_1->SetEntries(71);
  // Style
  S7_DELTAR_1->SetLineColor(46);
  S7_DELTAR_1->SetLineStyle(1);
  S7_DELTAR_1->SetLineWidth(1);
  S7_DELTAR_1->SetFillColor(46);
  S7_DELTAR_1->SetFillStyle(1001);

  // Creating a new THStack
  THStack* stack = new THStack("mystack_14","mystack");
  stack->Add(S7_DELTAR_0);
  stack->Add(S7_DELTAR_1);
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

  // Creating a TLegend
  TLegend* legend = new TLegend(.73,.5,.97,.95);
  legend->AddEntry(S7_DELTAR_0,"signal1TeV");
  legend->AddEntry(S7_DELTAR_1,"signal4TeV");
  legend->SetFillColor(0);
  legend->SetTextSize(0.05);
  legend->SetTextFont(22);
  legend->SetY1(TMath::Max(0.15,0.97-0.10*legend->GetListOfPrimitives()->GetSize()));
  legend->Draw();

  // Saving the image
  canvas->SaveAs("../../HTML/MadAnalysis5job_0/selection_6.png");
  canvas->SaveAs("../../PDF/MadAnalysis5job_0/selection_6.png");
  canvas->SaveAs("../../DVI/MadAnalysis5job_0/selection_6.eps");

}
