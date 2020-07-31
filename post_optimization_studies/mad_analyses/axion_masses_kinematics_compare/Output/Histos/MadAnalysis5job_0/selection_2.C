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
  S3_PHI_1->SetBinContent(1,1363.6550396);
  S3_PHI_1->SetBinContent(2,4772.7928386);
  S3_PHI_1->SetBinContent(3,5113.7048985);
  S3_PHI_1->SetBinContent(4,4772.7928386);
  S3_PHI_1->SetBinContent(5,5113.7048985);
  S3_PHI_1->SetBinContent(6,5795.5330183);
  S3_PHI_1->SetBinContent(7,4772.7928386);
  S3_PHI_1->SetBinContent(8,4090.9647188);
  S3_PHI_1->SetBinContent(9,7841.0173777);
  S3_PHI_1->SetBinContent(10,7500.1013178);
  S3_PHI_1->SetBinContent(11,8522.8454975);
  S3_PHI_1->SetBinContent(12,4431.8807787);
  S3_PHI_1->SetBinContent(13,5454.6209584);
  S3_PHI_1->SetBinContent(14,5113.7048985);
  S3_PHI_1->SetBinContent(15,5113.7048985);
  S3_PHI_1->SetBinContent(16,3750.0514589);
  S3_PHI_1->SetBinContent(17,4772.7928386);
  S3_PHI_1->SetBinContent(18,5454.6209584);
  S3_PHI_1->SetBinContent(19,5113.7048985);
  S3_PHI_1->SetBinContent(20,6477.3611381);
  S3_PHI_1->SetBinContent(21,4090.9647188);
  S3_PHI_1->SetBinContent(22,5795.5330183);
  S3_PHI_1->SetBinContent(23,6136.4490782);
  S3_PHI_1->SetBinContent(24,5795.5330183);
  S3_PHI_1->SetBinContent(25,3068.2237391);
  S3_PHI_1->SetBinContent(26,5454.6209584);
  S3_PHI_1->SetBinContent(27,4772.7928386);
  S3_PHI_1->SetBinContent(28,6477.3611381);
  S3_PHI_1->SetBinContent(29,8522.8454975);
  S3_PHI_1->SetBinContent(30,6136.4490782);
  S3_PHI_1->SetBinContent(31,4772.7928386);
  S3_PHI_1->SetBinContent(32,4772.7928386);
  S3_PHI_1->SetBinContent(33,4772.7928386);
  S3_PHI_1->SetBinContent(34,5795.5330183);
  S3_PHI_1->SetBinContent(35,5454.6209584);
  S3_PHI_1->SetBinContent(36,3409.137399);
  S3_PHI_1->SetBinContent(37,5795.5330183);
  S3_PHI_1->SetBinContent(38,5113.7048985);
  S3_PHI_1->SetBinContent(39,4431.8807787);
  S3_PHI_1->SetBinContent(40,4431.8807787);
  S3_PHI_1->SetBinContent(41,5113.7048985);
  S3_PHI_1->SetBinContent(42,8522.8454975);
  S3_PHI_1->SetBinContent(43,5113.7048985);
  S3_PHI_1->SetBinContent(44,2386.3964193);
  S3_PHI_1->SetBinContent(45,4431.8807787);
  S3_PHI_1->SetBinContent(46,4090.9647188);
  S3_PHI_1->SetBinContent(47,4772.7928386);
  S3_PHI_1->SetBinContent(48,5454.6209584);
  S3_PHI_1->SetBinContent(49,7500.1013178);
  S3_PHI_1->SetBinContent(50,3409.137399);
  S3_PHI_1->SetBinContent(51,5795.5330183);
  S3_PHI_1->SetBinContent(52,6818.273198);
  S3_PHI_1->SetBinContent(53,5454.6209584);
  S3_PHI_1->SetBinContent(54,4772.7928386);
  S3_PHI_1->SetBinContent(55,5795.5330183);
  S3_PHI_1->SetBinContent(56,6136.4490782);
  S3_PHI_1->SetBinContent(57,5113.7048985);
  S3_PHI_1->SetBinContent(58,5454.6209584);
  S3_PHI_1->SetBinContent(59,4431.8807787);
  S3_PHI_1->SetBinContent(60,5795.5330183);
  S3_PHI_1->SetBinContent(61,6136.4490782);
  S3_PHI_1->SetBinContent(62,7841.0173777);
  S3_PHI_1->SetBinContent(63,7500.1013178);
  S3_PHI_1->SetBinContent(64,2386.3964193);
  S3_PHI_1->SetBinContent(65,0.0); // overflow
  S3_PHI_1->SetEntries(999);
  // Style
  S3_PHI_1->SetLineColor(46);
  S3_PHI_1->SetLineStyle(1);
  S3_PHI_1->SetLineWidth(1);
  S3_PHI_1->SetFillColor(46);
  S3_PHI_1->SetFillStyle(1001);

  // Creating a new TH1F
  TH1F* S3_PHI_2 = new TH1F("S3_PHI_2","S3_PHI_2",64,-3.2,3.2);
  // Content
  S3_PHI_2->SetBinContent(0,0.0); // underflow
  S3_PHI_2->SetBinContent(1,433.601879037);
  S3_PHI_2->SetBinContent(2,1052.01770652);
  S3_PHI_2->SetBinContent(3,1052.01770652);
  S3_PHI_2->SetBinContent(4,1208.39886289);
  S3_PHI_2->SetBinContent(5,1300.80563711);
  S3_PHI_2->SetBinContent(6,1123.10008669);
  S3_PHI_2->SetBinContent(7,995.15212238);
  S3_PHI_2->SetBinContent(8,1130.2080847);
  S3_PHI_2->SetBinContent(9,1236.83165496);
  S3_PHI_2->SetBinContent(10,1315.02203315);
  S3_PHI_2->SetBinContent(11,1101.77529264);
  S3_PHI_2->SetBinContent(12,1123.10008669);
  S3_PHI_2->SetBinContent(13,1115.99168867);
  S3_PHI_2->SetBinContent(14,1179.96567082);
  S3_PHI_2->SetBinContent(15,1023.58491445);
  S3_PHI_2->SetBinContent(16,895.636550142);
  S3_PHI_2->SetBinContent(17,1158.64127677);
  S3_PHI_2->SetBinContent(18,1144.42488074);
  S3_PHI_2->SetBinContent(19,1023.58491445);
  S3_PHI_2->SetBinContent(20,1350.56322323);
  S3_PHI_2->SetBinContent(21,1179.96567082);
  S3_PHI_2->SetBinContent(22,1194.18246686);
  S3_PHI_2->SetBinContent(23,1144.42488074);
  S3_PHI_2->SetBinContent(24,1073.34250057);
  S3_PHI_2->SetBinContent(25,1094.66729462);
  S3_PHI_2->SetBinContent(26,1236.83165496);
  S3_PHI_2->SetBinContent(27,1137.31648272);
  S3_PHI_2->SetBinContent(28,1187.07406884);
  S3_PHI_2->SetBinContent(29,1307.91403513);
  S3_PHI_2->SetBinContent(30,1222.61525892);
  S3_PHI_2->SetBinContent(31,1286.58924108);
  S3_PHI_2->SetBinContent(32,1101.77529264);
  S3_PHI_2->SetBinContent(33,1016.47651643);
  S3_PHI_2->SetBinContent(34,1137.31648272);
  S3_PHI_2->SetBinContent(35,1151.53287875);
  S3_PHI_2->SetBinContent(36,1286.58924108);
  S3_PHI_2->SetBinContent(37,1151.53287875);
  S3_PHI_2->SetBinContent(38,1194.18246686);
  S3_PHI_2->SetBinContent(39,1165.74927479);
  S3_PHI_2->SetBinContent(40,1101.77529264);
  S3_PHI_2->SetBinContent(41,1115.99168867);
  S3_PHI_2->SetBinContent(42,980.935326346);
  S3_PHI_2->SetBinContent(43,1151.53287875);
  S3_PHI_2->SetBinContent(44,1080.45049858);
  S3_PHI_2->SetBinContent(45,1165.74927479);
  S3_PHI_2->SetBinContent(46,1080.45049858);
  S3_PHI_2->SetBinContent(47,1151.53287875);
  S3_PHI_2->SetBinContent(48,1052.01770652);
  S3_PHI_2->SetBinContent(49,980.935326346);
  S3_PHI_2->SetBinContent(50,1052.01770652);
  S3_PHI_2->SetBinContent(51,1123.10008669);
  S3_PHI_2->SetBinContent(52,1059.12610453);
  S3_PHI_2->SetBinContent(53,1073.34250057);
  S3_PHI_2->SetBinContent(54,1108.88369065);
  S3_PHI_2->SetBinContent(55,1208.39886289);
  S3_PHI_2->SetBinContent(56,959.610932295);
  S3_PHI_2->SetBinContent(57,1215.50686091);
  S3_PHI_2->SetBinContent(58,1009.36851841);
  S3_PHI_2->SetBinContent(59,1165.74927479);
  S3_PHI_2->SetBinContent(60,1172.85767281);
  S3_PHI_2->SetBinContent(61,1059.12610453);
  S3_PHI_2->SetBinContent(62,973.827328329);
  S3_PHI_2->SetBinContent(63,1307.91403513);
  S3_PHI_2->SetBinContent(64,490.467863173);
  S3_PHI_2->SetBinContent(65,0.0); // overflow
  S3_PHI_2->SetEntries(9999);
  // Style
  S3_PHI_2->SetLineColor(8);
  S3_PHI_2->SetLineStyle(1);
  S3_PHI_2->SetLineWidth(1);
  S3_PHI_2->SetFillColor(8);
  S3_PHI_2->SetFillStyle(1001);

  // Creating a new TH1F
  TH1F* S3_PHI_3 = new TH1F("S3_PHI_3","S3_PHI_3",64,-3.2,3.2);
  // Content
  S3_PHI_3->SetBinContent(0,0.0); // underflow
  S3_PHI_3->SetBinContent(1,37.914355132);
  S3_PHI_3->SetBinContent(2,125.188929964);
  S3_PHI_3->SetBinContent(3,110.881604254);
  S3_PHI_3->SetBinContent(4,112.312324825);
  S3_PHI_3->SetBinContent(5,107.304762826);
  S3_PHI_3->SetBinContent(6,105.874042255);
  S3_PHI_3->SetBinContent(7,103.727961399);
  S3_PHI_3->SetBinContent(8,130.196451963);
  S3_PHI_3->SetBinContent(9,105.874042255);
  S3_PHI_3->SetBinContent(10,104.443321684);
  S3_PHI_3->SetBinContent(11,113.743085396);
  S3_PHI_3->SetBinContent(12,105.15868197);
  S3_PHI_3->SetBinContent(13,98.7203994002);
  S3_PHI_3->SetBinContent(14,128.050371106);
  S3_PHI_3->SetBinContent(15,115.889166252);
  S3_PHI_3->SetBinContent(16,110.166243968);
  S3_PHI_3->SetBinContent(17,123.042809107);
  S3_PHI_3->SetBinContent(18,103.012601113);
  S3_PHI_3->SetBinContent(19,116.604526538);
  S3_PHI_3->SetBinContent(20,123.042809107);
  S3_PHI_3->SetBinContent(21,118.035247109);
  S3_PHI_3->SetBinContent(22,122.327448822);
  S3_PHI_3->SetBinContent(23,106.589402541);
  S3_PHI_3->SetBinContent(24,124.473529678);
  S3_PHI_3->SetBinContent(25,114.458445681);
  S3_PHI_3->SetBinContent(26,109.450883683);
  S3_PHI_3->SetBinContent(27,117.319886823);
  S3_PHI_3->SetBinContent(28,106.589402541);
  S3_PHI_3->SetBinContent(29,100.866480257);
  S3_PHI_3->SetBinContent(30,104.443321684);
  S3_PHI_3->SetBinContent(31,117.319886823);
  S3_PHI_3->SetBinContent(32,118.035247109);
  S3_PHI_3->SetBinContent(33,110.881604254);
  S3_PHI_3->SetBinContent(34,99.4357596857);
  S3_PHI_3->SetBinContent(35,120.896728251);
  S3_PHI_3->SetBinContent(36,115.889166252);
  S3_PHI_3->SetBinContent(37,118.035247109);
  S3_PHI_3->SetBinContent(38,128.050371106);
  S3_PHI_3->SetBinContent(39,115.173805967);
  S3_PHI_3->SetBinContent(40,109.450883683);
  S3_PHI_3->SetBinContent(41,117.319886823);
  S3_PHI_3->SetBinContent(42,120.181367965);
  S3_PHI_3->SetBinContent(43,103.727961399);
  S3_PHI_3->SetBinContent(44,109.450883683);
  S3_PHI_3->SetBinContent(45,104.443321684);
  S3_PHI_3->SetBinContent(46,103.727961399);
  S3_PHI_3->SetBinContent(47,115.889166252);
  S3_PHI_3->SetBinContent(48,114.458445681);
  S3_PHI_3->SetBinContent(49,111.596964539);
  S3_PHI_3->SetBinContent(50,114.458445681);
  S3_PHI_3->SetBinContent(51,118.035247109);
  S3_PHI_3->SetBinContent(52,117.319886823);
  S3_PHI_3->SetBinContent(53,115.173805967);
  S3_PHI_3->SetBinContent(54,118.750607394);
  S3_PHI_3->SetBinContent(55,131.627212534);
  S3_PHI_3->SetBinContent(56,97.2896788292);
  S3_PHI_3->SetBinContent(57,106.589402541);
  S3_PHI_3->SetBinContent(58,134.488653676);
  S3_PHI_3->SetBinContent(59,107.304762826);
  S3_PHI_3->SetBinContent(60,127.335010821);
  S3_PHI_3->SetBinContent(61,110.881604254);
  S3_PHI_3->SetBinContent(62,116.604526538);
  S3_PHI_3->SetBinContent(63,120.181367965);
  S3_PHI_3->SetBinContent(64,57.2292228407);
  S3_PHI_3->SetBinContent(65,0.0); // overflow
  S3_PHI_3->SetEntries(9999);
  // Style
  S3_PHI_3->SetLineColor(4);
  S3_PHI_3->SetLineStyle(1);
  S3_PHI_3->SetLineWidth(1);
  S3_PHI_3->SetFillColor(4);
  S3_PHI_3->SetFillStyle(1001);

  // Creating a new THStack
  THStack* stack = new THStack("mystack_6","mystack");
  stack->Add(S3_PHI_0);
  stack->Add(S3_PHI_1);
  stack->Add(S3_PHI_2);
  stack->Add(S3_PHI_3);
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
  legend->AddEntry(S3_PHI_0,"signal1MeV");
  legend->AddEntry(S3_PHI_1,"signal100GeV1TeV");
  legend->AddEntry(S3_PHI_2,"signal100GeV1p5TeV");
  legend->AddEntry(S3_PHI_3,"signal100GeV4TeV");
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
