void selection_3()
{

  // ROOT version
  Int_t root_version = gROOT->GetVersionInt();

  // Creating a new TCanvas
  TCanvas* canvas = new TCanvas("canvas_plotflow_tempo7","canvas_plotflow_tempo7",0,0,1000,500);
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
  TH1F* S4_PT_0 = new TH1F("S4_PT_0","S4_PT_0",100,0.0,1000.0);
  // Content
  S4_PT_0->SetBinContent(0,0.0); // underflow
  S4_PT_0->SetBinContent(1,0.0);
  S4_PT_0->SetBinContent(2,0.0);
  S4_PT_0->SetBinContent(3,53667.0718078);
  S4_PT_0->SetBinContent(4,42283.1535455);
  S4_PT_0->SetBinContent(5,34964.9186627);
  S4_PT_0->SetBinContent(6,23174.4204625);
  S4_PT_0->SetBinContent(7,22361.2845866);
  S4_PT_0->SetBinContent(8,17482.4573313);
  S4_PT_0->SetBinContent(9,18295.5972072);
  S4_PT_0->SetBinContent(10,17889.0292693);
  S4_PT_0->SetBinContent(11,13010.202014);
  S4_PT_0->SetBinContent(12,14636.4777658);
  S4_PT_0->SetBinContent(13,12197.0661381);
  S4_PT_0->SetBinContent(14,12197.0661381);
  S4_PT_0->SetBinContent(15,9351.08257257);
  S4_PT_0->SetBinContent(16,12603.6340761);
  S4_PT_0->SetBinContent(17,9757.65051051);
  S4_PT_0->SetBinContent(18,6911.67094494);
  S4_PT_0->SetBinContent(19,6911.67094494);
  S4_PT_0->SetBinContent(20,5691.96313113);
  S4_PT_0->SetBinContent(21,5691.96313113);
  S4_PT_0->SetBinContent(22,6911.67094494);
  S4_PT_0->SetBinContent(23,4472.25531732);
  S4_PT_0->SetBinContent(24,6505.09900701);
  S4_PT_0->SetBinContent(25,3252.5503035);
  S4_PT_0->SetBinContent(26,3659.11944144);
  S4_PT_0->SetBinContent(27,3252.5503035);
  S4_PT_0->SetBinContent(28,2032.84408969);
  S4_PT_0->SetBinContent(29,2032.84408969);
  S4_PT_0->SetBinContent(30,1219.70661381);
  S4_PT_0->SetBinContent(31,2439.41282763);
  S4_PT_0->SetBinContent(32,1626.27535175);
  S4_PT_0->SetBinContent(33,2439.41282763);
  S4_PT_0->SetBinContent(34,2439.41282763);
  S4_PT_0->SetBinContent(35,2439.41282763);
  S4_PT_0->SetBinContent(36,2032.84408969);
  S4_PT_0->SetBinContent(37,1626.27535175);
  S4_PT_0->SetBinContent(38,2032.84408969);
  S4_PT_0->SetBinContent(39,1219.70661381);
  S4_PT_0->SetBinContent(40,813.137475876);
  S4_PT_0->SetBinContent(41,1219.70661381);
  S4_PT_0->SetBinContent(42,2439.41282763);
  S4_PT_0->SetBinContent(43,1626.27535175);
  S4_PT_0->SetBinContent(44,1219.70661381);
  S4_PT_0->SetBinContent(45,1219.70661381);
  S4_PT_0->SetBinContent(46,0.0);
  S4_PT_0->SetBinContent(47,406.568737938);
  S4_PT_0->SetBinContent(48,406.568737938);
  S4_PT_0->SetBinContent(49,406.568737938);
  S4_PT_0->SetBinContent(50,406.568737938);
  S4_PT_0->SetBinContent(51,0.0);
  S4_PT_0->SetBinContent(52,813.137475876);
  S4_PT_0->SetBinContent(53,406.568737938);
  S4_PT_0->SetBinContent(54,813.137475876);
  S4_PT_0->SetBinContent(55,406.568737938);
  S4_PT_0->SetBinContent(56,0.0);
  S4_PT_0->SetBinContent(57,0.0);
  S4_PT_0->SetBinContent(58,813.137475876);
  S4_PT_0->SetBinContent(59,0.0);
  S4_PT_0->SetBinContent(60,0.0);
  S4_PT_0->SetBinContent(61,406.568737938);
  S4_PT_0->SetBinContent(62,0.0);
  S4_PT_0->SetBinContent(63,0.0);
  S4_PT_0->SetBinContent(64,406.568737938);
  S4_PT_0->SetBinContent(65,0.0);
  S4_PT_0->SetBinContent(66,0.0);
  S4_PT_0->SetBinContent(67,0.0);
  S4_PT_0->SetBinContent(68,0.0);
  S4_PT_0->SetBinContent(69,0.0);
  S4_PT_0->SetBinContent(70,0.0);
  S4_PT_0->SetBinContent(71,406.568737938);
  S4_PT_0->SetBinContent(72,0.0);
  S4_PT_0->SetBinContent(73,406.568737938);
  S4_PT_0->SetBinContent(74,0.0);
  S4_PT_0->SetBinContent(75,0.0);
  S4_PT_0->SetBinContent(76,0.0);
  S4_PT_0->SetBinContent(77,0.0);
  S4_PT_0->SetBinContent(78,0.0);
  S4_PT_0->SetBinContent(79,0.0);
  S4_PT_0->SetBinContent(80,0.0);
  S4_PT_0->SetBinContent(81,0.0);
  S4_PT_0->SetBinContent(82,0.0);
  S4_PT_0->SetBinContent(83,0.0);
  S4_PT_0->SetBinContent(84,0.0);
  S4_PT_0->SetBinContent(85,0.0);
  S4_PT_0->SetBinContent(86,406.568737938);
  S4_PT_0->SetBinContent(87,0.0);
  S4_PT_0->SetBinContent(88,0.0);
  S4_PT_0->SetBinContent(89,0.0);
  S4_PT_0->SetBinContent(90,0.0);
  S4_PT_0->SetBinContent(91,0.0);
  S4_PT_0->SetBinContent(92,0.0);
  S4_PT_0->SetBinContent(93,0.0);
  S4_PT_0->SetBinContent(94,0.0);
  S4_PT_0->SetBinContent(95,0.0);
  S4_PT_0->SetBinContent(96,0.0);
  S4_PT_0->SetBinContent(97,0.0);
  S4_PT_0->SetBinContent(98,0.0);
  S4_PT_0->SetBinContent(99,0.0);
  S4_PT_0->SetBinContent(100,0.0);
  S4_PT_0->SetBinContent(101,0.0); // overflow
  S4_PT_0->SetEntries(999);
  // Style
  S4_PT_0->SetLineColor(9);
  S4_PT_0->SetLineStyle(1);
  S4_PT_0->SetLineWidth(1);
  S4_PT_0->SetFillColor(9);
  S4_PT_0->SetFillStyle(1001);

  // Creating a new TH1F
  TH1F* S4_PT_1 = new TH1F("S4_PT_1","S4_PT_1",100,0.0,1000.0);
  // Content
  S4_PT_1->SetBinContent(0,0.0); // underflow
  S4_PT_1->SetBinContent(1,0.0);
  S4_PT_1->SetBinContent(2,0.0);
  S4_PT_1->SetBinContent(3,3123.11785289);
  S4_PT_1->SetBinContent(4,1277.63889437);
  S4_PT_1->SetBinContent(5,1703.51852582);
  S4_PT_1->SetBinContent(6,567.839508607);
  S4_PT_1->SetBinContent(7,283.919809859);
  S4_PT_1->SetBinContent(8,567.839508607);
  S4_PT_1->SetBinContent(9,283.919809859);
  S4_PT_1->SetBinContent(10,141.959877152);
  S4_PT_1->SetBinContent(11,283.919809859);
  S4_PT_1->SetBinContent(12,425.879687011);
  S4_PT_1->SetBinContent(13,425.879687011);
  S4_PT_1->SetBinContent(14,0.0);
  S4_PT_1->SetBinContent(15,0.0);
  S4_PT_1->SetBinContent(16,141.959877152);
  S4_PT_1->SetBinContent(17,141.959877152);
  S4_PT_1->SetBinContent(18,0.0);
  S4_PT_1->SetBinContent(19,0.0);
  S4_PT_1->SetBinContent(20,0.0);
  S4_PT_1->SetBinContent(21,141.959877152);
  S4_PT_1->SetBinContent(22,0.0);
  S4_PT_1->SetBinContent(23,141.959877152);
  S4_PT_1->SetBinContent(24,0.0);
  S4_PT_1->SetBinContent(25,0.0);
  S4_PT_1->SetBinContent(26,141.959877152);
  S4_PT_1->SetBinContent(27,0.0);
  S4_PT_1->SetBinContent(28,141.959877152);
  S4_PT_1->SetBinContent(29,0.0);
  S4_PT_1->SetBinContent(30,0.0);
  S4_PT_1->SetBinContent(31,0.0);
  S4_PT_1->SetBinContent(32,0.0);
  S4_PT_1->SetBinContent(33,0.0);
  S4_PT_1->SetBinContent(34,0.0);
  S4_PT_1->SetBinContent(35,0.0);
  S4_PT_1->SetBinContent(36,0.0);
  S4_PT_1->SetBinContent(37,0.0);
  S4_PT_1->SetBinContent(38,0.0);
  S4_PT_1->SetBinContent(39,0.0);
  S4_PT_1->SetBinContent(40,0.0);
  S4_PT_1->SetBinContent(41,141.959877152);
  S4_PT_1->SetBinContent(42,0.0);
  S4_PT_1->SetBinContent(43,0.0);
  S4_PT_1->SetBinContent(44,0.0);
  S4_PT_1->SetBinContent(45,0.0);
  S4_PT_1->SetBinContent(46,0.0);
  S4_PT_1->SetBinContent(47,0.0);
  S4_PT_1->SetBinContent(48,0.0);
  S4_PT_1->SetBinContent(49,0.0);
  S4_PT_1->SetBinContent(50,0.0);
  S4_PT_1->SetBinContent(51,0.0);
  S4_PT_1->SetBinContent(52,0.0);
  S4_PT_1->SetBinContent(53,0.0);
  S4_PT_1->SetBinContent(54,0.0);
  S4_PT_1->SetBinContent(55,0.0);
  S4_PT_1->SetBinContent(56,0.0);
  S4_PT_1->SetBinContent(57,0.0);
  S4_PT_1->SetBinContent(58,0.0);
  S4_PT_1->SetBinContent(59,0.0);
  S4_PT_1->SetBinContent(60,0.0);
  S4_PT_1->SetBinContent(61,0.0);
  S4_PT_1->SetBinContent(62,0.0);
  S4_PT_1->SetBinContent(63,0.0);
  S4_PT_1->SetBinContent(64,0.0);
  S4_PT_1->SetBinContent(65,0.0);
  S4_PT_1->SetBinContent(66,0.0);
  S4_PT_1->SetBinContent(67,0.0);
  S4_PT_1->SetBinContent(68,0.0);
  S4_PT_1->SetBinContent(69,0.0);
  S4_PT_1->SetBinContent(70,0.0);
  S4_PT_1->SetBinContent(71,0.0);
  S4_PT_1->SetBinContent(72,0.0);
  S4_PT_1->SetBinContent(73,0.0);
  S4_PT_1->SetBinContent(74,0.0);
  S4_PT_1->SetBinContent(75,0.0);
  S4_PT_1->SetBinContent(76,0.0);
  S4_PT_1->SetBinContent(77,0.0);
  S4_PT_1->SetBinContent(78,0.0);
  S4_PT_1->SetBinContent(79,0.0);
  S4_PT_1->SetBinContent(80,0.0);
  S4_PT_1->SetBinContent(81,0.0);
  S4_PT_1->SetBinContent(82,0.0);
  S4_PT_1->SetBinContent(83,0.0);
  S4_PT_1->SetBinContent(84,0.0);
  S4_PT_1->SetBinContent(85,0.0);
  S4_PT_1->SetBinContent(86,0.0);
  S4_PT_1->SetBinContent(87,0.0);
  S4_PT_1->SetBinContent(88,0.0);
  S4_PT_1->SetBinContent(89,0.0);
  S4_PT_1->SetBinContent(90,0.0);
  S4_PT_1->SetBinContent(91,0.0);
  S4_PT_1->SetBinContent(92,0.0);
  S4_PT_1->SetBinContent(93,0.0);
  S4_PT_1->SetBinContent(94,0.0);
  S4_PT_1->SetBinContent(95,0.0);
  S4_PT_1->SetBinContent(96,0.0);
  S4_PT_1->SetBinContent(97,0.0);
  S4_PT_1->SetBinContent(98,0.0);
  S4_PT_1->SetBinContent(99,0.0);
  S4_PT_1->SetBinContent(100,0.0);
  S4_PT_1->SetBinContent(101,0.0); // overflow
  S4_PT_1->SetEntries(71);
  // Style
  S4_PT_1->SetLineColor(46);
  S4_PT_1->SetLineStyle(1);
  S4_PT_1->SetLineWidth(1);
  S4_PT_1->SetFillColor(46);
  S4_PT_1->SetFillStyle(1001);

  // Creating a new THStack
  THStack* stack = new THStack("mystack_8","mystack");
  stack->Add(S4_PT_0);
  stack->Add(S4_PT_1);
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
  stack->GetXaxis()->SetTitle("p_{T} [ j_{2} ]   ( GeV ) ");

  // Finalizing the TCanvas
  canvas->SetLogx(0);
  canvas->SetLogy(0);

  // Creating a TLegend
  TLegend* legend = new TLegend(.73,.5,.97,.95);
  legend->AddEntry(S4_PT_0,"signal1TeV");
  legend->AddEntry(S4_PT_1,"signal4TeV");
  legend->SetFillColor(0);
  legend->SetTextSize(0.05);
  legend->SetTextFont(22);
  legend->SetY1(TMath::Max(0.15,0.97-0.10*legend->GetListOfPrimitives()->GetSize()));
  legend->Draw();

  // Saving the image
  canvas->SaveAs("../../HTML/MadAnalysis5job_0/selection_3.png");
  canvas->SaveAs("../../PDF/MadAnalysis5job_0/selection_3.png");
  canvas->SaveAs("../../DVI/MadAnalysis5job_0/selection_3.eps");

}
