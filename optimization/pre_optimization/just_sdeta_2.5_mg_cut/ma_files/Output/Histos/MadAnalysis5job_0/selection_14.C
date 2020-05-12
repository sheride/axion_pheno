void selection_14()
{

  // ROOT version
  Int_t root_version = gROOT->GetVersionInt();

  // Creating a new TCanvas
  TCanvas* canvas = new TCanvas("canvas_plotflow_tempo29","canvas_plotflow_tempo29",0,0,700,500);
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
  TH1F* S15_TET_0 = new TH1F("S15_TET_0","S15_TET_0",80,0.0,8000.0);
  // Content
  S15_TET_0->SetBinContent(0,0.0); // underflow
  S15_TET_0->SetBinContent(1,4.36738059366);
  S15_TET_0->SetBinContent(2,23.0195085171);
  S15_TET_0->SetBinContent(3,50.123110171);
  S15_TET_0->SetBinContent(4,87.6226633699);
  S15_TET_0->SetBinContent(5,108.414446577);
  S15_TET_0->SetBinContent(6,144.057572008);
  S15_TET_0->SetBinContent(7,155.938613818);
  S15_TET_0->SetBinContent(8,173.01762141);
  S15_TET_0->SetBinContent(9,204.205336182);
  S15_TET_0->SetBinContent(10,190.467866603);
  S15_TET_0->SetBinContent(11,202.348908413);
  S15_TET_0->SetBinContent(12,199.749925522);
  S15_TET_0->SetBinContent(13,206.061723989);
  S15_TET_0->SetBinContent(14,189.72531148);
  S15_TET_0->SetBinContent(15,171.903748765);
  S15_TET_0->SetBinContent(16,177.101714547);
  S15_TET_0->SetBinContent(17,166.705782983);
  S15_TET_0->SetBinContent(18,149.626815351);
  S15_TET_0->SetBinContent(19,126.607286854);
  S15_TET_0->SetBinContent(20,125.864731731);
  S15_TET_0->SetBinContent(21,108.414446577);
  S15_TET_0->SetBinContent(22,104.33035344);
  S15_TET_0->SetBinContent(23,80.196992258);
  S15_TET_0->SetBinContent(24,70.9149333389);
  S15_TET_0->SetBinContent(25,62.0041519813);
  S15_TET_0->SetBinContent(26,64.6031348724);
  S15_TET_0->SetBinContent(27,52.7220930621);
  S15_TET_0->SetBinContent(28,50.8657052549);
  S15_TET_0->SetBinContent(29,37.4995252262);
  S15_TET_0->SetBinContent(30,36.0143949999);
  S15_TET_0->SetBinContent(31,30.0738740948);
  S15_TET_0->SetBinContent(32,26.3610505272);
  S15_TET_0->SetBinContent(33,21.5343782908);
  S15_TET_0->SetBinContent(34,12.2523193717);
  S15_TET_0->SetBinContent(35,14.1087311555);
  S15_TET_0->SetBinContent(36,10.7671891454);
  S15_TET_0->SetBinContent(37,12.9948824868);
  S15_TET_0->SetBinContent(38,8.91077736157);
  S15_TET_0->SetBinContent(39,6.31180246266);
  S15_TET_0->SetBinContent(40,6.31180246266);
  S15_TET_0->SetBinContent(41,7.79692869284);
  S15_TET_0->SetBinContent(42,6.6830840202);
  S15_TET_0->SetBinContent(43,4.82667223638);
  S15_TET_0->SetBinContent(44,4.08410512519);
  S15_TET_0->SetBinContent(45,2.97025925373);
  S15_TET_0->SetBinContent(46,0.742564713529);
  S15_TET_0->SetBinContent(47,2.59897689696);
  S15_TET_0->SetBinContent(48,2.2276945402);
  S15_TET_0->SetBinContent(49,2.97025925373);
  S15_TET_0->SetBinContent(50,1.48512982667);
  S15_TET_0->SetBinContent(51,1.48512982667);
  S15_TET_0->SetBinContent(52,1.11384707029);
  S15_TET_0->SetBinContent(53,0.371282396726);
  S15_TET_0->SetBinContent(54,0.0);
  S15_TET_0->SetBinContent(55,0.0);
  S15_TET_0->SetBinContent(56,0.742564713529);
  S15_TET_0->SetBinContent(57,1.11384707029);
  S15_TET_0->SetBinContent(58,0.742564713529);
  S15_TET_0->SetBinContent(59,0.0);
  S15_TET_0->SetBinContent(60,0.0);
  S15_TET_0->SetBinContent(61,0.0);
  S15_TET_0->SetBinContent(62,0.371282396726);
  S15_TET_0->SetBinContent(63,0.0);
  S15_TET_0->SetBinContent(64,0.0);
  S15_TET_0->SetBinContent(65,0.0);
  S15_TET_0->SetBinContent(66,0.0);
  S15_TET_0->SetBinContent(67,0.0);
  S15_TET_0->SetBinContent(68,0.0);
  S15_TET_0->SetBinContent(69,0.0);
  S15_TET_0->SetBinContent(70,0.0);
  S15_TET_0->SetBinContent(71,0.0);
  S15_TET_0->SetBinContent(72,0.0);
  S15_TET_0->SetBinContent(73,0.0);
  S15_TET_0->SetBinContent(74,0.0);
  S15_TET_0->SetBinContent(75,0.0);
  S15_TET_0->SetBinContent(76,0.0);
  S15_TET_0->SetBinContent(77,0.0);
  S15_TET_0->SetBinContent(78,0.0);
  S15_TET_0->SetBinContent(79,0.0);
  S15_TET_0->SetBinContent(80,0.0);
  S15_TET_0->SetBinContent(81,0.0); // overflow
  S15_TET_0->SetEntries(10000);
  // Style
  S15_TET_0->SetLineColor(9);
  S15_TET_0->SetLineStyle(1);
  S15_TET_0->SetLineWidth(1);
  S15_TET_0->SetFillColor(9);
  S15_TET_0->SetFillStyle(1001);

  // Creating a new THStack
  THStack* stack = new THStack("mystack_30","mystack");
  stack->Add(S15_TET_0);
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
  canvas->SaveAs("../../HTML/MadAnalysis5job_0/selection_14.png");
  canvas->SaveAs("../../PDF/MadAnalysis5job_0/selection_14.png");
  canvas->SaveAs("../../DVI/MadAnalysis5job_0/selection_14.eps");

}
