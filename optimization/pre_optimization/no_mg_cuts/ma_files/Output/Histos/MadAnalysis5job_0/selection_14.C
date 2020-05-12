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
  S15_TET_0->SetBinContent(1,3.99989131956);
  S15_TET_0->SetBinContent(2,53.4468678033);
  S15_TET_0->SetBinContent(3,113.18160476);
  S15_TET_0->SetBinContent(4,295.529810204);
  S15_TET_0->SetBinContent(5,377.272069198);
  S15_TET_0->SetBinContent(6,540.756507187);
  S15_TET_0->SetBinContent(7,622.499086172);
  S15_TET_0->SetBinContent(8,880.301681456);
  S15_TET_0->SetBinContent(9,817.422989924);
  S15_TET_0->SetBinContent(10,946.324287566);
  S15_TET_0->SetBinContent(11,1134.95996217);
  S15_TET_0->SetBinContent(12,1251.28560151);
  S15_TET_0->SetBinContent(13,1160.11167878);
  S15_TET_0->SetBinContent(14,1216.70254116);
  S15_TET_0->SetBinContent(15,1216.70254116);
  S15_TET_0->SetBinContent(16,1417.91427407);
  S15_TET_0->SetBinContent(17,1241.85385778);
  S15_TET_0->SetBinContent(18,1219.84645574);
  S15_TET_0->SetBinContent(19,1213.55862658);
  S15_TET_0->SetBinContent(20,1263.86125982);
  S15_TET_0->SetBinContent(21,1175.83125167);
  S15_TET_0->SetBinContent(22,1122.38430387);
  S15_TET_0->SetBinContent(23,1182.11908082);
  S15_TET_0->SetBinContent(24,993.483006224);
  S15_TET_0->SetBinContent(25,1075.22558521);
  S15_TET_0->SetBinContent(26,861.437794004);
  S15_TET_0->SetBinContent(27,754.544298391);
  S15_TET_0->SetBinContent(28,666.513890252);
  S15_TET_0->SetBinContent(29,666.513890252);
  S15_TET_0->SetBinContent(30,688.521692281);
  S15_TET_0->SetBinContent(31,569.052138371);
  S15_TET_0->SetBinContent(32,518.749105147);
  S15_TET_0->SetBinContent(33,481.021730231);
  S15_TET_0->SetBinContent(34,437.006926151);
  S15_TET_0->SetBinContent(35,424.431267842);
  S15_TET_0->SetBinContent(36,355.264547161);
  S15_TET_0->SetBinContent(37,355.264547161);
  S15_TET_0->SetBinContent(38,295.529810204);
  S15_TET_0->SetBinContent(39,213.787511212);
  S15_TET_0->SetBinContent(40,207.499642059);
  S15_TET_0->SetBinContent(41,235.795033249);
  S15_TET_0->SetBinContent(42,201.211772905);
  S15_TET_0->SetBinContent(43,116.325559336);
  S15_TET_0->SetBinContent(44,125.757343066);
  S15_TET_0->SetBinContent(45,106.893735607);
  S15_TET_0->SetBinContent(46,78.5983444163);
  S15_TET_0->SetBinContent(47,69.1665606859);
  S15_TET_0->SetBinContent(48,78.5983444163);
  S15_TET_0->SetBinContent(49,62.8786915326);
  S15_TET_0->SetBinContent(50,50.3029532261);
  S15_TET_0->SetBinContent(51,59.7347369565);
  S15_TET_0->SetBinContent(52,34.5832723431);
  S15_TET_0->SetBinContent(53,37.7272069198);
  S15_TET_0->SetBinContent(54,22.0075380365);
  S15_TET_0->SetBinContent(55,37.7272069198);
  S15_TET_0->SetBinContent(56,12.5757343066);
  S15_TET_0->SetBinContent(57,15.7196688833);
  S15_TET_0->SetBinContent(58,15.7196688833);
  S15_TET_0->SetBinContent(59,9.43180372989);
  S15_TET_0->SetBinContent(60,6.28786915326);
  S15_TET_0->SetBinContent(61,0.0);
  S15_TET_0->SetBinContent(62,3.14393377665);
  S15_TET_0->SetBinContent(63,0.0);
  S15_TET_0->SetBinContent(64,6.28786915326);
  S15_TET_0->SetBinContent(65,6.28786915326);
  S15_TET_0->SetBinContent(66,3.14393377665);
  S15_TET_0->SetBinContent(67,6.28786915326);
  S15_TET_0->SetBinContent(68,3.14393377665);
  S15_TET_0->SetBinContent(69,0.0);
  S15_TET_0->SetBinContent(70,0.0);
  S15_TET_0->SetBinContent(71,3.14393377665);
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
