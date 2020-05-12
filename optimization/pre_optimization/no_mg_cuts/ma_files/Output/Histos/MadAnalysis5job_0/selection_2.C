void selection_2()
{

  // ROOT version
  Int_t root_version = gROOT->GetVersionInt();

  // Creating a new TCanvas
  TCanvas* canvas = new TCanvas("canvas_plotflow_tempo5","canvas_plotflow_tempo5",0,0,700,500);
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
  TH1F* S3_PHI_0 = new TH1F("S3_PHI_0","S3_PHI_0",64,-3.2,3.2);
  // Content
  S3_PHI_0->SetBinContent(0,0.0); // underflow
  S3_PHI_0->SetBinContent(1,257.809615257);
  S3_PHI_0->SetBinContent(2,569.067633677);
  S3_PHI_0->SetBinContent(3,474.746828095);
  S3_PHI_0->SetBinContent(4,528.195231258);
  S3_PHI_0->SetBinContent(5,474.746828095);
  S3_PHI_0->SetBinContent(6,493.611229211);
  S3_PHI_0->SetBinContent(7,455.882826978);
  S3_PHI_0->SetBinContent(8,493.611229211);
  S3_PHI_0->SetBinContent(9,493.611229211);
  S3_PHI_0->SetBinContent(10,547.059232374);
  S3_PHI_0->SetBinContent(11,550.20323256);
  S3_PHI_0->SetBinContent(12,512.475230328);
  S3_PHI_0->SetBinContent(13,443.306826234);
  S3_PHI_0->SetBinContent(14,512.475230328);
  S3_PHI_0->SetBinContent(15,443.306826234);
  S3_PHI_0->SetBinContent(16,509.331230141);
  S3_PHI_0->SetBinContent(17,477.890828281);
  S3_PHI_0->SetBinContent(18,465.314827537);
  S3_PHI_0->SetBinContent(19,512.475230328);
  S3_PHI_0->SetBinContent(20,493.611229211);
  S3_PHI_0->SetBinContent(21,490.467229025);
  S3_PHI_0->SetBinContent(22,462.170827351);
  S3_PHI_0->SetBinContent(23,525.051231072);
  S3_PHI_0->SetBinContent(24,499.899229583);
  S3_PHI_0->SetBinContent(25,477.890828281);
  S3_PHI_0->SetBinContent(26,474.746828095);
  S3_PHI_0->SetBinContent(27,521.907230886);
  S3_PHI_0->SetBinContent(28,506.187229955);
  S3_PHI_0->SetBinContent(29,540.771232002);
  S3_PHI_0->SetBinContent(30,493.611229211);
  S3_PHI_0->SetBinContent(31,503.043229769);
  S3_PHI_0->SetBinContent(32,531.339231444);
  S3_PHI_0->SetBinContent(33,525.051231072);
  S3_PHI_0->SetBinContent(34,550.20323256);
  S3_PHI_0->SetBinContent(35,474.746828095);
  S3_PHI_0->SetBinContent(36,509.331230141);
  S3_PHI_0->SetBinContent(37,515.619230514);
  S3_PHI_0->SetBinContent(38,474.746828095);
  S3_PHI_0->SetBinContent(39,474.746828095);
  S3_PHI_0->SetBinContent(40,553.347632746);
  S3_PHI_0->SetBinContent(41,503.043229769);
  S3_PHI_0->SetBinContent(42,531.339231444);
  S3_PHI_0->SetBinContent(43,503.043229769);
  S3_PHI_0->SetBinContent(44,484.178828653);
  S3_PHI_0->SetBinContent(45,562.779633304);
  S3_PHI_0->SetBinContent(46,493.611229211);
  S3_PHI_0->SetBinContent(47,521.907230886);
  S3_PHI_0->SetBinContent(48,446.45082642);
  S3_PHI_0->SetBinContent(49,515.619230514);
  S3_PHI_0->SetBinContent(50,452.738826792);
  S3_PHI_0->SetBinContent(51,440.162826048);
  S3_PHI_0->SetBinContent(52,449.594826606);
  S3_PHI_0->SetBinContent(53,462.170827351);
  S3_PHI_0->SetBinContent(54,512.475230328);
  S3_PHI_0->SetBinContent(55,452.738826792);
  S3_PHI_0->SetBinContent(56,459.026827165);
  S3_PHI_0->SetBinContent(57,503.043229769);
  S3_PHI_0->SetBinContent(58,534.48323163);
  S3_PHI_0->SetBinContent(59,462.170827351);
  S3_PHI_0->SetBinContent(60,531.339231444);
  S3_PHI_0->SetBinContent(61,427.586825304);
  S3_PHI_0->SetBinContent(62,556.491632932);
  S3_PHI_0->SetBinContent(63,600.507635537);
  S3_PHI_0->SetBinContent(64,216.937332838);
  S3_PHI_0->SetBinContent(65,0.0); // overflow
  S3_PHI_0->SetEntries(9999);
  // Style
  S3_PHI_0->SetLineColor(9);
  S3_PHI_0->SetLineStyle(1);
  S3_PHI_0->SetLineWidth(1);
  S3_PHI_0->SetFillColor(9);
  S3_PHI_0->SetFillStyle(1001);

  // Creating a new THStack
  THStack* stack = new THStack("mystack_6","mystack");
  stack->Add(S3_PHI_0);
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
  stack->GetXaxis()->SetTitle("#phi [ j_{1} ] ");

  // Finalizing the TCanvas
  canvas->SetLogx(0);
  canvas->SetLogy(0);

  // Saving the image
  canvas->SaveAs("../../HTML/MadAnalysis5job_0/selection_2.png");
  canvas->SaveAs("../../PDF/MadAnalysis5job_0/selection_2.png");
  canvas->SaveAs("../../DVI/MadAnalysis5job_0/selection_2.eps");

}
