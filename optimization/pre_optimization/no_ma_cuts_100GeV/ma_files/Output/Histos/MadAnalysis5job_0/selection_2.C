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
  S3_PHI_0->SetBinContent(1,1363.6550396);
  S3_PHI_0->SetBinContent(2,4772.7928386);
  S3_PHI_0->SetBinContent(3,5113.7048985);
  S3_PHI_0->SetBinContent(4,4772.7928386);
  S3_PHI_0->SetBinContent(5,5113.7048985);
  S3_PHI_0->SetBinContent(6,5795.5330183);
  S3_PHI_0->SetBinContent(7,4772.7928386);
  S3_PHI_0->SetBinContent(8,4090.9647188);
  S3_PHI_0->SetBinContent(9,7841.0173777);
  S3_PHI_0->SetBinContent(10,7500.1013178);
  S3_PHI_0->SetBinContent(11,8522.8454975);
  S3_PHI_0->SetBinContent(12,4431.8807787);
  S3_PHI_0->SetBinContent(13,5454.6209584);
  S3_PHI_0->SetBinContent(14,5113.7048985);
  S3_PHI_0->SetBinContent(15,5113.7048985);
  S3_PHI_0->SetBinContent(16,3750.0514589);
  S3_PHI_0->SetBinContent(17,4772.7928386);
  S3_PHI_0->SetBinContent(18,5454.6209584);
  S3_PHI_0->SetBinContent(19,5113.7048985);
  S3_PHI_0->SetBinContent(20,6477.3611381);
  S3_PHI_0->SetBinContent(21,4090.9647188);
  S3_PHI_0->SetBinContent(22,5795.5330183);
  S3_PHI_0->SetBinContent(23,6136.4490782);
  S3_PHI_0->SetBinContent(24,5795.5330183);
  S3_PHI_0->SetBinContent(25,3068.2237391);
  S3_PHI_0->SetBinContent(26,5454.6209584);
  S3_PHI_0->SetBinContent(27,4772.7928386);
  S3_PHI_0->SetBinContent(28,6477.3611381);
  S3_PHI_0->SetBinContent(29,8522.8454975);
  S3_PHI_0->SetBinContent(30,6136.4490782);
  S3_PHI_0->SetBinContent(31,4772.7928386);
  S3_PHI_0->SetBinContent(32,4772.7928386);
  S3_PHI_0->SetBinContent(33,4772.7928386);
  S3_PHI_0->SetBinContent(34,5795.5330183);
  S3_PHI_0->SetBinContent(35,5454.6209584);
  S3_PHI_0->SetBinContent(36,3409.137399);
  S3_PHI_0->SetBinContent(37,5795.5330183);
  S3_PHI_0->SetBinContent(38,5113.7048985);
  S3_PHI_0->SetBinContent(39,4431.8807787);
  S3_PHI_0->SetBinContent(40,4431.8807787);
  S3_PHI_0->SetBinContent(41,5113.7048985);
  S3_PHI_0->SetBinContent(42,8522.8454975);
  S3_PHI_0->SetBinContent(43,5113.7048985);
  S3_PHI_0->SetBinContent(44,2386.3964193);
  S3_PHI_0->SetBinContent(45,4431.8807787);
  S3_PHI_0->SetBinContent(46,4090.9647188);
  S3_PHI_0->SetBinContent(47,4772.7928386);
  S3_PHI_0->SetBinContent(48,5454.6209584);
  S3_PHI_0->SetBinContent(49,7500.1013178);
  S3_PHI_0->SetBinContent(50,3409.137399);
  S3_PHI_0->SetBinContent(51,5795.5330183);
  S3_PHI_0->SetBinContent(52,6818.273198);
  S3_PHI_0->SetBinContent(53,5454.6209584);
  S3_PHI_0->SetBinContent(54,4772.7928386);
  S3_PHI_0->SetBinContent(55,5795.5330183);
  S3_PHI_0->SetBinContent(56,6136.4490782);
  S3_PHI_0->SetBinContent(57,5113.7048985);
  S3_PHI_0->SetBinContent(58,5454.6209584);
  S3_PHI_0->SetBinContent(59,4431.8807787);
  S3_PHI_0->SetBinContent(60,5795.5330183);
  S3_PHI_0->SetBinContent(61,6136.4490782);
  S3_PHI_0->SetBinContent(62,7841.0173777);
  S3_PHI_0->SetBinContent(63,7500.1013178);
  S3_PHI_0->SetBinContent(64,2386.3964193);
  S3_PHI_0->SetBinContent(65,0.0); // overflow
  S3_PHI_0->SetEntries(999);
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
