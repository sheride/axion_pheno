void selection_4()
{

  // ROOT version
  Int_t root_version = gROOT->GetVersionInt();

  // Creating a new TCanvas
  TCanvas* canvas = new TCanvas("canvas_plotflow_tempo9","canvas_plotflow_tempo9",0,0,700,500);
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
  TH1F* S5_ETA_0 = new TH1F("S5_ETA_0","S5_ETA_0",160,-8.0,8.0);
  // Content
  S5_ETA_0->SetBinContent(0,0.0); // underflow
  S5_ETA_0->SetBinContent(1,0.0);
  S5_ETA_0->SetBinContent(2,0.0);
  S5_ETA_0->SetBinContent(3,0.0);
  S5_ETA_0->SetBinContent(4,0.0);
  S5_ETA_0->SetBinContent(5,0.0);
  S5_ETA_0->SetBinContent(6,0.0);
  S5_ETA_0->SetBinContent(7,0.0);
  S5_ETA_0->SetBinContent(8,0.0);
  S5_ETA_0->SetBinContent(9,0.0);
  S5_ETA_0->SetBinContent(10,0.0);
  S5_ETA_0->SetBinContent(11,0.0);
  S5_ETA_0->SetBinContent(12,0.0);
  S5_ETA_0->SetBinContent(13,0.0);
  S5_ETA_0->SetBinContent(14,0.0);
  S5_ETA_0->SetBinContent(15,0.0);
  S5_ETA_0->SetBinContent(16,0.0);
  S5_ETA_0->SetBinContent(17,0.0);
  S5_ETA_0->SetBinContent(18,0.0);
  S5_ETA_0->SetBinContent(19,0.0);
  S5_ETA_0->SetBinContent(20,0.0);
  S5_ETA_0->SetBinContent(21,0.0);
  S5_ETA_0->SetBinContent(22,0.0);
  S5_ETA_0->SetBinContent(23,0.0);
  S5_ETA_0->SetBinContent(24,0.0);
  S5_ETA_0->SetBinContent(25,0.0);
  S5_ETA_0->SetBinContent(26,0.0);
  S5_ETA_0->SetBinContent(27,0.0);
  S5_ETA_0->SetBinContent(28,0.0);
  S5_ETA_0->SetBinContent(29,0.0);
  S5_ETA_0->SetBinContent(30,0.0);
  S5_ETA_0->SetBinContent(31,6.68960853847);
  S5_ETA_0->SetBinContent(32,2.97315903932);
  S5_ETA_0->SetBinContent(33,6.68960853847);
  S5_ETA_0->SetBinContent(34,5.94631647864);
  S5_ETA_0->SetBinContent(35,4.83138438889);
  S5_ETA_0->SetBinContent(36,8.91947671796);
  S5_ETA_0->SetBinContent(37,10.4060568376);
  S5_ETA_0->SetBinContent(38,11.8926369573);
  S5_ETA_0->SetBinContent(39,11.5209929274);
  S5_ETA_0->SetBinContent(40,10.0344128077);
  S5_ETA_0->SetBinContent(41,12.2642809872);
  S5_ETA_0->SetBinContent(42,17.8389534359);
  S5_ETA_0->SetBinContent(43,20.4404696453);
  S5_ETA_0->SetBinContent(44,19.6971775855);
  S5_ETA_0->SetBinContent(45,24.9002060043);
  S5_ETA_0->SetBinContent(46,28.6166543035);
  S5_ETA_0->SetBinContent(47,28.9883023334);
  S5_ETA_0->SetBinContent(48,36.0495549018);
  S5_ETA_0->SetBinContent(49,41.2525633206);
  S5_ETA_0->SetBinContent(50,46.8272437693);
  S5_ETA_0->SetBinContent(51,46.0839637095);
  S5_ETA_0->SetBinContent(52,44.2257235599);
  S5_ETA_0->SetBinContent(53,48.6854839189);
  S5_ETA_0->SetBinContent(54,69.869245624);
  S5_ETA_0->SetBinContent(55,66.8960853847);
  S5_ETA_0->SetBinContent(56,74.328965983);
  S5_ETA_0->SetBinContent(57,70.2408856539);
  S5_ETA_0->SetBinContent(58,81.3902465514);
  S5_ETA_0->SetBinContent(59,82.1335266112);
  S5_ETA_0->SetBinContent(60,91.0530073292);
  S5_ETA_0->SetBinContent(61,91.796287389);
  S5_ETA_0->SetBinContent(62,83.248446701);
  S5_ETA_0->SetBinContent(63,76.1872061326);
  S5_ETA_0->SetBinContent(64,76.5588461625);
  S5_ETA_0->SetBinContent(65,78.4170863121);
  S5_ETA_0->SetBinContent(66,70.6125256838);
  S5_ETA_0->SetBinContent(67,67.6393654445);
  S5_ETA_0->SetBinContent(68,47.1988837992);
  S5_ETA_0->SetBinContent(69,42.7391634402);
  S5_ETA_0->SetBinContent(70,36.7928429616);
  S5_ETA_0->SetBinContent(71,33.0763946624);
  S5_ETA_0->SetBinContent(72,26.7584301539);
  S5_ETA_0->SetBinContent(73,22.6703378248);
  S5_ETA_0->SetBinContent(74,18.5822454957);
  S5_ETA_0->SetBinContent(75,17.0956653761);
  S5_ETA_0->SetBinContent(76,10.0344128077);
  S5_ETA_0->SetBinContent(77,10.7777008675);
  S5_ETA_0->SetBinContent(78,5.57467244872);
  S5_ETA_0->SetBinContent(79,5.94631647864);
  S5_ETA_0->SetBinContent(80,2.6015142094);
  S5_ETA_0->SetBinContent(81,3.34480386923);
  S5_ETA_0->SetBinContent(82,5.57467244872);
  S5_ETA_0->SetBinContent(83,8.17618865813);
  S5_ETA_0->SetBinContent(84,6.68960853847);
  S5_ETA_0->SetBinContent(85,14.1225051368);
  S5_ETA_0->SetBinContent(86,11.5209929274);
  S5_ETA_0->SetBinContent(87,18.9538895257);
  S5_ETA_0->SetBinContent(88,17.0956653761);
  S5_ETA_0->SetBinContent(89,27.1300781838);
  S5_ETA_0->SetBinContent(90,27.8733662436);
  S5_ETA_0->SetBinContent(91,39.394359171);
  S5_ETA_0->SetBinContent(92,42.3675234103);
  S5_ETA_0->SetBinContent(93,61.6930449659);
  S5_ETA_0->SetBinContent(94,62.4363250257);
  S5_ETA_0->SetBinContent(95,68.7542855343);
  S5_ETA_0->SetBinContent(96,73.5856859232);
  S5_ETA_0->SetBinContent(97,74.328965983);
  S5_ETA_0->SetBinContent(98,81.7618865813);
  S5_ETA_0->SetBinContent(99,81.0185665215);
  S5_ETA_0->SetBinContent(100,86.2216069403);
  S5_ETA_0->SetBinContent(101,83.6200867309);
  S5_ETA_0->SetBinContent(102,86.2216069403);
  S5_ETA_0->SetBinContent(103,91.0530073292);
  S5_ETA_0->SetBinContent(104,84.3634067907);
  S5_ETA_0->SetBinContent(105,76.5588461625);
  S5_ETA_0->SetBinContent(106,64.6662052052);
  S5_ETA_0->SetBinContent(107,66.8960853847);
  S5_ETA_0->SetBinContent(108,62.8080050556);
  S5_ETA_0->SetBinContent(109,52.0302841881);
  S5_ETA_0->SetBinContent(110,59.0915247565);
  S5_ETA_0->SetBinContent(111,39.7660032009);
  S5_ETA_0->SetBinContent(112,34.5629747821);
  S5_ETA_0->SetBinContent(113,32.7047506325);
  S5_ETA_0->SetBinContent(114,29.3599463633);
  S5_ETA_0->SetBinContent(115,31.9614585727);
  S5_ETA_0->SetBinContent(116,18.9538895257);
  S5_ETA_0->SetBinContent(117,15.6090852564);
  S5_ETA_0->SetBinContent(118,15.9807292863);
  S5_ETA_0->SetBinContent(119,20.0688256154);
  S5_ETA_0->SetBinContent(120,10.0344128077);
  S5_ETA_0->SetBinContent(121,11.1493448974);
  S5_ETA_0->SetBinContent(122,13.007569047);
  S5_ETA_0->SetBinContent(123,8.54783268804);
  S5_ETA_0->SetBinContent(124,8.91947671796);
  S5_ETA_0->SetBinContent(125,8.17618865813);
  S5_ETA_0->SetBinContent(126,4.45974035898);
  S5_ETA_0->SetBinContent(127,5.57467244872);
  S5_ETA_0->SetBinContent(128,4.08809232906);
  S5_ETA_0->SetBinContent(129,3.34480386923);
  S5_ETA_0->SetBinContent(130,4.45974035898);
  S5_ETA_0->SetBinContent(131,0.0);
  S5_ETA_0->SetBinContent(132,0.0);
  S5_ETA_0->SetBinContent(133,0.0);
  S5_ETA_0->SetBinContent(134,0.0);
  S5_ETA_0->SetBinContent(135,0.0);
  S5_ETA_0->SetBinContent(136,0.0);
  S5_ETA_0->SetBinContent(137,0.0);
  S5_ETA_0->SetBinContent(138,0.0);
  S5_ETA_0->SetBinContent(139,0.0);
  S5_ETA_0->SetBinContent(140,0.0);
  S5_ETA_0->SetBinContent(141,0.0);
  S5_ETA_0->SetBinContent(142,0.0);
  S5_ETA_0->SetBinContent(143,0.0);
  S5_ETA_0->SetBinContent(144,0.0);
  S5_ETA_0->SetBinContent(145,0.0);
  S5_ETA_0->SetBinContent(146,0.0);
  S5_ETA_0->SetBinContent(147,0.0);
  S5_ETA_0->SetBinContent(148,0.0);
  S5_ETA_0->SetBinContent(149,0.0);
  S5_ETA_0->SetBinContent(150,0.0);
  S5_ETA_0->SetBinContent(151,0.0);
  S5_ETA_0->SetBinContent(152,0.0);
  S5_ETA_0->SetBinContent(153,0.0);
  S5_ETA_0->SetBinContent(154,0.0);
  S5_ETA_0->SetBinContent(155,0.0);
  S5_ETA_0->SetBinContent(156,0.0);
  S5_ETA_0->SetBinContent(157,0.0);
  S5_ETA_0->SetBinContent(158,0.0);
  S5_ETA_0->SetBinContent(159,0.0);
  S5_ETA_0->SetBinContent(160,0.0);
  S5_ETA_0->SetBinContent(161,0.0); // overflow
  S5_ETA_0->SetEntries(9999);
  // Style
  S5_ETA_0->SetLineColor(9);
  S5_ETA_0->SetLineStyle(1);
  S5_ETA_0->SetLineWidth(1);
  S5_ETA_0->SetFillColor(9);
  S5_ETA_0->SetFillStyle(1001);

  // Creating a new THStack
  THStack* stack = new THStack("mystack_10","mystack");
  stack->Add(S5_ETA_0);
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
  stack->GetXaxis()->SetTitle("#eta [ j_{2} ] ");

  // Finalizing the TCanvas
  canvas->SetLogx(0);
  canvas->SetLogy(0);

  // Saving the image
  canvas->SaveAs("../../HTML/MadAnalysis5job_0/selection_4.png");
  canvas->SaveAs("../../PDF/MadAnalysis5job_0/selection_4.png");
  canvas->SaveAs("../../DVI/MadAnalysis5job_0/selection_4.eps");

}
