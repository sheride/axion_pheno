void selection_5()
{

  // ROOT version
  Int_t root_version = gROOT->GetVersionInt();

  // Creating a new TCanvas
  TCanvas* canvas = new TCanvas("canvas_plotflow_tempo11","canvas_plotflow_tempo11",0,0,1000,500);
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
  TH1F* S6_PHI_0 = new TH1F("S6_PHI_0","S6_PHI_0",64,-3.2,3.2);
  // Content
  S6_PHI_0->SetBinContent(0,0.0); // underflow
  S6_PHI_0->SetBinContent(1,2032.8441017);
  S6_PHI_0->SetBinContent(2,6505.09904545);
  S6_PHI_0->SetBinContent(3,7724.80686647);
  S6_PHI_0->SetBinContent(4,4472.25534374);
  S6_PHI_0->SetBinContent(5,6098.53110511);
  S6_PHI_0->SetBinContent(6,6505.09904545);
  S6_PHI_0->SetBinContent(7,6098.53110511);
  S6_PHI_0->SetBinContent(8,6911.67098579);
  S6_PHI_0->SetBinContent(9,5285.39522442);
  S6_PHI_0->SetBinContent(10,7318.23892613);
  S6_PHI_0->SetBinContent(11,5285.39522442);
  S6_PHI_0->SetBinContent(12,5285.39522442);
  S6_PHI_0->SetBinContent(13,6911.67098579);
  S6_PHI_0->SetBinContent(14,7318.23892613);
  S6_PHI_0->SetBinContent(15,6911.67098579);
  S6_PHI_0->SetBinContent(16,5691.96316476);
  S6_PHI_0->SetBinContent(17,8537.94674715);
  S6_PHI_0->SetBinContent(18,7318.23892613);
  S6_PHI_0->SetBinContent(19,5691.96316476);
  S6_PHI_0->SetBinContent(20,4472.25534374);
  S6_PHI_0->SetBinContent(21,4878.82728408);
  S6_PHI_0->SetBinContent(22,4472.25534374);
  S6_PHI_0->SetBinContent(23,6505.09904545);
  S6_PHI_0->SetBinContent(24,9757.65056817);
  S6_PHI_0->SetBinContent(25,6505.09904545);
  S6_PHI_0->SetBinContent(26,6911.67098579);
  S6_PHI_0->SetBinContent(27,6505.09904545);
  S6_PHI_0->SetBinContent(28,5285.39522442);
  S6_PHI_0->SetBinContent(29,8537.94674715);
  S6_PHI_0->SetBinContent(30,7318.23892613);
  S6_PHI_0->SetBinContent(31,8131.37480681);
  S6_PHI_0->SetBinContent(32,5285.39522442);
  S6_PHI_0->SetBinContent(33,5285.39522442);
  S6_PHI_0->SetBinContent(34,5691.96316476);
  S6_PHI_0->SetBinContent(35,8537.94674715);
  S6_PHI_0->SetBinContent(36,6098.53110511);
  S6_PHI_0->SetBinContent(37,7318.23892613);
  S6_PHI_0->SetBinContent(38,5691.96316476);
  S6_PHI_0->SetBinContent(39,4878.82728408);
  S6_PHI_0->SetBinContent(40,6911.67098579);
  S6_PHI_0->SetBinContent(41,6505.09904545);
  S6_PHI_0->SetBinContent(42,9351.08262783);
  S6_PHI_0->SetBinContent(43,7318.23892613);
  S6_PHI_0->SetBinContent(44,6911.67098579);
  S6_PHI_0->SetBinContent(45,4472.25534374);
  S6_PHI_0->SetBinContent(46,3659.11946306);
  S6_PHI_0->SetBinContent(47,4472.25534374);
  S6_PHI_0->SetBinContent(48,6098.53110511);
  S6_PHI_0->SetBinContent(49,10164.2185085);
  S6_PHI_0->SetBinContent(50,4065.6874034);
  S6_PHI_0->SetBinContent(51,5285.39522442);
  S6_PHI_0->SetBinContent(52,9351.08262783);
  S6_PHI_0->SetBinContent(53,9757.65056817);
  S6_PHI_0->SetBinContent(54,8537.94674715);
  S6_PHI_0->SetBinContent(55,4472.25534374);
  S6_PHI_0->SetBinContent(56,8131.37480681);
  S6_PHI_0->SetBinContent(57,5691.96316476);
  S6_PHI_0->SetBinContent(58,3252.55032272);
  S6_PHI_0->SetBinContent(59,5691.96316476);
  S6_PHI_0->SetBinContent(60,4878.82728408);
  S6_PHI_0->SetBinContent(61,7318.23892613);
  S6_PHI_0->SetBinContent(62,6505.09904545);
  S6_PHI_0->SetBinContent(63,9757.65056817);
  S6_PHI_0->SetBinContent(64,1626.27536136);
  S6_PHI_0->SetBinContent(65,0.0); // overflow
  S6_PHI_0->SetEntries(999);
  // Style
  S6_PHI_0->SetLineColor(9);
  S6_PHI_0->SetLineStyle(1);
  S6_PHI_0->SetLineWidth(1);
  S6_PHI_0->SetFillColor(9);
  S6_PHI_0->SetFillStyle(1001);

  // Creating a new TH1F
  TH1F* S6_PHI_1 = new TH1F("S6_PHI_1","S6_PHI_1",64,-3.2,3.2);
  // Content
  S6_PHI_1->SetBinContent(0,0.0); // underflow
  S6_PHI_1->SetBinContent(1,3409.13752713);
  S6_PHI_1->SetBinContent(2,4772.79301798);
  S6_PHI_1->SetBinContent(3,5795.53323612);
  S6_PHI_1->SetBinContent(4,8181.92974511);
  S6_PHI_1->SetBinContent(5,5454.6211634);
  S6_PHI_1->SetBinContent(6,5113.70509069);
  S6_PHI_1->SetBinContent(7,5113.70509069);
  S6_PHI_1->SetBinContent(8,6818.27345425);
  S6_PHI_1->SetBinContent(9,4772.79301798);
  S6_PHI_1->SetBinContent(10,3750.05159984);
  S6_PHI_1->SetBinContent(11,4090.96487255);
  S6_PHI_1->SetBinContent(12,5795.53323612);
  S6_PHI_1->SetBinContent(13,3750.05159984);
  S6_PHI_1->SetBinContent(14,5454.6211634);
  S6_PHI_1->SetBinContent(15,5795.53323612);
  S6_PHI_1->SetBinContent(16,6477.36138154);
  S6_PHI_1->SetBinContent(17,3068.22385441);
  S6_PHI_1->SetBinContent(18,5454.6211634);
  S6_PHI_1->SetBinContent(19,3750.05159984);
  S6_PHI_1->SetBinContent(20,4772.79301798);
  S6_PHI_1->SetBinContent(21,4431.88094527);
  S6_PHI_1->SetBinContent(22,4090.96487255);
  S6_PHI_1->SetBinContent(23,4772.79301798);
  S6_PHI_1->SetBinContent(24,6136.44930883);
  S6_PHI_1->SetBinContent(25,7159.18952697);
  S6_PHI_1->SetBinContent(26,5454.6211634);
  S6_PHI_1->SetBinContent(27,4090.96487255);
  S6_PHI_1->SetBinContent(28,5113.70509069);
  S6_PHI_1->SetBinContent(29,6136.44930883);
  S6_PHI_1->SetBinContent(30,6477.36138154);
  S6_PHI_1->SetBinContent(31,9545.58603596);
  S6_PHI_1->SetBinContent(32,5795.53323612);
  S6_PHI_1->SetBinContent(33,1704.56876356);
  S6_PHI_1->SetBinContent(34,5113.70509069);
  S6_PHI_1->SetBinContent(35,5454.6211634);
  S6_PHI_1->SetBinContent(36,6477.36138154);
  S6_PHI_1->SetBinContent(37,5795.53323612);
  S6_PHI_1->SetBinContent(38,4431.88094527);
  S6_PHI_1->SetBinContent(39,6136.44930883);
  S6_PHI_1->SetBinContent(40,6818.27345425);
  S6_PHI_1->SetBinContent(41,4090.96487255);
  S6_PHI_1->SetBinContent(42,6136.44930883);
  S6_PHI_1->SetBinContent(43,3068.22385441);
  S6_PHI_1->SetBinContent(44,5113.70509069);
  S6_PHI_1->SetBinContent(45,6818.27345425);
  S6_PHI_1->SetBinContent(46,4772.79301798);
  S6_PHI_1->SetBinContent(47,7500.10159968);
  S6_PHI_1->SetBinContent(48,7841.01767239);
  S6_PHI_1->SetBinContent(49,8181.92974511);
  S6_PHI_1->SetBinContent(50,5113.70509069);
  S6_PHI_1->SetBinContent(51,6136.44930883);
  S6_PHI_1->SetBinContent(52,3750.05159984);
  S6_PHI_1->SetBinContent(53,7159.18952697);
  S6_PHI_1->SetBinContent(54,5454.6211634);
  S6_PHI_1->SetBinContent(55,5113.70509069);
  S6_PHI_1->SetBinContent(56,5113.70509069);
  S6_PHI_1->SetBinContent(57,6136.44930883);
  S6_PHI_1->SetBinContent(58,6818.27345425);
  S6_PHI_1->SetBinContent(59,3068.22385441);
  S6_PHI_1->SetBinContent(60,5113.70509069);
  S6_PHI_1->SetBinContent(61,1704.56876356);
  S6_PHI_1->SetBinContent(62,5113.70509069);
  S6_PHI_1->SetBinContent(63,5454.6211634);
  S6_PHI_1->SetBinContent(64,3068.22385441);
  S6_PHI_1->SetBinContent(65,0.0); // overflow
  S6_PHI_1->SetEntries(999);
  // Style
  S6_PHI_1->SetLineColor(46);
  S6_PHI_1->SetLineStyle(1);
  S6_PHI_1->SetLineWidth(1);
  S6_PHI_1->SetFillColor(46);
  S6_PHI_1->SetFillStyle(1001);

  // Creating a new TH1F
  TH1F* S6_PHI_2 = new TH1F("S6_PHI_2","S6_PHI_2",64,-3.2,3.2);
  // Content
  S6_PHI_2->SetBinContent(0,0.0); // underflow
  S6_PHI_2->SetBinContent(1,497.575847189);
  S6_PHI_2->SetBinContent(2,1208.39882889);
  S6_PHI_2->SetBinContent(3,1151.53284635);
  S6_PHI_2->SetBinContent(4,1059.12607473);
  S6_PHI_2->SetBinContent(5,1265.26441142);
  S6_PHI_2->SetBinContent(6,1115.99165727);
  S6_PHI_2->SetBinContent(7,1130.2080529);
  S6_PHI_2->SetBinContent(8,1023.58488565);
  S6_PHI_2->SetBinContent(9,1059.12607473);
  S6_PHI_2->SetBinContent(10,1073.34247036);
  S6_PHI_2->SetBinContent(11,1187.07403544);
  S6_PHI_2->SetBinContent(12,1243.94001797);
  S6_PHI_2->SetBinContent(13,1094.66726382);
  S6_PHI_2->SetBinContent(14,1123.10005508);
  S6_PHI_2->SetBinContent(15,1222.61522452);
  S6_PHI_2->SetBinContent(16,1251.04801579);
  S6_PHI_2->SetBinContent(17,1030.69288346);
  S6_PHI_2->SetBinContent(18,1108.88365945);
  S6_PHI_2->SetBinContent(19,1009.36849001);
  S6_PHI_2->SetBinContent(20,1172.8576398);
  S6_PHI_2->SetBinContent(21,1400.32076995);
  S6_PHI_2->SetBinContent(22,1144.42484853);
  S6_PHI_2->SetBinContent(23,1030.69288346);
  S6_PHI_2->SetBinContent(24,1201.29043107);
  S6_PHI_2->SetBinContent(25,1137.31645072);
  S6_PHI_2->SetBinContent(26,1094.66726382);
  S6_PHI_2->SetBinContent(27,1300.80560051);
  S6_PHI_2->SetBinContent(28,945.394509659);
  S6_PHI_2->SetBinContent(29,1144.42484853);
  S6_PHI_2->SetBinContent(30,1087.558866);
  S6_PHI_2->SetBinContent(31,1052.01767691);
  S6_PHI_2->SetBinContent(32,1094.66726382);
  S6_PHI_2->SetBinContent(33,1009.36849001);
  S6_PHI_2->SetBinContent(34,1101.77526163);
  S6_PHI_2->SetBinContent(35,1158.64124417);
  S6_PHI_2->SetBinContent(36,1251.04801579);
  S6_PHI_2->SetBinContent(37,959.610905292);
  S6_PHI_2->SetBinContent(38,1158.64124417);
  S6_PHI_2->SetBinContent(39,1044.9096791);
  S6_PHI_2->SetBinContent(40,1187.07403544);
  S6_PHI_2->SetBinContent(41,1222.61522452);
  S6_PHI_2->SetBinContent(42,1087.558866);
  S6_PHI_2->SetBinContent(43,1066.23407255);
  S6_PHI_2->SetBinContent(44,1300.80560051);
  S6_PHI_2->SetBinContent(45,1194.18243325);
  S6_PHI_2->SetBinContent(46,1208.39882889);
  S6_PHI_2->SetBinContent(47,1059.12607473);
  S6_PHI_2->SetBinContent(48,1201.29043107);
  S6_PHI_2->SetBinContent(49,1151.53284635);
  S6_PHI_2->SetBinContent(50,1059.12607473);
  S6_PHI_2->SetBinContent(51,1151.53284635);
  S6_PHI_2->SetBinContent(52,1208.39882889);
  S6_PHI_2->SetBinContent(53,1052.01767691);
  S6_PHI_2->SetBinContent(54,1201.29043107);
  S6_PHI_2->SetBinContent(55,1030.69288346);
  S6_PHI_2->SetBinContent(56,1208.39882889);
  S6_PHI_2->SetBinContent(57,966.71890311);
  S6_PHI_2->SetBinContent(58,1094.66726382);
  S6_PHI_2->SetBinContent(59,980.935298744);
  S6_PHI_2->SetBinContent(60,1172.8576398);
  S6_PHI_2->SetBinContent(61,1044.9096791);
  S6_PHI_2->SetBinContent(62,1187.07403544);
  S6_PHI_2->SetBinContent(63,1137.31645072);
  S6_PHI_2->SetBinContent(64,554.441829725);
  S6_PHI_2->SetBinContent(65,0.0); // overflow
  S6_PHI_2->SetEntries(9999);
  // Style
  S6_PHI_2->SetLineColor(8);
  S6_PHI_2->SetLineStyle(1);
  S6_PHI_2->SetLineWidth(1);
  S6_PHI_2->SetFillColor(8);
  S6_PHI_2->SetFillStyle(1001);

  // Creating a new TH1F
  TH1F* S6_PHI_3 = new TH1F("S6_PHI_3","S6_PHI_3",64,-3.2,3.2);
  // Content
  S6_PHI_3->SetBinContent(0,0.0); // underflow
  S6_PHI_3->SetBinContent(1,50.7909381409);
  S6_PHI_3->SetBinContent(2,118.750602414);
  S6_PHI_3->SetBinContent(3,136.634768802);
  S6_PHI_3->SetBinContent(4,125.188924713);
  S6_PHI_3->SetBinContent(5,130.911846758);
  S6_PHI_3->SetBinContent(6,101.581876282);
  S6_PHI_3->SetBinContent(7,104.443317304);
  S6_PHI_3->SetBinContent(8,108.735518837);
  S6_PHI_3->SetBinContent(9,111.596959859);
  S6_PHI_3->SetBinContent(10,108.020158581);
  S6_PHI_3->SetBinContent(11,108.735518837);
  S6_PHI_3->SetBinContent(12,125.188924713);
  S6_PHI_3->SetBinContent(13,132.342567269);
  S6_PHI_3->SetBinContent(14,116.604521647);
  S6_PHI_3->SetBinContent(15,102.297236537);
  S6_PHI_3->SetBinContent(16,90.8513924492);
  S6_PHI_3->SetBinContent(17,118.750602414);
  S6_PHI_3->SetBinContent(18,125.904284969);
  S6_PHI_3->SetBinContent(19,100.866476026);
  S6_PHI_3->SetBinContent(20,116.604521647);
  S6_PHI_3->SetBinContent(21,135.204008291);
  S6_PHI_3->SetBinContent(22,88.7052716827);
  S6_PHI_3->SetBinContent(23,90.8513924492);
  S6_PHI_3->SetBinContent(24,110.881599603);
  S6_PHI_3->SetBinContent(25,104.443317304);
  S6_PHI_3->SetBinContent(26,110.166239348);
  S6_PHI_3->SetBinContent(27,115.889161392);
  S6_PHI_3->SetBinContent(28,121.612083436);
  S6_PHI_3->SetBinContent(29,118.035242158);
  S6_PHI_3->SetBinContent(30,111.596959859);
  S6_PHI_3->SetBinContent(31,113.743080625);
  S6_PHI_3->SetBinContent(32,125.188924713);
  S6_PHI_3->SetBinContent(33,111.596959859);
  S6_PHI_3->SetBinContent(34,100.866476026);
  S6_PHI_3->SetBinContent(35,108.735518837);
  S6_PHI_3->SetBinContent(36,113.02768037);
  S6_PHI_3->SetBinContent(37,99.4357555153);
  S6_PHI_3->SetBinContent(38,106.58939807);
  S6_PHI_3->SetBinContent(39,132.342567269);
  S6_PHI_3->SetBinContent(40,119.466002669);
  S6_PHI_3->SetBinContent(41,115.889161392);
  S6_PHI_3->SetBinContent(42,101.581876282);
  S6_PHI_3->SetBinContent(43,113.02768037);
  S6_PHI_3->SetBinContent(44,126.619645224);
  S6_PHI_3->SetBinContent(45,118.750602414);
  S6_PHI_3->SetBinContent(46,97.2896747488);
  S6_PHI_3->SetBinContent(47,121.612083436);
  S6_PHI_3->SetBinContent(48,108.020158581);
  S6_PHI_3->SetBinContent(49,110.881599603);
  S6_PHI_3->SetBinContent(50,102.297236537);
  S6_PHI_3->SetBinContent(51,110.881599603);
  S6_PHI_3->SetBinContent(52,118.035242158);
  S6_PHI_3->SetBinContent(53,123.758164202);
  S6_PHI_3->SetBinContent(54,110.166239348);
  S6_PHI_3->SetBinContent(55,125.188924713);
  S6_PHI_3->SetBinContent(56,109.450879092);
  S6_PHI_3->SetBinContent(57,120.181362925);
  S6_PHI_3->SetBinContent(58,113.743080625);
  S6_PHI_3->SetBinContent(59,115.889161392);
  S6_PHI_3->SetBinContent(60,118.750602414);
  S6_PHI_3->SetBinContent(61,108.735518837);
  S6_PHI_3->SetBinContent(62,120.89672318);
  S6_PHI_3->SetBinContent(63,125.188924713);
  S6_PHI_3->SetBinContent(64,42.9218953303);
  S6_PHI_3->SetBinContent(65,0.0); // overflow
  S6_PHI_3->SetEntries(9999);
  // Style
  S6_PHI_3->SetLineColor(4);
  S6_PHI_3->SetLineStyle(1);
  S6_PHI_3->SetLineWidth(1);
  S6_PHI_3->SetFillColor(4);
  S6_PHI_3->SetFillStyle(1001);

  // Creating a new THStack
  THStack* stack = new THStack("mystack_12","mystack");
  stack->Add(S6_PHI_0);
  stack->Add(S6_PHI_1);
  stack->Add(S6_PHI_2);
  stack->Add(S6_PHI_3);
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

  // Creating a TLegend
  TLegend* legend = new TLegend(.73,.5,.97,.95);
  legend->AddEntry(S6_PHI_0,"signal1MeV");
  legend->AddEntry(S6_PHI_1,"signal100GeV1TeV");
  legend->AddEntry(S6_PHI_2,"signal100GeV1p5TeV");
  legend->AddEntry(S6_PHI_3,"signal100GeV4TeV");
  legend->SetFillColor(0);
  legend->SetTextSize(0.05);
  legend->SetTextFont(22);
  legend->SetY1(TMath::Max(0.15,0.97-0.10*legend->GetListOfPrimitives()->GetSize()));
  legend->Draw();

  // Saving the image
  canvas->SaveAs("../../HTML/MadAnalysis5job_0/selection_5.png");
  canvas->SaveAs("../../PDF/MadAnalysis5job_0/selection_5.png");
  canvas->SaveAs("../../DVI/MadAnalysis5job_0/selection_5.eps");

}
