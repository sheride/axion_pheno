void selection_1()
{

  // ROOT version
  Int_t root_version = gROOT->GetVersionInt();

  // Creating a new TCanvas
  TCanvas* canvas = new TCanvas("canvas_plotflow_tempo3","canvas_plotflow_tempo3",0,0,700,500);
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
  TH1F* S2_ETA_0 = new TH1F("S2_ETA_0","S2_ETA_0",160,-8.0,8.0);
  // Content
  S2_ETA_0->SetBinContent(0,0.0); // underflow
  S2_ETA_0->SetBinContent(1,0.0);
  S2_ETA_0->SetBinContent(2,0.0);
  S2_ETA_0->SetBinContent(3,0.0);
  S2_ETA_0->SetBinContent(4,0.0);
  S2_ETA_0->SetBinContent(5,0.0);
  S2_ETA_0->SetBinContent(6,0.0);
  S2_ETA_0->SetBinContent(7,0.0);
  S2_ETA_0->SetBinContent(8,0.0);
  S2_ETA_0->SetBinContent(9,0.0);
  S2_ETA_0->SetBinContent(10,0.0);
  S2_ETA_0->SetBinContent(11,0.0);
  S2_ETA_0->SetBinContent(12,0.0);
  S2_ETA_0->SetBinContent(13,0.0);
  S2_ETA_0->SetBinContent(14,0.0);
  S2_ETA_0->SetBinContent(15,0.0);
  S2_ETA_0->SetBinContent(16,0.0);
  S2_ETA_0->SetBinContent(17,0.0);
  S2_ETA_0->SetBinContent(18,0.0);
  S2_ETA_0->SetBinContent(19,0.0);
  S2_ETA_0->SetBinContent(20,0.0);
  S2_ETA_0->SetBinContent(21,0.0);
  S2_ETA_0->SetBinContent(22,0.0);
  S2_ETA_0->SetBinContent(23,0.0);
  S2_ETA_0->SetBinContent(24,0.0);
  S2_ETA_0->SetBinContent(25,0.0);
  S2_ETA_0->SetBinContent(26,0.0);
  S2_ETA_0->SetBinContent(27,0.0);
  S2_ETA_0->SetBinContent(28,0.0);
  S2_ETA_0->SetBinContent(29,0.0);
  S2_ETA_0->SetBinContent(30,0.0);
  S2_ETA_0->SetBinContent(31,0.0);
  S2_ETA_0->SetBinContent(32,0.743289664766);
  S2_ETA_0->SetBinContent(33,0.743289664766);
  S2_ETA_0->SetBinContent(34,0.743289664766);
  S2_ETA_0->SetBinContent(35,1.85822456192);
  S2_ETA_0->SetBinContent(36,1.11493449715);
  S2_ETA_0->SetBinContent(37,1.11493449715);
  S2_ETA_0->SetBinContent(38,2.2298693943);
  S2_ETA_0->SetBinContent(39,2.2298693943);
  S2_ETA_0->SetBinContent(40,3.34480389145);
  S2_ETA_0->SetBinContent(41,4.4597403886);
  S2_ETA_0->SetBinContent(42,4.4597403886);
  S2_ETA_0->SetBinContent(43,5.94631651813);
  S2_ETA_0->SetBinContent(44,4.08809235622);
  S2_ETA_0->SetBinContent(45,10.0344128743);
  S2_ETA_0->SetBinContent(46,11.5209930039);
  S2_ETA_0->SetBinContent(47,7.80454068005);
  S2_ETA_0->SetBinContent(48,8.9194767772);
  S2_ETA_0->SetBinContent(49,8.54783274481);
  S2_ETA_0->SetBinContent(50,13.7508611982);
  S2_ETA_0->SetBinContent(51,12.2642810686);
  S2_ETA_0->SetBinContent(52,18.2105975868);
  S2_ETA_0->SetBinContent(53,21.5554018782);
  S2_ETA_0->SetBinContent(54,19.6971777163);
  S2_ETA_0->SetBinContent(55,27.5017223964);
  S2_ETA_0->SetBinContent(56,33.0763948821);
  S2_ETA_0->SetBinContent(57,41.9958836593);
  S2_ETA_0->SetBinContent(58,47.1988841127);
  S2_ETA_0->SetBinContent(59,46.4556040479);
  S2_ETA_0->SetBinContent(60,60.9497653109);
  S2_ETA_0->SetBinContent(61,57.233324987);
  S2_ETA_0->SetBinContent(62,68.0110059261);
  S2_ETA_0->SetBinContent(63,71.3558062176);
  S2_ETA_0->SetBinContent(64,80.2752869948);
  S2_ETA_0->SetBinContent(65,83.9917273186);
  S2_ETA_0->SetBinContent(66,82.1335271567);
  S2_ETA_0->SetBinContent(67,95.1410882901);
  S2_ETA_0->SetBinContent(68,83.6200872862);
  S2_ETA_0->SetBinContent(69,93.6545281606);
  S2_ETA_0->SetBinContent(70,105.547129197);
  S2_ETA_0->SetBinContent(71,86.2216075129);
  S2_ETA_0->SetBinContent(72,85.1066874158);
  S2_ETA_0->SetBinContent(73,83.6200872862);
  S2_ETA_0->SetBinContent(74,75.0722865414);
  S2_ETA_0->SetBinContent(75,73.2140463795);
  S2_ETA_0->SetBinContent(76,50.9153644365);
  S2_ETA_0->SetBinContent(77,45.7123239831);
  S2_ETA_0->SetBinContent(78,47.5705641451);
  S2_ETA_0->SetBinContent(79,40.1376434974);
  S2_ETA_0->SetBinContent(80,28.9883025259);
  S2_ETA_0->SetBinContent(81,35.3062630764);
  S2_ETA_0->SetBinContent(82,35.3062630764);
  S2_ETA_0->SetBinContent(83,44.2257238536);
  S2_ETA_0->SetBinContent(84,52.401924566);
  S2_ETA_0->SetBinContent(85,58.7198851166);
  S2_ETA_0->SetBinContent(86,72.4707663147);
  S2_ETA_0->SetBinContent(87,72.0991262823);
  S2_ETA_0->SetBinContent(88,83.9917273186);
  S2_ETA_0->SetBinContent(89,83.9917273186);
  S2_ETA_0->SetBinContent(90,98.4858885816);
  S2_ETA_0->SetBinContent(91,87.7082076424);
  S2_ETA_0->SetBinContent(92,92.5395680634);
  S2_ETA_0->SetBinContent(93,95.8843683549);
  S2_ETA_0->SetBinContent(94,78.4170868329);
  S2_ETA_0->SetBinContent(95,83.6200872862);
  S2_ETA_0->SetBinContent(96,88.4514877072);
  S2_ETA_0->SetBinContent(97,83.2484472538);
  S2_ETA_0->SetBinContent(98,65.0378456671);
  S2_ETA_0->SetBinContent(99,61.6930453756);
  S2_ETA_0->SetBinContent(100,60.5781252785);
  S2_ETA_0->SetBinContent(101,56.1183648899);
  S2_ETA_0->SetBinContent(102,43.8540838212);
  S2_ETA_0->SetBinContent(103,47.5705641451);
  S2_ETA_0->SetBinContent(104,37.5361352707);
  S2_ETA_0->SetBinContent(105,34.5629750116);
  S2_ETA_0->SetBinContent(106,30.103234623);
  S2_ETA_0->SetBinContent(107,26.0151422668);
  S2_ETA_0->SetBinContent(108,18.5822456192);
  S2_ETA_0->SetBinContent(109,21.1837578458);
  S2_ETA_0->SetBinContent(110,15.9807293925);
  S2_ETA_0->SetBinContent(111,12.635925101);
  S2_ETA_0->SetBinContent(112,8.54783274481);
  S2_ETA_0->SetBinContent(113,10.4060569067);
  S2_ETA_0->SetBinContent(114,6.6896085829);
  S2_ETA_0->SetBinContent(115,9.29112080958);
  S2_ETA_0->SetBinContent(116,9.66276884196);
  S2_ETA_0->SetBinContent(117,5.57467248575);
  S2_ETA_0->SetBinContent(118,3.71644872383);
  S2_ETA_0->SetBinContent(119,3.71644872383);
  S2_ETA_0->SetBinContent(120,4.4597403886);
  S2_ETA_0->SetBinContent(121,1.85822456192);
  S2_ETA_0->SetBinContent(122,4.08809235622);
  S2_ETA_0->SetBinContent(123,2.97315905907);
  S2_ETA_0->SetBinContent(124,1.11493449715);
  S2_ETA_0->SetBinContent(125,2.2298693943);
  S2_ETA_0->SetBinContent(126,0.743289664766);
  S2_ETA_0->SetBinContent(127,1.48657972953);
  S2_ETA_0->SetBinContent(128,0.371644872383);
  S2_ETA_0->SetBinContent(129,0.371644872383);
  S2_ETA_0->SetBinContent(130,0.371644872383);
  S2_ETA_0->SetBinContent(131,0.0);
  S2_ETA_0->SetBinContent(132,0.0);
  S2_ETA_0->SetBinContent(133,0.0);
  S2_ETA_0->SetBinContent(134,0.0);
  S2_ETA_0->SetBinContent(135,0.0);
  S2_ETA_0->SetBinContent(136,0.0);
  S2_ETA_0->SetBinContent(137,0.0);
  S2_ETA_0->SetBinContent(138,0.0);
  S2_ETA_0->SetBinContent(139,0.0);
  S2_ETA_0->SetBinContent(140,0.0);
  S2_ETA_0->SetBinContent(141,0.0);
  S2_ETA_0->SetBinContent(142,0.0);
  S2_ETA_0->SetBinContent(143,0.0);
  S2_ETA_0->SetBinContent(144,0.0);
  S2_ETA_0->SetBinContent(145,0.0);
  S2_ETA_0->SetBinContent(146,0.0);
  S2_ETA_0->SetBinContent(147,0.0);
  S2_ETA_0->SetBinContent(148,0.0);
  S2_ETA_0->SetBinContent(149,0.0);
  S2_ETA_0->SetBinContent(150,0.0);
  S2_ETA_0->SetBinContent(151,0.0);
  S2_ETA_0->SetBinContent(152,0.0);
  S2_ETA_0->SetBinContent(153,0.0);
  S2_ETA_0->SetBinContent(154,0.0);
  S2_ETA_0->SetBinContent(155,0.0);
  S2_ETA_0->SetBinContent(156,0.0);
  S2_ETA_0->SetBinContent(157,0.0);
  S2_ETA_0->SetBinContent(158,0.0);
  S2_ETA_0->SetBinContent(159,0.0);
  S2_ETA_0->SetBinContent(160,0.0);
  S2_ETA_0->SetBinContent(161,0.0); // overflow
  S2_ETA_0->SetEntries(9999);
  // Style
  S2_ETA_0->SetLineColor(9);
  S2_ETA_0->SetLineStyle(1);
  S2_ETA_0->SetLineWidth(1);
  S2_ETA_0->SetFillColor(9);
  S2_ETA_0->SetFillStyle(1001);

  // Creating a new THStack
  THStack* stack = new THStack("mystack_4","mystack");
  stack->Add(S2_ETA_0);
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
  stack->GetXaxis()->SetTitle("#eta [ j_{1} ] ");

  // Finalizing the TCanvas
  canvas->SetLogx(0);
  canvas->SetLogy(0);

  // Saving the image
  canvas->SaveAs("../../HTML/MadAnalysis5job_0/selection_1.png");
  canvas->SaveAs("../../PDF/MadAnalysis5job_0/selection_1.png");
  canvas->SaveAs("../../DVI/MadAnalysis5job_0/selection_1.eps");

}
