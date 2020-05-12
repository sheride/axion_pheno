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
  S8_M_0->SetBinContent(2,0.0);
  S8_M_0->SetBinContent(3,0.0);
  S8_M_0->SetBinContent(4,0.0);
  S8_M_0->SetBinContent(5,0.0);
  S8_M_0->SetBinContent(6,0.74328965567);
  S8_M_0->SetBinContent(7,1.1149344835);
  S8_M_0->SetBinContent(8,3.34480385051);
  S8_M_0->SetBinContent(9,4.08809230618);
  S8_M_0->SetBinContent(10,2.60151419484);
  S8_M_0->SetBinContent(11,4.08809230618);
  S8_M_0->SetBinContent(12,9.6627687237);
  S8_M_0->SetBinContent(13,6.31796447319);
  S8_M_0->SetBinContent(14,8.5478326402);
  S8_M_0->SetBinContent(15,10.4060567794);
  S8_M_0->SetBinContent(16,13.7508610299);
  S8_M_0->SetBinContent(17,15.2374411412);
  S8_M_0->SetBinContent(18,20.4404695309);
  S8_M_0->SetBinContent(19,17.8389533361);
  S8_M_0->SetBinContent(20,21.5554016144);
  S8_M_0->SetBinContent(21,20.8121135587);
  S8_M_0->SetBinContent(22,26.0151419484);
  S8_M_0->SetBinContent(23,18.2105973639);
  S8_M_0->SetBinContent(24,25.6434979206);
  S8_M_0->SetBinContent(25,24.1569178093);
  S8_M_0->SetBinContent(26,24.5285618371);
  S8_M_0->SetBinContent(27,31.2181703381);
  S8_M_0->SetBinContent(28,30.8465263103);
  S8_M_0->SetBinContent(29,34.9346186165);
  S8_M_0->SetBinContent(30,32.3331064216);
  S8_M_0->SetBinContent(31,33.4480385051);
  S8_M_0->SetBinContent(32,32.3331064216);
  S8_M_0->SetBinContent(33,30.4748822825);
  S8_M_0->SetBinContent(34,36.4211987278);
  S8_M_0->SetBinContent(35,37.9077788391);
  S8_M_0->SetBinContent(36,40.8809230618);
  S8_M_0->SetBinContent(37,37.1644867835);
  S8_M_0->SetBinContent(38,36.7928427556);
  S8_M_0->SetBinContent(39,41.9958831453);
  S8_M_0->SetBinContent(40,38.6510668948);
  S8_M_0->SetBinContent(41,38.279422867);
  S8_M_0->SetBinContent(42,44.5974033402);
  S8_M_0->SetBinContent(43,40.1376430062);
  S8_M_0->SetBinContent(44,47.9422035907);
  S8_M_0->SetBinContent(45,38.6510668948);
  S8_M_0->SetBinContent(46,43.4824432567);
  S8_M_0->SetBinContent(47,40.8809230618);
  S8_M_0->SetBinContent(48,40.509283034);
  S8_M_0->SetBinContent(49,40.1376430062);
  S8_M_0->SetBinContent(50,37.1644867835);
  S8_M_0->SetBinContent(51,39.3943589505);
  S8_M_0->SetBinContent(52,42.3675231732);
  S8_M_0->SetBinContent(53,44.5974033402);
  S8_M_0->SetBinContent(54,44.5974033402);
  S8_M_0->SetBinContent(55,38.279422867);
  S8_M_0->SetBinContent(56,40.8809230618);
  S8_M_0->SetBinContent(57,43.8540832845);
  S8_M_0->SetBinContent(58,44.2257233123);
  S8_M_0->SetBinContent(59,36.4211987278);
  S8_M_0->SetBinContent(60,40.509283034);
  S8_M_0->SetBinContent(61,41.6242431175);
  S8_M_0->SetBinContent(62,41.6242431175);
  S8_M_0->SetBinContent(63,34.9346186165);
  S8_M_0->SetBinContent(64,35.3062626443);
  S8_M_0->SetBinContent(65,36.4211987278);
  S8_M_0->SetBinContent(66,36.0495547);
  S8_M_0->SetBinContent(67,37.9077788391);
  S8_M_0->SetBinContent(68,37.9077788391);
  S8_M_0->SetBinContent(69,40.509283034);
  S8_M_0->SetBinContent(70,33.819682533);
  S8_M_0->SetBinContent(71,35.6779106721);
  S8_M_0->SetBinContent(72,35.6779106721);
  S8_M_0->SetBinContent(73,35.6779106721);
  S8_M_0->SetBinContent(74,31.9614583938);
  S8_M_0->SetBinContent(75,31.2181703381);
  S8_M_0->SetBinContent(76,33.819682533);
  S8_M_0->SetBinContent(77,33.4480385051);
  S8_M_0->SetBinContent(78,34.5629745886);
  S8_M_0->SetBinContent(79,39.3943589505);
  S8_M_0->SetBinContent(80,31.9614583938);
  S8_M_0->SetBinContent(81,36.4211987278);
  S8_M_0->SetBinContent(82,28.9883021711);
  S8_M_0->SetBinContent(83,28.9883021711);
  S8_M_0->SetBinContent(84,26.3867859763);
  S8_M_0->SetBinContent(85,29.7315902268);
  S8_M_0->SetBinContent(86,29.7315902268);
  S8_M_0->SetBinContent(87,28.6166541433);
  S8_M_0->SetBinContent(88,38.6510668948);
  S8_M_0->SetBinContent(89,23.0419817258);
  S8_M_0->SetBinContent(90,20.4404695309);
  S8_M_0->SetBinContent(91,28.2450101154);
  S8_M_0->SetBinContent(92,28.9883021711);
  S8_M_0->SetBinContent(93,26.0151419484);
  S8_M_0->SetBinContent(94,19.3255334474);
  S8_M_0->SetBinContent(95,30.8465263103);
  S8_M_0->SetBinContent(96,21.5554016144);
  S8_M_0->SetBinContent(97,27.8733660876);
  S8_M_0->SetBinContent(98,23.0419817258);
  S8_M_0->SetBinContent(99,20.4404695309);
  S8_M_0->SetBinContent(100,23.0419817258);
  S8_M_0->SetBinContent(101,31.2181703381);
  S8_M_0->SetBinContent(102,20.8121135587);
  S8_M_0->SetBinContent(103,23.0419817258);
  S8_M_0->SetBinContent(104,16.7240212526);
  S8_M_0->SetBinContent(105,18.9538894196);
  S8_M_0->SetBinContent(106,21.1837575866);
  S8_M_0->SetBinContent(107,19.3255334474);
  S8_M_0->SetBinContent(108,19.3255334474);
  S8_M_0->SetBinContent(109,17.8389533361);
  S8_M_0->SetBinContent(110,17.0956652804);
  S8_M_0->SetBinContent(111,12.6359249464);
  S8_M_0->SetBinContent(112,15.6090851691);
  S8_M_0->SetBinContent(113,19.3255334474);
  S8_M_0->SetBinContent(114,17.0956652804);
  S8_M_0->SetBinContent(115,18.5822453917);
  S8_M_0->SetBinContent(116,18.5822453917);
  S8_M_0->SetBinContent(117,13.0075689742);
  S8_M_0->SetBinContent(118,11.5209928629);
  S8_M_0->SetBinContent(119,14.1225050577);
  S8_M_0->SetBinContent(120,12.6359249464);
  S8_M_0->SetBinContent(121,11.5209928629);
  S8_M_0->SetBinContent(122,14.8657971134);
  S8_M_0->SetBinContent(123,13.7508610299);
  S8_M_0->SetBinContent(124,9.6627687237);
  S8_M_0->SetBinContent(125,12.6359249464);
  S8_M_0->SetBinContent(126,9.29112069587);
  S8_M_0->SetBinContent(127,11.149344835);
  S8_M_0->SetBinContent(128,10.0344127515);
  S8_M_0->SetBinContent(129,11.5209928629);
  S8_M_0->SetBinContent(130,9.29112069587);
  S8_M_0->SetBinContent(131,6.31796447319);
  S8_M_0->SetBinContent(132,11.149344835);
  S8_M_0->SetBinContent(133,8.91947666803);
  S8_M_0->SetBinContent(134,13.0075689742);
  S8_M_0->SetBinContent(135,8.5478326402);
  S8_M_0->SetBinContent(136,11.5209928629);
  S8_M_0->SetBinContent(137,10.4060567794);
  S8_M_0->SetBinContent(138,7.80454058453);
  S8_M_0->SetBinContent(139,11.149344835);
  S8_M_0->SetBinContent(140,7.80454058453);
  S8_M_0->SetBinContent(141,5.57467241752);
  S8_M_0->SetBinContent(142,7.06125252886);
  S8_M_0->SetBinContent(143,6.31796447319);
  S8_M_0->SetBinContent(144,10.4060567794);
  S8_M_0->SetBinContent(145,7.80454058453);
  S8_M_0->SetBinContent(146,7.4328965567);
  S8_M_0->SetBinContent(147,4.45974033402);
  S8_M_0->SetBinContent(148,5.57467241752);
  S8_M_0->SetBinContent(149,7.06125252886);
  S8_M_0->SetBinContent(150,8.17618861237);
  S8_M_0->SetBinContent(151,6.68960850103);
  S8_M_0->SetBinContent(152,7.06125252886);
  S8_M_0->SetBinContent(153,5.94631644536);
  S8_M_0->SetBinContent(154,5.94631644536);
  S8_M_0->SetBinContent(155,5.57467241752);
  S8_M_0->SetBinContent(156,3.71644867835);
  S8_M_0->SetBinContent(157,7.80454058453);
  S8_M_0->SetBinContent(158,7.06125252886);
  S8_M_0->SetBinContent(159,5.94631644536);
  S8_M_0->SetBinContent(160,2.97315902268);
  S8_M_0->SetBinContent(161,157.205771774); // overflow
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
