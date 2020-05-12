void selection_8()
{

  // ROOT version
  Int_t root_version = gROOT->GetVersionInt();

  // Creating a new TCanvas
  TCanvas* canvas = new TCanvas("canvas_plotflow_tempo17","canvas_plotflow_tempo17",0,0,700,500);
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
  TH1F* S9_sdETA_0 = new TH1F("S9_sdETA_0","S9_sdETA_0",100,-15.0,15.0);
  // Content
  S9_sdETA_0->SetBinContent(0,0.0); // underflow
  S9_sdETA_0->SetBinContent(1,0.0);
  S9_sdETA_0->SetBinContent(2,0.0);
  S9_sdETA_0->SetBinContent(3,0.0);
  S9_sdETA_0->SetBinContent(4,0.0);
  S9_sdETA_0->SetBinContent(5,0.0);
  S9_sdETA_0->SetBinContent(6,0.0);
  S9_sdETA_0->SetBinContent(7,0.0);
  S9_sdETA_0->SetBinContent(8,0.0);
  S9_sdETA_0->SetBinContent(9,0.0);
  S9_sdETA_0->SetBinContent(10,0.0);
  S9_sdETA_0->SetBinContent(11,0.0);
  S9_sdETA_0->SetBinContent(12,0.0);
  S9_sdETA_0->SetBinContent(13,0.0);
  S9_sdETA_0->SetBinContent(14,0.0);
  S9_sdETA_0->SetBinContent(15,0.0);
  S9_sdETA_0->SetBinContent(16,0.0);
  S9_sdETA_0->SetBinContent(17,0.002324775003);
  S9_sdETA_0->SetBinContent(18,0.116098978734);
  S9_sdETA_0->SetBinContent(19,0.350692617867);
  S9_sdETA_0->SetBinContent(20,0.801082689435);
  S9_sdETA_0->SetBinContent(21,1.25611749726);
  S9_sdETA_0->SetBinContent(22,2.12939443139);
  S9_sdETA_0->SetBinContent(23,3.16506844143);
  S9_sdETA_0->SetBinContent(24,4.6927738116);
  S9_sdETA_0->SetBinContent(25,5.97018421383);
  S9_sdETA_0->SetBinContent(26,8.25038706579);
  S9_sdETA_0->SetBinContent(27,10.5978352989);
  S9_sdETA_0->SetBinContent(28,13.8262332034);
  S9_sdETA_0->SetBinContent(29,17.2878313101);
  S9_sdETA_0->SetBinContent(30,21.3678854515);
  S9_sdETA_0->SetBinContent(31,26.2004266812);
  S9_sdETA_0->SetBinContent(32,31.0364776865);
  S9_sdETA_0->SetBinContent(33,36.5501632203);
  S9_sdETA_0->SetBinContent(34,42.4971861133);
  S9_sdETA_0->SetBinContent(35,48.1863004638);
  S9_sdETA_0->SetBinContent(36,53.5154029827);
  S9_sdETA_0->SetBinContent(37,57.6934350275);
  S9_sdETA_0->SetBinContent(38,62.8279009033);
  S9_sdETA_0->SetBinContent(39,65.2634772826);
  S9_sdETA_0->SetBinContent(40,65.9369304611);
  S9_sdETA_0->SetBinContent(41,66.4727508686);
  S9_sdETA_0->SetBinContent(42,64.3452592313);
  S9_sdETA_0->SetBinContent(43,61.684745413);
  S9_sdETA_0->SetBinContent(44,56.9707730366);
  S9_sdETA_0->SetBinContent(45,53.6170185807);
  S9_sdETA_0->SetBinContent(46,50.4736507858);
  S9_sdETA_0->SetBinContent(47,50.1584105789);
  S9_sdETA_0->SetBinContent(48,53.9007987264);
  S9_sdETA_0->SetBinContent(49,62.3007150234);
  S9_sdETA_0->SetBinContent(50,60.4743525363);
  S9_sdETA_0->SetBinContent(51,60.8712210088);
  S9_sdETA_0->SetBinContent(52,62.7867269985);
  S9_sdETA_0->SetBinContent(53,53.4203432297);
  S9_sdETA_0->SetBinContent(54,50.6379066836);
  S9_sdETA_0->SetBinContent(55,50.4211640509);
  S9_sdETA_0->SetBinContent(56,53.8954021466);
  S9_sdETA_0->SetBinContent(57,57.1728049927);
  S9_sdETA_0->SetBinContent(58,61.7686522345);
  S9_sdETA_0->SetBinContent(59,64.0358153507);
  S9_sdETA_0->SetBinContent(60,65.7659188449);
  S9_sdETA_0->SetBinContent(61,66.5552186022);
  S9_sdETA_0->SetBinContent(62,65.4569946351);
  S9_sdETA_0->SetBinContent(63,62.2581020307);
  S9_sdETA_0->SetBinContent(64,58.9323698149);
  S9_sdETA_0->SetBinContent(65,54.0698915586);
  S9_sdETA_0->SetBinContent(66,48.3625887357);
  S9_sdETA_0->SetBinContent(67,42.5154545352);
  S9_sdETA_0->SetBinContent(68,36.5408651133);
  S9_sdETA_0->SetBinContent(69,31.1096912852);
  S9_sdETA_0->SetBinContent(70,26.1912604906);
  S9_sdETA_0->SetBinContent(71,21.1448907811);
  S9_sdETA_0->SetBinContent(72,17.1393134378);
  S9_sdETA_0->SetBinContent(73,13.5584988882);
  S9_sdETA_0->SetBinContent(74,10.6214723183);
  S9_sdETA_0->SetBinContent(75,8.5453761075);
  S9_sdETA_0->SetBinContent(76,6.28580817753);
  S9_sdETA_0->SetBinContent(77,4.44214865293);
  S9_sdETA_0->SetBinContent(78,3.07241756175);
  S9_sdETA_0->SetBinContent(79,2.11783175959);
  S9_sdETA_0->SetBinContent(80,1.27962459892);
  S9_sdETA_0->SetBinContent(81,0.750176552751);
  S9_sdETA_0->SetBinContent(82,0.343744061726);
  S9_sdETA_0->SetBinContent(83,0.118376615213);
  S9_sdETA_0->SetBinContent(84,0.0023206420224);
  S9_sdETA_0->SetBinContent(85,0.0);
  S9_sdETA_0->SetBinContent(86,0.0);
  S9_sdETA_0->SetBinContent(87,0.0);
  S9_sdETA_0->SetBinContent(88,0.0);
  S9_sdETA_0->SetBinContent(89,0.0);
  S9_sdETA_0->SetBinContent(90,0.0);
  S9_sdETA_0->SetBinContent(91,0.0);
  S9_sdETA_0->SetBinContent(92,0.0);
  S9_sdETA_0->SetBinContent(93,0.0);
  S9_sdETA_0->SetBinContent(94,0.0);
  S9_sdETA_0->SetBinContent(95,0.0);
  S9_sdETA_0->SetBinContent(96,0.0);
  S9_sdETA_0->SetBinContent(97,0.0);
  S9_sdETA_0->SetBinContent(98,0.0);
  S9_sdETA_0->SetBinContent(99,0.0);
  S9_sdETA_0->SetBinContent(100,0.0);
  S9_sdETA_0->SetBinContent(101,0.0); // overflow
  S9_sdETA_0->SetEntries(999999);
  // Style
  S9_sdETA_0->SetLineColor(9);
  S9_sdETA_0->SetLineStyle(1);
  S9_sdETA_0->SetLineWidth(1);
  S9_sdETA_0->SetFillColor(9);
  S9_sdETA_0->SetFillStyle(1001);

  // Creating a new THStack
  THStack* stack = new THStack("mystack_18","mystack");
  stack->Add(S9_sdETA_0);
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
  stack->GetXaxis()->SetTitle("#Delta#eta ( j_{1} , j_{2} ) ");

  // Finalizing the TCanvas
  canvas->SetLogx(0);
  canvas->SetLogy(0);

  // Saving the image
  canvas->SaveAs("../../HTML/MadAnalysis5job_0/selection_8.png");
  canvas->SaveAs("../../PDF/MadAnalysis5job_0/selection_8.png");
  canvas->SaveAs("../../DVI/MadAnalysis5job_0/selection_8.eps");

}
