void selection_12()
{

  // ROOT version
  Int_t root_version = gROOT->GetVersionInt();

  // Creating a new TCanvas
  TCanvas* canvas = new TCanvas("canvas_plotflow_tempo25","canvas_plotflow_tempo25",0,0,700,500);
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
  TH1F* S13_THT_0 = new TH1F("S13_THT_0","S13_THT_0",80,0.0,4000.0);
  // Content
  S13_THT_0->SetBinContent(0,0.0); // underflow
  S13_THT_0->SetBinContent(1,16.5756262382);
  S13_THT_0->SetBinContent(2,191.779996255);
  S13_THT_0->SetBinContent(3,355.264560277);
  S13_THT_0->SetBinContent(4,550.188271231);
  S13_THT_0->SetBinContent(5,657.08217078);
  S13_THT_0->SetBinContent(6,754.544326249);
  S13_THT_0->SetBinContent(7,924.316519663);
  S13_THT_0->SetBinContent(8,958.899981277);
  S13_THT_0->SetBinContent(9,980.90738413);
  S13_THT_0->SetBinContent(10,984.051298823);
  S13_THT_0->SetBinContent(11,1046.92999268);
  S13_THT_0->SetBinContent(12,1122.3843453);
  S13_THT_0->SetBinContent(13,1147.53606284);
  S13_THT_0->SetBinContent(14,1197.83869793);
  S13_THT_0->SetBinContent(15,1270.14953585);
  S13_THT_0->SetBinContent(16,1185.26303916);
  S13_THT_0->SetBinContent(17,1125.52826);
  S13_THT_0->SetBinContent(18,1116.09651592);
  S13_THT_0->SetBinContent(19,984.051298823);
  S13_THT_0->SetBinContent(20,1040.64216329);
  S13_THT_0->SetBinContent(21,1034.3543339);
  S13_THT_0->SetBinContent(22,1021.77867513);
  S13_THT_0->SetBinContent(23,902.30911681);
  S13_THT_0->SetBinContent(24,839.430422956);
  S13_THT_0->SetBinContent(25,817.423020103);
  S13_THT_0->SetBinContent(26,738.824352794);
  S13_THT_0->SetBinContent(27,701.097376475);
  S13_THT_0->SetBinContent(28,657.08217078);
  S13_THT_0->SetBinContent(29,653.938256087);
  S13_THT_0->SetBinContent(30,553.332585914);
  S13_THT_0->SetBinContent(31,534.468697765);
  S13_THT_0->SetBinContent(32,468.446089218);
  S13_THT_0->SetBinContent(33,462.158259831);
  S13_THT_0->SetBinContent(34,468.446089218);
  S13_THT_0->SetBinContent(35,402.42348067);
  S13_THT_0->SetBinContent(36,295.529821115);
  S13_THT_0->SetBinContent(37,308.105519887);
  S13_THT_0->SetBinContent(38,279.810127652);
  S13_THT_0->SetBinContent(39,260.946519496);
  S13_THT_0->SetBinContent(40,216.931433798);
  S13_THT_0->SetBinContent(41,220.07538849);
  S13_THT_0->SetBinContent(42,166.628518714);
  S13_THT_0->SetBinContent(43,166.628518714);
  S13_THT_0->SetBinContent(44,172.916388099);
  S13_THT_0->SetBinContent(45,157.196694636);
  S13_THT_0->SetBinContent(46,135.189171787);
  S13_THT_0->SetBinContent(47,97.4619554744);
  S13_THT_0->SetBinContent(48,97.4619554744);
  S13_THT_0->SetBinContent(49,91.174086089);
  S13_THT_0->SetBinContent(50,100.605870168);
  S13_THT_0->SetBinContent(51,72.3104779327);
  S13_THT_0->SetBinContent(52,72.3104779327);
  S13_THT_0->SetBinContent(53,62.8786938541);
  S13_THT_0->SetBinContent(54,91.174086089);
  S13_THT_0->SetBinContent(55,59.7347391619);
  S13_THT_0->SetBinContent(56,50.3029550833);
  S13_THT_0->SetBinContent(57,44.0150856979);
  S13_THT_0->SetBinContent(58,28.2954082344);
  S13_THT_0->SetBinContent(59,37.7272083127);
  S13_THT_0->SetBinContent(60,25.1514735417);
  S13_THT_0->SetBinContent(61,40.8711310057);
  S13_THT_0->SetBinContent(62,22.007538849);
  S13_THT_0->SetBinContent(63,28.2954082344);
  S13_THT_0->SetBinContent(64,9.43180407811);
  S13_THT_0->SetBinContent(65,9.43180407811);
  S13_THT_0->SetBinContent(66,18.8636041563);
  S13_THT_0->SetBinContent(67,9.43180407811);
  S13_THT_0->SetBinContent(68,15.7196694636);
  S13_THT_0->SetBinContent(69,3.14393389273);
  S13_THT_0->SetBinContent(70,12.5757347709);
  S13_THT_0->SetBinContent(71,15.7196694636);
  S13_THT_0->SetBinContent(72,15.7196694636);
  S13_THT_0->SetBinContent(73,3.14393389273);
  S13_THT_0->SetBinContent(74,9.43180407811);
  S13_THT_0->SetBinContent(75,12.5757347709);
  S13_THT_0->SetBinContent(76,12.5757347709);
  S13_THT_0->SetBinContent(77,3.14393389273);
  S13_THT_0->SetBinContent(78,3.14393389273);
  S13_THT_0->SetBinContent(79,0.0);
  S13_THT_0->SetBinContent(80,3.14393389273);
  S13_THT_0->SetBinContent(81,15.7196694636); // overflow
  S13_THT_0->SetEntries(10000);
  // Style
  S13_THT_0->SetLineColor(9);
  S13_THT_0->SetLineStyle(1);
  S13_THT_0->SetLineWidth(1);
  S13_THT_0->SetFillColor(9);
  S13_THT_0->SetFillStyle(1001);

  // Creating a new THStack
  THStack* stack = new THStack("mystack_26","mystack");
  stack->Add(S13_THT_0);
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
  stack->GetXaxis()->SetTitle("THT");

  // Finalizing the TCanvas
  canvas->SetLogx(0);
  canvas->SetLogy(0);

  // Saving the image
  canvas->SaveAs("../../HTML/MadAnalysis5job_0/selection_12.png");
  canvas->SaveAs("../../PDF/MadAnalysis5job_0/selection_12.png");
  canvas->SaveAs("../../DVI/MadAnalysis5job_0/selection_12.eps");

}
