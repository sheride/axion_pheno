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
  S13_THT_0->SetBinContent(1,9.93661580303);
  S13_THT_0->SetBinContent(2,114.726283364);
  S13_THT_0->SetBinContent(3,170.418636082);
  S13_THT_0->SetBinContent(4,193.438124289);
  S13_THT_0->SetBinContent(5,227.596099025);
  S13_THT_0->SetBinContent(6,232.422787177);
  S13_THT_0->SetBinContent(7,210.517131638);
  S13_THT_0->SetBinContent(8,240.219735738);
  S13_THT_0->SetBinContent(9,205.690443486);
  S13_THT_0->SetBinContent(10,195.294552031);
  S13_THT_0->SetBinContent(11,199.749922666);
  S13_THT_0->SetBinContent(12,184.527343059);
  S13_THT_0->SetBinContent(13,187.868881025);
  S13_THT_0->SetBinContent(14,158.537594442);
  S13_THT_0->SetBinContent(15,132.547805863);
  S13_THT_0->SetBinContent(16,135.889343829);
  S13_THT_0->SetBinContent(17,115.840116032);
  S13_THT_0->SetBinContent(18,105.444184616);
  S13_THT_0->SetBinContent(19,96.16212583);
  S13_THT_0->SetBinContent(20,80.1969911112);
  S13_THT_0->SetBinContent(21,76.1128980327);
  S13_THT_0->SetBinContent(22,64.2318563924);
  S13_THT_0->SetBinContent(23,52.350814752);
  S13_THT_0->SetBinContent(24,56.0636302744);
  S13_THT_0->SetBinContent(25,35.6431129327);
  S13_THT_0->SetBinContent(26,35.6431129327);
  S13_THT_0->SetBinContent(27,31.5590038698);
  S13_THT_0->SetBinContent(28,22.2769450834);
  S13_THT_0->SetBinContent(29,24.5046383929);
  S13_THT_0->SetBinContent(30,21.1630964306);
  S13_THT_0->SetBinContent(31,14.480012506);
  S13_THT_0->SetBinContent(32,14.8512980543);
  S13_THT_0->SetBinContent(33,11.509756092);
  S13_THT_0->SetBinContent(34,10.0246258869);
  S13_THT_0->SetBinContent(35,6.68308392463);
  S13_THT_0->SetBinContent(36,4.45539061512);
  S13_THT_0->SetBinContent(37,4.82667216735);
  S13_THT_0->SetBinContent(38,6.31180237239);
  S13_THT_0->SetBinContent(39,2.97025921125);
  S13_THT_0->SetBinContent(40,3.34154156271);
  S13_THT_0->SetBinContent(41,3.34154156271);
  S13_THT_0->SetBinContent(42,4.08410506679);
  S13_THT_0->SetBinContent(43,1.48512980543);
  S13_THT_0->SetBinContent(44,0.74256470291);
  S13_THT_0->SetBinContent(45,2.22769450834);
  S13_THT_0->SetBinContent(46,0.74256470291);
  S13_THT_0->SetBinContent(47,1.48512980543);
  S13_THT_0->SetBinContent(48,1.48512980543);
  S13_THT_0->SetBinContent(49,1.85641215688);
  S13_THT_0->SetBinContent(50,0.0);
  S13_THT_0->SetBinContent(51,1.48512980543);
  S13_THT_0->SetBinContent(52,0.74256470291);
  S13_THT_0->SetBinContent(53,0.371282391416);
  S13_THT_0->SetBinContent(54,0.0);
  S13_THT_0->SetBinContent(55,0.0);
  S13_THT_0->SetBinContent(56,0.0);
  S13_THT_0->SetBinContent(57,0.371282391416);
  S13_THT_0->SetBinContent(58,0.0);
  S13_THT_0->SetBinContent(59,0.0);
  S13_THT_0->SetBinContent(60,0.0);
  S13_THT_0->SetBinContent(61,0.0);
  S13_THT_0->SetBinContent(62,0.0);
  S13_THT_0->SetBinContent(63,0.0);
  S13_THT_0->SetBinContent(64,0.0);
  S13_THT_0->SetBinContent(65,0.0);
  S13_THT_0->SetBinContent(66,0.0);
  S13_THT_0->SetBinContent(67,0.0);
  S13_THT_0->SetBinContent(68,0.0);
  S13_THT_0->SetBinContent(69,0.0);
  S13_THT_0->SetBinContent(70,0.0);
  S13_THT_0->SetBinContent(71,0.0);
  S13_THT_0->SetBinContent(72,0.0);
  S13_THT_0->SetBinContent(73,0.0);
  S13_THT_0->SetBinContent(74,0.0);
  S13_THT_0->SetBinContent(75,0.0);
  S13_THT_0->SetBinContent(76,0.0);
  S13_THT_0->SetBinContent(77,0.0);
  S13_THT_0->SetBinContent(78,0.0);
  S13_THT_0->SetBinContent(79,0.0);
  S13_THT_0->SetBinContent(80,0.0);
  S13_THT_0->SetBinContent(81,0.0); // overflow
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
