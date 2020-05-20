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
  S6_PHI_0->SetBinContent(1,3409.13752713);
  S6_PHI_0->SetBinContent(2,4772.79301798);
  S6_PHI_0->SetBinContent(3,5795.53323612);
  S6_PHI_0->SetBinContent(4,8181.92974511);
  S6_PHI_0->SetBinContent(5,5454.6211634);
  S6_PHI_0->SetBinContent(6,5113.70509069);
  S6_PHI_0->SetBinContent(7,5113.70509069);
  S6_PHI_0->SetBinContent(8,6818.27345425);
  S6_PHI_0->SetBinContent(9,4772.79301798);
  S6_PHI_0->SetBinContent(10,3750.05159984);
  S6_PHI_0->SetBinContent(11,4090.96487255);
  S6_PHI_0->SetBinContent(12,5795.53323612);
  S6_PHI_0->SetBinContent(13,3750.05159984);
  S6_PHI_0->SetBinContent(14,5454.6211634);
  S6_PHI_0->SetBinContent(15,5795.53323612);
  S6_PHI_0->SetBinContent(16,6477.36138154);
  S6_PHI_0->SetBinContent(17,3068.22385441);
  S6_PHI_0->SetBinContent(18,5454.6211634);
  S6_PHI_0->SetBinContent(19,3750.05159984);
  S6_PHI_0->SetBinContent(20,4772.79301798);
  S6_PHI_0->SetBinContent(21,4431.88094527);
  S6_PHI_0->SetBinContent(22,4090.96487255);
  S6_PHI_0->SetBinContent(23,4772.79301798);
  S6_PHI_0->SetBinContent(24,6136.44930883);
  S6_PHI_0->SetBinContent(25,7159.18952697);
  S6_PHI_0->SetBinContent(26,5454.6211634);
  S6_PHI_0->SetBinContent(27,4090.96487255);
  S6_PHI_0->SetBinContent(28,5113.70509069);
  S6_PHI_0->SetBinContent(29,6136.44930883);
  S6_PHI_0->SetBinContent(30,6477.36138154);
  S6_PHI_0->SetBinContent(31,9545.58603596);
  S6_PHI_0->SetBinContent(32,5795.53323612);
  S6_PHI_0->SetBinContent(33,1704.56876356);
  S6_PHI_0->SetBinContent(34,5113.70509069);
  S6_PHI_0->SetBinContent(35,5454.6211634);
  S6_PHI_0->SetBinContent(36,6477.36138154);
  S6_PHI_0->SetBinContent(37,5795.53323612);
  S6_PHI_0->SetBinContent(38,4431.88094527);
  S6_PHI_0->SetBinContent(39,6136.44930883);
  S6_PHI_0->SetBinContent(40,6818.27345425);
  S6_PHI_0->SetBinContent(41,4090.96487255);
  S6_PHI_0->SetBinContent(42,6136.44930883);
  S6_PHI_0->SetBinContent(43,3068.22385441);
  S6_PHI_0->SetBinContent(44,5113.70509069);
  S6_PHI_0->SetBinContent(45,6818.27345425);
  S6_PHI_0->SetBinContent(46,4772.79301798);
  S6_PHI_0->SetBinContent(47,7500.10159968);
  S6_PHI_0->SetBinContent(48,7841.01767239);
  S6_PHI_0->SetBinContent(49,8181.92974511);
  S6_PHI_0->SetBinContent(50,5113.70509069);
  S6_PHI_0->SetBinContent(51,6136.44930883);
  S6_PHI_0->SetBinContent(52,3750.05159984);
  S6_PHI_0->SetBinContent(53,7159.18952697);
  S6_PHI_0->SetBinContent(54,5454.6211634);
  S6_PHI_0->SetBinContent(55,5113.70509069);
  S6_PHI_0->SetBinContent(56,5113.70509069);
  S6_PHI_0->SetBinContent(57,6136.44930883);
  S6_PHI_0->SetBinContent(58,6818.27345425);
  S6_PHI_0->SetBinContent(59,3068.22385441);
  S6_PHI_0->SetBinContent(60,5113.70509069);
  S6_PHI_0->SetBinContent(61,1704.56876356);
  S6_PHI_0->SetBinContent(62,5113.70509069);
  S6_PHI_0->SetBinContent(63,5454.6211634);
  S6_PHI_0->SetBinContent(64,3068.22385441);
  S6_PHI_0->SetBinContent(65,0.0); // overflow
  S6_PHI_0->SetEntries(999);
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
