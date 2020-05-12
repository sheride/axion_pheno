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
  S3_PHI_0->SetBinContent(1,23.0419811851);
  S3_PHI_0->SetBinContent(2,60.9497631347);
  S3_PHI_0->SetBinContent(3,59.4631630582);
  S3_PHI_0->SetBinContent(4,55.0034428289);
  S3_PHI_0->SetBinContent(5,64.2945633067);
  S3_PHI_0->SetBinContent(6,63.1796432494);
  S3_PHI_0->SetBinContent(7,59.4631630582);
  S3_PHI_0->SetBinContent(8,65.0378433449);
  S3_PHI_0->SetBinContent(9,65.0378433449);
  S3_PHI_0->SetBinContent(10,53.8885227715);
  S3_PHI_0->SetBinContent(11,60.2064830965);
  S3_PHI_0->SetBinContent(12,66.5244434214);
  S3_PHI_0->SetBinContent(13,53.1452027333);
  S3_PHI_0->SetBinContent(14,58.71988302);
  S3_PHI_0->SetBinContent(15,55.375082848);
  S3_PHI_0->SetBinContent(16,57.9766029818);
  S3_PHI_0->SetBinContent(17,59.0915230391);
  S3_PHI_0->SetBinContent(18,70.9841636508);
  S3_PHI_0->SetBinContent(19,60.2064830965);
  S3_PHI_0->SetBinContent(20,62.064683192);
  S3_PHI_0->SetBinContent(21,55.0034428289);
  S3_PHI_0->SetBinContent(22,55.0034428289);
  S3_PHI_0->SetBinContent(23,59.8348430773);
  S3_PHI_0->SetBinContent(24,61.3214031538);
  S3_PHI_0->SetBinContent(25,59.0915230391);
  S3_PHI_0->SetBinContent(26,53.8885227715);
  S3_PHI_0->SetBinContent(27,63.5512832685);
  S3_PHI_0->SetBinContent(28,60.9497631347);
  S3_PHI_0->SetBinContent(29,57.2333229435);
  S3_PHI_0->SetBinContent(30,52.7735627142);
  S3_PHI_0->SetBinContent(31,52.4019226951);
  S3_PHI_0->SetBinContent(32,63.1796432494);
  S3_PHI_0->SetBinContent(33,60.9497631347);
  S3_PHI_0->SetBinContent(34,56.8616829244);
  S3_PHI_0->SetBinContent(35,58.3482430009);
  S3_PHI_0->SetBinContent(36,61.6930431729);
  S3_PHI_0->SetBinContent(37,52.0302826759);
  S3_PHI_0->SetBinContent(38,56.4900029053);
  S3_PHI_0->SetBinContent(39,56.8616829244);
  S3_PHI_0->SetBinContent(40,60.9497631347);
  S3_PHI_0->SetBinContent(41,52.7735627142);
  S3_PHI_0->SetBinContent(42,62.4363232111);
  S3_PHI_0->SetBinContent(43,59.8348430773);
  S3_PHI_0->SetBinContent(44,60.5781231156);
  S3_PHI_0->SetBinContent(45,63.1796432494);
  S3_PHI_0->SetBinContent(46,55.7467228671);
  S3_PHI_0->SetBinContent(47,61.6930431729);
  S3_PHI_0->SetBinContent(48,55.7467228671);
  S3_PHI_0->SetBinContent(49,57.2333229435);
  S3_PHI_0->SetBinContent(50,59.8348430773);
  S3_PHI_0->SetBinContent(51,60.9497631347);
  S3_PHI_0->SetBinContent(52,58.71988302);
  S3_PHI_0->SetBinContent(53,60.5781231156);
  S3_PHI_0->SetBinContent(54,61.6930431729);
  S3_PHI_0->SetBinContent(55,61.6930431729);
  S3_PHI_0->SetBinContent(56,62.064683192);
  S3_PHI_0->SetBinContent(57,66.1528034023);
  S3_PHI_0->SetBinContent(58,55.7467228671);
  S3_PHI_0->SetBinContent(59,56.4900029053);
  S3_PHI_0->SetBinContent(60,61.3214031538);
  S3_PHI_0->SetBinContent(61,49.4287625421);
  S3_PHI_0->SetBinContent(62,56.8616829244);
  S3_PHI_0->SetBinContent(63,59.8348430773);
  S3_PHI_0->SetBinContent(64,23.4136252042);
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
