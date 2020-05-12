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
  S15_TET_0->SetBinContent(1,2.59177698141);
  S15_TET_0->SetBinContent(2,44.835417609);
  S15_TET_0->SetBinContent(3,78.8052576906);
  S15_TET_0->SetBinContent(4,102.497138301);
  S15_TET_0->SetBinContent(5,118.590078117);
  S15_TET_0->SetBinContent(6,127.434609296);
  S15_TET_0->SetBinContent(7,133.165924022);
  S15_TET_0->SetBinContent(8,135.701715793);
  S15_TET_0->SetBinContent(9,131.077201662);
  S15_TET_0->SetBinContent(10,126.045871956);
  S15_TET_0->SetBinContent(11,118.073413941);
  S15_TET_0->SetBinContent(12,111.035348585);
  S15_TET_0->SetBinContent(13,103.481378559);
  S15_TET_0->SetBinContent(14,95.7545209078);
  S15_TET_0->SetBinContent(15,88.0667978198);
  S15_TET_0->SetBinContent(16,79.8206377079);
  S15_TET_0->SetBinContent(17,73.8471204101);
  S15_TET_0->SetBinContent(18,67.4746624182);
  S15_TET_0->SetBinContent(19,60.6083654147);
  S15_TET_0->SetBinContent(20,55.4430028278);
  S15_TET_0->SetBinContent(21,50.282636993);
  S15_TET_0->SetBinContent(22,45.103403422);
  S15_TET_0->SetBinContent(23,40.9942343241);
  S15_TET_0->SetBinContent(24,36.9641298354);
  S15_TET_0->SetBinContent(25,33.0658796432);
  S15_TET_0->SetBinContent(26,30.0335905884);
  S15_TET_0->SetBinContent(27,26.2600313489);
  S15_TET_0->SetBinContent(28,23.8937733833);
  S15_TET_0->SetBinContent(29,21.415927948);
  S15_TET_0->SetBinContent(30,19.1623487428);
  S15_TET_0->SetBinContent(31,16.9678231535);
  S15_TET_0->SetBinContent(32,15.2722132761);
  S15_TET_0->SetBinContent(33,13.1531906111);
  S15_TET_0->SetBinContent(34,11.8795824385);
  S15_TET_0->SetBinContent(35,10.4841534477);
  S15_TET_0->SetBinContent(36,9.51578287494);
  S15_TET_0->SetBinContent(37,8.08543258251);
  S15_TET_0->SetBinContent(38,7.00323999248);
  S15_TET_0->SetBinContent(39,6.38331893245);
  S15_TET_0->SetBinContent(40,5.48474299418);
  S15_TET_0->SetBinContent(41,4.88132320855);
  S15_TET_0->SetBinContent(42,4.1935422565);
  S15_TET_0->SetBinContent(43,3.82665153031);
  S15_TET_0->SetBinContent(44,3.31611377268);
  S15_TET_0->SetBinContent(45,2.76342581208);
  S15_TET_0->SetBinContent(46,2.39195046583);
  S15_TET_0->SetBinContent(47,2.11540941363);
  S15_TET_0->SetBinContent(48,1.90169472517);
  S15_TET_0->SetBinContent(49,1.61382863408);
  S15_TET_0->SetBinContent(50,1.3817766646);
  S15_TET_0->SetBinContent(51,1.19583992087);
  S15_TET_0->SetBinContent(52,1.04951582947);
  S15_TET_0->SetBinContent(53,0.90321452326);
  S15_TET_0->SetBinContent(54,0.72218179199);
  S15_TET_0->SetBinContent(55,0.631596671045);
  S15_TET_0->SetBinContent(56,0.531724786366);
  S15_TET_0->SetBinContent(57,0.455095394393);
  S15_TET_0->SetBinContent(58,0.408684760652);
  S15_TET_0->SetBinContent(59,0.332060965042);
  S15_TET_0->SetBinContent(60,0.260059924706);
  S15_TET_0->SetBinContent(61,0.255451719974);
  S15_TET_0->SetBinContent(62,0.195039427115);
  S15_TET_0->SetBinContent(63,0.21129286261);
  S15_TET_0->SetBinContent(64,0.127691402384);
  S15_TET_0->SetBinContent(65,0.130017530433);
  S15_TET_0->SetBinContent(66,0.0975111391307);
  S15_TET_0->SetBinContent(67,0.071966302915);
  S15_TET_0->SetBinContent(68,0.067343627589);
  S15_TET_0->SetBinContent(69,0.0557406493617);
  S15_TET_0->SetBinContent(70,0.0719811732495);
  S15_TET_0->SetBinContent(71,0.0371689447086);
  S15_TET_0->SetBinContent(72,0.0185728119334);
  S15_TET_0->SetBinContent(73,0.0185712289623);
  S15_TET_0->SetBinContent(74,0.0255566965066);
  S15_TET_0->SetBinContent(75,0.0139450439175);
  S15_TET_0->SetBinContent(76,0.00928174699497);
  S15_TET_0->SetBinContent(77,0.0139186570686);
  S15_TET_0->SetBinContent(78,0.00929156461365);
  S15_TET_0->SetBinContent(79,0.00930003510795);
  S15_TET_0->SetBinContent(80,0.0162422987342);
  S15_TET_0->SetBinContent(81,0.0255475344618); // overflow
  S15_TET_0->SetEntries(1000000);
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
