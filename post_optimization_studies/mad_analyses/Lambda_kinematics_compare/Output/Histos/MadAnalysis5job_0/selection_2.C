void selection_2()
{

  // ROOT version
  Int_t root_version = gROOT->GetVersionInt();

  // Creating a new TCanvas
  TCanvas* canvas = new TCanvas("canvas_plotflow_tempo5","canvas_plotflow_tempo5",0,0,1000,500);
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
  TH1F* S3_PHI_0 = new TH1F("S3_PHI_0","S3_PHI_0",64,-3.2,3.2);
  // Content
  S3_PHI_0->SetBinContent(0,0.0); // underflow
  S3_PHI_0->SetBinContent(1,1626.27534535);
  S3_PHI_0->SetBinContent(2,4878.82723604);
  S3_PHI_0->SetBinContent(3,6911.67091772);
  S3_PHI_0->SetBinContent(4,5691.96310871);
  S3_PHI_0->SetBinContent(5,4472.2552997);
  S3_PHI_0->SetBinContent(6,7318.23885405);
  S3_PHI_0->SetBinContent(7,4878.82723604);
  S3_PHI_0->SetBinContent(8,6505.09898138);
  S3_PHI_0->SetBinContent(9,6098.53104505);
  S3_PHI_0->SetBinContent(10,6911.67091772);
  S3_PHI_0->SetBinContent(11,7318.23885405);
  S3_PHI_0->SetBinContent(12,8944.5145994);
  S3_PHI_0->SetBinContent(13,5691.96310871);
  S3_PHI_0->SetBinContent(14,6098.53104505);
  S3_PHI_0->SetBinContent(15,6505.09898138);
  S3_PHI_0->SetBinContent(16,6098.53104505);
  S3_PHI_0->SetBinContent(17,6911.67091772);
  S3_PHI_0->SetBinContent(18,4065.68736336);
  S3_PHI_0->SetBinContent(19,5285.39517237);
  S3_PHI_0->SetBinContent(20,4878.82723604);
  S3_PHI_0->SetBinContent(21,7318.23885405);
  S3_PHI_0->SetBinContent(22,2845.98155435);
  S3_PHI_0->SetBinContent(23,5691.96310871);
  S3_PHI_0->SetBinContent(24,6505.09898138);
  S3_PHI_0->SetBinContent(25,5285.39517237);
  S3_PHI_0->SetBinContent(26,5691.96310871);
  S3_PHI_0->SetBinContent(27,8537.94666306);
  S3_PHI_0->SetBinContent(28,6098.53104505);
  S3_PHI_0->SetBinContent(29,4065.68736336);
  S3_PHI_0->SetBinContent(30,4065.68736336);
  S3_PHI_0->SetBinContent(31,6911.67091772);
  S3_PHI_0->SetBinContent(32,6505.09898138);
  S3_PHI_0->SetBinContent(33,7318.23885405);
  S3_PHI_0->SetBinContent(34,4472.2552997);
  S3_PHI_0->SetBinContent(35,6505.09898138);
  S3_PHI_0->SetBinContent(36,8944.5145994);
  S3_PHI_0->SetBinContent(37,7724.80679039);
  S3_PHI_0->SetBinContent(38,5285.39517237);
  S3_PHI_0->SetBinContent(39,6911.67091772);
  S3_PHI_0->SetBinContent(40,9757.65047207);
  S3_PHI_0->SetBinContent(41,7724.80679039);
  S3_PHI_0->SetBinContent(42,5285.39517237);
  S3_PHI_0->SetBinContent(43,7318.23885405);
  S3_PHI_0->SetBinContent(44,5691.96310871);
  S3_PHI_0->SetBinContent(45,6911.67091772);
  S3_PHI_0->SetBinContent(46,6098.53104505);
  S3_PHI_0->SetBinContent(47,7724.80679039);
  S3_PHI_0->SetBinContent(48,6911.67091772);
  S3_PHI_0->SetBinContent(49,5691.96310871);
  S3_PHI_0->SetBinContent(50,6098.53104505);
  S3_PHI_0->SetBinContent(51,7724.80679039);
  S3_PHI_0->SetBinContent(52,7724.80679039);
  S3_PHI_0->SetBinContent(53,8537.94666306);
  S3_PHI_0->SetBinContent(54,5691.96310871);
  S3_PHI_0->SetBinContent(55,6098.53104505);
  S3_PHI_0->SetBinContent(56,9351.08253574);
  S3_PHI_0->SetBinContent(57,6098.53104505);
  S3_PHI_0->SetBinContent(58,6505.09898138);
  S3_PHI_0->SetBinContent(59,7318.23885405);
  S3_PHI_0->SetBinContent(60,4878.82723604);
  S3_PHI_0->SetBinContent(61,8131.37472673);
  S3_PHI_0->SetBinContent(62,6911.67091772);
  S3_PHI_0->SetBinContent(63,9757.65047207);
  S3_PHI_0->SetBinContent(64,2439.41281802);
  S3_PHI_0->SetBinContent(65,0.0); // overflow
  S3_PHI_0->SetEntries(999);
  // Style
  S3_PHI_0->SetLineColor(9);
  S3_PHI_0->SetLineStyle(1);
  S3_PHI_0->SetLineWidth(1);
  S3_PHI_0->SetFillColor(9);
  S3_PHI_0->SetFillStyle(1001);

  // Creating a new TH1F
  TH1F* S3_PHI_1 = new TH1F("S3_PHI_1","S3_PHI_1",64,-3.2,3.2);
  // Content
  S3_PHI_1->SetBinContent(0,0.0); // underflow
  S3_PHI_1->SetBinContent(1,141.959877152);
  S3_PHI_1->SetBinContent(2,283.919809859);
  S3_PHI_1->SetBinContent(3,0.0);
  S3_PHI_1->SetBinContent(4,0.0);
  S3_PHI_1->SetBinContent(5,425.879687011);
  S3_PHI_1->SetBinContent(6,283.919809859);
  S3_PHI_1->SetBinContent(7,425.879687011);
  S3_PHI_1->SetBinContent(8,283.919809859);
  S3_PHI_1->SetBinContent(9,283.919809859);
  S3_PHI_1->SetBinContent(10,141.959877152);
  S3_PHI_1->SetBinContent(11,709.799385759);
  S3_PHI_1->SetBinContent(12,141.959877152);
  S3_PHI_1->SetBinContent(13,141.959877152);
  S3_PHI_1->SetBinContent(14,0.0);
  S3_PHI_1->SetBinContent(15,0.0);
  S3_PHI_1->SetBinContent(16,141.959877152);
  S3_PHI_1->SetBinContent(17,0.0);
  S3_PHI_1->SetBinContent(18,0.0);
  S3_PHI_1->SetBinContent(19,283.919809859);
  S3_PHI_1->SetBinContent(20,0.0);
  S3_PHI_1->SetBinContent(21,141.959877152);
  S3_PHI_1->SetBinContent(22,141.959877152);
  S3_PHI_1->SetBinContent(23,0.0);
  S3_PHI_1->SetBinContent(24,0.0);
  S3_PHI_1->SetBinContent(25,141.959877152);
  S3_PHI_1->SetBinContent(26,0.0);
  S3_PHI_1->SetBinContent(27,141.959877152);
  S3_PHI_1->SetBinContent(28,141.959877152);
  S3_PHI_1->SetBinContent(29,283.919809859);
  S3_PHI_1->SetBinContent(30,0.0);
  S3_PHI_1->SetBinContent(31,0.0);
  S3_PHI_1->SetBinContent(32,141.959877152);
  S3_PHI_1->SetBinContent(33,283.919809859);
  S3_PHI_1->SetBinContent(34,141.959877152);
  S3_PHI_1->SetBinContent(35,0.0);
  S3_PHI_1->SetBinContent(36,141.959877152);
  S3_PHI_1->SetBinContent(37,283.919809859);
  S3_PHI_1->SetBinContent(38,141.959877152);
  S3_PHI_1->SetBinContent(39,141.959877152);
  S3_PHI_1->SetBinContent(40,425.879687011);
  S3_PHI_1->SetBinContent(41,141.959877152);
  S3_PHI_1->SetBinContent(42,141.959877152);
  S3_PHI_1->SetBinContent(43,141.959877152);
  S3_PHI_1->SetBinContent(44,141.959877152);
  S3_PHI_1->SetBinContent(45,141.959877152);
  S3_PHI_1->SetBinContent(46,0.0);
  S3_PHI_1->SetBinContent(47,0.0);
  S3_PHI_1->SetBinContent(48,141.959877152);
  S3_PHI_1->SetBinContent(49,141.959877152);
  S3_PHI_1->SetBinContent(50,0.0);
  S3_PHI_1->SetBinContent(51,851.759262911);
  S3_PHI_1->SetBinContent(52,141.959877152);
  S3_PHI_1->SetBinContent(53,425.879687011);
  S3_PHI_1->SetBinContent(54,0.0);
  S3_PHI_1->SetBinContent(55,0.0);
  S3_PHI_1->SetBinContent(56,283.919809859);
  S3_PHI_1->SetBinContent(57,141.959877152);
  S3_PHI_1->SetBinContent(58,141.959877152);
  S3_PHI_1->SetBinContent(59,141.959877152);
  S3_PHI_1->SetBinContent(60,283.919809859);
  S3_PHI_1->SetBinContent(61,0.0);
  S3_PHI_1->SetBinContent(62,0.0);
  S3_PHI_1->SetBinContent(63,0.0);
  S3_PHI_1->SetBinContent(64,283.919809859);
  S3_PHI_1->SetBinContent(65,0.0); // overflow
  S3_PHI_1->SetEntries(71);
  // Style
  S3_PHI_1->SetLineColor(46);
  S3_PHI_1->SetLineStyle(1);
  S3_PHI_1->SetLineWidth(1);
  S3_PHI_1->SetFillColor(46);
  S3_PHI_1->SetFillStyle(1001);

  // Creating a new THStack
  THStack* stack = new THStack("mystack_6","mystack");
  stack->Add(S3_PHI_0);
  stack->Add(S3_PHI_1);
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

  // Creating a TLegend
  TLegend* legend = new TLegend(.73,.5,.97,.95);
  legend->AddEntry(S3_PHI_0,"signal1TeV");
  legend->AddEntry(S3_PHI_1,"signal4TeV");
  legend->SetFillColor(0);
  legend->SetTextSize(0.05);
  legend->SetTextFont(22);
  legend->SetY1(TMath::Max(0.15,0.97-0.10*legend->GetListOfPrimitives()->GetSize()));
  legend->Draw();

  // Saving the image
  canvas->SaveAs("../../HTML/MadAnalysis5job_0/selection_2.png");
  canvas->SaveAs("../../PDF/MadAnalysis5job_0/selection_2.png");
  canvas->SaveAs("../../DVI/MadAnalysis5job_0/selection_2.eps");

}
