void selection_0()
{

  // ROOT version
  Int_t root_version = gROOT->GetVersionInt();

  // Creating a new TCanvas
  TCanvas* canvas = new TCanvas("canvas_plotflow_tempo1","canvas_plotflow_tempo1",0,0,700,500);
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
  TH1F* S1_ETA_0 = new TH1F("S1_ETA_0","S1_ETA_0",100,-8.0,8.0);
  // Content
  S1_ETA_0->SetBinContent(0,0.0); // underflow
  S1_ETA_0->SetBinContent(1,0.0);
  S1_ETA_0->SetBinContent(2,0.0);
  S1_ETA_0->SetBinContent(3,0.0);
  S1_ETA_0->SetBinContent(4,0.0);
  S1_ETA_0->SetBinContent(5,0.00818816896832);
  S1_ETA_0->SetBinContent(6,0.00409408448416);
  S1_ETA_0->SetBinContent(7,0.00409408448416);
  S1_ETA_0->SetBinContent(8,0.00409408448416);
  S1_ETA_0->SetBinContent(9,0.0122822534525);
  S1_ETA_0->SetBinContent(10,0.0163763339367);
  S1_ETA_0->SetBinContent(11,0.0122822534525);
  S1_ETA_0->SetBinContent(12,0.0204704184208);
  S1_ETA_0->SetBinContent(13,0.0450349213258);
  S1_ETA_0->SetBinContent(14,0.0777876131991);
  S1_ETA_0->SetBinContent(15,0.0777876131991);
  S1_ETA_0->SetBinContent(16,0.110540265072);
  S1_ETA_0->SetBinContent(17,0.110540265072);
  S1_ETA_0->SetBinContent(18,0.212892377176);
  S1_ETA_0->SetBinContent(19,0.302962219828);
  S1_ETA_0->SetBinContent(20,0.39303206248);
  S1_ETA_0->SetBinContent(21,0.556795521846);
  S1_ETA_0->SetBinContent(22,0.749217356602);
  S1_ETA_0->SetBinContent(23,1.03170911401);
  S1_ETA_0->SetBinContent(24,1.30601287845);
  S1_ETA_0->SetBinContent(25,1.73589170928);
  S1_ETA_0->SetBinContent(26,2.13711176473);
  S1_ETA_0->SetBinContent(27,2.80854158814);
  S1_ETA_0->SetBinContent(28,3.47587741505);
  S1_ETA_0->SetBinContent(29,4.55262009039);
  S1_ETA_0->SetBinContent(30,5.64574315166);
  S1_ETA_0->SetBinContent(31,6.55463037114);
  S1_ETA_0->SetBinContent(32,7.72553736561);
  S1_ETA_0->SetBinContent(33,9.42048791006);
  S1_ETA_0->SetBinContent(34,10.8902626479);
  S1_ETA_0->SetBinContent(35,12.6548131325);
  S1_ETA_0->SetBinContent(36,14.3333876911);
  S1_ETA_0->SetBinContent(37,15.9423623093);
  S1_ETA_0->SetBinContent(38,17.444893019);
  S1_ETA_0->SetBinContent(39,18.8450678166);
  S1_ETA_0->SetBinContent(40,20.4499504384);
  S1_ETA_0->SetBinContent(41,21.3752136438);
  S1_ETA_0->SetBinContent(42,22.0998650215);
  S1_ETA_0->SetBinContent(43,22.4273927402);
  S1_ETA_0->SetBinContent(44,23.2298320511);
  S1_ETA_0->SetBinContent(45,22.5870606031);
  S1_ETA_0->SetBinContent(46,22.5624966242);
  S1_ETA_0->SetBinContent(47,22.6853205187);
  S1_ETA_0->SetBinContent(48,22.3373208176);
  S1_ETA_0->SetBinContent(49,21.7354933344);
  S1_ETA_0->SetBinContent(50,22.1612769688);
  S1_ETA_0->SetBinContent(51,22.0834890356);
  S1_ETA_0->SetBinContent(52,21.98522912);
  S1_ETA_0->SetBinContent(53,22.5051806734);
  S1_ETA_0->SetBinContent(54,22.619812575);
  S1_ETA_0->SetBinContent(55,23.4672878472);
  S1_ETA_0->SetBinContent(56,22.3987327649);
  S1_ETA_0->SetBinContent(57,22.7221644871);
  S1_ETA_0->SetBinContent(58,22.3168528352);
  S1_ETA_0->SetBinContent(59,22.2063129301);
  S1_ETA_0->SetBinContent(60,21.2810497247);
  S1_ETA_0->SetBinContent(61,19.8849669236);
  S1_ETA_0->SetBinContent(62,19.0333956549);
  S1_ETA_0->SetBinContent(63,17.6004688854);
  S1_ETA_0->SetBinContent(64,15.9792102777);
  S1_ETA_0->SetBinContent(65,14.0345199477);
  S1_ETA_0->SetBinContent(66,12.8226689884);
  S1_ETA_0->SetBinContent(67,11.4143061978);
  S1_ETA_0->SetBinContent(68,9.62519173427);
  S1_ETA_0->SetBinContent(69,7.99574513357);
  S1_ETA_0->SetBinContent(70,6.43180647662);
  S1_ETA_0->SetBinContent(71,5.64164715518);
  S1_ETA_0->SetBinContent(72,4.64269201304);
  S1_ETA_0->SetBinContent(73,3.55775894474);
  S1_ETA_0->SetBinContent(74,2.75941243033);
  S1_ETA_0->SetBinContent(75,2.34181598894);
  S1_ETA_0->SetBinContent(76,1.77273847764);
  S1_ETA_0->SetBinContent(77,1.32238926438);
  S1_ETA_0->SetBinContent(78,0.941639191358);
  S1_ETA_0->SetBinContent(79,0.741029363633);
  S1_ETA_0->SetBinContent(80,0.540419135909);
  S1_ETA_0->SetBinContent(81,0.405314451932);
  S1_ETA_0->SetBinContent(82,0.274303644439);
  S1_ETA_0->SetBinContent(83,0.19651603124);
  S1_ETA_0->SetBinContent(84,0.151481109914);
  S1_ETA_0->SetBinContent(85,0.143292956946);
  S1_ETA_0->SetBinContent(86,0.0777876131991);
  S1_ETA_0->SetBinContent(87,0.0532230742941);
  S1_ETA_0->SetBinContent(88,0.0409408448416);
  S1_ETA_0->SetBinContent(89,0.0409408448416);
  S1_ETA_0->SetBinContent(90,0.0204704184208);
  S1_ETA_0->SetBinContent(91,0.0163763339367);
  S1_ETA_0->SetBinContent(92,0.00409408448416);
  S1_ETA_0->SetBinContent(93,0.00818816896832);
  S1_ETA_0->SetBinContent(94,0.00409408448416);
  S1_ETA_0->SetBinContent(95,0.00818816896832);
  S1_ETA_0->SetBinContent(96,0.0);
  S1_ETA_0->SetBinContent(97,0.0);
  S1_ETA_0->SetBinContent(98,0.0);
  S1_ETA_0->SetBinContent(99,0.0);
  S1_ETA_0->SetBinContent(100,0.0);
  S1_ETA_0->SetBinContent(101,0.00409408448416); // overflow
  S1_ETA_0->SetEntries(187342);
  // Style
  S1_ETA_0->SetLineColor(9);
  S1_ETA_0->SetLineStyle(1);
  S1_ETA_0->SetLineWidth(1);
  S1_ETA_0->SetFillColor(9);
  S1_ETA_0->SetFillStyle(1001);

  // Creating a new THStack
  THStack* stack = new THStack("mystack_2","mystack");
  stack->Add(S1_ETA_0);
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
  stack->GetXaxis()->SetTitle("#eta [ a_{1} a_{2} ] ");

  // Finalizing the TCanvas
  canvas->SetLogx(0);
  canvas->SetLogy(0);

  // Saving the image
  canvas->SaveAs("../../HTML/MadAnalysis5job_0/selection_0.png");
  canvas->SaveAs("../../PDF/MadAnalysis5job_0/selection_0.png");
  canvas->SaveAs("../../DVI/MadAnalysis5job_0/selection_0.eps");

}
