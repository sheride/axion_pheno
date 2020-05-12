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
  S7_DELTAR_0->SetBinContent(13,36.4211990728);
  S7_DELTAR_0->SetBinContent(14,157.205773263);
  S7_DELTAR_0->SetBinContent(15,192.512056242);
  S7_DELTAR_0->SetBinContent(16,258.293181792);
  S7_DELTAR_0->SetBinContent(17,295.457664927);
  S7_DELTAR_0->SetBinContent(18,329.277387781);
  S7_DELTAR_0->SetBinContent(19,341.169988784);
  S7_DELTAR_0->SetBinContent(20,372.388191418);
  S7_DELTAR_0->SetBinContent(21,374.989671637);
  S7_DELTAR_0->SetBinContent(22,258.293181792);
  S7_DELTAR_0->SetBinContent(23,205.891257371);
  S7_DELTAR_0->SetBinContent(24,163.152093765);
  S7_DELTAR_0->SetBinContent(25,125.987610629);
  S7_DELTAR_0->SetBinContent(26,97.370968215);
  S7_DELTAR_0->SetBinContent(27,88.8231274939);
  S7_DELTAR_0->SetBinContent(28,73.9573262397);
  S7_DELTAR_0->SetBinContent(29,63.5512853617);
  S7_DELTAR_0->SetBinContent(30,51.287004327);
  S7_DELTAR_0->SetBinContent(31,38.6510672609);
  S7_DELTAR_0->SetBinContent(32,33.0763947906);
  S7_DELTAR_0->SetBinContent(33,26.7584302576);
  S7_DELTAR_0->SetBinContent(34,24.5285620694);
  S7_DELTAR_0->SetBinContent(35,17.4673094737);
  S7_DELTAR_0->SetBinContent(36,19.6971776618);
  S7_DELTAR_0->SetBinContent(37,13.7508611601);
  S7_DELTAR_0->SetBinContent(38,10.0344128466);
  S7_DELTAR_0->SetBinContent(39,13.7508611601);
  S7_DELTAR_0->SetBinContent(40,11.520992972);
  S7_DELTAR_0->SetBinContent(41,6.31796453304);
  S7_DELTAR_0->SetBinContent(42,3.71644871355);
  S7_DELTAR_0->SetBinContent(43,2.97315905084);
  S7_DELTAR_0->SetBinContent(44,1.48657972542);
  S7_DELTAR_0->SetBinContent(45,2.22986938813);
  S7_DELTAR_0->SetBinContent(46,1.85822455678);
  S7_DELTAR_0->SetBinContent(47,1.48657972542);
  S7_DELTAR_0->SetBinContent(48,0.74328966271);
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
  S7_DELTAR_0->SetEntries(9999);
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
