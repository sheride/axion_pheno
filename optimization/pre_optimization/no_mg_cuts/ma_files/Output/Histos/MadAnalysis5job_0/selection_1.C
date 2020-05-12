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
  S2_ETA_0->SetBinContent(32,0.0);
  S2_ETA_0->SetBinContent(33,0.0);
  S2_ETA_0->SetBinContent(34,0.0);
  S2_ETA_0->SetBinContent(35,0.0);
  S2_ETA_0->SetBinContent(36,0.0);
  S2_ETA_0->SetBinContent(37,0.0);
  S2_ETA_0->SetBinContent(38,9.43206062514);
  S2_ETA_0->SetBinContent(39,0.0);
  S2_ETA_0->SetBinContent(40,0.0);
  S2_ETA_0->SetBinContent(41,0.0);
  S2_ETA_0->SetBinContent(42,6.28804041676);
  S2_ETA_0->SetBinContent(43,6.28804041676);
  S2_ETA_0->SetBinContent(44,0.0);
  S2_ETA_0->SetBinContent(45,15.7200970419);
  S2_ETA_0->SetBinContent(46,6.28804041676);
  S2_ETA_0->SetBinContent(47,15.7200970419);
  S2_ETA_0->SetBinContent(48,6.28804041676);
  S2_ETA_0->SetBinContent(49,18.8641172503);
  S2_ETA_0->SetBinContent(50,15.7200970419);
  S2_ETA_0->SetBinContent(51,34.5842142922);
  S2_ETA_0->SetBinContent(52,22.0081374587);
  S2_ETA_0->SetBinContent(53,40.872242709);
  S2_ETA_0->SetBinContent(54,37.7282345006);
  S2_ETA_0->SetBinContent(55,31.4401940838);
  S2_ETA_0->SetBinContent(56,34.5842142922);
  S2_ETA_0->SetBinContent(57,88.0325658347);
  S2_ETA_0->SetBinContent(58,81.7445254179);
  S2_ETA_0->SetBinContent(59,122.616768127);
  S2_ETA_0->SetBinContent(60,141.480889377);
  S2_ETA_0->SetBinContent(61,128.904808544);
  S2_ETA_0->SetBinContent(62,191.785212711);
  S2_ETA_0->SetBinContent(63,191.785212711);
  S2_ETA_0->SetBinContent(64,213.79333417);
  S2_ETA_0->SetBinContent(65,251.52157667);
  S2_ETA_0->SetBinContent(66,358.418223755);
  S2_ETA_0->SetBinContent(67,427.58682834);
  S2_ETA_0->SetBinContent(68,389.858425839);
  S2_ETA_0->SetBinContent(69,625.660041468);
  S2_ETA_0->SetBinContent(70,679.10804501);
  S2_ETA_0->SetBinContent(71,767.140850845);
  S2_ETA_0->SetBinContent(72,889.757658972);
  S2_ETA_0->SetBinContent(73,984.078065223);
  S2_ETA_0->SetBinContent(74,987.222065432);
  S2_ETA_0->SetBinContent(75,1116.12687398);
  S2_ETA_0->SetBinContent(76,1270.18408419);
  S2_ETA_0->SetBinContent(77,1279.61608481);
  S2_ETA_0->SetBinContent(78,1314.2000871);
  S2_ETA_0->SetBinContent(79,1311.05608689);
  S2_ETA_0->SetBinContent(80,1292.19208564);
  S2_ETA_0->SetBinContent(81,1465.11329711);
  S2_ETA_0->SetBinContent(82,1383.36849169);
  S2_ETA_0->SetBinContent(83,1301.62408627);
  S2_ETA_0->SetBinContent(84,1320.48808752);
  S2_ETA_0->SetBinContent(85,1298.48008606);
  S2_ETA_0->SetBinContent(86,1144.42327585);
  S2_ETA_0->SetBinContent(87,1075.25487127);
  S2_ETA_0->SetBinContent(88,933.773661889);
  S2_ETA_0->SetBinContent(89,836.309255429);
  S2_ETA_0->SetBinContent(90,745.132449386);
  S2_ETA_0->SetBinContent(91,735.700448761);
  S2_ETA_0->SetBinContent(92,635.092042093);
  S2_ETA_0->SetBinContent(93,474.746831465);
  S2_ETA_0->SetBinContent(94,430.730828548);
  S2_ETA_0->SetBinContent(95,364.706264172);
  S2_ETA_0->SetBinContent(96,292.393819379);
  S2_ETA_0->SetBinContent(97,220.081374587);
  S2_ETA_0->SetBinContent(98,235.801455629);
  S2_ETA_0->SetBinContent(99,176.065091669);
  S2_ETA_0->SetBinContent(100,157.200970419);
  S2_ETA_0->SetBinContent(101,128.904808544);
  S2_ETA_0->SetBinContent(102,100.608606668);
  S2_ETA_0->SetBinContent(103,75.4564850011);
  S2_ETA_0->SetBinContent(104,69.1684445844);
  S2_ETA_0->SetBinContent(105,84.8885256263);
  S2_ETA_0->SetBinContent(106,59.7363639592);
  S2_ETA_0->SetBinContent(107,56.5923637509);
  S2_ETA_0->SetBinContent(108,22.0081374587);
  S2_ETA_0->SetBinContent(109,40.872242709);
  S2_ETA_0->SetBinContent(110,22.0081374587);
  S2_ETA_0->SetBinContent(111,18.8641172503);
  S2_ETA_0->SetBinContent(112,25.152157667);
  S2_ETA_0->SetBinContent(113,9.43206062514);
  S2_ETA_0->SetBinContent(114,18.8641172503);
  S2_ETA_0->SetBinContent(115,18.8641172503);
  S2_ETA_0->SetBinContent(116,6.28804041676);
  S2_ETA_0->SetBinContent(117,12.5760768335);
  S2_ETA_0->SetBinContent(118,6.28804041676);
  S2_ETA_0->SetBinContent(119,3.14401940838);
  S2_ETA_0->SetBinContent(120,9.43206062514);
  S2_ETA_0->SetBinContent(121,6.28804041676);
  S2_ETA_0->SetBinContent(122,3.14401940838);
  S2_ETA_0->SetBinContent(123,0.0);
  S2_ETA_0->SetBinContent(124,0.0);
  S2_ETA_0->SetBinContent(125,0.0);
  S2_ETA_0->SetBinContent(126,3.14401940838);
  S2_ETA_0->SetBinContent(127,0.0);
  S2_ETA_0->SetBinContent(128,0.0);
  S2_ETA_0->SetBinContent(129,3.14401940838);
  S2_ETA_0->SetBinContent(130,0.0);
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
