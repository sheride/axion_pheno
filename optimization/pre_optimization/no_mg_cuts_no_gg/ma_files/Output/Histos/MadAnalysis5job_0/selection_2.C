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
  S3_PHI_0->SetBinContent(1,15.3442714055);
  S3_PHI_0->SetBinContent(2,36.9467605991);
  S3_PHI_0->SetBinContent(3,36.8800188974);
  S3_PHI_0->SetBinContent(4,37.242189368);
  S3_PHI_0->SetBinContent(5,37.4603910803);
  S3_PHI_0->SetBinContent(6,37.1257951341);
  S3_PHI_0->SetBinContent(7,36.6245687916);
  S3_PHI_0->SetBinContent(8,37.073136507);
  S3_PHI_0->SetBinContent(9,36.8290951708);
  S3_PHI_0->SetBinContent(10,37.0121271723);
  S3_PHI_0->SetBinContent(11,36.7945210825);
  S3_PHI_0->SetBinContent(12,37.1697432815);
  S3_PHI_0->SetBinContent(13,37.2322116915);
  S3_PHI_0->SetBinContent(14,36.7751333697);
  S3_PHI_0->SetBinContent(15,36.9375744209);
  S3_PHI_0->SetBinContent(16,36.7524597393);
  S3_PHI_0->SetBinContent(17,36.952389032);
  S3_PHI_0->SetBinContent(18,36.8680704698);
  S3_PHI_0->SetBinContent(19,36.609750183);
  S3_PHI_0->SetBinContent(20,36.7966717195);
  S3_PHI_0->SetBinContent(21,36.6687128148);
  S3_PHI_0->SetBinContent(22,37.0859723722);
  S3_PHI_0->SetBinContent(23,37.1349773148);
  S3_PHI_0->SetBinContent(24,37.3138119764);
  S3_PHI_0->SetBinContent(25,37.133042541);
  S3_PHI_0->SetBinContent(26,36.9583932268);
  S3_PHI_0->SetBinContent(27,36.4706903137);
  S3_PHI_0->SetBinContent(28,37.0221967906);
  S3_PHI_0->SetBinContent(29,36.8820735952);
  S3_PHI_0->SetBinContent(30,37.1057958089);
  S3_PHI_0->SetBinContent(31,36.6659305781);
  S3_PHI_0->SetBinContent(32,37.2280423338);
  S3_PHI_0->SetBinContent(33,37.0660090242);
  S3_PHI_0->SetBinContent(34,36.7870018479);
  S3_PHI_0->SetBinContent(35,36.2733154021);
  S3_PHI_0->SetBinContent(36,36.8073529502);
  S3_PHI_0->SetBinContent(37,37.2628682625);
  S3_PHI_0->SetBinContent(38,37.2205870587);
  S3_PHI_0->SetBinContent(39,37.6740916453);
  S3_PHI_0->SetBinContent(40,36.2318017119);
  S3_PHI_0->SetBinContent(41,36.9312784111);
  S3_PHI_0->SetBinContent(42,36.8658758607);
  S3_PHI_0->SetBinContent(43,36.8942258935);
  S3_PHI_0->SetBinContent(44,37.0399135624);
  S3_PHI_0->SetBinContent(45,37.0902696487);
  S3_PHI_0->SetBinContent(46,36.9866193382);
  S3_PHI_0->SetBinContent(47,36.1732388267);
  S3_PHI_0->SetBinContent(48,37.0174597927);
  S3_PHI_0->SetBinContent(49,36.4685476716);
  S3_PHI_0->SetBinContent(50,37.0658491255);
  S3_PHI_0->SetBinContent(51,37.1856452035);
  S3_PHI_0->SetBinContent(52,37.0997676293);
  S3_PHI_0->SetBinContent(53,37.5922555099);
  S3_PHI_0->SetBinContent(54,37.1126474665);
  S3_PHI_0->SetBinContent(55,37.1886153211);
  S3_PHI_0->SetBinContent(56,37.2931530692);
  S3_PHI_0->SetBinContent(57,36.9055627087);
  S3_PHI_0->SetBinContent(58,36.7313571133);
  S3_PHI_0->SetBinContent(59,37.3311290016);
  S3_PHI_0->SetBinContent(60,36.8613787108);
  S3_PHI_0->SetBinContent(61,37.1822873315);
  S3_PHI_0->SetBinContent(62,36.5363726868);
  S3_PHI_0->SetBinContent(63,36.6469226246);
  S3_PHI_0->SetBinContent(64,15.4905586943);
  S3_PHI_0->SetBinContent(65,0.0); // overflow
  S3_PHI_0->SetEntries(999999);
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
