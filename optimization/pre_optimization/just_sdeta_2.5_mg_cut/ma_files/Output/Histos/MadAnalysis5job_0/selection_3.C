void selection_3()
{

  // ROOT version
  Int_t root_version = gROOT->GetVersionInt();

  // Creating a new TCanvas
  TCanvas* canvas = new TCanvas("canvas_plotflow_tempo7","canvas_plotflow_tempo7",0,0,700,500);
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
  TH1F* S4_PT_0 = new TH1F("S4_PT_0","S4_PT_0",100,0.0,1000.0);
  // Content
  S4_PT_0->SetBinContent(0,0.0); // underflow
  S4_PT_0->SetBinContent(1,0.0);
  S4_PT_0->SetBinContent(2,0.0);
  S4_PT_0->SetBinContent(3,284.308335112);
  S4_PT_0->SetBinContent(4,221.128691754);
  S4_PT_0->SetBinContent(5,217.040611536);
  S4_PT_0->SetBinContent(6,198.086730529);
  S4_PT_0->SetBinContent(7,182.105969679);
  S4_PT_0->SetBinContent(8,198.830010568);
  S4_PT_0->SetBinContent(9,156.834128336);
  S4_PT_0->SetBinContent(10,166.12524883);
  S4_PT_0->SetBinContent(11,147.914647862);
  S4_PT_0->SetBinContent(12,137.136967289);
  S4_PT_0->SetBinContent(13,120.4129264);
  S4_PT_0->SetBinContent(14,107.777005729);
  S4_PT_0->SetBinContent(15,121.52788646);
  S4_PT_0->SetBinContent(16,102.202325432);
  S4_PT_0->SetBinContent(17,99.6008452941);
  S4_PT_0->SetBinContent(18,91.4246448595);
  S4_PT_0->SetBinContent(19,85.8499645632);
  S4_PT_0->SetBinContent(20,72.0991238323);
  S4_PT_0->SetBinContent(21,64.2945634174);
  S4_PT_0->SetBinContent(22,69.1259636742);
  S4_PT_0->SetBinContent(23,73.5856839113);
  S4_PT_0->SetBinContent(24,57.9766030816);
  S4_PT_0->SetBinContent(25,60.2064832001);
  S4_PT_0->SetBinContent(26,46.0839624495);
  S4_PT_0->SetBinContent(27,44.5974023705);
  S4_PT_0->SetBinContent(28,47.1988825088);
  S4_PT_0->SetBinContent(29,47.5705625285);
  S4_PT_0->SetBinContent(30,31.9614576988);
  S4_PT_0->SetBinContent(31,28.9883015408);
  S4_PT_0->SetBinContent(32,30.4748816198);
  S4_PT_0->SetBinContent(33,26.0151413828);
  S4_PT_0->SetBinContent(34,27.130077442);
  S4_PT_0->SetBinContent(35,19.697177047);
  S4_PT_0->SetBinContent(36,21.5554011457);
  S4_PT_0->SetBinContent(37,23.7852732643);
  S4_PT_0->SetBinContent(38,15.2374408099);
  S4_PT_0->SetBinContent(39,20.4404690865);
  S4_PT_0->SetBinContent(40,20.4404690865);
  S4_PT_0->SetBinContent(41,21.9270491655);
  S4_PT_0->SetBinContent(42,18.2105969679);
  S4_PT_0->SetBinContent(43,14.8657967902);
  S4_PT_0->SetBinContent(44,12.6359246716);
  S4_PT_0->SetBinContent(45,13.0075686914);
  S4_PT_0->SetBinContent(46,8.9194764741);
  S4_PT_0->SetBinContent(47,11.5209926124);
  S4_PT_0->SetBinContent(48,9.6627685136);
  S4_PT_0->SetBinContent(49,9.6627685136);
  S4_PT_0->SetBinContent(50,8.17618843459);
  S4_PT_0->SetBinContent(51,10.0344125334);
  S4_PT_0->SetBinContent(52,10.7777005729);
  S4_PT_0->SetBinContent(53,8.17618843459);
  S4_PT_0->SetBinContent(54,4.8313842568);
  S4_PT_0->SetBinContent(55,4.8313842568);
  S4_PT_0->SetBinContent(56,4.8313842568);
  S4_PT_0->SetBinContent(57,5.94631631606);
  S4_PT_0->SetBinContent(58,4.08809221729);
  S4_PT_0->SetBinContent(59,4.45974023705);
  S4_PT_0->SetBinContent(60,3.71644859754);
  S4_PT_0->SetBinContent(61,3.34480377779);
  S4_PT_0->SetBinContent(62,3.71644859754);
  S4_PT_0->SetBinContent(63,1.48657967902);
  S4_PT_0->SetBinContent(64,2.60151413828);
  S4_PT_0->SetBinContent(65,1.85822449877);
  S4_PT_0->SetBinContent(66,1.11493445926);
  S4_PT_0->SetBinContent(67,2.22986931852);
  S4_PT_0->SetBinContent(68,0.743289639508);
  S4_PT_0->SetBinContent(69,2.22986931852);
  S4_PT_0->SetBinContent(70,2.60151413828);
  S4_PT_0->SetBinContent(71,1.11493445926);
  S4_PT_0->SetBinContent(72,1.48657967902);
  S4_PT_0->SetBinContent(73,1.11493445926);
  S4_PT_0->SetBinContent(74,2.22986931852);
  S4_PT_0->SetBinContent(75,1.48657967902);
  S4_PT_0->SetBinContent(76,1.11493445926);
  S4_PT_0->SetBinContent(77,0.371644859754);
  S4_PT_0->SetBinContent(78,0.0);
  S4_PT_0->SetBinContent(79,0.371644859754);
  S4_PT_0->SetBinContent(80,0.371644859754);
  S4_PT_0->SetBinContent(81,0.743289639508);
  S4_PT_0->SetBinContent(82,1.11493445926);
  S4_PT_0->SetBinContent(83,0.0);
  S4_PT_0->SetBinContent(84,0.0);
  S4_PT_0->SetBinContent(85,0.371644859754);
  S4_PT_0->SetBinContent(86,0.371644859754);
  S4_PT_0->SetBinContent(87,0.371644859754);
  S4_PT_0->SetBinContent(88,0.743289639508);
  S4_PT_0->SetBinContent(89,0.0);
  S4_PT_0->SetBinContent(90,0.0);
  S4_PT_0->SetBinContent(91,0.743289639508);
  S4_PT_0->SetBinContent(92,0.0);
  S4_PT_0->SetBinContent(93,0.0);
  S4_PT_0->SetBinContent(94,0.371644859754);
  S4_PT_0->SetBinContent(95,0.0);
  S4_PT_0->SetBinContent(96,0.371644859754);
  S4_PT_0->SetBinContent(97,0.371644859754);
  S4_PT_0->SetBinContent(98,0.0);
  S4_PT_0->SetBinContent(99,0.371644859754);
  S4_PT_0->SetBinContent(100,0.0);
  S4_PT_0->SetBinContent(101,1.48657967902); // overflow
  S4_PT_0->SetEntries(9999);
  // Style
  S4_PT_0->SetLineColor(9);
  S4_PT_0->SetLineStyle(1);
  S4_PT_0->SetLineWidth(1);
  S4_PT_0->SetFillColor(9);
  S4_PT_0->SetFillStyle(1001);

  // Creating a new THStack
  THStack* stack = new THStack("mystack_8","mystack");
  stack->Add(S4_PT_0);
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

  // Saving the image
  canvas->SaveAs("../../HTML/MadAnalysis5job_0/selection_3.png");
  canvas->SaveAs("../../PDF/MadAnalysis5job_0/selection_3.png");
  canvas->SaveAs("../../DVI/MadAnalysis5job_0/selection_3.eps");

}
