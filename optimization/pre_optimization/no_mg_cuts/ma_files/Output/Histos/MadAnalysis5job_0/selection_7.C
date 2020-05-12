void selection_7()
{

  // ROOT version
  Int_t root_version = gROOT->GetVersionInt();

  // Creating a new TCanvas
  TCanvas* canvas = new TCanvas("canvas_plotflow_tempo15","canvas_plotflow_tempo15",0,0,700,500);
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
  TH1F* S8_M_0 = new TH1F("S8_M_0","S8_M_0",160,0.0,3000.0);
  // Content
  S8_M_0->SetBinContent(0,0.0); // underflow
  S8_M_0->SetBinContent(1,0.0);
  S8_M_0->SetBinContent(2,9.4320608078);
  S8_M_0->SetBinContent(3,44.0162837697);
  S8_M_0->SetBinContent(4,44.0162837697);
  S8_M_0->SetBinContent(5,260.953622349);
  S8_M_0->SetBinContent(6,163.489014002);
  S8_M_0->SetBinContent(7,220.081378849);
  S8_M_0->SetBinContent(8,251.521581541);
  S8_M_0->SetBinContent(9,276.673743695);
  S8_M_0->SetBinContent(10,298.68186558);
  S8_M_0->SetBinContent(11,308.113906388);
  S8_M_0->SetBinContent(12,323.834027734);
  S8_M_0->SetBinContent(13,405.578434735);
  S8_M_0->SetBinContent(14,364.706271235);
  S8_M_0->SetBinContent(15,358.418230696);
  S8_M_0->SetBinContent(16,418.154435812);
  S8_M_0->SetBinContent(17,440.162837697);
  S8_M_0->SetBinContent(18,383.570392851);
  S8_M_0->SetBinContent(19,389.858433389);
  S8_M_0->SetBinContent(20,443.306837967);
  S8_M_0->SetBinContent(21,377.282352312);
  S8_M_0->SetBinContent(22,455.882839044);
  S8_M_0->SetBinContent(23,430.73083689);
  S8_M_0->SetBinContent(24,477.890840929);
  S8_M_0->SetBinContent(25,459.026839313);
  S8_M_0->SetBinContent(26,421.298436082);
  S8_M_0->SetBinContent(27,484.178841467);
  S8_M_0->SetBinContent(28,374.138352043);
  S8_M_0->SetBinContent(29,411.866435274);
  S8_M_0->SetBinContent(30,396.146473928);
  S8_M_0->SetBinContent(31,405.578434735);
  S8_M_0->SetBinContent(32,459.026839313);
  S8_M_0->SetBinContent(33,377.282352312);
  S8_M_0->SetBinContent(34,389.858433389);
  S8_M_0->SetBinContent(35,424.442836351);
  S8_M_0->SetBinContent(36,408.722435005);
  S8_M_0->SetBinContent(37,399.290474197);
  S8_M_0->SetBinContent(38,437.018837428);
  S8_M_0->SetBinContent(39,396.146473928);
  S8_M_0->SetBinContent(40,396.146473928);
  S8_M_0->SetBinContent(41,424.442836351);
  S8_M_0->SetBinContent(42,336.410108812);
  S8_M_0->SetBinContent(43,408.722435005);
  S8_M_0->SetBinContent(44,411.866435274);
  S8_M_0->SetBinContent(45,386.71443312);
  S8_M_0->SetBinContent(46,449.594838505);
  S8_M_0->SetBinContent(47,358.418230696);
  S8_M_0->SetBinContent(48,345.842149619);
  S8_M_0->SetBinContent(49,345.842149619);
  S8_M_0->SetBinContent(50,380.426392581);
  S8_M_0->SetBinContent(51,348.986189889);
  S8_M_0->SetBinContent(52,330.122068273);
  S8_M_0->SetBinContent(53,355.274230427);
  S8_M_0->SetBinContent(54,276.673743695);
  S8_M_0->SetBinContent(55,333.266068542);
  S8_M_0->SetBinContent(56,314.401946927);
  S8_M_0->SetBinContent(57,282.961784234);
  S8_M_0->SetBinContent(58,276.673743695);
  S8_M_0->SetBinContent(59,270.385703157);
  S8_M_0->SetBinContent(60,245.233541003);
  S8_M_0->SetBinContent(61,314.401946927);
  S8_M_0->SetBinContent(62,248.377541272);
  S8_M_0->SetBinContent(63,232.657459926);
  S8_M_0->SetBinContent(64,235.801460195);
  S8_M_0->SetBinContent(65,298.68186558);
  S8_M_0->SetBinContent(66,238.945500464);
  S8_M_0->SetBinContent(67,194.929216695);
  S8_M_0->SetBinContent(68,301.82586585);
  S8_M_0->SetBinContent(69,260.953622349);
  S8_M_0->SetBinContent(70,229.513419656);
  S8_M_0->SetBinContent(71,198.073256964);
  S8_M_0->SetBinContent(72,301.82586585);
  S8_M_0->SetBinContent(73,238.945500464);
  S8_M_0->SetBinContent(74,210.649298041);
  S8_M_0->SetBinContent(75,176.065095079);
  S8_M_0->SetBinContent(76,169.77705454);
  S8_M_0->SetBinContent(77,194.929216695);
  S8_M_0->SetBinContent(78,176.065095079);
  S8_M_0->SetBinContent(79,182.353135617);
  S8_M_0->SetBinContent(80,185.497175887);
  S8_M_0->SetBinContent(81,116.328729963);
  S8_M_0->SetBinContent(82,160.345013733);
  S8_M_0->SetBinContent(83,147.768932656);
  S8_M_0->SetBinContent(84,166.633054271);
  S8_M_0->SetBinContent(85,179.209135348);
  S8_M_0->SetBinContent(86,150.912932925);
  S8_M_0->SetBinContent(87,163.489014002);
  S8_M_0->SetBinContent(88,160.345013733);
  S8_M_0->SetBinContent(89,166.633054271);
  S8_M_0->SetBinContent(90,172.92109481);
  S8_M_0->SetBinContent(91,122.616770501);
  S8_M_0->SetBinContent(92,135.192851578);
  S8_M_0->SetBinContent(93,128.90481104);
  S8_M_0->SetBinContent(94,119.472730232);
  S8_M_0->SetBinContent(95,113.184689694);
  S8_M_0->SetBinContent(96,81.7445270009);
  S8_M_0->SetBinContent(97,97.4646083473);
  S8_M_0->SetBinContent(98,110.040689424);
  S8_M_0->SetBinContent(99,113.184689694);
  S8_M_0->SetBinContent(100,81.7445270009);
  S8_M_0->SetBinContent(101,113.184689694);
  S8_M_0->SetBinContent(102,116.328729963);
  S8_M_0->SetBinContent(103,66.0244056546);
  S8_M_0->SetBinContent(104,78.6004867317);
  S8_M_0->SetBinContent(105,103.752648886);
  S8_M_0->SetBinContent(106,81.7445270009);
  S8_M_0->SetBinContent(107,103.752648886);
  S8_M_0->SetBinContent(108,91.1765678087);
  S8_M_0->SetBinContent(109,81.7445270009);
  S8_M_0->SetBinContent(110,91.1765678087);
  S8_M_0->SetBinContent(111,94.320608078);
  S8_M_0->SetBinContent(112,91.1765678087);
  S8_M_0->SetBinContent(113,59.7363651161);
  S8_M_0->SetBinContent(114,78.6004867317);
  S8_M_0->SetBinContent(115,81.7445270009);
  S8_M_0->SetBinContent(116,56.5923648468);
  S8_M_0->SetBinContent(117,56.5923648468);
  S8_M_0->SetBinContent(118,56.5923648468);
  S8_M_0->SetBinContent(119,56.5923648468);
  S8_M_0->SetBinContent(120,69.1684459239);
  S8_M_0->SetBinContent(121,56.5923648468);
  S8_M_0->SetBinContent(122,75.4564864624);
  S8_M_0->SetBinContent(123,50.3043243083);
  S8_M_0->SetBinContent(124,50.3043243083);
  S8_M_0->SetBinContent(125,47.160284039);
  S8_M_0->SetBinContent(126,40.8722435005);
  S8_M_0->SetBinContent(127,28.2961784234);
  S8_M_0->SetBinContent(128,31.4401946927);
  S8_M_0->SetBinContent(129,37.7282352312);
  S8_M_0->SetBinContent(130,47.160284039);
  S8_M_0->SetBinContent(131,37.7282352312);
  S8_M_0->SetBinContent(132,50.3043243083);
  S8_M_0->SetBinContent(133,50.3043243083);
  S8_M_0->SetBinContent(134,47.160284039);
  S8_M_0->SetBinContent(135,37.7282352312);
  S8_M_0->SetBinContent(136,34.5842149619);
  S8_M_0->SetBinContent(137,25.1521581541);
  S8_M_0->SetBinContent(138,31.4401946927);
  S8_M_0->SetBinContent(139,28.2961784234);
  S8_M_0->SetBinContent(140,40.8722435005);
  S8_M_0->SetBinContent(141,34.5842149619);
  S8_M_0->SetBinContent(142,31.4401946927);
  S8_M_0->SetBinContent(143,34.5842149619);
  S8_M_0->SetBinContent(144,18.8641176156);
  S8_M_0->SetBinContent(145,28.2961784234);
  S8_M_0->SetBinContent(146,34.5842149619);
  S8_M_0->SetBinContent(147,37.7282352312);
  S8_M_0->SetBinContent(148,18.8641176156);
  S8_M_0->SetBinContent(149,28.2961784234);
  S8_M_0->SetBinContent(150,31.4401946927);
  S8_M_0->SetBinContent(151,25.1521581541);
  S8_M_0->SetBinContent(152,15.7200973463);
  S8_M_0->SetBinContent(153,18.8641176156);
  S8_M_0->SetBinContent(154,18.8641176156);
  S8_M_0->SetBinContent(155,31.4401946927);
  S8_M_0->SetBinContent(156,22.0081378849);
  S8_M_0->SetBinContent(157,34.5842149619);
  S8_M_0->SetBinContent(158,15.7200973463);
  S8_M_0->SetBinContent(159,12.5760770771);
  S8_M_0->SetBinContent(160,18.8641176156);
  S8_M_0->SetBinContent(161,499.899242813); // overflow
  S8_M_0->SetEntries(9999);
  // Style
  S8_M_0->SetLineColor(9);
  S8_M_0->SetLineStyle(1);
  S8_M_0->SetLineWidth(1);
  S8_M_0->SetFillColor(9);
  S8_M_0->SetFillStyle(1001);

  // Creating a new THStack
  THStack* stack = new THStack("mystack_16","mystack");
  stack->Add(S8_M_0);
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
  stack->GetXaxis()->SetTitle("M [ j_{1} , j_{2} ]   ( GeV ) ");

  // Finalizing the TCanvas
  canvas->SetLogx(0);
  canvas->SetLogy(0);

  // Saving the image
  canvas->SaveAs("../../HTML/MadAnalysis5job_0/selection_7.png");
  canvas->SaveAs("../../PDF/MadAnalysis5job_0/selection_7.png");
  canvas->SaveAs("../../DVI/MadAnalysis5job_0/selection_7.eps");

}
