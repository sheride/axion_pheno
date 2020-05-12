void selection_5()
{

  // ROOT version
  Int_t root_version = gROOT->GetVersionInt();

  // Creating a new TCanvas
  TCanvas* canvas = new TCanvas("canvas_plotflow_tempo11","canvas_plotflow_tempo11",0,0,700,500);
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
  TH1F* S6_PHI_0 = new TH1F("S6_PHI_0","S6_PHI_0",64,-3.2,3.2);
  // Content
  S6_PHI_0->SetBinContent(0,0.0); // underflow
  S6_PHI_0->SetBinContent(1,238.945492924);
  S6_PHI_0->SetBinContent(2,493.611226699);
  S6_PHI_0->SetBinContent(3,547.05922959);
  S6_PHI_0->SetBinContent(4,440.162823808);
  S6_PHI_0->SetBinContent(5,474.746825679);
  S6_PHI_0->SetBinContent(6,487.323226359);
  S6_PHI_0->SetBinContent(7,550.20322976);
  S6_PHI_0->SetBinContent(8,424.442822958);
  S6_PHI_0->SetBinContent(9,465.314825168);
  S6_PHI_0->SetBinContent(10,521.907228229);
  S6_PHI_0->SetBinContent(11,512.475227719);
  S6_PHI_0->SetBinContent(12,430.730823298);
  S6_PHI_0->SetBinContent(13,521.907228229);
  S6_PHI_0->SetBinContent(14,490.467226529);
  S6_PHI_0->SetBinContent(15,465.314825168);
  S6_PHI_0->SetBinContent(16,600.507632481);
  S6_PHI_0->SetBinContent(17,525.0512284);
  S6_PHI_0->SetBinContent(18,547.05922959);
  S6_PHI_0->SetBinContent(19,537.62722908);
  S6_PHI_0->SetBinContent(20,543.91522942);
  S6_PHI_0->SetBinContent(21,531.33922874);
  S6_PHI_0->SetBinContent(22,490.467226529);
  S6_PHI_0->SetBinContent(23,427.586823128);
  S6_PHI_0->SetBinContent(24,433.874823468);
  S6_PHI_0->SetBinContent(25,569.06763078);
  S6_PHI_0->SetBinContent(26,565.92363061);
  S6_PHI_0->SetBinContent(27,496.755226869);
  S6_PHI_0->SetBinContent(28,509.331227549);
  S6_PHI_0->SetBinContent(29,462.170824998);
  S6_PHI_0->SetBinContent(30,496.755226869);
  S6_PHI_0->SetBinContent(31,528.19522857);
  S6_PHI_0->SetBinContent(32,433.874823468);
  S6_PHI_0->SetBinContent(33,521.907228229);
  S6_PHI_0->SetBinContent(34,481.034826019);
  S6_PHI_0->SetBinContent(35,443.306823978);
  S6_PHI_0->SetBinContent(36,490.467226529);
  S6_PHI_0->SetBinContent(37,543.91522942);
  S6_PHI_0->SetBinContent(38,518.763228059);
  S6_PHI_0->SetBinContent(39,506.187227379);
  S6_PHI_0->SetBinContent(40,462.170824998);
  S6_PHI_0->SetBinContent(41,465.314825168);
  S6_PHI_0->SetBinContent(42,496.755226869);
  S6_PHI_0->SetBinContent(43,537.62722908);
  S6_PHI_0->SetBinContent(44,528.19522857);
  S6_PHI_0->SetBinContent(45,509.331227549);
  S6_PHI_0->SetBinContent(46,449.594824318);
  S6_PHI_0->SetBinContent(47,503.043227209);
  S6_PHI_0->SetBinContent(48,481.034826019);
  S6_PHI_0->SetBinContent(49,474.746825679);
  S6_PHI_0->SetBinContent(50,559.63563027);
  S6_PHI_0->SetBinContent(51,534.48322891);
  S6_PHI_0->SetBinContent(52,575.35563112);
  S6_PHI_0->SetBinContent(53,418.154422618);
  S6_PHI_0->SetBinContent(54,499.899227039);
  S6_PHI_0->SetBinContent(55,543.91522942);
  S6_PHI_0->SetBinContent(56,437.018823638);
  S6_PHI_0->SetBinContent(57,506.187227379);
  S6_PHI_0->SetBinContent(58,477.890825849);
  S6_PHI_0->SetBinContent(59,528.19522857);
  S6_PHI_0->SetBinContent(60,455.882824658);
  S6_PHI_0->SetBinContent(61,515.619227889);
  S6_PHI_0->SetBinContent(62,512.475227719);
  S6_PHI_0->SetBinContent(63,503.043227209);
  S6_PHI_0->SetBinContent(64,191.785210373);
  S6_PHI_0->SetBinContent(65,0.0); // overflow
  S6_PHI_0->SetEntries(9999);
  // Style
  S6_PHI_0->SetLineColor(9);
  S6_PHI_0->SetLineStyle(1);
  S6_PHI_0->SetLineWidth(1);
  S6_PHI_0->SetFillColor(9);
  S6_PHI_0->SetFillStyle(1001);

  // Creating a new THStack
  THStack* stack = new THStack("mystack_12","mystack");
  stack->Add(S6_PHI_0);
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
  stack->GetXaxis()->SetTitle("#phi [ j_{2} ] ");

  // Finalizing the TCanvas
  canvas->SetLogx(0);
  canvas->SetLogy(0);

  // Saving the image
  canvas->SaveAs("../../HTML/MadAnalysis5job_0/selection_5.png");
  canvas->SaveAs("../../PDF/MadAnalysis5job_0/selection_5.png");
  canvas->SaveAs("../../DVI/MadAnalysis5job_0/selection_5.eps");

}
